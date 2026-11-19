---
declaration: def
origin: cited
lean: TauCeti.waldschmidtInterpolationMatrix
statement: formalized
---

# TauCeti.waldschmidtInterpolationMatrix

Waldschmidt's interpolation matrix: the row `r` is the auxiliary function with polynomial
`F r` and exponent `t r`, the column `c` is the differential operator `(P c)(∂/∂z₀)` at the grid
point `s c · y`, and the entry is the coefficient-field factor
`TauCeti.waldschmidtOperatorEntry α b (t r) (s c) (F r) (P c)`.

```lean
TauCeti.waldschmidtInterpolationMatrix.{u_1, u_2, u_3} {n : ℕ} {K : Type u_1} [Field K]
  {ι : Type u_2} {κ : Type u_3} (α b : Fin (n + 1) → K) (F : ι → MvPolynomial (Fin (n + 1)) K)
  (t : ι → ℤ) (P : κ → Polynomial K) (s : κ → Fin (n + 1) → ℤ) : Matrix ι κ K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.waldschmidtInterpolationMatrix`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Matrix.html#TauCeti.waldschmidtInterpolationMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.waldschmidtInterpolationMatrix`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Matrix.html#TauCeti.waldschmidtInterpolationMatrix)
- [Source of `TauCeti.waldschmidtInterpolationMatrix` in TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Matrix.lean#L67)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
