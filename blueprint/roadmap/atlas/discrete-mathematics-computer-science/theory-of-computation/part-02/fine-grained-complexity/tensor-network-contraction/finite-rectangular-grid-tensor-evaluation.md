---
declaration: section
origin: cited
lean: TensorNetwork.gridRectangles, TensorNetwork.rectangleApply, TensorNetwork.gridLabelings, TensorNetwork.mem_gridLabelings, TensorNetwork.gridValue, TensorNetwork.Instance.onGrid, TensorNetwork.crossing, TensorNetwork.Instance.value_eq_gridValue_crossing
statement: formalized
proof: formalized
---

# Finite rectangular-grid tensor evaluation

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html).

## Tensor Network

## Ordered rectangles of a finite grid

Ordered grid rectangles, indexed by an increasing row pair and increasing column pair.

Formalized by `TensorNetwork.gridRectangles`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#grid-rectangles).

## Applying a rectangle kernel to its diagonal ends

Apply a rectangle kernel to its four directed diagonal ends `x`, `y`, `u`, `v`.

Formalized by `TensorNetwork.rectangleApply`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#rectangle-apply).

## Directed labelings of a finite grid

Directed grid labelings with independent finite choices on edges and diagonal entries.

Formalized by `TensorNetwork.gridLabelings`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#grid-labelings).

## Characterization of directed grid labelings

Membership in `gridLabelings` means precisely that diagonal and edge coordinates use their
respective finite choice sets.

Formalized by `TensorNetwork.mem_gridLabelings`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#mem-grid-labelings).

## Finite grid tensor evaluation

The finite grid evaluation: local tensors, row and column edge equalities, and one kernel per
ordered rectangle, summed over all directed labelings.

Formalized by `TensorNetwork.gridValue`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#grid-value).

## Transporting a tensor instance to a grid

Transport an instance to a grid, returning zero unless the self-label is the chosen default.

Formalized by `TensorNetwork.Instance.onGrid`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#on-grid).

## Crossing kernel on grid rectangles

The crossing kernel requires opposite directed copies on both rectangle diagonals to agree.

Formalized by `TensorNetwork.crossing`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#crossing).

## Complete-graph tensor value as a crossing grid evaluation

Complete-graph tensor evaluation is the crossing grid evaluation after transport. The
transport gates diagonal entries at `default`; other allowed diagonal labels therefore contribute
zero. The default need not belong to the edge-label set.

Formalized by `TensorNetwork.Instance.value_eq_gridValue_crossing`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#value-eq-grid-value-crossing).

## Number of ordered grid rectangles

The number of ordered grid rectangles is the product of the two pair counts.

Formalized by `TensorNetwork.card_gridRectangles`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Grid.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Grid.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html#card-grid-rectangles).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite rectangular-grid tensor evaluation](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-rectangular-grid-tensor-evaluation)
