---
declaration: theorem
origin: cited
lean: TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus along a map with an exact pullback

If a
differentiable map `i : N → M` pulls the one-form `φ` back to the differential of a `C¹` function
`f` on `N`, then the line integral of `φ` along `i ∘ c`, for a `C¹` curve `c` in `N`, is the
difference of the values of `f` at the endpoints of `c`. For instance, `i` may be an exact
Lagrangian map and `f` its primitive.

```lean
TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {E' : Type u_5} {H' : Type u_6}
  {N : Type u_7} [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [TopologicalSpace N] [ChartedSpace H' N]
  {φ : TauCeti.RoughForm I M F 1} {i : N → M} {f : N → F} (hi : MDiff i)
  (hf : ContMDiff J (modelWithCornersSelf ℝ F) 1 f)
  (hφ : TauCeti.mpullback J I i φ = TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction J f))
  {c : ℝ → N} (hc : ContMDiff (modelWithCornersSelf ℝ ℝ) J 1 c) (a b : ℝ) :
  TauCeti.pathIntegral φ (i ∘ c) a b = f (c b) - f (c a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for line integrals](the-fundamental-theorem-of-calculus-for-line-int.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq)
- [Source of `TauCeti.pathIntegral_comp_eq_sub_of_mpullback_eq` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean#L410)
