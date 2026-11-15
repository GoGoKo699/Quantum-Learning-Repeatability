# Thirty milestones for quantum learning repeatability

This map connects the source model, the exact moment thresholds, and the matching passive-sampling theorem. Its sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, especially Chapters 1–3. The [anchor bridge](anchor.md) identifies the relevant textbook foundations. The project supplies its own approximation, probability, and learning arguments; those arguments are not attributed to the textbook.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background moves from an individual state and measurement to the full statistical learning experiment. The narrative moves from a small equal-mean example through the scalar and quantum proof mechanisms to the complete sample law, its resource requirements, and its limits. This allocation leaves most of the map for the connection that the project establishes while making its data-access assumptions understandable before the theorem appears.

Each milestone records a conceptual target and its source dependencies. The map covers the load-bearing ideas, rather than every specialist lemma. Scientific claims and complete proofs remain in the [canonical scientific account](../science/README.md).

## Background and preliminaries — local objects to the complete experiment

### M01 — A conditional quantum state

**Phase:** Background/preliminaries.

**Central question:** What does the source assign to one classical context?

**Understanding target:** Interpret a density operator as the complete state supplied at a fixed context, including the possibility of a mixed state. Distinguish the state from a preparation description and from a measurement outcome.

**Dependencies and story role:** This is the local starting point; no earlier milestone is required. It introduces the object that remains fixed whenever its context is revisited.

**Conceptual connection:** The table entry $\rho_x$ is a physical statistical object, not a classical list of its matrix entries given to the learner.

**Sources:** Watrous, Chapter 2, “Basic notions of quantum information,” for states; [model](../science/model.md), “Source and hypotheses.”

### M02 — A known projector and its Born loss

**Phase:** Background/preliminaries.

**Central question:** How does a known measurement hypothesis assign a loss to an unknown state?

**Understanding target:** Read $\ell_h(x)=1-\operatorname{Tr}[\Pi_h(x)\rho_x]$ as a probability in $[0,1]$. Distinguish knowledge of a hypothesis measurement from knowledge of its probability on the unknown source.

**Dependencies and story role:** Uses M01 and adds the local measurement through which a hypothesis is evaluated.

**Conceptual connection:** Projector-valued hypotheses make the learning task concrete without giving the learner a preparation oracle or a description of $\rho_x$.

**Sources:** Watrous, Chapters 1–2, for operators, trace, and measurements; [model](../science/model.md), “Source and hypotheses” and “Tilted population risk.”

### M03 — One specimen and a conditional mean

**Phase:** Background/preliminaries.

**Central question:** Which information does one binary measurement outcome supply about its context?

**Understanding target:** Separate the observed bit $Y$ from the conditional probability $\ell_h(x)=\mathbb E[Y\mid X=x]$. Explain why applying a nonlinear function to the bit need not estimate that function of the probability.

**Dependencies and story role:** Uses M02. It isolates the local statistical distinction that eventually creates the repetition cost.

**Conceptual connection:** The objective concerns variation of conditional Born means across contexts, while measurements provide random outcomes within contexts.

**Sources:** Watrous, Chapter 1, for probability and expectation, and Chapter 2, for outcome probabilities; [model](../science/model.md), “Tilted population risk.”

### M04 — Independent copies and tensor products

**Phase:** Background/preliminaries.

**Central question:** What changes when the source supplies several independent specimens at the same context?

**Understanding target:** Interpret $\rho_x^{\otimes r}$ as repeated independent preparation. Distinguish this access from one specimen, a correlated multi-system state, or a procedure that clones an unknown received state.

**Dependencies and story role:** Uses M01–M03. It joins the state and outcome descriptions into the local repeated-observation experiment.

**Conceptual connection:** Independent conditional preparations are what make products of measurement outcomes encode powers of a Born probability.

**Sources:** Watrous, Chapters 1–2, for tensor products and composite registers; [model](../science/model.md), “Three access models” and “Moments and full quantum information.”

