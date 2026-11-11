---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection
statement: formalized
proof: formalized
---

# Recursive sign-invariant McCallum correctness

If the McCallum projection of a
squarefree basis of `F` is well-oriented, there is a sign-invariant CAD for `F` with analytic
cells. Its base CAD is order-invariant for that projection. No restriction is imposed on
nullification of the top-level basis, including over positive-dimensional base cells.

```lean
TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection {n : ℕ}
  (polynomialGCD : (m : ℕ) → NormalizedGCDMonoid (MvPolynomial (Fin m) ℝ))
  {F : Finset (MvPolynomial (Fin (n + 1)) ℝ)} {B : Finset (Polynomial (MvPolynomial (Fin n) ℝ))}
  (_hB : (Finset.map (MvPolynomial.finSuccEquiv ℝ n).toEmbedding F).IsSquarefreeBasis B)
  (_hproj :
    TauCeti.IsMcCallumWellOriented polynomialGCD n
      ((Finset.map (MvPolynomial.finSuccEquiv ℝ n).toEmbedding F).mcCallumProjection B)) :
  ∃ 𝒞,
    TauCeti.IsCAD (n + 1) 𝒞 ∧
      (∀ E ∈ 𝒞, ∃ d, TauCeti.IsAnalyticSubmanifold d E) ∧
        (∀ f ∈ F, ∀ E ∈ 𝒞, TauCeti.SignInvariant (fun x => (MvPolynomial.eval x) f) E) ∧
          ∀ q ∈ (Finset.map (MvPolynomial.finSuccEquiv ℝ n).toEmbedding F).mcCallumProjection B,
            ∀ C ∈ Set.image Fin.tail '' 𝒞, ∀ x ∈ C, ∀ y ∈ C, q.orderAt x = q.orderAt y
```

## Depends on

- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-02/analytic/the-analytic-implicit-root-theorem.md)
- [Correctness of McCallum's projection](correctness-of-mccallums-projection.md)
- [Hadamard's lemma along a graph](../../../analysis/part-02/analytic/hadamards-lemma-along-a-graph.md)
- [Identity theorem on the real points](../../../analysis/part-02/analytic/identity-theorem-on-the-real-points.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-02/complex/part-03/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.html#TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.html#TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection)
- [Source of `TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.lean#L41)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
