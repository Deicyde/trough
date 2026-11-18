---
catalog: module
lean: Relation.emptyHRelation_emptyRelation, Relation.emptyHrelation_apply, Relation.mem_dom, Relation.mem_cod, Relation.of_dom, Relation.of_cod, Relation.dom_mono, Relation.cod_mono, Relation.dom_empty, Relation.cod_empty, Relation.dom_eq_empty_iff, Relation.cod_eq_empty_iff, Relation.cod_inv, Relation.dom_inv, Std.Trichotomous.subsingleton_cod, Std.Trichotomous.subsingleton_dom
statement: formalized
proof: formalized
---

# Relations: Domain and Codomain

`Cslib.Foundations.Relation.Domain`, in [Cslib/Foundations/Relation/Domain.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

> This module proves basic properties of the domain and codomain of relations.
>
> ## References
>
> * [*Simple Laws about Nonprominent Properties of Binary Relations*][Burghardt2018]

`Relation.emptyHRelation_emptyRelation` (theorem, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L27))

```lean
theorem emptyHRelation_emptyRelation : (emptyHRelation : α → α → Prop) = emptyRelation
```

`Relation.emptyHrelation_apply` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L30))

```lean
theorem emptyHrelation_apply (a : α) (b : β) : emptyHRelation a b ↔ False
```

`Relation.mem_dom` (lemma, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L34))

```lean
lemma mem_dom : a ∈ dom r ↔ ∃ b, r a b
```

`Relation.mem_cod` (lemma, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L35))

```lean
lemma mem_cod : b ∈ cod r ↔ ∃ a, r a b
```

`Relation.of_dom` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L37))

```lean
theorem of_dom (hab : r a b) : a ∈ dom r
```

`Relation.of_cod` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L38))

```lean
theorem of_cod (hab : r a b) : b ∈ cod r
```

`Relation.dom_mono` (lemma, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L40))

```lean
lemma dom_mono (h : r₁ ≤ r₂) : dom r₁ ⊆ dom r₂
```

`Relation.cod_mono` (lemma, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L41))

```lean
lemma cod_mono (h : r₁ ≤ r₂) : cod r₁ ⊆ cod r₂
```

`Relation.dom_empty` (lemma, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L44))

```lean
lemma dom_empty : dom (emptyHRelation : α → β → Prop) = ∅
```

`Relation.cod_empty` (lemma, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L47))

```lean
lemma cod_empty : cod (emptyHRelation : α → β → Prop) = ∅
```

`Relation.dom_eq_empty_iff` (lemma, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L50))

```lean
lemma dom_eq_empty_iff : dom r = ∅ ↔ r = emptyHRelation
```

`Relation.cod_eq_empty_iff` (lemma, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L57))

```lean
lemma cod_eq_empty_iff : cod r = ∅ ↔ r = emptyHRelation
```

`Relation.cod_inv` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L64))

```lean
lemma cod_inv : cod (fun a b => r b a) = dom r
```

`Relation.dom_inv` (lemma, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L67))

```lean
lemma dom_inv : dom (fun a b => r b a) = cod r
```

`Std.Trichotomous.subsingleton_cod` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L69))

```lean
theorem _root_.Std.Trichotomous.subsingleton_cod (r : α → α → Prop) [Std.Trichotomous r] :
    Subsingleton ((cod r)ᶜ : Set α)
```

`Std.Trichotomous.subsingleton_dom` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean#L76))

```lean
theorem _root_.Std.Trichotomous.subsingleton_dom (r : α → α → Prop) [Std.Trichotomous r] :
    Subsingleton ((dom r)ᶜ : Set α)
```

## Depends on

- [Relations: Definitions](defs.md)

## Sources

- [Cslib/Foundations/Relation/Domain.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Domain.lean)
