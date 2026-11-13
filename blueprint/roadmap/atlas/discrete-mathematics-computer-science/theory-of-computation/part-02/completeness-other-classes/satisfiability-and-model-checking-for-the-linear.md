---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuSat, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuValid, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuModelCheck, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuSatDec, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuValidDec, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuModelCheckDec, MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linear_mu_calculus_pspace_complete
statement: formalized
---

# Satisfiability and model checking for the linear-time μ-calculus

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html).

## Satisfiability of a closed linear μ-calculus formula

A closed linear μ-calculus formula is satisfiable: some word and position
satisfy it under the empty environment.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-sat).

## Validity of a closed linear μ-calculus formula

A closed linear μ-calculus formula is valid: every word and position satisfy
it under the empty environment.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuValid`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-valid).

## Linear μ-calculus model checking on a finite Kripke structure

Model checking a linear μ-calculus formula against a finite Kripke structure:
every infinite path `π` from `start` following `edges` satisfies `φ` at
position `0`, where the path turns the structure's valuation `worldVal` into a
word valuation.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuModelCheck`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-model-check).

## Linear μ-calculus satisfiability as a decision problem

Satisfiability of the linear μ-calculus as a decision problem over bitstrings:
the input decodes to a formula token list, which decodes to a formula; the answer
is whether that formula is closed and satisfiable.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-sat-dec).

## Linear μ-calculus validity as a decision problem

Validity of the linear μ-calculus as a decision problem over bitstrings.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuValidDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-valid-dec).

## Linear μ-calculus model checking as a decision problem

Model checking of the linear μ-calculus as a decision problem over bitstrings:
the input decodes to `(n, edges, worldVals, start, tokens)`, where `worldVals`
lists, per world, the atoms true at that world; the answer is whether the
decoded formula is closed, the structure is well-formed and total (every world
has a successor world, so the path quantification is not vacuous at deadlocks),
and every path from `start` satisfies the formula.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linearMuModelCheckDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-model-check-dec).

## The model checking, satisfiability and validity problems of the linear modal μ-calculus are PSPACE-complete

**The model checking, satisfiability and validity problems of the linear modal
μ-calculus are PSPACE-complete**, like for linear temporal logic. Source:
M. Y. Vardi, "A temporal fixpoint calculus", POPL 1988, 250-259; cf. A. P. Sistla
and E. M. Clarke, "The complexity of propositional linear temporal logics",
JACM 32 (1985), 733-749.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.LinearMuCalculusPSPACEComplete.linear_mu_calculus_pspace_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/LinearMuCalculusPSPACECompleteWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html#linear-mu-calculus-pspace-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Satisfiability and model checking for the linear-time μ-calculus](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/satisfiability-and-model-checking-for-the-linear)
