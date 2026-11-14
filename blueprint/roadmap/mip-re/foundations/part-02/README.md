---
navigation: transparent
---

# The Mermin–Peres strategy is… to Game description

- [The Mermin–Peres strategy is perfect](lem-mermin-peres.md)
- [Perfect strategies from operator solutions](thm-lcs-perfect.md)

## Distance measures

- [Normalized Hilbert–Schmidt norm](def-hs-norm.md)
- [POVM distance](def-distance.md)
- [State-dependent POVM distance](def-state-distance.md)

Comments. This is *not* Definition [POVM distance](def-distance.md), and the difference is not presentational. Definition [POVM distance](def-distance.md) is the normalized Hilbert–Schmidt distance, which is the distance of a *synchronous* strategy — there the state is the normalized trace itself, which is why `MIPRE/Foundations/Closeness.lean` is the calculus of that one. The appendix of the Pauli basis test (Section [The quantum low individual degree test](../../background-results/README.md)) works throughout with the state-dependent distance above, on a bipartite state that is fixed by context, and every $\approx_\delta$ in that section is this one.

Two departures from the paper's own definition ((AuditSync26), `qld-prelim.tex`), both in the direction of a stronger statement. The paper writes $\leq O(\delta)$ *inside* the relation; here the relation is an inequality against $\delta$ and the constants appear in the lemmas that produce them, so Lemma [Averaging preserves closeness](../../background-results/part-02/lem-qld-averaging.md) preserves $\delta$ exactly and Lemma [From POVM elements to generalized observables](../../background-results/part-02/lem-qld-povm-to-obs.md) gives exactly $\left\vert {{\mathcal{A}}} \right\vert\delta$. And the paper defines $\approx_\delta$ only for question-indexed operators, using the answer-indexed form without comment; both are defined here.

- [Cross-party state-dependent distance](def-cross-distance.md)

Comments. This is the $\simeq_\delta$ of the Pauli appendix, and it is not Definition [State-dependent POVM distance](def-state-distance.md): that one compares two families of operators on the *same* factor, which is what the orthonormalization step of Corollary [Orthonormalization from consistency](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2095) needs, whereas every consistency statement of Lemma [Win implications](../../background-results/part-02/lem-qld-win.md) compares one player's operator with the *other* player's. The paper uses both symbols and says the two are interchangeable up to Fact `fact:agreement`; the formalization keeps them apart, because the conversion is the factor $2$ of [(1)](def-cross-distance.md) and it is better spent once than assumed throughout.

Inequality [(1)](def-cross-distance.md) is the whole analytic content of the file (`MIPRE/Foundations/CrossConsistency.lean`): expand each square, and the two diagonal sums are at most one because a POVM element satisfies $A^\dagger A = A^2 \leq A$ (`POVM.mul_self_le_self`) and the elements sum to the identity. **No projectivity is used**, so the inequality holds for arbitrary POVM strategies. On the paper's route projectivity arrives only later, through Corollary [Orthonormalization from consistency](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2095); the formalized route assumes it from the start, Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) being stated for projective strategies.

Two things the formalization needs that the paper leaves implicit. First, what a subtest buys is not that its decider *equals* an agreement predicate but that *accepting implies agreeing*: a real decider checks the answer formats first and rejects an ill-formatted pair even when the post-processings agree. So the readings that coarse-grain the answers may send an ill-formatted answer anywhere — $0$, here — and the implication is all `one_sub_sum_bornProb_le_condFail` asks. Second, “divided by the probability that the subtest is selected” needs no injectivity: the subtests of the Pauli basis test are indexed by the verifier's content and several contents give the same question pair, a $(\textsc{Pauli}, W)$ question reading none of it, so the hypothesis is a condition on the push-forward (`sum_condFail_le_of_pushforward`).

`xStateDist_obsOf_le` is Lemma [From POVM elements to generalized observables](../../background-results/part-02/lem-qld-povm-to-obs.md) across the two parties, with the same proof and the same factor $\left\vert {{\mathcal{A}}} \right\vert$: the appendix needs it to pass from a two-outcome coarse-graining of a point measurement to the $\pm 1$-observable it defines, and Definition [State-dependent POVM distance](def-state-distance.md)'s version compares the wrong pair.

