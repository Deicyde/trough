---
catalog: module
lean: Cslib.RelationAlgebra.AtomStructure, Cslib.RelationAlgebra.LawfulAtomStructure, Cslib.RelationAlgebra.AtomStructure.assoc, Cslib.RelationAlgebra.AtomStructure.id_cycle_right, Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_right, Cslib.RelationAlgebra.AtomStructure.cycle_left, Cslib.RelationAlgebra.AtomStructure.conv_conv, Cslib.RelationAlgebra.AtomStructure.conv_cycles, Cslib.RelationAlgebra.AtomStructure.assoc_symm, Cslib.RelationAlgebra.AtomStructure.conv_eq_self_of_mem_id, Cslib.RelationAlgebra.AtomStructure.id_cycle_left, Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_left, Cslib.RelationAlgebra.ComplexAlgebra, Cslib.RelationAlgebra.ComplexAlgebra.equivSet, Cslib.RelationAlgebra.ComplexAlgebra.orderIsoSet, Cslib.RelationAlgebra.ComplexAlgebra.ext, Cslib.RelationAlgebra.ComplexAlgebra.mem_mk, Cslib.RelationAlgebra.ComplexAlgebra.mem_carrier, Cslib.RelationAlgebra.ComplexAlgebra.mem_sup, Cslib.RelationAlgebra.ComplexAlgebra.mem_compl, Cslib.RelationAlgebra.ComplexAlgebra.mem_one, Cslib.RelationAlgebra.ComplexAlgebra.mem_mul, Cslib.RelationAlgebra.ComplexAlgebra.mem_star, Cslib.RelationAlgebra.ComplexAlgebra.isRelRefl_iff, Cslib.RelationAlgebra.ComplexAlgebra.isRelSymm_iff, Cslib.RelationAlgebra.ComplexAlgebra.isRelTrans_iff, Cslib.RelationAlgebra.ComplexAlgebra.coe_singleton, Cslib.RelationAlgebra.ComplexAlgebra.mem_singleton, Cslib.RelationAlgebra.ComplexAlgebra.singleton_injective, Cslib.RelationAlgebra.ComplexAlgebra.singleton_inj, Cslib.RelationAlgebra.ComplexAlgebra.singleton_le_iff, Cslib.RelationAlgebra.ComplexAlgebra.star_singleton, Cslib.RelationAlgebra.ComplexAlgebra.isAtom_iff, Cslib.RelationAlgebra.ComplexAlgebra.isAtom_singleton, Cslib.RelationAlgebra.ComplexAlgebra.ncard_preimage_singleton, Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_iff, Cslib.RelationAlgebra.ComplexAlgebra.singleton_mem_symmetricDiversityAtoms_iff, Cslib.RelationAlgebra.ComplexAlgebra.singleton_mem_nonsymmetricDiversityAtoms_iff, Cslib.RelationAlgebra.atomStructure, Cslib.RelationAlgebra.complexAlgebraEquiv, Cslib.RelationAlgebra.complexAlgebraEquiv_apply
statement: formalized
proof: formalized
---

# Atom structures

`Cslib.Foundations.RelationAlgebra.AtomStructure`, in [Cslib/Foundations/RelationAlgebra/AtomStructure.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean), by Chris Henson.

> This module defines atom structures and their complex relation algebras. It also constructs the
> atom structure of an atomic relation algebra and reconstructs a complete atomic relation algebra
> from its atom structure.
>
> ## References
>
> * [Steven Givant, *Advanced Topics in Relation Algebras*][Givant2017b]

`Cslib.RelationAlgebra.AtomStructure` (structure, [line 32](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L32))

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

`Cslib.RelationAlgebra.LawfulAtomStructure` (class, [line 42](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L42))

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

`Cslib.RelationAlgebra.AtomStructure.assoc` (theorem, [line 53](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L53))

```lean
theorem assoc {r q p s t : α} (h₁ : (r, q, p) ∈ A.cycles) (h₂ : (s, t, q) ∈ A.cycles) :
    ∃ q', (q', t, p) ∈ A.cycles ∧ (r, s, q') ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.id_cycle_right` (theorem, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L57))

```lean
theorem id_cycle_right {s r p : α} (hs : s ∈ A.id) (h : (r, s, p) ∈ A.cycles) : p = r
```

`Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_right` (theorem, [line 60](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L60))

```lean
theorem exists_id_cycle_right (r : α) : ∃ s ∈ A.id, (r, s, r) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.cycle_left` (theorem, [line 63](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L63))

