---
declaration: theorem
origin: cited
lean: Matrix.PosSemidef.det_fromBlocks_le
statement: formalized
proof: formalized
---

# Hadamard--Fischer inequality

The determinant of a positive-semidefinite
block matrix is at most the product of the diagonal-block determinants.

```lean
Matrix.PosSemidef.det_fromBlocks_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {m : Type u_2} {n : Type u_3}
  [RCLike 𝕜] [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n] {A : Matrix m m 𝕜}
  {B : Matrix m n 𝕜} {D : Matrix n n 𝕜} (h : (Matrix.fromBlocks A B B.conjTranspose D).PosSemidef) :
  (Matrix.fromBlocks A B B.conjTranspose D).det ≤ A.det * D.det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.PosSemidef.det_fromBlocks_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/Determinant.html#Matrix.PosSemidef.det_fromBlocks_le).

## Sources

- [Tau Ceti documentation: `Matrix.PosSemidef.det_fromBlocks_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/Determinant.html#Matrix.PosSemidef.det_fromBlocks_le)
- [Source of `Matrix.PosSemidef.det_fromBlocks_le` in TauCeti/Analysis/Matrix/PosSemidef/Determinant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/PosSemidef/Determinant.lean#L96)
