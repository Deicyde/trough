---
declaration: theorem
origin: cited
lean: TauCeti.isSubmersionOfComplement_torusFamilyProjection
statement: formalized
proof: formalized
---

# The projection of a family of tori is a submersion

For a `C^n` family of full lattices,
the projection `(Y × E)/Λ → Y` is a `C^n` submersion with complement `E`: around each point there
are a chart of `(Y × E)/Λ`, given by a local section of the orbit map followed by a product chart
of `Y × E`, and a chart of `Y`, in which the projection is `(u, v) ↦ u`.

```lean
TauCeti.isSubmersionOfComplement_torusFamilyProjection.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {EY : Type u_2} [NormedAddCommGroup EY] [NormedSpace 𝕜 EY]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 EY H} {Y : Type u_4}
  [TopologicalSpace Y] [ChartedSpace H Y] [T2Space Y] [LocallyCompactSpace Y] {Λ : Type u_5}
  [AddCommGroup Λ] {E : Type u_6} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedSpace 𝕜 E] (P : Y → Λ →ₗ[ℤ] E) [∀ (y : Y), DiscreteTopology ↥(P y).range]
  [∀ (y : Y), IsZLattice ℝ (P y).range] (hinj : ∀ (y : Y), Function.Injective ⇑(P y))
  {n : WithTop ℕ∞} [IsManifold I n Y]
  (hP : ∀ (l : Λ), ContMDiff I (modelWithCornersSelf 𝕜 E) n fun y => (P y) l) :
  Manifold.IsSubmersionOfComplement E (I.prod (modelWithCornersSelf 𝕜 E)) I n
    (TauCeti.torusFamilyProjection P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A family of tori is a manifold](a-family-of-tori-is-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSubmersionOfComplement_torusFamilyProjection`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Manifold.html#TauCeti.isSubmersionOfComplement_torusFamilyProjection).

## Sources

- [Tau Ceti documentation: `TauCeti.isSubmersionOfComplement_torusFamilyProjection`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Manifold.html#TauCeti.isSubmersionOfComplement_torusFamilyProjection)
- [Source of `TauCeti.isSubmersionOfComplement_torusFamilyProjection` in TauCeti/Algebra/Module/ZLattice/Family/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/Family/Manifold.lean#L211)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
