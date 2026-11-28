---
catalog: module
lean: Cslib.RelationAlgebra, Cslib.CompleteRelationAlgebra, Cslib.CompleteAtomicRelationAlgebra, Cslib.RelationAlgebra.ofTarski, Cslib.RelationAlgebra.star_mono, Cslib.RelationAlgebra.starOrderIso, Cslib.RelationAlgebra.star_bot, Cslib.RelationAlgebra.star_le_star_iff, Cslib.RelationAlgebra.star_lt_star_iff, Cslib.RelationAlgebra.le_star_iff, Cslib.RelationAlgebra.star_inf, Cslib.RelationAlgebra.star_compl, Cslib.RelationAlgebra.star_sdiff, Cslib.RelationAlgebra.star_sSup, Cslib.RelationAlgebra.mul_sup, Cslib.RelationAlgebra.mul_bot, Cslib.RelationAlgebra.bot_mul, Cslib.RelationAlgebra.inf_mul_le, Cslib.RelationAlgebra.mul_inf_le, Cslib.RelationAlgebra.isAtom_star_iff, Cslib.RelationAlgebra.left_modular, Cslib.RelationAlgebra.right_modular, Cslib.RelationAlgebra.le_mul_star_mul, Cslib.RelationAlgebra.mul_le_compl_right, Cslib.RelationAlgebra.mul_le_compl_left, Cslib.RelationAlgebra.mul_le_compl_star_tfae, Cslib.RelationAlgebra.leftResidual, Cslib.RelationAlgebra.le_leftResidual_iff, Cslib.RelationAlgebra.rightResidual, Cslib.RelationAlgebra.le_rightResidual_iff, Cslib.RelationAlgebra.star_leftResidual, Cslib.RelationAlgebra.star_rightResidual, Cslib.RelationAlgebra.mul_sSup, Cslib.RelationAlgebra.sSup_mul, Cslib.RelationAlgebra.instQuantale, Cslib.RelationAlgebra.leftMulResiduation_eq_leftResidual, Cslib.RelationAlgebra.rightMulResiduation_eq_rightResidual, Cslib.RelationAlgebra.inf_star_mul_ne_bot, Cslib.RelationAlgebra.atom_cycle_left, Cslib.RelationAlgebra.atom_cycle_left_iff, Cslib.RelationAlgebra.exists_atom_le_mul_right, Cslib.RelationAlgebra.exists_atom_le_mul_left, Cslib.RelationAlgebra.IsIntegral, Cslib.RelationAlgebra.IsIntegral.one_ne_bot, Cslib.RelationAlgebra.IsIntegral.nontrivial, Cslib.RelationAlgebra.one_eq_bot_iff, Cslib.RelationAlgebra.identityAtoms, Cslib.RelationAlgebra.symmetricDiversityAtoms, Cslib.RelationAlgebra.nonsymmetricDiversityAtoms, IsAtom.le_compl_iff, Cslib.RelationAlgebra.le_compl_one_of_mem_nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.disjoint_identityAtoms_symmetricDiversityAtoms, Cslib.RelationAlgebra.disjoint_identityAtoms_nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.disjoint_symmetricDiversityAtoms_nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.setOf_isAtom_eq, Cslib.RelationAlgebra.identityAtoms_eq_of_isIntegral, Cslib.RelationAlgebra.even_ncard_nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.ncard_setOf_isAtom, Cslib.RelationAlgebra.ncard_setOf_isAtom_of_isIntegral, SetRel.mul_eq_comp, SetRel.one_eq_id, SetRel.star_eq_inv, SetRel.mem_mul, SetRel.mem_one, SetRel.mem_star, SetRel.mem_leftResidual, SetRel.mem_rightResidual
statement: formalized
proof: formalized
---

# Relation algebras

`Cslib.Foundations.RelationAlgebra.Basic`, in [Cslib/Foundations/RelationAlgebra/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean), by Chris Henson.

> A relation algebra in the sense of Tarski (not to be confused with a relational algebra) is an
> extension of Boolean algebras that are designed to form an algebraic analysis of relations,
> `α → α → Prop` in Lean. They have applications in computer science such as the theory of constraint
> satisfaction as well as mathematical connections such as combinatorics.
>
> ## References
>
> * [R. Maddux, *Relation Algebras*][Maddux2006]

