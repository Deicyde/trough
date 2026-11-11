---
declaration: section
origin: cited
lean: Cslib.Logic.CLL.CF.Proof.equivCutFreeProof, Cslib.Logic.CLL.Proof.cut_elim_list, Cslib.Logic.CLL.Proof.cut_elim, Cslib.Logic.CLL.CutFreeProof.cutAdmList
statement: formalized
proof: formalized
---

# Canonical pinned API for the upstream CLL cut-elimination port

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html).

## Equivalence of source and pinned cut-free proof bundles

Source and pinned cut-free proof bundles contain the same proof values.

Formalized by `Cslib.Logic.CLL.CF.Proof.equivCutFreeProof`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html#equiv-cut-free-proof).

## Cut-free original proof from an explicit list presentation

Compute a cut-free original CLL proof using an explicit list presentation.

Formalized by `Cslib.Logic.CLL.Proof.cut_elim_list`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html#cut-elim-list).

## Cut elimination for original classical linear logic proofs

Every original CLL proof has a cut-free original proof of the same sequent.
This wrapper uses classical atom equality and a classical list representative.

Formalized by `Cslib.Logic.CLL.Proof.cut_elim`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html#cut-elim).

## Cut admissibility in the pinned bundle with list tails

Cut admissibility in the existing pinned bundle, with explicit list tails.

Formalized by `Cslib.Logic.CLL.CutFreeProof.cutAdmList`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LinearLogic/CLL/CutEliminationBridge.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html#cut-adm-list).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Canonical pinned API for the upstream CLL cut-elimination port](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/canonical-pinned-api-for-the-upstream-cll-cut-el)