```lean
theorem cycle_left {r s t : α} (h : (r, s, t) ∈ A.cycles) : (A.conv r, t, s) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.conv_conv` (theorem, [line 67](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L67))

```lean
theorem conv_conv (r : α) : A.conv (A.conv r) = r
```

`Cslib.RelationAlgebra.AtomStructure.conv_cycles` (theorem, [line 70](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L70))

```lean
theorem conv_cycles {r s t : α} (h : (r, s, t) ∈ A.cycles) :
    (A.conv s, A.conv r, A.conv t) ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.assoc_symm` (theorem, [line 76](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L76))

```lean
theorem assoc_symm {r s t p q : α} (h₁ : (q, t, p) ∈ A.cycles) (h₂ : (r, s, q) ∈ A.cycles) :
    ∃ q', (r, q', p) ∈ A.cycles ∧ (s, t, q') ∈ A.cycles
```

`Cslib.RelationAlgebra.AtomStructure.conv_eq_self_of_mem_id` (theorem, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L81))

```lean
theorem conv_eq_self_of_mem_id {r : α} (hr : r ∈ A.id) : A.conv r = r
```

`Cslib.RelationAlgebra.AtomStructure.id_cycle_left` (theorem, [line 84](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L84))

```lean
theorem id_cycle_left {s r p : α} (hs : s ∈ A.id) (h : (s, r, p) ∈ A.cycles) : p = r
```

`Cslib.RelationAlgebra.AtomStructure.exists_id_cycle_left` (theorem, [line 88](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L88))

```lean
theorem exists_id_cycle_left (r : α) : ∃ s ∈ A.id, (s, r, r) ∈ A.cycles
```

`Cslib.RelationAlgebra.ComplexAlgebra` (structure, [line 95](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L95))

> The complex relation algebra of an atom structure. "Complex" here means a subset of atoms.

```lean
structure ComplexAlgebra {α : Type*} (A : AtomStructure α) where
  /-- The underlying set. -/
  carrier : Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.equivSet` (definition, [line 104](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L104))

> Equivalence with the powerset of the atom type.

```lean
def equivSet : ComplexAlgebra A ≃ Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.orderIsoSet` (definition, [line 123](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L123))

> Order isomorphism with the powerset of the atom type.

```lean
def orderIsoSet : ComplexAlgebra A ≃o Set α
```

`Cslib.RelationAlgebra.ComplexAlgebra.ext` (theorem, [line 144](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L144))

```lean
theorem ext (h : ∀ a, a ∈ x ↔ a ∈ y) : x = y
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_mk` (theorem, [line 147](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L147))

```lean
theorem mem_mk {s : Set α} : a ∈ (⟨s⟩ : ComplexAlgebra A) ↔ a ∈ s
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_carrier` (theorem, [line 149](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L149))

```lean
theorem mem_carrier : a ∈ x.carrier ↔ a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_sup` (theorem, [line 152](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L152))

```lean
theorem mem_sup : a ∈ x ⊔ y ↔ a ∈ x ∨ a ∈ y
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_compl` (theorem, [line 155](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L155))

```lean
theorem mem_compl : a ∈ xᶜ ↔ a ∉ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_one` (theorem, [line 158](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L158))

```lean
theorem mem_one : a ∈ (1 : ComplexAlgebra A) ↔ a ∈ A.id
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_mul` (theorem, [line 161](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L161))

```lean
theorem mem_mul : a ∈ x * y ↔ ∃ r ∈ x, ∃ s ∈ y, (r, s, a) ∈ A.cycles
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_star` (theorem, [line 164](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L164))

```lean
theorem mem_star [LawfulAtomStructure A] : a ∈ star x ↔ A.conv a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.isRelRefl_iff` (theorem, [line 167](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L167))

```lean
protected theorem isRelRefl_iff (x : ComplexAlgebra A) : IsRelRefl x ↔ A.id ⊆ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.isRelSymm_iff` (theorem, [line 170](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L170))

```lean
protected theorem isRelSymm_iff [LawfulAtomStructure A] (x : ComplexAlgebra A) :
    IsRelSymm x ↔ ∀ {a : α}, a ∈ x → A.conv a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.isRelTrans_iff` (theorem, [line 176](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L176))

```lean
protected theorem isRelTrans_iff (x : ComplexAlgebra A) :
    IsRelTrans x ↔ ∀ {a b c : α}, a ∈ x → b ∈ x → (a, b, c) ∈ A.cycles → c ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.coe_singleton` (theorem, [line 182](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L182))