`Cslib.RelationAlgebra` (class, [line 39](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L39))

> The class of relation algebras. Note the notational differences from the literature. In addition
> to inheriting Mathlib's notations for Boolean algebras, `star` is used for converse, and the monoid
> reduct for composition uses multiplicative notation.

```lean
class RelationAlgebra (α : Type*) extends BooleanAlgebra α, Monoid α, StarMul α where
  sup_mul (a b c : α) : (a ⊔ b) * c = a * c ⊔ b * c
  star_sup (a b : α) : star (a ⊔ b) = star a ⊔ star b
  tarski (a b : α) : star a * (a * b)ᶜ ≤ bᶜ
```

`Cslib.CompleteRelationAlgebra` (class, [line 48](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L48))

> The relation algebra of a complete Boolean algebra.

```lean
class CompleteRelationAlgebra (α : Type*) extends RelationAlgebra α, CompleteBooleanAlgebra α
```

`Cslib.CompleteAtomicRelationAlgebra` (class, [line 51](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L51))

> The relation algebra of a complete and atomic Boolean algebra.

```lean
class CompleteAtomicRelationAlgebra (α : Type*) extends CompleteRelationAlgebra α,
    CompleteAtomicBooleanAlgebra α
```

`Cslib.RelationAlgebra.ofTarski` (definition, [line 58](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L58))

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

`Cslib.RelationAlgebra.star_mono` (theorem, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L91))

```lean
theorem star_mono : Monotone (star : α → α)
```

`Cslib.RelationAlgebra.starOrderIso` (definition, [line 97](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L97))

> Converse as an automorphism of a relation algebra.

```lean
def starOrderIso : α ≃o α
```

`Cslib.RelationAlgebra.star_bot` (theorem, [line 102](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L102))

```lean
theorem star_bot : star (⊥ : α) = ⊥
```

`Cslib.RelationAlgebra.star_le_star_iff` (theorem, [line 105](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L105))

```lean
theorem star_le_star_iff {a b : α} : star a ≤ star b ↔ a ≤ b
```

`Cslib.RelationAlgebra.star_lt_star_iff` (theorem, [line 108](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L108))

```lean
theorem star_lt_star_iff {a b : α} : star a < star b ↔ a < b
```

`Cslib.RelationAlgebra.le_star_iff` (theorem, [line 111](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L111))

```lean
theorem le_star_iff {a b : α} : a ≤ star b ↔ star a ≤ b
```

`Cslib.RelationAlgebra.star_inf` (theorem, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L114))

```lean
theorem star_inf (a b : α) : star (a ⊓ b) = star a ⊓ star b
```

`Cslib.RelationAlgebra.star_compl` (theorem, [line 117](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L117))

```lean
theorem star_compl (a : α) : star aᶜ = (star a)ᶜ
```

`Cslib.RelationAlgebra.star_sdiff` (theorem, [line 121](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L121))

```lean
theorem star_sdiff (a b : α) : star (a \ b) = star a \ star b
```

`Cslib.RelationAlgebra.star_sSup` (theorem, [line 125](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L125))

```lean
theorem star_sSup {α : Type*} [CompleteRelationAlgebra α] (s : Set α) :
    star (sSup s) = ⨆ a ∈ s, star a
```

`Cslib.RelationAlgebra.mul_sup` (theorem, [line 128](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L128))

```lean
theorem mul_sup (a b c : α) : a * (b ⊔ c) = a * b ⊔ a * c
```

`Cslib.RelationAlgebra.mul_bot` (theorem, [line 139](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L139))

```lean
theorem mul_bot (a : α) : a * ⊥ = ⊥
```

`Cslib.RelationAlgebra.bot_mul` (theorem, [line 142](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L142))

```lean
theorem bot_mul (a : α) : ⊥ * a = ⊥
```

`Cslib.RelationAlgebra.inf_mul_le` (theorem, [line 144](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L144))

```lean
theorem inf_mul_le (a b c : α) : (a ⊓ b) * c ≤ a * c ⊓ b * c
```

`Cslib.RelationAlgebra.mul_inf_le` (theorem, [line 148](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L148))

```lean
theorem mul_inf_le (a b c : α) : a * (b ⊓ c) ≤ a * b ⊓ a * c
```

`Cslib.RelationAlgebra.isAtom_star_iff` (theorem, [line 153](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L153))

