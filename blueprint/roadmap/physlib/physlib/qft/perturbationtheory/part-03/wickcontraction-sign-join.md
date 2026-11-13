---
declaration: module
origin: cited
lean: WickContraction.stat_signFinset_right, WickContraction.signFinset_right_map_uncontractedListEmd_eq_filter, WickContraction.sign_right_eq_prod_mul_prod, WickContraction.join_singleton_signFinset_eq_filter, WickContraction.join_singleton_left_signFinset_eq_filter, WickContraction.joinSignRightExtra, WickContraction.joinSignLeftExtra, WickContraction.join_singleton_sign_left
statement: formalized
proof: formalized
---

# Sign associated with joining two Wick contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Sign.Join`, [Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean): 15 declarations, 4 with a docstring.

**`WickContraction.stat_signFinset_right`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L27).

```lean
lemma stat_signFinset_right {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i j : Fin [φsΛ]ᵘᶜ.length) :
    (𝓕 |>ₛ ⟨[φsΛ]ᵘᶜ.get, φsucΛ.signFinset i j⟩) =
    (𝓕 |>ₛ ⟨φs.get, (φsucΛ.signFinset i j).map uncontractedListEmd⟩)
```

**`WickContraction.signFinset_right_map_uncontractedListEmd_eq_filter`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L39).

```lean
lemma signFinset_right_map_uncontractedListEmd_eq_filter {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length)
    (i j : Fin [φsΛ]ᵘᶜ.length) : (φsucΛ.signFinset i j).map uncontractedListEmd =
    ((join φsΛ φsucΛ).signFinset (uncontractedListEmd i) (uncontractedListEmd j)).filter
    (fun c => c ∈ φsΛ.uncontracted)
```

**`WickContraction.sign_right_eq_prod_mul_prod`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L97).

```lean
lemma sign_right_eq_prod_mul_prod {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    φsucΛ.sign = (∏ a, 𝓢(𝓕|>ₛ [φsΛ]ᵘᶜ[φsucΛ.sndFieldOfContract a], 𝓕|>ₛ ⟨φs.get,
    ((join φsΛ φsucΛ).signFinset (uncontractedListEmd (φsucΛ.fstFieldOfContract a))
      (uncontractedListEmd (φsucΛ.sndFieldOfContract a))).filter
      (fun c => ¬ c ∈ φsΛ.uncontracted)⟩)) *
    (∏ a, 𝓢(𝓕|>ₛ [φsΛ]ᵘᶜ[φsucΛ.sndFieldOfContract a], 𝓕|>ₛ ⟨φs.get,
      ((join φsΛ φsucΛ).signFinset (uncontractedListEmd (φsucΛ.fstFieldOfContract a))
        (uncontractedListEmd (φsucΛ.sndFieldOfContract a)))⟩))
```

**`WickContraction.join_singleton_signFinset_eq_filter`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L114).

```lean
lemma join_singleton_signFinset_eq_filter {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (join (singleton h) φsucΛ).signFinset i j =
    ((singleton h).signFinset i j).filter (fun c => ¬
    (((join (singleton h) φsucΛ).getDual? c).isSome ∧
    ((h1 : ((join (singleton h) φsucΛ).getDual? c).isSome) →
    (((join (singleton h) φsucΛ).getDual? c).get h1) < i)))
```

**`WickContraction.join_singleton_left_signFinset_eq_filter`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L156).

```lean
lemma join_singleton_left_signFinset_eq_filter {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (𝓕 |>ₛ ⟨φs.get, (singleton h).signFinset i j⟩)
    = (𝓕 |>ₛ ⟨φs.get, (join (singleton h) φsucΛ).signFinset i j⟩) *
      (𝓕 |>ₛ ⟨φs.get, ((singleton h).signFinset i j).filter (fun c =>
      (((join (singleton h) φsucΛ).getDual? c).isSome ∧
      ((h1 : ((join (singleton h) φsucΛ).getDual? c).isSome) →
      (((join (singleton h) φsucΛ).getDual? c).get h1) < i)))⟩)
```

**`WickContraction.joinSignRightExtra`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L173).

> The difference in sign between `φsucΛ.sign` and the direct contribution of `φsucΛ` to
> `(join (singleton h) φsucΛ)`.

```lean
def joinSignRightExtra {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) : ℂ
```

**`WickContraction.joinSignLeftExtra`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L183).

> The difference in sign between `(singleton h).sign` and the direct contribution of
> `(singleton h)` to `(join (singleton h) φsucΛ)`.

```lean
def joinSignLeftExtra {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) : ℂ
```

**`WickContraction.join_singleton_sign_left`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L191).

