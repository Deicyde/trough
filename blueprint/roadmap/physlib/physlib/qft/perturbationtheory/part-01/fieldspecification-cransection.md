---
declaration: module
origin: cited
lean: FieldSpecification.CrAnSection, FieldSpecification.CrAnSection.length_eq, FieldSpecification.CrAnSection.tail, FieldSpecification.CrAnSection.head_state_eq, FieldSpecification.CrAnSection.statistics_eq_state_statistics, FieldSpecification.CrAnSection.take_statistics_eq_take_state_statistics, FieldSpecification.CrAnSection.head, FieldSpecification.CrAnSection.eq_head_cons_tail
statement: formalized
proof: formalized
---

# Creation and annihilation sections

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.CrAnSection`, [Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean): 47 declarations, 15 with a docstring.

> In the module
> `Physlib.QFT.PerturbationTheory.FieldSpecification.Basic`
> we defined states for a field specification, and in the module
> `Physlib.QFT.PerturbationTheory.FieldStatistics.CrAnFieldOp`
> we defined a refinement of states called `CrAnFieldOp` which distinguishes between the
> creation and annihilation components of states.
> There exists, in particular, a map from `CrAnFieldOp` to `FieldOp` called `crAnFieldOpToFieldOp`.
>
> Given a list of `FieldOp`, `φs`, in this module we define a section of `φs` to be a list of
> `CrAnFieldOp`, `ψs`, such that under the map `crAnFieldOpToFieldOp`, `ψs` is mapped to `φs`.
> That is to say, the states underlying `ψs` are the states in `φs`.
> We denote these sections as `CrAnSection φs`.
>
> Looking forward the main consequence of this definition is the lemma
> `FieldSpecification.FieldOpFreeAlgebra.ofFieldOpListF_sum`.
>
> In this module we define various properties of `CrAnSection`.

**`FieldSpecification.CrAnSection`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L44).

> The sections in `𝓕.CrAnFieldOp` over a list `φs : List 𝓕.FieldOp`.
> In terms of physics, given some fields `φ₁...φₙ`, the different ways one can associate
> each field as a `creation` or an `annilation` operator. E.g. the number of terms
> `φ₁⁰φ₂¹...φₙ⁰` `φ₁¹φ₂¹...φₙ⁰` etc. If some fields are exclusively creation or annihilation
> operators at this point (e.g. asymptotic states) this is accounted for.

```lean
def CrAnSection (φs : List 𝓕.FieldOp) : Type
```

**`FieldSpecification.CrAnSection.length_eq`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L53).

```lean
lemma length_eq (ψs : CrAnSection φs) : ψs.1.length = φs.length
```

**`FieldSpecification.CrAnSection.tail`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L57).

> The tail of a section for `φs`.

```lean
def tail : {φs : List 𝓕.FieldOp} → (ψs : CrAnSection φs) → CrAnSection φs.tail
```

**`FieldSpecification.CrAnSection.head_state_eq`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L62).

```lean
lemma head_state_eq {φ : 𝓕.FieldOp} : (ψs : CrAnSection (φ :: φs)) →
    (ψs.1.head (by simp [← List.length_pos_iff_ne_nil])).1 = φ
```

**`FieldSpecification.CrAnSection.statistics_eq_state_statistics`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L69).

```lean
lemma statistics_eq_state_statistics (ψs : CrAnSection φs) :
    (𝓕 |>ₛ ψs.1) = 𝓕 |>ₛ φs
```

**`FieldSpecification.CrAnSection.take_statistics_eq_take_state_statistics`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L74).

```lean
lemma take_statistics_eq_take_state_statistics (ψs : CrAnSection φs) n :
    (𝓕 |>ₛ (ψs.1.take n)) = 𝓕 |>ₛ (φs.take n)
```

**`FieldSpecification.CrAnSection.head`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L81).

> The head of a section for `φ :: φs` as an element in `𝓕.fieldOpToCreateAnnihilateType φ`.

```lean
def head : {φ : 𝓕.FieldOp} → (ψs : CrAnSection (φ :: φs)) →
    𝓕.fieldOpToCrAnType φ
```

**`FieldSpecification.CrAnSection.eq_head_cons_tail`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L87).

```lean
lemma eq_head_cons_tail {φ : 𝓕.FieldOp} {ψs : CrAnSection (φ :: φs)} :
    ψs.1 = ⟨φ, head ψs⟩ :: ψs.tail.1
```

**`FieldSpecification.CrAnSection.cons`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L100).

> The creation of a section from for `φ : φs` from a section for `φs` and a
> element of `𝓕.fieldOpToCreateAnnihilateType φ`.

```lean
def cons {φ : 𝓕.FieldOp} (ψ : 𝓕.fieldOpToCrAnType φ) (ψs : CrAnSection φs) :
    CrAnSection (φ :: φs)
