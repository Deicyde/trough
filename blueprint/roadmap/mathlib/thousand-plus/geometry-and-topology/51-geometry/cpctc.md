---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanGeometry.triangle_congruent_iff_dist_eq, EuclideanGeometry.angle_eq_of_congruent
mathlib_file: Mathlib/Geometry/Euclidean/Congruence.lean
---

# CPCTC

Mathlib records this with 2 declarations.

`EuclideanGeometry.triangle_congruent_iff_dist_eq`.

```lean
EuclideanGeometry.triangle_congruent_iff_dist_eq.{u_4, u_5} {P₁ : Type u_4} {P₂ : Type u_5}
  [MetricSpace P₁] [MetricSpace P₂] {t₁ : Fin 3 → P₁} {t₂ : Fin 3 → P₂} :
  Congruent t₁ t₂ ↔ ∀ (i j : Fin 3), dist (t₁ i) (t₁ j) = dist (t₂ i) (t₂ j)
```

`EuclideanGeometry.angle_eq_of_congruent`: Corresponding angles are equal for congruent triangles.

```lean
EuclideanGeometry.angle_eq_of_congruent.{u_1, u_2, u_3, u_4, u_5} {ι : Type u_1} {V₁ : Type u_2}
  {V₂ : Type u_3} {P₁ : Type u_4} {P₂ : Type u_5} [NormedAddCommGroup V₁] [NormedAddCommGroup V₂]
  [InnerProductSpace ℝ V₁] [InnerProductSpace ℝ V₂] [MetricSpace P₁] [MetricSpace P₂]
  [NormedAddTorsor V₁ P₁] [NormedAddTorsor V₂ P₂] {v₁ : ι → P₁} {v₂ : ι → P₂} (h : Congruent v₁ v₂)
  (i j k : ι) :
  EuclideanGeometry.angle (v₁ i) (v₁ j) (v₁ k) = EuclideanGeometry.angle (v₂ i) (v₂ j) (v₂ k)
```

## Depends on

- [Angle](../../../overview/geometry/affine-and-euclidean-geometry/angle.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `EuclideanGeometry.triangle_congruent_iff_dist_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Congruence.html#EuclideanGeometry.triangle_congruent_iff_dist_eq)
- [Source of `EuclideanGeometry.triangle_congruent_iff_dist_eq` in Mathlib/Geometry/Euclidean/Congruence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Congruence.lean#L46)
- [Mathlib documentation: `EuclideanGeometry.angle_eq_of_congruent`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Congruence.html#EuclideanGeometry.angle_eq_of_congruent)
- [Source of `EuclideanGeometry.angle_eq_of_congruent` in Mathlib/Geometry/Euclidean/Congruence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Congruence.lean#L108)
- [1000+ theorems list: Q154210](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L62)
- [1000+ theorems project: Q154210](https://1000-plus.github.io/all.html?length=-1#Q154210)
- [Wikipedia: CPCTC](https://en.wikipedia.org/wiki/CPCTC)
- [Wikidata: Q154210](https://www.wikidata.org/wiki/Q154210)
