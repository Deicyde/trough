---
catalog: module
lean: WellFounded.ofTransGen, WellFounded.iff_transGen, Relation.transLeftRight, Relation.transLeft, Relation.transRight, Relation.comp_le_comp, Relation.comp_self_le, Relation.swap_le_iff_le_swap, Relation.ReflGen.le_reflGen, Relation.ReflGen.to_eqvGen, Relation.TransGen.le_transGen, Relation.TransGen.to_eqvGen, Relation.ReflTransGen.to_eqvGen, Relation.SymmGen.le_symmGen, Relation.SymmGen.to_eqvGen, Relation.sup_swap_eq_symmGen, Relation.EqvGen.le_eqvGen, Equivalence.eqvGen_le, Relation.Join.single, Relation.join₂_eq_join, Relation.join₂_eq_comp_swap, Relation.Join₂.single_left, Relation.Join₂.single_right, Relation.Join₂.join₂_le, Relation.Join₂.swap_iff, Relation.Join₂.mono, Relation.MJoin.refl, Relation.MJoin.single, Equivalence.join_reflTransGen_le, Relation.join_reflTransGen_le_eqvGen, Relation.join₂_reflTransGen_le, Relation.join₂_reflTransGen_le_of_isEquiv, Equivalence.join₂_reflTransGen_le, Relation.left_le_join₂_reflTransGen, Relation.swap_right_le_join₂_reflTransGen, Relation.reflTransGen_mono_closed, Relation.ReflGen.symmGen_symm, Relation.reflTransGen_symmGen, Relation.join_inl, Relation.join_inr, Relation.join_inl_reflTransGen, Relation.join_inr_reflTransGen, Relation.acyclic_le
statement: formalized
proof: formalized
---

# Basic properties of relations

`Cslib.Foundations.Relation.Basic`, in [Cslib/Foundations/Relation/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

> …

`WellFounded.ofTransGen` (theorem, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L24))

```lean
theorem WellFounded.ofTransGen (trans_wf : WellFounded (Relation.TransGen r)) : WellFounded r
```

`WellFounded.iff_transGen` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L28))

```lean
theorem WellFounded.iff_transGen : WellFounded (Relation.TransGen r) ↔ WellFounded r
```

`Relation.transLeftRight` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L37))

> A pair of subrelations lifts to transitivity on the relation.

```lean
def transLeftRight (s s' r : α → α → Prop) [IsTrans α r] (h : s ≤ r) (h' : s' ≤ r) :
    Trans s s' r
```

`Relation.transLeft` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L43))

> A subrelation lifts to transitivity on the left of the relation.

```lean
def transLeft (s r : α → α → Prop) [IsTrans α r] (h : s ≤ r) : Trans s r r
```

`Relation.transRight` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L48))

> A subrelation lifts to transitivity on the right of the relation.

```lean
def transRight (s r : α → α → Prop) [IsTrans α r] (h : s ≤ r) : Trans r s r
```

`Relation.comp_le_comp` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L52))

```lean
theorem comp_le_comp {s s' r r' : α → α → Prop} (hs : s ≤ s') (hr : r ≤ r') :
    Comp s r ≤ Comp s' r'
```

`Relation.comp_self_le` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L55))

```lean
theorem comp_self_le (r : α → α → Prop) [IsTrans α r] : Comp r r ≤ r
```

`Relation.swap_le_iff_le_swap` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L58))

```lean
theorem swap_le_iff_le_swap {r₁ r₂ : α → α → Prop} : swap r₁ ≤ r₂ ↔ r₁ ≤ swap r₂
```

`Relation.ReflGen.le_reflGen` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L64))

```lean
theorem ReflGen.le_reflGen : r ≤ ReflGen r
```

`Relation.ReflGen.to_eqvGen` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L66))

```lean
theorem ReflGen.to_eqvGen (h : ReflGen r a b) : EqvGen r a b
```

`Relation.TransGen.le_transGen` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L70))

```lean
theorem TransGen.le_transGen : r ≤ TransGen r
```

`Relation.TransGen.to_eqvGen` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L72))

```lean
theorem TransGen.to_eqvGen (h : TransGen r a b) : EqvGen r a b
```

`Relation.ReflTransGen.to_eqvGen` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L75))

```lean
theorem ReflTransGen.to_eqvGen (h : ReflTransGen r a b) : EqvGen r a b
```

`Relation.SymmGen.le_symmGen` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L79))

```lean
theorem SymmGen.le_symmGen : r ≤ SymmGen r
```

`Relation.SymmGen.to_eqvGen` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L81))

```lean
theorem SymmGen.to_eqvGen (h : SymmGen r a b) : EqvGen r a b
```

`Relation.sup_swap_eq_symmGen` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L84))

```lean
theorem sup_swap_eq_symmGen : r ⊔ Function.swap r = SymmGen r
```

`Relation.EqvGen.le_eqvGen` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L87))

```lean
theorem EqvGen.le_eqvGen : r ≤ EqvGen r
```

`Equivalence.eqvGen_le` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L89))

```lean
theorem _root_.Equivalence.eqvGen_le (h : Equivalence r₂) (hle : r₁ ≤ r₂) : EqvGen r₁ ≤ r₂
```

`Relation.Join.single` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L96))

```lean
theorem Join.single [Std.Refl r] (h : r a b) : Join r a b
```

`Relation.join₂_eq_join` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L98))

