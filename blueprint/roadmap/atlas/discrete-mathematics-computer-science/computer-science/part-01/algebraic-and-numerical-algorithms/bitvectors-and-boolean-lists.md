---
declaration: section
origin: cited
lean: BitVec.toBoolListLE, BitVec.equivBoolListLE, List.sum_map_toNat_eq_count_true
statement: formalized
proof: formalized
---

# Bitvectors and Boolean lists

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists/index.html).

## Little-endian bits of a bitvector

The bits of a bitvector in little-endian order, least significant bit first.

Formalized by `BitVec.toBoolListLE`, a definition declared in [MathlibExt/Data/BitVec/BoolList.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/BitVec/BoolList.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists/index.html#to-bool-list-le).

## Little-endian Boolean lists are equivalent to bitvectors

Fixed-width little-endian Boolean lists are equivalent to bitvectors of the same width.

Formalized by `BitVec.equivBoolListLE`, a definition declared in [MathlibExt/Data/BitVec/BoolList.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/BitVec/BoolList.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists/index.html#equiv-bool-list-le).

## Sum of a Boolean list counts its true entries

The sum of the natural values of a Boolean list is its number of `true` entries.

Formalized by `List.sum_map_toNat_eq_count_true`, a theorem declared in [MathlibExt/Data/Bool/Count.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Data/Bool/Count.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists/index.html#sum-map-to-nat-eq-count-true).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bitvectors and Boolean lists](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/bitvectors-and-boolean-lists)
