---
declaration: section
origin: cited
lean: Cslib.PDL.Program.toRelation, Cslib.PDL.Program.mem_toRelation, Cslib.PDL.Program.toRelation_seq, Cslib.PDL.Program.toRelation_choice, Cslib.PDL.Program.toRelation_test, Cslib.PDL.Program.toRelation_star
statement: formalized
proof: formalized
---

# Relational interpretation of PDL programs

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html).

## Relational interpretation of a PDL program

Interpret a PDL program in CSLib's canonical relation algebra.

Formalized by `Cslib.PDL.Program.toRelation`, a definition declared in [CSLibExt/Logics/PDL/Algebra.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#to-relation).

## Relational interpretation preserves executions

The representation conversion preserves exactly the executions.

Formalized by `Cslib.PDL.Program.mem_toRelation`, a theorem declared in [CSLibExt/Logics/PDL/Algebra.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#mem-to-relation).

## Sequencing is interpreted by relational composition

The interpretation of sequencing uses canonical composition.

Formalized by `Cslib.PDL.Program.toRelation_seq`, a theorem declared in [CSLibExt/Logics/PDL/Algebra.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#to-relation-seq).

## Choice is interpreted by relational union

The interpretation of choice uses canonical union.

Formalized by `Cslib.PDL.Program.toRelation_choice`, a theorem declared in [CSLibExt/Logics/PDL/Algebra.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#to-relation-choice).

## Tests are interpreted by PDL satisfaction

Formula tests use the existing PDL satisfaction predicate.

Formalized by `Cslib.PDL.Program.toRelation_test`, a theorem declared in [CSLibExt/Logics/PDL/Algebra.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#to-relation-test).

## Iteration is interpreted by reflexive-transitive closure

Iteration in the canonical carrier is the same reflexive-transitive
closure as in `ProgRel`, including its identity boundary.

Formalized by `Cslib.PDL.Program.toRelation_star`, a theorem declared in [CSLibExt/Logics/PDL/Algebra.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Algebra.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html#to-relation-star).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Relational interpretation of PDL programs](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/propositional-dynamic-logic/relational-interpretation-of-pdl-programs)
