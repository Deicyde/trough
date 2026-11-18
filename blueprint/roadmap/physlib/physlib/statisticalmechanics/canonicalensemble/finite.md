---
declaration: module
origin: cited
lean: CanonicalEnsemble.thermodynamicEntropy_eq_shannonEntropy, CanonicalEnsemble.fluctuation_dissipation_theorem_finite, CanonicalEnsemble.IsFinite, CanonicalEnsemble.shannonEntropy, CanonicalEnsemble.mathematicalPartitionFunction_of_fintype, CanonicalEnsemble.partitionFunction_of_fintype, CanonicalEnsemble.μBolt_of_fintype, CanonicalEnsemble.μProd_of_fintype
statement: formalized
proof: formalized
---

# Finite Canonical Ensemble

The module `Physlib.StatisticalMechanics.CanonicalEnsemble.Finite`, [Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean): 38 declarations (6 instances with no name), 15 with a docstring, 2 listed as significant.

> This file specializes the general measure-theoretic framework of the canonical ensemble to systems
> with a finite number of discrete microstates. This is a common and important case in statistical
> mechanics to study models like spin systems (e.g., the Ising model) and other systems with a
> discrete quantum state space.

## Main Definitions and Results

> The specialization is achieved through the `IsFinite` class, which asserts that:
> 1. The type of microstates `ι` is a `Fintype`.
> 2. The measure `μ` on `ι` is the standard counting measure.
> 3. The number of degrees of freedom `dof` is 0.
> 4. The `phaseSpaceunit` is 1.
>
> These assumptions correspond to systems where the state space is fundamentally discrete, and no
> semi-classical approximation from a continuous phase space is needed. Consequently, the
> dimensionless physical quantities are directly equivalent to their mathematical counterparts.
>
> The main results proved in this file are:
> - The abstract integral definitions for thermodynamic quantities (partition function, mean energy)
>   are shown to reduce to the familiar finite sums found in introductory texts. For example, the
>   partition function becomes `Z = ∑ᵢ exp(-β Eᵢ)`.
> - The abstract `thermodynamicEntropy`, defined generally for measure-theoretic systems, is proven
>   to be equal to the standard `shannonEntropy` (`S = -k_B ∑ᵢ pᵢ log pᵢ`). The semi-classical
>   correction terms from the general theory vanish under the `IsFinite` assumptions.
> - The **fluctuation-dissipation theorem** in the form `C_V = Var(E) / (k_B T²)`, which connects the
>   heat capacity `C_V` to the variance of energy fluctuations, is formally proven for these systems.
>
> This file also confirms that the `IsFinite` property is preserved under the composition of
> systems (addition, `nsmul`, and `congr`).

## References

> * L. D. Landau & E. M. Lifshitz, Statistical Physics, Part 1, §31. [ref: landau\_statphys1]
> * D. Tong, Lectures on Statistical Physics, §1.3. [ref: tong\_statistical\_physics]

**`CanonicalEnsemble.IsFinite`**, a class, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L65).

> A finite `CanonicalEnsemble` is one whose microstates form a finite type
> and whose measure is the counting measure. For such systems, the state space is
> inherently discrete and dimensionless, so we require `dof = 0` and
> `phaseSpaceUnit = 1`.

```lean
class IsFinite (𝓒 : CanonicalEnsemble ι) [Fintype ι] : Prop where
  μ_eq_count : 𝓒.μ = Measure.count
  dof_eq_zero : 𝓒.dof = 0
  phase_space_unit_eq_one : 𝓒.phaseSpaceunit = 1
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L70).

```lean
instance [IsFinite 𝓒] [IsFinite 𝓒1] : IsFinite (𝓒 + 𝓒1)
```

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L88).

```lean
instance [IsFinite 𝓒] (e : ι1 ≃ᵐ ι) : IsFinite (congr 𝓒 e)
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L111).

```lean
instance [IsFinite 𝓒] (n : ℕ) : IsFinite (nsmul n 𝓒)
```

**An instance with no name**, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L146).

```lean
instance [IsFinite 𝓒] : IsFiniteMeasure (𝓒.μ)
```

**An instance with no name**, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L151).

> In the finite (counting) case a nonempty index type gives a nonzero measure.

```lean
instance [IsFinite 𝓒] [Nonempty ι] : NeZero 𝓒.μ
```

**`CanonicalEnsemble.shannonEntropy`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L163).

> The Shannon entropy of a finite canonical ensemble.
> This is defined by the formula `S = -k_B ∑ pᵢ log pᵢ`. It is proven to be
> equivalent to the `differentialEntropy` and the `thermodynamicEntropy` for systems
> satisfying the `IsFinite` property.

```lean
noncomputable def shannonEntropy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.mathematicalPartitionFunction_of_fintype`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L166).

```lean
lemma mathematicalPartitionFunction_of_fintype [IsFinite 𝓒] (T : Temperature) :
    𝓒.mathematicalPartitionFunction kB T = ∑ i, exp (- β kB T * 𝓒.energy i)
```

**`CanonicalEnsemble.partitionFunction_of_fintype`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L173).