```lean
theorem join₂_eq_join : Join₂ r r = Join r
```

`Relation.join₂_eq_comp_swap` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L100))

```lean
theorem join₂_eq_comp_swap : Join₂ r₁ r₂ = Comp r₁ (swap r₂)
```

`Relation.Join₂.single_left` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L105))

```lean
theorem Join₂.single_left [Std.Refl r₂] (h : r₁ a b) : Join₂ r₁ r₂ a b
```

`Relation.Join₂.single_right` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L107))

```lean
theorem Join₂.single_right [Std.Refl r₁] (h : r₂ a b) : Join₂ r₁ r₂ b a
```

`Relation.Join₂.join₂_le` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L109))

```lean
theorem Join₂.join₂_le [IsTrans α r] (h₁ : r₁ ≤ r) (h₂ : swap r₂ ≤ r) : Join₂ r₁ r₂ ≤ r
```

`Relation.Join₂.swap_iff` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L112))

```lean
theorem Join₂.swap_iff {a b : α} : Join₂ r₁ r₂ b a ↔ Join₂ r₂ r₁ a b
```

`Relation.Join₂.mono` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L114))

```lean
protected theorem Join₂.mono (h₁ : r₁ ≤ r₁') (h₂ : r₂ ≤ r₂') : Join₂ r₁ r₂ ≤ Join₂ r₁' r₂'
```

`Relation.MJoin.refl` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L118))

```lean
theorem MJoin.refl (a : α) : MJoin r a a
```

`Relation.MJoin.single` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L121))

```lean
theorem MJoin.single (h : ReflTransGen r a b) : MJoin r a b
```

`Equivalence.join_reflTransGen_le` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L123))

```lean
theorem _root_.Equivalence.join_reflTransGen_le (h : Equivalence r₂) (hle : r₁ ≤ r₂) :
    Join (ReflTransGen r₁) ≤ r₂
```

`Relation.join_reflTransGen_le_eqvGen` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L128))

```lean
theorem join_reflTransGen_le_eqvGen : Join (ReflTransGen r) ≤ EqvGen r
```

`Relation.join₂_reflTransGen_le` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L131))

```lean
theorem join₂_reflTransGen_le [Std.Refl r] [IsTrans α r] (h₁ : r₁ ≤ r) (h₂ : swap r₂ ≤ r) :
    Join₂ (ReflTransGen r₁) (ReflTransGen r₂) ≤ r
```

`Relation.join₂_reflTransGen_le_of_isEquiv` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L136))

```lean
theorem join₂_reflTransGen_le_of_isEquiv [IsEquiv α r] (h₁ : r₁ ≤ r) (h₂ : r₂ ≤ r) :
    Join₂ (ReflTransGen r₁) (ReflTransGen r₂) ≤ r
```

`Equivalence.join₂_reflTransGen_le` (theorem, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L140))

```lean
theorem _root_.Equivalence.join₂_reflTransGen_le (h : Equivalence r) (h₁ : r₁ ≤ r) (h₂ : r₂ ≤ r) :
    Join₂ (ReflTransGen r₁) (ReflTransGen r₂) ≤ r
```

`Relation.left_le_join₂_reflTransGen` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L145))

```lean
theorem left_le_join₂_reflTransGen : r₁ ≤ Join₂ (ReflTransGen r₁) (ReflTransGen r₂)
```

`Relation.swap_right_le_join₂_reflTransGen` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L148))

```lean
theorem swap_right_le_join₂_reflTransGen : swap r₂ ≤ Join₂ (ReflTransGen r₁) (ReflTransGen r₂)
```

`Relation.reflTransGen_mono_closed` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L152))

> If a relation is squeezed by a relation and its multi-step closure, they are multi-step equal

```lean
theorem reflTransGen_mono_closed (h₁ : r₁ ≤ r₂) (h₂ : r₂ ≤ ReflTransGen r₁) :
    ReflTransGen r₁ = ReflTransGen r₂
```

`Relation.ReflGen.symmGen_symm` (lemma, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L158))

```lean
lemma ReflGen.symmGen_symm : ReflGen (SymmGen r) a b → ReflGen (SymmGen r) b a
```

`Relation.reflTransGen_symmGen` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L162))

```lean
theorem reflTransGen_symmGen : ReflTransGen (SymmGen r) = EqvGen r
```

`Relation.join_inl` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L165))

```lean
theorem join_inl (r₁_ab : r₁ a b) : (r₁ ⊔ r₂) a b
```

`Relation.join_inr` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L169))

```lean
theorem join_inr (r₂_ab : r₂ a b) : (r₁ ⊔ r₂) a b
```

`Relation.join_inl_reflTransGen` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L173))

```lean
theorem join_inl_reflTransGen (r₁_ab : ReflTransGen r₁ a b) : ReflTransGen (r₁ ⊔ r₂) a b
```

`Relation.join_inr_reflTransGen` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L177))

```lean
theorem join_inr_reflTransGen (r₂_ab : ReflTransGen r₂ a b) : ReflTransGen (r₁ ⊔ r₂) a b
```

`Relation.acyclic_le` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean#L180))

```lean
theorem acyclic_le {r s : α → α → Prop}
    (hle : r ≤ s) (ha : Acyclic s) : Acyclic r
```

## Depends on

- [Relations: Definitions](defs.md)

## Sources

- [Cslib/Foundations/Relation/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Basic.lean)
