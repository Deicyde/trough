---
declaration: module
origin: cited
lean: FieldSpecification.timeOrderRel, FieldSpecification.maxTimeFieldPos, FieldSpecification.maxTimeFieldPos_lt_length, FieldSpecification.maxTimeField, FieldSpecification.eraseMaxTimeField, FieldSpecification.eraseMaxTimeField_length, FieldSpecification.maxTimeFieldPos_lt_eraseMaxTimeField_length_succ, FieldSpecification.maxTimeFieldPosFin
statement: formalized
proof: formalized
---

# Time ordering of states

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.TimeOrder`, [Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean): 55 declarations (9 instances with no name), 23 with a docstring.

## Time ordering for states

**`FieldSpecification.timeOrderRel`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L31).

> The time ordering relation on states. We have that `timeOrderRel φ0 φ1` is true
> if and only if `φ1` has a time less-then or equal to `φ0`, or `φ1` is a negative
> asymptotic state, or `φ0` is a positive asymptotic state.

```lean
def timeOrderRel : 𝓕.FieldOp → 𝓕.FieldOp → Prop
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L42).

> The relation `timeOrderRel` is decidable, but not computable so due to
> `Real.decidableLE`.

```lean
noncomputable instance : (φ φ' : 𝓕.FieldOp) → Decidable (timeOrderRel φ φ')
```

**An instance with no name**, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L53).

> Time ordering is total.

```lean
instance : Std.Total 𝓕.timeOrderRel
```

**An instance with no name**, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L58).

> Time ordering is transitive.

```lean
instance : IsTrans 𝓕.FieldOp 𝓕.timeOrderRel
```

**`FieldSpecification.maxTimeFieldPos`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L73).

> Given a list `φ :: φs` of states, the (zero-based) position of the state which is
> of maximum time. For example
> - for the list `[φ1(t = 4), φ2(t = 5), φ3(t = 3), φ4(t = 5)]` this would return `1`.
> This is defined for a list `φ :: φs` instead of `φs` to ensure that such a position exists.

```lean
def maxTimeFieldPos (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) : ℕ
```

**`FieldSpecification.maxTimeFieldPos_lt_length`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L76).

```lean
lemma maxTimeFieldPos_lt_length (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    maxTimeFieldPos φ φs < (φ :: φs).length
```

**`FieldSpecification.maxTimeField`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L85).

> Given a list `φ :: φs` of states, the left-most state of maximum time, if there are more.
> As an example:
> - for the list `[φ1(t = 4), φ2(t = 5), φ3(t = 3), φ4(t = 5)]` this would return `φ2(t = 5)`.
> It is the state at the position `maxTimeFieldPos φ φs`.

```lean
def maxTimeField (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) : 𝓕.FieldOp
```

**`FieldSpecification.eraseMaxTimeField`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L94).

> Given a list `φ :: φs` of states, the list with the left-most state of maximum
> time removed.
> As an example:
> - for the list `[φ1(t = 4), φ2(t = 5), φ3(t = 3), φ4(t = 5)]` this would return
>   `[φ1(t = 4), φ3(t = 3), φ4(t = 5)]`.

```lean
def eraseMaxTimeField (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) : List 𝓕.FieldOp
```

**`FieldSpecification.eraseMaxTimeField_length`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L98).

```lean
lemma eraseMaxTimeField_length (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    (eraseMaxTimeField φ φs).length = φs.length
```

**`FieldSpecification.maxTimeFieldPos_lt_eraseMaxTimeField_length_succ`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L102).

```lean
lemma maxTimeFieldPos_lt_eraseMaxTimeField_length_succ (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    maxTimeFieldPos φ φs < (eraseMaxTimeField φ φs).length.succ
```

**`FieldSpecification.maxTimeFieldPosFin`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L111).

> Given a list `φ :: φs` of states, the position of the left-most state of maximum
> time as an element of `Fin (eraseMaxTimeField φ φs).length.succ`.
> As an example:
> - for the list `[φ1(t = 4), φ2(t = 5), φ3(t = 3), φ4(t = 5)]` this would return `⟨1,...⟩`.

