---
declaration: section
origin: cited
lean: Cslib.Language.CYKIndexed.cell_correct, Cslib.Language.CYKIndexed.row_get, Cslib.Language.CYKIndexed.table_size, Cslib.Language.CYKIndexed.lookup_table_other, Cslib.Language.CYKIndexed.lookup_table_new, Cslib.Language.CYKIndexed.table_correct, Cslib.Language.CYKIndexed.epsilon_ret, Cslib.Language.CYKIndexed.recognizes_iff
statement: formalized
proof: formalized
---

# Correctness of indexed CYK

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html).

## Correctness of one indexed CYK cell

A cell is correct once all strictly shorter, valid factors are correct.
The rule enumeration certificate constrains data only, not computation.

Formalized by `Cslib.Language.CYKIndexed.cell_correct`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#cell-correct).

## Indexing of a constructed CYK row

Row construction preserves the exact start-position indexing.

Formalized by `Cslib.Language.CYKIndexed.row_get`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#row-get).

## Indexed CYK table keeps its allocated size

The outer table retains its allocated size through every update.

Formalized by `Cslib.Language.CYKIndexed.table_size`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#table-size).

## CYK table update leaves other lengths' cells unchanged

Updating one length never changes another length's cells.

Formalized by `Cslib.Language.CYKIndexed.lookup_table_other`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#lookup-table-other).

## New CYK table row holds the computed cells

The new length's row contains exactly the cells just computed.

Formalized by `Cslib.Language.CYKIndexed.lookup_table_new`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#lookup-table-new).

## Correctness of the completed indexed CYK table

Every completed valid cell agrees with canonical grammar derivations.

Formalized by `Cslib.Language.CYKIndexed.table_correct`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#table-correct).

## Correctness of the CYK epsilon scan

Epsilon scanning agrees with existence of a start epsilon production.

Formalized by `Cslib.Language.CYKIndexed.epsilon_ret`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#epsilon-ret).

## Correctness of the indexed CYK recognizer

The indexed recognizer decides the existing canonical language.

Formalized by `Cslib.Language.CYKIndexed.recognizes_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#recognizes-iff).

## Indexed CYK agrees with the list-table CYK recognizer

Exact Boolean correspondence with the existing list-table recognizer.

Formalized by `Cslib.Language.CYKIndexed.recognizes_eq_cykAccepts`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Correctness.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html#recognizes-eq-cyk-accepts).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Correctness of indexed CYK](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/correctness-of-indexed-cyk)
