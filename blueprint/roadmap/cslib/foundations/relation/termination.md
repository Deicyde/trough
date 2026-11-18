---
catalog: module
lean: Relation.normal_iff, Relation.Normal_iff, Relation.Normal.reflTransGen_eq, Relation.SN_iff_SN_of_rel, Relation.SN.intro, Relation.SN.of_rel, Relation.SN.of_rel_reflTransGen, Relation.SN.transGen, Relation.SN.of_le, Relation.SN.iff_transGen, Relation.SN.iff_isEmpty_chain, Relation.SN.onFun_of_image, Relation.SN.of_normal, Relation.SN.normalizable, Relation.Terminating.apply, Relation.Terminating.iff_forall_sn, Relation.Terminating.to_transGen, Relation.Terminating.toTransGen, Relation.Terminating.to_acyclic, Relation.Terminating.toAcyclic, Relation.Terminating.of_transGen, Relation.Terminating.ofTransGen, Relation.Terminating.iff_transGen, Relation.Terminating.iff_isEmpty_chain, Relation.Terminating.of_le, Relation.Terminating.subtype_sn, Relation.Terminating.to_normalizing, Relation.Terminating.isNormalizing
statement: formalized
proof: formalized
---

# Termination (well-foundedness) properties of relations

`Cslib.Foundations.Relation.Termination`, in [Cslib/Foundations/Relation/Termination.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

`Relation.normal_iff` (theorem, [line 19](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L19))

```lean
theorem normal_iff (r : α → α → Prop) (x : α) : Normal r x ↔ ∀ y, ¬ r x y
```

`Relation.Normal_iff` (alias, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L22))

```lean
alias Normal_iff
```

`Relation.Normal.reflTransGen_eq` (theorem, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L26))

> A multi-step from a normal form must be reflexive.

```lean
theorem Normal.reflTransGen_eq (h : Normal r x) (xy : ReflTransGen r x y) : x = y
```

`Relation.SN_iff_SN_of_rel` (lemma, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L29))

```lean
lemma SN_iff_SN_of_rel (x : α) : SN r x ↔ ∀ y, r x y → SN r y
```

`Relation.SN.intro` (lemma, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L31))

```lean
lemma SN.intro : (h : ∀ y, r x y → SN r y) → SN r x
```

`Relation.SN.of_rel` (lemma, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L33))

```lean
lemma SN.of_rel (hx : SN r x) (h : r x y) : SN r y
```

`Relation.SN.of_rel_reflTransGen` (lemma, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L36))

```lean
lemma SN.of_rel_reflTransGen (hx : SN r x) (h : ReflTransGen r x y) : SN r y
```

`Relation.SN.transGen` (lemma, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L41))

```lean
lemma SN.transGen (hx : SN r x) : SN (TransGen r) x
```

`Relation.SN.of_le` (lemma, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L47))

```lean
lemma SN.of_le {r' : α → α → Prop} (hx : SN r x) (h : r' ≤ r) : SN r' x
```

`Relation.SN.iff_transGen` (lemma, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L52))

```lean
lemma SN.iff_transGen (x : α) : SN (TransGen r) x ↔ SN r x
```

`Relation.SN.iff_isEmpty_chain` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L57))

> `SN r x` is equivalent to the more elementary definition, that there is no infinite sequence
> of reductions starting with `x`.

```lean
theorem SN.iff_isEmpty_chain :
    SN r x ↔ IsEmpty {f : ℕ → α | f 0 = x ∧ ∀ n, r (f n) (f (n + 1))}
```

`Relation.SN.onFun_of_image` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L61))

```lean
lemma SN.onFun_of_image {r : β → β → Prop} {f : α → β} (hx : SN r (f x)) :
    SN (Function.onFun r f) x
```

`Relation.SN.of_normal` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L64))

```lean
lemma SN.of_normal (hx : Normal r x) : SN r x
```

`Relation.SN.normalizable` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L66))

```lean
theorem SN.normalizable (hx : SN r x) : Normalizable r x
```

`Relation.Terminating.apply` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L74))

```lean
lemma Terminating.apply (hr : Terminating r) (x : α) : SN r x
```

`Relation.Terminating.iff_forall_sn` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L76))

```lean
lemma Terminating.iff_forall_sn : Terminating r ↔ ∀ x, SN r x
```

`Relation.Terminating.to_transGen` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L79))

```lean
theorem Terminating.to_transGen (ht : Terminating r) : Terminating (TransGen r)
```

`Relation.Terminating.toTransGen` (alias, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L83))

```lean
alias Terminating.toTransGen
```

`Relation.Terminating.to_acyclic` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L86))

> A terminating relation is acyclic.

```lean
theorem Terminating.to_acyclic (ht : Terminating r) : Acyclic r
```

`Relation.Terminating.toAcyclic` (alias, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L89))

```lean
alias Terminating.toAcyclic
```

`Relation.Terminating.of_transGen` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L91))

```lean
theorem Terminating.of_transGen : Terminating (TransGen r) → Terminating r
```

`Relation.Terminating.ofTransGen` (alias, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L95))

```lean
alias Terminating.ofTransGen
```

`Relation.Terminating.iff_transGen` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L97))

```lean
theorem Terminating.iff_transGen : Terminating (TransGen r) ↔ Terminating r
```

`Relation.Terminating.iff_isEmpty_chain` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L100))

```lean
theorem Terminating.iff_isEmpty_chain :
    Terminating r ↔ IsEmpty {f : ℕ → α // ∀ n, r (f n) (f (n + 1))}
```

`Relation.Terminating.of_le` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L104))

```lean
theorem Terminating.of_le {r' : α → α → Prop} (hr : Terminating r) (h : r' ≤ r) :
    Terminating r'
```

`Relation.Terminating.subtype_sn` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L109))

```lean
lemma Terminating.subtype_sn (r : α → α → Prop) :
    Terminating (α := {x // SN r x}) (fun a b => r a b)
```

`Relation.Terminating.to_normalizing` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L113))

```lean
theorem Terminating.to_normalizing (hr : Terminating r) : Normalizing r
```

`Relation.Terminating.isNormalizing` (alias, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean#L116))

```lean
alias Terminating.isNormalizing
```

## Depends on

- [Relations: Definitions](defs.md)

## Sources

- [Cslib/Foundations/Relation/Termination.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Termination.lean)