**The order reversal, and where the sign comes from.** One algebraic rule is proved here rather than inlined at its two uses, because the paper's own correction note on Lemma [Signed commutation of the point observables](../../background-results/part-02/lem-qld-obs-commutation.md) records two displays that had it backwards. If $A \otimes {I} \simeq {I} \otimes A'$ and $B \otimes {I} \simeq {I} \otimes B'$ then

$$
AB \otimes {I} \;\simeq\; {I} \otimes B'A'\;,\qquad\text{(2)}
$$

Bob's factors in the *reverse* order, at the sum of the two deviations (`xNorm_mul_le_one`; `xNorm_mul_le` carries operator-norm bounds $K$ and $L$ in front of them). The proof is the split $AB \otimes {I} - {I} \otimes B'A' = (A \otimes {I})(B \otimes {I} - {I} \otimes B') + ({I} \otimes B')(A \otimes {I} - {I} \otimes A')$, and the reversal is exactly the step that commutes $A \otimes {I}$ past ${I} \otimes B'$ to factor the second summand: it puts $B'$ to the *left* of $A'$. Applying it in both orders and cancelling Bob's two products gives the form the anticommuting case of Lemma [Signed commutation of the point observables](../../background-results/part-02/lem-qld-obs-commutation.md) consumes,

