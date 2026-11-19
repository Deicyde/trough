---
declaration: structure
origin: cited
lean: TauCeti.PrimeBoundaryRemainder
statement: formalized
---

# Boundary data for the prime Dirichlet series of `S`

The function `series` is the sum
of the Dirichlet series of `primeVonMangoldtCoeff K S` on `Re s > 1`.  The function `remainder`
is continuous on `Re s ≥ 1` and agrees on the open half-plane with
`series s - δ / (s - 1)`.

The functions have precisely their mathematically relevant domains, so the structure carries no
arbitrary values elsewhere.

```lean
TauCeti.PrimeBoundaryRemainder.{u_2} (K : Type u_2) [Field K] [NumberField K]
  (S : Set (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))) (δ : ℝ) : Type
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PrimeBoundaryRemainder`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.PrimeBoundaryRemainder).

## Sources

- [Tau Ceti documentation: `TauCeti.PrimeBoundaryRemainder`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.PrimeBoundaryRemainder)
- [Source of `TauCeti.PrimeBoundaryRemainder` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean#L65)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ArithmeticDirichletSeries/STATUS.md)
