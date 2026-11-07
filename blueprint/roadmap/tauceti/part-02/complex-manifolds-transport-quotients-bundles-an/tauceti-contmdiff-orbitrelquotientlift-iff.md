---
declaration: theorem
origin: cited
lean: TauCeti.contMDiff_orbitRelQuotientLift_iff
statement: formalized
proof: formalized
---

# TauCeti.contMDiff\_orbitRelQuotientLift\_iff

For a free properly discontinuous action by `C^n` maps on a `C^n` manifold and `m ≤ n`, the
descent of a `G`-invariant map is `C^m` exactly when the map is. For holomorphic actions on complex
manifolds, this is the holomorphic descent of invariant holomorphic maps.

```lean
TauCeti.contMDiff_orbitRelQuotientLift_iff.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8} {G : Type u_1}
  {M : Type u_2} {N : Type u_3} [Group G] [MulAction G M] [TopologicalSpace M] [TopologicalSpace N]
  {f : M → N} {hf : ∀ (g : G) (x : M), f (g • x) = f x} {𝕜 : Type u_4} [NontriviallyNormedField 𝕜]
  {E : Type u_5} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_6} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} [ChartedSpace H M] {E' : Type u_7} [NormedAddCommGroup E']
  [NormedSpace 𝕜 E'] {H' : Type u_8} [TopologicalSpace H'] {I' : ModelWithCorners 𝕜 E' H'}
  [ChartedSpace H' N] {m n : WithTop ℕ∞} [ProperlyDiscontinuousSMul G M] [ContinuousConstSMul G M]
  [IsCancelSMul G M] [T2Space M] [LocallyCompactSpace M] [IsManifold I n M]
  [ContMDiffConstSMul I n G M] (hm : m ≤ n) :
  ContMDiff I I' m (TauCeti.MulAction.orbitRelQuotientLift f hf) ↔ ContMDiff I I' m f
```

## Depends on

- [Descent of an invariant map to the orbit space](descent-of-an-invariant-map-to-the-orbit-space.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.contMDiff_orbitRelQuotientLift_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Descent.html#TauCeti.contMDiff_orbitRelQuotientLift_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.contMDiff_orbitRelQuotientLift_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Descent.html#TauCeti.contMDiff_orbitRelQuotientLift_iff)
- [Source of `TauCeti.contMDiff_orbitRelQuotientLift_iff` in TauCeti/Geometry/Manifold/Quotient/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Quotient/Descent.lean#L82)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
