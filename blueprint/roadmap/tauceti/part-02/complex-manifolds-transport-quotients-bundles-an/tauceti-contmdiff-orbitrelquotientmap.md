---
declaration: theorem
origin: cited
lean: TauCeti.contMDiff_orbitRelQuotientMap
statement: formalized
proof: formalized
---

# TauCeti.contMDiff\_orbitRelQuotientMap

For free properly discontinuous actions by `C^n` maps on `C^n` manifolds and `m ≤ n`, a
`C^m` map carrying one action to the other along `σ` induces a `C^m` map of orbit spaces.

```lean
TauCeti.contMDiff_orbitRelQuotientMap.{u_1, u_2, u_4, u_5, u_6, u_7, u_8, u_9, u_10} {G : Type u_1}
  {M : Type u_2} [Group G] [MulAction G M] [TopologicalSpace M] {𝕜 : Type u_4}
  [NontriviallyNormedField 𝕜] {E : Type u_5} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_6}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} [ChartedSpace H M] {E' : Type u_7}
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] {H' : Type u_8} [TopologicalSpace H']
  {I' : ModelWithCorners 𝕜 E' H'} {m n : WithTop ℕ∞} [ProperlyDiscontinuousSMul G M]
  [ContinuousConstSMul G M] [IsCancelSMul G M] [T2Space M] [LocallyCompactSpace M]
  [IsManifold I n M] [ContMDiffConstSMul I n G M] {K : Type u_9} {N' : Type u_10} [Group K]
  [MulAction K N'] [TopologicalSpace N'] [ChartedSpace H' N'] [ProperlyDiscontinuousSMul K N']
  [ContinuousConstSMul K N'] [IsCancelSMul K N'] [T2Space N'] [LocallyCompactSpace N']
  [IsManifold I' n N'] [ContMDiffConstSMul I' n K N'] {σ : G → K} (hm : m ≤ n) {φ : M →ₑ[σ] N'}
  (hφ : ContMDiff I I' m ⇑φ) : ContMDiff I I' m φ.orbitRelQuotientMap
```

## Depends on

- [Descent of an invariant map to the orbit space](descent-of-an-invariant-map-to-the-orbit-space.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.contMDiff_orbitRelQuotientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Descent.html#TauCeti.contMDiff_orbitRelQuotientMap).

## Sources

- [Tau Ceti documentation: `TauCeti.contMDiff_orbitRelQuotientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Descent.html#TauCeti.contMDiff_orbitRelQuotientMap)
- [Source of `TauCeti.contMDiff_orbitRelQuotientMap` in TauCeti/Geometry/Manifold/Quotient/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Quotient/Descent.lean#L97)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
