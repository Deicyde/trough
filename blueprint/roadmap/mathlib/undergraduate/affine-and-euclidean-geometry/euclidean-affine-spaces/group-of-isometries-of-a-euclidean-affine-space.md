---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: AffineIsometryEquiv.instGroup
mathlib_file: Mathlib/Analysis/Normed/Affine/Isometry.lean
---

# Group of isometries of a Euclidean affine space

The group of affine isometries of a `NormedAddTorsor`, `P`.

```lean
AffineIsometryEquiv.instGroup.{u_1, u_2, u_7} {𝕜 : Type u_1} {V : Type u_2} {P : Type u_7}
  [NormedField 𝕜] [SeminormedAddCommGroup V] [NormedSpace 𝕜 V] [PseudoMetricSpace P]
  [NormedAddTorsor V P] : Group (P ≃ᵃⁱ[𝕜] P)
```

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Isometries of a Euclidean affine space](isometries-of-a-euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `AffineIsometryEquiv.instGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Affine/Isometry.html#AffineIsometryEquiv.instGroup)
- [Source of `AffineIsometryEquiv.instGroup` in Mathlib/Analysis/Normed/Affine/Isometry.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Affine/Isometry.lean#L594)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L260)
