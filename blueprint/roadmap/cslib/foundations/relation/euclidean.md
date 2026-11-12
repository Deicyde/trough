---
catalog: module
lean: Relation.refl_serial, Relation.RightEuclidean.reflOn_cod, Relation.RightEuclidean.leftEuclidean_swap, Relation.RightEuclidean.trichotomous_trans, Relation.RightEuclidean.antisymm_rightUnique, Relation.RightEuclidean.rightUnique_antisymm, Relation.RightEuclidean.rightUnique_trans, Relation.RightEuclidean.rightTotal_equiv, Relation.RightEuclidean.leftTotal_rightUnique_trans, Relation.RightEuclidean.trichotomous_antisymm_finite, Relation.RightEuclidean.trichotomous_antisymm_card, Relation.RightEuclidean.cod_subset_dom, Relation.RightEuclidean.rightTotal_cod, Relation.RightEuclidean.equiv_cod, Relation.LeftEuclidean.reflOn_dom, Relation.LeftEuclidean.rightEuclidean_swap, Relation.LeftEuclidean.trichotomous_trans, Relation.LeftEuclidean.antisymm_leftUnique, Relation.LeftEuclidean.leftUnique_antisymm, Relation.LeftEuclidean.leftUnique_trans, Relation.LeftEuclidean.leftTotal_equiv, Relation.LeftEuclidean.rightTotal_leftUnique_trans, Relation.LeftEuclidean.trichotomous_antisymm_finite, Relation.LeftEuclidean.trichotomous_antisymm_card, Relation.LeftEuclidean.dom_subset_cod, Relation.LeftEuclidean.leftTotal_dom, Relation.LeftEuclidean.equiv_dom, Relation.symm_leftEuclidean_iff_rightEuclidean, Relation.symm_leftEuclidean_iff_trans, Relation.symm_rightEuclidean_iff_trans, Relation.leftEuclidean_rightEuclidean_dom_cod_eq, Relation.dom_cod_leftEuclidean, Relation.dom_cod_rightEuclidean, Relation.leftEuclidean_rightEuclidean_iff_dom_cod
statement: formalized
proof: formalized
---

# Relations: Euclidean Relations

`Cslib.Foundations.Relation.Euclidean`, in [Cslib/Foundations/Relation/Euclidean.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

> This module proves basic properties about left and right Euclidean relations, which are use
> in modal logic.
>
> …
>
> ## References
>
> * [*Simple Laws about Nonprominent Properties of Binary Relations*][Burghardt2018]

`Relation.refl_serial` (lemma, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L41))

```lean
lemma refl_serial (r : α → α → Prop) (h : Std.Refl r) : Serial r
```

`Relation.RightEuclidean.reflOn_cod` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L51))

> A `RightEuclidean` relation is reflexive on its codomain

```lean
theorem reflOn_cod : (cod r).ReflOn r
```

`Relation.RightEuclidean.leftEuclidean_swap` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L54))

> The converse of a `RightEuclidean` relation is `LeftEuclidean`

```lean
theorem leftEuclidean_swap : LeftEuclidean (fun a b => r b a)
```

`Relation.RightEuclidean.trichotomous_trans` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L60))

```lean
theorem trichotomous_trans [Std.Trichotomous r] : IsTrans α r
```

`Relation.RightEuclidean.antisymm_rightUnique` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L67))

```lean
theorem antisymm_rightUnique [Std.Antisymm r] : Relator.RightUnique r
```

`Relation.RightEuclidean.rightUnique_antisymm` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L71))

```lean
theorem rightUnique_antisymm (h : Relator.RightUnique r) : Std.Antisymm r
```

`Relation.RightEuclidean.rightUnique_trans` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L74))

```lean
theorem rightUnique_trans (h : Relator.RightUnique r) : IsTrans α r
```

`Relation.RightEuclidean.rightTotal_equiv` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L79))

```lean
theorem rightTotal_equiv (h : Relator.RightTotal r) : IsEquiv α r
```

`Relation.RightEuclidean.leftTotal_rightUnique_trans` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L84))

```lean
theorem leftTotal_rightUnique_trans (h₁ : LeftTotal r) (h₂ : RightUnique r) [IsTrans α r] :
    RightEuclidean r
```

`Relation.RightEuclidean.trichotomous_antisymm_finite` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L103))

```lean
theorem trichotomous_antisymm_finite [Std.Trichotomous r] [Std.Antisymm r] : Finite α
```

`Relation.RightEuclidean.trichotomous_antisymm_card` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L111))

```lean
theorem trichotomous_antisymm_card [Std.Trichotomous r] [Std.Antisymm r] [Fintype α] :
    Fintype.card α ≤ 2
```

`Relation.RightEuclidean.cod_subset_dom` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L118))

```lean
theorem cod_subset_dom : cod r ⊆ dom r
```

`Relation.RightEuclidean.rightTotal_cod` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L120))

```lean
theorem rightTotal_cod : Relator.RightTotal (α := cod r) (β := cod r) r
```

