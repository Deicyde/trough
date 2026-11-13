---
declaration: module
origin: cited
lean: CanonicalEnsemble.helmholtzFreeEnergy_eq_meanEnergy_sub_temp_mul_thermodynamicEntropy, CanonicalEnsemble.differentialEntropy_eq_meanEnergy_sub_helmholtz_div_temp_add_correction, CanonicalEnsemble.meanEnergy_eq_neg_deriv_log_Z_of_beta, CanonicalEnsemble.energyVariance_eq_meanSquareEnergy_sub_meanEnergy_sq, CanonicalEnsemble.fluctuation_dissipation_energy_parametric, CanonicalEnsemble.mathematicalHelmholtzFreeEnergy, CanonicalEnsemble.helmholtzFreeEnergy_eq_helmholtzMathematicalFreeEnergy_add_correction, CanonicalEnsemble.differentialEntropy_eq_kB_beta_meanEnergy_add_kB_log_mathZ
statement: formalized
proof: formalized
---

# Canonical Ensemble: Thermodynamic Identities and Relations

The module `Physlib.StatisticalMechanics.CanonicalEnsemble.Lemmas`, [Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean): 26 declarations, 25 with a docstring, 5 listed as significant.

> This file develops relations between the *mathematical* objects defined in
> `Basic.lean` and the *physical* thermodynamic quantities, together with
> calculus identities for the canonical ensemble.

## Contents Overview

> 1. Helmholtz Free Energies
>   * `mathematicalHelmholtzFreeEnergy`
>   * Relation to physical `helmholtzFreeEnergy` with semi–classical correction.
>
> 2. Entropy Relations
>   * Pointwise logarithm of (mathematical / physical) Boltzmann probabilities.
>   * Key identity:
>       `differentialEntropy = kB * β * meanEnergy + kB * log Z_math`
>   * Fundamental link:
>       `thermodynamicEntropy = differentialEntropy - kB * dof * log h`
>     (semi–classical correction term).
>   * Specializations removing the correction when `dof = 0` or `phaseSpaceUnit = 1`.
>
> 3. Fundamental Thermodynamic Identity
>   * Proof of `F = U - T S_thermo`.
>   * Equivalent rearrangements giving entropy from energies and free energy.
>   * Discrete / normalized specialization (no correction).
>
> 4. Mean energy as
>       `U = - d/dβ log Z_math`
>       and likewise with the physical partition function (constant factor cancels).

## Design Notes

> * All derivative statements are given as `derivWithin` on `Set.Ioi 0`, matching the physical
>   domain β > 0.
> * Assumptions (finiteness, integrability) are parameterized to keep lemmas reusable.
> * Semi–classical correction appears systematically as
>     `kB * dof * log phaseSpaceUnit`.

## References

> * Same references as `Basic.lean`. [ref: landau\_statphys1]
> * Same references as `Basic.lean`, especially the identities `F = U - T S` and
>   `U = -∂_β log Z`. [ref: tong\_statistical\_physics]

**`CanonicalEnsemble.mathematicalHelmholtzFreeEnergy`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L71).

> An intermediate potential defined from the mathematical partition function. See
> `helmholtzFreeEnergy` for the physical thermodynamic quantity.

```lean
noncomputable def mathematicalHelmholtzFreeEnergy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.helmholtzFreeEnergy_eq_helmholtzMathematicalFreeEnergy_add_correction`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L75).

> The relationship between the physical Helmholtz Free Energy and the Helmholtz Potential.

```lean
lemma helmholtzFreeEnergy_eq_helmholtzMathematicalFreeEnergy_add_correction (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    𝓒.helmholtzFreeEnergy kB T = 𝓒.mathematicalHelmholtzFreeEnergy kB T +
      (kB : ℝ) * T.val * 𝓒.dof * Real.log (𝓒.phaseSpaceunit)
```

**`CanonicalEnsemble.differentialEntropy_eq_kB_beta_meanEnergy_add_kB_log_mathZ`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L85).

> General identity: S\_diff = kB β ⟨E⟩ + kB log Z\_math.
> This connects the differential entropy to the mean energy and the mathematical partition function.
> Integrability of `log (probability …)` follows from the pointwise formula.

