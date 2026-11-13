---
declaration: section
origin: cited
lean: TensorNetwork.gridRowNetwork, TensorNetwork.gridRowNetwork_interaction, TensorNetwork.gridRowNetwork_interaction_of_mem, TensorNetwork.gridRowNetwork_value
statement: formalized
proof: formalized
---

# Finite row networks for grid tensors

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html).

## Row network of a grid tensor

Merge every grid row into one vertex of a factored tensor network. The state and label
carriers may be infinite; only the supplied alphabets are enumerated. Capacity metadata charges
`L` per vertical edge and the supplied cut capacity for each active rectangle.

Formalized by `TensorNetwork.gridRowNetwork`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/GridRows.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridRows.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html#grid-row-network).

## Interaction between rows of the grid row network

The interaction between increasing rows is the rectangle-kernel product times vertical
equality indicators. For finite alphabets, an equal vertical value contributes only when it is
in `labels`.

Formalized by `TensorNetwork.gridRowNetwork_interaction`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRows.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridRows.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html#grid-row-network-interaction).

## Row interaction for enumerated left states

When the left state is enumerated by the row network, the alphabet-membership condition is
automatic, so the interaction recovers the source vertical-equality formula. The right state may
be arbitrary because equality with an allowed left value already forces its vertical value.

Formalized by `TensorNetwork.gridRowNetwork_interaction_of_mem`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRows.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridRows.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html#grid-row-network-interaction-of-mem).

## Grid row network computes the grid value

If each rectangle kernel is the finite sum of its top and bottom factors, contracting the
constructed row network gives the canonical finite grid value.

Formalized by `TensorNetwork.gridRowNetwork_value`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/GridRows.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/GridRows.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html#grid-row-network-value).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite row networks for grid tensors](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/finite-row-networks-for-grid-tensors)