$$
\left\| {(AB + BA) \otimes {I} |\psi\rangle} \right\| \;\leq\; 2 \left\| {(A \otimes {I} - {I} \otimes A')|\psi\rangle} \right\|
+ 2 \left\| {(B \otimes {I} - {I} \otimes B')|\psi\rangle} \right\|
+ \left\| {{I} \otimes (A'B' + B'A') |\psi\rangle} \right\|\;,\qquad\text{(3)}
$$

`norm_stateVec_anticomm_le`: an anticommutation on Bob's side transfers to Alice's. The two reversals do not cancel each other, because what sits between them is a *sum*. Both statements are on the unsquared deviation, since the triangle inequality is what the argument uses; `xSqNorm_mul_le_one` squares the first at the usual cost of a factor two.

Each operator in sight has to be a contraction, and for the $\pm 1$-observable of a two-outcome POVM that is `POVM.sub_mul_self_le_one`, which needs the observable written as a *difference* of two POVM elements rather than as the weighted sum $\sum_a (-1)^a M_a$ that `obsOf` produces. `obs2` is that difference and `obsOf_sgn_eq_obs2` identifies the two, so a consumer can quote whichever form its input is stated in.

**The swap, and the commutator form.** Two more entries serve the appendix's commutation step. `norm_stateVec_comm_le` is (3) with a commutator in the middle instead of an anticommutator — the same split, Bob's two products cancelling either way. And `snorm_swapVec_aOp_sub_bOp` exchanges the two sides of a cross-party deviation, which is what lets a lemma proved for Alice's factor be applied to Bob's: the clean statement is at the level of vectors, $(X \otimes Y)\,\mathrm{swap}|\psi\rangle = \mathrm{swap}\,(Y \otimes X)|\psi\rangle$, and everything else follows by linearity. On the paper's route Corollary [Orthonormalization from consistency](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2095) produces a projective measurement on *Alice's* factor only, so the commutation analysis below is run on Bob's observables and carried back; that swap is the bridge. The formalized route assumes the first player's measurements projective from the outset and uses the swap in the same way.

## The expanded state

- [The expanded state, and an inert ancilla](def-expanded-state.md)

Comments. Formalized in `MIPRE/Foundations/Expanded.lean`. This is the bookkeeping of the appendix's `sec:expanding`, isolated from the Pauli test: items 3 and 4 are what let a bound proved *before* the expansion be used *after* it, and they are why the expansion stage costs exactly the constant of Lemma [Signed commutation of the point observables](../../background-results/part-02/lem-qld-obs-commutation.md) and nothing more. The re-bipartition is the point — the ancilla halves are split between the parties, which is what makes the ancilla observables tied together — and it is why the statements are about $|\psi\rangle \otimes |e\rangle$ rather than about a tensor power.

**Born probabilities factorize, and that is where data processing lives.** The consistency half of the expansion stage is about a measurement of *product* form, and what it needs is that its Born probabilities split: $\langle\hat\psi| (M \otimes N) \otimes (M' \otimes N') |\hat\psi\rangle = \langle\psi| M \otimes M' |\psi\rangle \cdot \langlee| N \otimes N' |e\rangle$ (`bornProb_expVec_kron`; only the ancilla's two operators need be positive, which is what makes their quadratic form real so the real part of the product splits). `POVM.kron` is the product measurement, and `sum_bornProb_le_map` is the data-processing inequality that holds: coarse-graining *both* players the same way can only increase the probability that they agree.

That last one is stated at the Born level deliberately. The state-dependent distance has **no** data-processing inequality — NW19 states theirs for $\simeq_\delta$ and the remark following it gives a counterexample for $\approx_\delta$ — so every coarse-graining in the appendix is taken on Born probabilities and converted once, at the end, by [(1)](def-cross-distance.md). A formalization that reached for the $\approx$ form would be proving something false.

## Naimark dilation against a fixed state

- [Naimark dilation of a question-indexed family](lem-naimark-dilation.md)

Comments. Formalized in `MIPRE/Foundations/Dilation.lean`, extracted from the repetition development where it was written for `lem:povm-value-eq`. Its other consumers are Lemma [Direct Magic Square anticommutation — what the pipeline actually needs](../../background-results/part-01/lem-ms-direct-anticomm.md), which dilates the Magic Square's six constraint POVMs against one shared ancilla, and Theorem [Exact linearity from approximate linearity](../../background-results/part-02/thm-linearity.md).

## The commutation analysis

- [Commutation analysis](lem-commutation-analysis.md)

Comments. Formalized in `MIPRE/Foundations/Commutation.lean`. This is the paper's `lem:commutation-analysis` (`games.tex`), and it is the only step of the Pauli appendix that genuinely uses projectivity of a measurement.

**Proved for abstract families in one algebra.** The two parties enter only through four hypotheses — the two factors commute, and Bob's two marginals multiply to the joint element in either order — so `commutation_analysis_abstract` is stated for families in a single matrix algebra and the bipartite version is its instance. That is not tidiness: stating it with $\otimes$ in the hypotheses made the unifier's work quadratic in the number of rewrites and the proof timed out; in one algebra it elaborates in seconds.

**No square root, and the constant is exact.** Every step is a triangle inequality or an operator-norm bound, so $16\delta$ is what the argument gives. The last step of the appendix's commuting case is also exact: expanding a two-outcome observable as ${I} - 2 M_1$, the commutator of two of them is *four times* the commutator of the two $M_1$'s (`obs2_commutator_eq`), because the identity commutes with everything — a factor $16$ in the squared norm and no approximation.

## Attaching a projection, and the pasting lemma

- [Cool closeness fact, and the marginal step](lem-cool-closeness-fact.md)

Comments. Formalized in `MIPRE/Foundations/Commutation.lean` (the fact) and `MIPRE/Foundations/Pasting.lean` (the marginal step). This is the paper's `lem:cool-closeness-fact` in the partition form its round-11 repair gives it, and the partition form is the point: the consumer applies it to the $q$ fibres of an outcome map at once, and the single-subset form would cost a factor $q$ there.

- [Pasting, the two-measurement case](lem-pasting-updated.md)

Comments. Formalized in `MIPRE/Foundations/Pasting.lean`. This is NW19's Fact 4.35, the paper's `lem:pasting-updated` (`games.tex`), at $k = 2$; the paper's reduction of general $k$ to $k = 2$ is an induction that adds nothing, and the consumer (Lemma [Pairs of lines](../../background-results/part-02/lem-qld-pairs-of-lines.md)) needs $k = 2$ only.

**Two hypotheses of the paper's statement are absent, and both are absences rather than gaps.** First, the inner family is assumed *projective*; the paper allows a POVM there, and then the two diagonal sums of the commutator expansion are only approximately one, which is what its appeal to Fact 4.31 of (NW19) repairs. With projectivity they are exactly one and that fact is not needed at all — the consumer's inner family is a line measurement, which is projective. Second, the cross-party self-consistency of $G$ at the *fine* level is a hypothesis here, where the paper derives it from the backwards consistency and Alice's self-consistency and pays a further $\varepsilon$ for the passage from the fibres to the fine family. The consumer has the fine-level relation directly, as item 1 of Lemma [Expanded line measurements](../../background-results/part-02/lem-qld-expanded-lines.md), so the derivation would be work spent to weaken a hypothesis that is already met. Neither change touches the conclusion.

**The collision term is a hypothesis of the abstract lemma and a lemma of its own for the product case.** That split is what keeps the analytic core free of the question distribution: the core needs only that the off-diagonal cloud terms are small in total, and the product-distribution bridge (`sum_collisionTerm_le`) is where uniformity of the probe and the separating property of the outcome map are used.

**Constants.** $32\delta$ rather than the $16\delta$ of Lemma [Commutation analysis](lem-commutation-analysis.md) because the two marginal hypotheses enter that lemma as a single $\delta$, here instantiated at their sum. Nothing in the chain is a per-outcome estimate, so no constant depends on $|{\mathcal{C}}|$ or on $|{\mathcal{B}}|$.

## Generalized Pauli observables

- [Generalized Pauli observables in characteristic two](def-generalized-pauli.md)

Source. The pinned paper (AuditSync26), `preliminaries.tex`, `sec:generalized-pauli`: `eq:pauli-fp` and its $\mathbb{F}_q$ analogue, `eq:twisted-fq`, `eq:pauli-product-power`, `eq:pauli-obs-proj` and `eq:pauli-inversion-0`. The cancellation behind the inversion is the paper's `lem:cancellation` (Fact 3.2 of (NW19)).

Comments. The formalization is `MIPRE/Foundations/Weyl.lean`. It is the half of the Pauli basis test's infrastructure that was missing: `MIPRE/LCS/Pauli.lean` is the $2 \times 2$ Pauli matrices for the Magic Square, and what the expansion stage of Remark [How the soundness proof of Theorem Pauli basis test / quantum low individual degree test is organized](../../background-results/README.md) and its swap isometry both run on is this $\mathbb{F}_q$ Weyl system. Three points, two of them restrictions stated so that no later statement is read as more general than it is.

**Characteristic two only.** The paper gives the construction over $\mathbb{F}_p$ with phases $\omega = e^{2\pi i/p}$ and then specializes; this is the $p = 2$ case throughout, where $\omega = -1$ and every phase is the real sign `MIPRE.sgn`. Nothing is lost here: the test's parameters are admissible by hypothesis, which means $q = 2^k$, and no consumer instantiates it elsewhere. What it buys is that the operators are self-adjoint *involutions* rather than order-$p$ unitaries — so they are genuine $\pm 1$-observables, and item 2 above is where the paper needs $(\tau^W(a))^p = {I}$.

**One matrix, not an iterated Kronecker product.** $(\mathbb{C}^q)^{\otimes n}$ is presented as matrices indexed by the functions $n \to \mathbb{F}_q$, which *is* $\mathbb{F}_q^n$, so $\tau^W(a)$ is a single matrix and the $n$-register statements are the one-register statements with no associativity bookkeeping. The index set $n$ is an arbitrary finite type rather than $\{1, \ldots, n\}$, which is what lets the test use it at $n = \{0,1\}^m$ — the indexing of $\mathbb{F}_q^M$, $M = 2^m$, that Definition [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md) already uses.

**The cancellation lemma needed a generalization, not a port.** The identity behind the inversion in [(10)](def-generalized-pauli.md) is that a nontrivial sign character of $\mathbb{F}_q^n$ sums to zero, and that is the index-two kernel of a nonzero $\mathbb{F}_2$-linear functional. The repository had that count only for a functional on a field *extension* (`card_filter_ker_mul`); the proof uses nothing but the module structure and a vector off the kernel, so it is now stated for any finite $\mathbb{F}$-vector space (`card_filter_ker_mul'`), with the field-extension form as the instance. The paper's own correction note on `lem:cancellation` warns that the ambient space must be a subspace over the *base* field and that the statement is false over a subfield; here the space is all of $\mathbb{F}_q^n$ over $\mathbb{F}_2$, so there is nothing to check.

**The spectral theory is proved once, for both families.** The only properties of a family that [(10)](def-generalized-pauli.md) and [(11)](def-generalized-pauli.md) use are the three of `IsWeylFamily`: it represents the additive group, its operators are self-adjoint, and the identity sits at $0$. So the projectors are built by [(9)](def-generalized-pauli.md) from any such family and the statements hold for both, which means the paper's Fourier transform (`eq:fourier-f`) conjugating $\tau^Z$ into $\tau^X$ is *not needed* to reach the $X$-side projectors. That is worth avoiding: the transform carries a $q^{-1/2}$, and a square root in matrix entries costs far more in Lean than it does on paper.

Two of the identities turn out to need even less. The expansion of an operator in its own projectors, and the line average [(11)](def-generalized-pauli.md), use *no* group law at all — they are Fourier inversion on the index group and hold for an arbitrary family. What the group law buys is that the projectors are mutually *orthogonal*, which is what makes them a measurement rather than a resolution.

Equation [(11)](def-generalized-pauli.md) is the identity Lemma [Expanded point measurements](../../background-results/part-02/lem-qld-expanded-points.md) averages to, at $v = {\mathrm{ind}}_m(u)$.

- [The maximally entangled state of the Weyl system](def-weyl-epr.md)

Comments. Formalized in `MIPRE/Foundations/WeylEPR.lean`. The stabilizer relation of [(12)](def-weyl-epr.md) at $M = \tau^W(a)$ is what the expansion stage of Remark [How the soundness proof of Theorem Pauli basis test / quantum low individual degree test is organized](../../background-results/README.md) runs on: its expanded state adjoins $|\textsc{EPR}_q\rangle^{\otimes M}$ to each player, and the sign $(-1)^{\gamma(\omega)}$ that the strategy's own observables carry is cancelled against one the *ancilla* observables carry, for which the two ancilla halves must be tied together.

This is the second dividend of characteristic two, after the operators being involutions. Over $\mathbb{F}_p$ for odd $p$ the transpose of $\tau^Z(b)$ is $\tau^Z(b)$ but its conjugate is $\tau^Z(-b)$, and the bookkeeping reappears; here every entry is real and the transpose is the identity map on the whole family, projectors included (`stateVec_epr_proj`, which needs only that the family is symmetric).

[$\bullet$ easy]

- [Qudits are qubits, in characteristic two](lem-pauli-binary.md)

Comments. Formalized in `MIPRE/Foundations/WeylBinary.lean`; this is the paper's `lem:pauli-binary` (`preliminaries.tex`), which is what makes the Pauli basis test a self-test for *qubit* Pauli observables and $|\textsc{EPR}_2\rangle$, as its `cor:pauli-binary` states.

**A relabelling, not an isometry.** The paper builds an isometry $\theta : \mathbb{C}^q \to (\mathbb{C}^2)^{\otimes k}$ and states the conclusion as $\tau^W_u = \phi^\dagger (\bigotimes_{i,j} \sigma^W_{u_{ij}}) \phi$. Here both systems are matrices indexed by a finite set — $\mathbb{F}_q^L$ on one side, $\mathbb{F}_2^{L \times k}$ on the other — and $\phi$ is a bijection *of those index sets*, so conjugating by the corresponding permutation unitary is `Matrix.submatrix` along $\phi$ and no unitary has to be constructed. That is the same simplification as presenting $(\mathbb{C}^q)^{\otimes n}$ as one matrix rather than an iterated Kronecker product, and it is why the four items are four short calculations.

**What “these are qubit Paulis” means here.** The target is the Weyl system at $\mathbb{F} = \mathbb{F}_2$ and index set $L \times k$, whose matrices are indexed by $\mathbb{F}_2^{L \times k}$ — the computational basis of $(\mathbb{C}^2)^{\otimes L k}$. That the operators really are the tensor products of single-qubit Paulis is then a statement *inside* that system, and it is checked rather than read off the encoding: the form is the plain dot product (`trDot_two`, the field trace of a one-dimensional extension being the identity), its character is a product over the qubits (`sgn_trDot_two`), and each operator's entries factor accordingly (`wZ_two_diag` on the diagonal, `wX_two_apply` everywhere). The paper's $\bigotimes_{i=1}^L \bigotimes_{j=1}^k \sigma^W_{u_{ij}}$ is that factorization.

**The oddness of $k$ is inherited, not needed.** Every statement above holds for any self-dual basis, given as a hypothesis; only the existence clause asks $k$ to be odd, and that is the restriction of Lemma [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md)'s formalized half, not of this lemma. The paper's admissible sizes satisfy it.

- [Inconsistency](def-inconsistency.md)

Comments. This is Definition 4.8 of (JNVWY21qld), in the two-space form used by Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md). It is a different notion from the POVM distance of Definition [POVM distance](def-distance.md): consistency compares two families across the two factors of the state, whereas $\approx_\delta$ compares them as operator families.

**Remark (The POVM distance and the state).** Definition [POVM distance](def-distance.md) is *state-independent*, whereas the companion paper's $\approx_\delta$ (`games.tex`) is the state-dependent quantity $\mathop{\mathbb{E}}_{x \sim \mu} \sum_a \left\| {(M^x_a - N^x_a)|\psi\rangle} \right\|^2$. For a *synchronous* strategy the two agree. The state is then the maximally entangled state on $\mathbb{C}^d \otimes \mathbb{C}^d$, and for it $\langle\psi| (A^\dagger A) \otimes I |\psi\rangle = \operatorname{tr}(A^\dagger A)/d = \left\| {A} \right\|_{hs}^2$, so Definition [POVM distance](def-distance.md) *is* the state-dependent distance at the tracial state. Every formalized consumer of Definition [POVM distance](def-distance.md) is synchronous, and the soundness of oracularization (Lemma [Soundness of oracularization, at the level of games](../../structure-of-the-proof/part-06/lem-oracular-soundness.md)) reads it that way. For a general bipartite strategy the two notions differ, so a chapter 3 consumer that is not synchronous will need the state-dependent notion added rather than this one reused.

- [Closeness from two disagreements](lem-hs-closeness.md)
- [Close measurements have close values](lem-close-measurements-close-values.md)

Comments. The square root is spent here and nowhere else in the soundness of oracularization; everything before it, including Lemma [Closeness from two disagreements](lem-hs-closeness.md), is linear. That is what repair 1 of Remark [What the audit changed in oracularization](../../structure-of-the-proof/README.md) is about.

## Computability conventions

Turing machines are represented by their Gödel numbers; in Lean the intended model is Mathlib's `Nat.Partrec.Code`, with $\phi_e$ the partial function computed by code $e$ and “$e$ halts on empty input” meaning $(\texttt{e.eval } 0).\texttt{Dom}$. Running times are counted as in (MNY); polynomial-time computability of a function of strings and integers means time polynomial in the lengths of the string inputs and in $\log$ of the integer inputs, unless an integer is explicitly given in unary.

- [Recursively enumerable](def-re.md)

In Lean (`MIPRE.IsRE`) membership in $L$ is Mathlib's `REPred`, the domain of a partial computable function; equivalently (`MIPRE.isRE_iff`), $L$ is the halting set of a well-scoped program of the ambient model (Section [Efficient computability toolkit](../../computability/README.md)) on encoded strings, which is the form in which the compressibility criterion (Lemma [Compressibility criterion](../../computability/lem-compressible-criterion.md)) consumes recursive enumerability. The completeness of the halting problem is Theorem [Turing](../../background-results/part-03/thm-halting-undecidable.md), not part of the definition.

- [Succinct description](def-succinct.md)
- [Game description](def-game-description.md)