```lean
def maxTimeFieldPosFin (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    Fin (eraseMaxTimeField φ φs).length.succ
```

**`FieldSpecification.lt_maxTimeFieldPosFin_not_timeOrder`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L115).

```lean
lemma lt_maxTimeFieldPosFin_not_timeOrder (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin (eraseMaxTimeField φ φs).length)
    (hi : (maxTimeFieldPosFin φ φs).succAbove i < maxTimeFieldPosFin φ φs) :
    ¬ timeOrderRel ((eraseMaxTimeField φ φs)[i.val]) (maxTimeField φ φs)
```

**`FieldSpecification.timeOrder_maxTimeField`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L121).

```lean
lemma timeOrder_maxTimeField (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin (eraseMaxTimeField φ φs).length) :
    timeOrderRel (maxTimeField φ φs) ((eraseMaxTimeField φ φs)[i.val])
```

**`FieldSpecification.timeOrderSign`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L129).

> The sign associated with putting a list of states into time order (with
> the state of greatest time to the left).
> We pick up a minus sign for every fermion paired crossed.

```lean
def timeOrderSign (φs : List 𝓕.FieldOp) : ℂ
```

**`FieldSpecification.timeOrderSign_nil`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L133).

```lean
lemma timeOrderSign_nil : timeOrderSign (𝓕 := 𝓕) [] = 1
```

**`FieldSpecification.timeOrderSign_pair_ordered`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L136).

```lean
lemma timeOrderSign_pair_ordered {φ ψ : 𝓕.FieldOp} (h : timeOrderRel φ ψ) :
    timeOrderSign [φ, ψ] = 1
```

**`FieldSpecification.timeOrderSign_pair_not_ordered`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L140).

```lean
lemma timeOrderSign_pair_not_ordered {φ ψ : 𝓕.FieldOp} (h : ¬ timeOrderRel φ ψ) :
    timeOrderSign [φ, ψ] = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ)
```

**`FieldSpecification.timerOrderSign_of_eraseMaxTimeField`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L145).

```lean
lemma timerOrderSign_of_eraseMaxTimeField (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    timeOrderSign (eraseMaxTimeField φ φs) = timeOrderSign (φ :: φs) *
    𝓢(𝓕 |>ₛ maxTimeField φ φs, 𝓕 |>ₛ (φ :: φs).take (maxTimeFieldPos φ φs))
```

**`FieldSpecification.timeOrderList`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L155).

> The time ordering of a list of states. A schematic example is:
> - `normalOrderList [φ1(t = 4), φ2(t = 5), φ3(t = 3), φ4(t = 5)]` is equal to
>   `[φ2(t = 5), φ4(t = 5), φ1(t = 4), φ3(t = 3)]`

```lean
def timeOrderList (φs : List 𝓕.FieldOp) : List 𝓕.FieldOp
```

**`FieldSpecification.timeOrderList_pair_ordered`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L158).

```lean
lemma timeOrderList_pair_ordered {φ ψ : 𝓕.FieldOp} (h : timeOrderRel φ ψ) :
    timeOrderList [φ, ψ] = [φ, ψ]
```

**`FieldSpecification.timeOrderList_pair_not_ordered`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L162).

```lean
lemma timeOrderList_pair_not_ordered {φ ψ : 𝓕.FieldOp} (h : ¬ timeOrderRel φ ψ) :
    timeOrderList [φ, ψ] = [ψ, φ]
```

**`FieldSpecification.timeOrderList_nil`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L167).

```lean
lemma timeOrderList_nil : timeOrderList (𝓕 := 𝓕) [] = []
```

**`FieldSpecification.timeOrderList_eq_maxTimeField_timeOrderList`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L170).

```lean
lemma timeOrderList_eq_maxTimeField_timeOrderList (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    timeOrderList (φ :: φs) = maxTimeField φ φs :: timeOrderList (eraseMaxTimeField φ φs)
```

