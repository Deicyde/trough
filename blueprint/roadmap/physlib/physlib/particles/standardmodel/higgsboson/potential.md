---
declaration: module
origin: cited
lean: StandardModel.HiggsField.Potential.isMinOn_iff_field_of_𝓵_pos, StandardModel.HiggsField.Potential, StandardModel.HiggsField.Potential.toFun, StandardModel.HiggsField.Potential.toFun_smooth, StandardModel.HiggsField.Potential.neg, StandardModel.HiggsField.Potential.toFun_neg, StandardModel.HiggsField.Potential.μ2_neg, StandardModel.HiggsField.Potential.𝓵_neg
statement: formalized
proof: formalized
---

# The potential of the Higgs field

The module `Physlib.Particles.StandardModel.HiggsBoson.Potential`, [Physlib/Particles/StandardModel/HiggsBoson/Potential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean): 34 declarations, 20 with a docstring, 1 listed as significant.

> We define the potential of the Higgs field.
>
> We show that the potential is a smooth function on spacetime.

## The Higgs potential

**`StandardModel.HiggsField.Potential`**, a structure, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L41).

> The structure `Potential` is defined with two fields, `μ2` corresponding
> to the mass-squared of the Higgs boson, and `l` corresponding to the coefficient
> of the quartic term in the Higgs potential. Note that `l` is usually denoted `λ`.

```lean
structure Potential where
  /-- The mass-squared of the Higgs boson. -/
  μ2 : ℝ
  /-- The quartic coupling of the Higgs boson. Usually denoted λ. -/
  𝓵 : ℝ
```

**`StandardModel.HiggsField.Potential.toFun`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L58).

> Given a element `P` of `Potential`, `P.toFun` is Higgs potential.
> It is defined for a Higgs field `φ` and a spacetime point `x` as
>
> `-μ² ‖φ‖_H^2 x + l * ‖φ‖_H^2 x * ‖φ‖_H^2 x`.

```lean
def toFun (φ : HiggsField) (x : SpaceTime) : ℝ
```

**`StandardModel.HiggsField.Potential.toFun_smooth`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L62).

> The potential is smooth.

```lean
lemma toFun_smooth (φ : HiggsField) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℝ) ⊤ (fun x => P.toFun φ x)
```

**`StandardModel.HiggsField.Potential.neg`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L69).

> The Higgs potential formed by negating the mass squared and the quartic coupling.

```lean
def neg : Potential
```

**`StandardModel.HiggsField.Potential.toFun_neg`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L74).

```lean
lemma toFun_neg (φ : HiggsField) (x : SpaceTime) : P.neg.toFun φ x = - P.toFun φ x
```

**`StandardModel.HiggsField.Potential.μ2_neg`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L79).

```lean
lemma μ2_neg : P.neg.μ2 = - P.μ2
```

**`StandardModel.HiggsField.Potential.𝓵_neg`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L82).

```lean
lemma 𝓵_neg : P.neg.𝓵 = - P.𝓵
```

## Basic properties

**`StandardModel.HiggsField.Potential.toFun_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L91).

```lean
lemma toFun_zero (x : SpaceTime) : P.toFun 0 x = 0
```

**`StandardModel.HiggsField.Potential.toFun_eq_of_repGaugeGroupI`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L96).

> The Higgs potential is gauge invariant: at a spacetime point `x`, it takes the same value on
> two Higgs fields whose values at `x` are related by an element of the gauge group.

```lean
lemma toFun_eq_of_repGaugeGroupI (g : GaugeGroupI) (φ ψ : HiggsField) (x : SpaceTime)
    (h : ψ x = HiggsVec.repGaugeGroupI g (φ x)) : P.toFun ψ x = P.toFun φ x
