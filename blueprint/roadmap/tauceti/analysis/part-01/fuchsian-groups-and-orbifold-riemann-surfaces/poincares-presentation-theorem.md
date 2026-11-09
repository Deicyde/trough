---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective, TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.ker_lift_generatorsIn_eq_normalClosure_relators, TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_injective
statement: formalized
proof: formalized
---

# Poincaré's presentation theorem

The group of a locally finite fundamental polygon is
presented by the side generators, the side relations, and the finite-vertex cycle relations.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective {n : ℕ} [NeZero n]
  {P : TauCeti.UpperHalfPlane.ConvexPolygon n} (σ : P.SidePairing)
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hmap : ∀ (i : Fin n), σ.map i ∈ Γ)
  (hlf : LocallyFinite fun γ => ↑γ • P.carrier)
  (hdisj : ∀ (γ : ↥Γ), γ ≠ 1 → Disjoint (↑γ • interior P.carrier) (interior P.carrier)) :
  Function.Bijective ⇑(σ.relatorQuotientTo hmap)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Macbeath's theorem](../../../topology/algebra/part-01/macbeaths-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective).

## Other forms

**Poincaré's presentation theorem, as a description of the relations.** Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.ker_lift_generatorsIn_eq_normalClosure_relators`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.ker_lift_generatorsIn_eq_normalClosure_relators).

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.ker_lift_generatorsIn_eq_normalClosure_relators
  {n : ℕ} [NeZero n] {P : TauCeti.UpperHalfPlane.ConvexPolygon n} (σ : P.SidePairing)
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hmap : ∀ (i : Fin n), σ.map i ∈ Γ)
  (hlf : LocallyFinite fun γ => ↑γ • P.carrier)
  (hdisj : ∀ (γ : ↥Γ), γ ≠ 1 → Disjoint (↑γ • interior P.carrier) (interior P.carrier)) :
  (FreeGroup.lift (σ.generatorsIn hmap)).ker = Subgroup.normalClosure σ.relators
```

**Poincaré's presentation theorem.** Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_injective`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_injective).

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_injective {n : ℕ} [NeZero n]
  {P : TauCeti.UpperHalfPlane.ConvexPolygon n} (σ : P.SidePairing)
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hmap : ∀ (i : Fin n), σ.map i ∈ Γ)
  (hlf : LocallyFinite fun γ => ↑γ • P.carrier)
  (hdisj : ∀ (γ : ↥Γ), γ ≠ 1 → Disjoint (↑γ • interior P.carrier) (interior P.carrier)) :
  Function.Injective ⇑(σ.relatorQuotientTo hmap)
```

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.relatorQuotientTo_bijective` in TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/Presentation.lean#L470)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