## Time ordering for CrAnFieldOp

## timeOrderRel

**`FieldSpecification.crAnTimeOrderRel`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L199).

> For a field specification `𝓕`, `𝓕.crAnTimeOrderRel` is a relation on
>   `𝓕.CrAnFieldOp` representing time ordering.
>   It is defined such that `𝓕.crAnTimeOrderRel φ₀ φ₁` is true if and only if one of the following
>   holds
> - `φ₀` is an *outgoing* asymptotic operator
> - `φ₁` is an *incoming* asymptotic field operator
> - `φ₀` and `φ₁` are both position field operators where
>   the `SpaceTime` point of `φ₀` has a time *greater* than or equal to that of `φ₁`.
>
> Thus, colloquially `𝓕.crAnTimeOrderRel φ₀ φ₁` if `φ₀` has time *greater* than or equal to `φ₁`.
> The use of *greater* than rather then *less* than is because on ordering lists of operators
> it is needed that the operator with the greatest time is to the left.

```lean
def crAnTimeOrderRel (a b : 𝓕.CrAnFieldOp) : Prop
```

**An instance with no name**, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L203).

> The relation `crAnTimeOrderRel` is decidable, but not computable so due to
> `Real.decidableLE`.

```lean
noncomputable instance (φ φ' : 𝓕.CrAnFieldOp) : Decidable (crAnTimeOrderRel φ φ')
```

**An instance with no name**, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L207).

> Time ordering of `CrAnFieldOp` is total.

```lean
instance : Std.Total 𝓕.crAnTimeOrderRel
```

**An instance with no name**, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L211).

> Time ordering of `CrAnFieldOp` is transitive.

```lean
instance : IsTrans 𝓕.CrAnFieldOp 𝓕.crAnTimeOrderRel
```

**`FieldSpecification.crAnTimeOrderRel_refl`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L215).

```lean
lemma crAnTimeOrderRel_refl (φ : 𝓕.CrAnFieldOp) : crAnTimeOrderRel φ φ
```

**`FieldSpecification.crAnTimeOrderSign`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L222).

> For a field specification `𝓕`, and a list `φs` of `𝓕.CrAnFieldOp`,
> `𝓕.crAnTimeOrderSign φs` is the sign corresponding to the number of `ferimionic`-`fermionic`
> exchanges undertaken to time-order (i.e. order with respect to `𝓕.crAnTimeOrderRel`) `φs` using
> the insertion sort algorithm.

```lean
def crAnTimeOrderSign (φs : List 𝓕.CrAnFieldOp) : ℂ
```

**`FieldSpecification.crAnTimeOrderSign_nil`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L226).

```lean
lemma crAnTimeOrderSign_nil : crAnTimeOrderSign (𝓕 := 𝓕) [] = 1
```

**`FieldSpecification.crAnTimeOrderSign_pair_ordered`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L229).

```lean
lemma crAnTimeOrderSign_pair_ordered {φ ψ : 𝓕.CrAnFieldOp} (h : crAnTimeOrderRel φ ψ) :
    crAnTimeOrderSign [φ, ψ] = 1
```

**`FieldSpecification.crAnTimeOrderSign_pair_not_ordered`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L233).

```lean
lemma crAnTimeOrderSign_pair_not_ordered {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) :
    crAnTimeOrderSign [φ, ψ] = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ)
```

**`FieldSpecification.crAnTimeOrderSign_swap_eq_time`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L238).

```lean
lemma crAnTimeOrderSign_swap_eq_time {φ ψ : 𝓕.CrAnFieldOp}
    (h1 : crAnTimeOrderRel φ ψ) (h2 : crAnTimeOrderRel ψ φ) (φs φs' : List 𝓕.CrAnFieldOp) :
    crAnTimeOrderSign (φs ++ φ :: ψ :: φs') = crAnTimeOrderSign (φs ++ ψ :: φ :: φs')
```