```lean
lemma partitionFunction_of_fintype [IsFinite 𝓒] (T : Temperature) :
    𝓒.partitionFunction kB T = ∑ i, exp (- T.β kB * 𝓒.energy i)
```

**`CanonicalEnsemble.μBolt_of_fintype`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L179).

```lean
lemma μBolt_of_fintype (T : Temperature) [IsFinite 𝓒] (i : ι) :
    (𝓒.μBolt kB T).real {i} = Real.exp (- β kB T * 𝓒.energy i)
```

**An instance with no name**, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L187).

```lean
instance {T} [IsFinite 𝓒] : IsFiniteMeasure (𝓒.μBolt kB T)
```

**`CanonicalEnsemble.μProd_of_fintype`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L193).

```lean
lemma μProd_of_fintype (T : Temperature) [IsFinite 𝓒] (i : ι) :
    (𝓒.μProd kB T).real {i} = 𝓒.probability kB T i
```

**`CanonicalEnsemble.meanEnergy_of_fintype`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L200).

```lean
lemma meanEnergy_of_fintype [IsFinite 𝓒] (T : Temperature) :
    𝓒.meanEnergy kB T = ∑ i, 𝓒.energy i * 𝓒.probability kB T i
```

**`CanonicalEnsemble.entropy_of_fintype`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L218).

```lean
lemma entropy_of_fintype (T : Temperature) :
    𝓒.shannonEntropy kB T =
      - (kB : ℝ) * ∑ i, 𝓒.probability kB T i * log (𝓒.probability kB T i)
```

**`CanonicalEnsemble.probability_le_one`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L223).

```lean
lemma probability_le_one
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) (i : ι) :
    𝓒.probability kB T i ≤ 1
```

**`CanonicalEnsemble.mathematicalPartitionFunction_pos_finite`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L235).

> Finite specialization: strict positivity of the mathematical partition function.

```lean
lemma mathematicalPartitionFunction_pos_finite
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) :
    0 < 𝓒.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.partitionFunction_pos_finite`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L241).

> Finite specialization: strict positivity of the (physical) partition function.

```lean
lemma partitionFunction_pos_finite
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) :
    0 < 𝓒.partitionFunction kB T
```

**`CanonicalEnsemble.probability_nonneg_finite`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L249).

> Finite specialization: non-negativity (indeed positivity) of probabilities.

```lean
lemma probability_nonneg_finite
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) (i : ι) :
    0 ≤ 𝓒.probability kB T i
```

**`CanonicalEnsemble.sum_probability_eq_one`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L257).

> The sum of probabilities over all microstates is 1.

```lean
lemma sum_probability_eq_one
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) :
    ∑ i, 𝓒.probability kB T i = 1
```

**`CanonicalEnsemble.entropy_nonneg`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L266).

> The entropy of a finite canonical ensemble (Shannon entropy) is non-negative.

```lean
lemma entropy_nonneg [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) :
    0 ≤ 𝓒.shannonEntropy kB T
```

**`CanonicalEnsemble.shannonEntropy_eq_differentialEntropy`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L275).

```lean
lemma shannonEntropy_eq_differentialEntropy
    [MeasurableSingletonClass ι] [IsFinite 𝓒] (T : Temperature) :
    𝓒.shannonEntropy kB T = 𝓒.differentialEntropy kB T
```

**`CanonicalEnsemble.thermodynamicEntropy_eq_shannonEntropy`**, a theorem, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L283). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> In the finite, nonempty case the thermodynamic and Shannon entropies coincide.
> All semi-classical correction factors vanish (`dof = 0`, `phaseSpaceUnit = 1`),
> so the absolute thermodynamic entropy reduces to the discrete Shannon form.

```lean
theorem thermodynamicEntropy_eq_shannonEntropy [MeasurableSingletonClass ι] [IsFinite 𝓒]
    (T : Temperature) :-- (hT : 0 < T.val) :
    𝓒.thermodynamicEntropy kB T = 𝓒.shannonEntropy kB T
```

## Fluctuations in Finite Systems

**`CanonicalEnsemble.meanSquareEnergy_of_fintype`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L313).

```lean
lemma meanSquareEnergy_of_fintype [MeasurableSingletonClass ι] [IsFinite 𝓒] (T : Temperature) :
    𝓒.meanSquareEnergy kB T = ∑ i, (𝓒.energy i)^2 * 𝓒.probability kB T i
```

**`CanonicalEnsemble.energyVariance_of_fintype`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L320).

```lean
lemma energyVariance_of_fintype
    [MeasurableSingletonClass ι] [IsFinite 𝓒] [Nonempty ι] (T : Temperature) :
    𝓒.energyVariance kB T =
      (∑ i, (𝓒.energy i)^2 * 𝓒.probability kB T i) - (𝓒.meanEnergy kB T)^2
```

## β-parameterization for finite systems

**`CanonicalEnsemble.mathematicalPartitionFunctionBetaReal`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L333).

> The finite-sum partition function as a real function of the inverse temperature `b = β`,
> defined by `Z(b) = ∑ i exp (-b * 𝓒.energy i)`.