### M05 — Classical labels and a frozen quantum source

**Phase:** Background/preliminaries.

**Central question:** How are random context labels and their fixed conditional states combined into training data?

**Understanding target:** Read the classical-quantum source $M^{-1}\sum_x|x\rangle\langle x|\otimes\rho_x$ and its independent repetitions. Explain that the table is fixed even though the sampled label changes, and that revisiting a label does not redraw its hidden table entry.

**Dependencies and story role:** Uses M01 and M04. It moves from one context to the full source without yet specifying a learning objective.

**Conceptual connection:** Fixed conditional states permit useful repeated labels; uniform random labels determine how long such repetitions take to obtain.

**Sources:** Watrous, Chapter 2, for classical and quantum registers; [model](../science/model.md), “Source and hypotheses.”

### M06 — Passive, grouped, and replay access

**Phase:** Background/preliminaries.

**Central question:** Which kinds of repetition can a source actually supply?

**Understanding target:** Distinguish a naturally repeated passive label, an arrival containing a fixed number of same-context copies, and an interface that can re-prepare a sampled context on request. Keep a cap per arrival separate from the total copies accumulated after later visits.

**Dependencies and story role:** Uses M04–M05. It fixes the source capability before comparing algorithms or sample counts.

**Conceptual connection:** A stronger source can remove a waiting cost; it does not follow merely from the learner having a quantum processor.

**Sources:** Watrous, Chapter 2, for preparation and register operations; [model](../science/model.md), “Three access models”; [replay and resources](../science/replay_and_resources.md), “Conditional replay is an additional source capability.”

### M07 — Mean risk and tilted population risk

**Phase:** Background/preliminaries.

**Central question:** What does a positive tilt ask the learner to resolve beyond the mean loss?

**Understanding target:** Interpret $R_a(h)=a^{-1}\log\mathbb E_x e^{a\ell_h(x)}$ for $a>0$, its mean-loss limit, and its emphasis on larger conditional losses. Preserve the order of the conditional mean, exponential, context average, and logarithm.

**Dependencies and story role:** Uses M03 and M05. It connects the local measurement probability to the global objective.

**Conceptual connection:** The additional nonlinear dependence is the feature whose resolution will be indexed by the moment thresholds.

**Sources:** Watrous, Chapter 1, for expectation and convexity foundations; [model](../science/model.md), “Tilted population risk”; [interpretation](../science/interpretation.md), “The target is a nonlinear function of a probability.”

### M08 — Proper selection and the accuracy convention

**Phase:** Background/preliminaries.

**Central question:** What counts as a successful learning output in this project?

**Understanding target:** Explain proper selection from the supplied finite class, population excess risk, and the PAC failure probability. Distinguish the excess of the returned hypothesis from expected regret and from the nonlinear risk of a measurement outside the class.

**Dependencies and story role:** Uses M02 and M07. It specifies the decision and guarantee against which the converse and construction will be compared.

**Conceptual connection:** A lower bound for proper selection does not automatically apply to unrestricted improper prediction, and a bound on expected regret is not a PAC guarantee.

**Sources:** Watrous, Chapter 1, for probability and randomized decisions; [model](../science/model.md), “Learning guarantee and quantifiers” and “PAC excess and expected regret are different.”

### M09 — Same-context products reveal moments

**Phase:** Background/preliminaries.

**Central question:** Why do repeated conditional observations supply powers of a probability?

**Understanding target:** Explain $\mathbb E[\prod_{i=1}^{j}Y_i\mid x]=\ell_h(x)^j$ under conditional independence, then average over contexts. Recognize the first $r$ loss moments as accessible from grouped $r$-copy examples.

**Dependencies and story role:** Uses M03–M04 and M07. It converts physical repetition into the scalar information used by approximation theory.

**Conceptual connection:** Products of observations connect tensor-copy access to moments of the distribution of conditional losses.

