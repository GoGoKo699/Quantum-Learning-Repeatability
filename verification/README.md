# Finite verification

The verifier checks the numerical threshold values and finite mechanisms used by the repeatability account. It compares independently specified moment and polynomial optimization problems, constructs explicit matching-moment source states, verifies the copy observable, and counts context collisions. The analytic statements and their quantifiers remain in the scientific account.

## Run

From the repository root, using Python 3.12:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_repeatability.py
```

The dependencies are pinned to the versions used for the recorded run. The script writes [results.json](results.json) and exits with an error if a check fails. An alternate output path can be supplied with `--output PATH`.

[expected/results.json](expected/results.json) contains the fixed numerical reference values and the verification scope. The script computes the values again; it does not copy the reference values into its calculations.

## Checks

| Check | Computation | Scope |
|---|---|---|
| Moment/envelope duality | Independently solve the normalized ratio primal and polynomial-envelope dual on 4,001 points, for eight cases | (a=1,2), degrees (r=0,1,2,3); numerical agreement on the grid |
| Continuum envelope | Refine alternating contacts and inspect every real stationary point of (P(p)e^{-ap}), plus both endpoints | The eight displayed numerical cases; floating-point root calculations |
| Matching moment witnesses | Solve for positive atomic weights, compare moments through degree (r), and evaluate the tilted risk ratio | Explicit finite priors, independently checked against each envelope |
| First threshold | Compare the degree-one value with the analytic Specht expression | (a=1,2) |
| Quantum source blocks | Construct the full diagonal of each averaged two-qubit state for repeated contexts | Twenty blocks: repetitions through (r) agree; the next repetition distinguishes the selected witness |
| Several contexts | Tensor three independently assigned context blocks using explicit arrival words | Six words whose maximum multiplicity is at most (r); registers may be regrouped by a common permutation |
| Copy observable | Evaluate the falling-factorial estimator from the count of (r) independent Bernoulli outcomes | Eight envelope polynomials, tested on 101 loss probabilities each |
| Collision law | Count assignments exactly with integer dynamic programming before converting to probabilities | 126 finite cases, the union bound, monotonicity and the pigeonhole endpoint |
| Independent occupancy check | Enumerate every context word for small supports and compare with the dynamic program; also compare (k=2) with the ordinary birthday formula | 42 exhaustive cases, plus the two-fold collision cases above |

The source checks use

$$
\rho(p,q)=\operatorname{diag}(1-p,p)\otimes
\operatorname{diag}(1-q,q).
$$

One world draws the frozen coordinates independently from $\mu,\nu$; the other swaps these priors. Each averaged state is diagonal, so half the $\ell_1$ distance of its diagonal is its quantum half trace distance. This verifies an actual quantum input family, while keeping the finite calculation small. It does not restrict the learner's processing to measurements in that diagonal basis.

## Recorded thresholds

$\Gamma_r(a)$ is the logarithmic moment ambiguity divided by $a$.

| (a) | (Gamma_0) | (Gamma_1) | (Gamma_2) | (Gamma_3) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0.123301561482 | 0.010295312342 | 0.000644562136 |
| 2 | 1 | 0.237237323535 | 0.039761060549 | 0.005003925480 |

The recorded run passed all checks. Matched source-block half trace distances were below $1.3\times10^{-16}$. The refined moment and continuum-envelope residuals were below the script's $10^{-10}$ tolerance; exact values are retained in the result file. The collision calculation also records finite examples at $T\approx M^{1-1/k}$, alongside the fixed-(k) Poisson limit. Those examples illustrate the scaling and are not used to certify an asymptotic theorem.

## Limits

The calculations check selected finite statements. Floating-point optimization and root finding do not replace the proof of continuous moment duality, strict decrease of all thresholds, minimax asymptotics, or the occupancy construction for arbitrary parameters. The result file supplies no external priority certificate, general optimizer benchmark, hardware-noise guarantee, or quantum computational advantage.

The lower-bound source family concerns proper selection between the specified measurements. A statement about every finite class or arbitrary improper classifiers requires its own argument. The two coordinates above occupy two qubits; they are not independent coordinates of one diagonal qubit.
