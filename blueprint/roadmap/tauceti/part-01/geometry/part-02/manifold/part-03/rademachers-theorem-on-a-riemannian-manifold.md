---
declaration: theorem
origin: cited
lean: LipschitzWith.ae_mdifferentiableAt, LocallyLipschitz.ae_mdifferentiableAt, LocallyLipschitzOn.ae_mdifferentiableAt_of_mem, LocallyLipschitzOn.isNullSet_setOf_not_mdifferentiableAt
statement: formalized
proof: formalized
---

# Rademacher's theorem on a Riemannian manifold

On a Lindelöf manifold, a Lipschitz map is
differentiable almost everywhere for the Riemannian volume.

```lean
LipschitzWith.ae_mdifferentiableAt.{u_1, u_2, u_3, u_4} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [PseudoEMetricSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsRiemannianManifold I M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [FiniteDimensional ℝ E] {F : Type u_4}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : M → F} [MeasurableSpace M]
  [BorelSpace M] [LindelofSpace M] {K : NNReal} (hf : LipschitzWith K f) :
  ∀ᵐ (x : M) ∂TauCeti.riemannianVolume I M, MDiffAt f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../../../analysis/part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`LipschitzWith.ae_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Rademacher.html#LipschitzWith.ae_mdifferentiableAt).

## Other forms

**Rademacher's theorem on a Riemannian manifold.** Formalized in Tau Ceti as [`LocallyLipschitz.ae_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Rademacher.html#LocallyLipschitz.ae_mdifferentiableAt).

```lean
LocallyLipschitz.ae_mdifferentiableAt.{u_1, u_2, u_3, u_4} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [PseudoEMetricSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsRiemannianManifold I M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [FiniteDimensional ℝ E] {F : Type u_4}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : M → F} [MeasurableSpace M]
  [BorelSpace M] [LindelofSpace M] (hf : LocallyLipschitz f) :
  ∀ᵐ (x : M) ∂TauCeti.riemannianVolume I M, MDiffAt f x
```

**Rademacher's theorem on a Riemannian manifold.** Formalized in Tau Ceti as [`LocallyLipschitzOn.ae_mdifferentiableAt_of_mem`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Rademacher.html#LocallyLipschitzOn.ae_mdifferentiableAt_of_mem).

```lean
LocallyLipschitzOn.ae_mdifferentiableAt_of_mem.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [PseudoEMetricSpace M] [ChartedSpace H M]
  [IsManifold I 1 M] [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsRiemannianManifold I M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {U : Set M} [FiniteDimensional ℝ E]
  {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : M → F}
  [MeasurableSpace M] [BorelSpace M] [LindelofSpace M] (hf : LocallyLipschitzOn U f)
  (hU : IsOpen U) : ∀ᵐ (x : M) ∂TauCeti.riemannianVolume I M, x ∈ U → MDiffAt f x
```

**Rademacher's theorem on a Riemannian manifold, chartwise form.** Formalized in Tau Ceti as [`LocallyLipschitzOn.isNullSet_setOf_not_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Rademacher.html#LocallyLipschitzOn.isNullSet_setOf_not_mdifferentiableAt).

```lean
LocallyLipschitzOn.isNullSet_setOf_not_mdifferentiableAt.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [PseudoEMetricSpace M] [ChartedSpace H M]
  [IsManifold I 1 M] [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsRiemannianManifold I M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {U : Set M} [FiniteDimensional ℝ E]
  {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : M → F}
  [MeasurableSpace E] [BorelSpace E] (hf : LocallyLipschitzOn U f) (hU : IsOpen U) :
  TauCeti.IsNullSet I {x | x ∈ U ∧ ¬MDiffAt f x}
```

## Sources

- [Tau Ceti documentation: `LipschitzWith.ae_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Rademacher.html#LipschitzWith.ae_mdifferentiableAt)
- [Source of `LipschitzWith.ae_mdifferentiableAt` in TauCeti/Geometry/Manifold/Riemannian/Rademacher.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Rademacher.lean#L135)