**Sources:** Watrous, Chapters 1–2, for independent random variables and composite systems; [model](../science/model.md), “Moments and full quantum information”; [moment frontier](../science/moment_frontier.md), “From an envelope to a learning guarantee.”

### M10 — Indistinguishability before any measurement

**Phase:** Background/preliminaries.

**Central question:** What kind of equality defeats every collective learning strategy?

**Understanding target:** Distinguish equality of selected scalar statistics from equality of the full supplied density operators. Explain why identical training states have identical outcome laws under every allowed measurement, and how trace distance controls distinguishing success when equality holds only on a high-probability event.

**Dependencies and story role:** Uses M02, M04–M05. It supplies the measurement-independent language required for the converse.

**Conceptual connection:** The proof permits arbitrary quantum processing; it obtains its bound by comparing inputs rather than restricting the learner's measurement choices.

**Sources:** Watrous, Chapter 3, “Similarity and distance among states and channels,” for state discrimination and trace distance; [passive frontier](../science/passive_frontier.md), “Equality before a k-fold repeat.”

### M11 — Moments and a positive polynomial envelope

**Phase:** Background/preliminaries.

**Central question:** How can finitely many moments control a nonlinear exponential mean?

**Understanding target:** Interpret a degree-$r$ polynomial as a linear combination of the moments in M09. Understand the pointwise envelope $e^{au}\le p(u)\le K e^{au}$ as a multiplicative comparison that survives averaging.

**Dependencies and story role:** Uses M07 and M09. It introduces the classical approximation interface that links repetition to risk accuracy.

**Conceptual connection:** The envelope's positivity is a statement about its values on $[0,1]$; it does not assert that every coefficient or every associated measurement operator is positive.

**Sources:** Watrous, Chapter 1, for linear functionals, norms, and convexity foundations; [moment frontier](../science/moment_frontier.md), “Equivalent positive polynomial envelope” and “Relative approximation, strictness, and convergence.” The project supplies the approximation argument.

### M12 — The complete learning experiment

**Phase:** Background/preliminaries.

**Central question:** Which assumptions must be held together before the repeatability frontier has a definite meaning?

**Understanding target:** Assemble the fixed unknown state table, known uniform support, finite class-size cap, positive loss tilt, proper PAC decision, passive source access, and unrestricted quantum processing. Distinguish sample complexity from the cost of implementing a known measurement.

**Dependencies and story role:** Integrates M01–M11 and completes the background phase. It identifies the whole experiment to which the narrative applies.

**Conceptual connection:** The contribution concerns the information supplied by this source at a requested accuracy; changing its access, output model, or limiting regime changes the problem.

**Sources:** Watrous, Chapters 1–3, for the combined register, measurement, and discrimination framework; [model](../science/model.md); [scientific route](../science/README.md).

## Narrative and innovation — local mechanisms to the full frontier

### M13 — Equal mean losses can favor different hypotheses

**Phase:** Narrative/innovation.

**Central question:** What does the smallest useful example reveal about nonlinear risk?

**Understanding target:** Compare a hypothesis with losses $0$ and $1$ at equally likely contexts to one with constant loss $1/2$. Explain why their means agree while positive-tilt risks differ, and why the single-outcome substitution from M03 misses this distinction.

**Dependencies and story role:** Uses M07, M11–M12. It begins the narrative with a concrete need for information beyond the first moment.

**Conceptual connection:** A variance-sensitive decision creates the foothold for a quantitative moment hierarchy; the example alone is not the full converse.

**Sources:** Watrous, Chapters 1–2, for expectation and Born probabilities; [story](story.md); [moment frontier](../science/moment_frontier.md), “The one-copy value and small-tilt hierarchy.”

### M14 — Moment twins define the unresolved risk gap

**Phase:** Narrative/innovation.

**Central question:** How large can a tilted-risk difference remain when the first $r$ moments agree?

