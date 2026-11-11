---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_lazardDelineation_of_lazardProjection
statement: formalized
proof: formalized
---

# Lazard lifting of a family

Over a preconnected analytic submanifold on which the Lazard
projection of a family with respect to an irreducible basis is valuation-invariant, the family has
a Lazard delineation. Its members may be nullified at points of the base.

```lean
TauCeti.nonempty_lazardDelineation_of_lazardProjection {n d : ℕ}
  [NormalizedGCDMonoid (MvPolynomial (Fin n) ℝ)]
  {F B : Finset (Polynomial (MvPolynomial (Fin n) ℝ))} {S : Set (Fin n → ℝ)}
  (hB : F.IsIrreducibleBasis B) (hS : TauCeti.IsAnalyticSubmanifold d S) (hconn : IsPreconnected S)
  (hproj :
    ∀ q ∈ F.lazardProjection B, ∀ x ∈ S, ∀ y ∈ S, q.lazardValuation x = q.lazardValuation y) :
  Nonempty
    (TauCeti.LazardDelineation
      (fun f =>
        (MvPolynomial.rename ⇑finSuccEquivLast.symm)
          ((MvPolynomial.optionEquivLeft ℝ (Fin n)).symm ↑f))
      S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-02/analytic/the-analytic-implicit-root-theorem.md)
- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)
- [Hadamard's lemma along a graph](../../../analysis/part-02/analytic/hadamards-lemma-along-a-graph.md)
- [Identity theorem on the real points](../../../analysis/part-02/analytic/identity-theorem-on-the-real-points.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Riemann extension theorem across a coordinate hyperplane](../../../analysis/part-02/complex/part-03/the-riemann-extension-theorem-across-a-coordinat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_lazardDelineation_of_lazardProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.html#TauCeti.nonempty_lazardDelineation_of_lazardProjection).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_lazardDelineation_of_lazardProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.html#TauCeti.nonempty_lazardDelineation_of_lazardProjection)
- [Source of `TauCeti.nonempty_lazardDelineation_of_lazardProjection` in TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.lean#L140)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
