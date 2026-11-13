---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.ofGradient, Electromagnetism.ElectromagneticPotential.ofGradient_apply_sum, Electromagnetism.ElectromagneticPotential.ofGradient_apply, Electromagnetism.ElectromagneticPotential.ofGradient_zero, Electromagnetism.ElectromagneticPotential.ofGradient_add, Electromagnetism.ElectromagneticPotential.differentiable_ofGradient, Electromagnetism.ElectromagneticPotential.contDiff_ofGradient, Electromagnetism.ElectromagneticPotential.toFieldStrength_ofGradient
statement: formalized
proof: formalized
---

# Gauge Transformations of the Electromagnetic Potential

The module `Physlib.Electromagnetism.Kinematics.GaugeTransformation`, [Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean): 18 declarations, 18 with a docstring.

## i. Overview

> In this module we define gauge transformations of the electromagnetic potential
> `A^μ ↦ A^μ + ∂^μ χ` where `χ : SpaceTime d → ℝ` is a smooth gauge function, and prove
> that the field strength tensor is invariant under such transformations.
>
> The raised-index gradient `∂^μ χ := η^{μν} ∂_ν χ` is necessary because the bare covariant gradient
> `∂_μ χ` does not make `F^{μν}` invariant. The formal witness is
> `toFieldStrength_eval_bareGradient_inl_inr` (§B.5), which computes a specific nonzero component of
> the field strength of a bare-gradient potential. The invariance theorem
> `toFieldStrength_gaugeTransform` doubles as a correctness test of `ofGradient`.

## ii. Key results

> - `ofGradient` : The pure-gauge potential `A^μ = η^{μν} ∂_ν χ` built from a gauge function `χ`.
> - `gaugeTransform` : The gauge transformation `A^μ ↦ A^μ + ∂^μ χ`.
> - `toFieldStrength_ofGradient` : A pure-gauge potential has vanishing field strength.
> - `toFieldStrength_gaugeTransform` : The field strength tensor is invariant under gauge
>   transformations.
> - `toFieldStrength_eval_gaugeTransform` : The components of the field strength tensor are
>   invariant under gauge transformations.
> - `gaugeTransform_gaugeTransform` : Composing two gauge shifts equals shifting by the sum;
>   upgrades one-step F-invariance to invariance along any finite chain.
> - `ofGradient_equivariant` : `ofGradient` intertwines the Lorentz action with function composition.
> - `gaugeTransform_equivariant` : Gauge transformations commute with Lorentz transformations.
> - `toFieldStrength_eval_bareGradient_inl_inr` : The `(inl 0, inr i)` field-strength component of
>   the bare-gradient potential `χ(x) = x⁰·xⁱ` equals `2`; in particular the bare gradient does
>   not give a gauge-invariant field strength (necessity of the metric contraction in `ofGradient`).

## iv. References

> * https://en.wikipedia.org/wiki/Mathematical\_descriptions\_of\_the\_electromagnetic\_field#Gauge\_freedom.
>   [ref: wiki\_em\_field\_gauge\_freedom]

## A. The pure-gauge potential

### A.1. Definition and basic lemmas

**`Electromagnetism.ElectromagneticPotential.ofGradient`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L95).

> The pure-gauge electromagnetic potential `A^μ = ∂^μ χ = η^{μν} ∂_ν χ` built from a
> gauge function `χ`. The metric-contracted form `∑ κ, η μ κ * ∂_ κ χ` is the definition;
> the diagonal form (which equals `η μ μ * ∂_ μ χ` since `η` is diagonal) is derived in
> `ofGradient_apply`.

```lean
noncomputable def ofGradient {d} (χ : SpaceTime d → ℝ) : ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofGradient_apply_sum`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L99).

> Unfolding of the summed definition of `ofGradient`.

```lean
lemma ofGradient_apply_sum {d} (χ : SpaceTime d → ℝ) (x : SpaceTime d) (μ : Fin 1 ⊕ Fin d) :
    ofGradient χ x μ = ∑ κ, η μ κ * ∂_ κ χ x
```

**`Electromagnetism.ElectromagneticPotential.ofGradient_apply`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L104).

> Evaluation of `ofGradient` in the diagonal form; the off-diagonal entries of `η` vanish so
> only the `κ = μ` term survives.

```lean
lemma ofGradient_apply {d} (χ : SpaceTime d → ℝ) (x : SpaceTime d) (μ : Fin 1 ⊕ Fin d) :
    ofGradient χ x μ = η μ μ * ∂_ μ χ x
```