```lean
lemma differentialEntropy_eq_kB_beta_meanEnergy_add_kB_log_mathZ
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (hE : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    𝓒.differentialEntropy kB T = (kB : ℝ) * (T.β kB : ℝ) * 𝓒.meanEnergy kB T +
      (kB : ℝ) * Real.log (𝓒.mathematicalPartitionFunction kB T)
```

**`CanonicalEnsemble.log_probability`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L101).

> Pointwise logarithm of the Boltzmann probability.

```lean
lemma log_probability
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    Real.log (𝓒.probability kB T i)
      = - (β kB T) * 𝓒.energy i - Real.log (𝓒.mathematicalPartitionFunction kB T)
```

**`CanonicalEnsemble.kB_mul_beta`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L112).

> Auxiliary identity: `kB · β = 1 / T`.
> `β` is defined as `1 / (kB · T)` (see `Temperature.β`).

```lean
lemma kB_mul_beta (T : Temperature) (hT : 0 < T.val) :
    (kB : ℝ) * (T.β kB : ℝ) = 1 / T.val
```

**`CanonicalEnsemble.thermodynamicEntropy_eq_differentialEntropy_sub_correction`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L121).

> Fundamental relation between thermodynamic and differential entropy:
> `S_thermo = S_diff - kB * dof * log h`.

```lean
lemma thermodynamicEntropy_eq_differentialEntropy_sub_correction
    (T : Temperature)
    (hE : Integrable 𝓒.energy (𝓒.μProd kB T))
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    𝓒.thermodynamicEntropy kB T
      = 𝓒.differentialEntropy kB T
        - (kB : ℝ) * 𝓒.dof * Real.log 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.thermodynamicEntropy_eq_differentialEntropy_of_dof_zero`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L142).

> No semiclassical correction when `dof = 0`.

```lean
lemma thermodynamicEntropy_eq_differentialEntropy_of_dof_zero
    (T : Temperature) (hE : Integrable 𝓒.energy (𝓒.μProd kB T))
    (h0 : 𝓒.dof = 0)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    𝓒.thermodynamicEntropy kB T = 𝓒.differentialEntropy kB T
```

**`CanonicalEnsemble.thermodynamicEntropy_eq_differentialEntropy_of_phase_space_unit_one`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L151).

> No semiclassical correction when `phase_space_unit = 1`.

```lean
lemma thermodynamicEntropy_eq_differentialEntropy_of_phase_space_unit_one
    (T : Temperature) (hE : Integrable 𝓒.energy (𝓒.μProd kB T))
    (h1 : 𝓒.phaseSpaceunit = 1)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    𝓒.thermodynamicEntropy kB T = 𝓒.differentialEntropy kB T
```

## The Fundamental Thermodynamic Identity

**`CanonicalEnsemble.helmholtzFreeEnergy_eq_meanEnergy_sub_temp_mul_thermodynamicEntropy`**, a theorem, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L174). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Helmholtz free energy `F` is related to the mean energy `U` and the absolute
> thermodynamic entropy `S` by the identity `F = U - TS`. This theorem shows that the
> statistically-defined quantities in this framework correctly satisfy this principle of
> thermodynamics.

```lean
theorem helmholtzFreeEnergy_eq_meanEnergy_sub_temp_mul_thermodynamicEntropy
    (T : Temperature) (hT : 0 < T.val)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (hE : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    𝓒.helmholtzFreeEnergy kB T
      = 𝓒.meanEnergy kB T - T.val * 𝓒.thermodynamicEntropy kB T
```

**`CanonicalEnsemble.differentialEntropy_eq_meanEnergy_sub_helmholtz_div_temp_add_correction`**, a theorem, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L198). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Theorem: Helmholtz identity with semi–classical correction term**.
> Physical identity (always true for `T > 0`) :
>   (U - F)/T = S\_thermo
> and:
>   S\_thermo = S\_diff - kB * dof * log h.
> Hence:
>   S\_diff = (U - F)/T + kB * dof * log h.
> This theorem gives the correct relation for the (mathematical / differential) entropy.
> (Removing the correction is only valid in normalized discrete cases
> with `dof = 0` (or `phaseSpaceUnit = 1`).)

