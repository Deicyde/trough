---
declaration: section
origin: cited
lean: Matrix.PosSemidef.minkowski_det, Matrix.PosSemidef.det_le_det_add
statement: formalized
proof: formalized
---

# Minkowski's determinant inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html).

## Minkowski's determinant inequality

For positive semidefinite
`A` and `B`,
`(det (A + B)) ^ (1 / n) ≥ (det A) ^ (1 / n) + (det B) ^ (1 / n)`.

Formalized by `Matrix.PosSemidef.minkowski_det`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html#minkowski-det).

## Monotonicity of the determinant on the positive semidefinite cone

`det B ≤ det (A + B)` for `A` and `B` positive semidefinite.

Formalized by `Matrix.PosSemidef.det_le_det_add`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MinkowskiDeterminant.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html#det-le-det-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minkowski's determinant inequality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/minkowski-s-determinant-inequality)
