---
declaration: section
origin: cited
lean: TensorNetwork.gridRowNetwork_capacity_le, TensorNetwork.gridRowNetwork_shaped, TensorNetwork.gridRowNetwork_sized, TensorNetwork.gridRowNetwork_totalCapacity
statement: formalized
proof: formalized
---

# Bounds for finite grid row networks

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html).

## Capacity bound between grid rows

The capacity between two grid rows is at most `g²mL` when every active rectangle is
charged at most `2mL` and there are `g` columns.

Formalized by `TensorNetwork.gridRowNetwork_capacity_le`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html#grid-row-network-capacity-le).

## Shape bound for the grid row network

The grid row network has shape `m g³ L` when both raw-state alphabets have at most
`2^L` elements and every rectangle label set and capacity obeys its declared bound.

Formalized by `TensorNetwork.gridRowNetwork_shaped`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html#grid-row-network-shaped).

## Size bound for the grid row network

Under uniform raw tensor and factor bounds, the grid row network has exact source exponents
`m g³ L` for shape and `g B + g² b` for integer magnitudes.

Formalized by `TensorNetwork.gridRowNetwork_sized`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html#grid-row-network-sized).

## Total capacity of the grid row network

The directed total capacity consists of all vertical row edges plus twice the active
rectangle capacity; diagonal row capacities are excluded.

Formalized by `TensorNetwork.gridRowNetwork_totalCapacity`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/GridRowBounds.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html#grid-row-network-total-capacity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds for finite grid row networks](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-finite-grid-row-networks)
