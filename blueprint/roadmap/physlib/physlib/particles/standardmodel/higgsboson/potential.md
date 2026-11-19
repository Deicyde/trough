---
declaration: module
origin: cited
lean: StandardModel.HiggsField.Potential.isMinOn_iff_field_of_𝓵_pos, StandardModel.HiggsField.Potential, StandardModel.HiggsField.Potential.toFun, StandardModel.HiggsField.Potential.toFun_smooth, StandardModel.HiggsField.Potential.neg, StandardModel.HiggsField.Potential.toFun_neg, StandardModel.HiggsField.Potential.μ2_neg, StandardModel.HiggsField.Potential.𝓵_neg
statement: formalized
proof: formalized
---

# The potential of the Higgs field

The module `Physlib.Particles.StandardModel.HiggsBoson.Potential`, [Physlib/Particles/StandardModel/HiggsBoson/Potential.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean): 37 declarations, 23 with a docstring, 1 listed as significant; 1 private, not shown.

> The classical Higgs potential, its bounds, and its extrema.

## i. Overview

> The potential depends only on the squared norm of the field at a spacetime point. It is a
> polynomial of degree at most two in that squared norm, and constant fields realize every
> nonnegative squared norm. The bounds and extrema below compare values of the potential at
> points; they do not involve the kinetic term or an energy integral.

## ii. Key results

> - `Potential.toFun_smooth`: the potential evaluated on a Higgs field is smooth.
> - `Potential.isBounded_iff`: the criterion for boundedness below.
> - `Potential.isMinOn_iff_field_of_𝓵_zero`: the minimizing field values at zero quartic coupling.

## iv. References

> * None.

## A. The Higgs potential

**`StandardModel.HiggsField.Potential`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L63).

> The parameters of the classical Higgs potential. With `s` the squared norm of the field
> value, the potential is `-μ2 * s + 𝓵 * s ^ 2`.

```lean
structure Potential where
  /-- The mass parameter of the potential; its negative is the coefficient of the squared norm. -/
  μ2 : ℝ
  /-- The quartic coupling, usually denoted `λ`. -/
  𝓵 : ℝ
```

**`StandardModel.HiggsField.Potential.toFun`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L77).

> Evaluate the classical Higgs potential on the value of the field `φ` at the point `x`.

```lean
def toFun (φ : HiggsField) (x : SpaceTime) : ℝ
```

**`StandardModel.HiggsField.Potential.toFun_smooth`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L88).

> The potential is smooth.

```lean
lemma toFun_smooth (φ : HiggsField) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℝ) ⊤ (fun x => P.toFun φ x)
```

**`StandardModel.HiggsField.Potential.neg`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L95).

> The Higgs potential formed by negating both parameters.

```lean
def neg : Potential
```

**`StandardModel.HiggsField.Potential.toFun_neg`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L100).

```lean
lemma toFun_neg (φ : HiggsField) (x : SpaceTime) : P.neg.toFun φ x = - P.toFun φ x
```

**`StandardModel.HiggsField.Potential.μ2_neg`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L105).

```lean
lemma μ2_neg : P.neg.μ2 = - P.μ2
```

**`StandardModel.HiggsField.Potential.𝓵_neg`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L108).

```lean
lemma 𝓵_neg : P.neg.𝓵 = - P.𝓵
```

## B. Basic properties

**`StandardModel.HiggsField.Potential.toFun_zero`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L117).

```lean
lemma toFun_zero (x : SpaceTime) : P.toFun 0 x = 0
```

**`StandardModel.HiggsField.Potential.toFun_eq_of_repGaugeGroupI`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L122).

> The Higgs potential is gauge invariant: at a spacetime point `x`, it takes the same value on
> two Higgs fields whose values at `x` are related by an element of the gauge group.

```lean
lemma toFun_eq_of_repGaugeGroupI (g : GaugeGroupI) (φ ψ : HiggsField) (x : SpaceTime)
    (h : ψ x = HiggsVec.repGaugeGroupI g (φ x)) : P.toFun ψ x = P.toFun φ x
```

**`StandardModel.HiggsField.Potential.complete_square`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L126).

```lean
lemma complete_square (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x = P.𝓵 * (‖φ‖_H^2 x - P.μ2 / (2 * P.𝓵)) ^ 2 - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.as_quad`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L133).

