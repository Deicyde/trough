---
catalog: module
lean: SetRel.map, SetRel.mem_map, SetRel.map_mem_map, SetRel.map_inv, SetRel.map_subset_map, SetRel.map_subset_map_iff, SetRel.map_union, SetRel.map_inter_of_injective_prodMap, SetRel.map_inter_of_injective, SetRel.map_bot, SetRel.map_top_of_surjective_prodMap, SetRel.map_top_of_surjective, SetRel.map_id_of_surjective, SetRel.map_comp_of_injective, SetRel.map_id_fun, SetRel.map_comp_fun, SetRel.mapEquiv, SetRel.ofSet, SetRel.mem_ofSet, SetRel.mem_ofSet', SetRel.mem_ofSet_self_iff, SetRel.dom_ofSet, SetRel.cod_ofSet, SetRel.ofSet_injective, SetRel.ofSet_inj, SetRel.ofSet_subset_ofSet_iff, SetRel.eq_of_mem_ofSet, SetRel.left_mem_of_mem_ofSet, SetRel.right_mem_of_mem_ofSet, SetRel.ofSet_compl_eq, SetRel.ofSet_eq_id_iff, SetRel.ofSet_dom_comp_self, SetRel.self_comp_ofSet_cod, SetRel.mem_ofSet_comp_iff, SetRel.mem_comp_ofSet_iff, SetRel.comp_ofSet_eq_self_iff, SetRel.ofSet_comp_eq_self_iff
statement: formalized
proof: formalized
---

# Set-based relations

`Cslib.Foundations.Data.SetRel`, in [Cslib/Foundations/Data/SetRel.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean), by Thomas Waring.

`SetRel.map` (definition, [line 23](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L23))

> Map set-based relations along a pair of functions.

```lean
protected def map (f : α → α') (g : β → β') (r : SetRel α β) : SetRel α' β'
```

`SetRel.mem_map` (lemma, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L25))

```lean
lemma mem_map : c ~[r.map f g] d ↔ ∃ a b, a ~[r] b ∧ f a = c ∧ g b = d
```

`SetRel.map_mem_map` (lemma, [line 28](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L28))

```lean
lemma map_mem_map (h : a ~[r] b) : f a ~[r.map f g] g b
```

`SetRel.map_inv` (lemma, [line 30](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L30))

```lean
lemma map_inv : (s.map f g).inv = s.inv.map g f
```

`SetRel.map_subset_map` (lemma, [line 32](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L32))

```lean
lemma map_subset_map (h : s ⊆ r) : s.map f g ⊆ r.map f g
```

`SetRel.map_subset_map_iff` (lemma, [line 34](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L34))

```lean
lemma map_subset_map_iff (hf : f.Injective) (hg : g.Injective) :
    s.map f g ⊆ r.map f g ↔ s ⊆ r
```

`SetRel.map_union` (lemma, [line 37](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L37))

```lean
lemma map_union : (s ∪ r).map f g = s.map f g ∪ r.map f g
```

`SetRel.map_inter_of_injective_prodMap` (lemma, [line 39](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L39))

```lean
lemma map_inter_of_injective_prodMap (h : (Prod.map f g).Injective) :
    (s ∩ r).map f g = s.map f g ∩ r.map f g
```

`SetRel.map_inter_of_injective` (lemma, [line 43](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L43))

```lean
lemma map_inter_of_injective (hf : f.Injective) (hg : g.Injective) :
    (s ∩ r).map f g = s.map f g ∩ r.map f g
```

`SetRel.map_bot` (lemma, [line 47](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L47))

```lean
lemma map_bot : (∅ : SetRel α β).map f g = ⊥
```

`SetRel.map_top_of_surjective_prodMap` (lemma, [line 51](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L51))

```lean
lemma map_top_of_surjective_prodMap (h : (Prod.map f g).Surjective) :
    (⊤ : SetRel α β).map f g = ⊤
```

`SetRel.map_top_of_surjective` (lemma, [line 54](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L54))

```lean
lemma map_top_of_surjective (hf : f.Surjective) (hg : g.Surjective) :
    (⊤ : SetRel α β).map f g = ⊤
```

`SetRel.map_id_of_surjective` (lemma, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L57))

```lean
lemma map_id_of_surjective (hf : f.Surjective) :
    (.id : SetRel α α).map f f = SetRel.id
```

`SetRel.map_comp_of_injective` (lemma, [line 62](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L62))

```lean
lemma map_comp_of_injective (hg : g.Injective) {s : SetRel α β} {r : SetRel β γ} :
    (s ○ r).map f h = s.map f g ○ r.map g h
```

`SetRel.map_id_fun` (lemma, [line 68](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L68))

```lean
lemma map_id_fun : s.map id id = s
```

