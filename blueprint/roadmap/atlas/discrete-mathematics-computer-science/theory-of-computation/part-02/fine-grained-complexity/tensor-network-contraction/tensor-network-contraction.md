---
declaration: section
origin: cited
lean: TensorNetwork.gridValue_eq_sum_choices, TensorNetwork.Factored.abs_toInstance_le
statement: formalized
proof: formalized
---

# Tensor-network contraction: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/index.html).

## Grid value expanded over kernel choices

If every active rectangle kernel is a finite sum, the grid value is the sum over one kernel
choice for each active rectangle. Raw rectangle indices outside `gridRectangles` retain the
original kernel, which does not affect `gridValue`.

Formalized by `TensorNetwork.gridValue_eq_sum_choices`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridExpansion.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/GridExpansion.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/index.html#grid-value-eq-sum-choices).

## Entry bound for a converted tensor instance

A converted tensor entry is a sum of at most `2 ^ P` terms, each containing one weight and
`Fintype.card J - 1` off-diagonal factors.

Formalized by `TensorNetwork.Factored.abs_toInstance_le`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/PresentationBounds.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/PresentationBounds.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/index.html#abs-to-instance-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tensor-network contraction](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction)
