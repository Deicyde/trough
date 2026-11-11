---
declaration: section
origin: cited
lean: Cslib.Logic.PL.CNF.modelCount, Cslib.Logic.PL.CNF.compact, Cslib.Logic.PL.CNF.length_compact, Cslib.Logic.PL.CNF.clauseLengths_compact, Cslib.Logic.PL.CNF.boundedClauseLength_compact_iff, Cslib.Logic.PL.CNF.nodup_compact_iff, Cslib.Logic.PL.CNF.vars_compact, Cslib.Logic.PL.CNF.satisfies_compact_iff
statement: formalized
proof: formalized
---

# Model-count-preserving CNF transformations

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html).

## Model count of a CNF formula

The number of Boolean assignments to the variables occurring in a formula that satisfy it.

Formalized by `Cslib.Logic.PL.CNF.modelCount`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#model-count).

## Exact variable compaction of a CNF formula

Rename every occurring variable by its position in the last-occurrence list.

Formalized by `Cslib.Logic.PL.CNF.compact`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#compact).

## Compaction preserves the number of clauses

Compaction preserves the number of clauses.

Formalized by `Cslib.Logic.PL.CNF.length_compact`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#length-compact).

## Compaction preserves clause lengths

Compaction preserves every clause length, in the original clause order.

Formalized by `Cslib.Logic.PL.CNF.clauseLengths_compact`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#clause-lengths-compact).

## Compaction preserves clause-length bounds

Compaction preserves every upper bound on clause length.

Formalized by `Cslib.Logic.PL.CNF.boundedClauseLength_compact_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#bounded-clause-length-compact-iff).

## Compaction preserves absence of duplicate clauses

Compaction preserves the absence of duplicate clauses.

Formalized by `Cslib.Logic.PL.CNF.nodup_compact_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#nodup-compact-iff).

## Variables of a compacted formula form an initial range

The variables of a compacted formula are exactly its dense initial range.

Formalized by `Cslib.Logic.PL.CNF.vars_compact`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#vars-compact).

## Satisfaction is preserved by variable compaction

Satisfaction after compaction is satisfaction before compaction with names translated by
their exact last-occurrence positions.

Formalized by `Cslib.Logic.PL.CNF.satisfies_compact_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#satisfies-compact-iff).

## Variable compaction preserves the model count

Exact variable compaction preserves the number of assignments to the occurring variables.

Formalized by `Cslib.Logic.PL.CNF.modelCount_compact`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#model-count-compact).

## Counting satisfying assignments over a larger variable range

If every occurring name is below `N`, the count over all `Fin N` assignments is the support
count times one Boolean choice for each unused ambient variable.

Formalized by `Cslib.Logic.PL.CNF.card_satisfying_fin`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Compaction.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/Compaction.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#card-satisfying-fin).

## Number of fresh variables in the parsimonious 3-CNF reduction

The number of fresh variables used by the parsimonious width-three reduction.

Formalized by `Cslib.Logic.PL.CNF.numFreshParsimonious3`, a definition declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#num-fresh-parsimonious3).

## Parsimonious reduction of CNF to 3-CNF

Reduce a CNF to clauses of length at most three, allocating fresh variables consecutively
from `start`. Repeated output clauses are removed in last-occurrence order.

Formalized by `Cslib.Logic.PL.CNF.to3Parsimonious`, a definition declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#to3-parsimonious).

## Soundness of the parsimonious 3-CNF reduction

Satisfaction of the reduced formula implies satisfaction of the original formula under the
same values of the original variable names.

Formalized by `Cslib.Logic.PL.CNF.satisfies_of_satisfies_to3Parsimonious`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#satisfies-of-satisfies-to3-parsimonious).

## The parsimonious reduction outputs a duplicate-free 3-CNF

Every output clause has length at most three, and duplicate clauses have been removed.

Formalized by `Cslib.Logic.PL.CNF.isThreeCNF_to3Parsimonious`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#is-three-cnf-to3-parsimonious).

## Size bounds for the parsimonious 3-CNF reduction

A width bound on the input gives the source bounds on allocated fresh variables and output
clauses.

Formalized by `Cslib.Logic.PL.CNF.size_to3Parsimonious`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#size-to3-parsimonious).

## Unique satisfying extension in the parsimonious 3-CNF reduction

Every satisfying assignment of the original formula has exactly one satisfying extension that
can differ only on the allocated fresh-variable interval.

Formalized by `Cslib.Logic.PL.CNF.existsUnique_satisfies_to3Parsimonious`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#exists-unique-satisfies-to3-parsimonious).

## The parsimonious 3-CNF reduction preserves the model count

The parsimonious reduction preserves the number of assignments to the variables occurring in
the formula.

Formalized by `Cslib.Logic.PL.CNF.modelCount_to3Parsimonious`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Propositional/CNF/ParsimoniousThree.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html#model-count-to3-parsimonious).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Model-count-preserving CNF transformations](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/propositional-logic/model-count-preserving-cnf-transformations)
