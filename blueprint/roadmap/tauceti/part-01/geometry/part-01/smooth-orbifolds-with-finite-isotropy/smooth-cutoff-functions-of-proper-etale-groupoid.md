---
declaration: theorem
origin: cited
lean: TauCeti.Quiver.exists_isCutoff_contMDiff
statement: formalized
proof: formalized
---

# Smooth cutoff functions of proper étale groupoids

A groupoid whose objects form a
Hausdorff σ-compact finite-dimensional real manifold, whose total arrows form a Hausdorff manifold,
whose source and target are `C^n` local diffeomorphisms, and whose source-target map is proper, has
a `C^n` cutoff function.

```lean
TauCeti.Quiver.exists_isCutoff_contMDiff.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {E' : Type u_3} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] {H' : Type u_4} [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  {C : Type u_5} [CategoryTheory.Groupoid C] [TopologicalSpace C] [ChartedSpace H C]
  [IsManifold I (↑⊤) C] [T2Space C] [SigmaCompactSpace C] [TopologicalSpace (Quiver.Total C)]
  [ChartedSpace H' (Quiver.Total C)] [T2Space (Quiver.Total C)] {n : ℕ∞}
  (hp : IsProperMap fun a => (a.left, a.right)) (hs : IsLocalDiffeomorph J I (↑n) Quiver.Total.left)
  (ht : IsLocalDiffeomorph J I (↑n) Quiver.Total.right) :
  ∃ c, TauCeti.Quiver.IsCutoff c ∧ ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑n) c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Quiver.exists_isCutoff_contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Groupoid/Cutoff.html#TauCeti.Quiver.exists_isCutoff_contMDiff).

## Sources

- [Tau Ceti documentation: `TauCeti.Quiver.exists_isCutoff_contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Groupoid/Cutoff.html#TauCeti.Quiver.exists_isCutoff_contMDiff)
- [Source of `TauCeti.Quiver.exists_isCutoff_contMDiff` in TauCeti/Geometry/Manifold/Groupoid/Cutoff.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Groupoid/Cutoff.lean#L94)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
