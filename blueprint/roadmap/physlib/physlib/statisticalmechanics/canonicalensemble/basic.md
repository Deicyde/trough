---
declaration: module
origin: cited
lean: CanonicalEnsemble, CanonicalEnsemble.ext, CanonicalEnsemble.energy_measurable', CanonicalEnsemble.empty, CanonicalEnsemble.congr, CanonicalEnsemble.congr_energy_comp_symmm, CanonicalEnsemble.nsmul, CanonicalEnsemble.microstates
statement: formalized
proof: formalized
---

# Canonical Ensemble: Core Definitions

The module `Physlib.StatisticalMechanics.CanonicalEnsemble.Basic`, [Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean): 100 declarations (11 instances with no name), 26 with a docstring.

> A *canonical ensemble* describes a system in thermal equilibrium with a heat bath at fixed
> temperature `T`. This file gives a measure–theoretic, semi–classical formalization intended to
> work uniformly for discrete (counting measure) and continuous (Lebesgue–type) models.

## 1. Semi–Classical Normalization

> Classical phase–space integrals produce *dimensionful* quantities. To obtain dimensionless
> thermodynamic objects (and an absolute entropy) we introduce:
>
> * `phaseSpaceUnit : ℝ` (physically Planck's constant `h`);
> * `dof : ℕ` the number of degrees of freedom.
>
> The *physical* partition function is obtained from the *mathematical* one by dividing by
> `phaseSpaceUnit ^ dof`. This yields the standard semi–classical correction preventing
> ambiguities such as the Gibbs paradox.

## 2. Mathematical vs Physical Quantities

> We keep both layers:
>
> * Mathematical / raw:
>   - `mathematicalPartitionFunction kB T` : ∫ exp(-β E) dμ
>   - `probability` (density w.r.t. `μ`)
>   - `differentialEntropy` (can be negative, unit–dependent)
>
> * Physical / dimensionless:
>   - `partitionFunction` : `Z = Z_math / h^dof`
>   - `physicalProbability` : dimensionless density
>   - `helmholtzFreeEnergy` : `F = -kB T log Z`
>   - `thermodynamicEntropy` : absolute entropy `(U - F)/T = -kB ∫ ρ_phys log ρ_phys`
>
> Each physical quantity is expressed explicitly in terms of its mathematical ancestor.

## 3. Core Structure

> We assume `phaseSpaceUnit > 0` and `μ` σ–finite. No probability assumption is imposed:
> normalization is recovered via the Boltzmann weighted measure.

## 4. Boltzmann & Probability Measures

> * `μBolt kB T` : Boltzmann (unnormalized) measure `withDensity exp(-β E)`
> * `μProd kB T` : normalized probability measure (rescaled `μBolt kB T`)
> * `probability kB T i` : the density `exp(-β E(i)) / Z_math`
> * `physicalProbability` : `probability * (phase_space_unit ^ dof)`

## 5. Energies & Entropies

> * `meanEnergy` : expectation of energy under `μProd`.
> * `differentialEntropy` : `-kB ∫ log(probability) dμProd`
> * `thermodynamicEntropy` : `-kB ∫ log(physicalProbability) dμProd`
>   (proved later to coincide with the textbook `(U - F)/T`).
>
> A helper lemma supplies positivity of the partition function under mild assumptions and
> non–negativity criteria for the entropy when `probability ≤ 1` (automatic in finite discrete
> settings, not in general continuous ones).

## 6. Algebraic Operations

> We construct composite ensembles:
>
> * Addition `(𝓒₁ + 𝓒₂)` on product microstates: energies add, measures take product,
>   degrees of freedom add, and (physically) the same `phaseSpaceUnit` is reused.
> * Multiplicity `nsmul n 𝓒`: `n` distinguishable, non–interacting copies (product of `n` copies).
> * Transport along measurable equivalences via `congr`.
>
> These operations respect partition functions, free energies, and (under suitable hypotheses)
> mean energies and integrability.

## 7. Notational & Implementation Notes

> * We work over an arbitrary measurable type `ι`, allowing both finite and continuous models.
> * `β` is accessed through the `Temperature` structure (`T.β kB`, for a Boltzmann constant `kB`).
> * Every quantity that depends on the temperature takes the Boltzmann constant
>   `kB : BoltzmannConstant` before `T`.
> * Most positivity / finiteness conditions are hypotheses on lemmas instead of global axioms,
>   enabling reuse in formal derivations of fluctuation and response identities.

## 8. References

> * L. D. Landau & E. M. Lifshitz, Statistical Physics, Part 1. [ref: landau\_statphys1]
> * D. Tong, Cambridge Lecture Notes (sections on canonical ensemble).
>   - https://www.damtp.cam.ac.uk/user/tong/statphys/one.pdf [ref: tong\_statphys\_notes\_one]
>   - https://www.damtp.cam.ac.uk/user/tong/statphys/two.pdf [ref: tong\_statphys\_notes\_two]

…

**`CanonicalEnsemble`**, a structure, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L113).

