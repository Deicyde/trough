---
catalog: module
lean: Cslib.RelationAlgebra, Cslib.CompleteRelationAlgebra, Cslib.CompleteAtomicRelationAlgebra, Cslib.RelationAlgebra.ofTarski, Cslib.RelationAlgebra.star_mono, Cslib.RelationAlgebra.starOrderIso, Cslib.RelationAlgebra.star_bot, Cslib.RelationAlgebra.star_le_star_iff, Cslib.RelationAlgebra.star_lt_star_iff, Cslib.RelationAlgebra.star_inf, Cslib.RelationAlgebra.star_compl, Cslib.RelationAlgebra.star_sdiff, Cslib.RelationAlgebra.mul_sup, Cslib.RelationAlgebra.mul_bot, Cslib.RelationAlgebra.isAtom_star_iff, Cslib.RelationAlgebra.atom_cycle_left, Cslib.RelationAlgebra.left_modular, Cslib.RelationAlgebra.exists_atom_le_mul_right, Cslib.RelationAlgebra.exists_atom_le_mul_left, Cslib.RelationAlgebra.IsIntegral, Cslib.RelationAlgebra.identityAtoms, Cslib.RelationAlgebra.symmetricDiversityAtoms, Cslib.RelationAlgebra.nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.le_compl_one_of_mem_nonsymmetricDiversityAtoms
statement: formalized
proof: formalized
---

# Relation algebras

`Cslib.Foundations.RelationAlgebra.Basic`, in [Cslib/Foundations/RelationAlgebra/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean), by Chris Henson.

> A relation algebra in the sense of Tarski (not to be confused with a relational algebra) is an
> extension of Boolean algebras that are designed to form an algebraic analysis of relations,
> `α → α → Prop` in Lean. They have applications in computer science such as the theory of constraint
> satisfaction as well as mathematical connections such as combinatorics.
>
> ## References
>
> * [R. Maddux, *Relation Algebras*][Maddux2006]

`Cslib.RelationAlgebra` (class, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L36))

> The class of relation algebras. Note the notational differences from the literature. In addition
> to inheriting Mathlib's notations for Boolean algebras, `star` is used for converse, and the monoid
> reduct for composition uses multiplicative notation.

```lean
class RelationAlgebra (α : Type*) extends BooleanAlgebra α, Monoid α, StarMul α where
  sup_mul (a b c : α) : (a ⊔ b) * c = a * c ⊔ b * c
  star_sup (a b : α) : star (a ⊔ b) = star a ⊔ star b
  tarski (a b : α) : star a * (a * b)ᶜ ≤ bᶜ
```

`Cslib.CompleteRelationAlgebra` (class, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L42))

> The relation algebra of a complete Boolean algebra.

```lean
class CompleteRelationAlgebra (α : Type*) extends RelationAlgebra α, CompleteBooleanAlgebra α
```

`Cslib.CompleteAtomicRelationAlgebra` (class, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L45))

> The relation algebra of a complete and atomic Boolean algebra.

```lean
class CompleteAtomicRelationAlgebra (α : Type*) extends CompleteRelationAlgebra α,
    CompleteAtomicBooleanAlgebra α
```

`Cslib.RelationAlgebra.ofTarski` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L52))

> A `RelationAlgebra` can be constructed using Tarski's original ten axioms.

```lean
def ofTarski {α : Type*} [Max α] [Compl α] [Mul α] [One α] [Star α]
    (sup_comm : ∀ a b : α, a ⊔ b = b ⊔ a)
    (sup_assoc : ∀ a b c : α, (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c))
    (huntington : ∀ a b : α, (aᶜ ⊔ b)ᶜ ⊔ (aᶜ ⊔ bᶜ)ᶜ = a)
    (mul_assoc : ∀ a b c : α, (a * b) * c = a * (b * c))
    (mul_one : ∀ a : α, a * 1 = a)
    (star_involutive : ∀ a : α, star (star a) = a)
    (star_mul : ∀ a b : α, star (a * b) = star b * star a)
    (sup_mul : ∀ a b c : α, (a ⊔ b) * c = a * c ⊔ b * c)
    (star_sup : ∀ a b : α, star (a ⊔ b) = star a ⊔ star b)
    (tarski : ∀ a b : α, star a * (a * b)ᶜ ⊔ bᶜ = bᶜ) : RelationAlgebra α
```

