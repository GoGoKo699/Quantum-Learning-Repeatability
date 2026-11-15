# The passive context-support frontier

This file proves the fixed-parameter sample exponent for proper selection from a finite hypothesis class. The source and loss convention are specified in [the model](model.md). The scalar approximation theorem used below is proved in [the moment frontier](moment_frontier.md).

## Statement and scope

An unknown, fixed table assigns a density matrix $`\rho_x`$ to each identifiable context $`x\in[M]`$. A passive source independently draws $`X`$ uniformly from $`[M]`$ and supplies one fresh specimen of $`\rho_X`$. The learner cannot choose $`X`$ or request another specimen at that context. Different visits to a context prepare independent copies of its same fixed state.

There are $`m\le H`$ known projector-valued hypotheses $`\Pi_h(x)`$. Write

$$
\ell_h(x)=1-\mathrm{Tr}[\Pi_h(x)\rho_x],\qquad
A_h=\frac1M\sum_{x=1}^M e^{a\ell_h(x)},\qquad
R_a(h)=\frac1a\log A_h,
$$

where $`a>0`$. A proper learner returns an index $`\widehat h`$ in the supplied class. Its guarantee is

$$
\Pr\!\left[R_a(\widehat h)-\min_h R_a(h)\le\varepsilon\right]
\ge 1-\delta
$$

for every fixed source table and supplied class. The learner may otherwise process all supplied specimens jointly and adaptively.

For $`r\ge0`$, let

$$
K_r(a)=\sup_{\mu,\nu}
\frac{\int_0^1e^{au}\,d\mu(u)}{\int_0^1e^{au}\,d\nu(u)},
\qquad
\Gamma_r(a)=\frac1a\log K_r(a),
$$

where $`\mu,\nu`$ are probability measures with equal moments of degrees $`0,\ldots,r`$. Thus $`K_r(a)`$ is the same constant denoted $`\kappa_r(a)`$ in the moment account. The moment-frontier theorem gives the equivalent attained envelope problem

$$
K_r(a)=\min\left\lbraceK:
\exists P\in\mathbb R[u],\ \deg P\le r,\quad
e^{au}\le P(u)\le K e^{au}\quad(0\le u\le1)\right\rbrace.
$$

**Theorem.** Fix $`a>0`$, an integer $`H\ge2`$, confidence $`0\lt \delta\lt 1/2`$, and an integer $`k\ge1`$. If

$$
\Gamma_k(a)<\varepsilon<\Gamma_{k-1}(a),
$$

then the worst-case fixed-budget passive sample complexity, over classes of size at most $`H`$ and fixed source tables, satisfies

$$
N^{*}(M)=\Theta_{a,\varepsilon,H,\delta,k}
\!\left(M^{1-1/k}\right)
\qquad(M\to\infty).
$$

The upper bound holds for every such finite class. The lower bound is witnessed by one class of two constant commuting projectors on two qubits. It is not a lower bound for every class with two hypotheses. Constants can depend on the displayed fixed parameters and the distances from the two threshold values. Critical accuracies $`\varepsilon=\Gamma_r(a)`$, growing $`H`$ or $`k`$, and joint limits involving $`a`$, $`\varepsilon`$, and $`M`$ are not covered by this statement.

## Lower bound against arbitrary quantum processing

### Two moment-matched worlds

First suppose $`k\ge2`$, and put $`r=k-1`$. Because $`\varepsilon\lt \Gamma_r(a)`$, choose moment-matched probability measures $`\mu,\nu`$ such that

$$
u=\int e^{ap}\,d\mu(p),\qquad
v=\int e^{ap}\,d\nu(p),\qquad
g=\frac1a\log\frac vu>\varepsilon.
$$

The measures may be swapped to arrange $`v>u`$. An approximate maximizing pair with this strict gap is enough; no numerical approximation of an optimizer is used in the proof.

