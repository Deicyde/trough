---
declaration: def
origin: cited
lean: TauCeti.IsMcCallumWellOriented
statement: formalized
---

# TauCeti.IsMcCallumWellOriented

A finite family `F` of real polynomials in `n` variables is *well-oriented* in McCallum's
sense if, when `n` is positive, singling out the distinguished variable `X 0` gives a family with
a squarefree basis `B` such that each member of `B` is nullified at only finitely many points of
`ℝ ^ (n - 1)`, and the McCallum projection of the family with respect to `B` is again
well-oriented. Every family of constants is well-oriented.

```lean
TauCeti.IsMcCallumWellOriented
  (polynomialGCD : (m : ℕ) → NormalizedGCDMonoid (MvPolynomial (Fin m) ℝ)) (n : ℕ) :
  Finset (MvPolynomial (Fin n) ℝ) → Prop
```

## Depends on

- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.IsMcCallumWellOriented).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.IsMcCallumWellOriented)
- [Source of `TauCeti.IsMcCallumWellOriented` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean#L296)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
