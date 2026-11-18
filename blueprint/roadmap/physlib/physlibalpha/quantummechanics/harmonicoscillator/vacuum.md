---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator.loweringCLM_vacuumGaussian, QuantumMechanics.HarmonicOscillator.hasVacuum_vacuumGaussian, QuantumMechanics.HarmonicOscillator.deriv_realGaussian, QuantumMechanics.HarmonicOscillator.stdGaussian_apply', QuantumMechanics.HarmonicOscillator.deriv_stdGaussian, QuantumMechanics.HarmonicOscillator.momentumCLM_stdGaussian, QuantumMechanics.HarmonicOscillator.diagEquiv, QuantumMechanics.HarmonicOscillator.diagEquiv_apply
statement: formalized
proof: formalized
---

# A vacuum state for the harmonic oscillator

The module `PhyslibAlpha.QuantumMechanics.HarmonicOscillator.Vacuum`, [PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean): 18 declarations, 15 with a docstring, 2 listed as significant.

> An explicit Gaussian vacuum for the d-dimensional harmonic oscillator ladder system.

## i. Overview

> For a `d`-dimensional oscillator `Q`, `vacuumGaussian` is the Gaussian
> `exp(-∑ᵢ(xᵢ/ξᵢ)²/2)`, rescaled coordinatewise by the characteristic lengths `ξᵢ` through the
> diagonal continuous linear equivalence `diagEquiv`. Every annihilation operator kills this
> Schwartz function, so `hasVacuum_vacuumGaussian` supplies a `LadderSystem.HasVacuum` witness
> without an isotropy assumption.
>
> The isotropic unit-length case (`Q.ξ i = 1` for all `i`) is represented by
> `stdGaussian (Space d) ℂ`, the function `x ↦ exp(-‖x‖²/2)` from
> `Physlib.Mathematics.InnerProductSpace.Gaussian`.
> `hasVacuum_stdGaussian_of_forall_xi_eq_one` derives the unit-length case from `vacuumGaussian`.
> The theorem `loweringCLM_stdGaussian_of_xi_eq_one` assumes unit length only in the selected
> mode, so it is proved separately.

## ii. Key results

> - `diagEquiv` : the diagonal rescaling of `Space d` by the characteristic lengths.
> - `vacuumGaussian` : the anisotropic vacuum Gaussian, `exp(-∑ᵢ(xᵢ/ξᵢ)²/2)`.
> - `loweringCLM_vacuumGaussian` : every `loweringCLM i` kills the vacuum Gaussian.
> - `hasVacuum_vacuumGaussian` : `Q.vacuumGaussian` is a vacuum for `Q.toLadderSystem`.
> - `loweringCLM_stdGaussian_of_xi_eq_one`, `hasVacuum_stdGaussian_of_forall_xi_eq_one` : the
>     isotropic-unit-length special case.

## iv. References

> * None.

## A. The standard Gaussian: derivative and momentum action

> `Q`-free prerequisites about the plain, unscaled Gaussian, reused by both the general anisotropic
> case below and the isotropic-unit-length special case at the end of this file.

**`QuantumMechanics.HarmonicOscillator.deriv_realGaussian`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L72).

> The real-valued Gaussian `exp(-‖x‖²/2)`'s coordinate derivative,
> `∂ᵢ g = -xᵢ · g`.

```lean
lemma deriv_realGaussian (x : Space d) (i : Fin d) :
    Space.deriv i (fun x : Space d => Real.exp (-2⁻¹ * ‖x‖ ^ 2)) x =
      -x i * Real.exp (-2⁻¹ * ‖x‖ ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.stdGaussian_apply'`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L85).

> `stdGaussian (Space d) ℂ`'s pointwise value is the real-valued Gaussian, cast to `ℂ`.

```lean
lemma stdGaussian_apply' (x : Space d) :
    (stdGaussian (Space d) ℂ : Space d → ℂ) x = Real.exp (-2⁻¹ * ‖x‖ ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.deriv_stdGaussian`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L90).

> The coordinate derivative of the standard Gaussian, `∂ᵢ Ω = -xᵢ • Ω`.

