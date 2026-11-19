---
declaration: theorem
origin: cited
lean: TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker
statement: formalized
proof: formalized
---

# O'Neill's horizontal curvature formula

For horizontal vectors `u` and `w`,
`⟨R_M(u, w) w, u⟩ = ⟨R_N(f_* u, f_* w) f_* w, f_* u⟩ - 3 |A_u w|²`.

```lean
TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker.{u_1, u_2, u_3, u_4,
    u_5, u_6}
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
  inner ℝ (((((CovariantDerivative.leviCivitaConnection I M).curvatureTensor x) u) w) w) u =
    inner ℝ
        (((((CovariantDerivative.leviCivitaConnection J N).curvatureTensor (f x))
              ((mfderiv% f x) u))
            ((mfderiv% f x) w))
          ((mfderiv% f x) w))
        ((mfderiv% f x) u) -
      3 * ‖((h.oneillA x) u) w‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.html#TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.html#TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker)
- [Source of `TauCeti.IsRiemannianSubmersion.inner_curvatureTensor_self_of_mem_orthogonal_ker` in TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Submersion/Curvature.lean#L271)
