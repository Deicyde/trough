---
declaration: section
origin: cited
lean: TensorNetwork.sum_statePadding, TensorNetwork.Factored.StatePadding, TensorNetwork.Factored.StatePadding.value_totalCapacity
statement: formalized
proof: formalized
---

# State padding preserves tensor-network values

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values/index.html).

## Tensor Network

## State padding preserves the weighted pair sum

Padding the finite state sets preserves the full sum of vertex weights and arbitrary pair
kernels. No factorization, finiteness of the state carriers, or global injectivity is required.

Formalized by `TensorNetwork.sum_statePadding`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values/index.html#sum-state-padding).

## State padding of a factored tensor network

The source's local padding protocol for factored networks. The factor clause is retained
on source states and source labels, even though value preservation uses the interaction clause.
Only capacities between distinct vertices must agree.

Formalized by `TensorNetwork.Factored.StatePadding`, a structure declared in [MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values/index.html#state-padding).

## State padding preserves value and total capacity

A local state-padding certificate preserves both network value and directed total capacity.

Formalized by `TensorNetwork.Factored.StatePadding.value_totalCapacity`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/StatePadding.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values/index.html#value-total-capacity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: State padding preserves tensor-network values](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/state-padding-preserves-tensor-network-values)
