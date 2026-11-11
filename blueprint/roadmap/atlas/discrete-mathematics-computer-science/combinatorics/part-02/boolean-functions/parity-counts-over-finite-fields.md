---
declaration: section
origin: cited
lean: FiniteField.odd_dotProduct_power_count, FiniteField.odd_dotProduct_power_count_of_sixteen_mul_le, FiniteField.dotProduct_power_count_le_half
statement: formalized
proof: formalized
---

# Parity counts over finite fields

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields/index.html).

## Lower bound on odd-parity pairs in a finite field

Let a finite field be written as `s` binary coordinates.  For a nonempty
set `V` of exponents below `m`, the number of pairs `(a, b)` for which an odd
number of the dot products `bits (a ^ E) ⬝ᵥ bits b` equal one satisfies the
cleared-denominator lower bound

`|F| ^ 2 ≤ 2 * oddPairs + (m - 1) * |F|`.

This is a one-sided odd-frequency estimate.

Formalized by `FiniteField.odd_dotProduct_power_count`, a theorem declared in [MathlibExt/Combinatorics/FiniteField/SmallBias.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/FiniteField/SmallBias.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields/index.html#odd-dot-product-power-count).

## At least 15/32 of field pairs have odd parity

Under `16 * m ≤ 2 ^ s`, at least `15 / 32` of the field pairs have odd
parity across any nonempty exponent set `V`.  Fractions are cleared in the
statement.

Formalized by `FiniteField.odd_dotProduct_power_count_of_sixteen_mul_le`, a theorem declared in [MathlibExt/Combinatorics/FiniteField/SmallBias.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/FiniteField/SmallBias.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields/index.html#odd-dot-product-power-count-of-sixteen-m).

## At most half of field pairs have dot product one

For one exponent `E`, at most half of all field pairs satisfy
`dotProduct (bits (a ^ E)) (bits b) = 1`.

Formalized by `FiniteField.dotProduct_power_count_le_half`, a theorem declared in [MathlibExt/Combinatorics/FiniteField/SmallBias.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/FiniteField/SmallBias.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields/index.html#dot-product-power-count-le-half).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity counts over finite fields](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/parity-counts-over-finite-fields)
