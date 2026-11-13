---
declaration: module
origin: cited
lean: WickContraction.EqTimeOnly, WickContraction.EqTimeOnly.timeOrderRel_of_eqTimeOnly_pair, WickContraction.EqTimeOnly.timeOrderRel_both_of_eqTimeOnly, WickContraction.EqTimeOnly.eqTimeOnly_iff_forall_finset, WickContraction.EqTimeOnly.empty_mem, WickContraction.EqTimeOnly.staticContract_eq_timeContract_of_eqTimeOnly, WickContraction.EqTimeOnly.eqTimeOnly_congr, WickContraction.EqTimeOnly.quotContraction_eqTimeOnly
statement: formalized
proof: formalized
---

# Time contractions (TimeCond)

The module `Physlib.QFT.PerturbationTheory.WickContraction.TimeCond`, [Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean): 34 declarations (2 instances with no name), 7 with a docstring.

**`WickContraction.EqTimeOnly`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L27).

> The condition on a Wick contraction which is true iff and only if every contraction
> is between two fields of equal time.

```lean
def EqTimeOnly {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) : Prop
```

**An instance with no name**, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L31).

```lean
instance {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    Decidable (EqTimeOnly φsΛ)
```

**`WickContraction.EqTimeOnly.timeOrderRel_of_eqTimeOnly_pair`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L38).

```lean
lemma timeOrderRel_of_eqTimeOnly_pair {i j : Fin φs.length} (h : {i, j} ∈ φsΛ.1)
    (hc : EqTimeOnly φsΛ) :
    timeOrderRel φs[i] φs[j]
```

**`WickContraction.EqTimeOnly.timeOrderRel_both_of_eqTimeOnly`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L42).

```lean
lemma timeOrderRel_both_of_eqTimeOnly {i j : Fin φs.length} (h : {i, j} ∈ φsΛ.1)
    (hc : EqTimeOnly φsΛ) :
    timeOrderRel φs[i] φs[j] ∧ timeOrderRel φs[j] φs[i]
```

**`WickContraction.EqTimeOnly.eqTimeOnly_iff_forall_finset`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L48).

```lean
lemma eqTimeOnly_iff_forall_finset {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    φsΛ.EqTimeOnly ↔ ∀ (a : φsΛ.1),
      timeOrderRel (φs[φsΛ.fstFieldOfContract a]) (φs[φsΛ.sndFieldOfContract a])
      ∧ timeOrderRel (φs[φsΛ.sndFieldOfContract a]) (φs[φsΛ.fstFieldOfContract a])
```

**`WickContraction.EqTimeOnly.empty_mem`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L79).

```lean
lemma empty_mem {φs : List 𝓕.FieldOp} : empty (n := φs.length).EqTimeOnly
```

**`WickContraction.EqTimeOnly.staticContract_eq_timeContract_of_eqTimeOnly`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L86).

> Let `φs` be a list of `𝓕.FieldOp` and `φsΛ` a `WickContraction` of `φs` within
> which every contraction involves two `𝓕.FieldOp`s that have the same time, then
> `φsΛ.staticContract = φsΛ.timeContract`.

```lean
lemma staticContract_eq_timeContract_of_eqTimeOnly (h : φsΛ.EqTimeOnly) :
    φsΛ.staticContract = φsΛ.timeContract
```

**`WickContraction.EqTimeOnly.eqTimeOnly_congr`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L97).

```lean
lemma eqTimeOnly_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs') (φsΛ : WickContraction φs.length) :
    (congr (by simp [h]) φsΛ).EqTimeOnly (φs := φs') ↔ φsΛ.EqTimeOnly
```

**`WickContraction.EqTimeOnly.quotContraction_eqTimeOnly`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L102).

```lean
lemma quotContraction_eqTimeOnly {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (h : φsΛ.EqTimeOnly) (S : Finset (Finset (Fin φs.length))) (ha : S ⊆ φsΛ.1) :
    (φsΛ.quotContraction S ha).EqTimeOnly
```