> A Canonical ensemble is described by a type `ι`, corresponding to the type of microstates,
> and a map `ι → ℝ` which associates which each microstate an energy
> and physical constants needed to define dimensionless thermodynamic quantities.

```lean
structure CanonicalEnsemble (ι : Type) [MeasurableSpace ι] : Type where
  /-- The energy of associated with a microstate of the canonical ensemble. -/
  energy : ι → ℝ
  /-- The number of degrees of freedom, used to make the partition function dimensionless.
  For a classical system of N particles in 3D, this is `3N`. For a system of N spins,
  this is typically `0` as the state space is already discrete. -/
  dof : ℕ
  /-- The unit of action used to make the phase space volume dimensionless.
  This constant is necessary to define an absolute (rather than relative) thermodynamic
  entropy. In the semi-classical approach, this unit is identified with Planck's constant `h`.
  For discrete systems with a counting measure, this unit should be set to `1`. -/
  phaseSpaceunit : ℝ := 1
  /-- Assumption that the phase space unit is positive. -/
  hPos : 0 < phaseSpaceunit := by positivity
  energy_measurable : Measurable energy
  /-- The measure on the indexing set of microstates. -/
  μ : MeasureTheory.Measure ι := by volume_tac
  [μ_sigmaFinite : SigmaFinite μ]
```

**An instance with no name**, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L139).

```lean
instance : SigmaFinite 𝓒.μ
```

**`CanonicalEnsemble.ext`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L142).

```lean
lemma ext {𝓒 𝓒' : CanonicalEnsemble ι} (h_energy : 𝓒.energy = 𝓒'.energy)
    (h_dof : 𝓒.dof = 𝓒'.dof) (h_h : 𝓒.phaseSpaceunit = 𝓒'.phaseSpaceunit)
    (h_μ : 𝓒.μ = 𝓒'.μ) : 𝓒 = 𝓒'
```

**`CanonicalEnsemble.energy_measurable'`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L148).

```lean
lemma energy_measurable' : Measurable 𝓒.energy
```

**An instance with no name**, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L152).

> The addition of two `CanonicalEnsemble`. The degrees of freedom are added.
> Note: This is only physically meaningful if the two systems share the same `phase_space_unit`.

```lean
noncomputable instance {ι1 ι2 : Type} [MeasurableSpace ι1] [MeasurableSpace ι2] :
    HAdd (CanonicalEnsemble ι1) (CanonicalEnsemble ι2)
    (CanonicalEnsemble (ι1 × ι2))
```

**`CanonicalEnsemble.empty`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L165).

> The canonical ensemble with no microstates.

```lean
def empty : CanonicalEnsemble Empty
```

**`CanonicalEnsemble.congr`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L173).

> Given a measurable equivalence `e : ι1 ≃ᵐ ι`, this is the corresponding canonical ensemble
> on `ι1`. The physical properties (`dof`, `phase_space_unit`) are unchanged.

```lean
noncomputable def congr (e : ι1 ≃ᵐ ι) : CanonicalEnsemble ι1
```

**`CanonicalEnsemble.congr_energy_comp_symmm`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L186).

```lean
lemma congr_energy_comp_symmm (e : ι1 ≃ᵐ ι) :
    (𝓒.congr e).energy ∘ e.symm = 𝓒.energy
```

**`CanonicalEnsemble.nsmul`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L192).

> Scalar multiplication of `CanonicalEnsemble`, defined such that
> `nsmul n 𝓒` represents `n` non-interacting, distinguishable copies of the ensemble `𝓒`.

```lean
noncomputable def nsmul (n : ℕ) (𝓒 : CanonicalEnsemble ι) : CanonicalEnsemble (Fin n → ι)
```

**`CanonicalEnsemble.microstates`**, an abbrev, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L203).

> The microstates of a canonical ensemble.

```lean
abbrev microstates (𝓒 : CanonicalEnsemble ι) : Type
```

## Properties of physical parameters

**`CanonicalEnsemble.dof_add`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L208).

```lean
lemma dof_add (𝓒1 : CanonicalEnsemble ι) (𝓒2 : CanonicalEnsemble ι1) :
    (𝓒1 + 𝓒2).dof = 𝓒1.dof + 𝓒2.dof
```

