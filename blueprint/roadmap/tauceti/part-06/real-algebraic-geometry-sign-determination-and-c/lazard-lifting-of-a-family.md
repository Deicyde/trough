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

- [Circle.fundamentalGroupMulEquiv\_fromPath](../../part-07/universal-covers/circle-fundamentalgroupmulequiv-frompath.md)
- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_lazardDelineation_of_lazardProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.html#TauCeti.nonempty_lazardDelineation_of_lazardProjection).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_lazardDelineation_of_lazardProjection`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.html#TauCeti.nonempty_lazardDelineation_of_lazardProjection)
- [Source of `TauCeti.nonempty_lazardDelineation_of_lazardProjection` in TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Projection/Lazard/Lifting.lean#L140)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