```

**`FieldSpecification.CrAnSection.nilEquiv`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L106).

> For the empty list of states there is only one `CrAnSection`. Corresponding to the
> empty list of `CrAnFieldOp`.

```lean
def nilEquiv : CrAnSection (𝓕 := 𝓕) [] ≃ Unit
```

**`FieldSpecification.CrAnSection.singletonEquiv`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L120).

> The creation and annihilation sections for a singleton list is given by
> a choice of `𝓕.fieldOpToCreateAnnihilateType φ`. If `φ` is a asymptotic state
> there is no choice here, else there are two choices.

```lean
def singletonEquiv {φ : 𝓕.FieldOp} : CrAnSection [φ] ≃
    𝓕.fieldOpToCrAnType φ
```

**`FieldSpecification.CrAnSection.consEquiv`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L138).

> An equivalence separating the head of a creation and annihilation section
> from the tail.

```lean
def consEquiv {φ : 𝓕.FieldOp} {φs : List 𝓕.FieldOp} : CrAnSection (φ :: φs) ≃
    𝓕.fieldOpToCrAnType φ × CrAnSection φs
```

**`FieldSpecification.CrAnSection.fintype`**, an instance, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L153).

> The instance of a finite type on `CrAnSection`s defined recursively through
> `consEquiv`.

```lean
instance fintype : (φs : List 𝓕.FieldOp) → Fintype (CrAnSection φs)
```

**`FieldSpecification.CrAnSection.card_nil_eq`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L160).

```lean
lemma card_nil_eq : Fintype.card (CrAnSection (𝓕 := 𝓕) []) = 1
```

**`FieldSpecification.CrAnSection.card_cons_eq`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L164).

```lean
lemma card_cons_eq {φ : 𝓕.FieldOp} {φs : List 𝓕.FieldOp} :
    Fintype.card (CrAnSection (φ :: φs)) = Fintype.card (𝓕.fieldOpToCrAnType φ) *
    Fintype.card (CrAnSection φs)
```

**`FieldSpecification.CrAnSection.card_eq_mul`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L171).

```lean
lemma card_eq_mul : {φs : List 𝓕.FieldOp} → Fintype.card (CrAnSection φs) =
    2 ^ (List.countP 𝓕.statesIsPosition φs)