> The quadratic equation satisfied by the Higgs potential at a spacetime point `x`.

```lean
lemma as_quad (φ : HiggsField) (x : SpaceTime) :
    P.𝓵 * ‖φ‖_H^2 x * ‖φ‖_H^2 x + (- P.μ2) * ‖φ‖_H^2 x + (- P.toFun φ x) = 0
```

**`StandardModel.HiggsField.Potential.toFun_eq_zero_iff`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L140).

> With nonzero quartic coupling, the potential vanishes exactly when the field value is zero
> or has squared norm `P.μ2 / P.𝓵`.

```lean
lemma toFun_eq_zero_iff (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x = 0 ↔ φ x = 0 ∨ ‖φ‖_H^2 x = P.μ2 / P.𝓵
```

## C. The discriminant

**`StandardModel.HiggsField.Potential.quadDiscrim`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L162).

> The discriminant of the quadratic equation formed by the Higgs potential.

```lean
def quadDiscrim (φ : HiggsField) (x : SpaceTime) : ℝ
```

**`StandardModel.HiggsField.Potential.quadDiscrim_nonneg`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L165).

> The discriminant of the quadratic formed by the potential is non-negative.

```lean
lemma quadDiscrim_nonneg (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    0 ≤ P.quadDiscrim φ x
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_sqrt_mul_sqrt`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L173).

```lean
lemma quadDiscrim_eq_sqrt_mul_sqrt (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = Real.sqrt (P.quadDiscrim φ x) * Real.sqrt (P.quadDiscrim φ x)
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_zero_iff`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L177).

```lean
lemma quadDiscrim_eq_zero_iff (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = 0 ↔ P.toFun φ x = - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.quadDiscrim_eq_zero_iff_normSq`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L187).

```lean
lemma quadDiscrim_eq_zero_iff_normSq (h : P.𝓵 ≠ 0) (φ : HiggsField) (x : SpaceTime) :
    P.quadDiscrim φ x = 0 ↔ ‖φ‖_H^2 x = P.μ2 / (2 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.neg_𝓵_quadDiscrim_zero_bound`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L203).

> For an element `P` of `Potential`, if `l < 0` then the following upper bound for the potential
> exists
>
> `P.toFun φ x ≤ - μ2 ^ 2 / (4 * 𝓵)`.

```lean
lemma neg_𝓵_quadDiscrim_zero_bound (h : P.𝓵 < 0) (φ : HiggsField) (x : SpaceTime) :
    P.toFun φ x ≤ - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.pos_𝓵_quadDiscrim_zero_bound`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L214).

> For an element `P` of `Potential`, if `0 < l` then the following lower bound for the potential
> exists
>
> `- μ2 ^ 2 / (4 * 𝓵) ≤ P.toFun φ x`.

```lean
lemma pos_𝓵_quadDiscrim_zero_bound (h : 0 < P.𝓵) (φ : HiggsField) (x : SpaceTime) :
    - P.μ2 ^ 2 / (4 * P.𝓵) ≤ P.toFun φ x
```

**`StandardModel.HiggsField.Potential.neg_𝓵_toFun_neg`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L223).

> If `P.𝓵` is negative, then if `P.μ2` is greater than zero, for all space-time points,
> the potential is negative `P.toFun φ x ≤ 0`.

```lean
lemma neg_𝓵_toFun_neg (h : P.𝓵 < 0) (φ : HiggsField) (x : SpaceTime) :
    (0 < P.μ2 ∧ P.toFun φ x ≤ 0) ∨ P.μ2 ≤ 0
```

**`StandardModel.HiggsField.Potential.pos_𝓵_toFun_pos`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L234).

> If `P.𝓵` is bigger then zero, then if `P.μ2` is less than zero, for all space-time points,
> the potential is positive `0 ≤ P.toFun φ x`.

```lean
lemma pos_𝓵_toFun_pos (h : 0 < P.𝓵) (φ : HiggsField) (x : SpaceTime) :
    (P.μ2 < 0 ∧ 0 ≤ P.toFun φ x) ∨ 0 ≤ P.μ2
```

**`StandardModel.HiggsField.Potential.neg_𝓵_sol_exists_iff`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L246).

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

**`StandardModel.HiggsField.Potential.pos_𝓵_sol_exists_iff`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L289).

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

## D. Boundedness of the potential

