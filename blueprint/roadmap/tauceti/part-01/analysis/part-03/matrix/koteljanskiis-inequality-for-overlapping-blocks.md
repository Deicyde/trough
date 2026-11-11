---
declaration: theorem
origin: cited
lean: Matrix.PosSemidef.det_mul_det_fromBlocks_le
statement: formalized
proof: formalized
---

# Koteljanskii's inequality for overlapping blocks

The product of the
principal minors on the common block and on all three blocks is bounded by the
product of the two intermediate principal minors. No block need be nonsingular.

```lean
Matrix.PosSemidef.det_mul_det_fromBlocks_le.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {m : Type u_2}
  {n : Type u_3} {p : Type u_4} [RCLike 𝕜] [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
  [Fintype p] [DecidableEq p] {A : Matrix m m 𝕜} {B : Matrix m n 𝕜} {C : Matrix m p 𝕜}
  {D : Matrix n n 𝕜} {E : Matrix n p 𝕜} {F : Matrix p p 𝕜}
  (h :
    (Matrix.fromBlocks A (B.fromCols C) (B.fromCols C).conjTranspose
        (Matrix.fromBlocks D E E.conjTranspose F)).PosSemidef) :
  A.det *
      (Matrix.fromBlocks A (B.fromCols C) (B.fromCols C).conjTranspose
          (Matrix.fromBlocks D E E.conjTranspose F)).det ≤
    (Matrix.fromBlocks A B B.conjTranspose D).det * (Matrix.fromBlocks A C C.conjTranspose F).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard--Fischer inequality](hadamard-fischer-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.PosSemidef.det_mul_det_fromBlocks_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/Determinant.html#Matrix.PosSemidef.det_mul_det_fromBlocks_le).

## Sources

- [Tau Ceti documentation: `Matrix.PosSemidef.det_mul_det_fromBlocks_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/Determinant.html#Matrix.PosSemidef.det_mul_det_fromBlocks_le)
- [Source of `Matrix.PosSemidef.det_mul_det_fromBlocks_le` in TauCeti/Analysis/Matrix/PosSemidef/Determinant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/PosSemidef/Determinant.lean#L120)