```lean
theorem differentialEntropy_eq_meanEnergy_sub_helmholtz_div_temp_add_correction
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (hT : 0 < T.val)
    (hE : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    𝓒.differentialEntropy kB T
      = (𝓒.meanEnergy kB T - 𝓒.helmholtzFreeEnergy kB T) / T.val
        + (kB : ℝ) * 𝓒.dof * Real.log 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.differentialEntropy_eq_meanEnergy_sub_helmholtz_div_temp`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L216).

> Discrete / normalized specialization of the previous theorem.
> If either `dof = 0` (no semiclassical correction) or `phaseSpaceUnit = 1`
> (so `log h = 0`), the correction term vanishes and we recover the bare Helmholtz identity
> for the (differential) entropy.

```lean
lemma differentialEntropy_eq_meanEnergy_sub_helmholtz_div_temp
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (hT : 0 < T.val)
    (hE : Integrable 𝓒.energy (𝓒.μProd kB T))
    (hNorm : 𝓒.dof = 0 ∨ 𝓒.phaseSpaceunit = 1) :
    𝓒.differentialEntropy kB T
      = (𝓒.meanEnergy kB T - 𝓒.helmholtzFreeEnergy kB T) / T.val
```

**`CanonicalEnsemble.hasDerivWithinAt_log_comp`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L230).

> Chain rule convenience lemma for `log ∘ f` on a set.

```lean
lemma hasDerivWithinAt_log_comp
    {f : ℝ → ℝ} {f' : ℝ} {s : Set ℝ} {x : ℝ}
    (hf : HasDerivWithinAt f f' s x) (hx : f x ≠ 0) :
    HasDerivWithinAt (fun t => Real.log (f t)) ((f x)⁻¹ * f') s x
```

**`CanonicalEnsemble.hasDerivWithinAt_log_comp'`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L237).

> A version rewriting the derivative value with `1 / f x`.

```lean
lemma hasDerivWithinAt_log_comp'
    {f : ℝ → ℝ} {f' : ℝ} {s : Set ℝ} {x : ℝ}
    (hf : HasDerivWithinAt f f' s x) (hx : f x ≠ 0) :
    HasDerivWithinAt (fun t => Real.log (f t))
      ((1 / f x) * f') s x
```

**`CanonicalEnsemble.integral_bolt_eq_integral_mul_exp`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L244).

```lean
lemma integral_bolt_eq_integral_mul_exp
    {ι} [MeasurableSpace ι] (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    (φ : ι → ℝ) :
    ∫ x, φ x ∂ 𝓒.μBolt kB T
      = ∫ x, φ x * Real.exp (-T.β kB * 𝓒.energy x) ∂ 𝓒.μ
```

**`CanonicalEnsemble.integral_energy_bolt`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L259).

> A specialization of `integral_bolt_eq_integral_mul_exp`
> to the energy observable.

```lean
lemma integral_energy_bolt
    {ι} [MeasurableSpace ι] (𝓒 : CanonicalEnsemble ι) (T : Temperature) :
    ∫ x, 𝓒.energy x ∂ 𝓒.μBolt kB T
      = ∫ x, 𝓒.energy x * Real.exp (-T.β kB * 𝓒.energy x) ∂ 𝓒.μ
```

**`CanonicalEnsemble.meanEnergy_eq_ratio_of_integrals`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L266).

> The mean energy can be expressed as a ratio of integrals.

```lean
lemma meanEnergy_eq_ratio_of_integrals
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) :
    𝓒.meanEnergy kB T =
      (∫ i, 𝓒.energy i * Real.exp (- T.β kB * 𝓒.energy i) ∂ 𝓒.μ) /
        (∫ i, Real.exp (- T.β kB * 𝓒.energy i) ∂ 𝓒.μ)
```

**`CanonicalEnsemble.meanEnergy_eq_neg_deriv_log_mathZ_of_beta`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L282).