**`FieldSpecification.crAnTimeOrderList`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L245).

> For a field specification `𝓕`, and a list `φs` of `𝓕.CrAnFieldOp`,
> `𝓕.crAnTimeOrderList φs` is the list `φs` time-ordered using the insertion sort algorithm.

```lean
def crAnTimeOrderList (φs : List 𝓕.CrAnFieldOp) : List 𝓕.CrAnFieldOp
```

**`FieldSpecification.crAnTimeOrderList_nil`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L249).

```lean
lemma crAnTimeOrderList_nil : crAnTimeOrderList (𝓕 := 𝓕) [] = []
```

**`FieldSpecification.crAnTimeOrderList_pair_ordered`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L252).

```lean
lemma crAnTimeOrderList_pair_ordered {φ ψ : 𝓕.CrAnFieldOp} (h : crAnTimeOrderRel φ ψ) :
    crAnTimeOrderList [φ, ψ] = [φ, ψ]
```

**`FieldSpecification.crAnTimeOrderList_pair_not_ordered`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L256).

```lean
lemma crAnTimeOrderList_pair_not_ordered {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) :
    crAnTimeOrderList [φ, ψ] = [ψ, φ]
```

**`FieldSpecification.orderedInsert_swap_eq_time`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L260).

```lean
lemma orderedInsert_swap_eq_time {φ ψ : 𝓕.CrAnFieldOp}
    (h1 : crAnTimeOrderRel φ ψ) (h2 : crAnTimeOrderRel ψ φ) (φs : List 𝓕.CrAnFieldOp) :
    List.orderedInsert crAnTimeOrderRel φ (List.orderedInsert crAnTimeOrderRel ψ φs) =
    List.takeWhile (fun b => ¬ crAnTimeOrderRel ψ b) φs ++ φ :: ψ ::
    List.dropWhile (fun b => ¬ crAnTimeOrderRel ψ b) φs
```

**`FieldSpecification.orderedInsert_in_swap_eq_time`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L272).

```lean
lemma orderedInsert_in_swap_eq_time {φ ψ φ': 𝓕.CrAnFieldOp} (h1 : crAnTimeOrderRel φ ψ)
    (h2 : crAnTimeOrderRel ψ φ) : (φs φs' : List 𝓕.CrAnFieldOp) → ∃ l1 l2,
    List.orderedInsert crAnTimeOrderRel φ' (φs ++ φ :: ψ :: φs') = l1 ++ φ :: ψ :: l2 ∧
    List.orderedInsert crAnTimeOrderRel φ' (φs ++ ψ :: φ :: φs') = l1 ++ ψ :: φ :: l2
  | [], φs' => by
    have h1 (b : 𝓕.CrAnFieldOp) : (crAnTimeOrderRel b φ) ↔ (crAnTimeOrderRel b ψ) :=
      Iff.intro (fun h => IsTrans.trans _ _ _ h h1) (fun h => IsTrans.trans _ _ _ h h2)
    simp only [List.nil_append, List.orderedInsert, ← h1 φ']
    by_cases h : crAnTimeOrderRel φ' φ
    · use [φ'], φs'
      simp [h]
    · use [], List.orderedInsert crAnTimeOrderRel φ' φs'
      simp [h]
  | φ'' :: φs, φs' => by
    obtain ⟨l1, l2, hl⟩
```

**`FieldSpecification.crAnTimeOrderList_swap_eq_time`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L295).

