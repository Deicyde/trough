---
declaration: section
origin: cited
lean: Cslib.Logic.CLL.Sequent.presentSumForCut, Cslib.Logic.CLL.Sequent.presentTailForCut, Cslib.Logic.CLL.Sequent.splitCutHead, Cslib.Logic.CLL.Proof.CutPrincipal, Cslib.Logic.CLL.Proof.cutStep, Cslib.Logic.CLL.Proof.bangCutAdm, Cslib.Logic.CLL.Proof.questCutAdm, Cslib.Logic.CLL.Proof.cutPrincipal
statement: formalized
proof: formalized
---

# Source cut elimination for the locked CLL calculus

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html).

## List presentations of two summands from a supplied list

Present both summands using only the supplied list.

Formalized by `Cslib.Logic.CLL.Sequent.presentSumForCut`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#present-sum-for-cut).

## List presentation of a tail without choosing a representative

Present a tail without choosing a multiset representative.

Formalized by `Cslib.Logic.CLL.Sequent.presentTailForCut`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#present-tail-for-cut).

## Splitting a selected occurrence against a rule head

Split a selected occurrence against a rule head; the rule tail can be a multiset.

Formalized by `Cslib.Logic.CLL.Sequent.splitCutHead`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#split-cut-head).

## Principal shapes of a cut-free proof at the cut proposition

The shape of a cut-free proof when the cut proposition is in principal position.
Each constructor corresponds to a rule whose conclusion matches the cut proposition.
Axioms are handled separately in `cutStep`. Tensor carries explicit presentations
of both premises' residual contexts.

Formalized by `Cslib.Logic.CLL.Proof.CutPrincipal`, an inductive type declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-principal).

## Cut step exposing a principal rule or commuting the cut

Decompose a cut against a cut-free proof: either expose a principal rule matching
the cut proposition, or commute the cut through one inference (non-principal case).
Every recursive call is on a strictly shorter supplying derivation.

Formalized by `Cslib.Logic.CLL.Proof.cutStep`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-step).

## Cut admissibility for a bang proposition

Cut a bang proposition by commuting through its supplying proof to an axiom or promotion.
At promotion, delegates to `questMulticut` with one selected occurrence.

Formalized by `Cslib.Logic.CLL.Proof.bangCutAdm`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#bang-cut-adm).

## Question-mark cut via the bang case, duality and exchange

Reverse the exponential cut orientation using `bangCutAdm`, duality, and exchange.
This is a wrapper, not a recursive call that swaps premises at the same measure.

Formalized by `Cslib.Logic.CLL.Proof.questCutAdm`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#quest-cut-adm).

## Reduction of a cut between matching principal rules

Reduce a pair of principal rules whose conclusions match the cut proposition.
Every recursive call is on a proper subproposition of the original cut proposition,
so termination is guaranteed by proposition size.

Formalized by `Cslib.Logic.CLL.Proof.cutPrincipal`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-principal-2).

## Cut admissibility for non-exponential propositions

Cut admissibility for non-exponential propositions: uses height induction on the
sum of premise heights, with commuting cases for non-principal rules.
Only callable when neither `a` nor `a⫠` is a question mark.

Formalized by `Cslib.Logic.CLL.Proof.cutAdmNonExponential`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-adm-non-exponential).

## Proposition-size induction step for cut admissibility

The proposition-size induction step for cut admissibility.
Dispatches to `bangCutAdm`, `questCutAdm`, or `cutAdmNonExponential` depending on
the top-level connective.

Formalized by `Cslib.Logic.CLL.Proof.cutAdmOfSmaller`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-adm-of-smaller).

## Core cut admissibility procedure on list sequents

The core cut admissibility implementation: given decidable atom equality and explicit
list sequents, combine cut-free proofs of dual distinguished propositions into a cut-free
proof of the sum of their residual sequents. Recurses on proposition size.

Formalized by `Cslib.Logic.CLL.Proof.cutAdmImpl`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-adm-impl).

## Cut admissibility for cut-free classical linear logic proofs

Public entry point for cut admissibility: given cut-free proofs of `a ::ₘ Γ` and
`a⫠ ::ₘ Δ`, produce a cut-free proof of `(Γ : Sequent) + Δ`.

Formalized by `Cslib.Logic.CLL.Proof.cutAdm`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-adm).

## Cut elimination by structural recursion on the proof

Compute cut-free proofs by structural recursion on the original (possibly
non-cut-free) proof. Each case recursively normalises the premises, then uses
`cutAdm` at each cut. The list `Γ` is the explicit sequent for the current subgoal.

Formalized by `Cslib.Logic.CLL.Proof.cutElimAux`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-elim-aux).

## List-based cut elimination in the source calculus

List-based cut elimination with the concrete list presentation explicit.

Formalized by `Cslib.Logic.CLL.Proof.cutElimList`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-elim-list).

## Cut elimination with a noncomputable list presentation

Cut elimination, using a noncomputable list presentation.

Formalized by `Cslib.Logic.CLL.Proof.cutElim`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/CutElimination.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html#cut-elim).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Source cut elimination for the locked CLL calculus](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/proof-theory/cut-elimination-for-classical-linear-logic/source-cut-elimination-for-the-locked-cll-calcul)
