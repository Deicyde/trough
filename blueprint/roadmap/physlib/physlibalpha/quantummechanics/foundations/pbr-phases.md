---
declaration: module
origin: cited
lean: QuantumMechanics.PBR.exists_two_mul_pow_le, QuantumMechanics.PBR.exists_norm_pow_sub_pow_eq, QuantumMechanics.PBR.prod_phase_mul_prod_amp, QuantumMechanics.PBR.norm_prod_phase, QuantumMechanics.PBR.sum_phases_mul_amp, QuantumMechanics.PBR.exists_phases
statement: formalized
proof: formalized
---

# The choice of the PBR phases

The module `PhyslibAlpha.QuantumMechanics.Foundations.PBR.Phases`, [PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean): 6 declarations, 6 with a docstring.

> The choice of the number of copies, the angle and the unit-modulus phases in the PBR measurement.

## i. Overview

> The entangled measurement in the Pusey–Barrett–Rudolph (PBR) theorem acts on `n` qubits and
> involves a family of unit-modulus phases `ω z`. The product states it is tested against have real
> amplitudes `∏ i, ![c, s] (z i)` on the computational basis vectors `z`, with `0 ≤ s ≤ c`. This
> file makes the two choices on which the construction rests: a number of copies `n` with
> `2 cⁿ ≤ (c + s)ⁿ`, and phases with `∑ z, ω z * ∏ i, ![c, s] (z i) = 0`, found with the
> intermediate value theorem. In the PBR proof the latter makes every outcome of the measurement
> orthogonal to one product state.

## ii. Key results

> - `PBR.exists_two_mul_pow_le` : the choice of the number of copies.
> - `PBR.exists_norm_pow_sub_pow_eq` : the choice of the angle.
> - `PBR.exists_phases` : the choice of the unit-modulus phases.

## iv. References

> - M. F. Pusey, J. Barrett and T. Rudolph, *On the reality of the quantum state*,
>   Nature Phys. 8, 475–478 (2012), arXiv:1111.3328. [ref: Pusey:2011de]

## A. Choosing the number of copies

**`QuantumMechanics.PBR.exists_two_mul_pow_le`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L58).

> For `0 < c` and `0 < s`, some number of copies `n` gives `2 cⁿ ≤ (c + s)ⁿ`.

```lean
lemma exists_two_mul_pow_le {c s : ℝ} (hc : 0 < c) (hs : 0 < s) :
    ∃ n : ℕ, 2 * c ^ n ≤ (c + s) ^ n
```

## B. Choosing the phases

### B.1. Choosing the angle

**`QuantumMechanics.PBR.exists_norm_pow_sub_pow_eq`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L74).

> If `0 ≤ s ≤ c` and `2 cⁿ ≤ (c + s)ⁿ`, some angle `α` gives
> `‖(c + e^{iα} s)ⁿ - cⁿ‖ = cⁿ` (intermediate value theorem on `[0, π]`).

```lean
lemma exists_norm_pow_sub_pow_eq {c s : ℝ} {n : ℕ} (hs : 0 ≤ s) (hsc : s ≤ c)
    (hn : 2 * c ^ n ≤ (c + s) ^ n) :
    ∃ α : ℝ, ‖((c : ℂ) + Complex.exp (α * Complex.I) * s) ^ n - (c : ℂ) ^ n‖ = c ^ n
```

### B.2. Products of amplitudes

**`QuantumMechanics.PBR.prod_phase_mul_prod_amp`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L113).

> The phase product `∏ i, ![1, e] (z i)` times the amplitude product `∏ i, ![c, s] (z i)` is
> the amplitude product `∏ i, ![c, e * s] (z i)`.

```lean
lemma prod_phase_mul_prod_amp {n : ℕ} (e c s : ℂ) (z : Fin n → Fin 2) :
    (∏ i, ![1, e] (z i)) * ∏ i, ![c, s] (z i) = ∏ i, ![c, e * s] (z i)
```

**`QuantumMechanics.PBR.norm_prod_phase`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L121).

> The phase product `∏ i, ![1, e] (z i)` has unit norm when `e` does.

```lean
lemma norm_prod_phase {n : ℕ} {e : ℂ} (he : ‖e‖ = 1) (z : Fin n → Fin 2) :
    ‖∏ i, ![1, e] (z i)‖ = 1
```

### B.3. The phases

**`QuantumMechanics.PBR.sum_phases_mul_amp`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L135).

> The phases `ω 0 = -((c + e s)ⁿ - cⁿ) / cⁿ` and `ω z = ∏ i, ![1, e] (z i)` for `z ≠ 0`
> cancel the amplitude products.

```lean
lemma sum_phases_mul_amp {n : ℕ} (c s e : ℂ) (hc : c ^ n ≠ 0) :
    ∑ z : Fin n → Fin 2, (if z = 0 then -(((c + e * s) ^ n - c ^ n) / c ^ n)
      else ∏ i, ![1, e] (z i)) * ∏ i, ![c, s] (z i) = 0
```

**`QuantumMechanics.PBR.exists_phases`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean#L155).

> Unit-modulus phases `ω z` with `∑ z, ω z * ∏ i, ![c, s] (z i) = 0`, for `0 ≤ s ≤ c`,
> `0 < c` and `2 cⁿ ≤ (c + s)ⁿ`.

```lean
lemma exists_phases {c s : ℝ} {n : ℕ} (hc : 0 < c) (hs : 0 ≤ s) (hsc : s ≤ c)
    (hn : 2 * c ^ n ≤ (c + s) ^ n) :
    ∃ ω : (Fin n → Fin 2) → ℂ,
      (∀ z, ‖ω z‖ = 1) ∧ ∑ z, ω z * ∏ i, ![(c : ℂ), (s : ℂ)] (z i) = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Foundations/PBR/Phases.lean)