```

**`StandardModel.HiggsField.Potential.complete_square`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L100).

```lean
lemma complete_square (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x = P.𝓵 * (‖φ‖_H^2 x - P.μ2 / (2 * P.𝓵)) ^ 2 - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.as_quad`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L107).

> The quadratic equation satisfied by the Higgs potential at a spacetime point `x`.

```lean
lemma as_quad (φ : HiggsField) (x : SpaceTime) :
    P.𝓵 * ‖φ‖_H^2 x * ‖φ‖_H^2 x + (- P.μ2) * ‖φ‖_H^2 x + (- P.toFun φ x) = 0
```

**`StandardModel.HiggsField.Potential.toFun_eq_zero_iff`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L114).

> The Higgs potential is zero iff and only if the higgs field is zero, or the
> higgs field has norm-squared `P.μ2 / P.𝓵`, assuming `P.𝓁 = 0`.

```lean
lemma toFun_eq_zero_iff (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x = 0 ↔ φ x = 0 ∨ ‖φ‖_H^2 x = P.μ2 / P.𝓵
```

## The discriminant

**`StandardModel.HiggsField.Potential.quadDiscrim`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L136).

> The discriminant of the quadratic equation formed by the Higgs potential.

```lean
def quadDiscrim (φ : HiggsField) (x : SpaceTime) : ℝ
```

**`StandardModel.HiggsField.Potential.quadDiscrim_nonneg`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L139).

> The discriminant of the quadratic formed by the potential is non-negative.

```lean
lemma quadDiscrim_nonneg (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    0 ≤ P.quadDiscrim φ x
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_sqrt_mul_sqrt`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L147).

```lean
lemma quadDiscrim_eq_sqrt_mul_sqrt (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = Real.sqrt (P.quadDiscrim φ x) * Real.sqrt (P.quadDiscrim φ x)
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_zero_iff`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L151).

```lean
lemma quadDiscrim_eq_zero_iff (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = 0 ↔ P.toFun φ x = - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_zero_iff_normSq`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L161).

```lean
lemma quadDiscrim_eq_zero_iff_normSq (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = 0 ↔ ‖φ‖_H^2 x = P.μ2 / (2 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.neg_𝓵_quadDiscrim_zero_bound`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L177).

> For an element `P` of `Potential`, if `l < 0` then the following upper bound for the potential
> exists
>
> `P.toFun φ x ≤ - μ2 ^ 2 / (4 * 𝓵)`.

```lean
lemma neg_𝓵_quadDiscrim_zero_bound (h : P.𝓵 < 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x ≤ - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.pos_𝓵_quadDiscrim_zero_bound`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L188).

> For an element `P` of `Potential`, if `0 < l` then the following lower bound for the potential
> exists
>
> `- μ2 ^ 2 / (4 * 𝓵) ≤ P.toFun φ x`.

```lean
lemma pos_𝓵_quadDiscrim_zero_bound (h : 0 < P.𝓵) (φ : HiggsField) (x : SpaceTime) :
    - P.μ2 ^ 2 / (4 * P.𝓵) ≤ P.toFun φ x
```

**`StandardModel.HiggsField.Potential.neg_𝓵_toFun_neg`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L197).

> If `P.𝓵` is negative, then if `P.μ2` is greater than zero, for all space-time points,
> the potential is negative `P.toFun φ x ≤ 0`.

```lean
lemma neg_𝓵_toFun_neg (h : P.𝓵 < 0) (φ : HiggsField) (x : SpaceTime) :
    (0 < P.μ2 ∧ P.toFun φ x ≤ 0) ∨ P.μ2 ≤ 0
```

**`StandardModel.HiggsField.Potential.pos_𝓵_toFun_pos`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L208).

> If `P.𝓵` is bigger then zero, then if `P.μ2` is less than zero, for all space-time points,
> the potential is positive `0 ≤ P.toFun φ x`.

```lean
lemma pos_𝓵_toFun_pos (h : 0 < P.𝓵) (φ : HiggsField) (x : SpaceTime) :
    (P.μ2 < 0 ∧ 0 ≤ P.toFun φ x) ∨ 0 ≤ P.μ2
```

**`StandardModel.HiggsField.Potential.neg_𝓵_sol_exists_iff`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L220).

> For an element `P` of `Potential` with `l < 0` and a real `c : ℝ`, there exists
>   a Higgs field `φ` and a spacetime point `x` such that `P.toFun φ x = c` iff one of the
>   following two conditions hold:
> - `0 < μ2` and `c ≤ 0`. That is, if `l` is negative and `μ2` positive, then the potential
>   takes every non-positive value.
> - or `μ2 ≤ 0` and `c ≤ - μ2 ^ 2 / (4 * 𝓵)`. That is, if `l` is negative and `μ2` non-positive,
>   then the potential takes every value less then or equal to its bound.

```lean
lemma neg_𝓵_sol_exists_iff (h𝓵 : P.𝓵 < 0) (c : ℝ) : (∃ φ x, P.toFun φ x = c) ↔ (0 < P.μ2 ∧ c ≤ 0) ∨
    (P.μ2 ≤ 0 ∧ c ≤ - P.μ2 ^ 2 / (4 * P.𝓵))
```

**`StandardModel.HiggsField.Potential.pos_𝓵_sol_exists_iff`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L263).

> For an element `P` of `Potential` with `0 < l` and a real `c : ℝ`, there exists
>   a Higgs field `φ` and a spacetime point `x` such that `P.toFun φ x = c` iff one of the
>   following two conditions hold:
> - `μ2 < 0` and `0 ≤ c`. That is, if `l` is positive and `μ2` negative, then the potential
>   takes every non-negative value.
> - or `0 ≤ μ2` and `- μ2 ^ 2 / (4 * 𝓵) ≤ c`. That is, if `l` is positive and `μ2` non-negative,
>   then the potential takes every value greater then or equal to its bound.

```lean
lemma pos_𝓵_sol_exists_iff (h𝓵 : 0 < P.𝓵) (c : ℝ) : (∃ φ x, P.toFun φ x = c) ↔ (P.μ2 < 0 ∧ 0 ≤ c) ∨
    (0 ≤ P.μ2 ∧ - P.μ2 ^ 2 / (4 * P.𝓵) ≤ c)
```

## Boundedness of the potential

**`StandardModel.HiggsField.Potential.IsBounded`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L282).

> Given a element `P` of `Potential`, the proposition `IsBounded P` is true if and only if
> there exists a real `c` such that for all Higgs fields `φ` and spacetime points `x`,
> the Higgs potential corresponding to `φ` at `x` is greater then or equal to`c`. I.e.
>
> `∀ Φ x, c ≤ P.toFun Φ x`.

```lean
def IsBounded : Prop
```

**`StandardModel.HiggsField.Potential.isBounded_𝓵_nonneg`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L287).

> Given a element `P` of `Potential` which is bounded,
> the quartic coefficient `𝓵` of `P` is non-negative.

```lean
lemma isBounded_𝓵_nonneg (h : P.IsBounded) : 0 ≤ P.𝓵
```

**`StandardModel.HiggsField.Potential.isBounded_of_𝓵_pos`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L308).

> Given a element `P` of `Potential` with `0 < 𝓵`, then the potential is bounded.

```lean
lemma isBounded_of_𝓵_pos (h : 0 < P.𝓵) : P.IsBounded
```

## Minimum and maximum

**`StandardModel.HiggsField.Potential.eq_zero_iff_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L330).

```lean
lemma eq_zero_iff_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : P.toFun φ x = 0 ↔ φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L339).

```lean
lemma isMinOn_iff_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x)
    ↔ P.toFun φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L357).

```lean
lemma isMinOn_iff_field_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x)
    ↔ φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_of_μSq_nonneg_𝓵_pos`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L363).

```lean
lemma isMinOn_iff_of_μSq_nonneg_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : 0 ≤ P.μ2) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    P.toFun φ x = - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_μSq_nonneg_𝓵_pos`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L380).

```lean
lemma isMinOn_iff_field_of_μSq_nonneg_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : 0 ≤ P.μ2) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    ‖φ‖_H^2 x = P.μ2 /(2 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_𝓵_pos`**, a theorem, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L392). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Given an element `P` of `Potential` with `0 < l`, then the Higgs field `φ` and
>   spacetime point `x` minimize the potential if and only if one of the following conditions
>   holds
> - `0 ≤ μ2` and `‖φ‖_H^2 x = μ2 / (2 * 𝓵)`.
> - or `μ2 < 0` and `φ x = 0`.

```lean
theorem isMinOn_iff_field_of_𝓵_pos (h𝓵 : 0 < P.𝓵) (φ : HiggsField) (x : SpaceTime) :
    IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    (0 ≤ P.μ2 ∧ ‖φ‖_H^2 x = P.μ2 /(2 * P.𝓵)) ∨ (P.μ2 < 0 ∧ φ x = 0)
```

**`StandardModel.HiggsField.Potential.isMaxOn_iff_isMinOn_neg`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L399).

```lean
lemma isMaxOn_iff_isMinOn_neg (φ : HiggsField) (x : SpaceTime) :
    IsMaxOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    IsMinOn (fun (φ, x) => P.neg.toFun φ x) Set.univ (φ, x)
```

**`StandardModel.HiggsField.Potential.isMaxOn_iff_field_of_𝓵_neg`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L412).

> Given an element `P` of `Potential` with `l < 0`, then the Higgs field `φ` and
>   spacetime point `x` maximizes the potential if and only if one of the following conditions
>   holds
> - `μ2 ≤ 0` and `‖φ‖_H^2 x = μ2 / (2 * 𝓵)`.
> - or `0 < μ2` and `φ x = 0`.

```lean
lemma isMaxOn_iff_field_of_𝓵_neg (h𝓵 : P.𝓵 < 0) (φ : HiggsField) (x : SpaceTime) :
    IsMaxOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    (P.μ2 ≤ 0 ∧ ‖φ‖_H^2 x = P.μ2 /(2 * P.𝓵)) ∨ (0 < P.μ2 ∧ φ x = 0)
```

## Depends on

- [The Higgs field](basic.md)

## Sources

- [Physlib/Particles/StandardModel/HiggsBoson/Potential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean)
