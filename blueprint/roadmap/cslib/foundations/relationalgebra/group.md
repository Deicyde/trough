---
catalog: module
lean: Cslib.RelationAlgebra.AtomStructure.ofGroup, Cslib.RelationAlgebra.AtomStructure.ofGroup_conv, Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_id, Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_cycles, Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_ofGroup, Cslib.RelationAlgebra.ComplexAlgebra.cayley, Cslib.RelationAlgebra.ComplexAlgebra.mem_cayley, Cslib.RelationAlgebra.ComplexAlgebra.cayley_injective, Cslib.RelationAlgebra.ComplexAlgebra.mem_range_cayley, MulAction.set_mem_fixedPoints_iff, Cslib.RelationAlgebra.ComplexAlgebra.range_cayley, Cslib.RelationAlgebra.ComplexAlgebra.representable_ofGroup, Cslib.RelationAlgebra.GroupRepresentable, Cslib.RelationAlgebra.GroupRepresentable.of_injective, Cslib.RelationAlgebra.GroupRepresentable.representable, Cslib.RelationAlgebra.GroupRepresentable.isIntegral
statement: formalized
proof: formalized
---

# Group relation algebras

`Cslib.Foundations.RelationAlgebra.Group`, in [Cslib/Foundations/RelationAlgebra/Group.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean), by Chris Henson.

> Every group forms an atom structure (and thus a complex algebra) by defining composition as
> `X * Y = {f * g | f ∈ X, g ∈ Y}` and inheriting the inverse and (set containing) identity. These
> are some of the most common ways of constructing the representation of a relation algebra, so we
> also provide a predicate for being representable by a group and the data of the Cayley
> representation.
>
> ## References
>
> * [Steven Givant, *Introduction to Relation Algebras*][Givant2017a], Sections 3.5, 7.6
> * [J. D. Monk, *On representable relation algebras*][Monk1964]

`Cslib.RelationAlgebra.AtomStructure.ofGroup` (definition, [line 44](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L44))

> The atom structure of a group.

```lean
def ofGroup : AtomStructure G
```

`Cslib.RelationAlgebra.AtomStructure.ofGroup_conv` (theorem, [line 50](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L50))

```lean
theorem ofGroup_conv (g : G) : (ofGroup G).conv g = g⁻¹
```

`Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_id` (theorem, [line 53](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L53))

```lean
theorem mem_ofGroup_id {g : G} : g ∈ (ofGroup G).id ↔ g = 1
```

`Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_cycles` (theorem, [line 56](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L56))

```lean
theorem mem_ofGroup_cycles {f g h : G} : (f, g, h) ∈ (ofGroup G).cycles ↔ f * g = h
```

`Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_ofGroup` (theorem, [line 72](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L72))

```lean
theorem isIntegral_ofGroup : IsIntegral (ComplexAlgebra (ofGroup G))
```

`Cslib.RelationAlgebra.ComplexAlgebra.cayley` (definition, [line 77](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L77))

> The Cayley representation of the complex algebra of a group.

```lean
def cayley : RelationAlgebraHom (ComplexAlgebra (ofGroup G)) (SetRel G G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_cayley` (theorem, [line 91](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L91))

```lean
theorem mem_cayley {x : ComplexAlgebra (ofGroup G)} {g h : G} :
    (g, h) ∈ cayley G x ↔ g⁻¹ * h ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.cayley_injective` (theorem, [line 94](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L94))

```lean
theorem cayley_injective : Function.Injective (cayley G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_range_cayley` (theorem, [line 99](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L99))

```lean
theorem mem_range_cayley {r : SetRel G G} :
    r ∈ Set.range (cayley G) ↔ ∀ g h k : G, (g, h) ∈ r → (k * g, k * h) ∈ r
```

`MulAction.set_mem_fixedPoints_iff` (theorem, [line 112](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L112))

```lean
theorem _root_.MulAction.set_mem_fixedPoints_iff {G α : Type*} [Group G] [MulAction G α]
    {s : Set α} : s ∈ MulAction.fixedPoints G (Set α) ↔ ∀ g : G, g • s ⊆ s
```

`Cslib.RelationAlgebra.ComplexAlgebra.range_cayley` (theorem, [line 117](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L117))

```lean
theorem range_cayley : Set.range (cayley G) = MulAction.fixedPoints G (SetRel G G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.representable_ofGroup` (theorem, [line 122](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L122))

```lean
theorem representable_ofGroup (G : Type u) [Group G] : Representable (ComplexAlgebra (ofGroup G))
```

`Cslib.RelationAlgebra.GroupRepresentable` (definition, [line 128](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L128))

> A relation algebra is `GroupRepresentable` if it embeds into the complex algebra of a group.

```lean
def GroupRepresentable (α : Type u) [RelationAlgebra α] : Prop
```

`Cslib.RelationAlgebra.GroupRepresentable.of_injective` (theorem, [line 138](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L138))

> A relation algebra that embeds into an algebra representable over a group is itself
> representable over a group.

```lean
theorem of_injective (f : RelationAlgebraHom α α') (hf : Function.Injective f) :
    GroupRepresentable α' → GroupRepresentable α
```

`Cslib.RelationAlgebra.GroupRepresentable.representable` (theorem, [line 143](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L143))

> A relation algebra representable over a group is representable.

```lean
theorem representable : GroupRepresentable α → Representable α
```

`Cslib.RelationAlgebra.GroupRepresentable.isIntegral` (theorem, [line 147](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean#L147))

> A relation algebra representable over a group is integral.

```lean
theorem isIntegral : GroupRepresentable α → IsIntegral α
```

## Depends on

- [Atom structures](atomstructure.md)
- [Representable relation algebras](representation.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Group.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Group.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Group.json)
