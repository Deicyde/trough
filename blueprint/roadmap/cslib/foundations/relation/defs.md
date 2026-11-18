---
catalog: module
lean: Relation.emptyHRelation, Relation.dom, Relation.cod, Relation.Join₂, Relation.MJoin, Relation.UpTo, Relation.Preserves, Relation.Diamond, Relation.DiamondCommute, Relation.Confluent, Relation.Commute, Relation.SemiConfluent, Relation.SemiCommute, Relation.ChurchRosser, Relation.LocallyConfluent, Relation.LocallyCommute, Relation.StronglyConfluent, Relation.StronglyCommute, Relation.Reducible, Relation.Normal, Relation.Normalizable, Relation.Normalizing, Relation.SN, Relation.Terminating, Relation.Acyclic, Relation.Convergent, Relation.RightEuclidean, Relation.LeftEuclidean, Relation.Serial, Relation.successors, Relation.predecessors, Relation.restrict, Relation.IsIntervalOrder, Set.ReflOn, Set.LeftQuasiRefl, Set.RightQuasiRefl, Set.SymmOn
statement: formalized
proof: formalized
---

# Relations: Definitions

`Cslib.Foundations.Relation.Defs`, in [Cslib/Foundations/Relation/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

> ## References
>
> * [*Term Rewriting and All That*][Baader1998]
> * [*Simple Laws about Nonprominent Properties of Binary Relations*][Burghardt2018]
> * [*Applied Combinatorics*][KellerTrotter2017]

> ### Operations on relations

`Relation.emptyHRelation` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L30))

> The empty (heterogeneous) relation, which always returns `False`.

```lean
def emptyHRelation {α : Sort u} {β : Sort v} (_ : α) (_ : β)
```

`Relation.dom` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L33))

> Domain of a relation.

```lean
def dom (r : α → β → Prop) : Set α
```

`Relation.cod` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L36))

> Codomain of a relation, aka range.

```lean
def cod (r : α → β → Prop) : Set β
```

`Relation.Join₂` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L39))

> Generalisation of `Join` to two relations.

```lean
def Join₂ (r₁ r₂ : α → α → Prop) (a b : α) : Prop
```

`Relation.MJoin` (abbreviation, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L44))

> The join of the reflexive transitive closure. This is not named in Mathlib, but see
> `#loogle Relation.Join (Relation.ReflTransGen ?r)`

```lean
abbrev MJoin (r : α → α → Prop)
```

`Relation.UpTo` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L47))

> The relation `r` 'up to' the relation `s`.

```lean
def UpTo (r s : α → α → Prop) : α → α → Prop
```

`Relation.Preserves` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L50))

> Relation `r` preserves predicate `P`.

```lean
def Preserves (r : α → α → Prop) (P : α → Prop) : Prop
```

> ### Confluence and commutation properties

`Relation.Diamond` (abbreviation, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L55))

> A relation has the diamond property when all reductions with a common origin are joinable

```lean
abbrev Diamond (r : α → α → Prop)
```

`Relation.DiamondCommute` (abbreviation, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L58))

> Generalization of `Diamond` to two relations.

```lean
abbrev DiamondCommute (r₁ r₂ : α → α → Prop)
```

`Relation.Confluent` (abbreviation, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L62))

> A relation is confluent when its reflexive transitive closure has the diamond property.

```lean
abbrev Confluent (r : α → α → Prop)
```

`Relation.Commute` (abbreviation, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L65))

> Generalization of `Confluent` to two relations.

```lean
abbrev Commute (r₁ r₂ : α → α → Prop)
```

`Relation.SemiConfluent` (abbreviation, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L69))

> A relation is semi-confluent when single and multiple steps with common origin
> are multi-joinable.

```lean
abbrev SemiConfluent (r : α → α → Prop)
```

`Relation.SemiCommute` (abbreviation, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L73))

> Generalisation of `SemiConfluent` to two relations.

```lean
abbrev SemiCommute (r₁ r₂ : α → α → Prop)
```

`Relation.ChurchRosser` (abbreviation, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L77))

> A relation has the Church Rosser property when equivalence implies multi-joinability.

```lean
abbrev ChurchRosser (r : α → α → Prop)
```

`Relation.LocallyConfluent` (abbreviation, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L80))

> A relation is locally confluent when all reductions with a common origin are multi-joinable

```lean
abbrev LocallyConfluent (r : α → α → Prop)
```

`Relation.LocallyCommute` (definition, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L84))

> Generalization of `LocallyConfluent` to two relations.

```lean
def LocallyCommute (r₁ r₂ : α → α → Prop)
```

`Relation.StronglyConfluent` (abbreviation, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L88))

> A relation is strongly confluent when single steps are reflexive- and multi-joinable.

```lean
abbrev StronglyConfluent (r : α → α → Prop)
```