```

**`FieldSpecification.CrAnSection.card_perm_eq`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L193).

```lean
lemma card_perm_eq {φs φs' : List 𝓕.FieldOp} (h : φs.Perm φs') :
    Fintype.card (CrAnSection φs) = Fintype.card (CrAnSection φs')
```

**`FieldSpecification.CrAnSection.sum_nil`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L200).

```lean
lemma sum_nil (f : CrAnSection (𝓕 := 𝓕) [] → M) [AddCommMonoid M] :
    ∑ (s : CrAnSection []), f s = f ⟨[], rfl⟩
```

**`FieldSpecification.CrAnSection.sum_cons`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L206).

```lean
lemma sum_cons (f : CrAnSection (φ :: φs) → M) [AddCommMonoid M] :
    ∑ (s : CrAnSection (φ :: φs)), f s = ∑ (a : 𝓕.fieldOpToCrAnType φ),
    ∑ (s : CrAnSection φs), f (cons a s)
```

**`FieldSpecification.CrAnSection.sum_over_length`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L212).

```lean
lemma sum_over_length {s : CrAnSection φs} (f : Fin s.1.length → M)
    [AddCommMonoid M] : ∑ (n : Fin s.1.length), f n =
    ∑ (n : Fin φs.length), f (Fin.cast (length_eq s).symm n)
```

**`FieldSpecification.CrAnSection.congr`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L220).

> The equivalence between `CrAnSection φs` and
> `CrAnSection φs'` induced by an equality `φs = φs'`.

```lean
def congr : {φs φs' : List 𝓕.FieldOp} → (h : φs = φs') →
    CrAnSection φs ≃ CrAnSection φs'
```

**`FieldSpecification.CrAnSection.congr_fst`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L225).

```lean
lemma congr_fst {φs φs' : List 𝓕.FieldOp} (h : φs = φs') (ψs : CrAnSection φs) :
    (congr h ψs).1 = ψs.1
```

**`FieldSpecification.CrAnSection.congr_symm`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L231).

```lean
lemma congr_symm {φs φs' : List 𝓕.FieldOp} (h : φs = φs') :
    (congr h).symm = congr h.symm
```

**`FieldSpecification.CrAnSection.congr_trans_apply`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L237).

```lean
lemma congr_trans_apply {φs φs' φs'' : List 𝓕.FieldOp} (h1 : φs = φs') (h2 : φs' = φs'')
    (ψs : CrAnSection φs) :
    (congr h2 (congr h1 ψs)) = congr (by rw [h1, h2]) ψs
```

**`FieldSpecification.CrAnSection.take`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L244).

> Returns the first `n` elements of a section and its underlying list.

```lean
def take (n : ℕ) (ψs : CrAnSection φs) : CrAnSection (φs.take n)
```

**`FieldSpecification.CrAnSection.take_congr`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L248).

```lean
lemma take_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs') (n : ℕ)
    (ψs : CrAnSection φs) :
    (take n (congr h ψs)) = congr (by rw [h]) (take n ψs)
```

**`FieldSpecification.CrAnSection.drop`**, a def, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L255).

> Removes the first `n` elements of a section and its underlying list.

```lean
def drop (n : ℕ) (ψs : CrAnSection φs) : CrAnSection (φs.drop n)
```

**`FieldSpecification.CrAnSection.drop_congr`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L259).

```lean
lemma drop_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs') (n : ℕ)
    (ψs : CrAnSection φs) :
    (drop n (congr h ψs)) = congr (by rw [h]) (drop n ψs)
```

**`FieldSpecification.CrAnSection.append`**, a def, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L266).

> Appends two sections and their underlying lists.

```lean
def append {φs φs' : List 𝓕.FieldOp} (ψs : CrAnSection φs)
    (ψs' : CrAnSection φs') : CrAnSection (φs ++ φs')
```

**`FieldSpecification.CrAnSection.append_assoc`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L271).

```lean
lemma append_assoc {φs φs' φs'' : List 𝓕.FieldOp} (ψs : CrAnSection φs)
    (ψs' : CrAnSection φs') (ψs'' : CrAnSection φs'') :
    append ψs (append ψs' ψs'') = congr (by simp) (append (append ψs ψs') ψs'')
```

**`FieldSpecification.CrAnSection.append_assoc'`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L278).

```lean
lemma append_assoc' {φs φs' φs'' : List 𝓕.FieldOp} (ψs : CrAnSection φs)
    (ψs' : CrAnSection φs') (ψs'' : CrAnSection φs'') :
    (append (append ψs ψs') ψs'') = congr (by simp) (append ψs (append ψs' ψs''))
```

**`FieldSpecification.CrAnSection.singletonEquiv_append_eq_cons`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L285).

```lean
lemma singletonEquiv_append_eq_cons {φs : List 𝓕.FieldOp} {φ : 𝓕.FieldOp}
    (ψs : CrAnSection φs) (ψ : 𝓕.fieldOpToCrAnType φ) :
    append (singletonEquiv.symm ψ) ψs = cons ψ ψs
```

**`FieldSpecification.CrAnSection.take_append_drop`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L292).

```lean
lemma take_append_drop {n : ℕ} (ψs : CrAnSection φs) :
    append (take n ψs) (drop n ψs) = congr (List.take_append_drop n φs).symm ψs
```

**`FieldSpecification.CrAnSection.congr_append`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L297).

```lean
lemma congr_append {φs1 φs1' φs2 φs2' : List 𝓕.FieldOp} (h1 : φs1 = φs1') (h2 : φs2 = φs2')
    (ψs1 : CrAnSection φs1) (ψs2 : CrAnSection φs2) :
    (append (congr h1 ψs1) (congr h2 ψs2)) = congr (by rw [h1, h2]) (append ψs1 ψs2)
```

**`FieldSpecification.CrAnSection.congr_fst_append`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L304).

```lean
lemma congr_fst_append {φs1 φs1' φs2 : List 𝓕.FieldOp} (h1 : φs1 = φs1')
    (ψs1 : CrAnSection φs1) (ψs2 : CrAnSection φs2) :
    (append (congr h1 ψs1) (ψs2)) = congr (by rw [h1]) (append ψs1 ψs2)
```

**`FieldSpecification.CrAnSection.congr_snd_append`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L311).

```lean
lemma congr_snd_append {φs1 φs2 φs2' : List 𝓕.FieldOp} (h2 : φs2 = φs2')
    (ψs1 : CrAnSection φs1) (ψs2 : CrAnSection φs2) :
    (append ψs1 (congr h2 ψs2)) = congr (by rw [h2]) (append ψs1 ψs2)
```

**`FieldSpecification.CrAnSection.take_left`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L318).

```lean
lemma take_left {φs φs' : List 𝓕.FieldOp} (ψs : CrAnSection φs)
    (ψs' : CrAnSection φs') :
    take φs.length (ψs.append ψs') = congr (by simp) ψs
```

