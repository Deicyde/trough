---
declaration: section
origin: cited
lean: TensorNetwork.Factored.merge, TensorNetwork.Factored.merge_interaction_lt, TensorNetwork.Factored.merge_interaction, TensorNetwork.Factored.value_merge, TensorNetwork.Factored.card_merge_S
statement: formalized
proof: formalized
---

# Contraction of factored tensor networks

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html).

## Merging vertices of a factored tensor network

Merge vertices along `χ`, retaining source states and labels on their classes and padding all
other coordinates with the supplied defaults.

Formalized by `TensorNetwork.Factored.merge`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/Contraction.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Contraction.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html#merge).

## Interaction of merged classes in increasing order

The interaction of two increasingly ordered classes is the product of all source interactions
crossing between them.

Formalized by `TensorNetwork.Factored.merge_interaction_lt`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Contraction.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Contraction.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html#merge-interaction-lt).

## Interaction of two distinct merged classes

The interaction of two distinct classes is the product of all source interactions crossing
between them, oriented from the first class to the second.

Formalized by `TensorNetwork.Factored.merge_interaction`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Contraction.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Contraction.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html#merge-interaction).

## Merging vertices preserves network value

Merging along any map preserves the exact integer-valued network value.

Formalized by `TensorNetwork.Factored.value_merge`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Contraction.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Contraction.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html#value-merge).

## Number of states of a merged vertex

The number of merged states is the product of the state-set sizes in the class.

Formalized by `TensorNetwork.Factored.card_merge_S`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/Contraction.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/Contraction.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html#card-merge-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contraction of factored tensor networks](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/contraction-of-factored-tensor-networks)
