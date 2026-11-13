---
declaration: section
origin: cited
lean: TensorNetwork.Instance.transpose, TensorNetwork.Instance.transpose_transpose, TensorNetwork.transposeRectangleKernel, TensorNetwork.transposeRectangleKernel_transposeRectangleKernel, TensorNetwork.gridValue_transpose
statement: formalized
proof: formalized
---

# Transposition of finite grid tensor evaluations

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html).

## Transposition

## Transpose of a grid tensor instance

Swap the row and column coordinates of a grid tensor instance.

Formalized by `TensorNetwork.Instance.transpose`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html#transpose).

## Transposing a grid tensor instance is an involution

Transposing a grid tensor instance twice recovers the original instance.

Formalized by `TensorNetwork.Instance.transpose_transpose`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html#transpose-transpose).

## Transpose of a rectangle kernel

Transpose a rectangle kernel, exchanging the `y` and `u` directed diagonal ends.

Formalized by `TensorNetwork.transposeRectangleKernel`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html#transpose-rectangle-kernel).

## Transposing a rectangle kernel is an involution

Transposing a rectangle kernel twice recovers the original kernel.

Formalized by `TensorNetwork.transposeRectangleKernel_transposeRectangleKernel`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html#transpose-rectangle-kernel-transpose-rec).

## Transposition preserves the grid evaluation

Transposing the grid coordinates, local tensors, and rectangle kernels preserves the finite
grid evaluation. Edge and diagonal label choices remain independent.

Formalized by `TensorNetwork.gridValue_transpose`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridTranspose.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html#grid-value-transpose).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transposition of finite grid tensor evaluations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/transposition-of-finite-grid-tensor-evaluations)
