---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.wicks_theorem_normal_order, FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_eqTimeOnly, FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_eq_eqTimeOnly_empty, FieldSpecification.WickAlgebra.normalOrder_timeOrder_ofFieldOpList_eq_eqTimeOnly_empty, FieldSpecification.WickAlgebra.timeOrder_haveEqTime_split, FieldSpecification.WickAlgebra.normalOrder_timeOrder_ofFieldOpList_eq_not_haveEqTime_sub_inductive, FieldSpecification.WickAlgebra.wicks_theorem_normal_order_empty
statement: formalized
proof: formalized
---

# Wick's theorem for normal ordered lists

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.WicksTheoremNormal`, [Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean): 7 declarations, 4 with a docstring, 1 listed as significant.

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_eqTimeOnly`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L46).

> For a list `φs` of `𝓕.FieldOp`, then
>
> `𝓣(φs) = ∑ φsΛ, φsΛ.sign • φsΛ.timeContract * 𝓣(𝓝([φsΛ]ᵘᶜ))`
>
> where the sum is over all Wick contraction `φsΛ` which only have equal time contractions.
>
> This result follows from
> - `static_wick_theorem` to rewrite `𝓣(φs)` on the left hand side as a sum of
>   `𝓣(φsΛ.staticWickTerm)`.
> - `EqTimeOnly.timeOrder_staticContract_of_not_mem` and `timeOrder_timeOrder_mid` to set to
>   those `𝓣(φsΛ.staticWickTerm)` for which `φsΛ` has a contracted pair which are not
>   equal time to zero.
> - `staticContract_eq_timeContract_of_eqTimeOnly` to rewrite the static contract
>   in the remaining `𝓣(φsΛ.staticWickTerm)` as a time contract.
> - `timeOrder_timeContract_mul_of_eqTimeOnly_left` to move the time contracts out of the time
>   ordering.

```lean
lemma timeOrder_ofFieldOpList_eqTimeOnly (φs : List 𝓕.FieldOp) :
    𝓣(ofFieldOpList φs) = ∑ (φsΛ : {φsΛ // φsΛ.EqTimeOnly (φs := φs)}),
    φsΛ.1.sign • φsΛ.1.timeContract.1 * 𝓣(𝓝(ofFieldOpList [φsΛ.1]ᵘᶜ))
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_eq_eqTimeOnly_empty`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L68).

```lean
lemma timeOrder_ofFieldOpList_eq_eqTimeOnly_empty (φs : List 𝓕.FieldOp) :
    𝓣(ofFieldOpList φs) = 𝓣(𝓝(ofFieldOpList φs)) +
    ∑ (φsΛ : {φsΛ // φsΛ.EqTimeOnly (φs := φs) ∧ φsΛ ≠ empty}),
    φsΛ.1.sign • φsΛ.1.timeContract.1 * 𝓣(𝓝(ofFieldOpList [φsΛ.1]ᵘᶜ))
```

**`FieldSpecification.WickAlgebra.normalOrder_timeOrder_ofFieldOpList_eq_eqTimeOnly_empty`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L103).

> For a list `φs` of `𝓕.FieldOp`, then
>
> `𝓣(𝓝(φs)) = 𝓣(φs) - ∑ φsΛ, φsΛ.sign • φsΛ.timeContract.1 * 𝓣(𝓝([φsΛ]ᵘᶜ))`
>
> where the sum is over all *non-empty* Wick contraction `φsΛ` which only
>   have equal time contractions.
>
> This result follows directly from
> - `timeOrder_ofFieldOpList_eqTimeOnly`

```lean
lemma normalOrder_timeOrder_ofFieldOpList_eq_eqTimeOnly_empty (φs : List 𝓕.FieldOp) :
    𝓣(𝓝(ofFieldOpList φs)) = 𝓣(ofFieldOpList φs) -
    ∑ (φsΛ : {φsΛ // φsΛ.EqTimeOnly (φs := φs) ∧ φsΛ ≠ empty}),
    φsΛ.1.sign • φsΛ.1.timeContract.1 * 𝓣(𝓝(ofFieldOpList [φsΛ.1]ᵘᶜ))
```

**`FieldSpecification.WickAlgebra.timeOrder_haveEqTime_split`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L129).