`Relation.RightEuclidean.equiv_cod` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L123))

```lean
theorem equiv_cod : IsEquiv (cod r) r
```

`Relation.LeftEuclidean.reflOn_dom` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L132))

> A `LeftEuclidean` relation is reflexive on its domain

```lean
theorem reflOn_dom : (dom r).ReflOn r
```

`Relation.LeftEuclidean.rightEuclidean_swap` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L136))

> The converse of a `LeftEuclidean` relation is `RightEuclidean`

```lean
theorem rightEuclidean_swap : RightEuclidean (fun a b => r b a)
```

`Relation.LeftEuclidean.trichotomous_trans` (theorem, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L142))

```lean
theorem trichotomous_trans [Std.Trichotomous r] : IsTrans α r
```

`Relation.LeftEuclidean.antisymm_leftUnique` (theorem, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L149))

```lean
theorem antisymm_leftUnique [Std.Antisymm r] : Relator.LeftUnique r
```

`Relation.LeftEuclidean.leftUnique_antisymm` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L153))

```lean
theorem leftUnique_antisymm (h : Relator.LeftUnique r) : Std.Antisymm r
```

`Relation.LeftEuclidean.leftUnique_trans` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L156))

```lean
theorem leftUnique_trans (h : Relator.LeftUnique r) : IsTrans α r
```

`Relation.LeftEuclidean.leftTotal_equiv` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L161))

```lean
theorem leftTotal_equiv (h : Relator.LeftTotal r) : IsEquiv α r
```

`Relation.LeftEuclidean.rightTotal_leftUnique_trans` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L166))

```lean
theorem rightTotal_leftUnique_trans (h₁ : RightTotal r) (h₂ : LeftUnique r) [IsTrans α r] :
    LeftEuclidean r
```

`Relation.LeftEuclidean.trichotomous_antisymm_finite` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L174))

```lean
theorem trichotomous_antisymm_finite [Std.Trichotomous r] [Std.Antisymm r] : Finite α
```

`Relation.LeftEuclidean.trichotomous_antisymm_card` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L177))

```lean
theorem trichotomous_antisymm_card [Std.Trichotomous r] [Std.Antisymm r] [Fintype α] :
    Fintype.card α ≤ 2
```

`Relation.LeftEuclidean.dom_subset_cod` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L181))

```lean
theorem dom_subset_cod : dom r ⊆ cod r
```

`Relation.LeftEuclidean.leftTotal_dom` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L183))

```lean
theorem leftTotal_dom : Relator.LeftTotal (α := dom r) (β := dom r) r
```

`Relation.LeftEuclidean.equiv_dom` (theorem, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L186))

```lean
theorem equiv_dom : IsEquiv (dom r) r
```

`Relation.symm_leftEuclidean_iff_rightEuclidean` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L202))

> For a symmetric relation, `LeftEuclidean` and `RightEuclidean` are equivalent.

```lean
theorem symm_leftEuclidean_iff_rightEuclidean : LeftEuclidean r ↔ RightEuclidean r
```

`Relation.symm_leftEuclidean_iff_trans` (theorem, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L206))

> For a symmetric relation, `LeftEuclidean` and transitivity are equivalent.

```lean
theorem symm_leftEuclidean_iff_trans : LeftEuclidean r ↔  IsTrans α r
```

`Relation.symm_rightEuclidean_iff_trans` (theorem, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L210))

> For a symmetric relation, `RightEuclidean` and transitivity are equivalent.

```lean
theorem symm_rightEuclidean_iff_trans : RightEuclidean r ↔ IsTrans α r
```

`Relation.leftEuclidean_rightEuclidean_dom_cod_eq` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L215))

```lean
theorem leftEuclidean_rightEuclidean_dom_cod_eq [LeftEuclidean r] [RightEuclidean r] :
    dom r = cod r
```

`Relation.dom_cod_leftEuclidean` (theorem, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L221))

```lean
theorem dom_cod_leftEuclidean (eq : dom r = cod r) [equiv_dom : IsEquiv (dom r) r] :
    LeftEuclidean r
```

`Relation.dom_cod_rightEuclidean` (lemma, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L227))

```lean
lemma dom_cod_rightEuclidean (eq : dom r = cod r) [equiv_dom : IsEquiv (dom r) r] :
    RightEuclidean r
```

`Relation.leftEuclidean_rightEuclidean_iff_dom_cod` (theorem, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean#L235))

> A relation is both left and right Euclidean if and only if the relation is an equivalence on
> coinciding domain and codomain.

```lean
theorem leftEuclidean_rightEuclidean_iff_dom_cod :
    LeftEuclidean r ∧ RightEuclidean r ↔ dom r = cod r ∧ IsEquiv (dom r) r
```

## Depends on

- [Relations: Definitions](defs.md)

## Proof depends on

- [Relations: Properties on set restrictions](restriction.md)

## Sources

- [Cslib/Foundations/Relation/Euclidean.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Euclidean.lean)
