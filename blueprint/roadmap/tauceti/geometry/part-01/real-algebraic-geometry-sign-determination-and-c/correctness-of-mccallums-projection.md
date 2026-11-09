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

- [The analytic implicit root theorem](../../../analysis/part-01/analytic/the-analytic-implicit-root-theorem.md)
- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)
- [Hadamard's lemma along a graph](../../../analysis/part-01/analytic/hadamards-lemma-along-a-graph.md)
- [Identity theorem on the real points](../../../analysis/part-01/real-analytic-geometry-and-semianalytic-triangul/identity-theorem-on-the-real-points.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-02/complex/part-02/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented)
- [Source of `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean#L359)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
