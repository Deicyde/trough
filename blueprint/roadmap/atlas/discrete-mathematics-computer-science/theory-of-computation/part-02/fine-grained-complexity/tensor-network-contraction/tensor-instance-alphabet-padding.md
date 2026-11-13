---
declaration: section
origin: cited
lean: TensorNetwork.Instance.pad, TensorNetwork.Instance.toInstance_toFactored_eq_pad, TensorNetwork.Instance.toInstance_toFactored_univ_eq_pad, TensorNetwork.Instance.value_pad
statement: formalized
proof: formalized
---

# Tensor-instance alphabet padding

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html).

## Alphabet padding of a tensor instance

Rename the active edge alphabet of an instance through `dec`, returning zero when any
off-diagonal target label is outside `D`. The diagonal coordinate is replaced by `sourceDefault`.

Formalized by `TensorNetwork.Instance.pad`, a definition declared in [MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html#pad).

## Factoring and unfactoring a tensor instance gives its padding

Factoring an instance and converting it back through constant edge names gives its padded
version. The decoder must send every admitted target name into the explicit source alphabet.

Formalized by `TensorNetwork.Instance.toInstance_toFactored_eq_pad`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html#to-instance-to-factored-eq-pad).

## Factoring round trip with the full source alphabet

The source conversion theorem with the full finite source alphabet.

Formalized by `TensorNetwork.Instance.toInstance_toFactored_univ_eq_pad`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html#to-instance-to-factored-univ-eq-pad).

## Bijective alphabet padding preserves instance value

Padding through a bijective renaming of an explicit source alphabet preserves instance value.

Formalized by `TensorNetwork.Instance.value_pad`, a theorem declared in [MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/TensorNetwork/AlphabetPadding.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html#value-pad).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tensor-instance alphabet padding](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/tensor-network-contraction/tensor-instance-alphabet-padding)
