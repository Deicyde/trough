---
catalog: module
lean: Cslib.RelationAlgebra.AtomStructure.ofGroup, Cslib.RelationAlgebra.AtomStructure.ofGroup_conv, Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_id, Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_cycles, Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_ofGroup, Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelRefl_iff, Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelSymm_iff, Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelTrans_iff, Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_carrier_eq_subgroup, Cslib.RelationAlgebra.ComplexAlgebra.cayley, Cslib.RelationAlgebra.ComplexAlgebra.mem_cayley, Cslib.RelationAlgebra.ComplexAlgebra.cayley_injective, Cslib.RelationAlgebra.ComplexAlgebra.mem_range_cayley, MulAction.set_mem_fixedPoints_iff, Cslib.RelationAlgebra.ComplexAlgebra.range_cayley, Cslib.RelationAlgebra.ComplexAlgebra.representable_ofGroup, Cslib.RelationAlgebra.GroupRepresentable, Cslib.RelationAlgebra.GroupRepresentable.of_injective, Cslib.RelationAlgebra.GroupRepresentable.representable, Cslib.RelationAlgebra.GroupRepresentable.isIntegral
statement: formalized
proof: formalized
---

# Group relation algebras

`Cslib.Foundations.RelationAlgebra.Group`, in [Cslib/Foundations/RelationAlgebra/Group.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean), by Chris Henson.

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

`Cslib.RelationAlgebra.AtomStructure.ofGroup` (definition, [line 44](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L44))

> The atom structure of a group.

```lean
def ofGroup : AtomStructure G
```

`Cslib.RelationAlgebra.AtomStructure.ofGroup_conv` (theorem, [line 50](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L50))

```lean
theorem ofGroup_conv (g : G) : (ofGroup G).conv g = g⁻¹
```

`Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_id` (theorem, [line 53](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L53))

```lean
theorem mem_ofGroup_id {g : G} : g ∈ (ofGroup G).id ↔ g = 1
```

`Cslib.RelationAlgebra.AtomStructure.mem_ofGroup_cycles` (theorem, [line 56](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L56))

```lean
theorem mem_ofGroup_cycles {f g h : G} : (f, g, h) ∈ (ofGroup G).cycles ↔ f * g = h
```

`Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_ofGroup` (theorem, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L72))

```lean
theorem isIntegral_ofGroup : IsIntegral (ComplexAlgebra (ofGroup G))
```

`Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelRefl_iff` (lemma, [line 75](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L75))

```lean
lemma ofGroup_isRelRefl_iff (x : ComplexAlgebra (ofGroup G)) : IsRelRefl x ↔ 1 ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelSymm_iff` (lemma, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L78))

```lean
lemma ofGroup_isRelSymm_iff (x : ComplexAlgebra (ofGroup G)) :
  IsRelSymm x ↔ ∀ {g : G}, g ∈ x → g⁻¹ ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_isRelTrans_iff` (lemma, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L81))

```lean
lemma ofGroup_isRelTrans_iff (x : ComplexAlgebra (ofGroup G)) :
    IsRelTrans x ↔ ∀ {g₁ g₂ : G}, g₁ ∈ x → g₂ ∈ x → g₁ * g₂ ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.ofGroup_carrier_eq_subgroup` (theorem, [line 85](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L85))

```lean
theorem ofGroup_carrier_eq_subgroup (x : ComplexAlgebra (ofGroup G)) :
    IsRelRefl x ∧ IsRelSymm x ∧ IsRelTrans x ↔ ∃ H : Subgroup G, (x : Set G) = H
```

`Cslib.RelationAlgebra.ComplexAlgebra.cayley` (definition, [line 97](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L97))

> The Cayley representation of the complex algebra of a group.

```lean
def cayley : RelationAlgebraHom (ComplexAlgebra (ofGroup G)) (SetRel G G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_cayley` (theorem, [line 111](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L111))

```lean
theorem mem_cayley {x : ComplexAlgebra (ofGroup G)} {g h : G} :
    (g, h) ∈ cayley G x ↔ g⁻¹ * h ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.cayley_injective` (theorem, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L114))

```lean
theorem cayley_injective : Function.Injective (cayley G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_range_cayley` (theorem, [line 119](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L119))

```lean
theorem mem_range_cayley {r : SetRel G G} :
    r ∈ Set.range (cayley G) ↔ ∀ g h k : G, (g, h) ∈ r → (k * g, k * h) ∈ r
```

`MulAction.set_mem_fixedPoints_iff` (theorem, [line 132](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L132))

```lean
theorem _root_.MulAction.set_mem_fixedPoints_iff {G α : Type*} [Group G] [MulAction G α]
    {s : Set α} : s ∈ MulAction.fixedPoints G (Set α) ↔ ∀ g : G, g • s ⊆ s
```

`Cslib.RelationAlgebra.ComplexAlgebra.range_cayley` (theorem, [line 138](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L138))

> `cayley` represents `ComplexAlgebra (ofGroup G)` by the left-invariant relations on `G`.

```lean
theorem range_cayley : Set.range (cayley G) = MulAction.fixedPoints G (SetRel G G)
```

`Cslib.RelationAlgebra.ComplexAlgebra.representable_ofGroup` (theorem, [line 143](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L143))

```lean
theorem representable_ofGroup (G : Type u) [Group G] : Representable (ComplexAlgebra (ofGroup G))
```

`Cslib.RelationAlgebra.GroupRepresentable` (definition, [line 149](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L149))

> A relation algebra is `GroupRepresentable` if it embeds into the complex algebra of a group.

```lean
def GroupRepresentable (α : Type u) [RelationAlgebra α] : Prop
```

`Cslib.RelationAlgebra.GroupRepresentable.of_injective` (theorem, [line 159](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L159))

> A relation algebra that embeds into an algebra representable over a group is itself
> representable over a group.

```lean
theorem of_injective (f : RelationAlgebraHom α α') (hf : Function.Injective f) :
    GroupRepresentable α' → GroupRepresentable α
```

`Cslib.RelationAlgebra.GroupRepresentable.representable` (theorem, [line 164](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L164))

> A relation algebra representable over a group is representable.

```lean
theorem representable : GroupRepresentable α → Representable α
```

`Cslib.RelationAlgebra.GroupRepresentable.isIntegral` (theorem, [line 168](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean#L168))

> A relation algebra representable over a group is integral.

```lean
theorem isIntegral : GroupRepresentable α → IsIntegral α
```

## Depends on

- [Atom structures](atomstructure.md)
- [Representable relation algebras](representation.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Group.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Group.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Group.json)