**`CanonicalEnsemble.phase_space_unit_add`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L212).

```lean
lemma phase_space_unit_add (𝓒1 : CanonicalEnsemble ι) (𝓒2 : CanonicalEnsemble ι1) :
    (𝓒1 + 𝓒2).phaseSpaceunit = 𝓒1.phaseSpaceunit
```

**`CanonicalEnsemble.dof_nsmul`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L216).

```lean
lemma dof_nsmul (n : ℕ) : (nsmul n 𝓒).dof = n * 𝓒.dof
```

**`CanonicalEnsemble.phase_space_unit_nsmul`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L219).

```lean
lemma phase_space_unit_nsmul (n : ℕ) :
    (nsmul n 𝓒).phaseSpaceunit = 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.dof_congr`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L223).

```lean
lemma dof_congr (e : ι1 ≃ᵐ ι) :
    (𝓒.congr e).dof = 𝓒.dof
```

**`CanonicalEnsemble.phase_space_unit_congr`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L227).

```lean
lemma phase_space_unit_congr (e : ι1 ≃ᵐ ι) :
    (𝓒.congr e).phaseSpaceunit = 𝓒.phaseSpaceunit
```

## The measure

**`CanonicalEnsemble.μ_add`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L232).

```lean
lemma μ_add : (𝓒 + 𝓒1).μ = 𝓒.μ.prod 𝓒1.μ
```

**`CanonicalEnsemble.μ_nsmul`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L234).

```lean
lemma μ_nsmul (n : ℕ) : (nsmul n 𝓒).μ = MeasureTheory.Measure.pi fun _ => 𝓒.μ
```

**`CanonicalEnsemble.μ_nsmul_zero_eq`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L236).

```lean
lemma μ_nsmul_zero_eq : (nsmul 0 𝓒).μ = Measure.pi (fun _ => 0)
```

## The energy of the microstates

**`CanonicalEnsemble.energy_add_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L246).

```lean
lemma energy_add_apply (i : microstates (𝓒 + 𝓒1)) :
    (𝓒 + 𝓒1).energy i = 𝓒.energy i.1 + 𝓒1.energy i.2
```

**`CanonicalEnsemble.energy_nsmul_apply`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L250).

```lean
lemma energy_nsmul_apply (n : ℕ) (f : Fin n → microstates 𝓒) :
    (nsmul n 𝓒).energy f = ∑ i, 𝓒.energy (f i)
```

**`CanonicalEnsemble.energy_congr_apply`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L254).

```lean
lemma energy_congr_apply (e : ι1 ≃ᵐ ι) (i : ι1) :
    (𝓒.congr e).energy i = 𝓒.energy (e i)
```

## Induction for nsmul

**`CanonicalEnsemble.nsmul_succ`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L261).

```lean
lemma nsmul_succ (n : ℕ) [SigmaFinite 𝓒.μ] : nsmul n.succ 𝓒 = (𝓒 + nsmul n 𝓒).congr
    (MeasurableEquiv.piFinSuccAbove (fun _ => ι) 0)
```

## Non zero nature of the measure

**An instance with no name**, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L275).

```lean
instance [NeZero 𝓒.μ] [NeZero 𝓒1.μ] : NeZero (𝓒 + 𝓒1).μ
```

**`CanonicalEnsemble.μ_neZero_congr`**, an instance, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L280).

```lean
instance μ_neZero_congr [NeZero 𝓒.μ] (e : ι1 ≃ᵐ ι) :
    NeZero (𝓒.congr e).μ
```

**An instance with no name**, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L284).

```lean
instance [NeZero 𝓒.μ] (n : ℕ) : NeZero (nsmul n 𝓒).μ
```

## The Boltzmann measure

**`CanonicalEnsemble.μBolt`**, a def, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L296).

> The Boltzmann measure on the space of microstates.

```lean
noncomputable def μBolt (T : Temperature) : MeasureTheory.Measure ι
```

**An instance with no name**, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L299).

```lean
instance (T : Temperature) : SigmaFinite (𝓒.μBolt kB T)
```

**`CanonicalEnsemble.μBolt_add`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L304).

```lean
lemma μBolt_add (T : Temperature) :
    (𝓒 + 𝓒1).μBolt kB T = (𝓒.μBolt kB T).prod (𝓒1.μBolt kB T)
```

**`CanonicalEnsemble.μBolt_congr`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L314).

```lean
lemma μBolt_congr (e : ι1 ≃ᵐ ι) (T : Temperature) : (𝓒.congr e).μBolt kB T =
    (𝓒.μBolt kB T).map e.symm