`Relation.StronglyCommute` (definition, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L92))

> Generalization of `StronglyConfluent` to two relations.

```lean
def StronglyCommute (r₁ r₂ : α → α → Prop)
```

> ### Normalization properties

`Relation.Reducible` (abbreviation, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L98))

> An element is reducible with respect to a relation if there is a value it is related to.

```lean
abbrev Reducible (r : α → α → Prop) (x : α) : Prop
```

`Relation.Normal` (abbreviation, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L101))

> An element is normal if it is not reducible.

```lean
abbrev Normal (r : α → α → Prop) (x : α) : Prop
```

`Relation.Normalizable` (abbreviation, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L104))

> An element is normalizable if it is related to a normal element.

```lean
abbrev Normalizable (r : α → α → Prop) (x : α) : Prop
```

`Relation.Normalizing` (abbreviation, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L108))

> A relation is normalizing when every element is normalizable.

```lean
abbrev Normalizing (r : α → α → Prop) : Prop
```

`Relation.SN` (abbreviation, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L113))

> An element `x` is `SN` (for strongly-normalising) for a relation `r` if it is accessible under
> the inverse of `r`.

```lean
abbrev SN (r : α → α → Prop)
```

`Relation.Terminating` (abbreviation, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L117))

> A relation is terminating when the inverse of its transitive closure is well-founded.
> Note that this is also called Noetherian or strongly normalizing in the literature.

```lean
abbrev Terminating (r : α → α → Prop)
```

`Relation.Acyclic` (abbreviation, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L121))

> A relation is acyclic if its transitive closure is irreflexive, equivalently if it admits no
> nonempty cycle.

```lean
abbrev Acyclic (r : α → α → Prop)
```

`Relation.Convergent` (abbreviation, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L124))

> A relation is convergent when it is both confluent and terminating.

```lean
abbrev Convergent (r : α → α → Prop)
```

> ### Modal properties

`Relation.RightEuclidean` (class, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L129))

> A relation `r` is (right) Euclidean if `r a b` and `r a c` guarantee `r b c`.

```lean
class RightEuclidean (r : α → α → Prop) where
  rightEuclidean : r a b → r a c → r b c
```

`Relation.LeftEuclidean` (class, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L133))

> A relation `r` is (left) Euclidean if `r a c` and `r b c` guarantee `r a b`.

```lean
class LeftEuclidean (r : α → α → Prop) where
  leftEuclidean {a b c} : r a c → r b c → r a b
```

`Relation.Serial` (class, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L137))

> A relation `r` is serial if every element is `Reducible`, i.e. `Relator.LeftTotal`.

```lean
class Serial (r : α → α → Prop) where
  serial : Relator.LeftTotal r
```

> ### Relations and sets in the underlying types

`Relation.successors` (abbreviation, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L143))

> The set of successors of an element `a` in a relation `r`.

```lean
abbrev successors (r : α → β → Prop) (a : α) : Set β
```

`Relation.predecessors` (abbreviation, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L146))

> The set of predecessors of an element `b` in a relation `r`.

```lean
abbrev predecessors (r : α → β → Prop) (b : β) : Set α
```

`Relation.restrict` (definition, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L149))

> The restriction of a relation `r` to a set `s`.

```lean
def restrict (r : α → α → Prop) (s : Set α) : α → α → Prop
```

> ### Interval order

`Relation.IsIntervalOrder` (definition, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L158))

> Fishburn's theorem (see sections 6.6 and 6.7 of [KellerTrotter2017]) shows that
> the definition below is a sufficient and necessary condition for a relation `r` to have
> a representation by closed intervals on the real line such that `r i1 i2` iff the right
> endpoint of `i1` is less than the left endpoint of `i2`.

```lean
def IsIntervalOrder (r : α → α → Prop) : Prop
```

> ### Properties of relations on restrictions of their (co)domain

`Set.ReflOn` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L175))

> `ReflOn s r` is true when a relation `r` is reflexive on its restriction to a set `s`.

```lean
def ReflOn (s : Set α) (r : α → α → Prop) : Prop
```

`Set.LeftQuasiRefl` (abbreviation, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L181))

> `LeftQuasiRefl r` is true when a relation `r` is reflexive on its domain.

```lean
abbrev LeftQuasiRefl (r : α → α → Prop)
```

`Set.RightQuasiRefl` (abbreviation, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L184))

> `RightQuasiRefl r` is true when a relation `r` is reflexive on its codomain.

```lean
abbrev RightQuasiRefl (r : α → α → Prop)
```

`Set.SymmOn` (definition, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean#L187))

> `SymmOn s r` is true when a relation `r` is symmetric on its restriction to a set `s`.

```lean
def SymmOn (s : Set α) (r : α → α → Prop) : Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Relation/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Defs.lean)
