---
declaration: section
origin: cited
lean: Matrix.bitSinglet, Matrix.bitSwap_eq_one_sub_vecMulVec, Matrix.bitSwapPiece, Matrix.sum_bitSwapPiece, Matrix.bitSwapPiece_eq_zero_of_lt, Matrix.abs_bitSwapPiece_le_choose, Matrix.abs_bitSwapPiece_le_two_pow
statement: formalized
proof: formalized
---

# Decomposition of the bit-swap permutation matrix

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html).

## Antisymmetric two-bit singlet vector

The unnormalized antisymmetric two-bit vector, in order `00, 01, 10, 11`.

Formalized by `Matrix.bitSinglet`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#bit-singlet).

## One-bit swap matrix as identity minus singlet outer product

The one-bit swap matrix is the identity minus the singlet outer product.

Formalized by `Matrix.bitSwap_eq_one_sub_vecMulVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#bit-swap-eq-one-sub-vec-mul-vec).

## Piece of an n-bit swap with i antisymmetric factors

The part of an `n`-bit swap with exactly `i` antisymmetric factors.

Formalized by `Matrix.bitSwapPiece`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#bit-swap-piece).

## Bit-swap pieces sum to the swap permutation matrix

The `n + 1` grouped pieces sum to the permutation matrix swapping the two bit strings.

Formalized by `Matrix.sum_bitSwapPiece`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#sum-bit-swap-piece).

## Bit-swap pieces vanish beyond the number of bits

There is no piece containing more antisymmetric factors than bit positions.

Formalized by `Matrix.bitSwapPiece_eq_zero_of_lt`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#bit-swap-piece-eq-zero-of-lt).

## Binomial entry bound for bit-swap pieces

Each entry of the `i`th piece is bounded by the number of `i`-subsets of the bit positions.

Formalized by `Matrix.abs_bitSwapPiece_le_choose`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#abs-bit-swap-piece-le-choose).

## Uniform power-of-two entry bound for bit-swap pieces

The uniform entry bound used in the source: every piece has absolute value at most `2 ^ n`.

Formalized by `Matrix.abs_bitSwapPiece_le_two_pow`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/BitSwap.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/BitSwap.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html#abs-bit-swap-piece-le-two-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decomposition of the bit-swap permutation matrix](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities/decomposition-of-the-bit-swap-permutation-matrix)