```

**`CanonicalEnsemble.μBolt_nsmul`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L324).

```lean
lemma μBolt_nsmul [SigmaFinite 𝓒.μ] (n : ℕ) (T : Temperature) :
    (nsmul n 𝓒).μBolt kB T = MeasureTheory.Measure.pi fun _ => (𝓒.μBolt kB T)
```

**`CanonicalEnsemble.μBolt_ne_zero_of_μ_ne_zero`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L334).

```lean
lemma μBolt_ne_zero_of_μ_ne_zero (T : Temperature) (h : 𝓒.μ ≠ 0) :
    𝓒.μBolt kB T ≠ 0
```

**An instance with no name**, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L340).

```lean
instance (T : Temperature) [NeZero 𝓒.μ] : NeZero (𝓒.μBolt kB T)
```

**An instance with no name**, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L345).

```lean
instance (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [IsFiniteMeasure (𝓒1.μBolt kB T)] :
    IsFiniteMeasure ((𝓒 + 𝓒1).μBolt kB T)
```

**An instance with no name**, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L349).

```lean
instance (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] (n : ℕ) :
    IsFiniteMeasure ((nsmul n 𝓒).μBolt kB T)
```

## The Mathematical Partition Function

**`CanonicalEnsemble.mathematicalPartitionFunction`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L362).

> The mathematical partition function, defined as the integral of the Boltzmann factor.
> This quantity may have physical dimensions. See `CanonicalEnsemble.partitionFunction` for
> the dimensionless physical version.

```lean
noncomputable def mathematicalPartitionFunction (T : Temperature) : ℝ
```

**`CanonicalEnsemble.mathematicalPartitionFunction_eq_integral`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L365).

```lean
lemma mathematicalPartitionFunction_eq_integral (T : Temperature) :
    mathematicalPartitionFunction kB 𝓒 T = ∫ i, exp (- T.β kB * 𝓒.energy i) ∂𝓒.μ
```

**`CanonicalEnsemble.mathematicalPartitionFunction_add`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L374).

```lean
lemma mathematicalPartitionFunction_add {T : Temperature} :
    (𝓒 + 𝓒1).mathematicalPartitionFunction kB T =
    𝓒.mathematicalPartitionFunction kB T * 𝓒1.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.mathematicalPartitionFunction_congr`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L381).

```lean
lemma mathematicalPartitionFunction_congr (e : ι1 ≃ᵐ ι) (T : Temperature) :
    (𝓒.congr e).mathematicalPartitionFunction kB T = 𝓒.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.mathematicalPartitionFunction_nsmul`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L386).

> The `mathematicalPartitionFunction_nsmul` function of `n` copies of a canonical ensemble.

```lean
lemma mathematicalPartitionFunction_nsmul (n : ℕ) (T : Temperature) :
    (nsmul n 𝓒).mathematicalPartitionFunction kB T =
      (𝓒.mathematicalPartitionFunction kB T) ^ n
```

**`CanonicalEnsemble.mathematicalPartitionFunction_nonneg`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L391).

```lean
lemma mathematicalPartitionFunction_nonneg (T : Temperature) :
    0 ≤ 𝓒.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.mathematicalPartitionFunction_eq_zero_iff`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L394).

```lean
lemma mathematicalPartitionFunction_eq_zero_iff (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] :
    mathematicalPartitionFunction kB 𝓒 T = 0 ↔ 𝓒.μ = 0
```

**`CanonicalEnsemble.mathematicalPartitionFunction_comp_ofβ_apply`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L404).

```lean
lemma mathematicalPartitionFunction_comp_ofβ_apply (β : ℝ≥0) :
    𝓒.mathematicalPartitionFunction kB (ofβ kB β) =
    (𝓒.μ.withDensity (fun i => ENNReal.ofReal (exp (- β * 𝓒.energy i)))).real Set.univ
```

**`CanonicalEnsemble.mathematicalPartitionFunction_pos`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L411).

> The partition function is strictly positive provided the underlying
> measure is non-zero and the Boltzmann measure is finite.

```lean
lemma mathematicalPartitionFunction_pos (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    0 < 𝓒.mathematicalPartitionFunction kB T
```

## The probability density

**`CanonicalEnsemble.probability`**, a def, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L423).

> The probability density function of the canonical ensemble.
> Note: In the general measure-theoretic case, this is a density with respect to the
> underlying measure `𝓒.μ` and is not necessarily less than or equal to 1. In the
> case of a finite ensemble with the counting measure, this value corresponds to the
> probability of the microstate.

```lean
noncomputable def probability (T : Temperature) (i : ι) : ℝ
```

## The probability measure

**`CanonicalEnsemble.probability_add`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L429).

```lean
lemma probability_add {T : Temperature} (i : ι × ι1) :
    (𝓒 + 𝓒1).probability kB T i = 𝓒.probability kB T i.1 * 𝓒1.probability kB T i.2
```

**`CanonicalEnsemble.probability_congr`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L434).

```lean
lemma probability_congr (e : ι1 ≃ᵐ ι) (T : Temperature) (i : ι1) :
    (𝓒.congr e).probability kB T i = 𝓒.probability kB T (e i)
```

**`CanonicalEnsemble.probability_nsmul`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L438).

```lean
lemma probability_nsmul (n : ℕ) (T : Temperature) (f : Fin n → ι) :
    (nsmul n 𝓒).probability kB T f = ∏ i, 𝓒.probability kB T (f i)
```

**`CanonicalEnsemble.μProd`**, a def, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L450).

> The probability measure associated with the Boltzmann distribution of a
> canonical ensemble.

```lean
noncomputable def μProd (T : Temperature) : MeasureTheory.Measure ι
```

**An instance with no name**, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L453).

```lean
instance (T : Temperature) : SigmaFinite (𝓒.μProd kB T)
```

**An instance with no name**, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L456).

```lean
instance (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)]
  [NeZero 𝓒.μ] : IsProbabilityMeasure (𝓒.μProd kB T)
```

**An instance with no name**, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L460).

```lean
instance {T} : IsFiniteMeasure (𝓒.μProd kB T)
```

**`CanonicalEnsemble.μProd_add`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L464).

```lean
lemma μProd_add {T : Temperature} [IsFiniteMeasure (𝓒.μBolt kB T)]
    [IsFiniteMeasure (𝓒1.μBolt kB T)] :
    (𝓒 + 𝓒1).μProd kB T = (𝓒.μProd kB T).prod (𝓒1.μProd kB T)
```

**`CanonicalEnsemble.μProd_congr`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L472).

```lean
lemma μProd_congr (e : ι1 ≃ᵐ ι) (T : Temperature) :
    (𝓒.congr e).μProd kB T = (𝓒.μProd kB T).map e.symm
```

**`CanonicalEnsemble.μProd_nsmul`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L477).

```lean
lemma μProd_nsmul (n : ℕ) (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] :
    (nsmul n 𝓒).μProd kB T = MeasureTheory.Measure.pi fun _ => 𝓒.μProd kB T
```

## Integrability of energy

**`CanonicalEnsemble.integrable_energy_add`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L494).

```lean
lemma integrable_energy_add (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)]
    [IsFiniteMeasure (𝓒1.μBolt kB T)]
    (h : Integrable 𝓒.energy (𝓒.μProd kB T)) (h1 : Integrable 𝓒1.energy (𝓒1.μProd kB T)) :
    Integrable (𝓒 + 𝓒1).energy ((𝓒 + 𝓒1).μProd kB T)
