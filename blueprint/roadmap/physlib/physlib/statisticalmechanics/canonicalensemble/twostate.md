---
declaration: module
origin: cited
lean: CanonicalEnsemble.twoState, CanonicalEnsemble.twoState_partitionFunction_apply, CanonicalEnsemble.twoState_partitionFunction_apply_eq_cosh, CanonicalEnsemble.twoState_energy_fst, CanonicalEnsemble.twoState_energy_snd, CanonicalEnsemble.twoState_probability_fst, CanonicalEnsemble.twoState_probability_snd, CanonicalEnsemble.twoState_meanEnergy_eq
statement: formalized
proof: formalized
---

# Two-state canonical ensemble

The module `Physlib.StatisticalMechanics.CanonicalEnsemble.TwoState`, [Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean): 13 declarations (1 instance with no name), 7 with a docstring.

> This module contains the definitions and properties related to the two-state
> canonical ensemble.

**`CanonicalEnsemble.twoState`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L29).

> The canonical ensemble corresponding to state system, with one state of energy
> `E₀` and the other state of energy `E₁`.

```lean
noncomputable def twoState (E₀ E₁ : ℝ) : CanonicalEnsemble (Fin 2)
```

**An instance with no name**, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L35).

```lean
instance {E₀ E₁} : IsFinite (twoState E₀ E₁)
```

**`CanonicalEnsemble.twoState_partitionFunction_apply`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L40).

```lean
lemma twoState_partitionFunction_apply (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).partitionFunction kB T = exp (- β kB T * E₀) + exp (- β kB T * E₁)
```

**`CanonicalEnsemble.twoState_partitionFunction_apply_eq_cosh`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L45).

```lean
lemma twoState_partitionFunction_apply_eq_cosh (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).partitionFunction kB T =
    2 * exp (- β kB T * (E₀ + E₁) / 2) * cosh (β kB T * (E₁ - E₀) / 2)
```

**`CanonicalEnsemble.twoState_energy_fst`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L54).

```lean
lemma twoState_energy_fst (E₀ E₁ : ℝ) : (twoState E₀ E₁).energy 0 = E₀
```

**`CanonicalEnsemble.twoState_energy_snd`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L58).

```lean
lemma twoState_energy_snd (E₀ E₁ : ℝ) : (twoState E₀ E₁).energy 1 = E₁
```

**`CanonicalEnsemble.twoState_probability_fst`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L62).

> Probability of the first state (energy `E₀`) in closed form.

```lean
lemma twoState_probability_fst (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).probability kB T 0 = 1 / 2 * (1 + Real.tanh (β kB T * (E₁ - E₀) / 2))
```

**`CanonicalEnsemble.twoState_probability_snd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L79).

> Probability of the second state (energy `E₁`) in closed form.

```lean
lemma twoState_probability_snd (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).probability kB T 1 = 1 / 2 * (1 - Real.tanh (β kB T * (E₁ - E₀) / 2))
```

**`CanonicalEnsemble.twoState_meanEnergy_eq`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L95).

```lean
lemma twoState_meanEnergy_eq (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).meanEnergy kB T =
    (E₀ + E₁) / 2 - (E₁ - E₀) / 2 * Real.tanh (β kB T * (E₁ - E₀) / 2)
```

**`CanonicalEnsemble.twoState_entropy_eq`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L106).

> A simplification of the `entropy` of the two-state canonical ensemble.
>
> Since `β kB 0 = 0`, at `T = 0` the right-hand side evaluates to `kB * Real.log 2`.
> See `twoState_entropy_eq_T_neq_zero` for the same statement carrying `T ≠ 0`.

```lean
lemma twoState_entropy_eq (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).thermodynamicEntropy kB T =
      (kB : ℝ) * (Real.log (2 * Real.cosh (β kB T * (E₁ - E₀) / 2))
        - β kB T * (E₁ - E₀) / 2 * Real.tanh (β kB T * (E₁ - E₀) / 2))
```

**`CanonicalEnsemble.twoState_entropy_eq_T_neq_zero`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L128).

> An instance of `twoState_entropy_eq` assuming T ≠ 0

```lean
lemma twoState_entropy_eq_T_neq_zero (E₀ E₁ : ℝ) (T : Temperature) (_ : T ≠ 0) :
    (twoState E₀ E₁).thermodynamicEntropy kB T =
      (kB : ℝ) * (Real.log (2 * Real.cosh (β kB T * (E₁ - E₀) / 2))
        - β kB T * (E₁ - E₀) / 2 * Real.tanh (β kB T * (E₁ - E₀) / 2))
```

**`CanonicalEnsemble.twoState_helmholtzFreeEnergy_eq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L135).

> A simplification of the `helmholtzFreeEnergy` of the two-state canonical ensemble.

```lean
lemma twoState_helmholtzFreeEnergy_eq (E₀ E₁ : ℝ) (T : Temperature) :
    (twoState E₀ E₁).helmholtzFreeEnergy kB T =
      (β kB T  * (E₀ + E₁) / 2 - Real.log
          (2 * Real.cosh (β kB T * (E₁ - E₀) / 2))) / β kB T
```

**`CanonicalEnsemble.twoState_helmholtzFreeEnergy_eq_T_neq_zero`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean#L160).

> An instance of `twoState_helmholtzFreeEnergy_eq` assuming T ≠ 0

```lean
lemma twoState_helmholtzFreeEnergy_eq_T_neq_zero (E₀ E₁ : ℝ) (T : Temperature) (Th : T ≠ 0) :
    (twoState E₀ E₁).helmholtzFreeEnergy kB T =
      (E₀ + E₁) / 2 - Real.log (2 * Real.cosh (β kB T * (E₁ - E₀) / 2)) / β kB T
```

## Depends on

- [Finite Canonical Ensemble](finite.md)

## Sources

- [Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/CanonicalEnsemble/TwoState.lean)
