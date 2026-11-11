---
declaration: section
origin: cited
lean: List.allQuest, Cslib.Logic.CLL.Sequent.allQuest_coe, Cslib.Logic.CLL.Sequent.allQuest_zero, Cslib.Logic.CLL.Sequent.allQuest_cons_iff, Cslib.Logic.CLL.Sequent.allQuest_quest_cons, Cslib.Logic.CLL.Sequent.not_allQuest_bang_cons, Cslib.Logic.CLL.Sequent.allQuest_add, Cslib.Logic.CLL.Proof.height
statement: formalized
proof: formalized
---

# Prerequisite APIs for the frozen cut-elimination source port

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html).

## Sequent

## Check that every proposition in a list is a why-not proposition

Checks that all propositions in a list are question marks (`ʔ`).

Formalized by `List.allQuest`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest).

## Why-not check agrees on a list and its multiset

Checking a list context agrees with checking its multiset coercion.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_coe`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest-coe).

## Empty sequent consists of question-mark propositions

The empty sequent consists of `ʔ`-propositions.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_zero`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest-zero).

## A cons sequent is all question marks iff its head and tail are

A cons sequent consists of `ʔ`-propositions exactly when its head and tail do.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_cons_iff`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest-cons-iff).

## A question-mark head does not change the all-question-mark property

Adding a `ʔ`-proposition preserves and reflects `allQuest`.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_quest_cons`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest-quest-cons).

## A sequent headed by a bang proposition is not all question marks

A sequent containing a `!`-proposition cannot satisfy `allQuest`.

Formalized by `Cslib.Logic.CLL.Sequent.not_allQuest_bang_cons`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#not-all-quest-bang-cons).

## A sum of sequents is all question marks iff both summands are

A sum consists of `ʔ`-propositions exactly when both summands do.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_add`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#all-quest-add).

## Height of a classical linear logic proof

Height of a proof.

Formalized by `Cslib.Logic.CLL.Proof.height`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#height).

## Conclusion transport preserves proof height

Transporting a conclusion preserves proof height.

Formalized by `Cslib.Logic.CLL.Proof.rwConclusion_height`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#rw-conclusion-height).

## Conclusion transport preserves the Boolean cut-free check

Conclusion transport preserves the pinned Boolean cut-free check.

Formalized by `Cslib.Logic.CLL.Proof.cutFree_rwConclusion`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutCompat.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html#cut-free-rw-conclusion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prerequisite APIs for the frozen cut-elimination source port](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/prerequisite-apis-for-the-frozen-cut-elimination)