For each context independently freeze two latent probabilities. In world $`0`$, draw $`p_x\sim\mu`$ and $`q_x\sim\nu`$, independently, and set

$$
\rho_x=\tau_{p_x}\otimes\tau_{q_x},\qquad
\tau_p=\mathrm{diag}(1-p,p).
$$

World $`1`$ swaps the two priors. The fixed class consists of

$$
\Pi_1=|0\rangle\langle0|\otimes I,
\qquad
\Pi_2=I\otimes|0\rangle\langle0|.
$$

Their losses are $`p_x`$ and $`q_x`$. These are valid supervised examples with a constant reference label, if labels are included in the source notation. Only proper selection between the two supplied measurements is claimed: an unrestricted improper classifier would be a different task.

The random tables are priors for a lower-bound argument. Once drawn, each table is fixed throughout all sampling; the source does not redraw $`p_x`$ or $`q_x`$ when a context is revisited.

### Equality before a $`k`$-fold repeat

Condition on the entire sequence of sampled context labels. If context $`x`$ occurs $`s`$ times, its specimens have state $`\rho_x^{\otimes s}`$. After regrouping tensor factors by coordinate,

$$
\mathbb E[\rho_x^{\otimes s}]
=\mathbb E[\tau_{p_x}^{\otimes s}]
 \otimes\mathbb E[\tau_{q_x}^{\otimes s}].
$$

Every matrix entry of $`\tau_p^{\otimes s}`$ is a polynomial in $`p`$ of degree at most $`s`$. Therefore the two worlds have exactly the same prior-averaged state whenever $`s\le r`$. Independence of the frozen parameters at distinct contexts makes the *entire* prior-averaged training state identical whenever every context count is at most $`k-1`$.

This equality is at the level of the supplied quantum registers, with their classical context labels. Consequently it survives every collective measurement, intermediate measurement, adaptive control, and classical postprocessing allowed to the learner. It does not depend on a restriction to a particular measurement strategy.

For $`n`$ iid uniform context draws, let $`E`$ be the event that no context occurs $`k`$ times. A union bound over subsets of $`k`$ sample positions gives

$$
q_n:=\Pr(E^c)
\le {n\choose k}M^{1-k}
\le\frac{n^k}{k!M^{k-1}}.
$$

If $`\omega_0,\omega_1`$ are the prior-averaged classical-quantum training states, their trace distance obeys

$$
\frac12\|\omega_0-\omega_1\|_1\le q_n.
$$

Indeed their contributions on $`E`$ are equal, and the remaining subnormalized states each have trace $`q_n`$. With equal world priors, no procedure can identify the world with average probability greater than $`(1+q_n)/2`$.

### Fixed-table risks and the PAC contradiction

It remains to relate the annealed gap $`g`$ to a source with a fixed deterministic table. Define

$$
\zeta=\frac{a(g-\varepsilon)}4>0.
$$

Both coordinate exponential moments are averages of $`M`$ independent random variables in $`[1,e^a]`$. Hoeffding's inequality and a union bound show that, in either world, with probability at least $`1-\eta_M`$,

$$
\left|\frac1M\sum_xe^{ap_x}-\mathbb E e^{ap_x}\right|\le\zeta,
\qquad
\left|\frac1M\sum_xe^{aq_x}-\mathbb E e^{aq_x}\right|\le\zeta,
$$

where

$$
\eta_M=4\exp\!\left(-\frac{2M\zeta^2}{(e^a-1)^2}\right).
$$

All exponential moments are at least one, so $`\log`$ is 1-Lipschitz on their range. On this good-table event the two actual risks differ, in the intended direction, by at least

$$
g-\frac{2\zeta}{a}
=\frac{g+\varepsilon}{2}>\varepsilon.
$$

Thus, on every good table, an $`(\varepsilon,\delta)`$-PAC proper learner must select the corresponding world's unique better hypothesis with probability at least $`1-\delta`$. Averaging over the table prior would identify the world with probability at least $`1-\delta-\eta_M`$.

