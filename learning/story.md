# When learning accuracy requires repeated contexts

An experiment has two equally likely settings. Two candidate measurements each have mean loss $`1/2`$. The first works perfectly at one setting and always fails at the other; the second has loss probability $`1/2`$ at both settings.

| Context | Loss of $`h_1`$ | Loss of $`h_2`$ |
| --- | ---: | ---: |
| $`x=1`$ | $`0`$ | $`1/2`$ |
| $`x=2`$ | $`1`$ | $`1/2`$ |

Mean loss ties them. A criterion that puts extra weight on settings with high loss prefers $`h_2`$. This small example introduces the question: how much conditional information must a data source supply before a learner can resolve that preference at a specified accuracy?

## A complete quantum realization

Write $`\tau_u=\mathrm{diag}(1-u,u)`$ for a qubit state. Use the two-qubit source table

$$
\rho_1=\tau_0\otimes\tau_{1/2},\qquad
\rho_2=\tau_1\otimes\tau_{1/2},
$$

and the known projectors

$$
\Pi_1=\lvert0\rangle\langle0\rvert\otimes I,\qquad
\Pi_2=I\otimes\lvert0\rangle\langle0\rvert.
$$

For hypothesis $`h`$, the loss at context $`x`$ is

$$
\ell_h(x)=1-\mathrm{Tr}[\Pi_h(x)\rho_x].
$$

The state table and projectors give exactly the displayed losses. Measuring the complementary projector $`I-\Pi_h(x)`$ produces a loss bit with that probability. These notions connect to Watrous's states and measurements through [the anchor bridge](anchor.md).

For positive tilt $`a`$, define the population risk

$$
R_a(h)=\frac1a\log\left(\frac12
e^{a\ell_h(1)}+\frac12e^{a\ell_h(2)}\right).
$$

Direct substitution gives

$$
R_a(h_2)=\frac12,\qquad
R_a(h_1)=\frac12+\frac1a\log\cosh(a/2).
$$

At $`a=1`$ the gap is about $`0.12011451`$. The extra cost comes from variation between contexts, despite equal means. This example illustrates the objective; the support-size lower bound below uses many contexts and specially matched frozen-table priors.

## A probability and one observed bit are different objects

Suppose an arrival at context $`x`$ gives one state, and measuring it gives a bit $`Y`$ with mean $`\ell_h(x)`$. Exponentiating that bit yields

$$
\mathbb E[e^{aY}\mid x]
=1+(e^a-1)\ell_h(x).
$$

The target instead contains $`e^{a\ell_h(x)}`$. The first quantity is affine in the loss probability, and the second is nonlinear. Exponentiating an outcome therefore does not solve the conditional-probability estimation problem.

If the source prepares $`j`$ independent specimens at the same context, their loss bits satisfy

$$
\mathbb E[Y_1\cdots Y_j\mid x]=\ell_h(x)^j.
$$

Repeated preparations reveal higher moments. Passive data can supply such repetitions when a context reappears, but the learner cannot request them. The project asks which repeat order is actually necessary for the requested excess-risk tolerance.

## A scalar threshold measures the missing information

Let $`\mu`$ and $`\nu`$ be probability distributions of a loss value $`u\in[0,1]`$. Matching their first $`r`$ moments means

$$
\int u^j\,d\mu(u)=\int u^j\,d\nu(u)
\quad(0\le j\le r).
$$

Define

$$
\kappa_r(a)=
\max_{\mu,\nu\ \mathrm{matching\ through}\ r}
\frac{\int e^{au}\,d\mu(u)}
{\int e^{au}\,d\nu(u)},\qquad
\Gamma_r(a)=\frac1a\log\kappa_r(a).
$$

Thus $`\Gamma_r(a)`$ is the largest possible tilted-risk gap that remains compatible with those moments. An inherited approximation duality gives an equivalent envelope:

$$
\kappa_r(a)=\min\left\lbraceK:\ \exists P,\ \deg P\le r,\quad
e^{au}\le P(u)\le K e^{au}\quad(0\le u\le1)\right\rbrace.
$$

One scalar quantity controls both sides of the argument: indistinguishable moment pairs give a lower bound, and a polynomial envelope gives a learner. The local derivation and attribution are in [the moment frontier](../science/moment_frontier.md).

The thresholds satisfy $`1=\Gamma_0(a)>\Gamma_1(a)>\cdots>0`$ and tend to zero. The first value is the classical logarithmic Specht ratio,

$$
\Gamma_1(a)=\frac1a\log\frac{e^a-1}{a}
-\frac1a+\frac1{e^a-1}.
$$

It is approximately $`a/8`$ at small tilt. The two-context example does not attain this maximum for every $`a`$: the sharp value optimizes over all admissible loss distributions with the same mean.

## The accuracy–support theorem

Now let the source have a known uniform support of $`M`$ contexts and an arbitrary unknown **fixed** state $`\rho_x`$ at each context. Each draw independently supplies a uniformly random label $`x`$ and one fresh specimen of $`\rho_x`$. There are at most $`H`$ known projector hypotheses. The learner must return one of those hypotheses: this is proper selection.

Fix $`a>0`$, $`H\ge2`$, $`0\lt \delta\lt 1/2`$ and an integer $`k\ge1`$. If

$$
\Gamma_k(a)<\varepsilon<\Gamma_{k-1}(a),
$$

