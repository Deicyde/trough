---
declaration: module
origin: cited
lean: ite_eq_top, subtype_val_iSup, subtype_val_iSup', subtype_val_iInf, subtype_val_iInf', ENNReal.bdd_le_mul_tendsto_zero, csInf_mul_nonneg, Multiset.map_univ_eq_iff
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Misc

The module `QuantumInfo.ForMathlib.Misc`, [QuantumInfo/ForMathlib/Misc.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean): 9 declarations, 3 with a docstring.

**`ite_eq_top`**, a lemma, [line 16](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L16).

```lean
lemma ite_eq_top {α : Type*} [Top α] (h : Prop) [Decidable h] {x y : α} (hx : x ≠ ⊤) (hy : y ≠ ⊤) :
    (if h then x else y) ≠ ⊤
```

**`subtype_val_iSup`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L45).

```lean
lemma subtype_val_iSup (h : ∀ i, f i ∈ Set.Icc a b) :
    (⨆ i, (⟨f i, h i⟩ : ↑(Set.Icc a b))).val = ⨆ i, f i
```

**`subtype_val_iSup'`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L51).

```lean
lemma subtype_val_iSup' (h : ∀ i, f i ∈ Set.Icc a b) :
    ⨆ i, (⟨f i, h i⟩ : ↑(Set.Icc a b)) =
      ⟨⨆ i, f i, ⟨(h i.some).1.trans (le_ciSup ⟨b, by intro; grind⟩ _), ciSup_le (h ·|>.2)⟩⟩
```

**`subtype_val_iInf`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L58).

```lean
lemma subtype_val_iInf (h : ∀ i, f i ∈ Set.Icc a b) :
    (⨅ i, (⟨f i, h i⟩ : ↑(Set.Icc a b))).val = ⨅ i, f i
```

**`subtype_val_iInf'`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L64).

```lean
lemma subtype_val_iInf' (h : ∀ i, f i ∈ Set.Icc a b) :
    ⨅ i, (⟨f i, h i⟩ : ↑(Set.Icc a b)) =
      ⟨⨅ i, f i, ⟨le_ciInf (h ·|>.1), (ciInf_le ⟨a, by intro; grind⟩ _).trans (h i.some).2⟩⟩
```

**`ENNReal.bdd_le_mul_tendsto_zero`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L75).

> Analogous to `bdd_le_mul_tendsto_zero`, for `ENNReal` (which otherwise lacks a continuous
> multiplication function). The product of a sequence that tends to zero with any bounded sequence
> also tends to zero.

```lean
protected lemma ENNReal.bdd_le_mul_tendsto_zero
  {α : Type*} {l : Filter α} {f g : α → ℝ≥0∞} {b : ℝ≥0∞} (hb : b ≠ ⊤)
  (hf : l.Tendsto f (𝓝 0)) (hg : ∀ᶠ (x : α) in l, g x ≤ b) :
    l.Tendsto (fun x ↦ f x * g x) (𝓝 0)
```

**`csInf_mul_nonneg`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L90).

```lean
lemma csInf_mul_nonneg {s t : Set ℝ}
  (hs₀ : s.Nonempty) (hs₁ : ∀ x ∈ s, 0 ≤ x) (ht₀ : t.Nonempty) (ht₁ : ∀ x ∈ t, 0 ≤ x) :
    sInf (s * t) = sInf s * sInf t
```

**`Multiset.map_univ_eq_iff`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L127).

> If two functions from finite types have the same multiset of values, there exists a bijection between the domains that commutes with the functions.

```lean
lemma Multiset.map_univ_eq_iff {α β : Type*} [Fintype α] (f g : α → β) :
    Multiset.map f Finset.univ.val = Multiset.map g Finset.univ.val ↔ ∃ (e : α ≃ α), f = g ∘ e
```

**`exists_equiv_of_multiset_map_eq`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean#L167).

> If two functions from finite types have the same multiset of values, there exists a bijection between the domains that commutes with the functions.

```lean
lemma exists_equiv_of_multiset_map_eq {α β γ : Type*} [Fintype α] [Fintype β] [DecidableEq γ]
    (f : α → γ) (g : β → γ) (h : Multiset.map f Finset.univ.val = Multiset.map g Finset.univ.val) :
    ∃ e : α ≃ β, f = g ∘ e
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/Misc.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Misc.lean)
