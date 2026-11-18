---
declaration: theorem
origin: cited
lean: TauCeti.isManifold_torusFamily
statement: formalized
proof: formalized
---

# A family of tori is a manifold

For a `C^n` family of full lattices, the orbit space
`(Y × E)/Λ` of the period translation action is a `C^n` manifold for the quotient atlas.

```lean
TauCeti.isManifold_torusFamily.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {EY : Type u_2} [NormedAddCommGroup EY] [NormedSpace 𝕜 EY]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 EY H} {Y : Type u_4}
  [TopologicalSpace Y] [ChartedSpace H Y] [T2Space Y] [LocallyCompactSpace Y] {Λ : Type u_5}
  [AddCommGroup Λ] {E : Type u_6} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedSpace 𝕜 E] (P : Y → Λ →ₗ[ℤ] E) [∀ (y : Y), DiscreteTopology ↥(P y).range]
  [∀ (y : Y), IsZLattice ℝ (P y).range] (hinj : ∀ (y : Y), Function.Injective ⇑(P y))
  {n : WithTop ℕ∞} [IsManifold I n Y]
  (hP : ∀ (l : Λ), ContMDiff I (modelWithCornersSelf 𝕜 E) n fun y => (P y) l) :
  IsManifold (I.prod (modelWithCornersSelf 𝕜 E)) n (AddAction.orbitRel.Quotient Λ (Y × E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isManifold_torusFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Manifold.html#TauCeti.isManifold_torusFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.isManifold_torusFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Manifold.html#TauCeti.isManifold_torusFamily)
- [Source of `TauCeti.isManifold_torusFamily` in TauCeti/Algebra/Module/ZLattice/Family/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Module/ZLattice/Family/Manifold.lean#L183)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexTori/STATUS.md)
