---
declaration: module
origin: cited
lean: WickContraction.join, WickContraction.join_congr, WickContraction.joinLiftLeft, WickContraction.jointLiftLeft_injective, WickContraction.joinLiftRight, WickContraction.joinLiftRight_injective, WickContraction.jointLiftLeft_disjoint_joinLiftRight, WickContraction.jointLiftLeft_ne_joinLiftRight
statement: formalized
proof: formalized
---

# Join of contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Join`, [Physlib/QFT/PerturbationTheory/WickContraction/Join.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean): 43 declarations, 4 with a docstring.

**`WickContraction.join`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L34).

> Given a list `φs` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs` and a Wick contraction
> `φsucΛ` of `[φsΛ]ᵘᶜ`, `join φsΛ φsucΛ` is defined as the Wick contraction of `φs` consisting of
> the contractions in `φsΛ` and those in `φsucΛ`.
>
> As an example, for `φs = [φ1, φ2, φ3, φ4]`,
> `φsΛ = {{0, 1}}` corresponding to the contraction of `φ1` and `φ2` in `φs` and
> `φsucΛ = {{0, 1}}`
> corresponding to the contraction of `φ3` and `φ4` in `[φsΛ]ᵘᶜ = [φ3, φ4]`, then
> `join φsΛ φsucΛ` is the contraction `{{0, 1}, {2, 3}}` of `φs`.

```lean
def join {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) : WickContraction φs.length
```

**`WickContraction.join_congr`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L69).

```lean
lemma join_congr {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} {φsΛ' : WickContraction φs.length}
    (h1 : φsΛ = φsΛ') :
    join φsΛ φsucΛ = join φsΛ' (congr (by simp [h1]) φsucΛ)
```

**`WickContraction.joinLiftLeft`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L78).

> Given a contracting pair within `φsΛ` the corresponding contracting pair within
> `(join φsΛ φsucΛ)`.

```lean
def joinLiftLeft {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : φsΛ.1 → (join φsΛ φsucΛ).1
```

**`WickContraction.jointLiftLeft_injective`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L82).

```lean
lemma jointLiftLeft_injective {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} :
    Function.Injective (@joinLiftLeft _ _ φsΛ φsucΛ)
```

**`WickContraction.joinLiftRight`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L91).

> Given a contracting pair within `φsucΛ` the corresponding contracting pair within
> `(join φsΛ φsucΛ)`.

```lean
def joinLiftRight {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : φsucΛ.1 → (join φsΛ φsucΛ).1
```

**`WickContraction.joinLiftRight_injective`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L101).

```lean
lemma joinLiftRight_injective {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} :
    Function.Injective (@joinLiftRight _ _ φsΛ φsucΛ)
```

**`WickContraction.jointLiftLeft_disjoint_joinLiftRight`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L108).

```lean
lemma jointLiftLeft_disjoint_joinLiftRight {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} (a : φsΛ.1) (b : φsucΛ.1) :
    Disjoint (@joinLiftLeft _ _ _ φsucΛ a).1 (joinLiftRight b).1
```

**`WickContraction.jointLiftLeft_ne_joinLiftRight`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L113).

```lean
lemma jointLiftLeft_ne_joinLiftRight {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} (a : φsΛ.1) (b : φsucΛ.1) :
    joinLiftLeft a ≠ joinLiftRight b
```

**`WickContraction.joinLift`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L124).

> The map from contracted pairs of `φsΛ` and `φsucΛ` to contracted pairs in
> `(join φsΛ φsucΛ)`.

```lean
def joinLift {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : φsΛ.1 ⊕ φsucΛ.1 → (join φsΛ φsucΛ).1
```

**`WickContraction.joinLift_injective`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L130).

```lean
lemma joinLift_injective {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : Function.Injective (@joinLift _ _ φsΛ φsucΛ)
```

**`WickContraction.joinLift_surjective`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L143).

```lean
lemma joinLift_surjective {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : Function.Surjective (@joinLift _ _ φsΛ φsucΛ)
```

**`WickContraction.joinLift_bijective`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L158).

```lean
lemma joinLift_bijective {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} : Function.Bijective (@joinLift _ _ φsΛ φsucΛ)
```

**`WickContraction.prod_join`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L162).

```lean
lemma prod_join {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (f : (join φsΛ φsucΛ).1 → M) [CommMonoid M]:
      ∏ (a : (join φsΛ φsucΛ).1), f a = (∏ (a : φsΛ.1), f (joinLiftLeft a)) *
      ∏ (a : φsucΛ.1), f (joinLiftRight a)
```

**`WickContraction.joinLiftLeft_or_joinLiftRight_of_mem_join`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L170).

```lean
lemma joinLiftLeft_or_joinLiftRight_of_mem_join {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) {a : Finset (Fin φs.length)}
    (ha : a ∈ (join φsΛ φsucΛ).1) :
    (∃ b, a = (joinLiftLeft (φsucΛ := φsucΛ) b).1) ∨
    (∃ b, a = (joinLiftRight (φsucΛ := φsucΛ) b).1)
```

**`WickContraction.join_fstFieldOfContract_joinLiftRight`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L183).

```lean
lemma join_fstFieldOfContract_joinLiftRight {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (a : φsucΛ.1) :
    (join φsΛ φsucΛ).fstFieldOfContract (joinLiftRight a) =
    uncontractedListEmd (φsucΛ.fstFieldOfContract a)
```

**`WickContraction.join_sndFieldOfContract_joinLiftRight`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L194).

```lean
lemma join_sndFieldOfContract_joinLiftRight {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (a : φsucΛ.1) :
    (join φsΛ φsucΛ).sndFieldOfContract (joinLiftRight a) =
    uncontractedListEmd (φsucΛ.sndFieldOfContract a)
```

**`WickContraction.join_fstFieldOfContract_joinLiftLeft`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L205).

```lean
lemma join_fstFieldOfContract_joinLiftLeft {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (a : φsΛ.1) :
    (join φsΛ φsucΛ).fstFieldOfContract (joinLiftLeft a) =
    (φsΛ.fstFieldOfContract a)
```

**`WickContraction.join_sndFieldOfContract_joinLift`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L215).

```lean
lemma join_sndFieldOfContract_joinLift {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (a : φsΛ.1) :
    (join φsΛ φsucΛ).sndFieldOfContract (joinLiftLeft a) =
    (φsΛ.sndFieldOfContract a)
```

**`WickContraction.mem_join_right_iff`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L224).

```lean
lemma mem_join_right_iff {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (a : Finset (Fin [φsΛ]ᵘᶜ.length)) :
    a ∈ φsucΛ.1 ↔ a.map uncontractedListEmd ∈ (join φsΛ φsucΛ).1
```

**`WickContraction.join_card`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L239).

```lean
lemma join_card {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {φsucΛ : WickContraction [φsΛ]ᵘᶜ.length} :
    (join φsΛ φsucΛ).1.card = φsΛ.1.card + φsucΛ.1.card
```

**`WickContraction.empty_join`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L258).

```lean
lemma empty_join {φs : List 𝓕.FieldOp} (φsΛ : WickContraction [empty (n := φs.length)]ᵘᶜ.length) :
    join empty φsΛ = congr (by simp) φsΛ
```

**`WickContraction.join_empty`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L283).

```lean
lemma join_empty {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    join φsΛ empty = φsΛ
```

**`WickContraction.join_timeContract`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L289).

```lean
lemma join_timeContract {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).timeContract = φsΛ.timeContract * φsucΛ.timeContract
```

**`WickContraction.join_staticContract`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L297).

```lean
lemma join_staticContract {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).staticContract = φsΛ.staticContract * φsucΛ.staticContract
```

**`WickContraction.mem_join_uncontracted_of_mem_right_uncontracted`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L305).

```lean
lemma mem_join_uncontracted_of_mem_right_uncontracted {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin [φsΛ]ᵘᶜ.length)
    (ha : i ∈ φsucΛ.uncontracted) :
    uncontractedListEmd i ∈ (join φsΛ φsucΛ).uncontracted
```

**`WickContraction.exists_mem_left_uncontracted_of_mem_join_uncontracted`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L325).

```lean
lemma exists_mem_left_uncontracted_of_mem_join_uncontracted {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin φs.length)
    (ha : i ∈ (join φsΛ φsucΛ).uncontracted) :
    i ∈ φsΛ.uncontracted
```

**`WickContraction.exists_mem_right_uncontracted_of_mem_join_uncontracted`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L337).

```lean
lemma exists_mem_right_uncontracted_of_mem_join_uncontracted {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin φs.length)
    (hi : i ∈ (join φsΛ φsucΛ).uncontracted) :
    ∃ a, uncontractedListEmd a = i ∧ a ∈ φsucΛ.uncontracted
```

**`WickContraction.join_uncontractedList`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L356).

```lean
lemma join_uncontractedList {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).uncontractedList = List.map uncontractedListEmd φsucΛ.uncontractedList
```

**`WickContraction.join_uncontractedList_get`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L375).

```lean
lemma join_uncontractedList_get {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    ((join φsΛ φsucΛ).uncontractedList).get =
    φsΛ.uncontractedListEmd ∘ (φsucΛ.uncontractedList).get ∘
        (Fin.cast (by rw [join_uncontractedList]; simp))
```

**`WickContraction.join_uncontractedListGet`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L388).

```lean
lemma join_uncontractedListGet {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).uncontractedListGet = φsucΛ.uncontractedListGet
```

**`WickContraction.join_uncontractedListEmb`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L398).

```lean
lemma join_uncontractedListEmb {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).uncontractedListEmd =
    ((finCongr (congrArg List.length (join_uncontractedListGet _ _))).toEmbedding.trans
      φsucΛ.uncontractedListEmd).trans φsΛ.uncontractedListEmd
```

**`WickContraction.join_assoc`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L409).

```lean
lemma join_assoc {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (φsucΛ' : WickContraction [φsΛ.join φsucΛ]ᵘᶜ.length) :
    join (join φsΛ φsucΛ) (φsucΛ') = join φsΛ (join φsucΛ (congr
      (congrArg List.length (join_uncontractedListGet _ _)) φsucΛ'))
```

**`WickContraction.join_getDual?_apply_uncontractedListEmb_eq_none_iff`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L460).

```lean
lemma join_getDual?_apply_uncontractedListEmb_eq_none_iff {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin [φsΛ]ᵘᶜ.length) :
    (join φsΛ φsucΛ).getDual? (uncontractedListEmd i) = none
    ↔ φsucΛ.getDual? i = none
```

**`WickContraction.join_getDual?_apply_uncontractedListEmb_isSome_iff`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L475).

```lean
lemma join_getDual?_apply_uncontractedListEmb_isSome_iff {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin [φsΛ]ᵘᶜ.length) :
    ((join φsΛ φsucΛ).getDual? (uncontractedListEmd i)).isSome
    ↔ (φsucΛ.getDual? i).isSome
```

**`WickContraction.join_getDual?_apply_uncontractedListEmb_some`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L483).

```lean
lemma join_getDual?_apply_uncontractedListEmb_some {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length) (i : Fin [φsΛ]ᵘᶜ.length)
    (hi :((join φsΛ φsucΛ).getDual? (uncontractedListEmd i)).isSome) :
    ((join φsΛ φsucΛ).getDual? (uncontractedListEmd i)) =
    some (uncontractedListEmd ((φsucΛ.getDual? i).get (by
    simpa [join_getDual?_apply_uncontractedListEmb_isSome_iff]using hi)))
```

**`WickContraction.join_getDual?_apply_uncontractedListEmb`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L501).

```lean
lemma join_getDual?_apply_uncontractedListEmb {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length)
    (i : Fin [φsΛ]ᵘᶜ.length) : ((join φsΛ φsucΛ).getDual? (uncontractedListEmd i)) =
    Option.map uncontractedListEmd (φsucΛ.getDual? i)
```

## Subcontractions and quotient contractions

**`WickContraction.join_sub_quot`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L523).

```lean
lemma join_sub_quot (S : Finset (Finset (Fin φs.length))) (ha : S ⊆ φsΛ.1) :
    join (subContraction S ha) (quotContraction S ha) = φsΛ
```

**`WickContraction.subContraction_card_plus_quotContraction_card_eq`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L543).

```lean
lemma subContraction_card_plus_quotContraction_card_eq (S : Finset (Finset (Fin φs.length)))
    (ha : S ⊆ φsΛ.1) :
    (subContraction S ha).1.card + (quotContraction S ha).1.card = φsΛ.1.card
```

**`WickContraction.join_singleton_getDual?_left`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L553).

```lean
lemma join_singleton_getDual?_left {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (join (singleton h) φsucΛ).getDual? i = some j
```

**`WickContraction.join_singleton_getDual?_right`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L561).

```lean
lemma join_singleton_getDual?_right {φs : List 𝓕.FieldOp}
    {i j : Fin φs.length} (h : i < j)
    (φsucΛ : WickContraction [singleton h]ᵘᶜ.length) :
    (join (singleton h) φsucΛ).getDual? j = some i
```

**`WickContraction.exists_contraction_pair_of_card_ge_zero`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L571).

```lean
lemma exists_contraction_pair_of_card_ge_zero {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (h : 0 < φsΛ.1.card) :
    ∃ a, a ∈ φsΛ.1
```

**`WickContraction.exists_join_singleton_of_card_ge_zero`**, a lemma, [line 576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L576).

```lean
lemma exists_join_singleton_of_card_ge_zero {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length)
    (h : 0 < φsΛ.1.card) (hc : φsΛ.GradingCompliant) :
    ∃ (i j : Fin φs.length) (h : i < j) (φsucΛ : WickContraction [singleton h]ᵘᶜ.length),
    φsΛ = join (singleton h) φsucΛ ∧ (𝓕 |>ₛ φs[i]) = (𝓕 |>ₛ φs[j])
    ∧ φsucΛ.GradingCompliant ∧ φsucΛ.1.card + 1 = φsΛ.1.card
```

**`WickContraction.join_not_gradingCompliant_of_left_not_gradingCompliant`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean#L600).

```lean
lemma join_not_gradingCompliant_of_left_not_gradingCompliant {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (φsucΛ : WickContraction [φsΛ]ᵘᶜ.length)
    (hc : ¬ φsΛ.GradingCompliant) : ¬ (join φsΛ φsucΛ).GradingCompliant
```

## Depends on

- [Singleton of contractions](wickcontraction-singleton.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Join.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Join.lean)
