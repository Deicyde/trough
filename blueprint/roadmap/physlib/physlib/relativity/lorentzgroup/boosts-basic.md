---
declaration: module
origin: cited
lean: LorentzGroup.γ, LorentzGroup.γ_tanh, LorentzGroup.γ_sq, LorentzGroup.γ_zero, LorentzGroup.γ_neg, LorentzGroup.γ_det_not_zero, LorentzGroup.boost, LorentzGroup.boost_transpose_eq_self
statement: formalized
proof: formalized
---

# Boosts in the Lorentz group

The module `Physlib.Relativity.LorentzGroup.Boosts.Basic`, [Physlib/Relativity/LorentzGroup/Boosts/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean): 30 declarations, 3 with a docstring.

> Lorentz factors, finite coordinate boosts and their matrix entries.

## i. Overview

> The Lorentz factor `γ β` determines a boost at speed `β`, with `|β| < 1`.
> Parametrizing the speed by rapidity gives `γ (Real.tanh r) = Real.cosh r`.
> The Minkowski signature has one positive time coordinate and negative spatial coordinates.
> The time-space entries of a boost are `-γ β * β`.

## ii. Key results

> - `γ_tanh`: the Lorentz factor expressed in terms of rapidity.
> - `boost`: a Lorentz boost along one spatial coordinate.
> - `boost_transpose_eq_self` and `boost_inverse`: transpose and inverse identities.
> - `boost_inl_0_inr_self`: the active time-space matrix entry of a boost.

## iv. References

> The rapidity identity uses the hyperbolic-function identities in
> `Mathlib.Analysis.SpecialFunctions.Artanh`.

## A. The Lorentz factor

**`LorentzGroup.γ`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L57).

> The Lorentz factor (aka gamma factor or Lorentz term).

```lean
def γ (β : ℝ) : ℝ
```

**`LorentzGroup.γ_tanh`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L60).

> The Lorentz factor expressed in terms of rapidity.

```lean
lemma γ_tanh (r : ℝ) : γ (Real.tanh r) = Real.cosh r
```

**`LorentzGroup.γ_sq`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L64).

```lean
lemma γ_sq (β : ℝ) (hβ : |β| < 1) : (γ β)^2 = 1 / (1 - β^2)
```

**`LorentzGroup.γ_zero`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L71).

```lean
lemma γ_zero : γ 0 = 1
```

**`LorentzGroup.γ_neg`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L74).

```lean
lemma γ_neg (β : ℝ) : γ (-β) = γ β
```

**`LorentzGroup.γ_det_not_zero`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L77).

```lean
lemma γ_det_not_zero (β : ℝ) (hβ : |β| < 1) : (1 - β^2) ≠ 0
```

## B. Lorentz boosts

**`LorentzGroup.boost`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L89).

> The Lorentz boost with in the space direction `i` with speed `β` with
> `|β| < 1`.

```lean
def boost (i : Fin d) (β : ℝ) (hβ : |β| < 1) : LorentzGroup d
```

**`LorentzGroup.boost_transpose_eq_self`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L186).

```lean
lemma boost_transpose_eq_self (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    transpose (boost i β hβ) = boost i β hβ
```

**`LorentzGroup.boost_transpose_matrix_eq_self`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L201).

```lean
lemma boost_transpose_matrix_eq_self (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    Matrix.transpose (boost i β hβ).1 = (boost i β hβ).1
```

**`LorentzGroup.boost_zero_eq_id`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L206).

```lean
lemma boost_zero_eq_id (i : Fin d) : boost i 0 (by simp) = 1
```

**`LorentzGroup.boost_inverse`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L223).

```lean
lemma boost_inverse (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    (boost i β hβ)⁻¹ = boost i (-β) (by simpa using hβ)
```

**`LorentzGroup.boost_inl_0_inl_0`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L250).

```lean
lemma boost_inl_0_inl_0 (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    (boost i β hβ).1 (Sum.inl 0) (Sum.inl 0) = γ β
```

**`LorentzGroup.boost_inr_self_inr_self`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L255).

```lean
lemma boost_inr_self_inr_self (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    (boost i β hβ).1 (Sum.inr i) (Sum.inr i) = γ β
```

**`LorentzGroup.boost_inl_0_inr_self`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L260).

