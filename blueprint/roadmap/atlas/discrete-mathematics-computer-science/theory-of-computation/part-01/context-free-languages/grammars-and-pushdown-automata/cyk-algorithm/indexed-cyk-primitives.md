---
declaration: section
origin: cited
lean: Cslib.Language.CYKIndexed.member, Cslib.Language.CYKIndexed.member_ret, Cslib.Language.CYKIndexed.lookup, Cslib.Language.CYKIndexed.splits, Cslib.Language.CYKIndexed.splits_ret, Cslib.Language.CYKIndexed.fits, Cslib.Language.CYKIndexed.cell, Cslib.Language.CYKIndexed.mem_cell
statement: formalized
proof: formalized
---

# Indexed CYK primitives

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html).

## Charged list-membership scan

Full membership scan, charging equality and list/control operations.

Formalized by `Cslib.Language.CYKIndexed.member`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#member).

## Charged membership scan agrees with list membership

The charged scan has ordinary list-membership semantics.

Formalized by `Cslib.Language.CYKIndexed.member_ret`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#member-ret).

## CYK table lookup with empty default cells

Two bounded array reads; invalid indices denote an empty cell.

Formalized by `Cslib.Language.CYKIndexed.lookup`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#lookup).

## Charged scan of CYK split positions

Scan split positions `1,...,count`, with two table reads per split.
The 16 units cover four array reads, bounds/default tests, index arithmetic,
Boolean combinations and recursion control.

Formalized by `Cslib.Language.CYKIndexed.splits`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#splits).

## Successful CYK split scans find a split in range

Every successful scan names a split in exactly the scanned interval.

Formalized by `Cslib.Language.CYKIndexed.splits_ret`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#splits-ret).

## Production-output fit test for indexed CYK

Test a production output without constructing or comparing substrings.
Pattern inspection is bounded (at most three cons and two symbol tags).

Formalized by `Cslib.Language.CYKIndexed.fits`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#fits).

## Charged computation of one CYK cell

Scan every production once, retaining its input exactly when it fits.
Duplicates are allowed; no set insertion or uncharged deduplication occurs.

Formalized by `Cslib.Language.CYKIndexed.cell`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#cell).

## CYK cell members come from scanned productions

Membership in a computed cell names an actual scanned production.

Formalized by `Cslib.Language.CYKIndexed.mem_cell`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#mem-cell).

## Charged construction of one CYK row

Build one row in increasing start-position order. Each cell is evaluated
once against the already completed shorter rows.

Formalized by `Cslib.Language.CYKIndexed.row`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#row).

## Charged construction of the indexed CYK table

Fill rows `1,...,depth` in a fixed outer array of size `w.size + 1`.
Row conversion is linear; the outer update is an indexed primitive.

Formalized by `Cslib.Language.CYKIndexed.table`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#table).

## Charged scan for start epsilon productions

Scan start epsilon rules; output emptiness is a single list-tag test.

Formalized by `Cslib.Language.CYKIndexed.epsilon`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#epsilon).

## Charged indexed CYK recognizer

The charged indexed recognizer. The nonempty branch pays for the input
length scan, conversion, completed table, final lookup and membership.

Formalized by `Cslib.Language.CYKIndexed.recognizes`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/CYKIndexed.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html#recognizes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Indexed CYK primitives](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-primitives)