**`Electromagnetism.ElectromagneticPotential.ofGradient_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L114).

> The pure-gauge potential built from the zero gauge function has all components zero.

```lean
lemma ofGradient_zero {d} (x : SpaceTime d) (μ : Fin 1 ⊕ Fin d) :
    ofGradient (0 : SpaceTime d → ℝ) x μ = 0
```

**`Electromagnetism.ElectromagneticPotential.ofGradient_add`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L120).

> `ofGradient` is additive in the gauge function (when both summands are differentiable).

```lean
lemma ofGradient_add {d} {χ₁ χ₂ : SpaceTime d → ℝ}
    (hχ₁ : Differentiable ℝ χ₁) (hχ₂ : Differentiable ℝ χ₂) :
    ofGradient (χ₁ + χ₂) = ofGradient χ₁ + ofGradient χ₂
```

### A.2. Differentiability of the pure-gauge potential

**`Electromagnetism.ElectromagneticPotential.differentiable_ofGradient`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L136).

> The pure-gauge potential is differentiable when `χ` is `C^2`.

```lean
lemma differentiable_ofGradient {d} {χ : SpaceTime d → ℝ} (hχ : ContDiff ℝ 2 χ) :
    Differentiable ℝ (ofGradient χ)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_ofGradient`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L145).

> The pure-gauge potential is `C^n` when `χ` is `C^{n+1}`.

```lean
lemma contDiff_ofGradient {n} {d} {χ : SpaceTime d → ℝ} (hχ : ContDiff ℝ (n + 1) χ) :
    ContDiff ℝ n (ofGradient χ)
```

### A.3. Vanishing field strength of the pure-gauge potential

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_ofGradient`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L161).

> A pure-gauge potential has vanishing field strength.

```lean
lemma toFieldStrength_ofGradient {d} {χ : SpaceTime d → ℝ} (hχ : ContDiff ℝ 2 χ)
    (x : SpaceTime d) : (ofGradient χ).toFieldStrength x = 0
```

### A.4. Lorentz equivariance of the pure-gauge potential

> `ofGradient` intertwines the Lorentz action on potentials with composition by Λ⁻¹ on the gauge
> function: `Λ • ofGradient χ = ofGradient (χ ∘ (Λ⁻¹ • ·))`. The proof reduces to the
> metric-commutativity identity `Λ * η = η * (Λ⁻¹)ᵀ`, which is the defining property of the
> Lorentz group (`LorentzGroup.comm_minkowskiMatrix`).

**`Electromagnetism.ElectromagneticPotential.ofGradient_equivariant`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L192).

> `ofGradient` intertwines the Lorentz action on potentials with composition by Λ⁻¹ on the
> gauge function: `Λ • ofGradient χ = ofGradient (χ ∘ (Λ⁻¹ • ·))`.

```lean
lemma ofGradient_equivariant {d} (χ : SpaceTime d → ℝ) (hχ : Differentiable ℝ χ)
    (Λ : LorentzGroup d) :
    Λ • ofGradient χ = ofGradient (χ ∘ (Λ⁻¹ • ·))
```

## B. Gauge transformations

### B.1. Definition and basic lemmas

**`Electromagnetism.ElectromagneticPotential.gaugeTransform`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L242).

> The gauge transformation `A^μ ↦ A^μ + ∂^μ χ` of an electromagnetic potential.

```lean
noncomputable def gaugeTransform {d} (χ : SpaceTime d → ℝ) (A : ElectromagneticPotential d) :
    ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.gaugeTransform_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L246).

> Evaluation of `gaugeTransform`.

```lean
lemma gaugeTransform_apply {d} (χ : SpaceTime d → ℝ) (A : ElectromagneticPotential d)
    (x : SpaceTime d) : gaugeTransform χ A x = A x + ofGradient χ x
```

### B.2. Invariance of the field strength

> The key ingredient — that a pure-gauge potential has vanishing field strength — is proved in §A.3
> (`toFieldStrength_ofGradient`).

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_gaugeTransform`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L260).

> The field strength tensor is invariant under gauge transformations.

```lean
lemma toFieldStrength_gaugeTransform {d} (A : ElectromagneticPotential d)
    (χ : SpaceTime d → ℝ) (hA : Differentiable ℝ A) (hχ : ContDiff ℝ 2 χ) (x : SpaceTime d) :
    (gaugeTransform χ A).toFieldStrength x = A.toFieldStrength x
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_gaugeTransform`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L267).

> The components of the field strength tensor are invariant under gauge transformations.

```lean
lemma toFieldStrength_eval_gaugeTransform {d} (A : ElectromagneticPotential d)
    (χ : SpaceTime d → ℝ) (hA : Differentiable ℝ A) (hχ : ContDiff ℝ 2 χ) (x : SpaceTime d)
    (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {(gaugeTransform χ A).toFieldStrength x | [μ] [ν]}ᵀ =
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ
```