**Understanding target:** Interpret $\kappa_r(a)$ as the largest ratio of exponential means over matching-moment laws and $\Gamma_r(a)=a^{-1}\log\kappa_r(a)$ as the corresponding risk gap. Explain why exchanging the two laws removes a sign ambiguity.

**Dependencies and story role:** Uses M09, M11 and M13. It replaces an isolated example by the exact scalar quantity that will control the theorem.

**Conceptual connection:** The hidden distinction is quantified in the same loss units as the requested PAC tolerance.

**Sources:** Watrous, Chapter 1, for probability measures and linear expectation foundations; [moment frontier](../science/moment_frontier.md), “A sharp moment-ratio constant.”

### M15 — The converse and the envelope are dual descriptions

**Phase:** Narrative/innovation.

**Central question:** Why does the largest moment-twin gap equal the best positive polynomial-envelope distortion?

**Understanding target:** Follow the easy integration inequality and the converse finite-grid linear-program argument, including the compactness step that produces a continuum envelope. Identify this scalar duality as inherited mathematics, not a new quantum effect.

**Dependencies and story role:** Uses M11 and M14. It makes one exact threshold serve both the lower and upper proofs.

**Conceptual connection:** Matching moments erase every degree-$r$ polynomial difference, while a positive envelope bounds what remains of the exponential objective.

**Sources:** Watrous, Chapter 1, for finite-dimensional linear and convex foundations; [moment frontier](../science/moment_frontier.md), Theorem 1 and its explicit attribution; [related work](../references/related_work.md), “Classical conditional learning and approximation theory.”

### M16 — The explicit first threshold

**Phase:** Narrative/innovation.

**Central question:** What accuracy can first-moment information support at a fixed tilt?

**Understanding target:** Explain the extremal constant-loss and endpoint-Bernoulli laws at a common mean, the maximizing mean, and the explicit value of $\Gamma_1(a)$. Recognize its logarithmic Specht-ratio origin and its leading behavior $a/8$.

**Dependencies and story role:** Uses M13–M15. It turns the abstract frontier into a concrete scale for the first change in passive sample behavior.

**Conceptual connection:** The small-tilt regime is an accuracy comparison, rather than a statement that every nonzero tilt already forces support-dependent samples.

**Sources:** Watrous, Chapter 1, for convexity and expectation foundations; [moment frontier](../science/moment_frontier.md), Proposition 3; [interpretation](../science/interpretation.md), “The target is a nonlinear function of a probability.”

### M17 — More moments reduce the ambiguity

**Phase:** Narrative/innovation.

**Central question:** How do successive repetition levels change the threshold sequence?

**Understanding target:** Explain positivity, strict decrease, and convergence of $\Gamma_r(a)$, and the role of relative approximation in those properties. Interpret the fixed-degree small-tilt asymptotic while keeping that limit separate from the fixed-parameter support-size limit.

**Dependencies and story role:** Uses M14–M16. It establishes that adjacent accuracy intervals form a genuine ordered hierarchy.

**Conceptual connection:** Higher moments provide progressively finer control of the nonlinear objective; they do not create a uniform joint-limit theorem in all parameters.

**Sources:** Watrous, Chapter 1, for norms and finite-dimensional linear algebra; [moment frontier](../science/moment_frontier.md), Propositions 2 and 4. The project supplies the approximation, weighted-alternation and shifted-Chebyshev arguments.

### M18 — A signed polynomial is a bounded estimator

**Phase:** Narrative/innovation.

**Central question:** How is an envelope implemented without treating its coefficients as probabilities?

**Understanding target:** Construct the polynomial statistic from products of same-context loss bits. Explain its unbiased expectation and coefficient-norm bound, and distinguish a bounded Hermitian observable from a positive effect or projector.

**Dependencies and story role:** Uses M02, M09 and M15. It supplies a physically valid upper-bound primitive.