**`WickContraction.EqTimeOnly.exists_join_singleton_of_card_ge_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L114).

```lean
lemma exists_join_singleton_of_card_ge_zero {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (h : 0 < φsΛ.1.card) (h1 : φsΛ.EqTimeOnly) :
    ∃ (i j : Fin φs.length) (h : i < j) (φsucΛ : WickContraction [singleton h]ᵘᶜ.length),
    φsΛ = join (singleton h) φsucΛ ∧ (timeOrderRel φs[i] φs[j] ∧ timeOrderRel φs[j] φs[i])
    ∧ φsucΛ.EqTimeOnly ∧ φsucΛ.1.card + 1 = φsΛ.1.card
```

**`WickContraction.EqTimeOnly.timeOrder_timeContract_mul_of_eqTimeOnly_mid_induction`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L140).

```lean
lemma timeOrder_timeContract_mul_of_eqTimeOnly_mid_induction {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (hl : φsΛ.EqTimeOnly) (a b: 𝓕.WickAlgebra) : (n : ℕ) → (hn : φsΛ.1.card = n) →
    𝓣(a * φsΛ.timeContract.1 * b) = φsΛ.timeContract.1 * 𝓣(a * b)
  | 0, hn => by
    rw [@card_zero_iff_empty] at hn
    subst hn
    simp
  | Nat.succ n, hn => by
    obtain ⟨i, j, hij, φsucΛ, rfl, h2, h3, h4⟩
```

**`WickContraction.EqTimeOnly.timeOrder_timeContract_mul_of_eqTimeOnly_mid`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L162).

```lean
lemma timeOrder_timeContract_mul_of_eqTimeOnly_mid {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (hl : φsΛ.EqTimeOnly) (a b : 𝓕.WickAlgebra) :
    𝓣(a * φsΛ.timeContract.1 * b) = φsΛ.timeContract.1 * 𝓣(a * b)
```

**`WickContraction.EqTimeOnly.timeOrder_timeContract_mul_of_eqTimeOnly_left`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L174).

> Let `φs` be a list of `𝓕.FieldOp`, `φsΛ` a `WickContraction` of `φs` within
> which every contraction involves two `𝓕.FieldOp`s that have the same time and
> `b` a general element in `𝓕.WickAlgebra`. Then
> `𝓣(φsΛ.timeContract.1 * b) = φsΛ.timeContract.1 * 𝓣(b)`.
>
> This follows from properties of orderings and the ideal defining `𝓕.WickAlgebra`.

```lean
lemma timeOrder_timeContract_mul_of_eqTimeOnly_left {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (hl : φsΛ.EqTimeOnly) (b : 𝓕.WickAlgebra) :
    𝓣(φsΛ.timeContract.1 * b) = φsΛ.timeContract.1 * 𝓣(b)
```

**`WickContraction.EqTimeOnly.exists_join_singleton_of_not_eqTimeOnly`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L183).

```lean
lemma exists_join_singleton_of_not_eqTimeOnly {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (h1 : ¬ φsΛ.EqTimeOnly) :
    ∃ (i j : Fin φs.length) (h : i < j) (φsucΛ : WickContraction [singleton h]ᵘᶜ.length),
    φsΛ = join (singleton h) φsucΛ ∧ (¬ timeOrderRel φs[i] φs[j] ∨ ¬ timeOrderRel φs[j] φs[i])
```

**`WickContraction.EqTimeOnly.timeOrder_timeContract_of_not_eqTimeOnly`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L202).

```lean
lemma timeOrder_timeContract_of_not_eqTimeOnly {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (hl : ¬ φsΛ.EqTimeOnly) : 𝓣(φsΛ.timeContract.1) = 0
```

**`WickContraction.EqTimeOnly.timeOrder_staticContract_of_not_mem`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L217).

> Let `φs` be a list of `𝓕.FieldOp` and `φsΛ` a `WickContraction` with
> at least one contraction between `𝓕.FieldOp` that do not have the same time. Then
> `𝓣(φsΛ.staticContract.1) = 0`.

```lean
lemma timeOrder_staticContract_of_not_mem {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (hl : ¬ φsΛ.EqTimeOnly) : 𝓣(φsΛ.staticContract.1) = 0
```

**`WickContraction.HaveEqTime`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L232).

> The condition on a Wick contraction which is true if it has at least one contraction
> which is between two equal time fields.

```lean
def HaveEqTime {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) : Prop
```

**An instance with no name**, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L236).

```lean
noncomputable instance {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    Decidable (HaveEqTime φsΛ)
```

**`WickContraction.haveEqTime_iff_finset`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L242).

```lean
lemma haveEqTime_iff_finset {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    HaveEqTime φsΛ ↔ ∃ (a : Finset (Fin φs.length)) (h : a ∈ φsΛ.1),
      timeOrderRel φs[φsΛ.fstFieldOfContract ⟨a, h⟩] φs[φsΛ.sndFieldOfContract ⟨a, h⟩]
    ∧ timeOrderRel φs[φsΛ.sndFieldOfContract ⟨a, h⟩] φs[φsΛ.fstFieldOfContract ⟨a, h⟩]
```

**`WickContraction.empty_not_haveEqTime`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L273).

```lean
lemma empty_not_haveEqTime {φs : List 𝓕.FieldOp} :
    ¬ HaveEqTime (empty : WickContraction φs.length)
```

**`WickContraction.eqTimeContractSet`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L279).

> Given a Wick contraction the subset of contracted pairs between equal time fields.

```lean
def eqTimeContractSet {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    Finset (Finset (Fin φs.length))
```

**`WickContraction.eqTimeContractSet_subset`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L286).

```lean
lemma eqTimeContractSet_subset {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    eqTimeContractSet φsΛ ⊆ φsΛ.1
```

**`WickContraction.mem_of_mem_eqTimeContractSet`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L292).

```lean
lemma mem_of_mem_eqTimeContractSet{φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {a : Finset (Fin φs.length)} (h : a ∈ eqTimeContractSet φsΛ) : a ∈ φsΛ.1
```

**`WickContraction.join_eqTimeContractSet`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L296).

```lean
lemma join_eqTimeContractSet {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    eqTimeContractSet (join φsΛ φsucΛ) = φsΛ.eqTimeContractSet ∪
    φsucΛ.eqTimeContractSet.map (Finset.mapEmbedding uncontractedListEmd).toEmbedding
```

**`WickContraction.eqTimeContractSet_of_not_haveEqTime`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L340).

```lean
lemma eqTimeContractSet_of_not_haveEqTime {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (h : ¬ HaveEqTime φsΛ) : eqTimeContractSet φsΛ = ∅
```

**`WickContraction.eqTimeContractSet_of_mem_eqTimeOnly`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L350).

```lean
lemma eqTimeContractSet_of_mem_eqTimeOnly {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (h : φsΛ.EqTimeOnly) : eqTimeContractSet φsΛ = φsΛ.1
```

**`WickContraction.subContraction_eqTimeContractSet_eqTimeOnly`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L358).

```lean
lemma subContraction_eqTimeContractSet_eqTimeOnly {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) :
    (φsΛ.subContraction (eqTimeContractSet φsΛ) (eqTimeContractSet_subset φsΛ)).EqTimeOnly
```

**`WickContraction.pair_mem_eqTimeContractSet_iff`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L369).

```lean
lemma pair_mem_eqTimeContractSet_iff {φs : List 𝓕.FieldOp} {i j : Fin φs.length}
    (φsΛ : WickContraction φs.length) (h : {i, j} ∈ φsΛ.1) :
    {i, j} ∈ φsΛ.eqTimeContractSet ↔ timeOrderRel φs[i] φs[j] ∧ timeOrderRel φs[j] φs[i]
```

**`WickContraction.subContraction_eqTimeContractSet_not_empty_of_haveEqTime`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L389).

```lean
lemma subContraction_eqTimeContractSet_not_empty_of_haveEqTime
    {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) (h : HaveEqTime φsΛ) :
    φsΛ.subContraction (eqTimeContractSet φsΛ) (eqTimeContractSet_subset φsΛ) ≠ empty
```

**`WickContraction.quotContraction_eqTimeContractSet_not_haveEqTime`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L404).

```lean
lemma quotContraction_eqTimeContractSet_not_haveEqTime {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) :
    ¬ HaveEqTime (φsΛ.quotContraction (eqTimeContractSet φsΛ) (eqTimeContractSet_subset φsΛ))
```

**`WickContraction.join_haveEqTime_of_eqTimeOnly_nonEmpty`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L422).

```lean
lemma join_haveEqTime_of_eqTimeOnly_nonEmpty {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (h1 : φsΛ.EqTimeOnly) (h2 : φsΛ ≠ empty)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    HaveEqTime (join φsΛ φsucΛ)
```

**`WickContraction.hasEqTimeEquiv_ext_sigma`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L434).

```lean
lemma hasEqTimeEquiv_ext_sigma {φs : List 𝓕.FieldOp} {x1 x2 :
    Σ (φsΛ : {φsΛ : WickContraction φs.length // φsΛ.EqTimeOnly ∧ φsΛ ≠ empty}),
    {φssucΛ : WickContraction [φsΛ.1]ᵘᶜ.length // ¬ HaveEqTime φssucΛ}}
    (h1 : x1.1.1 = x2.1.1) (h2 : x1.2.1 = congr (by simp [h1]) x2.2.1) : x1 = x2
```

**`WickContraction.hasEqTimeEquiv`**, a def, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L449).

> The equivalence which separates a Wick contraction which has an equal time contraction
> into a non-empty contraction only between equal-time fields and a Wick contraction which
> does not have equal time contractions.

```lean
def hasEqTimeEquiv (φs : List 𝓕.FieldOp) :
    {φsΛ : WickContraction φs.length // HaveEqTime φsΛ} ≃
    Σ (φsΛ : {φsΛ : WickContraction φs.length // φsΛ.EqTimeOnly ∧ φsΛ ≠ empty}),
    {φssucΛ : WickContraction [φsΛ.1]ᵘᶜ.length // ¬ HaveEqTime φssucΛ}
```

**`WickContraction.sum_haveEqTime`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean#L490).

```lean
lemma sum_haveEqTime (φs : List 𝓕.FieldOp)
    (f : WickContraction φs.length → M) [AddCommMonoid M]:
  ∑ (φsΛ : {φsΛ : WickContraction φs.length // HaveEqTime φsΛ}), f φsΛ =
  ∑ (φsΛ : {φsΛ : WickContraction φs.length // φsΛ.EqTimeOnly ∧ φsΛ ≠ empty}),
  ∑ (φssucΛ : {φssucΛ : WickContraction [φsΛ.1]ᵘᶜ.length // ¬ HaveEqTime φssucΛ}),
    f (join φsΛ.1 φssucΛ.1)
```

## Depends on

- [Join of contractions](wickcontraction-join.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeCond.lean)
