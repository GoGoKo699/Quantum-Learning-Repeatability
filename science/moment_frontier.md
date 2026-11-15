# The moment frontier for tilted risk

The [learning model](model.md) uses positive tilt $`a>0`$ and per-context losses in $`[0,1]`$. This page defines a scalar constant that measures the largest tilted-risk ambiguity compatible with the first $`r`$ moments. It proves its equivalent polynomial formulation and its operational meaning. The polynomial and moment-duality tools are classical; the learning statements use them with an explicit quantum source construction.

## 1. A sharp moment-ratio constant

Let $`\mathcal P([0,1])`$ denote the probability measures on $`[0,1]`$, put $`f_a(u)=e^{au}`$, and let $`r\geq0`$ be an integer. Define

$$
\kappa_r(a)=
\max_{\substack{\mu,\nu\in\mathcal P([0,1])\\
\int u^j\,d\mu=\int u^j\,d\nu\ (0\leq j\leq r)}}
\frac{\int f_a\,d\mu}{\int f_a\,d\nu},
\qquad
\Gamma_r(a)=\frac{\log\kappa_r(a)}a.
$$

The order-zero condition records equal mass. Both measures already have mass one, but retaining it makes the linear-program formulation transparent. Swapping $`\mu`$ and $`\nu`$ is allowed, so

$$
\Gamma_r(a)=
\max_{\mu,\nu\text{ matching through }r}
\left|
\frac1a\log\int f_a\,d\mu-
\frac1a\log\int f_a\,d\nu
\right|.
$$

The maximum exists. The space of probability measures on the compact interval is weakly compact; the moment constraints are closed; the exponential integrals are continuous; and the denominator is at least one. In particular, $`1\leq\kappa_r(a)\leq e^a`$.

The measures can be chosen with finite support. Indeed, the vector

$$
\left(\int u\,d\mu,\ldots,\int u^r\,d\mu,\int f_a\,d\mu\right)
$$

lies in the convex hull of the curve $`(u,\ldots,u^r,f_a(u))\in\mathbb R^{r+1}`$. Carathéodory's theorem replaces it by a measure on at most $`r+2`$ points. Applying this separately to an optimal pair preserves its moments and exponential integrals.

## 2. Equivalent positive polynomial envelope

**Theorem 1 — moment ratio and polynomial envelope.** For every $`a>0`$ and integer $`r\geq0`$,

$$
\kappa_r(a)=
\min\left\lbraceK:\ \exists p\in\mathbb R[u],\ \deg p\leq r,
\quad f_a(u)\leq p(u)\leq Kf_a(u)\quad(0\leq u\leq1)\right\rbrace.
$$

The polynomial minimum is attained. Equivalently, over strictly positive polynomials of degree at most $`r`$,

$$
\kappa_r(a)=
\min_{p>0,\ \deg p\leq r}
\frac{\max_{u\in[0,1]}p(u)/f_a(u)}
{\min_{u\in[0,1]}p(u)/f_a(u)}.
$$

**Proof.** First suppose $`f_a\leq p\leq Kf_a`$ and $`\mu,\nu`$ match moments through $`r`$. Then

$$
\int f_a\,d\mu
\leq\int p\,d\mu
=\int p\,d\nu
\leq K\int f_a\,d\nu.
$$

Thus every feasible envelope bounds the moment ratio from above.

For the converse, take nested finite sets $`G_N\subset[0,1]`$ whose union is dense and that all contain $`r+1`$ fixed distinct points. When $`r=0`$, one fixed point suffices. On a finite grid, scale a moment-matched pair of probability measures by the reciprocal of its denominator. The ratio problem becomes the finite linear program

$$
\begin{aligned}
\text{maximize }&\sum_{u\in G_N} f_a(u)\alpha_u,\\
\text{subject to }&\alpha_u,\beta_u\geq0,\\
&\sum_{u\in G_N}u^j(\alpha_u-\beta_u)=0\quad(0\leq j\leq r),\\
&\sum_{u\in G_N}f_a(u)\beta_u=1.
\end{aligned}
$$

Conversely, feasible finite measures $`\alpha,\beta`$ have the same nonzero mass; normalizing both by that mass recovers probability measures with the same objective ratio. The feasible set is nonempty and bounded: $`f_a\geq1`$ bounds the mass of $`\beta`$ by one, and the order-zero constraint gives the same bound for $`\alpha`$.

