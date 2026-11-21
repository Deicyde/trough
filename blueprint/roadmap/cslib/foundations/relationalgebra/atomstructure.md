---
catalog: module
lean: Cslib.RelationAlgebra.AtomStructure, Cslib.RelationAlgebra.LawfulAtomStructure, Cslib.RelationAlgebra.AtomStructure.assoc, Cslib.RelationAlgebra.AtomStructure.id_cycle_right, Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_right, Cslib.RelationAlgebra.AtomStructure.cycle_left, Cslib.RelationAlgebra.AtomStructure.conv_conv, Cslib.RelationAlgebra.AtomStructure.conv_cycles, Cslib.RelationAlgebra.AtomStructure.assoc_symm, Cslib.RelationAlgebra.AtomStructure.conv_eq_self_of_mem_id, Cslib.RelationAlgebra.AtomStructure.id_cycle_left, Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_left, Cslib.RelationAlgebra.ComplexAlgebra, Cslib.RelationAlgebra.ComplexAlgebra.equivSet, Cslib.RelationAlgebra.ComplexAlgebra.orderIsoSet, Cslib.RelationAlgebra.ComplexAlgebra.ext, Cslib.RelationAlgebra.ComplexAlgebra.mem_mk, Cslib.RelationAlgebra.ComplexAlgebra.mem_carrier, Cslib.RelationAlgebra.ComplexAlgebra.mem_sup, Cslib.RelationAlgebra.ComplexAlgebra.mem_compl, Cslib.RelationAlgebra.ComplexAlgebra.mem_one, Cslib.RelationAlgebra.ComplexAlgebra.mem_mul, Cslib.RelationAlgebra.ComplexAlgebra.mem_star, Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_iff, Cslib.RelationAlgebra.atomStructure, Cslib.RelationAlgebra.complexAlgebraEquiv, Cslib.RelationAlgebra.complexAlgebraEquiv_apply
statement: formalized
proof: formalized
---

# Atom structures

`Cslib.Foundations.RelationAlgebra.AtomStructure`, in [Cslib/Foundations/RelationAlgebra/AtomStructure.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean), by Chris Henson.

> This module defines atom structures and their complex relation algebras. It also constructs the
> atom structure of an atomic relation algebra and reconstructs a complete atomic relation algebra
> from its atom structure.
>
> ## References
>
> * [Steven Givant, *Advanced Topics in Relation Algebras*][Givant2017b]

`Cslib.RelationAlgebra.AtomStructure` (structure, [line 31](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L31))

> The data of an atom structure.

```lean
structure AtomStructure (α : Type*) where
  /-- The converse operation, presented as a function for stating the cycle rules. -/
  conv : α → α
  /-- The set of identity atoms. -/
  id : Set α
  /-- The set of atom cycles, where `(r, s, t)` represents `t ≤ r * s`. -/
  cycles : Set (α × α × α)
```

`Cslib.RelationAlgebra.LawfulAtomStructure` (class, [line 41](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L41))

> `LawfulAtomStructure` asserts the cycles of an atom structure follow associativity, converse,
> and identity conditions, so that its complex algebra is a relation algebra.

```lean
class LawfulAtomStructure {α : Type*} (A : AtomStructure α) : Prop where
  assoc : (r, q, p) ∈ A.cycles → (s, t, q) ∈ A.cycles →
    ∃ q', (q', t, p) ∈ A.cycles ∧ (r, s, q') ∈ A.cycles
  id_cycle_right : s ∈ A.id → (r, s, p) ∈ A.cycles → p = r
  exists_id_cycle_right (r) : ∃ s ∈ A.id, (r, s, r) ∈ A.cycles
  cycle_left : (r, s, t) ∈ A.cycles → (A.conv r, t, s) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.assoc` (theorem, [line 52](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L52))

```lean
theorem assoc {r q p s t : α} (h₁ : (r, q, p) ∈ A.cycles) (h₂ : (s, t, q) ∈ A.cycles) :
    ∃ q', (q', t, p) ∈ A.cycles ∧ (r, s, q') ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.id_cycle_right` (theorem, [line 56](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L56))

```lean
theorem id_cycle_right {s r p : α} (hs : s ∈ A.id) (h : (r, s, p) ∈ A.cycles) : p = r
```

`Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_right` (theorem, [line 59](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L59))

```lean
theorem exists_id_cycle_right (r : α) : ∃ s ∈ A.id, (r, s, r) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.cycle_left` (theorem, [line 62](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L62))

```lean
theorem cycle_left {r s t : α} (h : (r, s, t) ∈ A.cycles) : (A.conv r, t, s) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.conv_conv` (theorem, [line 66](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L66))