```lean
lemma join_singleton_sign_left {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (singleton h).sign = 𝓢(𝓕 |>ₛ φs[j],
    (𝓕 |>ₛ ⟨φs.get, (join (singleton h) φsucΛ).signFinset i j⟩)) * (joinSignLeftExtra h φsucΛ)
```

**`WickContraction.join_singleton_sign_right`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L201).

```lean
lemma join_singleton_sign_right {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    φsucΛ.sign =
    (joinSignRightExtra h φsucΛ) *
    (∏ a, 𝓢(𝓕|>ₛ [singleton h]ᵘᶜ[φsucΛ.sndFieldOfContract a], 𝓕|>ₛ ⟨φs.get,
      ((join (singleton h) φsucΛ).signFinset (uncontractedListEmd (φsucΛ.fstFieldOfContract a))
        (uncontractedListEmd (φsucΛ.sndFieldOfContract a)))⟩))
```

**`WickContraction.joinSignRightExtra_eq_i_j_finset_eq_if`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L212).

```lean
lemma joinSignRightExtra_eq_i_j_finset_eq_if {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j) (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    joinSignRightExtra h φsucΛ = ∏ a,
    𝓢((𝓕|>ₛ [singleton h]ᵘᶜ[φsucΛ.sndFieldOfContract a]),
    𝓕 |>ₛ ⟨φs.get, (if uncontractedListEmd (φsucΛ.fstFieldOfContract a) < j ∧
        j < uncontractedListEmd (φsucΛ.sndFieldOfContract a) ∧
        uncontractedListEmd (φsucΛ.fstFieldOfContract a) < i then {j} else ∅)
        ∪ (if uncontractedListEmd (φsucΛ.fstFieldOfContract a) < i ∧
        i < uncontractedListEmd (φsucΛ.sndFieldOfContract a) then {i} else ∅)⟩)
```

**`WickContraction.joinSignLeftExtra_eq_joinSignRightExtra`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L304).

```lean
lemma joinSignLeftExtra_eq_joinSignRightExtra {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j) (hs : (𝓕 |>ₛ φs[i]) = (𝓕 |>ₛ φs[j]))
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    joinSignLeftExtra h φsucΛ = joinSignRightExtra h φsucΛ
```

**`WickContraction.join_sign_singleton`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L384).

```lean
lemma join_sign_singleton {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j) (hs : (𝓕 |>ₛ φs[i]) = (𝓕 |>ₛ φs[j]))
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (join (singleton h) φsucΛ).sign = (singleton h).sign * φsucΛ.sign
```

**`WickContraction.join_sign_induction`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L402).

```lean
lemma join_sign_induction {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (hc : φsΛ.GradingCompliant) :
    (n : ℕ) → (hn : φsΛ.1.card = n) →
    (join φsΛ φsucΛ).sign = φsΛ.sign * φsucΛ.sign
  | 0, hn => by
    rw [@card_zero_iff_empty] at hn
    subst hn
    simp only [empty_join, sign_empty, one_mul]
    apply sign_congr
    simp
  | Nat.succ n, hn => by
    obtain ⟨i, j, hij, φsucΛ', rfl, h1, h2, h3⟩
```

**`WickContraction.join_sign`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L434).

> For a list `φs` of `𝓕.FieldOp`, a grading compliant Wick contraction `φsΛ` of `φs`,
> and a Wick contraction `φsucΛ` of `[φsΛ]ᵘᶜ`, the following relation holds
> `(join φsΛ φsucΛ).sign = φsΛ.sign * φsucΛ.sign`.
>
> In `φsΛ.sign` the sign is determined by starting with the contracted pair
> whose first element occurs at the left-most position. This lemma manifests that this
> choice does not matter, and that contracted pairs can be brought together in any order.

```lean
lemma join_sign {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (hc : φsΛ.GradingCompliant) :
    (join φsΛ φsucΛ).sign = φsΛ.sign * φsucΛ.sign
```

**`WickContraction.join_sign_timeContract`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean#L444).

> For a list `φs` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`,
> and a Wick contraction `φsucΛ` of `[φsΛ]ᵘᶜ`,
> `(join φsΛ φsucΛ).sign • (join φsΛ φsucΛ).timeContract` is equal to the product of
> - `φsΛ.sign • φsΛ.timeContract` and
> - `φsucΛ.sign • φsucΛ.timeContract`.

```lean
lemma join_sign_timeContract {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).sign • (join φsΛ φsucΛ).timeContract.1 =
    (φsΛ.sign • φsΛ.timeContract.1) * (φsucΛ.sign • φsucΛ.timeContract.1)
```

## Depends on

- [Join of contractions](wickcontraction-join.md)

## Proof depends on

- [Sign on inserting and not contracting](wickcontraction-sign-insertnone.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Join.lean)
