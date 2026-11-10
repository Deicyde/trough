---
declaration: theorem
origin: cited
lean: VectorField.jacobi_identity_mlieBracket_apply
statement: formalized
proof: formalized
---

# VectorField.jacobi_identity_mlieBracket_apply

The **Jacobi identity** for the manifold Lie bracket, in cyclic form:
`[U, [V, W]] + [V, [W, U]] + [W, [U, V]] = 0`. This rearranges Mathlib's Leibniz form
`leibniz_identity_mlieBracket_apply`.

```lean
VectorField.jacobi_identity_mlieBracket_apply.{u_1, u_2, u_4, u_5} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {H : Type u_4} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_5}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (minSmoothness 𝕜 3) M]
  {U V W : (y : M) → TangentSpace I y} {x : M}
  (hU : ContMDiffAt I I.tangent (minSmoothness 𝕜 2) (fun y => ⟨y, U y⟩) x)
  (hV : ContMDiffAt I I.tangent (minSmoothness 𝕜 2) (fun y => ⟨y, V y⟩) x)
  (hW : ContMDiffAt I I.tangent (minSmoothness 𝕜 2) (fun y => ⟨y, W y⟩) x) :
  VectorField.mlieBracket I U (VectorField.mlieBracket I V W) x +
        VectorField.mlieBracket I V (VectorField.mlieBracket I W U) x +
      VectorField.mlieBracket I W (VectorField.mlieBracket I U V) x =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`VectorField.jacobi_identity_mlieBracket_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorField/LieBracket.html#VectorField.jacobi_identity_mlieBracket_apply).

## Sources

- [Tau Ceti documentation: `VectorField.jacobi_identity_mlieBracket_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorField/LieBracket.html#VectorField.jacobi_identity_mlieBracket_apply)
- [Source of `VectorField.jacobi_identity_mlieBracket_apply` in TauCeti/Geometry/Manifold/VectorField/LieBracket.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorField/LieBracket.lean#L314)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
