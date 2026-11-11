---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.QTree, Cslib.Algorithms.Lean.QTree.height, Cslib.Algorithms.Lean.QTree.compressed, Cslib.Algorithms.Lean.QTree.selectTree, Cslib.Algorithms.Lean.QTree.height_children_le
statement: formalized
proof: formalized
---

# Quadtree carrier and structural invariants

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html).

## Quadtrees

## Region quadtree

A finite region quadtree with a value leaf or four ordered quadrants.

Formalized by `Cslib.Algorithms.Lean.QTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html#qtree).

## Height of a quadtree

The maximum number of branches from the root to a leaf.

Formalized by `Cslib.Algorithms.Lean.QTree.height`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html#height).

## Compressed quadtree

Every subtree is compressed and no branch has four identical leaves.
Identical nonleaf children are allowed: they need not represent a constant.

Formalized by `Cslib.Algorithms.Lean.QTree.compressed`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html#compressed).

## Quadrant selection by coordinate flags

Selects low/low, low/high, high/low, or high/high, respectively, when
`(x, y)` is `(true, true)`, `(true, false)`, `(false, true)`, or
`(false, false)`.
In lookup, `true` means that the corresponding coordinate is below the split.

Formalized by `Cslib.Algorithms.Lean.QTree.selectTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html#select-tree).

## Height bound for the children of a quadtree branch

A bound on branch height bounds all four child heights one level lower.

Formalized by `Cslib.Algorithms.Lean.QTree.height_children_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Basic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html#height-children-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadtree carrier and structural invariants](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/quadtree-carrier-and-structural-invariants)
