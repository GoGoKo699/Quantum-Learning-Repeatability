# Quantum learning from repeated contexts

The scarce resource studied here is a repeated occurrence of the **same classical context**. The learner receives quantum data at random contexts. It may process every supplied system jointly, but it cannot ask the source to reproduce a chosen context.

The objective is a nonlinear function of a conditional Born probability. This distinction matters even for commuting states: measuring one example produces a random outcome, whereas the objective applies its nonlinearity to the outcome's conditional mean.

## 1. Source and hypotheses

Let $M\geq 1$, let $\mathsf Q\cong\mathbb C^d$ be a finite-dimensional quantum register, and write $[M]=\{1,\ldots,M\}$. An unknown source is a fixed table

$$
\rho:[M]\longrightarrow\mathcal D(\mathsf Q),\qquad x\longmapsto\rho_x.
$$

One passive example is the classical-quantum state

$$
\Omega_\rho=\frac1M\sum_{x=1}^M |x\rangle\langle x|\otimes\rho_x.
$$

Training data consist of $n$ independent copies of $\Omega_\rho$. Equivalently, $X_1,\ldots,X_n$ are IID uniform on $[M]$, and, conditional on their labels, the supplied quantum state is

$$
\rho_{X_1}\otimes\cdots\otimes\rho_{X_n}.
$$

The table is fixed throughout the experiment. If a label reappears, the source supplies an independent copy of that label's same conditional state. Mixed states are allowed. No preparation circuit, purification, coherent source oracle, or chosen-input interface is supplied.

The learner knows $M$ and a finite hypothesis class

$$
\mathcal H=\{h_1,\ldots,h_m\},\qquad 1\leq m\leq H,\quad H\geq2.
$$

Here $H$ is the fixed class-size cap; $m$ is the size of the supplied class. Each hypothesis specifies known projectors $\Pi_h(x)$ on $\mathsf Q$. Its conditional loss is

$$
\ell_h(x)=1-\operatorname{Tr}\!\left(\Pi_h(x)\rho_x\right)\in[0,1].
$$

This is agnostic learning: the unknown table need not belong to the hypothesis class. The lower bounds use constant projectors on a fixed number of qubits, so they do not rely on difficult hypothesis evaluation or a growing quantum output dimension.

## 2. Tilted population risk

Fix a positive tilt $a>0$. The canonical risk is

$$
R_a(h;\rho)=\frac1a\log\left(\frac1M\sum_{x=1}^M e^{a\ell_h(x)}\right).
$$

The task is to minimize this quantity over $h\in\mathcal H$. It lies in $[0,1]$. As $a\to0$, it tends to the mean loss $M^{-1}\sum_x\ell_h(x)$; a positive tilt gives more weight to contexts with larger conditional loss.

Let $Y_h\in\{0,1\}$ be the loss outcome obtained by measuring $\{\Pi_h(x),I-\Pi_h(x)\}$ on one copy at context $x$, with $Y_h=1$ for the second outcome. Then

$$
\mathbb E[Y_h\mid X=x]=\ell_h(x).
$$

However, exponentiating that observed bit estimates a different quantity:

$$
\mathbb E[e^{aY_h}]
=1+(e^a-1)\mathbb E[\ell_h(X)],
$$

whereas the desired exponential mean is $\mathbb E[e^{a\ell_h(X)}]$. Replacing the conditional mean by one observed outcome therefore changes the learning objective.

All main statements use $a>0$. For comparison with a signed tilt $\gamma$, the identity

$$
R_{-a}(\ell)=1-R_a(1-\ell)
$$

converts minimization at negative tilt into maximization of the complemented positive-tilt risk. Reflection $u\mapsto1-u$ leaves the distortion constants in [the moment frontier](moment_frontier.md) unchanged. The direction of optimization must still be reversed when using this identity.

## 3. Learning guarantee and quantifiers

A learner is **proper**: on each run it outputs an index $\widehat h\in\mathcal H$. It may use arbitrary classical computation, classical randomness, ancillary systems initially independent of the source, and any collective quantum measurement on all supplied examples. There is no restriction to local measurements or to a bounded number of jointly processed copies.

The excess risk of its realized output is

$$
\mathcal E_a(\widehat h;\rho)
=R_a(\widehat h;\rho)-\min_{h\in\mathcal H}R_a(h;\rho).
$$

An $(\epsilon,\delta)$ guarantee means

$$
\Pr\!\left[\mathcal E_a(\widehat h;\rho)\leq\epsilon\right]\geq1-\delta
$$

for every fixed source table $\rho$. Probability is over the sampled labels, measurement outcomes, and learner randomness.

For a specified class and dimension, let $N^*(M,\mathcal H,d;a,\epsilon,\delta)$ be the least number of passive examples permitting this guarantee. The worst-case finite-class copy complexity is

$$
\mathsf N^*(M;a,H,\epsilon,\delta)
=\sup_{d,\,\mathcal H:\,1\leq|\mathcal H|\leq H}
N^*(M,\mathcal H,d;a,\epsilon,\delta).
$$

