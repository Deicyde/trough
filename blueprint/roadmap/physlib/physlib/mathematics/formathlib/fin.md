---
declaration: module
origin: cited
lean: Physlib.Fin.predAboveI, Physlib.Fin.predAboveI_self, Physlib.Fin.predAboveI_succAbove, Physlib.Fin.succsAbove_predAboveI, Physlib.Fin.predAboveI_eq_iff, Physlib.Fin.predAboveI_lt, Physlib.Fin.predAboveI_ge, Physlib.Fin.succAbove_succAbove_predAboveI
statement: formalized
proof: formalized
---

# Fin lemmas

The module `Physlib.Mathematics.ForMathlib.Fin`, [Physlib/Mathematics/ForMathlib/Fin.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean): 37 declarations, 7 with a docstring.

> The purpose of this file is to define some results Fin currently
> in Mathlib.
>
> At some point these should either be up-streamed to Mathlib or replaced with definitions already
> in Mathlib.

**`Physlib.Fin.predAboveI`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L29).

> Given a `i` and `x` in `Fin n.succ.succ` returns an element of `Fin n.succ`
> subtracting 1 if `i.val ≤ x.val` else casting x.

```lean
def predAboveI (i x : Fin n.succ.succ) : Fin n.succ
```

**`Physlib.Fin.predAboveI_self`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L35).

```lean
lemma predAboveI_self (i : Fin n.succ.succ) : predAboveI i i = ⟨i.val - 1, by omega⟩
```

**`Physlib.Fin.predAboveI_succAbove`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L39).

```lean
lemma predAboveI_succAbove (i : Fin n.succ.succ) (x : Fin n.succ) :
    predAboveI i (Fin.succAbove i x) = x
```

**`Physlib.Fin.succsAbove_predAboveI`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L45).

```lean
lemma succsAbove_predAboveI {i x : Fin n.succ.succ} (h : i ≠ x) :
    Fin.succAbove i (predAboveI i x) = x
```

**`Physlib.Fin.predAboveI_eq_iff`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L52).

```lean
lemma predAboveI_eq_iff {i x : Fin n.succ.succ} (h : i ≠ x) (y : Fin n.succ) :
    y = predAboveI i x ↔ i.succAbove y = x
```

**`Physlib.Fin.predAboveI_lt`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L59).

```lean
lemma predAboveI_lt {i x : Fin n.succ.succ} (h : x.val < i.val) :
    predAboveI i x = ⟨x.val, by omega⟩
```

**`Physlib.Fin.predAboveI_ge`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L63).

```lean
lemma predAboveI_ge {i x : Fin n.succ.succ} (h : i.val < x.val) :
    predAboveI i x = ⟨x.val - 1, by omega⟩
```

**`Physlib.Fin.succAbove_succAbove_predAboveI`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L68).

```lean
lemma succAbove_succAbove_predAboveI (i : Fin n.succ.succ) (j : Fin n.succ) (x : Fin n) :
    i.succAbove (j.succAbove x) =
    (i.succAbove j).succAbove ((predAboveI (i.succAbove j) i).succAbove x)
```

**`Physlib.Fin.finExtractOne`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L77).

> The equivalence between `Fin n.succ` and `Fin 1 ⊕ Fin n` extracting the
> `i`th component.

```lean
def finExtractOne {n : ℕ} (i : Fin (n + 1)) : Fin (n + 1) ≃ Fin 1 ⊕ Fin n
```

**`Physlib.Fin.finExtractOne_apply_eq`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L86).

```lean
lemma finExtractOne_apply_eq {n : ℕ} (i : Fin n.succ) :
    finExtractOne i i = Sum.inl 0
```

**`Physlib.Fin.finExtractOne_symm_inr`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L91).

```lean
lemma finExtractOne_symm_inr {n : ℕ} (i : Fin n.succ) :
    (finExtractOne i).symm ∘ Sum.inr = i.succAbove
```

**`Physlib.Fin.finExtractOne_symm_inr_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L135).

```lean
lemma finExtractOne_symm_inr_apply {n : ℕ} (i : Fin n.succ) (x : Fin n) :
    (finExtractOne i).symm (Sum.inr x) = i.succAbove x
```

**`Physlib.Fin.finExtractOne_symm_inl_apply`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L141).

```lean
lemma finExtractOne_symm_inl_apply {n : ℕ} (i : Fin n.succ) :
    (finExtractOne i).symm (Sum.inl 0) = i