**`FieldSpecification.CrAnSection.drop_left`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L325).

```lean
lemma drop_left {φs φs' : List 𝓕.FieldOp} (ψs : CrAnSection φs)
    (ψs' : CrAnSection φs') :
    drop φs.length (ψs.append ψs') = congr (by simp) ψs'
```

**`FieldSpecification.CrAnSection.appendEquiv`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L334).

> The equivalence between `CrAnSection (φs ++ φs')` and
> `CrAnSection φs × CrAnSection φs` formed by `append`, `take`
> and `drop` and their interrelationship.

```lean
def appendEquiv {φs φs' : List 𝓕.FieldOp} : CrAnSection (φs ++ φs') ≃
    CrAnSection φs × CrAnSection φs'
```

**`List.map_eraseIdx`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L349).

```lean
lemma _root_.List.map_eraseIdx {α β : Type} (f : α → β) : (l : List α) → (n : ℕ) →
    List.map f (l.eraseIdx n) = (List.map f l).eraseIdx n
```

**`FieldSpecification.CrAnSection.eraseIdx`**, a def, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L358).

> Erasing an element from a section and it's underlying list.

```lean
def eraseIdx (n : ℕ) (ψs : CrAnSection φs) : CrAnSection (φs.eraseIdx n)
```

**`FieldSpecification.CrAnSection.eraseIdxEquiv`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L362).

> The equivalence formed by extracting an element from a section.

```lean
def eraseIdxEquiv (n : ℕ) (φs : List 𝓕.FieldOp) (hn : n < φs.length) :
    CrAnSection φs ≃ 𝓕.fieldOpToCrAnType φs[n] ×
    CrAnSection (φs.eraseIdx n)
```

**`FieldSpecification.CrAnSection.eraseIdxEquiv_apply_snd`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L375).

```lean
lemma eraseIdxEquiv_apply_snd {n : ℕ} (ψs : CrAnSection φs) (hn : n < φs.length) :
    (eraseIdxEquiv n φs hn ψs).snd = eraseIdx n ψs
```

**`FieldSpecification.CrAnSection.eraseIdxEquiv_symm_eq_take_cons_drop`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L386).

```lean
lemma eraseIdxEquiv_symm_eq_take_cons_drop {n : ℕ} (φs : List 𝓕.FieldOp) (hn : n < φs.length)
    (a : 𝓕.fieldOpToCrAnType φs[n]) (s : CrAnSection (φs.eraseIdx n)) :
    (eraseIdxEquiv n φs hn).symm ⟨a, s⟩ =
    congr (by
    rw [Physlib.List.take_eraseIdx_same, Physlib.List.drop_eraseIdx_succ]
    conv_rhs => rw [← List.take_append_drop n φs]) (append (take n s) (cons a (drop n s)))
```

**`FieldSpecification.CrAnSection.eraseIdxEquiv_symm_getElem`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L409).

```lean
lemma eraseIdxEquiv_symm_getElem {n : ℕ} (φs : List 𝓕.FieldOp) (hn : n < φs.length)
    (a : 𝓕.fieldOpToCrAnType φs[n]) (s : CrAnSection (φs.eraseIdx n)) :
    getElem ((eraseIdxEquiv n φs hn).symm ⟨a,s⟩).1 n
    (by rw [length_eq]; exact hn) = ⟨φs[n], a⟩
```

**`FieldSpecification.CrAnSection.eraseIdxEquiv_symm_eraseIdx`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L422).

```lean
lemma eraseIdxEquiv_symm_eraseIdx {n : ℕ} (φs : List 𝓕.FieldOp) (hn : n < φs.length)
    (a : 𝓕.fieldOpToCrAnType φs[n]) (s : CrAnSection (φs.eraseIdx n)) :
    ((eraseIdxEquiv n φs hn).symm ⟨a, s⟩).1.eraseIdx n = s.1
```

**`FieldSpecification.CrAnSection.sum_eraseIdxEquiv`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean#L429).

```lean
lemma sum_eraseIdxEquiv (n : ℕ) (φs : List 𝓕.FieldOp) (hn : n < φs.length)
    (f : CrAnSection φs → M) [AddCommMonoid M] : ∑ (s : CrAnSection φs), f s =
    ∑ (a : 𝓕.fieldOpToCrAnType φs[n]), ∑ (s : CrAnSection (φs.eraseIdx n)),
    f ((eraseIdxEquiv n φs hn).symm ⟨a, s⟩)
```

## Depends on

- [Creation and annihilation states](fieldspecification-cranfieldop.md)

## Proof depends on

- [List lemmas (List)](../../../mathematics/formathlib/list.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/CrAnSection.lean)
