---
declaration: section
origin: cited
lean: Cslib.Language.CYKIndexed.member_time, Cslib.Language.CYKIndexed.cell_length, Cslib.Language.CYKIndexed.lookup_length, Cslib.Language.CYKIndexed.splits_time_le, Cslib.Language.CYKIndexed.fits_time_le, Cslib.Language.CYKIndexed.cell_time_le, Cslib.Language.CYKIndexed.row_time_le, Cslib.Language.CYKIndexed.table_time_le
statement: formalized
proof: formalized
---

# Cubic cost of indexed CYK

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html).

## Exact cost of a membership scan

Exact charge for a full membership scan, including a failed scan.

Formalized by `Cslib.Language.CYKIndexed.member_time`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#member-time).

## Computed CYK cell length bounded by the rule count

Even with duplicates, a cell never exceeds the rule enumeration length.

Formalized by `Cslib.Language.CYKIndexed.cell_length`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#cell-length).

## Every CYK table lookup is bounded by the rule count

All table cells, including invalid/default positions, have bounded
membership-scan length. This invariant is proved from construction.

Formalized by `Cslib.Language.CYKIndexed.lookup_length`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#lookup-length).

## Cost bound for the CYK split scan

Each split pays for both indexed cell reads and both membership scans.

Formalized by `Cslib.Language.CYKIndexed.splits_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#splits-time-le).

## Cost bound for the CYK production fit test

Output inspection is bounded; only binary productions scan splits.

Formalized by `Cslib.Language.CYKIndexed.fits_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#fits-time-le).

## Cost bound for computing one CYK cell

A cell charges every rule, its test, and its possible output cons.

Formalized by `Cslib.Language.CYKIndexed.cell_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#cell-time-le).

## Cost bound for building one CYK row

Row cost counts all starts, not only successful or distinct factors.

Formalized by `Cslib.Language.CYKIndexed.row_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#row-time-le).

## Cost bound for filling the indexed CYK table

Table cost includes allocation, every row conversion and every update.
The memory-size hypothesis needed for split costs is discharged internally.

Formalized by `Cslib.Language.CYKIndexed.table_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#table-time-le).

## Length of a computed CYK row

The linear row-conversion charge uses the actual number of entries.

Formalized by `Cslib.Language.CYKIndexed.row_length`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#row-length).

## Exact cost of the CYK epsilon scan

Exact cost of the empty-input production scan.

Formalized by `Cslib.Language.CYKIndexed.epsilon_time`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#epsilon-time).

## Explicit cubic cost bound for indexed CYK

Explicit cubic bound, for every word including the empty word.
The coefficient depends only on the rule enumeration and equality costs;
no semantic or assumed recurrence hypothesis occurs in this cost theorem.

Formalized by `Cslib.Language.CYKIndexed.recognizes_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#recognizes-time-le).

## Indexed CYK costs a constant times $n^3$ on nonempty words

In the usual nonempty-input form, the bound is a constant times `n³`.

Formalized by `Cslib.Language.CYKIndexed.recognizes_time_le_cubic`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Cost.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html#recognizes-time-le-cubic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubic cost of indexed CYK](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/cubic-cost-of-indexed-cyk)