The dual has a real polynomial $`p_N`$ of degree at most $`r`$ for the moment constraints and a scalar $`K_N`$ for the exponential normalization. Its inequalities are exactly

$$
f_a(u)\leq p_N(u)\leq K_Nf_a(u)\qquad(u\in G_N).
$$

Finite-dimensional linear-program duality therefore gives an attained grid optimum $`K_N`$, equal to the grid moment ratio. Since grid-supported pairs are admissible in the full problem,

$$
1\leq K_N\leq\kappa_r(a)\leq e^a.
$$

At the $`r+1`$ fixed nodes, the values of $`p_N`$ are uniformly bounded. The inverse of their fixed Vandermonde matrix consequently bounds every coefficient of $`p_N`$. Pass to a subsequence on which its coefficients and $`K_N`$ converge, obtaining a polynomial $`p`$ and $`K\leq\kappa_r(a)`$. At any $`u\in[0,1]`$, choose grid points tending to $`u`$. Uniform convergence of the polynomials and continuity of $`f_a`$ give

$$
f_a(u)\leq p(u)\leq Kf_a(u).
$$

The first part of the proof now gives $`\kappa_r(a)\leq K`$, establishing equality and attainment. Finally, a positive polynomial can be scaled so that its minimum ratio $`p/f_a`$ is one; the smallest resulting $`K`$ is its maximum-to-minimum ratio. This proves the equivalent formula. $`\square`$

This scalar identity is inherited. In particular, [Adibi and Krysta, Appendix I, Theorem I.1 and Corollary I.2](https://arxiv.org/abs/2610.28999), give the exact weighted relative-approximation duality and matching-moment expectation ratio $`(1+d)/(1-d)`$ used here. The finite-grid proof above specializes that identity to the exponential and fixes the notation needed for the learning theorem. Related polynomial-approximation and moment-matching methods appear in [discrete functional estimation](https://arxiv.org/abs/1406.6956) and [population-parameter learning](https://arxiv.org/abs/1709.02707). The duality itself is not a new quantum principle.

## 3. Relative approximation, strictness, and convergence

Define the best relative approximation error

$$
E_r(a)=\min_{\deg q\leq r}\max_{0\leq u\leq1}
\left|q(u)e^{-au}-1\right|.
$$

The minimum exists by the same coefficient-compactness argument as above, and $`E_r(a)\lt 1`$: a suitable positive constant already gives error $`\tanh(a/2)\lt 1`$. Scaling an envelope to balance its upper and lower relative errors, and conversely scaling a relative approximant upward, gives

$$
E_r(a)=\frac{\kappa_r(a)-1}{\kappa_r(a)+1},
\qquad
\Gamma_r(a)=\frac1a\log\frac{1+E_r(a)}{1-E_r(a)}.
$$

In detail, $`f_a\leq p\leq Kf_a`$ implies that $`q=2p/(K+1)`$ has relative error at most $`(K-1)/(K+1)`$. If $`q`$ has relative error $`E\lt 1`$, then $`p=q/(1-E)`$ satisfies $`f_a\leq p\leq[(1+E)/(1-E)]f_a`$. Taking the optima proves both identities.

**Proposition 2 — a strictly decreasing frontier.** For every fixed $`a>0`$,

$$
1=\Gamma_0(a)>\Gamma_1(a)>\Gamma_2(a)>\cdots>0,
\qquad
\lim_{r\to\infty}\Gamma_r(a)=0.
$$

**Proof.** Moment matching becomes more restrictive with $`r`$, so the sequence is nonincreasing. If a finite-degree value had $`\kappa_r=1`$, Theorem 1 would give a polynomial identical to $`e^{au}`$, which is impossible for $`a>0`$. Thus each finite-degree value is positive.

For strictness, use the standard weighted Chebyshev alternation theorem: a best degree-$`s`$ approximation to $`f_a`$ with positive weight $`e^{-au}`$ has $`s+2`$ alternating extrema of its weighted error. If $`E_{r+1}=E_r`$, an optimal degree-$`r`$ polynomial $`q_r`$ would also be optimal at degree $`r+1`$. Its error

$$
e(u)=q_r(u)e^{-au}-1
$$

would then have $`r+3`$ alternating extreme points. Their $`r+1`$ middle points are interior extrema, so $`e'`$ would have at least $`r+1`$ distinct zeros. But

$$
e'(u)=e^{-au}\big(q'_r(u)-a q_r(u)\big),
$$

