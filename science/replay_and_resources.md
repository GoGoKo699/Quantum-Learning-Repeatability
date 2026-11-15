# Repeated-input access and resource charges

The passive theorem counts naturally occurring one-copy examples. Controlled repetition changes that source interface. This file specifies the stronger interface and records what the constructive bounds cost. The central convention is the positive-loss tilt in [the model](model.md): $`R_a(h)=a^{-1}\log\mathbb E e^{a\ell_h(X)}`$, with $`a>0`$.

## Conditional replay is an additional source capability

A natural source event first draws $`X`$ from its prescribed distribution and supplies $`(X,\rho_X)`$. In the replay model the learner may then request further independent preparations of that *same* $`\rho_X`$. The source table is unchanged. The learner need not be allowed to select an arbitrary context before the natural draw.

This is independent preparation by a source capable of repeating the underlying input or experiment. It is not cloning the received unknown specimen, inferring an unknown preparation circuit, or assuming free coherent access to classical data. Every initial specimen, repeated preparation, and known hypothesis-measurement operation is charged.

If the physical source cannot repeat an event—such as a unique uncontrolled trajectory—this interface is unavailable. The replay bounds do not manufacture it from passive examples.

## A finite replica cap removes the support dependence above its threshold

Suppose each natural source event can provide exactly $`k`$ independent copies of its sampled conditional state. Let $`P`$ be a degree-$`k`$ relative envelope from [the moment frontier](moment_frontier.md), and use the bounded estimator $`Z_h`$ from [the passive proof](passive_frontier.md). Independent natural events are already iid groups, so no collision search is needed.

For every fixed tolerance $`\varepsilon>\Gamma_k(a)`$, the same estimates and surrogate minimization give a proper learner with a finite number of source groups independent of the context support. One explicit per-hypothesis group count is

$$
L=\left\lceil\frac{2A_P^2}{\eta^2}
\log\frac{2H}{\delta}\right\rceil,
\qquad
\eta=\frac{e^{a\varepsilon}-K_k(a)}4,
\qquad A_P=\sum_{j=0}^k|c_j|,
$$

where $`P(u)=\sum_{j=0}^kc_ju^j`$. Using independent groups for each of $`m\le H`$ hypotheses costs at most $`H L`$ natural source events and $`kHL`$ physical specimens. The coefficients and therefore the constants can grow with $`a`$ and $`k`$; this formula does not hide an optimized joint limit.

Conversely, a hard cap of $`k`$ copies per natural event cannot uniformly support error below $`\Gamma_k(a)`$ using a number of events independent of unrestricted context support. Matching $`k`$-moment priors make the first group at each context identical between two lower-bound worlds. A second visit can supply more copies, but for any fixed number of events its probability can be made arbitrarily small by increasing the uniform support. Fixed-table concentration then gives the same proper-selection obstruction as in the passive proof.

This is a support-independent accuracy statement, not a claim that a fixed finite support remains unlearnable forever. Nor is a cap per source event the same as a lifetime cap on the total number of visits to one context.

## An exact exponential estimator with random replica depth

There is a useful alternative to choosing a deterministic cap. Draw $`K\sim\mathrm{Poisson}(a)`$, independently of the sampled context. For a fixed hypothesis, measure its loss projector $`I-\Pi_h(X)`$ on $`K`$ copies and let

$$
B_h=\prod_{j=1}^K Y_j,
\qquad \prod_{j=1}^0Y_j=1.
$$

Conditional on $`X=x`$,

$$
\mathbb E[B_h\mid x]
=\mathbb E[\ell_h(x)^K]
=e^{a(\ell_h(x)-1)}.
$$

Consequently

$$
\beta_h:=\mathbb EB_h=e^{-a}\mathbb E e^{a\ell_h(X)},
\qquad
R_a(h)=1+\frac1a\log\beta_h.
$$

Thus minimizing the true risk is equivalent to minimizing $`\beta_h`$. The block operator $`(I-\Pi_h(x))^{\otimes K}`$, with its empty-product convention, is a projector. If a learning primitive maximizes acceptance, use its complementary projector.