For explicit constants put $`w=1-2\delta>0`$. Take $`M`$ large enough that $`\eta_M\le w/8`$, and take

$$
n\le c\,M^{1-1/k},\qquad
c=\left(\frac{wk!}{4}\right)^{1/k}.
$$

Then $`q_n\le w/4`$. The learning guarantee would give world-identification success at least $`1/2+3w/8`$, whereas the trace-distance bound permits at most $`1/2+w/8`$. This contradiction proves the lower bound. In particular, some deterministic fixed table violates the proposed learning guarantee; a random-table prior is not being substituted for the original task.

When $`k=1`$, the asserted exponent is zero. Since $`\varepsilon\lt \Gamma_0(a)=1`$, two deterministic tables with opposite optimal hypotheses and risk gap one rule out a zero-sample learner at $`\delta\lt 1/2`$. Hence $`N^{*}(M)\ge1=\Omega(M^0)`$. The preceding collision argument is unnecessary in this case.

## Upper bound from uniformly selected collision groups

The upper proof requires no coherent quantum memory for fixed $`H`$. It uses separate data batches for different hypotheses, measures each specimen immediately, and stores only classical context labels and measurement outcomes.

### A constant-probability $`k`$-collision

For fixed $`k\ge2`$, take a batch of

$$
b_M=\left\lceil M^{1-1/k}\right\rceil
$$

iid contexts. Let $`C`$ count subsets of $`k`$ positions having the same context. Then

$$
\mathbb EC={b_M\choose k}M^{1-k}\longrightarrow\lambda_k=\frac1{k!}.
$$

In $`\mathbb EC^2`$, disjoint pairs of subsets contribute asymptotically $`\lambda_k^2`$, identical subsets contribute $`\lambda_k`$, and pairs overlapping in $`j\in\{1,\ldots,k-1\}`$ positions contribute

$$
{b_M\choose k}{k\choose j}{b_M-k\choose k-j}
M^{1-2k+j}=O_k(M^{-1+j/k})=o(1).
$$

Consequently $`\mathbb EC^2\to\lambda_k^2+\lambda_k`$. The second-moment bound gives a constant $`\alpha_k>0`$ such that, for all sufficiently large $`M`$,

$$
\Pr(C>0)\ge\frac{(\mathbb EC)^2}{\mathbb EC^2}\ge\alpha_k.
$$

For example $`\alpha_k=1/[2(k!+1)]`$ works after increasing the finite lower cutoff on $`M`$. For $`k=1`$, use $`b_M=1`$ and $`\alpha_1=1`$.

### Uniformity and independence are preserved

In a successful batch select uniformly from the set of contexts occurring at least $`k`$ times, and retain the first $`k`$ associated outcomes. The selection uses only the context labels and independent random coins. Label-permutation symmetry gives

$$
\Pr(X_{\mathrm{selected}}=x\mid\text{batch succeeds})=\frac1M
$$

for every $`x`$, for every fixed source table. No symmetry of the unknown states is assumed. Choosing the first $`k`$ occurrences also uses no measurement outcome.

Independent batches give independent selected groups. More precisely, a successful batch has a fixed conditional distribution: a uniform context and $`k`$ independent outcomes from its conditional state. This distribution does not depend on which batch succeeded. Therefore the first $`L`$ successful batches supply iid groups, independently of the event that a prescribed number of batches contains at least $`L`$ successes. Repeated selected labels across different batches do not spoil independence: source visits are independent preparations from the same fixed table.

### A signed polynomial is an observable, not automatically an effect

Choose an optimal degree-$`k`$ envelope

$$
e^{au}\le P(u)=\sum_{j=0}^k c_j u^j
\le K_k(a)e^{au}.
$$

Fix hypothesis $`h`$ for a batch. Upon receiving $`(x,\rho_x)`$, measure the loss projector $`I-\Pi_h(x)`$, producing $`Y\in\{0,1\}`$ with mean $`\ell_h(x)`$. For a selected collision group define

