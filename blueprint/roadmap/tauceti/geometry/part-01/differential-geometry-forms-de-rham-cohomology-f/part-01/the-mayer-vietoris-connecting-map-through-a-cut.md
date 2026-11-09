---
declaration: theorem
origin: cited
lean: TauCeti.deRhamCohomology.mayerVietorisδ_mk_eq_mk_extendByZero
statement: formalized
proof: formalized
---

# The Mayer–Vietoris connecting map through a cut-off function

Let `ρ` be a smooth function
on `U ⊔ V` supported in `V` such that `1 - ρ` is supported in `U`, and let `φ` be a closed form on
`U ⊓ V`. If `σ` is the closed form on `U ⊔ V` extending `d(ρ φ)` by zero
(`TauCeti.exists_closedForms_coe_eq_extendByZero_mextDeriv`), then the connecting map sends the
class of `φ` to the class of `σ`.

```lean
TauCeti.deRhamCohomology.mayerVietorisδ_mk_eq_mk_extendByZero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] {k : ℕ}
  [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  {U V : TopologicalSpace.Opens M} {ρ : ↥(U ⊔ V) → ℝ}
  (hρ : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) ρ) (hρV : tsupport ρ ⊆ {x | ↑x ∈ V})
  (hρU : (tsupport fun x => 1 - ρ x) ⊆ {x | ↑x ∈ U}) (φ : ↥(TauCeti.closedForms I (↥(U ⊓ V)) k))
  (σ : ↥(TauCeti.closedForms I (↥(U ⊔ V)) (k + 1)))
  (hσ :
    ↑↑σ =
      TauCeti.RoughForm.extendByZero (U ⊔ V)
        (TauCeti.mextDeriv fun y => ρ (TopologicalSpace.Opens.inclusion ⋯ y) • ↑↑φ y)) :
  (TauCeti.deRhamCohomology.mayerVietorisδ I U V k) ((TauCeti.deRhamCohomology.mk I k) φ) =
    (TauCeti.deRhamCohomology.mk I (k + 1)) σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris short exact sequence of de Rham complexes](the-mayer-vietoris-short-exact-sequence-of-de-rh.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.deRhamCohomology.mayerVietorisδ_mk_eq_mk_extendByZero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.html#TauCeti.deRhamCohomology.mayerVietoris%CE%B4_mk_eq_mk_extendByZero).

## Sources

- [Tau Ceti documentation: `TauCeti.deRhamCohomology.mayerVietorisδ_mk_eq_mk_extendByZero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.html#TauCeti.deRhamCohomology.mayerVietoris%CE%B4_mk_eq_mk_extendByZero)
- [Source of `TauCeti.deRhamCohomology.mayerVietorisδ_mk_eq_mk_extendByZero` in TauCeti/Geometry/Manifold/DeRham/MayerVietoris.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/MayerVietoris.lean#L517)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