then the worst-case fixed-budget sample complexity for

$$
\Pr\left[
R_a(\widehat h)-\min_hR_a(h)\le\varepsilon
\right]\ge1-\delta
$$

is

$$
\mathsf N^{*}(M)
=\Theta_{a,\varepsilon,H,\delta,k}(M^{1-1/k})
\qquad(M\to\infty).
$$

The upper bound holds for every supplied class of size at most $`H`$. One particular pair of commuting projectors on two qubits witnesses the lower bound. It is not a lower bound for every class. All displayed parameters except $`M`$ are fixed; constants need not be uniform near a threshold or when other parameters grow.

At $`a=1`$, the strict tolerance intervals illustrate the staircase:

| Tolerance | Source-cost dependence |
| --- | --- |
| $`0.12330156\ldots\lt \varepsilon\lt 1`$ | $`\Theta(1)`$ |
| $`0.01029531\ldots\lt \varepsilon\lt 0.12330156\ldots`$ | $`\Theta(M^{1/2})`$ |
| $`0.00064456\ldots\lt \varepsilon\lt 0.01029531\ldots`$ | $`\Theta(M^{2/3})`$ |

Endpoint equalities are not covered. These decimal values illustrate the analytically defined thresholds; numerical grids are not the proof.

## Why collective quantum processing cannot remove the cost

For the lower bound, choose loss distributions that match through degree $`k-1`$ but have a tilted-risk gap greater than $`\varepsilon`$. Draw latent loss parameters independently at each context and freeze them. One world makes the first coordinate better; the other swaps the coordinate priors.

For a diagonal qubit $`\tau_u`$, every entry of $`\tau_u^{\otimes s}`$ is a polynomial of degree at most $`s`$ in $`u`$. Until a context occurs $`k`$ times, moment matching therefore makes the **complete prior-averaged training state** identical between the two worlds. This is stronger than saying the learner's chosen measurement has equal mean.

With $`n`$ passive draws, a union bound gives

$$
\Pr[\text{some context appears at least }k\text{ times}]
\le {n\choose k}M^{1-k}.
$$

Below the scale $`M^{1-1/k}`$, the two full input states are almost indistinguishable. Watrous's binary discrimination theorem then limits every possible final hypothesis choice, including one produced by collective measurements and adaptive processing. Concentration of the frozen-table risks makes the preferred hypotheses genuinely opposite with high prior probability. Averaging any claimed guarantee over these fixed-table priors yields a contradiction. The source is fixed after its initial draw; the construction does not redraw its hidden parameters on each visit.

## Why the same power is sufficient

For one hypothesis at a time, measure every arriving specimen immediately and cache its context and loss bit. A batch of order $`M^{1-1/k}`$ draws contains a $`k`$-fold repeat with probability bounded away from zero. Select a repeated context using only its labels, symmetrically across labels, and retain its first $`k`$ outcomes.

Uniform context sampling makes the selected context exactly uniform. Independent successful batches give independent effective repeated-context examples. A degree-$`k`$ envelope can be estimated by products of their loss bits. Its coefficients may be signed; boundedness permits statistical estimation even though the estimator is not a binary effect.

Minimizing the estimated envelope surrogate loses at most $`\Gamma_k(a)`$ plus statistical slack. The strict inequality $`\Gamma_k(a)\lt \varepsilon`$ leaves room for that slack. A fixed number of independent batches, with their failures included in $`\delta`$, proves the matching fixed-budget upper bound. [The passive proof](../science/passive_frontier.md) gives the extraction and concentration details.

## Replay and the meaning of the resource

If the source can deliberately prepare $`k`$ independent copies at a sampled context, the learner obtains effective groups directly. For fixed tolerance above $`\Gamma_k(a)`$, the number of groups can be independent of $`M`$. Every initial and repeated specimen is still charged. This capability is independent preparation from the source, not cloning a received unknown state.

Random replica depth is another interface choice. With $`K\sim\mathrm{Poisson}(a)`$, the loss-bit product has mean $`e^{a(\ell_h(x)-1)}`$. The identity is inherited Bernoulli-factory machinery. If a natural arrival always prepares an initial specimen, the physical count is $`\max\{1,K\}`$, with mean $`a+e^{-a}`$, rather than $`a`$. A finite expected count with an unbounded tail is different from a deterministic cap.

The [resource account](../science/replay_and_resources.md) also charges discarded passive arrivals, classical caches, measurement circuits and any quantum waiting memory.

## What the result establishes

This is a quantum-data access theorem with a classical statistical core. Commuting states already force the lower bound, and immediate individual measurements attain the support exponent for fixed $`H`$. It establishes no quantum processing advantage or general runtime speedup.

The PAC requirement concerns the excess of the hypothesis actually returned. Expected regret is a different criterion and has a different sharp moment-limited factor. Improper predictions outside the supplied class, nonuniform contexts, evolving or smooth state tables, critical threshold equalities and joint parameter limits require separate analysis.

The conclusion is quantitative: a chosen nonlinear-risk accuracy determines which repeated conditional observations the source must supply. The settled [30-milestone map](milestones.md) connects this story to the proofs: M01–M12 assemble the model; M13–M19 explain the scalar frontier; M20–M27 establish the passive theorem; M28–M30 locate replay, metrics, resources and scope.
