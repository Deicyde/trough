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

- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-02/analytic/the-analytic-implicit-root-theorem.md)
- [Hadamard's lemma along a graph](../../../analysis/part-02/analytic/hadamards-lemma-along-a-graph.md)
- [Identity theorem on the real points](../../../analysis/part-02/analytic/identity-theorem-on-the-real-points.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-02/complex/part-03/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.html#TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented)
- [Source of `TauCeti.exists_isCAD_orderAt_eq_of_isMcCallumWellOriented` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Basic.lean#L379)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
