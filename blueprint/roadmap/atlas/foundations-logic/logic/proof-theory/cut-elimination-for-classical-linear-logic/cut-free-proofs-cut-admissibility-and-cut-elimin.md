---
declaration: section
origin: cited
lean: Cslib.Logic.CLL.Proof.IsCutFree, Cslib.Logic.CLL.Proof.isCutFree_iff_cutFree, Cslib.Logic.CLL.Proof.IsCutFree.rec, Cslib.Logic.CLL.Proof.isCutFree_rwConclusion, Cslib.Logic.CLL.CF, Cslib.Logic.CLL.CF.Proof, Cslib.Logic.CLL.CF.Proof.rwConclusion, Cslib.Logic.CLL.CF.Proof.ax
statement: formalized
proof: formalized
---

# Cut-free proofs, cut admissibility, and cut elimination for classical linear logic

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html).

## CLL

## Cut-freeness of a proof

A proof is cut-free if it does not contain any applications of rule cut.

Formalized by `Cslib.Logic.CLL.Proof.IsCutFree`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#is-cut-free).

## Cut-freeness predicate agrees with the Boolean check

The source predicate agrees exactly with the pinned Boolean predicate.

Formalized by `Cslib.Logic.CLL.Proof.isCutFree_iff_cutFree`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#is-cut-free-iff-cut-free).

## Recursor for cut-free proofs

Recursor for cut-free proofs: never sees the `cut` case.

Formalized by `Cslib.Logic.CLL.Proof.IsCutFree.rec`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#rec).

## Conclusion transport preserves cut-freeness

Transporting a conclusion preserves cut-freeness.

Formalized by `Cslib.Logic.CLL.Proof.isCutFree_rwConclusion`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#is-cut-free-rw-conclusion).

## Cut-free fragment of classical linear logic

Tag for the cut-free fragment of CLL.

Formalized by `Cslib.Logic.CLL.CF`, an opaque constant declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#cf).

## Proofs of the cut-free inference system

Proofs in the CF inference system.

Formalized by `Cslib.Logic.CLL.CF.Proof`, an abbreviation declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#proof).

## Rewriting the conclusion of a cut-free proof

Rewrites the conclusion of a cut-free proof.
If `h` is omitted, tries to prove the equality using `grind only [multiset]`.

Formalized by `Cslib.Logic.CLL.CF.Proof.rwConclusion`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#rw-conclusion).

## Axiom rule of the cut-free system

Axiom for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.ax`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#ax).

## Unit rule $1$ of the cut-free system

Rule `1` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.one`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#one).

## Top rule of the cut-free system

Rule `⊤` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.top`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#top).

## Bottom rule of the cut-free system

Rule `⊥` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.bot`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#bot).

## Par rule of the cut-free system

Rule `⅋` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.parr`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#parr).

## Tensor rule of the cut-free system

Rule `⊗` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.tensor`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#tensor).

## First plus rule of the cut-free system

Rule `⊕₁` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.oplus₁`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#oplus).

## Second plus rule of the cut-free system

Rule `⊕₂` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.oplus₂`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#oplus-2).

## With rule of the cut-free system

Rule `&` for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.with`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#with).

## Dereliction rule of the cut-free system

Rule `?` (dereliction) for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.quest`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#quest).

## Weakening rule of the cut-free system

Rule `?` (weaken) for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.weaken`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#weaken).

## Contraction rule of the cut-free system

Rule `?` (contract) for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.contract`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#contract).

## Promotion rule of the cut-free system

Rule `!` (bang/promotion) for CF.

Formalized by `Cslib.Logic.CLL.CF.Proof.bang`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#bang).

## Weakening by a list of question-mark propositions

Given a list of `ʔ`-propositions `Γ`, transforms a cut-free proof of `Δ` into a proof of `Γ + Δ`
via weakening.

Formalized by `Cslib.Logic.CLL.CF.Proof.weakenContext`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#weaken-context).

## Contraction of a duplicated question-mark context

Given a list of `ʔ`-propositions `Γ`, transforms a proof of `Γ + Γ + Δ` into a proof of `Γ + Δ`
via contraction.

Formalized by `Cslib.Logic.CLL.CF.Proof.contractContext`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#contract-context).

## Empty sum of sequents has an empty right summand

An empty sum has an empty right residual context.

Formalized by `Cslib.Logic.CLL.Sequent.eq_zero_of_zero_eq_add`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#eq-zero-of-zero-eq-add).

## Case split on an equation of cons sequents

Distinguish a principal selected occurrence using decidable equality.
Given `a ::ₘ Γ = b ::ₘ Δ`, either `a = b` and `Γ = Δ`, or `a ≠ b` and the propositions are swapped:
`Γ = b ::ₘ Λ` and `Δ = a ::ₘ Λ` for some `Λ`.
The tail `Δ` can be an arbitrary multiset; the residual list is obtained from `Γ`.

Formalized by `Cslib.Logic.CLL.Sequent.splitCons`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#split-cons).

## Locating a head proposition in a sum of sequents

Given `a ::ₘ Γ = (Δ : Sequent) + Θ`, locate `a` in either `Δ` or `Θ` and
erase it from that summand, returning the residual list.

Formalized by `Cslib.Logic.CLL.Sequent.splitConsAdd`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#split-cons-add).

## Case split of a cons against replicated copies

Given `Multiset.replicate n a + Γ = b ::ₘ Δ`, either the head `b` is one of the
`n` copies of `a` (so `b = a` and the tail is `replicate (n-1) a + Γ`), or `b` belongs to
`Γ` (so `Δ = Multiset.replicate n a + Γ'` where `Γ = b ::ₘ Γ'`).
The tail `Δ` can be an arbitrary multiset; the residual list is obtained from `Γ`.

Formalized by `Cslib.Logic.CLL.Sequent.splitReplicateCons`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#split-replicate-cons).

## Splitting replicated copies across a sum of sequents

Given `Multiset.replicate n a + Γ = (Δ : Sequent) + Θ`, split the `n` copies of `a`
between `Δ` and `Θ`, returning counts `k` and `l` and residual lists.

Formalized by `Cslib.Logic.CLL.Sequent.splitReplicateAdd`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutFree.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutFree.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html#split-replicate-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cut-free proofs, cut admissibility, and cut elimination for classical linear logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/cut-free-proofs-cut-admissibility-and-cut-elimin)