```

**`CanonicalEnsemble.integrable_energy_congr`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L502).

```lean
lemma integrable_energy_congr (T : Temperature) (e : ι1 ≃ᵐ ι)
    (h : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    Integrable (𝓒.congr e).energy ((𝓒.congr e).μProd kB T)
```

**`CanonicalEnsemble.integrable_energy_nsmul`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L509).

```lean
lemma integrable_energy_nsmul (n : ℕ) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)]
    (h : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    Integrable (nsmul n 𝓒).energy ((nsmul n 𝓒).μProd kB T)
```

## The mean energy

**`CanonicalEnsemble.meanEnergy`**, a def, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L526).

> The mean energy of the canonical ensemble at temperature `T`.

```lean
noncomputable def meanEnergy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.meanSquareEnergy`**, a def, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L529).

> The mean square energy ⟨E²⟩ of the canonical ensemble at temperature T.

```lean
noncomputable def meanSquareEnergy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.energyVariance`**, a def, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L533).

> Energy variance at temperature `T`.

```lean
noncomputable def energyVariance (T : Temperature) : ℝ
```

**`CanonicalEnsemble.meanEnergy_add`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L537).

```lean
lemma meanEnergy_add {T : Temperature}
    [IsFiniteMeasure (𝓒1.μBolt kB T)] [IsFiniteMeasure (𝓒.μBolt kB T)]
    [NeZero 𝓒.μ] [NeZero 𝓒1.μ]
    (h1 : Integrable 𝓒.energy (𝓒.μProd kB T))
    (h2 : Integrable 𝓒1.energy (𝓒1.μProd kB T)) :
    (𝓒 + 𝓒1).meanEnergy kB T = 𝓒.meanEnergy kB T + 𝓒1.meanEnergy kB T
```

**`CanonicalEnsemble.meanEnergy_congr`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L548).

```lean
lemma meanEnergy_congr (e : ι1 ≃ᵐ ι) (T : Temperature) :
    (𝓒.congr e).meanEnergy kB T = 𝓒.meanEnergy kB T
```

**`CanonicalEnsemble.meanEnergy_nsmul`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L553).

```lean
lemma meanEnergy_nsmul (n : ℕ) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (h1 : Integrable 𝓒.energy (𝓒.μProd kB T)) :
    (nsmul n 𝓒).meanEnergy kB T = n * 𝓒.meanEnergy kB T
```

## The differential entropy

**`CanonicalEnsemble.differentialEntropy`**, a def, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L574).

> The (differential) entropy of the canonical ensemble. In the continuous case, this quantity
> is not absolute but depends on the choice of units for the measure. It can be negative.
> See `thermodynamicEntropy` for the absolute physical quantity.

```lean
noncomputable def differentialEntropy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.probability_nonneg`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L581).

> Probabilities are non-negative, assuming a positive partition function.

```lean
lemma probability_nonneg
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    0 ≤ 𝓒.probability kB T i
```

**`CanonicalEnsemble.probability_pos`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L587).

> Probabilities are strictly positive.

```lean
lemma probability_pos
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    0 < 𝓒.probability kB T i
```

**`CanonicalEnsemble.differentialEntropy_nonneg_of_prob_le_one`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L596).

> General entropy non-negativity under a pointwise upper bound `probability ≤ 1`.
> This assumption holds automatically in the finite/counting case (since sums bound each term),
> but can fail in general (continuous) settings; hence we separate it as a hypothesis.
> Finite case: see `CanonicalEnsemble.entropy_nonneg` in `Finite`.

```lean
lemma differentialEntropy_nonneg_of_prob_le_one
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ]
    (hInt : Integrable (fun i => Real.log (𝓒.probability kB T i)) (𝓒.μProd kB T))
    (hP_le_one : ∀ i, 𝓒.probability kB T i ≤ 1) :
    0 ≤ 𝓒.differentialEntropy kB T
