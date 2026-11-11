---
declaration: section
origin: cited
lean: Cslib.Logic.CLL.CutAdmissibleAt, Cslib.Logic.CLL.CutAdmissibleBelow, Cslib.Logic.CLL.splitHead, Cslib.Logic.CLL.splitAdd, Cslib.Logic.CLL.Proof.questMulticutAx, Cslib.Logic.CLL.Proof.questMulticut
statement: formalized
proof: formalized
---

# Source exponential multicut for the locked CLL calculus

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html).

## Cut admissibility at a fixed proposition

Cut admissibility at a fixed proposition `a`: for any list sequents `Γ`, `Δ`, given
cut-free proofs of `a ::ₘ Γ` and `a⫠ ::ₘ Δ`, produce a cut-free proof of
`(Γ : Sequent Atom) + Δ`.

Formalized by `Cslib.Logic.CLL.CutAdmissibleAt`, an abbreviation declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#cut-admissible-at).

## Cut admissibility below a size bound

The outer induction hypothesis for cut admissibility: for all propositions `a` with
`sizeOf a < bound`, cut is admissible at `a`.

Formalized by `Cslib.Logic.CLL.CutAdmissibleBelow`, an abbreviation declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#cut-admissible-below).

## Locating a selected question mark or a residual head

Locate a selected question mark or a residual head using `Sequent.splitReplicateCons`.

Formalized by `Cslib.Logic.CLL.splitHead`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#split-head).

## Splitting replicated question marks across two summands

Split replicated question marks across two arbitrary multiset summands.

Formalized by `Cslib.Logic.CLL.splitAdd`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#split-add).

## Axiom case of the exponential multicut

Ax case for `questMulticut`: the selected dual question mark is one of the copies of `a⫠`.
This isolates the recursive branch from the plain-term outer proof.

Formalized by `Cslib.Logic.CLL.Proof.questMulticutAx`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#quest-multicut-ax).

## Exponential multicut against replicated question marks

Exponential/multicut helper: given `p : CF⇓(a ::ₘ Γ)` (the "substitutend") and
`q : CF⇓(Multiset.replicate n (ʔ(a⫠)) + Δ)` (the "supply" with `n` selected dual question marks),
produce `CF⇓((Γ : Sequent) + Δ)`.

Formalized by `Cslib.Logic.CLL.Proof.questMulticut`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/Multicut.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/Multicut.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html#quest-multicut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Source exponential multicut for the locked CLL calculus](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-exponential-multicut-for-the-locked-cll-c)
