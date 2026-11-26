---
declaration: module
origin: cited
lean: Representation.tprod_apply_one, Representation.tprod_apply_one_tmul, Representation.tprod_apply_tmul_one, Representation.tprod_apply_mul, Representation.restrictSubalgebra, Representation.restrictScalars, Representation.restrictScalars_apply, Representation.apply_one_of_mul
statement: formalized
proof: formalized
---

# Representations acting by algebra maps

The module `PhyslibAlpha.Mathematics.AlgebraRepresentation`, [PhyslibAlpha/Mathematics/AlgebraRepresentation.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean): 19 declarations, 13 with a docstring.

> Representations on algebras which respect the multiplication, and algebra maps between them.

## i. Overview

> A representation of a monoid on an algebra need not respect the multiplication. The ones
> that do are the ones a field theory uses, acting on an algebra of fields, and this file
> collects the constructions on them that Mathlib does not have.
>
> Section A is about `Representation.tprod` on a tensor product of two algebras. The unit and
> the product of `A ⊗[k] B` are given by those of the factors, so a pair of unit-preserving
> or multiplicative representations gives one on the tensor product. The lemmas are stated at
> abstract types with the factor laws as hypotheses, which is what lets them be applied at a
> large concrete algebra without unfolding it: neither the unit nor the product of a free
> algebra presented as a quotient can be reduced cheaply.
>
> Section B restricts a representation to a subalgebra it preserves. The invariance
> hypothesis is stated pointwise, in the form the ambient invariance lemmas produce.
>
> Section C restricts the scalars of a representation, so that a representation on a complex
> vector space is in particular a representation on the underlying real vector space. Section D
> turns a multiplicative representation of a group into one by algebra maps.
>
> Section E bundles an algebra map together with equivariance for two independently supplied
> pairs of representations of two monoids, the two target representations being multiplicative
> on the whole target: `Representation.EquivariantAlgHom`. Nothing relates the two pairs, the
> target actions are not assumed to commute, and they are not assumed unital, which over a
> monoid does not follow from multiplicativity.

## ii. Key results

> - `Representation.tprod_apply_one`, `Representation.tprod_apply_one_tmul`,
>   `Representation.tprod_apply_tmul_one` : the unit laws on a tensor product.
> - `Representation.tprod_apply_mul` : multiplicativity on a tensor product.
> - `Representation.restrictSubalgebra` : the restriction to an invariant subalgebra.
> - `Representation.restrictScalars` : the restriction of scalars.
> - `Representation.toAlgHom` : a multiplicative representation of a group as algebra maps.
> - `Representation.EquivariantAlgHom` : an algebra map intertwining two pairs of
>   representations, with `EquivariantAlgHom.id`, `EquivariantAlgHom.comp`,
>   `EquivariantAlgHom.restrictSubalgebra` and `EquivariantAlgHom.compFst`.

## iv. References

> * None.

## A. Tensor products of multiplicative representations

**`Representation.tprod_apply_one`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L79).

> The tensor product of two unit-preserving representations preserves the unit.

```lean
lemma tprod_apply_one {k G A B : Type*} [CommSemiring k] [Monoid G]
    [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G)
    (hρ : ρ g 1 = 1) (hσ : σ g 1 = 1) : (ρ.tprod σ) g 1 = 1
```

**`Representation.tprod_apply_one_tmul`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L87).

> On a pure tensor whose left entry is the unit only the right factor moves.

```lean
lemma tprod_apply_one_tmul {k G A B : Type*} [CommSemiring k]
    [Monoid G] [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G)
    (hρ : ρ g 1 = 1) (y : B) :
    (ρ.tprod σ) g ((1 : A) ⊗ₜ[k] y) = (1 : A) ⊗ₜ[k] σ g y
```

**`Representation.tprod_apply_tmul_one`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L95).

> On a pure tensor whose right entry is the unit only the left factor moves.

```lean
lemma tprod_apply_tmul_one {k G A B : Type*} [CommSemiring k]
    [Monoid G] [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G) (x : A)
    (hσ : σ g 1 = 1) :
    (ρ.tprod σ) g (x ⊗ₜ[k] (1 : B)) = ρ g x ⊗ₜ[k] (1 : B)
```