```

## Thermodynamic Quantities

> These are the dimensionless physical quantities derived from the mathematical definitions
> by incorporating the phase space volume `𝓒.phaseSpaceUnit ^ 𝓒.dof`.

**`CanonicalEnsemble.partitionFunction`**, a def, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L615).

> The dimensionless thermodynamic partition function, `Z = Z_math / h^dof`.

```lean
noncomputable def partitionFunction (T : Temperature) : ℝ
```

**`CanonicalEnsemble.partitionFunction_def`**, a lemma, [line 619](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L619).

```lean
lemma partitionFunction_def (𝓒 : CanonicalEnsemble ι) (T : Temperature) :
    𝓒.partitionFunction kB T =
      𝓒.mathematicalPartitionFunction kB T / (𝓒.phaseSpaceunit ^ 𝓒.dof)
```

**`CanonicalEnsemble.partitionFunction_pos`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L623).

```lean
lemma partitionFunction_pos
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    0 < 𝓒.partitionFunction kB T
```

**`CanonicalEnsemble.partitionFunction_congr`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L629).

```lean
lemma partitionFunction_congr
    (𝓒 : CanonicalEnsemble ι) (e : ι1 ≃ᵐ ι) (T : Temperature) :
    (𝓒.congr e).partitionFunction kB T = 𝓒.partitionFunction kB T
```

**`CanonicalEnsemble.partitionFunction_add`**, a lemma, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L634).

```lean
lemma partitionFunction_add
    (𝓒 : CanonicalEnsemble ι) (𝓒1 : CanonicalEnsemble ι1)
    (T : Temperature)
    (h : 𝓒.phaseSpaceunit = 𝓒1.phaseSpaceunit) :
    (𝓒 + 𝓒1).partitionFunction kB T
      = 𝓒.partitionFunction kB T * 𝓒1.partitionFunction kB T
```

**`CanonicalEnsemble.partitionFunction_nsmul`**, a lemma, [line 642](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L642).

```lean
lemma partitionFunction_nsmul
    (𝓒 : CanonicalEnsemble ι) (n : ℕ) (T : Temperature) :
    (nsmul n 𝓒).partitionFunction kB T
      = (𝓒.partitionFunction kB T) ^ n
```

**`CanonicalEnsemble.partitionFunction_dof_zero`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L648).

```lean
lemma partitionFunction_dof_zero
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (h : 𝓒.dof = 0) :
    𝓒.partitionFunction kB T = 𝓒.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.partitionFunction_phase_space_unit_one`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L653).

```lean
lemma partitionFunction_phase_space_unit_one
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (h : 𝓒.phaseSpaceunit = 1) :
    𝓒.partitionFunction kB T = 𝓒.mathematicalPartitionFunction kB T