**`StandardModel.HiggsField.Potential.IsBounded`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L304).

> The Higgs potential has a uniform lower bound over all field values at spacetime points.

```lean
def IsBounded : Prop
```

**`StandardModel.HiggsField.Potential.isBounded_𝓵_nonneg`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L309).

> Given a element `P` of `Potential` which is bounded,
> the quartic coefficient `𝓵` of `P` is non-negative.

```lean
lemma isBounded_𝓵_nonneg (h : P.IsBounded) : 0 ≤ P.𝓵
```

**`StandardModel.HiggsField.Potential.isBounded_of_𝓵_pos`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L330).

> Given a element `P` of `Potential` with `0 < 𝓵`, then the potential is bounded.

```lean
lemma isBounded_of_𝓵_pos (h : 0 < P.𝓵) : P.IsBounded
```

**`StandardModel.HiggsField.Potential.isBounded_iff_of_𝓵_zero`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L341).

> With zero quartic coupling, the Higgs potential is bounded below exactly when the
> coefficient `-P.μ2` of the squared norm is nonnegative.

```lean
lemma isBounded_iff_of_𝓵_zero (h𝓵 : P.𝓵 = 0) : P.IsBounded ↔ P.μ2 ≤ 0
```

**`StandardModel.HiggsField.Potential.isBounded_iff`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L357).

> The Higgs potential is bounded below exactly when the quartic coupling is positive or is
> zero with a nonnegative coefficient of the squared norm.

```lean
lemma isBounded_iff : P.IsBounded ↔ 0 < P.𝓵 ∨ P.𝓵 = 0 ∧ P.μ2 ≤ 0
```

## E. Minimum and maximum

**`StandardModel.HiggsField.Potential.eq_zero_iff_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L373).

```lean
lemma eq_zero_iff_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : P.toFun φ x = 0 ↔ φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L382).

```lean
lemma isMinOn_iff_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x)
    ↔ P.toFun φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_μSq_nonpos_𝓵_pos`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L400).

```lean
lemma isMinOn_iff_field_of_μSq_nonpos_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : P.μ2 ≤ 0) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x)
    ↔ φ x = 0
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_of_μSq_nonneg_𝓵_pos`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L406).

```lean
lemma isMinOn_iff_of_μSq_nonneg_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : 0 ≤ P.μ2) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    P.toFun φ x = - P.μ2 ^ 2 / (4 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_μSq_nonneg_𝓵_pos`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L423).

```lean
lemma isMinOn_iff_field_of_μSq_nonneg_𝓵_pos (h𝓵 : 0 < P.𝓵) (hμ2 : 0 ≤ P.μ2) (φ : HiggsField)
    (x : SpaceTime) : IsMinOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    ‖φ‖_H^2 x = P.μ2 /(2 * P.𝓵)
```

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_𝓵_pos`**, a theorem, [line 435](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L435). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/scripts/lint/exemptions/Theorems.txt).

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

**`StandardModel.HiggsField.Potential.isMinOn_iff_field_of_𝓵_zero`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L445).

> With zero quartic coupling, every field value minimizes the potential if the coefficient
> of the squared norm is zero. If that coefficient is positive, only the zero field value
> minimizes it. If the coefficient is negative, the potential has no minimum.

```lean
lemma isMinOn_iff_field_of_𝓵_zero (h𝓵 : P.𝓵 = 0) (φ : HiggsField) (x : SpaceTime) :
    IsMinOn (fun (ψ, y) => P.toFun ψ y) Set.univ (φ, x) ↔
      P.μ2 = 0 ∨ (P.μ2 < 0 ∧ φ x = 0)
```

**`StandardModel.HiggsField.Potential.isMaxOn_iff_isMinOn_neg`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L469).

```lean
lemma isMaxOn_iff_isMinOn_neg (φ : HiggsField) (x : SpaceTime) :
    IsMaxOn (fun (φ, x) => P.toFun φ x) Set.univ (φ, x) ↔
    IsMinOn (fun (φ, x) => P.neg.toFun φ x) Set.univ (φ, x)
```

**`StandardModel.HiggsField.Potential.isMaxOn_iff_field_of_𝓵_neg`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean#L482).

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

- [Physlib/Particles/StandardModel/HiggsBoson/Potential.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Particles/StandardModel/HiggsBoson/Potential.lean)
