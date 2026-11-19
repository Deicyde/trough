---
declaration: theorem
origin: cited
lean: TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative
statement: formalized
proof: formalized
---

# The orbit-torus series labelled by the return maps give the orbit zeta function

Under the
hypotheses of
`TauCeti.SmoothMappingTorus.hasProd_ofPowerSeries_torusWeightSeries_fixedPointDerivative`, the
product of the orbit-torus series labelled by the linearized return maps `D i = d(φ^[d i])_(x i)`
is, over any `ℚ`-algebra `K`, the orbit zeta function
`exp (∑ᵢ ∑_{n ≥ 1} sgn det (1 - d(φ^[d i * n])_(x i)) e^(n [γ_(x i)]) / n)` in
`Nov(K, H₁(Y_φ; ℤ), N)`. The sign `sgn det (1 - d(φ^[d i * n])_(x i))` is the local Lefschetz
index of `x i` as a fixed point of `φ^[d i * n]`.

```lean
TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative.{u_1,
    u_3}
  {E H M : Type} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {φ : Diffeomorph I I M M ↑⊤}
  (hφ : ∀ (N : ℕ), TauCeti.IsNondegenerateUpToPeriod I (⇑φ) N) {ι : Type u_1} {x : ι → M}
  (hx : Function.Injective x) {d : ι → ℕ} (hxd : ∀ (i : ι), Function.IsPeriodicPt (⇑φ) (d i) (x i))
  (hd : ∀ (i : ι), 0 < d i) {σ : TauCeti.SmoothTwoForm I M} (hE : Module.finrank ℝ E = 2)
  (hσ : σ.IsNondegenerate) (hφσ : (TauCeti.SmoothForm.mpullback ⇑φ ⋯) σ = σ) (K : Type u_3)
  [CommRing K] [Algebra ℚ K] :
  (TauCeti.NovikovSeries.orbitZeta K (TauCeti.SmoothMappingTorus.timePeriodHom φ)
      (fun i => TauCeti.SmoothMappingTorus.closedOrbitHomologyClass ⋯) fun i n =>
      ↑(SignType.sign
          (LinearMap.det
            (LinearMap.id - TauCeti.fixedPointDerivative I (⇑φ)^[d i * n] ⟨x i, ⋯⟩)))) =
    (TauCeti.NovikovSeries.mapRingHom (Int.castRingHom K)
        (AddMonoidHom.id
          ↑(HomologicalComplex.homology
              ((TauCeti.singularChains ℤ).obj ↧(TauCeti.SmoothMappingTorus φ)) 1))
        ⋯)
      (∏' (i : ι),
        (TauCeti.NovikovSeries.ofPowerSeries (TauCeti.SmoothMappingTorus.closedOrbitHomologyClass ⋯)
            ⋯)
          (TauCeti.torusWeightSeries
            (decide
              (0 <
                LinearMap.det (LinearMap.id - TauCeti.fixedPointDerivative I (⇑φ)^[d i] ⟨x i, ⋯⟩)))
            (if
                LinearMap.det (LinearMap.id + TauCeti.fixedPointDerivative I (⇑φ)^[d i] ⟨x i, ⋯⟩) <
                  0 then
              1
            else 0)))
```

## Depends on

- [TauCeti.fixedPointDerivative](../../../algebra/part-01/morse-novikov-homology-and-dynamical-reidemeiste/tauceti-fixedpointderivative.md)

## Proof depends on

- [Cayley–Hamilton in size two](../../../linear-algebra/part-01/matrix/cayley-hamilton-in-size-two.md)
- [The fundamental theorem of calculus for line integrals](../../../geometry/part-02/manifold/part-02/the-fundamental-theorem-of-calculus-for-line-int.md)
- [Integrality of the orbit zeta function](../../../algebra/part-01/morse-novikov-homology-and-dynamical-reidemeiste/integrality-of-the-orbit-zeta-function.md)
- [The Poincaré lemma on manifolds](../../../geometry/part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/ClosedOrbit.html#TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/ClosedOrbit.html#TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative)
- [Source of `TauCeti.SmoothMappingTorus.orbitZeta_closedOrbitHomologyClass_eq_mapRingHom_tprod_fixedPointDerivative` in TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/ClosedOrbit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/ClosedOrbit.lean#L222)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
