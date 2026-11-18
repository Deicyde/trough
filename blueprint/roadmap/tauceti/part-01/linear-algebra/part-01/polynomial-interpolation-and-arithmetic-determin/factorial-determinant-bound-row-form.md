---
declaration: theorem
origin: cited
lean: Matrix.abv_det_le_factorial_prod
statement: formalized
proof: formalized
---

# Factorial determinant bound, row form

If row `i` of `A` is bounded entrywise in `abv` by
`b i`, then `abv A.det ≤ n! · ∏ i, b i`, where `n` is the size of the matrix. This refines
Mathlib's uniform `Matrix.det_le` to row-dependent bounds.

```lean
Matrix.abv_det_le_factorial_prod.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} [CommRing R]
  [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {n : Type u_3} [Fintype n] [DecidableEq n]
  (A : Matrix n n R) (abv : AbsoluteValue R S) {b : n → S} (hA : ∀ (i j : n), abv (A i j) ≤ b i) :
  abv A.det ≤ ↑(Fintype.card n).factorial * ∏ i, b i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.abv_det_le_factorial_prod`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_factorial_prod).

## Sources

- [Tau Ceti documentation: `Matrix.abv_det_le_factorial_prod`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_factorial_prod)
- [Source of `Matrix.abv_det_le_factorial_prod` in TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean#L170)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