and the factor in parentheses is a nonzero polynomial of degree at most $`r`$. It is nonzero because a nonzero polynomial cannot satisfy $`q'=aq`$ for $`a>0`$, while the zero approximant has error one and is not optimal. This contradiction proves strictness.

For convergence, put

$$
T_r(a)=e^a-\sum_{j=0}^{r}\frac{a^j}{j!}.
$$

The polynomial

$$
p_r(u)=\sum_{j=0}^{r}\frac{(au)^j}{j!}+T_r(a)
$$

satisfies $`f_a\leq p_r\leq f_a+T_r(a)\leq(1+T_r(a))f_a`$. Therefore

$$
0\leq\Gamma_r(a)\leq\frac1a\log\big(1+T_r(a)\big)\longrightarrow0.
$$

For $`r=0`$, the largest ratio of unconstrained exponential means is $`e^a`$, attained by $`\delta_1`$ and $`\delta_0`$, so $`\Gamma_0=1`$. $`\square`$

The alternation theorem used here is the usual best-approximation theorem for a positive weight on an interval. Its role is only to establish strictness; the dual characterization and the learning bounds do not depend on inferring strictness from numerical grids.

## 4. The one-copy value and small-tilt hierarchy

**Proposition 3 — the first frontier value.** Let $`b=e^a-1`$ and

$$
m_{*}(a)=\frac1a-\frac1b.
$$

Then $`m_{*}\in(0,1)`$ and

$$
\kappa_1(a)=\frac ba\exp\left(-1+\frac ab\right),
\qquad
\Gamma_1(a)=\frac1a\log\frac ba-\frac1a+\frac1b.
$$

**Proof.** Among probability measures with mean $`m`$, convexity gives

$$
e^{am}\leq\int e^{au}\,d\mu(u)\leq1+m(e^a-1).
$$

The lower endpoint is attained by $`\delta_m`$, and the upper by $`(1-m)\delta_0+m\delta_1`$. Hence

$$
\kappa_1(a)=\max_{0\leq m\leq1}(1+bm)e^{-am}.
$$

The derivative of its logarithm is $`b/(1+bm)-a`$. It is positive at zero and negative at one, and is strictly decreasing. The unique maximizer is $`m_{*}`$; substitution gives the displayed formula. $`\square`$

Writing $`S(h)=(h-1)h^{1/(h-1)}/(e\log h)`$, this is $`\Gamma_1(a)=a^{-1}\log S(e^a)`$. The function $`S`$ is the classical [Specht ratio](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1259-1.pdf), a sharp reverse arithmetic-geometric mean constant. The constant is inherited; its operational interpretation is supplied below.

**Proposition 4 — fixed-degree small-tilt asymptotics.** For each fixed integer $`r\geq1`$,

$$
\Gamma_r(a)\sim\frac{a^r}{(r+1)!\,4^r}\qquad(a\downarrow0).
$$

**Proof.** Let $`P_r(u)=\sum_{j=0}^{r}(au)^j/j!`$. Uniformly on $`[0,1]`$,

$$
\frac{f_a(u)-P_r(u)}{a^{r+1}}
\longrightarrow\frac{u^{r+1}}{(r+1)!}.
$$

Subtracting $`P_r`$ does not change distance from the degree-$`r`$ polynomial space. After rescaling, the relative weight $`e^{-au}`$ converges uniformly to one and lies between $`e^{-a}`$ and one. Uniform approximation distance is Lipschitz in its target. Consequently,

$$
\frac{E_r(a)}{a^{r+1}}
\longrightarrow
\frac1{(r+1)!}\inf_{\deg q\leq r}\|u^{r+1}-q(u)\|_\infty.
$$

The last infimum is $`2^{-(2r+1)}`$. Indeed, the monic shifted Chebyshev polynomial $`2^{-(2r+1)}\mathrm T_{r+1}(2u-1)`$ has exactly that norm. A monic polynomial with smaller norm would differ from it by a degree-$`r`$ polynomial with at least $`r+1`$ sign changes between its alternating extreme points, a contradiction. Finally,

$$
\log\frac{1+E_r}{1-E_r}\sim2E_r,
$$

and division by $`a`$ yields the stated constant. $`\square`$

In particular, $`\Gamma_1(a)\sim a/8`$, $`\Gamma_2(a)\sim a^2/96`$, and $`\Gamma_3(a)\sim a^3/1536`$. These are fixed-degree limits; they do not assert uniformity when $`r`$ grows with $`1/a`$.

