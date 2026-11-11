---
declaration: theorem
origin: cited
lean: TauCeti.contMDiff_section_orbitRelQuotientRec_iff
statement: formalized
proof: formalized
---

# TauCeti.contMDiff_section_orbitRelQuotientRec_iff

For a free properly discontinuous action by `C^n` maps on a `C^n` manifold and `m ≤ n`, the
descent of an invariant section is `C^m` exactly when the section upstairs is. For holomorphic
actions on complex manifolds, this is the holomorphic descent of invariant holomorphic
sections.

```lean
TauCeti.contMDiff_section_orbitRelQuotientRec_iff.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {G : Type u_1}
  {M : Type u_2} [Group G] [MulAction G M] [TopologicalSpace M] {F : Type u_3}
  {V : MulAction.orbitRel.Quotient G M → Type u_4} {t : (x : M) → V ⟦x⟧}
  {ht : ∀ (g : G) (x : M), t (g • x) ≍ t x} {𝕜 : Type u_5} [NontriviallyNormedField 𝕜]
  {E : Type u_6} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_7} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} [ChartedSpace H M] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [TopologicalSpace (Bundle.TotalSpace F V)]
  [(q : MulAction.orbitRel.Quotient G M) → TopologicalSpace (V q)] {m n : WithTop ℕ∞}
  [ProperlyDiscontinuousSMul G M] [ContinuousConstSMul G M] [IsCancelSMul G M] [T2Space M]
  [LocallyCompactSpace M] [IsManifold I n M] [ContMDiffConstSMul I n G M] [FiberBundle F V]
  (hm : m ≤ n) :
  (ContMDiff I (I.prod (modelWithCornersSelf 𝕜 F)) m fun q =>
      ⟨q, TauCeti.MulAction.orbitRelQuotientRec t ht q⟩) ↔
    ContMDiff I (I.prod (modelWithCornersSelf 𝕜 F)) m fun x => ⟨⟦x⟧, t x⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.contMDiff_section_orbitRelQuotientRec_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Section.html#TauCeti.contMDiff_section_orbitRelQuotientRec_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.contMDiff_section_orbitRelQuotientRec_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Section.html#TauCeti.contMDiff_section_orbitRelQuotientRec_iff)
- [Source of `TauCeti.contMDiff_section_orbitRelQuotientRec_iff` in TauCeti/Geometry/Manifold/Quotient/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Quotient/Section.lean#L85)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