```

**`CanonicalEnsemble.log_partitionFunction`**, a lemma, [line 658](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L658).

```lean
lemma log_partitionFunction
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    Real.log (𝓒.partitionFunction kB T)
      = Real.log (𝓒.mathematicalPartitionFunction kB T)
        - (𝓒.dof : ℝ) * Real.log 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.log_partitionFunction_ofβ`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L669).

> A rewriting form convenient under a coercion to a temperature obtained from an inverse
> temperature.

```lean
lemma log_partitionFunction_ofβ
    (𝓒 : CanonicalEnsemble ι) (β : ℝ≥0)
    [IsFiniteMeasure (𝓒.μBolt kB (ofβ kB β))] [NeZero 𝓒.μ] :
    Real.log (𝓒.partitionFunction kB (ofβ kB β))
      = Real.log (𝓒.mathematicalPartitionFunction kB (ofβ kB β))
        - (𝓒.dof : ℝ) * Real.log 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.log_mathematicalPartitionFunction_eq`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L678).

> The logarithm of the mathematical partition function as an integral.

```lean
lemma log_mathematicalPartitionFunction_eq
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) :
    Real.log (𝓒.mathematicalPartitionFunction kB T)
      = Real.log (∫ i, Real.exp (- T.β kB * 𝓒.energy i) ∂ 𝓒.μ)
```

**`CanonicalEnsemble.helmholtzFreeEnergy`**, a def, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L686).

> The Helmholtz free energy, `F = -k_B T log(Z)`. This is the central
> quantity from which other thermodynamic properties are derived.

```lean
noncomputable def helmholtzFreeEnergy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.helmholtzFreeEnergy_def`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L690).

```lean
lemma helmholtzFreeEnergy_def
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) :
    𝓒.helmholtzFreeEnergy kB T = - (kB : ℝ) * T.val * Real.log (𝓒.partitionFunction kB T)
```

**`CanonicalEnsemble.helmholtzFreeEnergy_congr`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L694).

```lean
lemma helmholtzFreeEnergy_congr
    (𝓒 : CanonicalEnsemble ι) (e : ι1 ≃ᵐ ι) (T : Temperature) :
    (𝓒.congr e).helmholtzFreeEnergy kB T = 𝓒.helmholtzFreeEnergy kB T
```

**`CanonicalEnsemble.helmholtzFreeEnergy_dof_zero`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L699).

```lean
lemma helmholtzFreeEnergy_dof_zero
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (h : 𝓒.dof = 0) :
    𝓒.helmholtzFreeEnergy kB T
      = -(kB : ℝ) * T.val * Real.log (𝓒.mathematicalPartitionFunction kB T)
```

**`CanonicalEnsemble.helmholtzFreeEnergy_phase_space_unit_one`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L705).

```lean
lemma helmholtzFreeEnergy_phase_space_unit_one
    (𝓒 : CanonicalEnsemble ι) (T : Temperature) (h : 𝓒.phaseSpaceunit = 1) :
    𝓒.helmholtzFreeEnergy kB T
      = -(kB : ℝ) * T.val * Real.log (𝓒.mathematicalPartitionFunction kB T)
```

**`CanonicalEnsemble.helmholtzFreeEnergy_add`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L711).

```lean
lemma helmholtzFreeEnergy_add
    (𝓒 : CanonicalEnsemble ι) (𝓒1 : CanonicalEnsemble ι1) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [IsFiniteMeasure (𝓒1.μBolt kB T)]
    [NeZero 𝓒.μ] [NeZero 𝓒1.μ]
    (h : 𝓒.phaseSpaceunit = 𝓒1.phaseSpaceunit) :
    (𝓒 + 𝓒1).helmholtzFreeEnergy kB T
      = 𝓒.helmholtzFreeEnergy kB T + 𝓒1.helmholtzFreeEnergy kB T
```

**`CanonicalEnsemble.helmholtzFreeEnergy_nsmul`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L723).

```lean
lemma helmholtzFreeEnergy_nsmul
    (𝓒 : CanonicalEnsemble ι) (n : ℕ) (T : Temperature) :
    (nsmul n 𝓒).helmholtzFreeEnergy kB T
      = n * 𝓒.helmholtzFreeEnergy kB T