```lean
lemma crAnTimeOrderList_swap_eq_time {φ ψ : 𝓕.CrAnFieldOp}
    (h1 : crAnTimeOrderRel φ ψ) (h2 : crAnTimeOrderRel ψ φ) :
    (φs φs' : List 𝓕.CrAnFieldOp) →
    ∃ (l1 l2 : List 𝓕.CrAnFieldOp),
      crAnTimeOrderList (φs ++ φ :: ψ :: φs') = l1 ++ φ :: ψ :: l2 ∧
      crAnTimeOrderList (φs ++ ψ :: φ :: φs') = l1 ++ ψ :: φ :: l2
  | [], φs' => by
    simp only [crAnTimeOrderList, List.nil_append, List.insertionSort]
    refine ⟨_, _, orderedInsert_swap_eq_time h1 h2 _, ?_⟩
    have h1' (b : 𝓕.CrAnFieldOp) : (crAnTimeOrderRel φ b) ↔ (crAnTimeOrderRel ψ b) :=
      Iff.intro (fun h => IsTrans.trans _ _ _ h2 h) (fun h => IsTrans.trans _ _ _ h1 h)
    simpa only [← h1', decide_not, List.foldr_cons] using orderedInsert_swap_eq_time h2 h1 _
  | φ'' :: φs, φs' => by
    obtain ⟨l1, l2, hl⟩
```

## Relationship to sections

**`FieldSpecification.koszulSignInsert_crAnTimeOrderRel_crAnSection`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L318).

```lean
lemma koszulSignInsert_crAnTimeOrderRel_crAnSection {φ : 𝓕.FieldOp} {ψ : 𝓕.CrAnFieldOp}
    (h : ψ.1 = φ) : {φs : List 𝓕.FieldOp} → (ψs : CrAnSection φs) →
    Wick.koszulSignInsert 𝓕.crAnStatistics 𝓕.crAnTimeOrderRel ψ ψs.1 =
    Wick.koszulSignInsert 𝓕.fieldOpStatistic 𝓕.timeOrderRel φ φs
  | [], ⟨[], h⟩ => by
    simp [Wick.koszulSignInsert]
  | φ' :: φs, ⟨ψ' :: ψs, h1⟩ => by
    simp only [List.map_cons, List.cons.injEq] at h1
    obtain ⟨rfl, h2⟩
```

**`FieldSpecification.crAnTimeOrderSign_crAnSection`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L333).

```lean
lemma crAnTimeOrderSign_crAnSection : {φs : List 𝓕.FieldOp} → (ψs : CrAnSection φs) →
    crAnTimeOrderSign ψs.1 = timeOrderSign φs
```

**`FieldSpecification.orderedInsert_crAnTimeOrderRel_crAnSection`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L343).

```lean
lemma orderedInsert_crAnTimeOrderRel_crAnSection {φ : 𝓕.FieldOp} {ψ : 𝓕.CrAnFieldOp}
    (h : ψ.1 = φ) : {φs : List 𝓕.FieldOp} → (ψs : CrAnSection φs) →
    (List.orderedInsert 𝓕.crAnTimeOrderRel ψ ψs.1).map 𝓕.crAnFieldOpToFieldOp =
    List.orderedInsert 𝓕.timeOrderRel φ φs
  | [], ⟨[], _⟩ => by
    simp [crAnFieldOpToFieldOp, h]
  | φ' :: φs, ⟨ψ' :: ψs, h1⟩ => by
    simp only [List.map_cons, List.cons.injEq] at h1
    obtain ⟨rfl, h2⟩
```

**`FieldSpecification.crAnTimeOrderList_crAnSection_is_crAnSection`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L357).

```lean
lemma crAnTimeOrderList_crAnSection_is_crAnSection : {φs : List 𝓕.FieldOp} → (ψs : CrAnSection φs) →
    (crAnTimeOrderList ψs.1).map 𝓕.crAnFieldOpToFieldOp = timeOrderList φs
```

**`FieldSpecification.crAnSectionTimeOrder`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L367).

> Time ordering of sections of a list of states.

```lean
def crAnSectionTimeOrder (φs : List 𝓕.FieldOp) (ψs : CrAnSection φs) :
    CrAnSection (timeOrderList φs)
```

**`FieldSpecification.orderedInsert_crAnTimeOrderRel_injective`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L372).

