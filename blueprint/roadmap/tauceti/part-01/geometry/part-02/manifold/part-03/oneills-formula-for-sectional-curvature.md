---
declaration: theorem
origin: cited
lean: TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv
statement: formalized
proof: formalized
---

# O'Neill's formula for sectional curvature

The image under `f_*` of the plane spanned by
horizontal vectors `u` and `w` has sectional curvature larger by `3 |A_u w|² / |u ∧ w|²`. For an
orthonormal pair this is `K_N(f_* u, f_* w) = K_M(u, w) + 3 |A_u w|²`. On a dependent pair both
sides are zero.

```lean
TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] {G : Type u_5} [TopologicalSpace G] {J : ModelWithCorners ℝ F G}
  {N : Type u_6} [TopologicalSpace N] [ChartedSpace G N] [IsManifold J (↑⊤) N]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [Bundle.RiemannianBundle fun y => TangentSpace J y]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle J (↑⊤) F fun y => TangentSpace J y] {f : M → N}
  (h : TauCeti.IsRiemannianSubmersion I J f) [T2Space M] [T2Space N] {x : M}
  {u w : TangentSpace I x} (hu : u ∈ (↑(mfderiv% f x)).kerᗮ) (hw : w ∈ (↑(mfderiv% f x)).kerᗮ) :
  (CovariantDerivative.leviCivitaConnection J N).sectionalCurvature ⋯ (f x) ((mfderiv% f x) u)
      ((mfderiv% f x) w) =
    (CovariantDerivative.leviCivitaConnection I M).sectionalCurvature ⋯ x u w +
      3 * ‖((h.oneillA x) u) w‖ ^ 2 / (Matrix.gram ℝ ![u, w]).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](the-koszul-formula.md)
- [O'Neill's horizontal curvature formula](oneills-horizontal-curvature-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.html#TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.html#TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv)
- [Source of `TauCeti.IsRiemannianSubmersion.sectionalCurvature_mfderiv` in TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.lean#L284)