> The mean energy is the negative derivative of the logarithm of the
> (mathematical) partition function with respect to β = 1/(kB T).
> see: Tong (§1.3.2, §1.3.3), L&L (§31, implicitly, and §36)
> Here the derivative is a `derivWithin` over `Set.Ioi 0`
> since `β > 0`.

```lean
lemma meanEnergy_eq_neg_deriv_log_mathZ_of_beta
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    (hT_pos : 0 < T.val) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (h_deriv :
        HasDerivWithinAt
          (fun β : ℝ => ∫ i, Real.exp (-β * 𝓒.energy i) ∂ 𝓒.μ)
          (- ∫ i, 𝓒.energy i * Real.exp (-(T.β kB : ℝ) * 𝓒.energy i) ∂𝓒.μ)
          (Set.Ioi 0) (T.β kB : ℝ)) :
    𝓒.meanEnergy kB T =
      - (derivWithin
          (fun β : ℝ => Real.log (∫ i, Real.exp (-β * 𝓒.energy i) ∂𝓒.μ))
          (Set.Ioi 0) (T.β kB : ℝ))
```

**`CanonicalEnsemble.log_phys_eq_log_math_sub_const_on_Ioi`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L321).

> Helper: equality (on `Set.Ioi 0`) between the β–parametrized logarithm of the
> physical partition function and the β–parametrized logarithm of the *mathematical*
> partition function up to the (β–independent) semiclassical correction. This is used only
> to identify derivatives (the correction drops).
> We add the hypothesis `h_fin` giving finiteness of the Boltzmann measure for every β > 0
> (as needed to ensure the mathematical partition function is strictly positive).

```lean
lemma log_phys_eq_log_math_sub_const_on_Ioi
    (𝓒 : CanonicalEnsemble ι) [NeZero 𝓒.μ]
    (h_fin :
      ∀ β > 0,
        IsFiniteMeasure (𝓒.μBolt kB (Temperature.ofβ kB (Real.toNNReal β)))) :
    Set.EqOn
      (fun β : ℝ =>
        Real.log (𝓒.partitionFunction kB (Temperature.ofβ kB (Real.toNNReal β))))
      (fun β : ℝ =>
        Real.log (∫ i, Real.exp (-β * 𝓒.energy i) ∂ 𝓒.μ)
          - (𝓒.dof : ℝ) * Real.log 𝓒.phaseSpaceunit)
      (Set.Ioi (0 : ℝ))
```

**`CanonicalEnsemble.derivWithin_log_phys_eq_derivWithin_log_math`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L342).

> Derivative equality needed in `meanEnergy_eq_neg_deriv_log_Z_of_beta`.
> Adds `h_fin` (finiteness of the Boltzmann measure for every β > 0).

```lean
lemma derivWithin_log_phys_eq_derivWithin_log_math
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    (hT_pos : 0 < T.val) [NeZero 𝓒.μ]
    (h_fin :
        ∀ β > 0,
          IsFiniteMeasure (𝓒.μBolt kB (Temperature.ofβ kB (Real.toNNReal β)))) :
    derivWithin
      (fun β : ℝ => Real.log (𝓒.partitionFunction kB (ofβ kB (Real.toNNReal β))))
      (Set.Ioi 0) (T.β kB : ℝ)
    =
    derivWithin
      (fun β : ℝ => Real.log (∫ i, Real.exp (-β * 𝓒.energy i) ∂ 𝓒.μ))
      (Set.Ioi 0) (T.β kB : ℝ)
```

**`CanonicalEnsemble.meanEnergy_eq_neg_deriv_log_Z_of_beta`**, a theorem, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L362). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The mean energy can also be expressed as the negative derivative of the logarithm of the
> *physical* partition function with respect to β. This follows from the fact that the physical and
> mathematical partition functions differ only by a constant factor, which vanishes upon
> differentiation.