### B.3. Group structure of gauge shifts

> Composing two gauge shifts by χ₁ and χ₂ is the same as shifting by χ₁ + χ₂. Together with
> `gaugeTransform_zero` this shows that the map `χ ↦ (A ↦ gaugeTransform χ A)` is a group action
> of the additive group of smooth functions. (We do not build the formal `MulAction` here —
> the composition lemma is the agreeable core, and the rest is straightforward from it.)
>
> The `ofGradient` lemmas used here — `ofGradient_zero` and `ofGradient_add` — are proved in §A.1.

**`Electromagnetism.ElectromagneticPotential.gaugeTransform_zero`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L288).

> Shifting by the zero gauge function is the identity.

```lean
lemma gaugeTransform_zero {d} (A : ElectromagneticPotential d) :
    gaugeTransform (0 : SpaceTime d → ℝ) A = A
```

**`Electromagnetism.ElectromagneticPotential.gaugeTransform_gaugeTransform`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L296).

> Two successive gauge shifts compose: shifting by χ₂ then χ₁ equals shifting by χ₁ + χ₂.
> This upgrades one-step F-invariance to invariance along any finite chain of gauge shifts.

```lean
lemma gaugeTransform_gaugeTransform {d} (A : ElectromagneticPotential d)
    (χ₁ χ₂ : SpaceTime d → ℝ) (hχ₁ : Differentiable ℝ χ₁) (hχ₂ : Differentiable ℝ χ₂) :
    gaugeTransform χ₁ (gaugeTransform χ₂ A) = gaugeTransform (χ₁ + χ₂) A
```

### B.4. Equivariance under Lorentz transformations

> The gauge-transformation map commutes with the Lorentz group action: applying Λ to a potential
> and then gauge-transforming by χ is the same as gauge-transforming by `χ ∘ (Λ⁻¹ • ·)` and then
> applying Λ. The proof delegates to `ofGradient_equivariant` (§A.4).

**`Electromagnetism.ElectromagneticPotential.gaugeTransform_equivariant`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L317).

> Gauge transformations commute with Lorentz transformations: applying Λ and then performing
> a gauge transformation by `χ` equals performing a gauge transformation by `χ ∘ (Λ⁻¹ • ·)`
> and then applying Λ.

```lean
lemma gaugeTransform_equivariant {d} (A : ElectromagneticPotential d)
    (χ : SpaceTime d → ℝ) (hχ : Differentiable ℝ χ) (Λ : LorentzGroup d) :
    Λ • gaugeTransform χ A = gaugeTransform (χ ∘ (Λ⁻¹ • ·)) (Λ • A)
```

### B.5. Necessity: bare gradient does not give gauge invariance

> We exhibit a concrete gauge function `χ(x) = x⁰·xⁱ` whose **bare** covariant gradient
> `B^μ := ∂_μ χ` has a nonzero field-strength component (equal to `2`), certifying that the metric
> contraction in `ofGradient` is required for gauge invariance.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_bareGradient_inl_inr`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L342).

> The `(inl 0, inr i)` component of the field strength tensor of the bare-gradient potential
> `B^μ := ∂_μ χ` for `χ(x) = x⁰·xⁱ` equals `2`. This witnesses that the bare covariant gradient
> does not produce a gauge-invariant field strength, so the raised-index contraction
> `η^{μν} ∂_ν χ` in `ofGradient` is necessary (see the module overview).

```lean
lemma toFieldStrength_eval_bareGradient_inl_inr {d : ℕ} (i : Fin d)
    (x : SpaceTime d) :
    let χ : SpaceTime d → ℝ := fun y => y (Sum.inl 0) * y (Sum.inr i)
    let B : ElectromagneticPotential d := ⟨fun y μ => ∂_ μ χ y⟩
    toScalar {B.toFieldStrength x | [Sum.inl 0] [Sum.inr i]}ᵀ = 2
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_bareGradient_ne_zero`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean#L390).

> The field strength of the bare-gradient potential `B^μ := ∂_μ χ` for
> `χ(x) = x⁰·xⁱ` is nonzero (follows from `toFieldStrength_eval_bareGradient_inl_inr`).

```lean
lemma toFieldStrength_bareGradient_ne_zero {d : ℕ} (i : Fin d)
    (x : SpaceTime d) :
    let χ : SpaceTime d → ℝ := fun y => y (Sum.inl 0) * y (Sum.inr i)
    let B : ElectromagneticPotential d := ⟨fun y μ => ∂_ μ χ y⟩
    B.toFieldStrength x ≠ 0
```

## Depends on

- [The Field Strength Tensor (Kinematics/FieldStrength)](fieldstrength.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean)
