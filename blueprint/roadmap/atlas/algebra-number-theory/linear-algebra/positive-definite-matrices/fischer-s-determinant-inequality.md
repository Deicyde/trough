---
declaration: section
origin: cited
lean: Matrix.one_le_det_of_posSemidef_sub_one, Matrix.det_le_det_of_posSemidef_le, Matrix.fischer_det_fromBlocks_le, Matrix.fischer_det_fromBlocks_eq_iff
statement: formalized
proof: formalized
---

# Fischer's determinant inequality

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html).

## Determinant at least one when W minus identity is positive semidefinite

If `W - 1` is positive semidefinite, then `1 ≤ det W`, since every
eigenvalue of `W` is at least `1`.

Formalized by `Matrix.one_le_det_of_posSemidef_sub_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html#one-le-det-of-pos-semidef-sub-one).

## Monotonicity of the determinant on the positive semidefinite cone

**Monotonicity of the determinant on the positive semidefinite
cone**: if `S` and `D - S` are positive semidefinite, then
`det S ≤ det D`.

Formalized by `Matrix.det_le_det_of_posSemidef_le`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html#det-le-det-of-pos-semidef-le).

## Fischer's determinant inequality

For a positive semidefinite
block matrix `[[A, B], [Bᴴ, D]]` with real entries,
`det [[A, B], [Bᴴ, D]] ≤ det A * det D`.

Formalized by `Matrix.fischer_det_fromBlocks_le`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html#fischer-det-from-blocks-le).

## Equality case of Fischer's inequality

For `A` and `D`
positive definite and `[[A, B], [Bᴴ, D]]` positive semidefinite,
`det [[A, B], [Bᴴ, D]] = det A * det D` iff `B = 0`.

Formalized by `Matrix.fischer_det_fromBlocks_eq_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/FischerDeterminant.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html#fischer-det-from-blocks-eq-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fischer's determinant inequality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/fischer-s-determinant-inequality)