**Conceptual connection:** Pointwise positivity of the scalar polynomial does not justify an uncharged binary measurement; a shift, rescaling, or dilation has its own implementation and accuracy obligations.

**Sources:** Watrous, Chapters 1–2, for operator norms, effects, and measurements; [passive frontier](../science/passive_frontier.md), “A signed polynomial is an observable, not automatically an effect”; [moment frontier](../science/moment_frontier.md), “From an envelope to a learning guarantee.”

### M19 — One envelope distortion is enough for selection

**Phase:** Narrative/innovation.

**Central question:** How does minimizing a surrogate yield the required proper-risk decision?

**Understanding target:** Follow the chain comparing the selected exponential mean, its polynomial mean, and the optimal hypothesis's polynomial mean. Explain why the distortion enters once as $\Gamma_r(a)$, with a separate estimation slack, rather than twice.

**Dependencies and story role:** Uses M08, M15 and M18. It connects local estimation to the actual learning output.

**Conceptual connection:** An estimator is useful here because it preserves a near-optimal decision at the stated tolerance, not merely because it approximates a scalar function.

**Sources:** Watrous, Chapter 1, for inequalities and probabilistic estimation; [moment frontier](../science/moment_frontier.md), “From an envelope to a learning guarantee”; [passive frontier](../science/passive_frontier.md), “Finite estimates and a fixed sample budget.”

### M20 — Two frozen worlds encode opposite decisions

**Phase:** Narrative/innovation.

**Central question:** How can scalar moment twins become legitimate quantum learning sources?

**Understanding target:** Build the two-qubit diagonal product-state table from latent probabilities drawn once per context. Identify the two constant commuting projector hypotheses and the swapped worlds in which their optimal choices differ.

**Dependencies and story role:** Uses M01–M02, M05 and M14. It starts the converse by constructing an allowed source rather than assuming a restriction on measurements.

**Conceptual connection:** A random table prior is a proof device; each table sampled from it is fixed during the learner's experiment.

**Sources:** Watrous, Chapter 2, for diagonal states and tensor-product registers; [passive frontier](../science/passive_frontier.md), “Two moment-matched worlds”; [moment frontier](../science/moment_frontier.md), “Why the same constant is unavoidable.”

### M21 — Low occupancy hides the entire training state

**Phase:** Narrative/innovation.

**Central question:** Why can no collective quantum measurement distinguish the two worlds before sufficient repetitions occur?

**Understanding target:** Explain why entries of an $s$-copy conditional state are degree-$s$ polynomials in its latent probability. Use the matching moments and independence between frozen context entries to obtain equality of the complete prior-averaged training states when every occupancy is small enough.

**Dependencies and story role:** Uses M04, M10 and M20. It provides the measurement-independent core of the lower bound.

**Conceptual connection:** Equality of all supplied quantum information is stronger than equality of the particular loss moments used by the upper algorithm.

**Sources:** Watrous, Chapters 2–3, for composite states and operational indistinguishability; [passive frontier](../science/passive_frontier.md), “Equality before a k-fold repeat.”

### M22 — The first informative collision sets a lower scale

**Phase:** Narrative/innovation.

**Central question:** At what sample scale can a context first occur often enough to expose the hidden distinction?

**Understanding target:** Interpret the bound $\Pr(\text{a k-fold repeat})\leq\binom nk M^{1-k}$ for $k\geq2$. Derive the scale $M^{1-1/k}$ and explain how a rare bad-label event bounds distinguishing advantage.

**Dependencies and story role:** Uses M05, M10 and M21. It turns full-state equality into a support-dependent information bound.

**Conceptual connection:** The familiar collision exponent enters through random source labels, not through a limit on quantum circuit power.

**Sources:** Watrous, Chapter 1, for probability bounds, and Chapter 3, for state discrimination; [passive frontier](../science/passive_frontier.md), “Equality before a k-fold repeat.”

### M23 — From a prior comparison to a fixed-source PAC lower bound

