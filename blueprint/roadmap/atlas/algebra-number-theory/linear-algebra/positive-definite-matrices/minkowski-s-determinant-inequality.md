---
declaration: section
origin: cited
lean: Matrix.PosSemidef.minkowski_det, Matrix.PosSemidef.det_le_det_add
statement: formalized
proof: formalized
---

# Minkowski's determinant inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html).

## Minkowski's determinant inequality

For positive semidefinite
`A` and `B`,
`(det (A + B)) ^ (1 / n) ≥ (det A) ^ (1 / n) + (det B) ^ (1 / n)`.

Formalized by `Matrix.PosSemidef.minkowski_det`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html#minkowski-det).

## Monotonicity of the determinant on the positive semidefinite cone

`det B ≤ det (A + B)` for `A` and `B` positive semidefinite.

Formalized by `Matrix.PosSemidef.det_le_det_add`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html#det-le-det-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minkowski's determinant inequality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality)