> For a list `φs` of `𝓕.FieldOp`, then `𝓣(φs)` is equal to the sum of
>
> - `∑ φsΛ, φsΛ.wickTerm` where the sum is over all Wick contraction `φsΛ` which have
>   no contractions of equal time.
> - `∑ φsΛ, φsΛ.sign • φsΛ.timeContract * (∑ φssucΛ, φssucΛ.wickTerm)`, where
>   the first sum is over all Wick contraction `φsΛ` which only have equal time contractions
>   and the second sum is over all Wick contraction `φssucΛ` of the uncontracted elements of `φsΛ`
>   which do not have any equal time contractions.
>
> The proof proceeds as follows
> - `wicks_theorem` is used to rewrite `𝓣(φs)` as a sum over all Wick contractions.
> - The sum over all Wick contractions is then split additively into two parts based on having
>   or not having an equal time contractions.
> - Using `join`, the sum `∑ φsΛ, _` over Wick contractions which do have equal time contractions
>   is split into two sums `∑ φsΛ, ∑ φsucΛ, _`, the first over non-zero elements
>   which only have equal time contractions and the second over Wick contractions `φsucΛ` of
>   `[φsΛ]ᵘᶜ` which do not have equal time contractions.
> - `join_sign_timeContract` is then used to equate terms.

```lean
lemma timeOrder_haveEqTime_split (φs : List 𝓕.FieldOp) :
    𝓣(ofFieldOpList φs) = (∑ (φsΛ : {φsΛ : WickContraction φs.length // ¬ HaveEqTime φsΛ}),
    φsΛ.1.sign • φsΛ.1.timeContract.1 * 𝓝(ofFieldOpList [φsΛ.1]ᵘᶜ))
    + ∑ (φsΛ : {φsΛ // φsΛ.EqTimeOnly (φs := φs) ∧ φsΛ ≠ empty}), φsΛ.1.sign • φsΛ.1.timeContract *
    (∑ φssucΛ : { φssucΛ : WickContraction [φsΛ.1]ᵘᶜ.length // ¬ φssucΛ.HaveEqTime },
      φssucΛ.1.wickTerm)
```

**`FieldSpecification.WickAlgebra.normalOrder_timeOrder_ofFieldOpList_eq_not_haveEqTime_sub_inductive`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L161).

```lean
lemma normalOrder_timeOrder_ofFieldOpList_eq_not_haveEqTime_sub_inductive (φs : List 𝓕.FieldOp) :
    𝓣(𝓝(ofFieldOpList φs)) =
      (∑ (φsΛ : {φsΛ : WickContraction φs.length // ¬ HaveEqTime φsΛ}), φsΛ.1.wickTerm)
      + ∑ (φsΛ : {φsΛ // φsΛ.EqTimeOnly (φs := φs) ∧ φsΛ ≠ empty}),
        sign φs ↑φsΛ • (φsΛ.1).timeContract *
        (∑ φssucΛ : { φssucΛ : WickContraction [φsΛ.1]ᵘᶜ.length // ¬ φssucΛ.HaveEqTime },
        φssucΛ.1.wickTerm - 𝓣(𝓝(ofFieldOpList [φsΛ.1]ᵘᶜ)))
```

**`FieldSpecification.WickAlgebra.wicks_theorem_normal_order_empty`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L173).

```lean
lemma wicks_theorem_normal_order_empty : 𝓣(𝓝(ofFieldOpList [])) =
    ∑ (φsΛ : {φsΛ : WickContraction ([] : List 𝓕.FieldOp).length // ¬ HaveEqTime φsΛ}),
    φsΛ.1.wickTerm
```

**`FieldSpecification.WickAlgebra.wicks_theorem_normal_order`**, a theorem, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean#L213). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a list `φs` of `𝓕.FieldOp`, the normal-ordered version of Wick's theorem states that
>
> `𝓣(𝓝(φs)) = ∑ φsΛ, φsΛ.wickTerm`
>
> where the sum is over all Wick contraction `φsΛ` in which no two contracted elements
> have the same time.
>
> The proof proceeds by induction on `φs`, with the base case `[]` holding by following
> through definitions. and the inductive case holding as a result of
> - `timeOrder_haveEqTime_split`
> - `normalOrder_timeOrder_ofFieldOpList_eq_eqTimeOnly_empty`
> - and the induction hypothesis on `𝓣(𝓝([φsΛ.1]ᵘᶜ))` for contractions `φsΛ` of `φs` which only
>   have equal time contractions and are non-empty.

```lean
theorem wicks_theorem_normal_order : (φs : List 𝓕.FieldOp) →
    𝓣(𝓝(ofFieldOpList φs)) =
    ∑ (φsΛ : {φsΛ : WickContraction φs.length // ¬ HaveEqTime φsΛ}), φsΛ.1.wickTerm
```

## Depends on

- [Wick term](wickalgebra-wickterm.md)
- [Time contractions](../part-03/wickcontraction-timecond.md)

## Proof depends on

- [Static Wick's theorem](wickalgebra-staticwicktheorem.md)
- [Wick's theorem](wickalgebra-wickstheorem.md)
- [Sign associated with joining two Wick contractions](../part-03/wickcontraction-sign-join.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheoremNormal.lean)
