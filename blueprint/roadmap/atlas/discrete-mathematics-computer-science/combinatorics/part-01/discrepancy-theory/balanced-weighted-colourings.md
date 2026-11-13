---
declaration: section
origin: cited
lean: Matrix.exists_balanced_coloring, Matrix.exists_balanced_coloring_offDiagonal, Matrix.exists_balanced_coloring_fin
statement: formalized
proof: formalized
---

# Balanced weighted colourings

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings/index.html).

## Balanced coloring of a weighted symmetric matrix

A finite symmetric natural-valued matrix with zero diagonal and bounded row sums has a
coloring with balanced fibers and bounded weight in every ordered color block.

Formalized by `Matrix.exists_balanced_coloring`, a theorem declared in [MathlibExt/Combinatorics/WeightedColoring.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedColoring.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings/index.html#exists-balanced-coloring).

## Balanced coloring with bounded off-diagonal block weight

A finite symmetric natural-valued matrix with bounded off-diagonal row sums has a balanced
coloring whose blocks between distinct colors have bounded off-diagonal weight. Diagonal entries
are unrestricted and ignored.

Formalized by `Matrix.exists_balanced_coloring_offDiagonal`, a theorem declared in [MathlibExt/Combinatorics/WeightedColoring.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedColoring.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings/index.html#exists-balanced-coloring-off-diagonal).

## Balanced off-diagonal coloring for matrices indexed by $\{0,\dots,n-1\}$

The `Fin`-indexed form of `Matrix.exists_balanced_coloring_offDiagonal`.

Formalized by `Matrix.exists_balanced_coloring_fin`, a theorem declared in [MathlibExt/Combinatorics/WeightedColoring.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedColoring.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings/index.html#exists-balanced-coloring-fin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanced weighted colourings](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/discrepancy-theory/balanced-weighted-colourings)