The algorithm may depend on the known class, $M$, and the displayed parameters. In support-size asymptotics, $a,H,\epsilon,\delta$ are fixed and $M\to\infty$. Constants may depend on those fixed parameters. The sharp exponent statements concern $0<\delta<1/2$ and errors strictly between successive moment-frontier values; they do not assert endpoint behavior or uniform constants when the tilt, accuracy, or class size also vary.

A support-independent guarantee uses a number of examples bounded independently of $M$. This is a uniform assertion over all finite context supports, not an assertion that a particular finite table remains unidentifiable with infinitely many examples.

### PAC excess and expected regret are different

The PAC condition above bounds the excess of the hypothesis actually returned. A different criterion is expected regret,

$$
\mathbb E\!\left[\mathcal E_a(\widehat h;\rho)\right].
$$

Randomizing between hypotheses can reduce expected regret while leaving a substantial probability of returning a hypothesis with large excess. Consequently, for a class of size $m$ the sharp interval-based expected-regret factor is $1-1/m$; its worst case under the cap is $1-1/H$. The PAC tolerance floor has no such factor. These statements must not be substituted for one another.

Returning an arbitrary POVM or a mixture outside $\mathcal H$ is not proper learning. In particular, the nonlinear risk of an averaged measurement need not equal the average of the hypotheses' risks. The results here do not claim lower bounds for that different output model.

## 4. Three access models

| Access | What one arrival supplies | What can happen later |
| --- | --- | --- |
| Passive single-copy examples | A random $x$ and one $\rho_x$ | The same label may reappear naturally; it cannot be requested. |
| Grouped $r$-copy examples | A random $x$ and $\rho_x^{\otimes r}$ | A later random group may repeat $x$; the learner cannot ask for an extra group there. |
| Context re-preparation | A random $x$ followed by a requested number of independent copies of $\rho_x$ | The requested copies are an additional source capability, and each is charged. |

For grouped access the source state is

$$
\Omega_\rho^{(r)}=\frac1M\sum_{x=1}^M |x\rangle\langle x|\otimes\rho_x^{\otimes r}.
$$

$G$ groups contain $rG$ physical output copies. A cap of $r$ copies **per arrival** is not a cap of $r$ copies over a context's entire lifetime: natural repeated labels can provide more. Accordingly, the grouped-access distortion floor is a support-independent limit. At a fixed finite $M$, sufficiently many random groups can reveal additional information through repeated labels.

Context re-preparation means obtaining fresh copies from a source, not cloning the one already supplied. A protocol with a finite expected number of re-prepared copies and an unbounded copy-count tail is also distinct from a hard cap of $r$ copies per arrival.

## 5. Moments and full quantum information

For each hypothesis, push the uniform context distribution through its loss:

$$
\mu_h^\rho=\frac1M\sum_{x=1}^M\delta_{\ell_h(x)}.
$$

Then

$$
R_a(h;\rho)=\frac1a\log\int_0^1e^{au}\,d\mu_h^\rho(u).
$$

With $r$ copies at one context, measuring the same hypothesis on those copies gives IID conditional Bernoulli losses. For $j\leq r$,

$$
\mathbb E\!\left[\prod_{i=1}^{j}Y_{h,i}\right]
=\int_0^1u^j\,d\mu_h^\rho(u).
$$

This provides an upper-bound method using the first $r$ loss moments. The algebraic fact that an $r$-copy observable has an expectation polynomial of degree at most $r$ in the state, and that polynomial state functionals can be represented on multiple copies, is established background; see [Brun (2004)](https://arxiv.org/abs/quant-ph/0401067).

Equal scalar loss moments alone do **not** imply indistinguishability against arbitrary quantum measurements. The lower bounds require an explicit source construction whose entire averaged tensor-product state agrees whenever every context has limited occupancy. That stronger equality, rather than a restriction on the learner's measurement choice, is what protects the lower bound against collective processing.

## 6. Resources and scope

The primary complexity is the number of passive output copies. Known hypothesis measurements are operations available to the learner; their circuit cost is not claimed to be constant in a generic implementation. If one measurement costs $T_\Pi$ elementary operations, the direct upper construction incurs that cost for every example it measures, in addition to processing and storing its classical labels and outcomes. Hypothesis descriptions, polynomial coefficients, measurement work registers, and classical records are resources of that implementation.

For fixed class size and fixed frontier parameters, the collision-based upper construction can measure each example immediately and retain only classical data. It needs no QRAM and no coherent source oracle. In a batch of $n$ examples its label-and-outcome storage is $O(n\log M)$ bits, apart from the known measurement implementation and fixed-parameter coefficient precision. A dictionary implementation takes expected $O(n)$ word operations per batch; bit costs depend on the representation of labels and the dictionary used.

The present results concern proper agnostic learning, uniform IID contexts, arbitrary fixed mixed-state output tables, and finite known classes. They do not establish a computational quantum advantage, a claim for every structured or realizable source family, or a bound for nonuniform and temporally drifting context distributions.

The passive classical-quantum setting is shared with [Fanizza, Quek, and Rosati (2024)](https://doi.org/10.1103/PRXQuantum.5.020367). Nonlinear tilted objectives are studied by [Qiu, Pira, and Rebentrost](https://arxiv.org/abs/2508.21369). The account here isolates repeatability and quantifies the access-dependent distortion; it does not replace their models by a chosen-input oracle.
