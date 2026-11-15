# What the repeatability frontier means

The learning objective determines which features of a quantum-data source must be accessible. For a known projector-valued hypothesis, write

$$
\ell_h(x)=1-\mathrm{Tr}[\Pi_h(x)\rho(x)],\qquad
R_a(h)=\frac1a\log\mathbb E_x e^{a\ell_h(x)},\qquad a>0.
$$

Ordinary mean loss depends linearly on each conditional state. Tilted risk also depends on how its Born probability varies between contexts. The frontier quantifies how accurately a learner can resolve that additional dependence using passive examples. The source returns a random context and one copy of its fixed conditional state on each draw; repeated contexts can occur naturally. It does not promise a fresh copy of a context chosen by the learner.

## Accuracy determines the required repetition level

Let $`\Gamma_r(a)`$ be the largest $`a^{-1}`$-scaled log expectation-ratio gap between probability laws on $`[0,1]`$ whose moments through degree $`r`$ agree, as defined in [the moment frontier](moment_frontier.md). Equivalently, it is the smallest $`a^{-1}`$-scaled logarithmic multiplicative error of a degree-$`r`$ polynomial envelope of $`e^{ap}`$. These are inherited approximation-theoretic descriptions of the same scalar quantity.

For every fixed integer $`k\geq1`$, the strict interval

$$
\Gamma_k(a)<\epsilon<\Gamma_{k-1}(a)
$$

has worst-case proper-learning source cost

$$
N_{\min}(M)=\Theta_{a,\epsilon,H,\delta}\left(M^{1-1/k}\right).
$$

Here the input distribution is uniform on a known $`M`$-point support, the conditional-state table is unknown and fixed, the finite class size $`H\geq2`$ and failure probability $`0\lt \delta\lt 1/2`$ are fixed, and $`M`$ grows. The upper bound holds for each fixed finite class. The lower bound is witnessed by a particular two-hypothesis class on a four-dimensional output space; it is not a lower bound for every class.

For example, at $`a=1`$, the first thresholds give the following strict intervals. Decimal values are numerical evaluations, not exact endpoint statements.

| Excess-risk tolerance | Needed collision level | Dependence on support size |
| --- | --- | --- |
| $`0.12330156\ldots\lt \epsilon\lt 1`$ | One observation per effective example | $`\Theta(1)`$ |
| $`0.01029531\ldots\lt \epsilon\lt 0.12330156\ldots`$ | Two observations of one context | $`\Theta(M^{1/2})`$ |
| $`0.00064456\ldots\lt \epsilon\lt 0.01029531\ldots`$ | Three observations of one context | $`\Theta(M^{2/3})`$ |

The exponent changes because a new moment becomes necessary to separate decisions at the requested accuracy. A $`k`$-fold repeated context first becomes available at the scale $`M^{1-1/k}`$. A polynomial envelope shows that this much conditional information is sufficient, up to the strict accuracy margin. Matching moments show it is necessary in the worst case. Constants can grow strongly as a tolerance approaches a threshold; the theorem does not locate finite-$`M`$ crossover points.

## The target is a nonlinear function of a probability

A single projector measurement gives a Bernoulli loss outcome $`B`$ with conditional mean $`\ell_h(x)`$. Exponentiating that outcome does not give an unbiased observation of the target exponential:

$$
\mathbb E[e^{aB}\mid x]
=1+(e^a-1)\ell_h(x),
\qquad
e^{a\mathbb E[B\mid x]}=e^{a\ell_h(x)}.
$$

The first expression remains affine in the conditional state. The distinction matters whenever the intended learning criterion is exponential in the conditional Born probability. Repeated preparations or structural information can supply the missing conditional information. Changing the objective to an exponential of the observed outcome defines a different statistical task.

This is a precision statement, not an assertion that any nonzero tilt requires support-dependent samples. The first threshold is the inherited logarithmic Specht ratio:

$$
\Gamma_1(a)
=\frac1a\log\frac{e^a-1}{a}-\frac1a+\frac1{e^a-1}
=\frac a8-\frac{a^3}{576}+O(a^5).
$$

At tolerances above this threshold, first-moment information is enough for proper selection. At finer fixed tolerances the worst-case source must supply repetitions. This explains why a sufficient learning guarantee that ties tilt to its error tolerance can coexist with a repetition lower bound for a fixed tilt resolved more accurately. The published small-tilt results of Qiu, Pira and Rebentrost are compared on their stated terms in [related work](../references/related_work.md).

## Replay changes source access

Chosen-input replay supplies fresh preparations of the same conditional state. It permits direct construction of the repeated-context observations without waiting for passive collisions, removing the support-size dependence for fixed parameters. It does not manufacture copies of an unknown received state. A hard cap of $`r`$ preparations per source event and an unbounded random count with finite expectation are also different resources; [replay and resources](replay_and_resources.md) keeps them separate.

Uniform contexts play a substantive role in the passive upper bound. A context-label-symmetric collision rule selects an exactly uniform repeated context. Independent batches therefore yield independent effective examples for every fixed state table. For a nonuniform law, ordinary collision selection reweights a context according to a higher power of its probability, so this argument does not transfer unchanged.

Every consumed source output is counted, including samples that do not contribute a useful collision. Classical records of contexts and outcomes, projector implementation, processing time, and any quantum waiting memory must also be charged. The support exponent alone is not a complete experimental cost model.

## What is quantum about the statement

The model allows quantum outputs, incompatible hypothesis measurements, and arbitrary collective processing. The lower bound excludes a collective quantum shortcut around the need for repeated contexts. Its witness nevertheless uses commuting two-qubit states, so the obstruction already exists in a classical population of conditional Bernoulli variables.

For a fixed finite class, one can allocate independent sample batches to hypotheses, measure every arrival immediately, and keep classical context/outcome records until suitable repetitions appear. This achieves the same power of $`M`$ as the quantum upper bound. Collective quantum ERM can be an additional tool for class-size dependence, but that ingredient and its guarantees are inherited. No quantum processing speedup is claimed for the support-size staircase.

The exact statement is limited to proper selection, fixed parameters, arbitrary fixed tables, and strict intervals between adjacent thresholds. It does not settle critical equality cases, unrestricted improper prediction, nonuniform or smooth sources, or simultaneous limits in tilt, accuracy, class size and moment degree. Its practical consequence is a quantitative choice: resolve a nonlinear risk only to a tolerance supported by the available conditional information, obtain the required passive repetitions, or explicitly provide replay or additional source structure.
