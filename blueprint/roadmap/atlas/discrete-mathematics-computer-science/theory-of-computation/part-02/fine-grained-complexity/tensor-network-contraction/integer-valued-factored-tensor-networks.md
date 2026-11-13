---
declaration: section
origin: cited
lean: TensorNetwork.orderedPairs, TensorNetwork.mem_orderedPairs, TensorNetwork.pairIndex, TensorNetwork.edgeLabelings, TensorNetwork.mem_edgeLabelings, TensorNetwork.incidentLabels, TensorNetwork.Instance, TensorNetwork.Instance.value
statement: formalized
proof: formalized
---

# Integer-valued factored tensor networks

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html).

## Tensor Network

## Ordered pairs representing unordered pairs

Pairs `(a, b)` with `a < b`, representing unordered pairs once.

Formalized by `TensorNetwork.orderedPairs`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#ordered-pairs).

## Membership in the ordered pairs

Membership in `orderedPairs` is strict ordering of the two coordinates.

Formalized by `TensorNetwork.mem_orderedPairs`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#mem-ordered-pairs).

## Ordered representative of an unordered pair

The ordered representative `(min a b, max a b)` of the pair `{a, b}`.

Formalized by `TensorNetwork.pairIndex`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#pair-index).

## Edge labelings of the complete graph

Complete-graph edge labelings, free on `orderedPairs` and default elsewhere.

Formalized by `TensorNetwork.edgeLabelings`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#edge-labelings).

## Characterization of complete-graph edge labelings

A labeling belongs to `edgeLabelings` exactly when active edges use allowed labels and all
other coordinates contain the default.

Formalized by `TensorNetwork.mem_edgeLabelings`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#mem-edge-labelings).

## Edge labels incident to a vertex

Labels incident to `v`, indexed by the other endpoint.

Formalized by `TensorNetwork.incidentLabels`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#incident-labels).

## Integer-valued complete-graph tensor instance

An integer-valued local tensor at each vertex.

Formalized by `TensorNetwork.Instance`, an abbreviation declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#instance).

## Value of a complete-graph tensor instance

The sum, over complete-graph edge labelings, of the product of local tensors.

Formalized by `TensorNetwork.Instance.value`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#value).

## Integer-valued factored tensor network

An integer-valued factored tensor network.

Only `Θ a b` with `a < b` supplies labels. The factors `f a b` and `f b a` are the two
sides of the same interaction. Capacities `c` are metadata used by `totalCapacity`, `Shaped`,
and `Sized`; `value` does not read them.

Formalized by `TensorNetwork.Factored`, a structure declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#factored).

## Label set of an unordered vertex pair

The label set of an unordered vertex pair.

Formalized by `TensorNetwork.Factored.labelSet`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#label-set).

## Label set is symmetric in its endpoints

The label set is independent of endpoint order.

Formalized by `TensorNetwork.Factored.labelSet_comm`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#label-set-comm).

## Interaction of two states in a factored network

The interaction of two states, summed over their shared edge labels.

Formalized by `TensorNetwork.Factored.interaction`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#interaction).

## Interaction is symmetric under swapping endpoints

Reading an interaction from the other endpoint swaps its states.

Formalized by `TensorNetwork.Factored.interaction_comm`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#interaction-comm).

## Value of a factored tensor network

The network value: sum over states of vertex weights times all pair interactions.

Formalized by `TensorNetwork.Factored.value`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#value-2).

## Directed total capacity of a factored network

The directed total capacity `Σ_{a ≠ b} c a b`; both orientations are counted.

Formalized by `TensorNetwork.Factored.totalCapacity`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#total-capacity).

## Factored tensor network with shape parameter

A network of shape parameter `P`: at most `2 ^ P` states per vertex, symmetric
capacities summing to at most `P` at each vertex, and at most `2 ^ c` labels per edge.

Formalized by `TensorNetwork.Factored.Shaped`, a structure declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#shaped).

## Shaped tensor network with bounded entries

A shaped network whose weights, factors and off-diagonal interactions are bounded by
`2 ^ B` in absolute value.

Formalized by `TensorNetwork.Factored.Sized`, a structure declared in [MathlibExt/Combinatorics/TensorNetwork/Basic.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Basic.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html#sized).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer-valued factored tensor networks](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/integer-valued-factored-tensor-networks)
