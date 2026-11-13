---
declaration: section
origin: cited
lean: StatMech.Percolation.coordShift, StatMech.Percolation.stepSign, StatMech.Percolation.boundaryEdges, StatMech.Percolation.card_boundaryEdges_le, StatMech.Percolation.connWithinProb, StatMech.Percolation.phi, StatMech.Percolation.tildePcSet, StatMech.Percolation.tildePc
statement: formalized
proof: formalized
---

# The Duminil-Copin–Tassion quantity φ_p(S) and the threshold p̃\_c

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html).

## Shift of a lattice site in one coordinate

The site `x + δ e_i` obtained by moving `x` by `δ` in coordinate `i`.

Formalized by `StatMech.Percolation.coordShift`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#coord-shift).

## Sign of a unit lattice step

The unit step `+1` (for `true`) or `-1` (for `false`).

Formalized by `StatMech.Percolation.stepSign`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#step-sign).

## Oriented edge boundary of a finite lattice set

The oriented edge boundary `∂S = {(x, x ± e_i) : x ∈ S, x ± e_i ∉ S}` of a finite set
`S ⊆ ℤ^d`, as ordered pairs (inner endpoint first).

Formalized by `StatMech.Percolation.boundaryEdges`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#boundary-edges).

## Size bound for the edge boundary

The edge boundary of `S` has at most `2d |S|` elements.

Formalized by `StatMech.Percolation.card_boundaryEdges_le`, a theorem declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#card-boundary-edges-le).

## Probability of connection inside a set

The probability `ℙ_p(0 ↔ x inside S)` that the origin and `x` are joined by an open path
using only vertices of `S`; it is `0` if `0 ∉ S` or `x ∉ S`.

Formalized by `StatMech.Percolation.connWithinProb`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#conn-within-prob).

## Duminil-Copin–Tassion quantity

The Duminil-Copin–Tassion quantity `φ_p(S) = p ∑_{(x, y) ∈ ∂S} ℙ_p(0 ↔ x inside S)`.

Formalized by `StatMech.Percolation.phi`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#phi).

## Densities with a finite set of small Duminil-Copin–Tassion quantity

The set of densities `p ∈ [0, 1]` for which some finite `S ∋ 0` has `φ_p(S) < 1`.

Formalized by `StatMech.Percolation.tildePcSet`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#tilde-pc-set).

## Duminil-Copin–Tassion threshold

The Duminil-Copin–Tassion threshold `p̃_c(d) = sup {p : ∃ S ∋ 0 finite, φ_p(S) < 1}`.

Formalized by `StatMech.Percolation.tildePc`, a definition declared in [MathlibExt/Probability/Percolation/TildePc.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TildePc.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html#tilde-pc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Duminil-Copin–Tassion quantity φ_p(S) and the threshold p̃_c](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/sharpness/the-duminil-copin-tassion-quantity-p-s-and-the-t)
