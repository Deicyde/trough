---
declaration: section
origin: cited
lean: TensorNetwork.Factored.toInstance, TensorNetwork.Factored.value_toInstance, TensorNetwork.Instance.toFactored, TensorNetwork.Instance.value_toFactored, TensorNetwork.Instance.value_eq_halfEdges
statement: formalized
proof: formalized
---

# Equivalent presentations of finite tensor networks

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html).

## Factored

## Complete-graph instance of a factored network

Turn a factored network into a complete-graph tensor instance.

The finite set `D a b` names the source labels on the edge `{a, b}` through `dec a b`.
Labels outside `D a b` make the corresponding directed factor zero.

Formalized by `TensorNetwork.Factored.toInstance`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Presentation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Presentation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html#to-instance).

## Converting a factored network to an instance preserves value

Naming every source edge alphabet bijectively inside `labels` preserves network value.

Formalized by `TensorNetwork.Factored.value_toInstance`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Presentation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Presentation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html#value-to-instance).

## Half-edge factored presentation of a tensor instance

Present an instance as a half-edge network.

A state at `v` chooses one label for every off-diagonal half-edge from `v`; the two sides of
each edge are constrained to agree. The capacities are zero because this construction makes no
size claim.

Formalized by `TensorNetwork.Instance.toFactored`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Presentation.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Presentation.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html#to-factored).

## Half-edge presentation preserves instance value

The half-edge presentation of an instance has the same value.

Formalized by `TensorNetwork.Instance.value_toFactored`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Presentation.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Presentation.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html#value-to-factored).

## Instance value as a sum over half-edge vectors

Expand an instance value as a sum over directed half-edge vectors with equality factors.

Formalized by `TensorNetwork.Instance.value_eq_halfEdges`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Presentation.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/Presentation.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html#value-eq-half-edges).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equivalent presentations of finite tensor networks](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/equivalent-presentations-of-finite-tensor-networ)