## 5. From an envelope to a learning guarantee

Let $`p(u)=\sum_{j=0}^{r}c_ju^j`$ be an optimal envelope. In a grouped $`r`$-copy example, measure hypothesis $`h`$ on its copies to obtain conditional IID Bernoulli losses $`Y_1,\ldots,Y_r`$. The statistic

$$
Z_h=c_0+\sum_{j=1}^{r}c_j\prod_{i=1}^{j}Y_i
$$

is unbiased for $`P_h=\mathbb E[p(\ell_h(X))]`$ and obeys $`|Z_h|\leq\sum_{j=0}^{r}|c_j|`$. Let $`A_h=\mathbb E[e^{a\ell_h(X)}]`$. The envelope gives

$$
A_h\leq P_h\leq\kappa_r(a)A_h.
$$

If all $`P_h`$ are estimated to additive error at most $`\eta`$ and the learner minimizes those estimates, then for a true risk minimizer $`h^{*}`$,

$$
A_{\widehat h}\leq P_{\widehat h}
\leq P_{h^{*}}+2\eta
\leq\kappa_r(a)A_{h^{*}}+2\eta.
$$

Since $`A_{h^{*}}\geq1`$,

$$
R_a(\widehat h)-R_a(h^{*})
\leq\Gamma_r(a)+\frac1a\log\left(1+\frac{2\eta}{\kappa_r(a)}\right)
\leq\Gamma_r(a)+\frac{2\eta}{a\kappa_r(a)}.
$$

For fixed $`a,r,H,\eta,\delta`$, bounded-variable concentration and a union bound estimate all hypotheses with finitely many groups, independently of $`M`$ and $`d`$. Separate groups are allocated to different hypotheses, so this construction does not attempt incompatible measurements on one copy. Every supplied copy is charged. The polynomial representation is a direct instance of established multi-copy polynomial estimation, not a new state-preparation assumption.

Thus every tolerance strictly above $`\Gamma_r(a)`$ admits a support-independent grouped-access PAC guarantee. A finite known $`M`$ may permit better tolerances after sufficiently many natural repeated groups; the statement is uniform over unbounded supports.

## 6. Why the same constant is unavoidable

Choose an optimal pair $`\mu_-,\mu_+`$ matching moments through $`r`$, oriented so that

$$
\frac1a\log\int f_a\,d\mu_+
-\frac1a\log\int f_a\,d\mu_-
=\Gamma_r(a).
$$

To witness the worst case under the class-size cap $`H`$, use exactly $`H`$ hypotheses. For each world $`j\in[H]`$ and each context $`x`$, independently draw latent probabilities $`U_{x,j}\sim\mu_-`$ and $`U_{x,h}\sim\mu_+`$ for $`h\ne j`$. Freeze these draws, and define

$$
\tau_u=\begin{pmatrix}1-u&0\\0&u\end{pmatrix},
\qquad
\rho_x=\bigotimes_{h=1}^{H}\tau_{U_{x,h}}.
$$

Hypothesis $`h`$ uses the projector $`|0\rangle\langle0|`$ on coordinate $`h`$, tensored with identities elsewhere. Hence $`\ell_h(x)=U_{x,h}`$. This is a valid source on $`H`$ qubits; for two hypotheses, two qubits suffice, independently of $`M`$.

For any $`s\leq r`$, each entry of $`\tau_u^{\otimes s}`$ is a polynomial in $`u`$ of degree at most $`s`$. Therefore

$$
\int\tau_u^{\otimes s}\,d\mu_-(u)
=\int\tau_u^{\otimes s}\,d\mu_+(u).
$$

Regrouping tensor factors by hypothesis coordinate proves that the averaged $`s`$-copy state at a context is identical in every world. Conditional on a sequence of distinct grouped-example labels, the complete averaged training state is consequently identical across worlds, even when the learner is allowed a collective measurement on all groups. With $`G`$ groups, the probability of a repeated group label is at most $`G(G-1)/(2M)`$.

For each fixed world, the table averages of $`f_a(U_{x,h})\in[1,e^a]`$ concentrate around their prior means as $`M\to\infty`$. The log is $`1`$-Lipschitz on $`[1,\infty)`$, so the actual frozen-table risks concentrate as well. With probability tending to one over the table construction, world $`j`$ has unique optimal hypothesis $`j`$, and every other hypothesis has excess tending to $`\Gamma_r(a)`$.

