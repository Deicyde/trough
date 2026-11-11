---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.QTree.Boolean.Qc, Cslib.Algorithms.Lean.QTree.Boolean.get, Cslib.Algorithms.Lean.QTree.Boolean.neg, Cslib.Algorithms.Lean.QTree.Boolean.qtUnion, Cslib.Algorithms.Lean.QTree.Boolean.qtDiff, Cslib.Algorithms.Lean.QTree.Boolean.height_Qc_le, Cslib.Algorithms.Lean.QTree.Boolean.compressed_Qc, Cslib.Algorithms.Lean.QTree.Boolean.get_Qc_succ
statement: formalized
proof: formalized
---

# Boolean region quadtree operations

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html).

## Compressing branch constructor for Boolean quadtrees

A branch constructor that collapses four identical Boolean leaves.
This is local compression, not recursive normalization of its arguments.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.Qc`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#qc).

## Boolean quadtree lookup

Boolean lookup with `false` on a nonleaf at scale zero.
Leaves ignore coordinates; positive scales use the shared quadrant order.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.get`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#get).

## Complement of a Boolean quadtree

Complements every leaf, compressing the rebuilt branches.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.neg`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#neg).

## Union of Boolean quadtrees

Boolean union, short-circuiting constant regions and compressing
branches when both inputs are branches.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.qtUnion`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#qt-union).

## Difference of Boolean quadtrees

Ordered Boolean difference: cells in the first region but not the second.
A full first region complements the second; an empty second returns the
first.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.qtDiff`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#qt-diff).

## Local compression does not increase quadtree height

Local compression never increases a branch's height.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.height_Qc_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#height-qc-le).

## Local compression of compressed children is compressed

Four compressed children produce a compressed result.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.compressed_Qc`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#compressed-qc).

## Local compression preserves lookup at positive scales

Compression preserves positive-scale lookup. Scale zero is excluded:
collapsing four `true` leaves changes a branch's zero-scale default.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.get_Qc_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#get-qc-succ).

## Quadtree complementation does not increase height

Complementation does not increase height.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.height_neg_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#height-neg-le).

## Quadtree complementation preserves compression

Complementation preserves compression of the input.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.compressed_neg`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#compressed-neg).

## Quadtree complementation negates lookup at sufficient scale

Complementation negates each lookup whenever the scale bounds height.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.get_neg_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#get-neg-correct).

## Height bound for quadtree union

Union height is bounded by the maximum input height.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.height_qtUnion_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#height-qt-union-le).

## Height bound for quadtree difference

Difference height is bounded by the maximum input height.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.height_qtDiff_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#height-qt-diff-le).

## Quadtree union preserves compression

Union preserves compression when both inputs are compressed.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.compressed_qtUnion`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#compressed-qt-union).

## Quadtree difference preserves compression

Difference preserves compression when both inputs are compressed.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.compressed_qtDiff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#compressed-qt-diff).

## Quadtree union is pointwise disjunction at sufficient scale

Union is pointwise Boolean disjunction at a scale bounding both heights.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.get_qtUnion_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#get-qt-union-correct).

## Quadtree difference is pointwise set difference at sufficient scale

Difference is pointwise conjunction with the second region's complement,
provided the scale bounds both heights.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.get_qtDiff_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#get-qt-diff-correct).

## Six-part correctness of Boolean quadtree operations

The original graded six-part correctness statement, under its original
name.

Formalized by `Cslib.Algorithms.Lean.QTree.Boolean.fdsa_chap13_ex01`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Quadtree/Boolean.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html#fdsa-chap13-ex01).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boolean region quadtree operations](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/region-quadtree/boolean-region-quadtree-operations)