```lean
lemma orderedInsert_crAnTimeOrderRel_injective {ψ ψ' : 𝓕.CrAnFieldOp} (h : ψ.1 = ψ'.1) :
    {φs : List 𝓕.FieldOp} → (ψs ψs' : 𝓕.CrAnSection φs) →
    (ho : List.orderedInsert crAnTimeOrderRel ψ ψs.1 =
    List.orderedInsert crAnTimeOrderRel ψ' ψs'.1) → ψ = ψ' ∧ ψs = ψs'
  | [], ⟨[], _⟩, ⟨[], _⟩, h => by
    simpa using h
  | φ :: φs, ⟨ψ1 :: ψs, h1⟩, ⟨ψ1' :: ψs', h1'⟩, ho => by
    simp only [List.map_cons, List.cons.injEq] at h1 h1'
    have key : crAnTimeOrderRel ψ ψ1 ↔ crAnTimeOrderRel ψ' ψ1' := by
      rw [crAnFieldOpToFieldOp] at h1 h1'
      simp only [crAnTimeOrderRel, h, h1.1, h1'.1]
    simp only [List.orderedInsert] at ho
    by_cases hr : crAnTimeOrderRel ψ ψ1
    · simp_all
    · simp only [hr, key.not.mp hr, ↓reduceIte, List.cons.injEq] at ho
      obtain ⟨rfl, ho2⟩
```

**`FieldSpecification.crAnSectionTimeOrder_injective`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L392).

```lean
lemma crAnSectionTimeOrder_injective : {φs : List 𝓕.FieldOp} →
    Function.Injective (𝓕.crAnSectionTimeOrder φs)
```

**`FieldSpecification.crAnSectionTimeOrder_bijective`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L409).

```lean
lemma crAnSectionTimeOrder_bijective (φs : List 𝓕.FieldOp) :
    Function.Bijective (𝓕.crAnSectionTimeOrder φs)
```

**`FieldSpecification.sum_crAnSections_timeOrder`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L414).

```lean
lemma sum_crAnSections_timeOrder {φs : List 𝓕.FieldOp} [AddCommMonoid M]
    (f : CrAnSection (timeOrderList φs) → M) : ∑ s, f s = ∑ s, f (𝓕.crAnSectionTimeOrder φs s)
```

## normTimeOrderRel

**`FieldSpecification.normTimeOrderRel`**, a def, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L426).

> The time ordering relation on `CrAnFieldOp` such that if two CrAnFieldOp have the same
> time, we normal order them.

```lean
def normTimeOrderRel (a b : 𝓕.CrAnFieldOp) : Prop
```

**An instance with no name**, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L431).

> The relation `normTimeOrderRel` is decidable, but not computable so due to
> `Real.decidableLE`.

```lean
noncomputable instance (φ φ' : 𝓕.CrAnFieldOp) : Decidable (normTimeOrderRel φ φ')
```

**An instance with no name**, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L435).

> Norm-Time ordering of `CrAnFieldOp` is total.

```lean
instance : Std.Total 𝓕.normTimeOrderRel
```

**An instance with no name**, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L443).

> Norm-Time ordering of `CrAnFieldOp` is transitive.

```lean
instance : IsTrans 𝓕.CrAnFieldOp 𝓕.normTimeOrderRel
```

**`FieldSpecification.normTimeOrderSign`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L453).

> The sign associated with putting a list of `CrAnFieldOp` into normal-time order (with
> the state of greatest time to the left).
> We pick up a minus sign for every fermion paired crossed.

```lean
def normTimeOrderSign (φs : List 𝓕.CrAnFieldOp) : ℂ
```

**`FieldSpecification.normTimeOrderList`**, a def, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean#L457).

> Sort a list of `CrAnFieldOp` based on `normTimeOrderRel`.

```lean
def normTimeOrderList (φs : List 𝓕.CrAnFieldOp) : List 𝓕.CrAnFieldOp
```

## Depends on

- [List lemmas (InsertionSort)](../../../mathematics/formathlib/list-insertionsort.md)
- [Creation and annihilation sections](fieldspecification-cransection.md)
- [Normal Ordering of states](fieldspecification-normalorder.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/TimeOrder.lean)