```lean
lemma boost_inl_0_inr_self (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    (boost i β hβ).1 (Sum.inl 0) (Sum.inr i) = - γ β * β
```

**`LorentzGroup.boost_inr_self_inl_0`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L265).

```lean
lemma boost_inr_self_inl_0 (i : Fin d) {β : ℝ} (hβ : |β| < 1) :
    (boost i β hβ).1 (Sum.inr i) (Sum.inl 0) = - γ β * β
```

**`LorentzGroup.boost_inl_0_inr_other`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L269).

```lean
lemma boost_inl_0_inr_other {i j : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inl 0) (Sum.inr j) = 0
```

**`LorentzGroup.boost_inr_other_inl_0`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L273).

```lean
lemma boost_inr_other_inl_0 {i j : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inr j) (Sum.inl 0) = 0
```

**`LorentzGroup.boost_inr_self_inr_other`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L277).

```lean
lemma boost_inr_self_inr_other {i j : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inr i) (Sum.inr j) = 0
```

**`LorentzGroup.boost_inr_other_inr_self`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L281).

```lean
lemma boost_inr_other_inr_self {i j : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inr j) (Sum.inr i) = 0
```

**`LorentzGroup.boost_inr_other_inr`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L285).

```lean
lemma boost_inr_other_inr {i j k : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inr j) (Sum.inr k) = if j = k then 1 else 0
```

**`LorentzGroup.boost_inr_inr_other`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L289).

```lean
lemma boost_inr_inr_other {i j k : Fin d} {β : ℝ} (hβ : |β| < 1) (hij : j ≠ i) :
    (boost i β hβ).1 (Sum.inr k) (Sum.inr j) = if j = k then 1 else 0
```

## C. Boosts in the zero-direction

**`LorentzGroup.boost_zero_inl_0_inr_succ`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L302).

```lean
lemma boost_zero_inl_0_inr_succ {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : Fin d) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inl 0) (Sum.inr i.succ) = 0
```

**`LorentzGroup.boost_zero_inr_succ_inl_0`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L307).

```lean
lemma boost_zero_inr_succ_inl_0{d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : Fin d) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr i.succ) (Sum.inl 0) = 0
```

**`LorentzGroup.boost_zero_inl_0_inr_nat_succ`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L312).

```lean
lemma boost_zero_inl_0_inr_nat_succ {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : ℕ) (h : i + 1 < d + 1) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inl 0) (Sum.inr ⟨i + 1, h⟩) = 0
```

**`LorentzGroup.boost_zero_inr_nat_succ_inl_0`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L317).

```lean
lemma boost_zero_inr_nat_succ_inl_0 {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : ℕ) (h : i + 1 < d + 1) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr ⟨i + 1, h⟩) (Sum.inl 0) = 0
```

**`LorentzGroup.boost_zero_inr_0_inr_succ`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L322).

```lean
lemma boost_zero_inr_0_inr_succ {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : Fin d) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr 0) (Sum.inr i.succ) = 0
```

**`LorentzGroup.boost_zero_inr_succ_inr_0`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L327).

```lean
lemma boost_zero_inr_succ_inr_0 {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : Fin d) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr i.succ) (Sum.inr 0) = 0
```

**`LorentzGroup.boost_zero_inr_0_inr_nat_succ`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L332).

```lean
lemma boost_zero_inr_0_inr_nat_succ {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : ℕ) (h : i + 1 < d + 1) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr 0) (Sum.inr ⟨i + 1, h⟩) = 0
```

**`LorentzGroup.boost_zero_inr_nat_succ_inr_0`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L337).

```lean
lemma boost_zero_inr_nat_succ_inr_0 {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i : ℕ) (h : i + 1 < d + 1) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr ⟨i + 1, h⟩) (Sum.inr 0) = 0
```

**`LorentzGroup.boost_zero_inr_succ_inr_succ`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean#L341).

```lean
lemma boost_zero_inr_succ_inr_succ {d : ℕ} {β : ℝ} (hβ : |β| < 1) (i1 i2 : Fin d) :
    (boost (0 : Fin d.succ) β hβ).1 (Sum.inr i1.succ) (Sum.inr i2.succ) =
    if i1 = i2 then 1 else 0
```

## Depends on

- [The Lorentz Group](basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Boosts/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Basic.lean)