```lean
theorem isAtom_star_iff {a : α} : IsAtom (star a) ↔ IsAtom a
```

`Cslib.RelationAlgebra.left_modular` (theorem, [line 156](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L156))

```lean
theorem left_modular (a b c : α) : a * b ⊓ c ≤ a * (b ⊓ star a * c)
```

`Cslib.RelationAlgebra.right_modular` (theorem, [line 165](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L165))

```lean
theorem right_modular (a b c : α) : a * b ⊓ c ≤ (a ⊓ c * star b) * b
```

`Cslib.RelationAlgebra.le_mul_star_mul` (lemma, [line 169](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L169))

```lean
lemma le_mul_star_mul (a : α) : a ≤ a * star a * a
```

`Cslib.RelationAlgebra.mul_le_compl_right` (theorem, [line 174](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L174))

```lean
theorem mul_le_compl_right (a b c : α) : a * b ≤ cᶜ ↔ star a * c ≤ bᶜ
```

`Cslib.RelationAlgebra.mul_le_compl_left` (theorem, [line 179](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L179))

```lean
theorem mul_le_compl_left (a b c : α) : a * b ≤ cᶜ ↔ c * star b ≤ aᶜ
```

`Cslib.RelationAlgebra.mul_le_compl_star_tfae` (theorem, [line 183](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L183))

```lean
theorem mul_le_compl_star_tfae {a b c : α} :
    [a * b ≤ (star c)ᶜ, b * c ≤ (star a)ᶜ, c * a ≤ (star b)ᶜ].TFAE
```

`Cslib.RelationAlgebra.leftResidual` (definition, [line 192](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L192))

> The right residual, defined so that `a ≤ leftResidual b c ↔ a * b ≤ c`.

```lean
def leftResidual (a b : α) : α
```

`Cslib.RelationAlgebra.le_leftResidual_iff` (theorem, [line 194](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L194))

```lean
theorem le_leftResidual_iff {a b c : α} : a ≤ leftResidual b c ↔ a * b ≤ c
```

`Cslib.RelationAlgebra.rightResidual` (definition, [line 198](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L198))

> The left residual, defined so that `a ≤ rightResidual b c ↔ b * a ≤ c`.

```lean
def rightResidual (a b : α) : α
```

`Cslib.RelationAlgebra.le_rightResidual_iff` (theorem, [line 200](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L200))

```lean
theorem le_rightResidual_iff {a b c : α} : a ≤ rightResidual b c ↔ b * a ≤ c
```

`Cslib.RelationAlgebra.star_leftResidual` (theorem, [line 204](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L204))

```lean
theorem star_leftResidual {a b : α} :
    star (leftResidual a b) = rightResidual (star a) (star b)
```

`Cslib.RelationAlgebra.star_rightResidual` (theorem, [line 211](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L211))

```lean
theorem star_rightResidual {a b : α} :
    star (rightResidual a b) = leftResidual (star a) (star b)
```

`Cslib.RelationAlgebra.mul_sSup` (theorem, [line 217](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L217))

```lean
theorem mul_sSup {α : Type*} [CompleteRelationAlgebra α] {a : α} {s : Set α} :
    a * sSup s = ⨆ b ∈ s, a * b
```

`Cslib.RelationAlgebra.sSup_mul` (theorem, [line 222](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L222))

```lean
theorem sSup_mul {α : Type*} [CompleteRelationAlgebra α] {s : Set α} {b : α} :
    sSup s * b = ⨆ a ∈ s, a * b
```

`Cslib.RelationAlgebra.instQuantale` (instance, [line 227](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L227))

```lean
instance instQuantale (α : Type*) [CompleteRelationAlgebra α] : IsQuantale α
```

`Cslib.RelationAlgebra.leftMulResiduation_eq_leftResidual` (theorem, [line 232](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L232))

```lean
theorem leftMulResiduation_eq_leftResidual {α : Type*} [CompleteRelationAlgebra α]
    {a b : α} : a ⇨ₗ b = leftResidual a b
```

`Cslib.RelationAlgebra.rightMulResiduation_eq_rightResidual` (theorem, [line 238](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L238))

```lean
theorem rightMulResiduation_eq_rightResidual {α : Type*} [CompleteRelationAlgebra α]
    {a b : α} : a ⇨ᵣ b = rightResidual a b
```

