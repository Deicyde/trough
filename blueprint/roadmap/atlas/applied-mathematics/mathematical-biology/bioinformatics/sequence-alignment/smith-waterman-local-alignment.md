---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Alignment.SmithWaterman.nextRowAux, Cslib.Bioinformatics.Alignment.SmithWaterman.nextRow, Cslib.Bioinformatics.Alignment.SmithWaterman.swTabAux, Cslib.Bioinformatics.Alignment.SmithWaterman.swTab, Cslib.Bioinformatics.Alignment.SmithWaterman.nextRow_eq, Cslib.Bioinformatics.Alignment.SmithWaterman.swTab_eq_swScore, Cslib.Bioinformatics.Alignment.SmithWaterman.swTab_eq_localScore
statement: formalized
proof: formalized
---

# Smith–Waterman local alignment

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html).

## Auxiliary row computation for the Smith–Waterman table

The cells `H[i+1][j+1], H[i+1][j+2], …` of a row from the remaining letters `b :: ys` of the
second sequence, the remaining cells `up :: prev` of the previous row, the previous row's cell
`diag` to the upper left and the cell `left` just computed. A previous row that is too short ends
the row early (this does not happen for rows of the table, `nextRow_eq`).

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.nextRowAux`, a definition declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#next-row-aux).

## Next row of the Smith–Waterman table

The row of the table for the prefix extended by `a`, from the previous row: `H[i+1][0] = 0`,
then the recurrence left to right.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.nextRow`, a definition declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#next-row).

## Row-by-row filling of the Smith–Waterman table

The Smith–Waterman table, filled row by row over the remaining letters of the first sequence:
`row` is the current row and `best` the largest cell of the earlier rows.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.swTabAux`, a definition declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#sw-tab-aux).

## The Smith–Waterman table

The largest cell of the `(|xs| + 1) × (|ys| + 1)` table, with
the zero row `H[0][j] = 0` to start.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.swTab`, a definition declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#sw-tab).

## One row of the table

From the row of the prefix `px`, `nextRow` computes the row of
`px ++ [a]`: the cells `H[i+1][j] = swCellScore σ gap (px ++ [a]) py` for the prefixes `py` of
`ys`, shortest first.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.nextRow_eq`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#next-row-eq).

## The table computes the Smith–Waterman score

`swTab` is the largest cell
`swCellScore σ gap px py` over all pairs of prefixes.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.swTab_eq_swScore`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#sw-tab-eq-sw-score).

## The table computes the optimal local alignment score

**The table computes the optimal local alignment score** (Smith–Waterman 1981, `gap ≤ 0`):
`swTab` is the maximum, over all pairs of infixes of `xs` and `ys` (including the empty ones,
which give the floor `0`), of their optimal global alignment score `nwScore`.

Formalized by `Cslib.Bioinformatics.Alignment.SmithWaterman.swTab_eq_localScore`, a theorem declared in [CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Alignment/SmithWaterman.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html#sw-tab-eq-local-score).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smith–Waterman local alignment](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/smith-waterman-local-alignment)
