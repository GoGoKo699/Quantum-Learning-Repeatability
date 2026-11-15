#!/usr/bin/env python3
"""Finite numerical checks for the repeatability moment/frontier account.

The analytic statements and quantifiers live in science/. These checks do not
constitute a formal proof, a novelty review, or a general learning experiment.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog, root
from scipy.sparse import csr_matrix


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def grid_primal_dual(a: float, r: int, points: int = 4001) -> dict:
    """Independently solve the matching-moment ratio and envelope LPs."""
    x = np.linspace(0.0, 1.0, points)
    f = np.exp(a * x)
    moments = np.stack([x**j for j in range(r + 1)])
    # Charnes--Cooper ratio primal: moments(u-v)=0 and f.v=1.
    eq = np.vstack(
        [np.c_[moments, -moments], np.r_[np.zeros(points), f]]
    )
    options = {
        "dual_feasibility_tolerance": 1e-9,
        "primal_feasibility_tolerance": 1e-9,
    }
    primal = linprog(
        np.r_[-f, np.zeros(points)],
        A_eq=csr_matrix(eq),
        b_eq=np.r_[np.zeros(r + 1), 1.0],
        bounds=(0.0, None),
        method="highs",
        options=options,
    )
    # A separately specified envelope dual, f <= P <= K f.
    inequalities = np.vstack(
        [np.c_[-moments.T, np.zeros(points)], np.c_[moments.T, -f]]
    )
    dual = linprog(
        np.r_[np.zeros(r + 1), 1.0],
        A_ub=inequalities,
        b_ub=np.r_[-f, np.zeros(points)],
        bounds=[(None, None)] * (r + 1) + [(1.0, None)],
        method="highs",
        options=options,
    )
    require(primal.success, f"Primal LP failed: {primal.message}")
    require(dual.success, f"Envelope LP failed: {dual.message}")
    gap = float(dual.fun + primal.fun)
    require(abs(gap) < 1e-7, f"Grid primal/dual gap: {gap}")
    coefficients = dual.x[:-1]
    derivative = np.r_[np.arange(1, r + 1) * coefficients[1:], 0.0]
    derivative -= a * coefficients
    stationary = np.polynomial.polynomial.polyroots(derivative)
    nodes = sorted(
        [0.0, 1.0]
        + [float(z.real) for z in stationary if abs(z.imag) < 1e-8 and 0 < z.real < 1]
    )
    return {
        "ratio_primal": float(-primal.fun),
        "ratio_dual": float(dual.fun),
        "gap": gap,
        "coefficients": coefficients,
        "stationary_nodes": nodes,
    }


def refine_envelope(a: float, r: int, grid: dict) -> dict:
    """Refine alternation contacts, then independently construct moment atoms."""
    if r == 0:
        return {
            "a": a,
            "r": r,
            "gamma": 1.0,
            "ratio": math.exp(a),
            "coefficients": [math.exp(a)],
            "nodes": [0.0, 1.0],
            "mu": [[1.0, 1.0]],
            "nu": [[0.0, 1.0]],
            "moment_residual": 0.0,
            "envelope_residual": 0.0,
            "alternation_residual": 0.0,
        }
    seed_nodes = grid["stationary_nodes"]
    require(len(seed_nodes) == r + 2, "Unexpected number of envelope contacts")
    seed = np.r_[grid["coefficients"], grid["ratio_dual"], seed_nodes[1:-1]]
    # Lower contacts support the maximizing numerator measure. Upper contacts
    # support the denominator measure. This orientation is checked below.
    high = np.array([(i + r) % 2 == 0 for i in range(r + 2)])

    def equations(v: np.ndarray) -> np.ndarray:
        c, ratio = v[: r + 1], v[r + 1]
        nodes = np.r_[0.0, v[r + 2 :], 1.0]
        targets = np.where(high, ratio, 1.0)
        contact = np.polynomial.polynomial.polyval(nodes, c) - targets * np.exp(a * nodes)
        derivative = np.r_[np.arange(1, r + 1) * c[1:], 0.0] - a * c
        return np.r_[contact, np.polynomial.polynomial.polyval(nodes[1:-1], derivative)]

    solution = root(equations, seed, tol=1e-12)
    equation_residual = float(np.linalg.norm(equations(solution.x), np.inf))
    require(equation_residual < 1e-10, "Alternation equations did not converge")
    coefficients = solution.x[: r + 1]
    ratio = float(solution.x[r + 1])
    nodes = np.r_[0.0, solution.x[r + 2 :], 1.0]
    require(np.all(np.diff(nodes) > 0), "Envelope contacts are unordered")

    sign = np.where(high, -1.0, 1.0)
    system = np.stack(
        [sign * nodes**j for j in range(r + 1)] + [(~high).astype(float)]
    )
    rhs = np.r_[np.zeros(r + 1), 1.0]
    weights = np.linalg.solve(system, rhs)
    require(np.min(weights) > 0, "Moment witness has nonpositive atoms")
    moment_residual = float(np.linalg.norm(system @ weights - rhs, np.inf))
    witness_ratio = float(
        np.dot(weights[~high], np.exp(a * nodes[~high]))
        / np.dot(weights[high], np.exp(a * nodes[high]))
    )
    require(abs(witness_ratio - ratio) < 1e-10, "Moment witness and envelope disagree")

    # All extrema of P exp(-a p) are roots of the degree-r polynomial P'-aP.
    derivative = np.r_[np.arange(1, r + 1) * coefficients[1:], 0.0] - a * coefficients
    stationary = np.polynomial.polynomial.polyroots(derivative)
    all_extrema = [0.0, 1.0] + [
        float(z.real) for z in stationary if abs(z.imag) < 1e-8 and 0 < z.real < 1
    ]
    relative_values = np.polynomial.polynomial.polyval(all_extrema, coefficients)
    relative_values *= np.exp(-a * np.array(all_extrema))
    envelope_residual = float(max(0.0, 1.0 - min(relative_values), max(relative_values) - ratio))
    require(envelope_residual < 1e-10, "Continuum envelope violation")
    require(abs(ratio - grid["ratio_primal"]) < 2e-6, "Grid and continuum values disagree")
    return {
        "a": a,
        "r": r,
        "gamma": float(math.log(ratio) / a),
        "ratio": ratio,
        "coefficients": coefficients.tolist(),
        "nodes": nodes.tolist(),
        "mu": [[float(x), float(w)] for x, w in zip(nodes[~high], weights[~high])],
        "nu": [[float(x), float(w)] for x, w in zip(nodes[high], weights[high])],
        "moment_residual": moment_residual,
        "envelope_residual": envelope_residual,
        "alternation_residual": equation_residual,
    }


def tilted_risk(prior: list[list[float]], a: float) -> float:
    return math.log(sum(w * math.exp(a * p) for p, w in prior)) / a


def coordinate_state_average(mu: list, nu: list, repeats: int) -> np.ndarray:
    """Diagonal of the annealed two-qubit state for repeated one context."""
    out = np.zeros(4**repeats)
    for p, wp in mu:
        for q, wq in nu:
            diagonal = np.array([(1 - p) * (1 - q), (1 - p) * q, p * (1 - q), p * q])
            tensor = np.ones(1)
            for _ in range(repeats):
                tensor = np.kron(tensor, diagonal)
            out += wp * wq * tensor
    return out


def moment_source_checks(row: dict) -> dict:
    a, r = row["a"], row["r"]
    mu, nu = row["mu"], row["nu"]
    residual = max(
        abs(sum(w * p**j for p, w in mu) - sum(w * p**j for p, w in nu))
        for j in range(r + 1)
    )
    risk_gap = tilted_risk(mu, a) - tilted_risk(nu, a)
    require(abs(risk_gap - row["gamma"]) < 1e-10, "Tilted risk gap is incorrect")
    distances = []
    for repeats in range(1, r + 2):
        first = coordinate_state_average(mu, nu, repeats)
        second = coordinate_state_average(nu, mu, repeats)
        require(abs(first.sum() - 1) < 1e-10 and np.min(first) > -1e-12, "Invalid density state")
        distance = float(np.abs(first - second).sum() / 2)
        if repeats <= r:
            require(distance < 1e-10, "Moment matching failed to hide a source block")
        else:
            require(distance > 1e-8, "First unmatched moment did not distinguish this witness")
        distances.append({"repeats": repeats, "half_trace_distance": distance})
    # A fixed three-context word with no (r+1)-fold context. Grouping registers
    # by context applies one common permutation to both full input states.
    pattern = {1: [0, 1, 2], 2: [0, 1, 0, 2, 1], 3: [0, 1, 0, 2, 1, 0]}.get(r)
    multicontext = None
    if pattern is not None:
        first, second = np.ones(1), np.ones(1)
        for count in Counter(pattern).values():
            first = np.kron(first, coordinate_state_average(mu, nu, count))
            second = np.kron(second, coordinate_state_average(nu, mu, count))
        distance = float(np.abs(first - second).sum() / 2)
        require(distance < 1e-10, "No-high-multiplicity context word revealed the world")
        multicontext = {"context_word": pattern, "joint_half_trace_distance": distance}
    return {"a": a, "r": r, "moment_residual": residual, "risk_gap": risk_gap, "source_distances": distances, "multicontext_check": multicontext}


def polynomial_copy_estimator_check(row: dict) -> dict:
    """Verify the degree-r envelope estimator from r Bernoulli outcomes."""
    degree = row["r"]
    coefficients = row["coefficients"]
    if degree == 0:
        return {"a": row["a"], "r": 0, "max_residual": 0.0, "range": [coefficients[0], coefficients[0]]}
    # The falling-factorial U-statistic for p^j, evaluated from the success count.
    values = []
    for count in range(degree + 1):
        value = coefficients[0]
        for j in range(1, degree + 1):
            value += coefficients[j] * math.comb(count, j) / math.comb(degree, j) if count >= j else 0.0
        values.append(value)
    residual = 0.0
    for p in np.linspace(0.0, 1.0, 101):
        expectation = sum(
            math.comb(degree, count) * p**count * (1 - p) ** (degree - count) * values[count]
            for count in range(degree + 1)
        )
        residual = max(residual, abs(expectation - np.polynomial.polynomial.polyval(p, coefficients)))
    require(residual < 1e-10, "Copy observable is not an unbiased polynomial estimator")
    return {"a": row["a"], "r": degree, "max_residual": float(residual), "range": [min(values), max(values)]}


def exact_repeat_probability(contexts: int, samples: int, multiplicity: int) -> float:
    """Exact integer occupancy count before conversion to a floating ratio."""
    counts = [0] * (samples + 1)
    counts[0] = 1
    for _ in range(contexts):
        updated = [0] * (samples + 1)
        for t in range(samples + 1):
            updated[t] = sum(
                math.comb(t, j) * counts[t - j]
                for j in range(min(multiplicity - 1, t) + 1)
            )
        counts = updated
    return 1.0 - counts[samples] / contexts**samples


def occupancy_checks() -> dict:
    tested = 0
    largest_bound_violation = 0.0
    for contexts in [2, 5, 11]:
        for multiplicity in [2, 3, 4]:
            previous = -1.0
            for samples in range(0, 14):
                probability = exact_repeat_probability(contexts, samples, multiplicity)
                bound = math.comb(samples, multiplicity) / contexts ** (multiplicity - 1) if samples >= multiplicity else 0.0
                require(probability >= previous - 1e-12, "Repeat probability is not monotone")
                require(-1e-12 <= probability <= 1 + 1e-12, "Invalid probability")
                require(probability <= bound + 1e-12, "Birthday union bound violated")
                if multiplicity == 2:
                    no_repeat = math.prod((contexts - j) / contexts for j in range(samples)) if samples <= contexts else 0.0
                    require(abs(probability - (1 - no_repeat)) < 1e-12, "Integer DP disagrees with the ordinary birthday formula")
                if samples > contexts * (multiplicity - 1):
                    require(abs(probability - 1) < 1e-12, "Pigeonhole endpoint failed")
                previous = probability
                largest_bound_violation = max(largest_bound_violation, probability - bound)
                tested += 1
    brute_force_cases = 0
    for contexts in [2, 3]:
        for samples in range(0, 7):
            for multiplicity in [2, 3, 4]:
                favorable = sum(
                    max(Counter(word).values(), default=0) >= multiplicity
                    for word in product(range(contexts), repeat=samples)
                )
                brute = favorable / contexts**samples
                require(abs(brute - exact_repeat_probability(contexts, samples, multiplicity)) < 1e-12, "Integer occupancy DP disagrees with exhaustive context words")
                brute_force_cases += 1
    examples = []
    for multiplicity in [2, 3, 4]:
        for contexts in [100, 1000]:
            samples = round(contexts ** (1 - 1 / multiplicity))
            examples.append({
                "M": contexts,
                "k": multiplicity,
                "T": samples,
                "exact_k_repeat_probability": exact_repeat_probability(contexts, samples, multiplicity),
                "fixed_c_one_poisson_limit": 1 - math.exp(-1 / math.factorial(multiplicity)),
            })
    return {"finite_cases": tested, "brute_force_cases": brute_force_cases, "largest_union_bound_violation": largest_bound_violation, "scaling_examples": examples}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    expected_path = Path(__file__).with_name("expected") / "results.json"
    expected = json.loads(expected_path.read_text())
    rows = []
    for a in [1.0, 2.0]:
        for degree in range(4):
            grid = grid_primal_dual(a, degree)
            row = refine_envelope(a, degree, grid)
            key = f"a={int(a)},r={degree}"
            require(abs(row["gamma"] - expected["gamma"][key]) < 1e-9, f"Unexpected Gamma value: {key}")
            row["grid_primal_dual_gap"] = grid["gap"]
            rows.append(row)
        first = next(v for v in rows if v["a"] == a and v["r"] == 1)
        p = 1 / a - 1 / math.expm1(a)
        specht = math.log((1 + math.expm1(a) * p) * math.exp(-a * p)) / a
        require(abs(first["gamma"] - specht) < 1e-12, "Gamma_1 is not the Specht value")
        sequence = [v["gamma"] for v in rows if v["a"] == a]
        require(all(x > y for x, y in zip(sequence, sequence[1:])), "Checked Gamma sequence is not strictly decreasing")
    result = {
        "status": "passed",
        "scope": expected["scope"],
        "moment_envelopes": rows,
        "coordinate_source_checks": [moment_source_checks(row) for row in rows],
        "copy_observable_checks": [polynomial_copy_estimator_check(row) for row in rows],
        "occupancy": occupancy_checks(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"PASS: 8 moment-envelope cases; 20 repeated-context blocks; 6 joint context words; 8 copy observables; {result['occupancy']['finite_cases']} occupancy cases; {result['occupancy']['brute_force_cases']} exhaustive cross-checks")
    print(f"Results: {args.output}")


if __name__ == "__main__":
    main()
