---
declaration: theorem
origin: cited
lean: TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton
statement: formalized
proof: formalized
---

# Uniqueness of Wasserstein geodesics

Let `X` be a complete separable metric space and
`1 < p < ∞`. Suppose that every optimal coupling of `μ` and `ν` for the cost `d ^ p` is `π`, and
that `π`-almost every pair of points of `X` is joined by at most one geodesic path. Then any two
geodesic segments of `P_p (X)` from `μ` to `ν` agree on `[0, 1]`.

```lean
TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton.{u_1} {p : ENNReal}
  [Fact (1 ≤ p)] {X : Type u_1} [MetricSpace X] [CompleteSpace X] [SecondCountableTopology X]
  [MeasurableSpace X] [BorelSpace X] (hp1 : 1 < p) (hp : p ≠ ⊤) {μ ν : TauCeti.WassersteinSpace p X}
  {π : MeasureTheory.Measure (X × X)}
  (hπ :
    ∀ (π' : MeasureTheory.Measure (X × X)),
      TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ p.toReal) π' ↑↑μ ↑↑ν → π' = π)
  (hgeo : ∀ᵐ (z : X × X) ∂π, {c | c ∈ TauCeti.geodesicPaths X ∧ c 0 = z.1 ∧ c 1 = z.2}.Subsingleton)
  {γ γ' : ℝ → TauCeti.WassersteinSpace p X} (h : TauCeti.IsGeodesicSegment γ μ ν)
  (h' : TauCeti.IsGeodesicSegment γ' μ ν) : Set.EqOn γ γ' (Set.Icc 0 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lisini's superposition principle](lisinis-superposition-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Unique.html#TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton).

## Sources

- [Tau Ceti documentation: `TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Unique.html#TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton)
- [Source of `TauCeti.WassersteinSpace.eqOn_of_isGeodesicSegment_of_ae_subsingleton` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Unique.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Unique.lean#L81)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