`Cslib.RelationAlgebra.inf_star_mul_ne_bot` (theorem, [line 244](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L244))

> If a nonzero element lies below a product, the right factor meets its converse image.

```lean
theorem inf_star_mul_ne_bot {r s p : α} (hp : p ≠ ⊥) (h : p ≤ r * s) : s ⊓ star r * p ≠ ⊥
```

`Cslib.RelationAlgebra.atom_cycle_left` (theorem, [line 247](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L247))

```lean
theorem atom_cycle_left {r s p : α} (hs : IsAtom s) (hp : p ≠ ⊥) (h : p ≤ r * s) :
    s ≤ star r * p
```

`Cslib.RelationAlgebra.atom_cycle_left_iff` (theorem, [line 252](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L252))

> For atoms, the cycle law is an equivalence.

```lean
theorem atom_cycle_left_iff {r s p : α} (hs : IsAtom s) (hp : IsAtom p) :
    p ≤ r * s ↔ s ≤ star r * p
```

`Cslib.RelationAlgebra.exists_atom_le_mul_right` (theorem, [line 257](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L257))

> If an atom lies below a product, its right factor can be replaced by an atom below it.

```lean
theorem exists_atom_le_mul_right [IsAtomic α] {a b p : α} (hp : IsAtom p) (h : p ≤ a * b) :
    ∃ s, IsAtom s ∧ s ≤ b ∧ p ≤ a * s
```

`Cslib.RelationAlgebra.exists_atom_le_mul_left` (theorem, [line 264](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L264))

> If an atom lies below a product, its left factor can be replaced by an atom below it.

```lean
theorem exists_atom_le_mul_left [IsAtomic α] {a b p : α} (hp : IsAtom p) (h : p ≤ a * b) :
    ∃ r, IsAtom r ∧ r ≤ a ∧ p ≤ r * b
```

`Cslib.RelationAlgebra.IsIntegral` (definition, [line 271](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L271))

> A relation algebra is *integral* when its identity is an atom.

```lean
def IsIntegral (α : Type*) [RelationAlgebra α] : Prop
```

`Cslib.RelationAlgebra.IsIntegral.one_ne_bot` (lemma, [line 273](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L273))

```lean
lemma IsIntegral.one_ne_bot {α : Type*} [RelationAlgebra α] (h : IsIntegral α) : (1 : α) ≠ ⊥
```

`Cslib.RelationAlgebra.IsIntegral.nontrivial` (lemma, [line 276](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L276))

```lean
lemma IsIntegral.nontrivial {α : Type*} [RelationAlgebra α] (h : IsIntegral α) : Nontrivial α
```

`Cslib.RelationAlgebra.one_eq_bot_iff` (lemma, [line 279](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L279))

```lean
lemma one_eq_bot_iff (α : Type*) [RelationAlgebra α] : (1 : α) = ⊥ ↔ Subsingleton α
```

`Cslib.RelationAlgebra.identityAtoms` (definition, [line 285](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L285))

> The set of identity atoms.

```lean
def identityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`Cslib.RelationAlgebra.symmetricDiversityAtoms` (definition, [line 288](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L288))

> The set of symmetric diversity atoms, those below the complement of identity.

```lean
def symmetricDiversityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`Cslib.RelationAlgebra.nonsymmetricDiversityAtoms` (definition, [line 293](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L293))

> The set of nonsymmetric diversity atoms. The diversity condition follows from
> `le_compl_one_of_mem_nonsymmetricDiversityAtoms`.

```lean
def nonsymmetricDiversityAtoms (α : Type*) [RelationAlgebra α] : Set α
```

`IsAtom.le_compl_iff` (theorem, [line 296](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L296))

```lean
theorem _root_.IsAtom.le_compl_iff {α : Type*} [HeytingAlgebra α] {a b : α} (ha : IsAtom a) :
    a ≤ bᶜ ↔ ¬a ≤ b
```

`Cslib.RelationAlgebra.le_compl_one_of_mem_nonsymmetricDiversityAtoms` (theorem, [line 301](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L301))

> Every nonsymmetric atom lies below the complement of identity.

```lean
theorem le_compl_one_of_mem_nonsymmetricDiversityAtoms {a : α}
    (h : a ∈ nonsymmetricDiversityAtoms α) : a ≤ 1ᶜ
```