```

**`CanonicalEnsemble.physicalProbability`**, a def, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L733).

> The dimensionless physical probability density. This is is the probability density w.r.t. the
> measure, obtained by dividing the phase space measure by the fundamental unit `h^dof`, making the
> probability density `ρ_phys = ρ_math * h^dof` dimensionless.

```lean
noncomputable def physicalProbability (T : Temperature) (i : ι) : ℝ
```

**`CanonicalEnsemble.physicalProbability_def`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L737).

```lean
lemma physicalProbability_def (T : Temperature) (i : ι) :
    𝓒.physicalProbability kB T i
      = 𝓒.probability kB T i * (𝓒.phaseSpaceunit ^ 𝓒.dof)
```

**`CanonicalEnsemble.physicalProbability_measurable`**, a lemma, [line 741](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L741).

```lean
lemma physicalProbability_measurable (T : Temperature) :
    Measurable (𝓒.physicalProbability kB T)
```

**`CanonicalEnsemble.physicalProbability_nonneg`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L746).

```lean
lemma physicalProbability_nonneg
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    0 ≤ 𝓒.physicalProbability kB T i
```

**`CanonicalEnsemble.physicalProbability_pos`**, a lemma, [line 751](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L751).

```lean
lemma physicalProbability_pos
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    0 < 𝓒.physicalProbability kB T i
```

**`CanonicalEnsemble.log_physicalProbability`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L756).

```lean
lemma log_physicalProbability
    (T : Temperature) [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] (i : ι) :
    Real.log (𝓒.physicalProbability kB T i)
      = Real.log (𝓒.probability kB T i) + (𝓒.dof : ℝ) * Real.log 𝓒.phaseSpaceunit
```

**`CanonicalEnsemble.integral_probability`**, a lemma, [line 763](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L763).

```lean
lemma integral_probability
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    (∫ i, 𝓒.probability kB T i ∂ 𝓒.μ) = 1
```

**`CanonicalEnsemble.integral_physicalProbability_base`**, a lemma, [line 772](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L772).

> Normalization of the dimensionless physical probability density over the base measure.

```lean
lemma integral_physicalProbability_base
    (𝓒 : CanonicalEnsemble ι) (T : Temperature)
    [IsFiniteMeasure (𝓒.μBolt kB T)] [NeZero 𝓒.μ] :
    (∫ i, 𝓒.physicalProbability kB T i ∂ 𝓒.μ)
      = 𝓒.phaseSpaceunit ^ 𝓒.dof
```

**`CanonicalEnsemble.physicalProbability_dof_zero`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L779).

```lean
lemma physicalProbability_dof_zero
    (T : Temperature) (h : 𝓒.dof = 0) (i : ι) :
    𝓒.physicalProbability kB T i = 𝓒.probability kB T i
```

**`CanonicalEnsemble.physicalProbability_phase_space_unit_one`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L784).

```lean
lemma physicalProbability_phase_space_unit_one
    (T : Temperature) (h : 𝓒.phaseSpaceunit = 1) (i : ι) :
    𝓒.physicalProbability kB T i = 𝓒.probability kB T i
```

**`CanonicalEnsemble.physicalProbability_congr`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L789).

```lean
lemma physicalProbability_congr (e : ι1 ≃ᵐ ι) (T : Temperature) (i : ι1) :
    (𝓒.congr e).physicalProbability kB T i
      = 𝓒.physicalProbability kB T (e i)
```

**`CanonicalEnsemble.physicalProbability_add`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L794).

```lean
lemma physicalProbability_add
    {ι1} [MeasurableSpace ι1]
    (𝓒1 : CanonicalEnsemble ι1) (T : Temperature) (i : ι × ι1)
    (h : 𝓒.phaseSpaceunit = 𝓒1.phaseSpaceunit) :
    (𝓒 + 𝓒1).physicalProbability kB T i
      = 𝓒.physicalProbability kB T i.1 * 𝓒1.physicalProbability kB T i.2
```

**`CanonicalEnsemble.thermodynamicEntropy`**, a def, [line 806](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L806).

> The absolute thermodynamic entropy, defined from its statistical mechanical foundation as
> the Gibbs-Shannon entropy of the dimensionless physical probability distribution.
> This corresponds to Landau & Lifshitz, Statistical Physics, §7, Eq. 7.12.

```lean
noncomputable def thermodynamicEntropy (T : Temperature) : ℝ
```

**`CanonicalEnsemble.thermodynamicEntropy_def`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean#L810).

```lean
lemma thermodynamicEntropy_def (T : Temperature) :
    𝓒.thermodynamicEntropy kB T =
      -(kB : ℝ) * ∫ i, Real.log (𝓒.physicalProbability kB T i) ∂ 𝓒.μProd kB T
```

## Depends on

- [Temperature](../../thermodynamics/temperature/basic.md)

## Sources

- [Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/Basic.lean)
