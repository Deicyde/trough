---
declaration: section
origin: cited
lean: StatMech.Universality.projHom, StatMech.Universality.liftWalk, StatMech.Universality.colLeq
statement: formalized
proof: formalized
---

# Left–right paths cross every column

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column/index.html).

## Projection of an induced open subgraph to the lattice

The graph homomorphism from the open subgraph induced on `R` to the lattice `ℤ²`
(forgetting `R`).

Formalized by `StatMech.Universality.projHom`, a definition declared in [MathlibExt/Probability/Percolation/Universality/VSeparates.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/VSeparates.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column/index.html#proj-hom).

## Walk in an induced open subgraph as a lattice walk

A walk in the open subgraph induced on `R`, mapped to a walk in the lattice `ℤ²`.

Formalized by `StatMech.Universality.liftWalk`, a definition declared in [MathlibExt/Probability/Percolation/Universality/VSeparates.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/VSeparates.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column/index.html#lift-walk).

## Half-plane left of a column

The half-plane `{z ∈ ℤ² : z_0 ≤ k}`.

Formalized by `StatMech.Universality.colLeq`, a definition declared in [MathlibExt/Probability/Percolation/Universality/VSeparates.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/VSeparates.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column/index.html#col-leq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Left–right paths cross every column](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/left-right-paths-cross-every-column)