```

**`Physlib.Fin.finExtractOne_apply_neq`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L145).

```lean
lemma finExtractOne_apply_neq {n : ℕ} (i j : Fin (n + 1 + 1)) (hij : i ≠ j) :
    finExtractOne i j = Sum.inr (predAboveI i j)
```

**`Physlib.Fin.finExtractOnPermHom`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L154).

> Given an equivalence `Fin n.succ.succ ≃ Fin n.succ.succ`, and an `i : Fin n.succ.succ`,
> the map `Fin n.succ → Fin n.succ` obtained by dropping `i` and it's image.

```lean
def finExtractOnPermHom {m : ℕ} (i : Fin n.succ.succ) (σ : Fin n.succ.succ ≃ Fin m.succ.succ) :
    Fin n.succ → Fin m.succ
```

**`Physlib.Fin.finExtractOnPermHom_inv`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L157).

```lean
lemma finExtractOnPermHom_inv {m : ℕ} (i : Fin n.succ.succ)
    (σ : Fin n.succ.succ ≃ Fin m.succ.succ) :
    (finExtractOnPermHom (σ i) σ.symm) ∘ (finExtractOnPermHom i σ) = id
```

**`Physlib.Fin.finExtractOnePerm`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L167).

> Given an equivalence `Fin n.succ.succ ≃ Fin n.succ.succ`, and an `i : Fin n.succ.succ`,
> the equivalence `Fin n.succ ≃ Fin n.succ` obtained by dropping `i` and it's image.

```lean
def finExtractOnePerm {m : ℕ} (i : Fin n.succ.succ) (σ : Fin n.succ.succ ≃ Fin m.succ.succ) :
    Fin n.succ ≃ Fin m.succ
```

**`Physlib.Fin.finExtractOnePerm_equiv`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L174).

```lean
lemma finExtractOnePerm_equiv {n m : ℕ} (e : Fin n.succ.succ ≃ Fin m.succ.succ)
    (i : Fin n.succ.succ) :
    e ∘ i.succAbove = (e i).succAbove ∘ finExtractOnePerm i e
```

**`Physlib.Fin.finExtractOnePerm_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L183).

```lean
lemma finExtractOnePerm_apply (i : Fin n.succ.succ) (σ : Fin n.succ.succ ≃ Fin n.succ.succ)
    (x : Fin n.succ) : finExtractOnePerm i σ x = predAboveI (σ i)
    (σ ((finExtractOne i).symm (Sum.inr x)))
```

**`Physlib.Fin.finExtractOnePerm_symm_apply`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L188).

```lean
lemma finExtractOnePerm_symm_apply (i : Fin n.succ.succ) (σ : Fin n.succ.succ ≃ Fin n.succ.succ)
    (x : Fin n.succ) : (finExtractOnePerm i σ).symm x = predAboveI (σ.symm (σ i))
    (σ.symm ((finExtractOne (σ i)).symm (Sum.inr x)))
```

**`Physlib.Fin.finExtractTwo`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L194).

> The equivalence of types `Fin n.succ.succ ≃ (Fin 1 ⊕ Fin 1) ⊕ Fin n` extracting
> the `i` and `(i.succAbove j)`.

```lean
def finExtractTwo {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    Fin n.succ.succ ≃ (Fin 1 ⊕ Fin 1) ⊕ Fin n
```

**`Physlib.Fin.finExtractTwo_apply_fst`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L201).

```lean
lemma finExtractTwo_apply_fst {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    finExtractTwo i j i = Sum.inl (Sum.inl 0)
```

**`Physlib.Fin.finExtractTwo_symm_inr`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L205).

```lean
lemma finExtractTwo_symm_inr {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    (finExtractTwo i j).symm ∘ Sum.inr = i.succAbove ∘ j.succAbove
```

**`Physlib.Fin.finExtractTwo_symm_inr_apply`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L211).

```lean
lemma finExtractTwo_symm_inr_apply {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) (x : Fin n) :
    (finExtractTwo i j).symm (Sum.inr x) = i.succAbove (j.succAbove x)
```

**`Physlib.Fin.finExtractTwo_symm_inl_inr_apply`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L216).

```lean
lemma finExtractTwo_symm_inl_inr_apply {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    (finExtractTwo i j).symm (Sum.inl (Sum.inr 0)) = i.succAbove j
```

