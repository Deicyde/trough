---
declaration: section
origin: cited
lean: ParityProduct.evenIndicator, ParityProduct.parityCoeff, ParityProduct.two_mul_parityCoeff, ParityProduct.two_mul_evenIndicator, ParityProduct.sum_powerset_parityCoeff, ParityProduct.prod_evenIndicator_mul_prod_neg_one_pow_modEq
statement: formalized
proof: formalized
---

# Parity products modulo powers of two

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html).

## Even indicator of a natural number

The integer indicator that a natural number is even.

Formalized by `ParityProduct.evenIndicator`, a definition declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#even-indicator).

## Coefficients of the even-indicator expansion

The coefficients of the even-indicator expansion: one at zero and
`(-1) ^ i * 2 ^ (i - 1)` at positive indices.

Formalized by `ParityProduct.parityCoeff`, a definition declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#parity-coeff).

## Twice a parity coefficient is a sign coefficient

Twice the parity coefficient is the sign coefficient, with a correction at zero.

Formalized by `ParityProduct.two_mul_parityCoeff`, a theorem declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#two-mul-parity-coeff).

## Twice the even indicator is one plus the parity sign

Twice the even indicator is one plus the parity sign.

Formalized by `ParityProduct.two_mul_evenIndicator`, a theorem declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#two-mul-even-indicator).

## Subset sum of parity coefficients is the even-cardinality indicator

Summing parity coefficients over all subsets gives the even-cardinality indicator.

Formalized by `ParityProduct.sum_powerset_parityCoeff`, a theorem declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#sum-powerset-parity-coeff).

## Truncated subset expansion of parity products modulo powers of two

A product of even-cardinality indicators and parity signs is congruent to its finite
subset expansion cut off at total degree `M`. Each even-indicator factor costs at most one
power of two, so the cutoff must satisfy `ν - 1 + #J₁ ≤ M`, with `1 ≤ ν`.
Indices outside `J₁ ∪ J₂` select only the empty subset.

Formalized by `ParityProduct.prod_evenIndicator_mul_prod_neg_one_pow_modEq`, a theorem declared in [MathlibExt/Combinatorics/ParityProduct.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/ParityProduct.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html#prod-even-indicator-mul-prod-neg-one-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity products modulo powers of two](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/parity-products-modulo-powers-of-two)
