---
navigation: transparent
---

# Nonlocal game to The Magic Square

- [Nonlocal game](def-game.md)
- [Synchronous game](def-sync-game.md)

### Strategies

- [Tensor-product strategy](def-tensor-strategy.md)
- [Synchronous strategy](def-sync-strategy.md)
- [Commuting strategy](def-commuting-strategy.md)

**Remark.** A synchronous strategy (Definition [Synchronous strategy](def-sync-strategy.md)) is exactly the finite-dimensional case ${\mathscr{A}} = \mathbb{C}^{d \times d}$, $\tau = \operatorname{tr}/d$. Via the GNS representation, commuting strategies capture exactly the synchronous commuting-operator correlations of the usual two-prover picture, with Bob's measurements acting in the commutant on $L^2({\mathscr{A}}, \tau)$ — (PSSTW16, Theorem 5.5); see also (Lin23) and (Lin25, Section 3.4).

- [PCC strategy](def-pcc.md)

**Remark (Source PCC and the required representation bridge).** The paper's PCC condition applies to a tensor-product strategy on equal local spaces. Besides projectivity and $[A^x_a,B^y_b]=0$ on the support of the question distribution, it requires each measurement separately to be consistent with itself on the state:

$$
(A^x_a\otimes{I})|\psi\rangle=({I}\otimes A^x_a)|\psi\rangle,
\qquad
(B^y_b\otimes{I})|\psi\rangle=({I}\otimes B^y_b)|\psi\rangle.
$$

These are the conditions of `def:consistent-measurement`, `def:consistent-strategy` and `def:spcc` in the companion `games.tex` (AuditSync26); see also (JNVWY20, Section 5.2). The checked realization in Lemma [Synchronous value lower-bounds the quantum value](lem-sync-le-valstar.md) uses $A=M$ and $B=M^{\mathsf T}$. It preserves probabilities and gives cross-player consistency, but does not establish the displayed same-measurement identities for arbitrary complex $M$, nor does commutation of two matrices imply commutation of one with the transpose of the other.

Consequently Definition [PCC strategy](def-pcc.md) is the current synchronous PCC interface, and using it as an input to the paper's completeness theorems requires a separate *PCC representation bridge*. The forward bridge must preserve all probabilities and support commutation while producing a source PCC strategy. A candidate is to realify each complex projector on dimension $2d$, then use the same real symmetric projectors on both halves of a maximally entangled state. Projectivity, the normalized trace probabilities, the two consistency identities and the symmetry required for SPCC all need verification for that construction; no such bridge is proved here. Any transfer back from source PCC strategies to this synchronous interface also needs its own stated hypotheses and proof. The name PCC in the Lean definition does not discharge either direction. In both interfaces, commutation is required only on question pairs in the support of $\mu$ and is distinct from the commuting-operator model of Definition [Commuting strategy](def-commuting-strategy.md).

### Values

- [Quantum value](def-q-value.md)
- [Synchronous value](def-sync-value.md)
- [Commuting value](def-commuting-value.md)
- [A perfect strategy rejects nothing on the support](lem-perfect-rejects-nothing.md)

Comments. Every completeness argument in the pipeline needs this step — a strategy of value $1$ does not merely win on average, it assigns probability zero to each rejected answer at each question actually asked — and it was used implicitly inside the proof that the value is at most one, without being available as a lemma. It is stated at the generic tracial level, so it serves synchronous and commuting strategies alike.

Two formalization notes. The instance set of the ambient algebra must be exactly the $[\mathrm{Ring}]\,[\mathrm{StarRing}]\,[\mathrm{Module}\ \mathbb{C}]$ of Definition [Commuting strategy](def-commuting-strategy.md): demanding a normed algebra instead sends the elaborator looking for a normed-algebra instance on matrices at every application, which is a `whnf` timeout. And the application to a synchronous strategy goes through the named `value_eq_tracialValue` rather than letting the unifier see through `SyncStrategy.value`, for the same reason.

- [Entanglement requirement](def-ent.md)

### Relationship lemmas

- [Synchronous value lower-bounds the quantum value](lem-sync-le-valstar.md)

The converse direction — every good tensor-product strategy for a synchronous game whose questions carry proportional weight on the diagonal can be rounded to a good synchronous strategy — is the almost-synchronicity theorem, imported as Theorem [Almost-synchronous strategies are near synchronous strategies](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L137). The hypothesis on the diagonal cannot be dropped: without it the two values are unrelated (Remark [The diagonal-weight hypothesis cannot be dropped](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L180)).

- [Synchronous value lower-bounds the commuting value](lem-sync-le-valco.md)

## Linear constraint system games

A well-studied class of nonlocal games arises from systems of linear equations over $\mathbb{F}_2$: the referee asks Alice for a satisfying assignment to a randomly chosen equation and Bob for the value of a randomly chosen variable in it, and checks consistency. The Mermin–Peres magic square is the canonical example. The formalization of this subsection was contributed by Sean Perazzolo (`MIPRE.LCS`); beyond the definitions below it includes observable- and projector-based strategy formalisms and their equivalence, a sum-of-squares decomposition of the loss operators, the extraction of operator identities from perfect play on the EPR state, matrix representations of solution groups, and the magic square as a worked example (`MIPRE.LCS.MagicSquare.merminPeresStrategy`).

- [LCS instance](def-lcs-instance.md)
- [LCS game](def-lcs-game.md)

Comments. The orientation is what makes the game *symmetric in the players*, and it is not cosmetic. A one-directional version — the equation always to Alice, the variable always to Bob — cannot express a statement about both players' variable observables, which is exactly what the Pauli basis test consumes from the Magic Square (Lemma [Direct Magic Square anticommutation — what the pipeline actually needs](../../background-results/part-01/lem-ms-direct-anticomm.md)): Alice would never receive a variable question, so $A^{\textsc{Variable}_j}$ would not exist. It also fixes that lemma's constant, the conditional failures being summed over $2 \sum_i \left\vert {V_i} \right\vert$ oriented incidences rather than $\sum_i \left\vert {V_i} \right\vert$ unoriented ones.

The shape and support checks in the decider are the discipline Definition [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md) learned the hard way: a missing format check made the seeded CL game vacuous and a soundness theorem about it false. The formalization pins each outcome with explicit answers — an accepted pair in each orientation, and one rejected for disagreement, one for parity, one for shape, one for being off support.

- [Solution group](def-solution-group.md)
- [Binary observables](def-observable.md)
- [Observables and projective measurements correspond](lem-observable-projector.md)
- [From an observable strategy to a projective strategy](lem-observable-strategy.md)
- [The Magic Square](def-magic-square.md)