`SetRel.map_comp_fun` (lemma, [line 70](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L70))

```lean
lemma map_comp_fun {α₁ α₂ α₃ β₁ β₂ β₃ : Type*} {f₁ : α₁ → α₂} {f₂ : α₂ → α₃} {g₁ : β₁ → β₂}
    {g₂ : β₂ → β₃} {s : SetRel α₁ β₁} : (s.map f₁ g₁).map f₂ g₂ = s.map (f₂ ∘ f₁) (g₂ ∘ g₁)
```

`SetRel.mapEquiv` (definition, [line 76](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L76))

> Equivalences between types lift the their types of set-based relations.

```lean
def mapEquiv (eα : α ≃ α') (eβ : β ≃ β') : SetRel α β ≃ SetRel α' β'
```

`SetRel.ofSet` (definition, [line 87](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L87))

> Encode a `s` set as a relation, by relating each element of `s` to itself.

```lean
def ofSet (s : Set α) : SetRel α α
```

`SetRel.mem_ofSet` (lemma, [line 89](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L89))

```lean
lemma mem_ofSet : x ~[ofSet s] y ↔ x = y ∧ x ∈ s
```

`SetRel.mem_ofSet'` (lemma, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L91))

```lean
lemma mem_ofSet' : x ~[ofSet s] y ↔ x = y ∧ y ∈ s
```

`SetRel.mem_ofSet_self_iff` (lemma, [line 93](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L93))

```lean
lemma mem_ofSet_self_iff : x ~[ofSet s] x ↔ x ∈ s
```

`SetRel.dom_ofSet` (lemma, [line 95](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L95))

```lean
lemma dom_ofSet : (ofSet s).dom = s
```

`SetRel.cod_ofSet` (lemma, [line 97](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L97))

```lean
lemma cod_ofSet : (ofSet s).cod = s
```

`SetRel.ofSet_injective` (lemma, [line 99](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L99))

```lean
lemma ofSet_injective : Function.Injective (α := Set α) ofSet
```

`SetRel.ofSet_inj` (lemma, [line 103](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L103))

```lean
lemma ofSet_inj {s t : Set α} : ofSet s = ofSet t ↔ s = t
```

`SetRel.ofSet_subset_ofSet_iff` (lemma, [line 105](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L105))

```lean
lemma ofSet_subset_ofSet_iff {s t : Set α} : ofSet s ⊆ ofSet t ↔ s ⊆ t
```

`SetRel.eq_of_mem_ofSet` (lemma, [line 108](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L108))

```lean
lemma eq_of_mem_ofSet (h : x ~[ofSet s] y) : x = y
```

`SetRel.left_mem_of_mem_ofSet` (lemma, [line 110](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L110))

```lean
lemma left_mem_of_mem_ofSet (h : x ~[ofSet s] y) : x ∈ s
```

`SetRel.right_mem_of_mem_ofSet` (lemma, [line 112](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L112))

```lean
lemma right_mem_of_mem_ofSet (h : x ~[ofSet s] y) : y ∈ s
```

`SetRel.ofSet_compl_eq` (lemma, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L114))

```lean
lemma ofSet_compl_eq {s : Set α} : ofSet sᶜ = .id \ ofSet s
```

`SetRel.ofSet_eq_id_iff` (lemma, [line 117](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L117))

```lean
lemma ofSet_eq_id_iff {s : Set α} : ofSet s = .id ↔ s = .univ
```

`SetRel.ofSet_dom_comp_self` (lemma, [line 120](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L120))

```lean
lemma ofSet_dom_comp_self (r : SetRel α α) : ofSet r.dom ○ r = r
```

`SetRel.self_comp_ofSet_cod` (lemma, [line 123](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L123))

```lean
lemma self_comp_ofSet_cod (r : SetRel α α) : r ○ ofSet r.cod = r
```

`SetRel.mem_ofSet_comp_iff` (lemma, [line 126](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L126))

```lean
lemma mem_ofSet_comp_iff : x ~[ofSet s ○ r] y ↔ x ∈ s ∧ x ~[r] y
```

`SetRel.mem_comp_ofSet_iff` (lemma, [line 128](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L128))

```lean
lemma mem_comp_ofSet_iff : x ~[r ○ ofSet s] y ↔ y ∈ s ∧ x ~[r] y
```

`SetRel.comp_ofSet_eq_self_iff` (lemma, [line 130](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L130))

```lean
lemma comp_ofSet_eq_self_iff : ofSet s ○ r = r ↔ r.dom ⊆ s
```

`SetRel.ofSet_comp_eq_self_iff` (lemma, [line 133](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean#L133))

```lean
lemma ofSet_comp_eq_self_iff : r ○ ofSet s = r ↔ r.cod ⊆ s
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/SetRel.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/SetRel.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Data.SetRel.json)
