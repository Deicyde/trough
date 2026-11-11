---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.muSat, MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.muCalculusSatDec, MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.mu_calculus_sat_exp_complete
statement: formalized
---

# Satisfiability of the modal μ-calculus

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus/index.html).

## Satisfiability of a closed modal μ-calculus formula

A closed μ-calculus formula is satisfiable: some Kripke model has a world
satisfying it under the empty environment.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.muSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus/index.html#mu-sat).

## Modal μ-calculus satisfiability as a decision problem

Satisfiability of the modal μ-calculus as a decision problem over bitstrings:
the input decodes to a formula token list, which decodes to a formula; the answer
is whether that formula is closed and satisfiable.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.muCalculusSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus/index.html#mu-calculus-sat-dec).

## Satisfiability of a modal μ-calculus formula is EXPTIME-complete

Sources:
D. Kozen, "Results on the propositional μ-calculus", Theoretical Computer Science 27
(1983), 333-354; E. A. Emerson and C. S. Jutla, "Tree automata, μ-calculus and
determinacy", FOCS 1991, 368-377.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MuCalculusEXPTIMEComplete.mu_calculus_sat_exp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MuCalculusEXPTIMECompleteWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus/index.html#mu-calculus-sat-exp-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Satisfiability of the modal μ-calculus](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-of-the-modal-calculus)
