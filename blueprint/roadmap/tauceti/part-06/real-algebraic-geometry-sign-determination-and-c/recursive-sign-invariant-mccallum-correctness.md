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
- [TauCeti.IsMcCallumWellOriented](tauceti-ismccallumwelloriented.md)

## Proof depends on

- [Circle.fundamentalGroupMulEquiv\_fromPath](../../part-07/universal-covers/circle-fundamentalgroupmulequiv-frompath.md)
- [Correctness of McCallum's projection](correctness-of-mccallums-projection.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.html#TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.html#TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection)
- [Source of `TauCeti.exists_isCAD_signInvariant_of_isMcCallumWellOriented_projection` in TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/McCallum/Existence.lean#L41)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