**`Representation.tprod_apply_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L104).

> The tensor product of two multiplicative representations on algebras is
> multiplicative.

```lean
lemma tprod_apply_mul {k G A B : Type*} [CommSemiring k] [Monoid G]
    [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B)
    (hρ : ∀ (g : G) (x y : A), ρ g (x * y) = ρ g x * ρ g y)
    (hσ : ∀ (g : G) (x y : B), σ g (x * y) = σ g x * σ g y)
    (g : G) (x y : A ⊗[k] B) :
    (ρ.tprod σ) g (x * y) = (ρ.tprod σ) g x * (ρ.tprod σ) g y
```

## B. Restriction to an invariant subalgebra

**`Representation.restrictSubalgebra`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L131).

> The restriction of a representation to a subalgebra each group element preserves.

```lean
noncomputable def restrictSubalgebra {k A G : Type*} [CommSemiring k]
    [Monoid G] [Semiring A] [Algebra k A] (ρ : Representation k G A) (S : Subalgebra k A)
    (hS : ∀ (g : G) {x : A}, x ∈ S → ρ g x ∈ S) : Representation k G S
```

## C. Restriction of scalars

**`Representation.restrictScalars`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L151).

> The restriction of scalars of a representation. A representation on an `S`-module is a
> representation on the same space as an `R`-module, for `R` acting through `S`.

```lean
def restrictScalars (R : Type*) {S G V : Type*} [CommSemiring R] [CommSemiring S] [Monoid G]
    [AddCommMonoid V] [Module R V] [Module S V] [LinearMap.CompatibleSMul V V R S]
    (ρ : Representation S G V) : Representation R G V
```

**`Representation.restrictScalars_apply`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L159).

```lean
lemma restrictScalars_apply (R : Type*) {S G V : Type*} [CommSemiring R] [CommSemiring S]
    [Monoid G] [AddCommMonoid V] [Module R V] [Module S V] [LinearMap.CompatibleSMul V V R S]
    (ρ : Representation S G V) (g : G) (x : V) : ρ.restrictScalars R g x = ρ g x
```

## D. Multiplicative representations as algebra maps

**`Representation.apply_one_of_mul`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L178).

> A representation of a group acting by multiplicative maps preserves the unit. The
> action of `g` is surjective, its inverse being the action of `g⁻¹`, so `ρ g 1` is a left
> unit on the whole algebra.

```lean
lemma apply_one_of_mul (g : G) : ρ g 1 = 1
```

**`Representation.toAlgHom`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L188).

> A representation of a group acting by multiplicative maps acts by algebra
> endomorphisms.

```lean
noncomputable def toAlgHom (g : G) : A →ₐ[k] A
```

**`Representation.toAlgHom_apply`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L198).

```lean
lemma toAlgHom_apply (g : G) (x : A) : ρ.toAlgHom hρ g x = ρ g x
```

## E. Equivariant algebra maps

**`Representation.EquivariantAlgHom`**, a structure, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L221).

> An algebra map `A →ₐ[k] B` intertwining two pairs of representations, `ρ₁, σ₁` of the
> monoid `G₁` and `ρ₂, σ₂` of the monoid `G₂`, with both target representations multiplicative
> on the whole of `B`. The two pairs are independent. The actions of `G₁` and `G₂` are not
> assumed to commute, and no relation between them is used. Unit preservation is not a field
> and does not follow from multiplicativity over a monoid; when the acting monoid is a group
> and the target is a ring it does (`Representation.apply_one_of_mul`), and the target action
> is then by algebra endomorphisms.

```lean
structure EquivariantAlgHom (ρ₁ : Representation k G₁ A) (σ₁ : Representation k G₁ B)
    (ρ₂ : Representation k G₂ A) (σ₂ : Representation k G₂ B) where
  /-- The underlying algebra map. -/
  toAlgHom : A →ₐ[k] B
  /-- The map is equivariant for the first pair of representations. -/
  map_fst : ∀ (g : G₁) (x : A), toAlgHom (ρ₁ g x) = σ₁ g (toAlgHom x)
  /-- The map is equivariant for the second pair of representations. -/
  map_snd : ∀ (g : G₂) (x : A), toAlgHom (ρ₂ g x) = σ₂ g (toAlgHom x)
  /-- The first target action is multiplicative on the whole of `B`. -/
  fst_mul : ∀ (g : G₁) (b₁ b₂ : B), σ₁ g (b₁ * b₂) = σ₁ g b₁ * σ₁ g b₂
  /-- The second target action is multiplicative on the whole of `B`. -/
  snd_mul : ∀ (g : G₂) (b₁ b₂ : B), σ₂ g (b₁ * b₂) = σ₂ g b₁ * σ₂ g b₂