```lean
lemma deriv_stdGaussian (x : Space d) (i : Fin d) :
    Space.deriv i (fun x : Space d => (stdGaussian (Space d) ℂ : Space d → ℂ) x) x =
      (-x i : ℂ) * (stdGaussian (Space d) ℂ : Space d → ℂ) x
```

**`QuantumMechanics.HarmonicOscillator.momentumCLM_stdGaussian`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L111).

> The momentum operator applied to the standard Gaussian,
> `𝐩ᵢ Ω = -iℏ·(-xᵢ)Ω = iℏxᵢ·Ω`.

```lean
lemma momentumCLM_stdGaussian (i : Fin d) (x : Space d) :
    (𝐩[d] i (stdGaussian (Space d) ℂ) : 𝓢(Space d, ℂ)) x =
      (I * ℏ * x i : ℂ) * (stdGaussian (Space d) ℂ : Space d → ℂ) x
```

## B. The general, anisotropic vacuum

> No isotropy assumption needed: every oscillator `Q` (any masses/frequencies, hence any
> characteristic lengths `ξᵢ`) has an explicit vacuum, the Gaussian rescaled coordinatewise by `ξ`.

**`QuantumMechanics.HarmonicOscillator.diagEquiv`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L133).

> The diagonal rescaling of `Space d` by the characteristic lengths, `(Q.diagEquiv x) i = ξᵢxᵢ`.
> Composing the standard Gaussian with its inverse turns the standard Gaussian's isotropic width into
> the anisotropic width `ξᵢ` required by a vacuum of `Q`, whether or not `Q` itself is
> isotropic (contrast `stdGaussian`/`hasVacuum_stdGaussian_of_forall_xi_eq_one` below, which only
> covers `∀ i, ξᵢ = 1`).

```lean
noncomputable def diagEquiv (Q : HarmonicOscillator d) : Space d ≃L[ℝ] Space d
```

**`QuantumMechanics.HarmonicOscillator.diagEquiv_apply`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L139).

```lean
lemma diagEquiv_apply (x : Space d) (i : Fin d) : Q.diagEquiv x i = Q.ξ i * x i
```

**`QuantumMechanics.HarmonicOscillator.diagEquiv_symm_apply`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L141).

```lean
lemma diagEquiv_symm_apply (x : Space d) (i : Fin d) :
    Q.diagEquiv.symm x i = (Q.ξ i)⁻¹ * x i
```

**`QuantumMechanics.HarmonicOscillator.vacuumGaussian`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L146).

> The vacuum Gaussian of `Q`: the anisotropic Gaussian `exp(-∑ᵢ(xᵢ/ξᵢ)²/2)`, `Q.diagEquiv`
> applied to the standard one. Equals `stdGaussian (Space d) ℂ` exactly when every `ξᵢ = 1`.

```lean
noncomputable def vacuumGaussian (Q : HarmonicOscillator d) : 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.vacuumGaussian_apply`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L149).

```lean
lemma vacuumGaussian_apply (x : Space d) :
    (Q.vacuumGaussian : Space d → ℂ) x = Real.exp (-2⁻¹ * ‖Q.diagEquiv.symm x‖ ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.diagEquiv_symm_basis`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L154).

> `Q.diagEquiv.symm` applied to a basis vector rescales it by `(ξᵢ)⁻¹`.

```lean
lemma diagEquiv_symm_basis (i : Fin d) :
    Q.diagEquiv.symm (Space.basis i) = (Q.ξ i)⁻¹ • Space.basis i
```

**`QuantumMechanics.HarmonicOscillator.fderiv_norm_sq_diagEquiv_symm`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L161).

> The Fréchet derivative of the anisotropic Gaussian's real exponent `‖Q.diagEquiv.symm ·‖²`,
> at the CLM level (mirrors `fderiv_norm_sq_apply`, composed with `Q.diagEquiv.symm`).

```lean
lemma fderiv_norm_sq_diagEquiv_symm (x : Space d) :
    fderiv ℝ (fun x : Space d => ‖Q.diagEquiv.symm x‖ ^ 2) x =
      (2 • innerSL ℝ (Q.diagEquiv.symm x)) ∘L (Q.diagEquiv.symm : Space d →L[ℝ] Space d)
```