$$
Z_h=\sum_{j=0}^k c_j\prod_{i=1}^jY_i,
$$

with empty product one. Conditional independence of the specimens at that context gives

$$
\mathbb E[Z_h\mid x]=P(\ell_h(x)),\qquad
|Z_h|\le A_P:=\sum_{j=0}^k|c_j|.
$$

The coefficients need not be positive. Pointwise positivity of $`P`$ does not make this estimator a binary outcome or its associated operator a positive effect. Its bounded range is sufficient for the following classical estimate.

Equivalently, on $`k`$ quantum copies one may use the Hermitian observable

$$
O_h(x)=\sum_{j=0}^k c_j
\bigl(I-\Pi_h(x)\bigr)^{\otimes j}\otimes I^{\otimes(k-j)},
\qquad \|O_h(x)\|\le A_P.
$$

If a binary effect is needed by another learning primitive, $`(O_h+A_PI)/(2A_P)`$ lies between zero and identity and admits a standard projector dilation. This shift and rescaling, including its effect on accuracy and gate costs, must be retained.

### Finite estimates and a fixed sample budget

Put

$$
\eta=\frac{e^{a\varepsilon}-K_k(a)}4>0,
\qquad
L=\left\lceil\frac{2A_P^2}{\eta^2}
\log\frac{4H}{\delta}\right\rceil.
$$

For each hypothesis, average $`Z_h`$ over $`L`$ successful independent batches. Hoeffding's inequality gives, simultaneously for all $`m\le H`$, with probability at least $`1-\delta/2`$,

$$
|\widehat S_h-S_h|\le\eta,
\qquad
S_h=\frac1M\sum_xP(\ell_h(x)).
$$

To obtain a fixed rather than merely expected sample budget, allocate per hypothesis

$$
B=\left\lceil
\frac{2L+8\log(2H/\delta)}{\alpha_k}\right\rceil
$$

independent batches. Their success indicators are iid with probability at least $`\alpha_k`$. A Chernoff bound shows that fewer than $`L`$ successes occurs with probability at most $`\delta/(2H)`$. If there are too few successes the learner may return any index; this event is included in its failure probability. The complete budget is

$$
N\le H B b_M
=O_{a,\varepsilon,H,\delta,k}(M^{1-1/k}).
$$

Choose $`\widehat h`$ minimizing $`\widehat S_h`$, and let $`h_{*}`$ minimize the true tilted risk. On the simultaneous good event,

$$
A_{\widehat h}\le S_{\widehat h}
\le S_{h_{*}}+2\eta
\le K_k(a)A_{h_{*}}+2\eta.
$$

Since $`A_{h_{*}}\ge1`$,

$$
R_a(\widehat h)-R_a(h_{*})
\le\frac1a\log\bigl(K_k(a)+2\eta\bigr)
<\varepsilon.
$$

The envelope distortion enters once, as $`\Gamma_k(a)`$, rather than twice. Combining the statistical and batch-failure probabilities proves the upper bound.

## What the theorem establishes

For fixed parameters in a strict threshold interval, increasing the required nonlinear-risk accuracy changes which repeat order the passive stream must supply. That repeat order determines the power of the context support in the sample budget. Even unrestricted quantum processing cannot recover moments absent from the prior-averaged input states.

The matching exponent is already achievable by immediate single-copy measurements and classical collision bookkeeping for fixed $`H`$. Thus the theorem is a data-access and statistical-accuracy frontier. It asserts no quantum-processing speedup, no advantage over a matched classical latent-Bernoulli experiment, and no lower bound for every hypothesis class. The resources behind the upper construction and the stronger repeated-input model are described in [replay and resources](replay_and_resources.md).

The proof uses established moment matching, polynomial-observable estimation, and generalized-birthday methods. Its scalar relative-approximation duality and closest scientific comparisons are credited in [the moment frontier](moment_frontier.md) and the repository's related-work account.
