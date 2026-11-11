---
declaration: theorem
origin: cited
lean: Matrix.inv_add_vecMulVec
statement: formalized
proof: formalized
---

# Sherman–Morrison formula over a commutative ring

The rank-one correction is the
outer product of the updated column and row, divided by the scalar denominator.

```lean
Matrix.inv_add_vecMulVec.{u_1, u_2} {n : Type u_1} {R : Type u_2} [Fintype n] [DecidableEq n]
  [CommRing R] (A : Matrix n n R) (hA : IsUnit A) (u v : n → R)
  (hd : IsUnit (1 + v ⬝ᵥ A⁻¹.mulVec u)) :
  (A + Matrix.vecMulVec u v)⁻¹ =
    A⁻¹ -
      Ring.inverse (1 + v ⬝ᵥ A⁻¹.mulVec u) • Matrix.vecMulVec (A⁻¹.mulVec u) (Matrix.vecMul v A⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.inv_add_vecMulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SchurComplement.html#Matrix.inv_add_vecMulVec).

## Sources

- [Tau Ceti documentation: `Matrix.inv_add_vecMulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/SchurComplement.html#Matrix.inv_add_vecMulVec)
- [Source of `Matrix.inv_add_vecMulVec` in TauCeti/LinearAlgebra/Matrix/SchurComplement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/SchurComplement.lean#L135)
