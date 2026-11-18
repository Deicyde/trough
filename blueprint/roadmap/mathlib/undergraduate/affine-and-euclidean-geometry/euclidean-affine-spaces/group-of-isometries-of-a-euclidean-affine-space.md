# Group of isometries of a Euclidean affine space

The group of affine isometries of a `NormedAddTorsor`, `P`.

```lean
AffineIsometryEquiv.instGroup.{u_1, u_2, u_7} {𝕜 : Type u_1} {V : Type u_2} {P : Type u_7}
  [NormedField 𝕜] [SeminormedAddCommGroup V] [NormedSpace 𝕜 V] [PseudoMetricSpace P]
  [NormedAddTorsor V P] : Group (P ≃ᵃⁱ[𝕜] P)
```

## Depends on

- [Isometries of a Euclidean affine space](isometries-of-a-euclidean-affine-space.md)

## Sources

- [Mathlib documentation: `AffineIsometryEquiv.instGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Affine/Isometry.html#AffineIsometryEquiv.instGroup)
- [Source of `AffineIsometryEquiv.instGroup` in Mathlib/Analysis/Normed/Affine/Isometry.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Normed/Affine/Isometry.lean#L618)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L260)