`Cslib.RelationAlgebra.star_mono` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L85))

```lean
theorem star_mono : Monotone (star : α → α)
```

`Cslib.RelationAlgebra.starOrderIso` (definition, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L91))

> Converse as an automorphism of a relation algebra.

```lean
def starOrderIso : α ≃o α
```

`Cslib.RelationAlgebra.star_bot` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L96))

```lean
theorem star_bot : star (⊥ : α) = ⊥
```

`Cslib.RelationAlgebra.star_le_star_iff` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L99))

```lean
theorem star_le_star_iff {a b : α} : star a ≤ star b ↔ a ≤ b
```

`Cslib.RelationAlgebra.star_lt_star_iff` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L102))

```lean
theorem star_lt_star_iff {a b : α} : star a < star b ↔ a < b
```

`Cslib.RelationAlgebra.star_inf` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L105))

```lean
theorem star_inf (a b : α) : star (a ⊓ b) = star a ⊓ star b
```

`Cslib.RelationAlgebra.star_compl` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L108))

```lean
theorem star_compl (a : α) : star aᶜ = (star a)ᶜ
```

`Cslib.RelationAlgebra.star_sdiff` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L112))

```lean
theorem star_sdiff (a b : α) : star (a \ b) = star a \ star b
```

`Cslib.RelationAlgebra.mul_sup` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L115))

```lean
theorem mul_sup (a b c : α) : a * (b ⊔ c) = a * b ⊔ a * c
```

`Cslib.RelationAlgebra.mul_bot` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L126))

```lean
theorem mul_bot (a : α) : a * ⊥ = ⊥
```

`Cslib.RelationAlgebra.isAtom_star_iff` (theorem, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L133))

```lean
theorem isAtom_star_iff {a : α} : IsAtom (star a) ↔ IsAtom a
```

`Cslib.RelationAlgebra.atom_cycle_left` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L136))

```lean
theorem atom_cycle_left {r s p : α} (hs : IsAtom s) (hp : p ≠ ⊥) (h : p ≤ r * s) :
    s ≤ star r * p
```

`Cslib.RelationAlgebra.left_modular` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L146))

```lean
theorem left_modular (a b c : α) : a * b ⊓ c ≤ a * (b ⊓ star a * c)
```

`Cslib.RelationAlgebra.exists_atom_le_mul_right` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L156))

> If an atom lies below a product, its right factor can be replaced by an atom below it.

```lean
theorem exists_atom_le_mul_right [IsAtomic α] {a b p : α} (hp : IsAtom p) (h : p ≤ a * b) :
    ∃ s, IsAtom s ∧ s ≤ b ∧ p ≤ a * s
```

`Cslib.RelationAlgebra.exists_atom_le_mul_left` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L166))

> If an atom lies below a product, its left factor can be replaced by an atom below it.

```lean
theorem exists_atom_le_mul_left [IsAtomic α] {a b p : α} (hp : IsAtom p) (h : p ≤ a * b) :
    ∃ r, IsAtom r ∧ r ≤ a ∧ p ≤ r * b
```

`Cslib.RelationAlgebra.IsIntegral` (definition, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L173))

> A relation algebra is *integral* when its identity is an atom.

```lean
def IsIntegral (α : Type*) [RelationAlgebra α] : Prop
```

`Cslib.RelationAlgebra.identityAtoms` (definition, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L176))

> The set of identity atoms.

```lean
def identityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`Cslib.RelationAlgebra.symmetricDiversityAtoms` (definition, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L179))

> The set of symmetric diversity atoms, those below the complement of identity.

```lean
def symmetricDiversityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`Cslib.RelationAlgebra.nonsymmetricDiversityAtoms` (definition, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L184))

> The set of nonsymmetric diversity atoms. The diversity condition follows from
> `le_compl_one_of_mem_nonsymmetricDiversityAtoms`.

```lean
def nonsymmetricDiversityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`Cslib.RelationAlgebra.le_compl_one_of_mem_nonsymmetricDiversityAtoms` (theorem, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean#L188))

> Every nonsymmetric atom lies below the complement of identity.

```lean
theorem le_compl_one_of_mem_nonsymmetricDiversityAtoms {a : α}
    (h : a ∈ nonsymmetricDiversityAtoms α) : a ≤ 1ᶜ
```

## Depends on

- [Huntington's axioms for Boolean Algebras](../order/huntington.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Basic.lean)
