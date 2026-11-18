---
declaration: module
origin: cited
lean: TauCeti.norm_integral_smul_sub_le, TauCeti.tendsto_integral_smul_of_tendsto, TauCeti.exists_integral_eq_one_norm_eq_one
statement: formalized
proof: formalized
---

# Integrals against `L¹` peak functions concentrating at a point

The module `PhyslibAlpha.Mathematics.TauCeti.MeasureTheory.Integral.PeakFunction`, [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean): 3 declarations, 3 with a docstring.

> Let `f i` be a net of `L¹` classes of unit integral, `∫ f i = 1`, with uniformly bounded `L¹` norms,
> which concentrate at a point `x₀`: for every neighbourhood `U` of `x₀`, eventually each `f i`
> vanishes almost everywhere outside `U`.

## i. Overview

> Let `f i` be a net of `L¹` classes of unit integral, `∫ f i = 1`, with uniformly bounded `L¹` norms,
> which concentrate at a point `x₀`: for every neighbourhood `U` of `x₀`, eventually each `f i`
> vanishes almost everywhere outside `U`. Then `∫ x, f i x • φ x ∂μ` tends to `a` for every `φ`
> with limit `a` at `x₀` whose products `f i • φ` with the weights are almost everywhere strongly
> measurable. This is the approximate-identity argument in its pointwise form: since `∫ f i = 1`,
> the difference is `∫ x, f i x • (φ x - a) ∂μ`, and `φ x` stays close to `a` on the set where
> `f i` lives.
>
> Only the integrands `f i • φ` are asked to be almost everywhere strongly measurable, not `φ`
> itself. This holds when `φ` is, but also for a continuous `φ` and a measure that is inner regular
> for compact sets but not σ-finite, such as the Haar measure `MeasureTheory.Measure.addHaar` of a
> locally compact group that is not σ-compact
> (`MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul`).
>
> On a measure that charges every open set and is finite on some neighbourhood of each point, such
> peak functions exist inside every neighbourhood of every point (normalized indicators), so the
> statement is never vacuous.
>
> The weights here are `L¹` classes with values in an `RCLike` field, as consumed by integrated forms
> of representations. Mathlib's peak-function results
> (`tendsto_integral_peak_smul_of_integrable_of_tendsto` in
> `Mathlib/MeasureTheory/Integral/PeakFunction.lean`) do not apply in that situation: they ask for
> nonnegative real weights, defined pointwise, and for `φ` to be integrable. The latter fails for the
> orbits `g ↦ π g v` of a unitary representation of a non-compact group, which have constant norm.
> Similarly, `tendsto_integral_smul_of_tendsto_average_norm_sub` asks for pointwise bounds
> `|g i| ≤ K / μ (a i)` on the weights. Here, instead, `φ` only has to be bounded near `x₀`, which
> its limit at `x₀` provides.

## ii. Key results

> * `TauCeti.norm_integral_smul_sub_le`: the approximate-identity estimate
>   `‖∫ x, f x • φ x ∂μ - y‖ ≤ ε * ‖f‖` when `∫ f = 1`, `f` vanishes off `U`, and `φ` stays within `ε`
>   of `y` on `U`.
> * `TauCeti.tendsto_integral_smul_of_tendsto`: a net of `L¹` peak functions concentrating at
>   `x₀` integrates `φ` to its limit at `x₀`.
> * `TauCeti.exists_integral_eq_one_norm_eq_one`: peak functions of unit integral and unit
>   `L¹` norm exist inside every neighbourhood of a point.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016), §2.5.

## A. Development

**`TauCeti.norm_integral_smul_sub_le`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean#L82).

> **The approximate-identity estimate.** If an `L¹` class `f` has unit integral and vanishes
> almost everywhere outside `U`, and `φ` stays within `ε` of `y` on `U`, then the integral of `φ`
> against `f` is within `ε * ‖f‖` of `y`. The integrand `f • φ` is assumed almost everywhere
> strongly measurable.

```lean
lemma norm_integral_smul_sub_le {f : α →₁[μ] 𝕜} (hf : ∫ x, f x ∂μ = 1) {U : Set α}
    (hfU : ∀ᵐ x ∂μ, x ∉ U → f x = 0) {φ : α → E}
    (hφ : AEStronglyMeasurable (fun x ↦ f x • φ x) μ) {y : E}
    {ε : ℝ} (hφU : ∀ x ∈ U, ‖φ x - y‖ ≤ ε) :
    ‖(∫ x, f x • φ x ∂μ) - y‖ ≤ ε * ‖f‖
```

**`TauCeti.tendsto_integral_smul_of_tendsto`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean#L112).

> **`L¹` peak functions integrate a function to its limit at the peak.** Let `f i` be `L¹`
> classes which eventually have unit integral and `L¹` norm at most `C`, and which concentrate at
> `x₀`: for every neighbourhood `U` of `x₀`, eventually `f i` vanishes almost everywhere outside `U`.
> Then `∫ x, f i x • φ x ∂μ` tends to `a` for every `φ` tending to `a` at `x₀` whose products
> `f i • φ` are eventually almost everywhere strongly measurable.

```lean
lemma tendsto_integral_smul_of_tendsto {ι : Type*} {l : Filter ι} {f : ι → α →₁[μ] 𝕜}
    {C : ℝ} {x₀ : α} [TopologicalSpace α] (hf : ∀ᶠ i in l, ∫ x, f i x ∂μ = 1)
    (hfC : ∀ᶠ i in l, ‖f i‖ ≤ C) (hfx₀ : ∀ U ∈ 𝓝 x₀, ∀ᶠ i in l, ∀ᵐ x ∂μ, x ∉ U → f i x = 0)
    {φ : α → E} (hφ : ∀ᶠ i in l, AEStronglyMeasurable (fun x ↦ f i x • φ x) μ) {a : E}
    (hφa : Tendsto φ (𝓝 x₀) (𝓝 a)) :
    Tendsto (fun i ↦ ∫ x, f i x • φ x ∂μ) l (𝓝 a)
```

**`TauCeti.exists_integral_eq_one_norm_eq_one`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean#L137).

> **`L¹` peak functions exist.** For a measure positive on nonempty open sets and finite on some
> neighbourhood of each point, every neighbourhood `U` of a point carries an `L¹` class of unit
> integral and unit `L¹` norm vanishing almost everywhere outside `U`: the indicator of a
> neighbourhood of finite measure inside `U`, normalized by that measure.

```lean
lemma exists_integral_eq_one_norm_eq_one [TopologicalSpace α] [OpensMeasurableSpace α]
    [μ.IsOpenPosMeasure] [IsLocallyFiniteMeasure μ] {x₀ : α} {U : Set α} (hU : U ∈ 𝓝 x₀) :
    ∃ f : α →₁[μ] 𝕜, ∫ x, f x ∂μ = 1 ∧ ‖f‖ = 1 ∧ ∀ᵐ x ∂μ, x ∉ U → f x = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Integral/PeakFunction.lean)
