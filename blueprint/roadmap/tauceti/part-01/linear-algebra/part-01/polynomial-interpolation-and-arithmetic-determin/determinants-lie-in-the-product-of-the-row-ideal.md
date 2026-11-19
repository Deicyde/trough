---
declaration: theorem
origin: cited
lean: Matrix.det_mem_prod_row_ideals
statement: formalized
proof: formalized
---

# Determinants lie in the product of the row ideals

If every entry of row `i` lies in the
ideal `J i`, then `det A ∈ ∏ i, J i`. The empty product is `⊤`.

```lean
Matrix.det_mem_prod_row_ideals.{u_1, u_3} {m : Type u_1} {R : Type u_3} [CommRing R] [Fintype m]
  [DecidableEq m] (A : Matrix m m R) (J : m → Ideal R) (h : ∀ (i j : m), A i j ∈ J i) :
  A.det ∈ ∏ i, J i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.det_mem_prod_row_ideals`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/IdealDivisibility.html#Matrix.det_mem_prod_row_ideals).

## Sources

- [Tau Ceti documentation: `Matrix.det_mem_prod_row_ideals`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/IdealDivisibility.html#Matrix.det_mem_prod_row_ideals)
- [Source of `Matrix.det_mem_prod_row_ideals` in TauCeti/LinearAlgebra/Matrix/Determinant/IdealDivisibility.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Determinant/IdealDivisibility.lean#L53)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
