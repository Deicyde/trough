---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented
statement: formalized
proof: formalized
---

# Correctness of McCallum's projection

A finite family of real polynomials that is
well-oriented in McCallum's sense has a cylindrical algebraic decomposition into analytic
submanifolds, on each cell of which every member of the family has constant ambient order.

```lean
TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented {n : ℕ}
  (polynomialGCD : (m : ℕ) → NormalizedGCDMonoid (MvPolynomial (Fin m) ℝ))
  {F : Finset (MvPolynomial (Fin n) ℝ)} (hF : TauCeti.IsMcCallumWellOriented polynomialGCD n F) :
  ∃ 𝒞,
    TauCeti.IsCAD n 𝒞 ∧
      (∀ E ∈ 𝒞, ∃ d, TauCeti.IsAnalyticSubmanifold d E) ∧
        ∀ f ∈ F, ∀ E ∈ 𝒞, ∀ y ∈ E, ∀ y' ∈ E, f.orderAt y = f.orderAt y'
```

## Depends on

- [TauCeti.IsMcCallumWellOriented](tauceti-ismccallumwelloriented.md)

## Proof depends on

- [Circle.fundamentalGroupMulEquiv\_fromPath](../../part-07/universal-covers/circle-fundamentalgroupmulequiv-frompath.md)
- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented)
- [Source of `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean#L359)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
