# Quantum Learning Repeatability

**How does the accuracy of a nonlinear quantum training loss change the number of examples needed when inputs cannot be replayed?**

This project establishes an accuracy-dependent sample exponent for selecting among a fixed finite collection of known measurement hypotheses. Each passive example supplies a classical context, sampled uniformly from a known set of size $`M`$, and one fresh copy of its unknown conditional quantum state. The state table is fixed throughout the experiment.

For loss $`\ell_h(x)=1-\mathrm{Tr}[\Pi_h(x)\rho_x]`$ and fixed tilt $`a>0`$, minimize

```math
R_a(h)=\frac{1}{a}\log\left(\frac{1}{M}\sum_{x=1}^{M}e^{a\ell_h(x)}\right).
```

Let $`\kappa_r(a)`$ be the largest ratio between exponential moments of two distributions on $`[0,1]`$ whose first $`r`$ moments agree, and set $`\Gamma_r(a)=a^{-1}\log\kappa_r(a)`$. Equivalently, $`\kappa_r(a)`$ is the best multiplicative distortion of a degree-$`r`$ polynomial envelope of $`e^{au}`$; the scalar approximation duality is inherited and credited in the [moment account](science/moment_frontier.md).

For every fixed integer $`k\ge1`$, at accuracies strictly between adjacent thresholds,

```math
\Gamma_k(a)<\varepsilon<\Gamma_{k-1}(a)
\quad\Longrightarrow\quad
N_{\mathrm{worst}}(M)
=\Theta_{a,\varepsilon,H,\delta}\!\left(M^{1-1/k}\right).
```

Here $`H\ge2`$ is a fixed finite cap on the number of hypotheses, the failure target satisfies $`0\lt \delta\lt 1/2`$, and $`M`$ tends to infinity while the other parameters remain fixed. The upper bound holds for every such class; a particular two-hypothesis class on two-qubit outputs witnesses the worst-case lower bound. Arbitrary collective quantum measurements are allowed.

| Same-context observations that become necessary | Passive source exponent |
|---|---:|
| One | $`0`$ |
| Two | $`1/2`$ |
| Three | $`2/3`$ |
| $`k`$ | $`1-1/k`$ |

The first threshold is explicit:

```math
\Gamma_1(a)=\frac{1}{a}\log\frac{e^a-1}{a}
-\frac{1}{a}+\frac{1}{e^a-1}
=\frac{a}{8}+O(a^3).
```

At $`a=1`$, the first three thresholds are approximately $`0.12330156`$, $`0.01029531`$ and $`0.00064456`$. These values are checked numerically; the theorem uses the exact variational thresholds.

## Read the science

Start with the [scientific route](science/README.md), or go directly to the [model](science/model.md), [moment thresholds](science/moment_frontier.md), [passive sampling theorem and proof](science/passive_frontier.md), and [replay and resource account](science/replay_and_resources.md). The [interpretation](science/interpretation.md) explains what the frontier changes in quantum learning. The [related-work comparison](references/related_work.md) separates the result from established ensemble, classical moment and multi-observation methods.

## Learn the project

The [learning route](learning/README.md) starts with a concrete two-context example, connects Watrous's *The Theory of Quantum Information* (2018) to the project notation, and follows a shared map of exactly 30 milestones from the data model to the theorem and its resource limits.

## Meaning and scope

A nonlinear objective depends on within-context outcome probabilities, rather than only their mean across contexts. Better accuracy can require higher same-context occupancies. Passive sampling must wait for these coincidences; selected-input replay supplies them directly and removes the support-size factor.

The lower bound rules out bypassing this repetition cost with collective quantum processing. For fixed $`H`$, matching source exponents also admit immediate per-hypothesis measurements and classical storage of their outcomes. This is a data-access law, with a classical latent-variable core. It establishes no processing-time speedup or hardware crossover.

The theorem concerns proper selection from the supplied hypothesis class, uniform contexts, independent source draws, arbitrary fixed conditional states, fixed parameters and strict threshold gaps. It does not determine the critical accuracies $`\varepsilon=\Gamma_r(a)`$, joint precision/support limits, or nonuniform-context rates. Source preparation, classical caching, quantum storage when used, and known measurement circuits are accounted for separately.

## Reproduce the finite checks

See [verification](verification/README.md) for dependencies, exact commands, expected results and the limits of numerical validation. The analytical proofs remain authoritative.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