**Phase:** Narrative/innovation.

**Central question:** Why does the argument establish a failure for a fixed unknown source, rather than a different resampling model?

**Understanding target:** Combine concentration of the table's exponential means, a strict risk gap above $\epsilon$, and the world-identification bound. Explain how averaging a purported guarantee over table priors leads to a contradiction and therefore to a violating deterministic table.

**Dependencies and story role:** Uses M08 and M20–M22. It closes the lower proof under the original task's quantifiers.

**Conceptual connection:** Concentration controls the target decision, while indistinguishability controls the observations; both are needed to transfer a moment-twin prior into a proper-learning converse.

**Sources:** Watrous, Chapter 1, for probability foundations, and Chapter 3, for distinguishing success; [passive frontier](../science/passive_frontier.md), “Fixed-table risks and the PAC contradiction,” for the concentration argument.

### M24 — A collision batch succeeds at the matching scale

**Phase:** Narrative/innovation.

**Central question:** Is the lower collision scale also enough to obtain a useful repeated context?

**Understanding target:** Follow the first- and second-moment calculation for the number of equal-label $k$-subsets in a batch of order $M^{1-1/k}$. Explain why overlap terms vanish at fixed $k$ and why the chance of success stays bounded away from zero.

**Dependencies and story role:** Uses M22. It begins the constructive half at the same support exponent as the converse.

**Conceptual connection:** A constant batch-success probability supplies repeated conditional observations without requesting a context or discarding their acquisition cost.

**Sources:** Watrous, Chapter 1, for expectations and probability inequalities; [passive frontier](../science/passive_frontier.md), “A constant-probability k-collision.” The specific occupancy proof is supplied there.

### M25 — Extraction preserves the right context law

**Phase:** Narrative/innovation.

**Central question:** Why does a selected repeated context represent the original uniform population?

**Understanding target:** Explain label-permutation symmetry, outcome-independent selection, and independent data batches. Distinguish uniformity of labels from symmetry of unknown states, and explain why selected groups remain IID for each fixed source table.

**Dependencies and story role:** Uses M05, M09 and M24. It verifies the statistical interface between collision finding and risk estimation.

**Conceptual connection:** A repeated context is useful only if its selection law matches the risk's averaging law; nonuniform context distributions do not inherit this property automatically.

**Sources:** Watrous, Chapters 1–2, for conditional probability and independent preparations; [passive frontier](../science/passive_frontier.md), “Uniformity and independence are preserved”; [interpretation](../science/interpretation.md), “Replay changes source access.”

### M26 — Confidence and the full fixed sample budget

**Phase:** Narrative/innovation.

**Central question:** How are enough useful groups obtained within a prescribed total budget?

**Understanding target:** Separate collision-batch failures from errors in the bounded polynomial estimates. Explain the fixed number of batches, the confidence allocation across hypotheses, and why every source output is counted even when it yields no selected group.

**Dependencies and story role:** Uses M18–M19 and M24–M25. It completes the upper construction as a fixed-budget learning algorithm rather than an expected waiting-time argument.

**Conceptual connection:** The theorem's constant may depend on the tilt, class cap, confidence, degree, and threshold margin even though its power of $M$ is sharp.

**Sources:** Watrous, Chapter 1, for probability notation; [passive frontier](../science/passive_frontier.md), “Finite estimates and a fixed sample budget,” for bounded-variable concentration and confidence bookkeeping; [replay and resources](../science/replay_and_resources.md), “Physical and computational resources.”

### M27 — The accuracy-dependent passive staircase

**Phase:** Narrative/innovation.

**Central question:** How do the exact thresholds and the collision scale combine into one theorem?

**Understanding target:** Explain why $\Gamma_k(a)<\epsilon<\Gamma_{k-1}(a)$ gives worst-case sample complexity $\Theta(M^{1-1/k})$. State the fixed-parameter limiting order, the confidence and proper-selection conditions, and the distinction between an upper bound for every finite class and a lower bound witnessed by one two-hypothesis class.

