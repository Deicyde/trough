---
declaration: module
origin: cited
lean: Constants.ℏ, Constants.ℏ_pos, Constants.ℏ_nonneg, Constants.ℏ_ne_zero, Constants.ℏ_ofReal_ne_zero, Constants.h, Constants.h_pos, Constants.h_nonneg
statement: formalized
proof: formalized
---

# Planck's constant

The module `Physlib.QuantumMechanics.PlanckConstant`, [Physlib/QuantumMechanics/PlanckConstant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean): 10 declarations, 10 with a docstring.

> In this module we define the reduced Planck's constant `ℏ` as a positive real number.
> and also define the Planck's constant `h` also to be a positive real number with the
> definition `h = 2 π ℏ`.

**`Constants.ℏ`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L26).

> The value of the reduced Planck's constant in units of J.s.

```lean
def ℏ : Subtype fun x : ℝ => 0 < x
```

**`Constants.ℏ_pos`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L30).

> reduced Planck's constant is positive.

```lean
lemma ℏ_pos : 0 < (ℏ : ℝ)
```

**`Constants.ℏ_nonneg`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L34).

> reduced Planck's constant is non-negative.

```lean
lemma ℏ_nonneg : 0 ≤ (ℏ : ℝ)
```

**`Constants.ℏ_ne_zero`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L38).

> reduced Planck's constant is not equal to zero.

```lean
lemma ℏ_ne_zero : (ℏ : ℝ) ≠ 0
```

**`Constants.ℏ_ofReal_ne_zero`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L41).

> reduced Planck's constant is not equal to zero, as a complex number.

```lean
lemma ℏ_ofReal_ne_zero : ((ℏ : ℝ) : ℂ) ≠ 0
```

**`Constants.h`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L45).

> The definition of Planck's constant in terms of Reduced Planck's constant,
> defined as `2 π ℏ`

```lean
noncomputable def h : Subtype fun x : ℝ => 0 < x
```

**`Constants.h_pos`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L50).

> Planck's constant is positive.

```lean
lemma h_pos : 0 < (h : ℝ)
```

**`Constants.h_nonneg`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L54).

> Planck's constant is non-negative.

```lean
lemma h_nonneg : 0 ≤ (h : ℝ)
```

**`Constants.h_ne_zero`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L58).

> Planck's constnat is not equal to zero.

```lean
lemma h_ne_zero : (h : ℝ) ≠ 0
```

**`Constants.h_eq_two_pi_hbar`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean#L61).

> Planck's constant is `2 π` times the reduced Planck's constant.

```lean
lemma h_eq_two_pi_hbar : (h : ℝ) = 2 * Real.pi * (ℏ : ℝ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/PlanckConstant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PlanckConstant.lean)