`Cslib.RelationAlgebra.disjoint_identityAtoms_symmetricDiversityAtoms` (theorem, [line 318](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L318))

```lean
theorem disjoint_identityAtoms_symmetricDiversityAtoms :
    Disjoint (identityAtoms α) (symmetricDiversityAtoms α)
```

`Cslib.RelationAlgebra.disjoint_identityAtoms_nonsymmetricDiversityAtoms` (theorem, [line 325](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L325))

```lean
theorem disjoint_identityAtoms_nonsymmetricDiversityAtoms :
    Disjoint (identityAtoms α) (nonsymmetricDiversityAtoms α)
```

`Cslib.RelationAlgebra.disjoint_symmetricDiversityAtoms_nonsymmetricDiversityAtoms` (theorem, [line 332](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L332))

```lean
theorem disjoint_symmetricDiversityAtoms_nonsymmetricDiversityAtoms :
    Disjoint (symmetricDiversityAtoms α) (nonsymmetricDiversityAtoms α)
```

`Cslib.RelationAlgebra.setOf_isAtom_eq` (theorem, [line 338](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L338))

```lean
theorem setOf_isAtom_eq : {a : α | IsAtom a} =
    identityAtoms α ∪ symmetricDiversityAtoms α ∪ nonsymmetricDiversityAtoms α
```

`Cslib.RelationAlgebra.identityAtoms_eq_of_isIntegral` (theorem, [line 342](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L342))

```lean
theorem identityAtoms_eq_of_isIntegral (h : IsIntegral α) : identityAtoms α = {1}
```

`Cslib.RelationAlgebra.even_ncard_nonsymmetricDiversityAtoms` (theorem, [line 350](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L350))

```lean
theorem even_ncard_nonsymmetricDiversityAtoms : Even (nonsymmetricDiversityAtoms α).ncard
```

`Cslib.RelationAlgebra.ncard_setOf_isAtom` (theorem, [line 358](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L358))

```lean
theorem ncard_setOf_isAtom [Finite α] :
    {a : α | IsAtom a}.ncard = (identityAtoms α).ncard +
      (symmetricDiversityAtoms α).ncard + (nonsymmetricDiversityAtoms α).ncard
```

`Cslib.RelationAlgebra.ncard_setOf_isAtom_of_isIntegral` (theorem, [line 363](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L363))

```lean
theorem ncard_setOf_isAtom_of_isIntegral [Finite α] (h : IsIntegral α) :
    {a : α | IsAtom a}.ncard =
      1 + (symmetricDiversityAtoms α).ncard + (nonsymmetricDiversityAtoms α).ncard
```

`SetRel.mul_eq_comp` (theorem, [line 391](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L391))

```lean
theorem _root_.SetRel.mul_eq_comp : R * S = R.comp S
```

`SetRel.one_eq_id` (theorem, [line 393](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L393))

```lean
theorem _root_.SetRel.one_eq_id : (1 : SetRel α α) = SetRel.id
```

`SetRel.star_eq_inv` (theorem, [line 395](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L395))

```lean
theorem _root_.SetRel.star_eq_inv : star R = R.inv
```

`SetRel.mem_mul` (theorem, [line 397](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L397))

```lean
theorem _root_.SetRel.mem_mul : a ~[R * S] c ↔ ∃ b, a ~[R] b ∧ b ~[S] c
```

`SetRel.mem_one` (theorem, [line 399](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L399))

```lean
theorem _root_.SetRel.mem_one : a ~[(1 : SetRel α α)] b ↔ a = b
```

`SetRel.mem_star` (theorem, [line 401](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L401))

```lean
theorem _root_.SetRel.mem_star : a ~[star R] b ↔ b ~[R] a
```

`SetRel.mem_leftResidual` (theorem, [line 403](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L403))

```lean
theorem _root_.SetRel.mem_leftResidual : a ~[leftResidual R S] b ↔ ∀ c, b ~[R] c → a ~[S] c
```

`SetRel.mem_rightResidual` (theorem, [line 406](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean#L406))

```lean
theorem _root_.SetRel.mem_rightResidual : a ~[rightResidual R S] b ↔ ∀ c, c ~[R] a → c ~[S] b
```

## Depends on

- [Huntington's axioms for Boolean Algebras](../order/huntington.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Basic.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Basic.json)