```lean
theorem meanEnergy_eq_neg_deriv_log_Z_of_beta
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    (hT_pos : 0 < T.val) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (h_fin :
        ∀ β > 0,
          IsFiniteMeasure (𝓒.μBolt kB (Temperature.ofβ kB (Real.toNNReal β))))
    (h_deriv :
        HasDerivWithinAt
          (fun β : ℝ => ∫ i, Real.exp (-β * 𝓒.energy i) ∂ 𝓒.μ)
          (- ∫ i, 𝓒.energy i * Real.exp (-(T.β kB : ℝ) * 𝓒.energy i) ∂𝓒.μ)
          (Set.Ioi 0) (T.β kB : ℝ)) :
    𝓒.meanEnergy kB T =
      - (derivWithin
          (fun β : ℝ => Real.log (𝓒.partitionFunction kB (ofβ kB (Real.toNNReal β))))
          (Set.Ioi 0) (T.β kB : ℝ))
```

## Fluctuations: variance identity

**`CanonicalEnsemble.energyVariance_eq_meanSquareEnergy_sub_meanEnergy_sq`**, a theorem, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L387). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity Var(E) = ⟨E²⟩ - ⟨E⟩².

```lean
theorem energyVariance_eq_meanSquareEnergy_sub_meanEnergy_sq
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) [IsProbabilityMeasure (𝓒.μProd kB T)]
    (hE_int : Integrable 𝓒.energy (𝓒.μProd kB T))
    (hE2_int : Integrable (fun i => (𝓒.energy i)^2) (𝓒.μProd kB T)) :
    𝓒.energyVariance kB T = 𝓒.meanSquareEnergy kB T - (𝓒.meanEnergy kB T)^2
```

## Heat capacity and parametric FDT

**`CanonicalEnsemble.meanEnergyT`**, a def, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L410).

> The mean energy as a function of the real-valued temperature t.

```lean
noncomputable def meanEnergyT (𝓒 : CanonicalEnsemble ι) (t : ℝ) : ℝ
```

**`CanonicalEnsemble.meanEnergyBeta`**, a def, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L414).

> The mean energy as a function of the real-valued inverse temperature b.

```lean
noncomputable def meanEnergyBeta (𝓒 : CanonicalEnsemble ι) (b : ℝ) : ℝ
```

**`CanonicalEnsemble.heatCapacity`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L418).

> The heat capacity (at constant volume) C\_V = ∂U/∂T (as a derivWithin on T > 0).

```lean
noncomputable def heatCapacity (𝓒 : CanonicalEnsemble ι) (T : Temperature) : ℝ
```

**`CanonicalEnsemble.heatCapacity_eq_deriv_meanEnergyBeta`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L422).

> Relates C\_V = dU/dT to dU/dβ. C\_V = dU/dβ * (-1/(kB T²)).

```lean
lemma heatCapacity_eq_deriv_meanEnergyBeta
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (hT_pos : 0 < T.val)
    (hU_deriv :
      HasDerivWithinAt (𝓒.meanEnergyBeta kB)
        (derivWithin (𝓒.meanEnergyBeta kB) (Set.Ioi 0) (T.β kB : ℝ))
        (Set.Ioi 0) (T.β kB : ℝ)) :
    𝓒.heatCapacity kB T
      = (derivWithin (𝓒.meanEnergyBeta kB) (Set.Ioi 0) (T.β kB : ℝ))
        * (-1 / ((kB : ℝ) * (T.val : ℝ)^2))
```

**`CanonicalEnsemble.fluctuation_dissipation_energy_parametric`**, a theorem, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean#L442). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Parametric FDT: C\_V = Var(E)/(kB T²), assuming Var(E) = - dU/dβ.

```lean
theorem fluctuation_dissipation_energy_parametric
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (hT_pos : 0 < T.val)
    (h_Var_eq_neg_dUdβ :
      𝓒.energyVariance kB T = - derivWithin (𝓒.meanEnergyBeta kB) (Set.Ioi 0) (T.β kB : ℝ))
    (hU_deriv :
      DifferentiableWithinAt ℝ (𝓒.meanEnergyBeta kB) (Set.Ioi 0) (T.β kB : ℝ)) :
    𝓒.heatCapacity kB T = 𝓒.energyVariance kB T / ((kB : ℝ) * (T.val : ℝ)^2)
```

## Depends on

- [Canonical Ensemble: Core Definitions](basic.md)

## Sources

- [Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Lemmas.lean)