```lean
theorem coe_singleton : (({a} : ComplexAlgebra A) : Set α) = {a}
```

`Cslib.RelationAlgebra.ComplexAlgebra.mem_singleton` (theorem, [line 185](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L185))

```lean
theorem mem_singleton {b : α} : b ∈ ({a} : ComplexAlgebra A) ↔ b = a
```

`Cslib.RelationAlgebra.ComplexAlgebra.singleton_injective` (theorem, [line 188](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L188))

```lean
theorem singleton_injective : Function.Injective (singleton : α → ComplexAlgebra A)
```

`Cslib.RelationAlgebra.ComplexAlgebra.singleton_inj` (theorem, [line 192](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L192))

```lean
theorem singleton_inj {b : α} : ({a} : ComplexAlgebra A) = {b} ↔ a = b
```

`Cslib.RelationAlgebra.ComplexAlgebra.singleton_le_iff` (theorem, [line 196](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L196))

```lean
theorem singleton_le_iff : {a} ≤ x ↔ a ∈ x
```

`Cslib.RelationAlgebra.ComplexAlgebra.star_singleton` (theorem, [line 199](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L199))

```lean
theorem star_singleton : star ({a} : ComplexAlgebra A) = {A.conv a}
```

`Cslib.RelationAlgebra.ComplexAlgebra.isAtom_iff` (theorem, [line 202](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L202))

```lean
theorem isAtom_iff : IsAtom x ↔ ∃ a, x = {a}
```

`Cslib.RelationAlgebra.ComplexAlgebra.isAtom_singleton` (theorem, [line 207](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L207))

```lean
theorem isAtom_singleton : IsAtom ({a} : ComplexAlgebra A)
```

`Cslib.RelationAlgebra.ComplexAlgebra.ncard_preimage_singleton` (theorem, [line 209](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L209))

```lean
theorem ncard_preimage_singleton {S : Set (ComplexAlgebra A)} (hS : ∀ x ∈ S, IsAtom x) :
    (singleton ⁻¹' S).ncard = S.ncard
```

`Cslib.RelationAlgebra.ComplexAlgebra.isIntegral_iff` (theorem, [line 231](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L231))

> A complex algebra is integral exactly when its identity set is a singleton.

```lean
theorem isIntegral_iff : IsIntegral (ComplexAlgebra A) ↔ ∃ a, A.id = {a}
```

`Cslib.RelationAlgebra.ComplexAlgebra.singleton_mem_symmetricDiversityAtoms_iff` (theorem, [line 237](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L237))

```lean
theorem singleton_mem_symmetricDiversityAtoms_iff :
    {a} ∈ symmetricDiversityAtoms (ComplexAlgebra A) ↔ a ∉ A.id ∧ A.conv a = a
```

`Cslib.RelationAlgebra.ComplexAlgebra.singleton_mem_nonsymmetricDiversityAtoms_iff` (theorem, [line 242](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L242))

```lean
theorem singleton_mem_nonsymmetricDiversityAtoms_iff :
    {a} ∈ nonsymmetricDiversityAtoms (ComplexAlgebra A) ↔ A.conv a ≠ a
```

`Cslib.RelationAlgebra.atomStructure` (definition, [line 249](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L249))

> The atom structure formed by the atoms of an atomic relation algebra.

```lean
def atomStructure (α : Type*) [RelationAlgebra α] : AtomStructure {a : α // IsAtom a}
```

`Cslib.RelationAlgebra.complexAlgebraEquiv` (definition, [line 272](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L272))

> The isomorphism from a complete atomic relation algebra to the complex algebra of its
> atom structure.

```lean
noncomputable def complexAlgebraEquiv {α : Type*} [CompleteAtomicRelationAlgebra α] :
    RelationAlgebraEquiv α (ComplexAlgebra (atomStructure α))
```

`Cslib.RelationAlgebra.complexAlgebraEquiv_apply` (theorem, [line 291](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean#L291))

```lean
theorem complexAlgebraEquiv_apply {α : Type*} [CompleteAtomicRelationAlgebra α] (x : α) :
    complexAlgebraEquiv x = ⟨{a | a.val ≤ x}⟩
```

## Depends on

- [Morphisms and isomorphisms of relation algebras](hom.md)
- [Element properties for relation algebras](specialelements.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/AtomStructure.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/AtomStructure.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.AtomStructure.json)