**`Physlib.Fin.finExtractTwo_symm_inl_inl_apply`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L221).

```lean
lemma finExtractTwo_symm_inl_inl_apply {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    (finExtractTwo i j).symm (Sum.inl (Sum.inl 0)) = i
```

**`Physlib.Fin.finExtractTwo_apply_snd`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L225).

```lean
lemma finExtractTwo_apply_snd {n : ℕ} (i : Fin n.succ.succ) (j : Fin n.succ) :
    finExtractTwo i j (i.succAbove j) = Sum.inl (Sum.inr 0)
```

**`Physlib.Fin.finMapToEquiv`**, a def, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L230).

> Takes two maps `Fin n → Fin n` and returns the equivalence they form.

```lean
def finMapToEquiv (f1 : Fin n → Fin m) (f2 : Fin m → Fin n)
    (h : ∀ x, f1 (f2 x) = x := by decide)
    (h' : ∀ x, f2 (f1 x) = x := by decide) : Fin n ≃ Fin m
```

**`Physlib.Fin.finMapToEquiv_apply`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L239).

```lean
lemma finMapToEquiv_apply {f1 : Fin n → Fin m} {f2 : Fin m → Fin n}
    {h : ∀ x, f1 (f2 x) = x} {h' : ∀ x, f2 (f1 x) = x} (x : Fin n) :
    finMapToEquiv f1 f2 h h' x = f1 x
```

**`Physlib.Fin.finMapToEquiv_symm_apply`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L244).

```lean
lemma finMapToEquiv_symm_apply {f1 : Fin n → Fin m} {f2 : Fin m → Fin n}
    {h : ∀ x, f1 (f2 x) = x} {h' : ∀ x, f2 (f1 x) = x} (x : Fin m) :
    (finMapToEquiv f1 f2 h h').symm x = f2 x
```

**`Physlib.Fin.finMapToEquiv_symm_eq`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L248).

```lean
lemma finMapToEquiv_symm_eq {f1 : Fin n → Fin m} {f2 : Fin m → Fin n}
    {h : ∀ x, f1 (f2 x) = x} {h' : ∀ x, f2 (f1 x) = x} :
    (finMapToEquiv f1 f2 h h').symm = finMapToEquiv f2 f1 h' h
```

**`Physlib.Fin.equivCons`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L254).

> Given an equivalence between `Fin n` and `Fin m`, the induced equivalence between
> `Fin n.succ` and `Fin m.succ` derived by `Fin.cons`.

```lean
def equivCons {n m : ℕ} (e : Fin n ≃ Fin m) : Fin n.succ ≃ Fin m.succ
```

**`Physlib.Fin.equivCons_zero`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L261).

```lean
lemma equivCons_zero {n m : ℕ} (e : Fin n ≃ Fin m) :
    equivCons e 0 = 0
```

**`Physlib.Fin.equivCons_trans`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L265).

```lean
lemma equivCons_trans {n m k : ℕ} (e : Fin n ≃ Fin m) (f : Fin m ≃ Fin k) :
    Fin.equivCons (e.trans f) = (Fin.equivCons e).trans (Fin.equivCons f)
```

**`Physlib.Fin.equivCons_castOrderIso`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L271).

```lean
lemma equivCons_castOrderIso {n m : ℕ} (h : n = m) :
    (Fin.equivCons (Fin.castOrderIso h).toEquiv) = (Fin.castOrderIso (by simp [h])).toEquiv
```

**`Physlib.Fin.equivCons_symm_succ`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L277).

```lean
lemma equivCons_symm_succ {n m : ℕ} (e : Fin n ≃ Fin m) (i : ℕ) (hi : i + 1 < m.succ) :
    (Fin.equivCons e).symm ⟨i + 1, hi⟩ = (e.symm ⟨i, Nat.succ_lt_succ_iff.mp hi⟩).succ
```

**`Physlib.Fin.equivCons_succ`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean#L281).

```lean
lemma equivCons_succ {n m : ℕ} (e : Fin n ≃ Fin m) (i : ℕ) (hi : i + 1 < n.succ) :
    (Fin.equivCons e) ⟨i + 1, hi⟩ = (e ⟨i, Nat.succ_lt_succ_iff.mp hi⟩).succ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Fin.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin.lean)