```

**`Representation.EquivariantAlgHom.id`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L241).

> The identity map of an algebra carrying two multiplicative representations.

```lean
def id (h₁ : ∀ (g : G₁) (x y : A), ρ₁ g (x * y) = ρ₁ g x * ρ₁ g y)
    (h₂ : ∀ (g : G₂) (x y : A), ρ₂ g (x * y) = ρ₂ g x * ρ₂ g y) :
    EquivariantAlgHom ρ₁ ρ₁ ρ₂ ρ₂
```

**`Representation.EquivariantAlgHom.id_toAlgHom`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L251).

```lean
lemma id_toAlgHom (h₁ : ∀ (g : G₁) (x y : A), ρ₁ g (x * y) = ρ₁ g x * ρ₁ g y)
    (h₂ : ∀ (g : G₂) (x y : A), ρ₂ g (x * y) = ρ₂ g x * ρ₂ g y) :
    (EquivariantAlgHom.id ρ₁ ρ₂ h₁ h₂).toAlgHom = AlgHom.id k A
```

**`Representation.EquivariantAlgHom.comp`**, a def, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L258).

> The precomposition with an algebra map into the source intertwining two representations
> on its own source with the two source representations; the target and its two actions are
> unchanged.

```lean
def comp {A' : Type*} [Semiring A'] [Algebra k A'] {ρ₁' : Representation k G₁ A'}
    {ρ₂' : Representation k G₂ A'} (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : A' →ₐ[k] A)
    (hφ₁ : ∀ (g : G₁) (x : A'), φ (ρ₁' g x) = ρ₁ g (φ x))
    (hφ₂ : ∀ (g : G₂) (x : A'), φ (ρ₂' g x) = ρ₂ g (φ x)) :
    EquivariantAlgHom ρ₁' σ₁ ρ₂' σ₂
```

**`Representation.EquivariantAlgHom.comp_toAlgHom`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L270).

```lean
lemma comp_toAlgHom {A' : Type*} [Semiring A'] [Algebra k A'] {ρ₁' : Representation k G₁ A'}
    {ρ₂' : Representation k G₂ A'} (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : A' →ₐ[k] A)
    (hφ₁ : ∀ (g : G₁) (x : A'), φ (ρ₁' g x) = ρ₁ g (φ x))
    (hφ₂ : ∀ (g : G₂) (x : A'), φ (ρ₂' g x) = ρ₂ g (φ x)) :
    (f.comp φ hφ₁ hφ₂).toAlgHom = f.toAlgHom.comp φ
```

**`Representation.EquivariantAlgHom.restrictSubalgebra`**, a def, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L278).

> The restriction to a subalgebra of the source preserved by both source representations,
> along its inclusion; the target and its two actions are unchanged.

```lean
noncomputable def restrictSubalgebra (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (S : Subalgebra k A)
    (hS₁ : ∀ (g : G₁) {x : A}, x ∈ S → ρ₁ g x ∈ S)
    (hS₂ : ∀ (g : G₂) {x : A}, x ∈ S → ρ₂ g x ∈ S) :
    EquivariantAlgHom (ρ₁.restrictSubalgebra S hS₁) σ₁ (ρ₂.restrictSubalgebra S hS₂) σ₂
```

**`Representation.EquivariantAlgHom.restrictSubalgebra_toAlgHom_apply`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L285).

```lean
lemma restrictSubalgebra_toAlgHom_apply (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (S : Subalgebra k A)
    (hS₁ : ∀ (g : G₁) {x : A}, x ∈ S → ρ₁ g x ∈ S)
    (hS₂ : ∀ (g : G₂) {x : A}, x ∈ S → ρ₂ g x ∈ S) (x : S) :
    (f.restrictSubalgebra S hS₁ hS₂).toAlgHom x = f.toAlgHom x
```

**`Representation.EquivariantAlgHom.compFst`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L292).

> The precomposition of the first pair of representations with a monoid map; the algebra
> map is unchanged.

```lean
def compFst {H : Type*} [Monoid H] (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : H →* G₁) :
    EquivariantAlgHom (ρ₁.comp φ) (σ₁.comp φ) ρ₂ σ₂
```

**`Representation.EquivariantAlgHom.compFst_toAlgHom`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L301).

```lean
lemma compFst_toAlgHom {H : Type*} [Monoid H] (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : H →* G₁) :
    (f.compFst φ).toAlgHom = f.toAlgHom
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/AlgebraRepresentation.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean)