Suppose a fixed finite number of groups gave a uniform guarantee at $`\epsilon\lt \Gamma_r(a)`$ and confidence $`1-\delta>1/H`$. Average that guarantee over a uniformly random world and its frozen-table prior. As $`M\to\infty`$, label collisions and atypical tables vanish, while all training states become identical across worlds. No learner can then output the correct world index with average probability greater than $`1/H`$. This contradicts the claimed guarantee. Since a guarantee for every fixed table also holds after averaging over any table prior, the argument supplies a worst-case fixed source rather than assuming a freshly randomized process on every use.

Together with the envelope upper bound, this proves the worst-case support-independent PAC boundary over classes of size at most $`H`$, with strict inequalities:

- $`\epsilon>\Gamma_r(a)`$: finitely many grouped examples suffice uniformly in $`M`$;
- $`\epsilon\lt \Gamma_r(a)`$ and $`\delta\lt 1-1/H`$: no finite uniform bound exists.

No claim at $`\epsilon=\Gamma_r(a)`$ follows from these statements. The lower-bound states commute, and the quantum measurement class is unrestricted. The obstruction is unavailable conditional repetition, not a computational separation between quantum and classical processors.

## 7. Expected regret has a different exact floor

The following elementary decision lemma identifies the metric distinction.

**Lemma 5 — interval uncertainty.** Suppose each of $`H`$ action risks lies in a known interval $`[l_h,l_h+W]`$. A randomized action can guarantee worst-case expected regret at most $`(1-1/H)W`$ over the product of these intervals.

**Proof.** By the finite-action compact-game minimax theorem, it suffices to bound the Bayes regret under every distribution of admissible risk vectors. Choose a measurable minimizing action $`J`$ for each vector, breaking ties deterministically, and let $`p_h=\Pr(J=h)`$. Pointwise,

$$
R_h-R_J\leq l_h-l_J+W\,\mathbf1\{h\ne J\}.
$$

Averaging its expectation over a fixed random action with probabilities $`p_h`$ cancels the $`l`$ terms, giving

$$
\sum_h p_h\mathbb E[R_h-R_J]
\leq W\left(1-\sum_h p_h^2\right)
\leq W(1-1/H).
$$

Some fixed action has Bayes regret at most this weighted average. Minimax gives the result. $`\square`$

If the first $`r`$ moments of every loss distribution were known exactly, each risk would lie in an interval of width at most $`\Gamma_r(a)`$. The lemma gives expected regret at most $`(1-1/H)\Gamma_r(a)`$. The $`H`$ indistinguishable worlds above attain that value in the large-support limit.

This ideal-moment statement also has a statistical version with arbitrarily small slack. For $`\xi\geq0`$, let $`\Gamma_r(a;\xi)`$ be the largest risk difference between two probability measures whose moments of orders $`1,\ldots,r`$ differ by at most $`\xi`$. Compactness gives

$$
\Gamma_r(a;\xi)\downarrow\Gamma_r(a)\qquad(\xi\downarrow0).
$$

Indeed, any sequence of approximate maximizers with $`\xi\downarrow0`$ has a subsequence converging to an exactly moment-matched pair. Estimate every moment within $`\xi/2`$, form the corresponding feasible moment intervals for each action, and use the interval decision rule. On the estimation event the risk intervals have width at most $`\Gamma_r(a;\xi)`$. Its complement contributes at most its probability because excess risk is bounded by one. Thus finite grouped samples achieve expected regret arbitrarily close to $`(1-1/H)\Gamma_r(a)`$, uniformly in $`M`$.

This expected value does not give a PAC guarantee below $`\Gamma_r(a)`$: under an indistinguishable world, randomization still returns a wrong, high-excess hypothesis with substantial probability.

## 8. What the frontier does and does not establish

The constants quantify the exact ambiguity of the exponential conditional-loss objective under moment-limited access. The passive single-copy exponent law additionally needs the probability of obtaining repeated contexts; it is not a consequence of polynomial approximation alone.

Moment matching, repeated-observation identifiability, and collision estimation have substantial classical antecedents, including [population-parameter learning](https://arxiv.org/abs/1709.02707), [multi-observation elicitation](https://proceedings.mlr.press/v65/casalaina-martin17a.html), and [Rényi entropy estimation](https://arxiv.org/abs/1408.1000). The construction here uses them to prove a full-training-state indistinguishability statement and a matching quantum-learning access boundary. A restriction to a structured source family or a different output model can remove this worst-case obstruction and requires its own analysis.
