---
declaration: section
origin: cited
lean: TensorNetwork.Factored.merge_shaped, TensorNetwork.Factored.merge_sized
statement: formalized
proof: formalized
---

# Bounds for contraction of factored tensor networks

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-contraction-of-factored-tensor-networ/index.html).

## Shape bound for contracted tensor networks

If every contraction class has at most `m` vertices, contraction multiplies the network's
shape parameter by `m`.

Formalized by `TensorNetwork.Factored.merge_shaped`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/ContractionBounds.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/ContractionBounds.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-contraction-of-factored-tensor-networ/index.html#merge-shaped).

## Size bound for contracted tensor networks

If every contraction class has at most `m` vertices, contraction multiplies the shape
parameter by `m` and changes the absolute-value exponent from `B` to `B * (m + m * m)`.

Formalized by `TensorNetwork.Factored.merge_sized`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/ContractionBounds.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/TensorNetwork/ContractionBounds.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-contraction-of-factored-tensor-networ/index.html#merge-sized).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds for contraction of factored tensor networks](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-contraction-of-factored-tensor-networ/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/bounds-for-contraction-of-factored-tensor-networ)