The identity is the classical Poisson probability-generating-function/exponential Bernoulli-factory construction. Its use here must be credited as inherited; it is not a nonlinear measurement on one unknown quantum specimen. For example, Dughmi, Hartline, Kleinberg, and Niazadeh describe the Poisson-exponential factory and expected-payoff applications in [their Bernoulli-factory account](https://www.sigecom.org/exchanges/volume_16/1/DUGHMI.pdf).

### The initial specimen is still charged

Under the natural-source interface, the first specimen is prepared even when $`K=0`$. The physical number prepared for an untruncated event is therefore

$$
\max\{1,K\},\qquad
\mathbb E\max\{1,K\}=a+e^{-a}\le 1+a.
$$

When $`K=0`$ this initial specimen is unused. An expected cost of exactly $`a`$ is valid only under an explicitly stronger interface that can reveal the context while preparing no quantum output on zero-copy events. That interface is not assumed here.

An exact bounded Bernoulli-factory lower bound on expected coin flips is a statement about that primitive. It is not automatically a lower bound on every tilted-risk learning algorithm.

### Finite-depth truncation

For a hard cap $`r\ge1`$, if $`K>r`$ discard the natural initial specimen, make no further requests, and set the estimator to zero. Otherwise use the preceding product estimator. Writing $`t_r=\Pr(K>r)`$, its mean $`\beta_h^{(r)}`$ satisfies

$$
0\le\beta_h-\beta_h^{(r)}\le t_r,
\qquad \beta_h\ge e^{-a}.
$$

Every event prepares at most $`r`$ specimens. Its expected count is at most $`a+e^{-a}`$, since truncation discards rather than prepares the oversized groups. Padding with known ancillas is bookkeeping for a learning algorithm, not an extra unknown-state preparation.

Suppose estimates of $`\beta_h^{(r)}`$ have uniform additive error at most $`\eta`$. Selecting a minimizer then gives

$$
\beta_{\widehat h}\le\beta_{h_{*}}+2\eta+t_r,
$$

and hence

$$
R_a(\widehat h)-R_a(h_{*})
\le\frac1a\log\!\left(1+e^a(2\eta+t_r)\right).
$$

For instance it suffices to choose $`2\eta+t_r\le e^{-a}(e^{a\varepsilon}-1)`$. Independent estimation per hypothesis uses

$$
L\ge\frac{1}{2\eta^2}\log\frac{2H}{\delta}
$$

groups per hypothesis by Hoeffding's inequality. This supplies a valid support-independent finite-class learner without any quantum collective-search theorem. Optimizing its dependence on tilt or hypothesis count is a separate question.

For fixed $`a`$, the Poisson tail admits caps of order $`\log(1/\varepsilon)/\log\log(1/\varepsilon)`$ as $`\varepsilon\to0`$. The matching necessity requires the moment-approximation lower bound at the same error convention; it is not inferred from this upper-tail calculation alone. This asymptotic is distinct from the passive theorem, which fixes $`a`$, $`\varepsilon`$, and $`k`$ before taking $`M\to\infty`$.

For a negative tilt $`-a`$, use acceptance rather than loss bits: $`\prod_{j=1}^K(1-Y_j)`$ has mean $`\mathbb E e^{-a\ell_h(X)}`$. Minimizing $`R_{-a}`$ then means *maximizing* this mean. Copy charges and tail estimates are unchanged; the optimization direction must be reversed.

## Physical and computational resources

The following accounting describes the constructions, rather than an optimized universal frontier in all resources.

| Construction | Natural source events | Physical specimens | Persistent storage | Hypothesis operations |
|---|---:|---:|---|---|
| Passive fixed-$`H`$ frontier | $`O(M^{1-1/k})`$ at fixed parameters | One per event | Classical context/outcome cache for one batch | One known single-copy measurement per received specimen |
| Deterministic $`k`$-copy replay, separate hypotheses | $`\le HL`$ | $`\le kHL`$ | Classical running estimates; source may prepare copies sequentially | At most $`k`$ known measurements per group |
| Capped Poisson replay, separate hypotheses | $`\le HL`$ | At most $`rHL`$; expectation at most $`(a+e^{-a})HL`$ | Classical running estimates | At most $`r`$ known measurements per group |
| Shared quantum collision blocks with joint QERM | Depends on the inherited QERM group count | Includes all specimens consumed while finding collision groups | Quantum cache of unknown specimens plus classical context records | Block-projector/dilation and threshold-search operations must be implemented |

### Passive storage and processing

For the memoryless-measurement upper bound, each batch can maintain a dictionary indexed by observed contexts, with counts capped at $`k`$ and the first $`k`$ binary outcomes. There are at most $`b_M`$ entries. A conservative peak classical-memory charge is

$$
O\!\left(b_M(\log M+k+\log(k+1))\right)\text{ bits}.
$$

Hypotheses and batches can be processed sequentially, reusing this cache. Uniform selection among eligible contexts can use reservoir sampling when a context first reaches count $`k`$. This selection is independent of all quantum measurement outcomes. Hash-table processing has expected linear word-operation cost per batch; bit operations, reading context labels, and implementing $`\Pi_h(x)`$ have their usual additional costs.

The source Hilbert-space dimension does not appear in the sample exponent. The cost of realizing its hypothesis measurements does: this work assumes those known measurements are implementable and does not replace their circuits with free oracles. No QRAM is required by the immediate-measurement construction.

### Optional joint QERM changes the storage obligation

Fanizza, Quek, and Rosati's [QERM theorem](https://doi.org/10.1103/PRXQuantum.5.020367) provides dimension-independent sample bounds with polylogarithmic dependence on the size of a finite projector class. Applying that theorem to the lifted replay projectors, or to a shifted/rescaled polynomial observable with a projector dilation, is an inherited route to improving hypothesis-count dependence.

It requires quantum data availability appropriate to that learning primitive. To use a collision group for several noncommuting hypotheses, one cannot first measure every incoming specimen with a chosen hypothesis and then treat its classical outcome as the untouched quantum state. A straightforward collision extractor retains unknown quantum specimens until the repeated context is identified, charging up to $`O(b_M\log d)`$ quantum bits for a batch of $`d`$-dimensional outputs, as well as the retained accepted groups and QERM workspace. Replay blocks likewise consume their full conditional-state copy count.

A block product projector needs the constituent known hypothesis tests and conjunction/complement controls; a signed polynomial surrogate additionally needs its shift, scale, and dilation. The QERM sample theorem does not imply a polylogarithmic gate count in the number of hypotheses. Threshold search and hypothesis-circuit evaluation can be expensive. These costs cannot be replaced by the sample count.

## Interpretation limits

The fixed-$`H`$ matching passive exponent already has a classical latent-Bernoulli realization. The result therefore does not establish a quantum processing advantage, a time speedup, a practical crossover, or a benefit from a particular hardware implementation. Its operational conclusion is which repeated conditional observations the selected nonlinear-risk accuracy requires, and what changes when the physical source can supply them deliberately.

Nonuniform or unknown context probabilities, an evolving state table, restrictions on quantum or classical memory, improper hypothesis outputs, and the exact threshold endpoints require their own analysis. They are not obtained by silently extending the displayed asymptotic.