**`QuantumMechanics.HarmonicOscillator.deriv_realGaussian_diag`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L172).

> The real-valued anisotropic Gaussian's coordinate derivative,
> `∂ᵢ g = -(xᵢ/ξᵢ²) · g`.

```lean
lemma deriv_realGaussian_diag (x : Space d) (i : Fin d) :
    Space.deriv i (fun x : Space d => Real.exp (-2⁻¹ * ‖Q.diagEquiv.symm x‖ ^ 2)) x =
      -(x i / (Q.ξ i) ^ 2) * Real.exp (-2⁻¹ * ‖Q.diagEquiv.symm x‖ ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.deriv_vacuumGaussian`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L190).

> The coordinate derivative of the vacuum Gaussian, `∂ᵢ Ω = -(xᵢ/ξᵢ²) • Ω`.

```lean
lemma deriv_vacuumGaussian (x : Space d) (i : Fin d) :
    Space.deriv i (fun x : Space d => (Q.vacuumGaussian : Space d → ℂ) x) x =
      (-(x i / (Q.ξ i) ^ 2 : ℝ) : ℂ) * (Q.vacuumGaussian : Space d → ℂ) x
```

**`QuantumMechanics.HarmonicOscillator.momentumCLM_vacuumGaussian`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L214).

> The momentum operator applied to the vacuum Gaussian,
> `𝐩ᵢ Ω = iℏ(xᵢ/ξᵢ²)·Ω`.

```lean
lemma momentumCLM_vacuumGaussian (i : Fin d) (x : Space d) :
    (𝐩[d] i (Q.vacuumGaussian) : 𝓢(Space d, ℂ)) x =
      (I * ℏ * (x i / (Q.ξ i) ^ 2 : ℝ) : ℂ) * (Q.vacuumGaussian : Space d → ℂ) x
```

**`QuantumMechanics.HarmonicOscillator.loweringCLM_vacuumGaussian`**, a theorem, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L224). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every `loweringCLM i` kills the vacuum Gaussian, without an isotropy or unit-length
> assumption.

```lean
theorem loweringCLM_vacuumGaussian (i : Fin d) :
    Q.loweringCLM i (Q.vacuumGaussian) = 0
```

**`QuantumMechanics.HarmonicOscillator.hasVacuum_vacuumGaussian`**, a theorem, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L239). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Q.vacuumGaussian` is a vacuum for `Q.toLadderSystem`, without an isotropy assumption.

```lean
theorem hasVacuum_vacuumGaussian : Q.toLadderSystem.HasVacuum (Q.vacuumGaussian)
```

## C. The isotropic-unit-length special case

**`QuantumMechanics.HarmonicOscillator.loweringCLM_stdGaussian_of_xi_eq_one`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L260).

> Every `loweringCLM i` kills the standard Gaussian, provided that mode has unit
> characteristic length. Independent of `hasVacuum_vacuumGaussian`/`loweringCLM_vacuumGaussian`
> above: the hypothesis here is genuinely weaker (unit length in mode `i` alone, not every mode), so
> this isn't a corollary of the general anisotropic result.

```lean
lemma loweringCLM_stdGaussian_of_xi_eq_one (i : Fin d) (hξ : Q.ξ i = 1) :
    Q.loweringCLM i (stdGaussian (Space d) ℂ) = 0
```

**`QuantumMechanics.HarmonicOscillator.hasVacuum_stdGaussian_of_forall_xi_eq_one`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean#L274).

> `stdGaussian (Space d) ℂ` is a vacuum for `Q.toLadderSystem` when every mode has unit
> characteristic length.

```lean
lemma hasVacuum_stdGaussian_of_forall_xi_eq_one (hξ : ∀ i, Q.ξ i = 1) :
    Q.toLadderSystem.HasVacuum (stdGaussian (Space d) ℂ)
```

## Depends on

- [Gaussians in inner product spaces](../../../physlib/mathematics/innerproductspace/gaussian.md)
- [Vacuum states and creation-operator words](../../mathematics/part-02/laddersystem/vacuum.md)
- [The harmonic oscillator as a ladder system](laddersystem.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/Vacuum.lean)
