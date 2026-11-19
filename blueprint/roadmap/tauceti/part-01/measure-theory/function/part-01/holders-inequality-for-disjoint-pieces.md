---
declaration: theorem
origin: cited
lean: TauCeti.sum_eLpNorm_indicator_le, TauCeti.enorm_integral_inner_le, TauCeti.enorm_integral_mul_le, TauCeti.enorm_integral_smul_le, MeasureTheory.MemLp.setIntegral_norm_sq_le_eLpNorm_sq_mul_measureReal_rpow, TauCeti.rpow_lintegral_le_measure_univ_rpow_mul
statement: formalized
proof: formalized
---

# Hölder's inequality for disjoint pieces

For `1 ≤ r`, the `Lʳ` seminorms of the restrictions
of `g` to the members of a finite family of `N` pairwise disjoint measurable sets add up to at most
`N^{1 - 1/r} ‖g‖_r`.

```lean
TauCeti.sum_eLpNorm_indicator_le.{u_1, u_2, u_3} {α : Type u_1} {ι : Type u_2} {F : Type u_3}
  [MeasurableSpace α] [TopologicalSpace F] [ESeminormedAddMonoid F] {μ : MeasureTheory.Measure α}
  {r : ENNReal} (hr : 1 ≤ r) (s : Finset ι) {J : ι → Set α} (hJ : ∀ i ∈ s, MeasurableSet (J i))
  (hd : (↑s).PairwiseDisjoint J) (g : α → F) :
  ∑ i ∈ s, MeasureTheory.eLpNorm ((J i).indicator g) r μ ≤
    ↑s.card ^ (1 - r.toReal⁻¹) * MeasureTheory.eLpNorm g r μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_eLpNorm_indicator_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSeminorm/Indicator.html#TauCeti.sum_eLpNorm_indicator_le).

## Other forms

**Hölder's inequality for the integral of an inner product.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_inner_le).

```lean
TauCeti.enorm_integral_inner_le.{u_1, u_4, u_5} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} {H : Type u_5} [RCLike 𝕜] [NormedAddCommGroup H]
  [InnerProductSpace 𝕜 H] {p q : ENNReal} [p.HolderConjugate q] {u v : α → H} :
  ‖∫ (x : α), inner 𝕜 (u x) (v x) ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

**Hölder's inequality for the integral of a product.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_mul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_mul_le).

```lean
TauCeti.enorm_integral_mul_le.{u_1, u_4} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} [NonUnitalNormedRing 𝕜] [NormedSpace ℝ 𝕜]
  {p q : ENNReal} [p.HolderConjugate q] {u v : α → 𝕜} :
  ‖∫ (x : α), u x * v x ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

**Hölder's inequality for the Bochner integral of a pointwise scalar multiple.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_smul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Holder.html#TauCeti.enorm_integral_smul_le).

```lean
TauCeti.enorm_integral_smul_le.{u_1, u_2, u_3} {α : Type u_1} {𝕜 : Type u_2} {F : Type u_3}
  [MeasurableSpace α] [NormedAddGroup 𝕜] [NormedAddCommGroup F] [SMulZeroClass 𝕜 F]
  [IsBoundedSMul 𝕜 F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure α} {p q : ENNReal}
  [p.HolderConjugate q] {a : α → 𝕜} {f : α → F} :
  ‖∫ (x : α), a x • f x ∂μ‖ₑ ≤ MeasureTheory.eLpNorm a p μ * MeasureTheory.eLpNorm f q μ
```

**Hölder's inequality for the `L²` mass on a subset.** Formalized in Tau Ceti as [`MeasureTheory.MemLp.setIntegral_norm_sq_le_eLpNorm_sq_mul_measureReal_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Norm.html#MeasureTheory.MemLp.setIntegral_norm_sq_le_eLpNorm_sq_mul_measureReal_rpow).

```lean
MeasureTheory.MemLp.setIntegral_norm_sq_le_eLpNorm_sq_mul_measureReal_rpow.{u_1, u_2} {X : Type u_1}
  {F : Type u_2} [MeasurableSpace X] {μ : MeasureTheory.Measure X} [NormedAddCommGroup F]
  {g : X → F} {s t : Set X} {q : ENNReal} (hg : MeasureTheory.MemLp g q (μ.restrict t)) (hq : 2 ≤ q)
  (hst : s ⊆ t) (hs : μ s ≠ ⊤) :
  ∫ (x : X) in s, ‖g x‖ ^ 2 ∂μ ≤
    (MeasureTheory.eLpNorm g q (μ.restrict t)).toReal ^ 2 * μ.real s ^ (1 - 2 / q.toReal)
```

**Hölder's inequality in extended-valued `∫⁻` form, raised to the power `r`.** Formalized in Tau Ceti as [`TauCeti.rpow_lintegral_le_measure_univ_rpow_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.rpow_lintegral_le_measure_univ_rpow_mul).

```lean
TauCeti.rpow_lintegral_le_measure_univ_rpow_mul.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {u : α → ENNReal} {r : ℝ} (hr : 1 ≤ r) :
  (∫⁻ (x : α), u x ∂μ) ^ r ≤ μ Set.univ ^ (r - 1) * ∫⁻ (x : α), u x ^ r ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_eLpNorm_indicator_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSeminorm/Indicator.html#TauCeti.sum_eLpNorm_indicator_le)
- [Source of `TauCeti.sum_eLpNorm_indicator_le` in TauCeti/MeasureTheory/Function/LpSeminorm/Indicator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/LpSeminorm/Indicator.lean#L34)