**Dependencies and story role:** Integrates M14–M26. It is the global synthesis of the main scientific proof.

**Conceptual connection:** Required risk precision selects the needed moment level; passive repetition then assigns its source-cost exponent. Neither half alone establishes the complete law.

**Sources:** Watrous, Chapters 1–3, for the combined probability, quantum-input, and discrimination framework; [passive frontier](../science/passive_frontier.md), theorem and “What the theorem establishes”; [interpretation](../science/interpretation.md), “Accuracy determines the required repetition level.”

### M28 — Grouped access has an accuracy floor, with distinct decision metrics

**Phase:** Narrative/innovation.

**Central question:** What remains ambiguous when each random arrival already supplies $r$ copies?

**Understanding target:** Explain the support-independent PAC boundary at $\Gamma_r(a)$, why later natural visits prevent it from being an eternal impossibility for a fixed finite support, and why the worst-case expected-regret factor $1-1/H$ describes a different guarantee.

**Dependencies and story role:** Uses M06, M08, M15, M19 and M23. It places the passive staircase inside the broader access comparison without changing the output metric silently.

**Conceptual connection:** The number supplied per event, the support over which uniformity is required, and the decision criterion jointly determine the meaning of a copy threshold.

**Sources:** Watrous, Chapters 1–3, for randomized decisions, composite states, and discrimination; [moment frontier](../science/moment_frontier.md), “Why the same constant is unavoidable” and “Expected regret has a different exact floor”; [replay and resources](../science/replay_and_resources.md), “A finite replica cap removes the support dependence above its threshold.”

### M29 — Replay and random depth change the source bill

**Phase:** Narrative/innovation.

**Central question:** What does deliberate repetition remove, and which preparation costs remain?

**Understanding target:** Explain how replay bypasses collision waiting, how the Poisson product identity estimates the exponential with random depth, and why a finite expected count differs from a hard copy cap. Account for the initial specimen even when the random depth is zero, giving expected preparations $a+e^{-a}$ under the stated natural-event interface.

**Dependencies and story role:** Uses M04, M06, M09 and M28. It completes the source-access comparison with its physical preparation obligations.

**Conceptual connection:** A repeated-input capability can alter support dependence without cloning a specimen or providing free data loading; the probability-generating-function identity is inherited classical machinery.

**Sources:** Watrous, Chapters 1–2, for probability, expectation, and preparation/register foundations; [replay and resources](../science/replay_and_resources.md), “An exact exponential estimator with random replica depth,” “The initial specimen is still charged,” and “Finite-depth truncation.” The project supplies and attributes the Poisson construction.

### M30 — The full scientific consequence and its boundaries

**Phase:** Narrative/innovation.

**Central question:** What can now be concluded about quantum learning from passive data, and which conclusions require a different theorem?

**Understanding target:** Give a connected account of the exact accuracy thresholds, the matched support exponent, the impossibility of a collective-processing shortcut, and the fixed-class immediate-measurement upper bound. Keep source copies, classical records, optional quantum storage, and known measurement circuits visible. State the limits at critical accuracies, nonuniform or drifting sources, structured families, improper outputs, and joint parameter limits.

**Dependencies and story role:** Integrates M12 and M27–M29, with the preceding proof mechanisms and access comparisons. It completes the narrative as one scientific contribution.

**Conceptual connection:** The result is a quantitative law about available conditional information and requested decision precision. Its commuting lower-bound witness and classical statistical ingredients delimit the claim; they do not establish a quantum processing speedup or a hardware crossover.

**Sources:** Watrous, Chapters 1–3, as the common quantum-information foundation; [interpretation](../science/interpretation.md); [replay and resources](../science/replay_and_resources.md), “Physical and computational resources” and “Interpretation limits”; [related work](../references/related_work.md), “Scope and limitation.”