```lean
theorem conv_conv (r : α) : A.conv (A.conv r) = r
```

`Cslib.RelationAlgebra.AtomStructure.conv_cycles` (theorem, [line 69](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L69))

```lean
theorem conv_cycles {r s t : α} (h : (r, s, t) ∈ A.cycles) :
    (A.conv s, A.conv r, A.conv t) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.assoc_symm` (theorem, [line 75](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L75))

```lean
theorem assoc_symm {r s t p q : α} (h₁ : (q, t, p) ∈ A.cycles) (h₂ : (r, s, q) ∈ A.cycles) :
    ∃ q', (r, q', p) ∈ A.cycles ∧ (s, t, q') ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.conv_eq_self_of_mem_id` (theorem, [line 80](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L80))

```lean
theorem conv_eq_self_of_mem_id {r : α} (hr : r ∈ A.id) : A.conv r = r
```

`Cslib.RelationAlgebra.AtomStructure.id_cycle_left` (theorem, [line 83](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L83))

```lean
theorem id_cycle_left {s r p : α} (hs : s ∈ A.id) (h : (s, r, p) ∈ A.cycles) : p = r
```

`Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_left` (theorem, [line 87](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L87))

```lean
theorem exists_id_cycle_left (r : α) : ∃ s ∈ A.id, (s, r, r) ∈ A.cycles
```

`Cslib.RelationAlgebra.ComplexAlgebra` (structure, [line 94](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L94))

> The complex relation algebra of an atom structure. "Complex" here means a subset of atoms.

```lean
structure ComplexAlgebra {α : Type*} (A : AtomStructure α) where
  /-- The underlying set. -/
  carrier : Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.equivSet` (definition, [line 103](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L103))

> Equivalence with the powerset of the atom type.

```lean
def equivSet : ComplexAlgebra A ≃ Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.orderIsoSet` (definition, [line 122](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L122))

> Order isomorphism with the powerset of the atom type.

```lean
def orderIsoSet : ComplexAlgebra A ≃o Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.ext` (theorem, [line 140](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L140))

```lean
theorem ext (h : ∀ a, a ∈ x ↔ a ∈ y) : x = y
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_mk` (theorem, [line 143](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L143))

```lean
theorem mem_mk {s : Set α} : a ∈ (⟨s⟩ : ComplexAlgebra A) ↔ a ∈ s
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_carrier` (theorem, [line 145](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L145))

```lean
theorem mem_carrier : a ∈ x.carrier ↔ a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_sup` (theorem, [line 148](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L148))

```lean
theorem mem_sup : a ∈ x ⊔ y ↔ a ∈ x ∨ a ∈ y
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_compl` (theorem, [line 151](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L151))

```lean
theorem mem_compl : a ∈ xᶜ ↔ a ∉ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_one` (theorem, [line 154](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L154))

```lean
theorem mem_one : a ∈ (1 : ComplexAlgebra A) ↔ a ∈ A.id
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_mul` (theorem, [line 157](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L157))

```lean
theorem mem_mul : a ∈ x * y ↔ ∃ r ∈ x, ∃ s ∈ y, (r, s, a) ∈ A.cycles
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_star` (theorem, [line 160](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L160))

```lean
theorem mem_star [LawfulAtomStructure A] : a ∈ star x ↔ A.conv a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_iff` (theorem, [line 180](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L180))

> A complex algebra is integral exactly when its identity set is a singleton.

```lean
theorem isIntegral_iff : IsIntegral (ComplexAlgebra A) ↔ ∃ a, A.id = {a}
```

`Cslib.RelationAlgebra.atomStructure` (definition, [line 186](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L186))

> The atom structure formed by the atoms of an atomic relation algebra.

```lean
def atomStructure (α : Type*) [RelationAlgebra α] : AtomStructure {a : α // IsAtom a}
```

`Cslib.RelationAlgebra.complexAlgebraEquiv` (definition, [line 209](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L209))

> The isomorphism from a complete atomic relation algebra to the complex algebra of its
> atom structure.

```lean
noncomputable def complexAlgebraEquiv {α : Type*} [CompleteAtomicRelationAlgebra α] :
    RelationAlgebraEquiv α (ComplexAlgebra (atomStructure α))
```

`Cslib.RelationAlgebra.complexAlgebraEquiv_apply` (theorem, [line 228](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L228))

```lean
theorem complexAlgebraEquiv_apply {α : Type*} [CompleteAtomicRelationAlgebra α] (x : α) :
    complexAlgebraEquiv x = ⟨{a | a.val ≤ x}⟩
```

## Depends on

- [Morphisms and isomorphisms of relation algebras](hom.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/AtomStructure.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/AtomStructure.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.AtomStructure.json)