```lean
noncomputable def mathematicalPartitionFunctionBetaReal (b : ℝ) : ℝ
```

**`CanonicalEnsemble.mathematicalPartitionFunctionBetaReal_pos`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L336).

```lean
lemma mathematicalPartitionFunctionBetaReal_pos [Nonempty ι] (b : ℝ) :
    0 < 𝓒.mathematicalPartitionFunctionBetaReal b
```

**`CanonicalEnsemble.probabilityBetaReal`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L344).

> For inverse temperature `b = β`, the (real-valued) Boltzmann probability of microstate `i`,
> given by `exp (-b * E i) / Z(b)` where `Z(b) = ∑ i exp (-b * E i)`.

```lean
noncomputable def probabilityBetaReal (b : ℝ) (i : ι) : ℝ
```

**`CanonicalEnsemble.meanEnergyBetaReal`**, a def, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L350).

> The mean energy as a function of inverse temperature `b = β` in the finite case,
> defined by `U(b) = ∑ i, E i * p_b i` with `p_b i = exp (-b * E i) / Z(b)` and `Z(b) = ∑ i,
> exp (-b * E i)`.

```lean
noncomputable def meanEnergyBetaReal (b : ℝ) : ℝ
```

**`CanonicalEnsemble.meanEnergy_Beta_eq_finite`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L353).

```lean
lemma meanEnergy_Beta_eq_finite [MeasurableSingletonClass ι] [IsFinite 𝓒] (b : ℝ) (hb : 0 < b) :
    𝓒.meanEnergyBeta kB b = 𝓒.meanEnergyBetaReal b
```

**`CanonicalEnsemble.differentiable_meanEnergyBetaReal`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L363).

```lean
lemma differentiable_meanEnergyBetaReal
    [Nonempty ι] : Differentiable ℝ 𝓒.meanEnergyBetaReal
```

> Derivatives of Z and numerator

**`CanonicalEnsemble.differentiable_mathematicalPartitionFunctionBetaReal`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L375).

```lean
lemma differentiable_mathematicalPartitionFunctionBetaReal :
    Differentiable ℝ 𝓒.mathematicalPartitionFunctionBetaReal
```

**`CanonicalEnsemble.meanEnergyNumerator`**, a def, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L383).

> The numerator in the finite-sum expression of the mean energy as a function of the
> inverse temperature `b = β`,
> namely `∑ i, E i * exp (-b * E i)` (so that `U(b) = meanEnergyNumerator b / Z(b)`).

```lean
noncomputable def meanEnergyNumerator (b : ℝ) : ℝ
```

**`CanonicalEnsemble.differentiable_meanEnergyNumerator`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L386).

```lean
lemma differentiable_meanEnergyNumerator :
    Differentiable ℝ 𝓒.meanEnergyNumerator
```

**`CanonicalEnsemble.deriv_mathematicalPartitionFunctionBetaReal`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L391).

```lean
lemma deriv_mathematicalPartitionFunctionBetaReal (b : ℝ) :
    deriv 𝓒.mathematicalPartitionFunctionBetaReal b = -𝓒.meanEnergyNumerator b
```

**`CanonicalEnsemble.deriv_meanEnergyNumerator`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L404).

```lean
lemma deriv_meanEnergyNumerator (b : ℝ) :
    deriv 𝓒.meanEnergyNumerator b =
      -∑ i, (𝓒.energy i)^2 * Real.exp (-b * 𝓒.energy i)
```

> Quotient rule: dU/db = U^2 - ⟨E^2⟩\_β

**`CanonicalEnsemble.deriv_meanEnergyBetaReal`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L424).

```lean
lemma deriv_meanEnergyBetaReal (b : ℝ) :
    deriv 𝓒.meanEnergyBetaReal b =
    (𝓒.meanEnergyBetaReal b)^2 - ∑ i, (𝓒.energy i)^2 * 𝓒.probabilityBetaReal b i
```

**`CanonicalEnsemble.derivWithin_meanEnergy_Beta_eq_neg_variance`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L447).

> (∂U/∂β) = -Var(E) for finite systems.

```lean
lemma derivWithin_meanEnergy_Beta_eq_neg_variance
    [MeasurableSingletonClass ι][𝓒.IsFinite] (T : Temperature) (hT_pos : 0 < T.val) :
    derivWithin (𝓒.meanEnergyBeta kB) (Set.Ioi 0) (T.β kB : ℝ) = - 𝓒.energyVariance kB T
```

**`CanonicalEnsemble.fluctuation_dissipation_theorem_finite`**, a theorem, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean#L474). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> FDT for finite canonical ensembles: C\_V = Var(E) / (k\_B T²).

```lean
theorem fluctuation_dissipation_theorem_finite
    [MeasurableSingletonClass ι] [𝓒.IsFinite] (T : Temperature) (hT_pos : 0 < T.val) :
    𝓒.heatCapacity kB T = 𝓒.energyVariance kB T / ((kB : ℝ) * (T.val : ℝ)^2)
```

## Depends on

- [Canonical Ensemble: Thermodynamic Identities and Relations](lemmas.md)

## Sources

- [Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Finite.lean)
