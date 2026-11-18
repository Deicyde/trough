---
declaration: module
origin: cited
lean: Representation.tprod_apply_one, Representation.tprod_apply_one_tmul, Representation.tprod_apply_tmul_one, Representation.tprod_apply_mul, Representation.restrictSubalgebra, Representation.coe_restrictSubalgebra, Representation.inclusion_restrictSubalgebra, Representation.restrictScalars
statement: formalized
proof: formalized
---

# Representations acting by algebra maps

The module `PhyslibAlpha.Mathematics.AlgebraRepresentation`, [PhyslibAlpha/Mathematics/AlgebraRepresentation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean): 31 declarations, 21 with a docstring.

## i. Overview

> A representation of a monoid on an algebra need not respect the multiplication; the ones
> that do are the ones a field theory uses, and this file collects the two constructions on
> them that are otherwise missing.
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
> Section C restricts the scalars of a representation: a representation on a complex vector
> space is in particular a representation on the underlying real vector space.
>
> Section E bundles an algebra map together with equivariance for two independently supplied
> pairs of representations of two monoids, the two target representations being multiplicative
> on the whole target: `Representation.EquivariantAlgHom`. Nothing relates the two pairs, the
> target actions are not assumed to commute, and they are not assumed unital, which over a
> monoid does not follow from multiplicativity. Section F base changes such a map along an
> extension of scalars, in both directions, and section G records the one affine identity an
> algebra map is used for when a representation acts on generators by a shift.

## ii. Key results

> - `Representation.tprod_apply_one`, `Representation.tprod_apply_one_tmul`,
>   `Representation.tprod_apply_tmul_one` : the unit laws on a tensor product.
> - `Representation.tprod_apply_mul` : multiplicativity on a tensor product.
> - `Representation.restrictSubalgebra` : the restriction to an invariant subalgebra, with
>   `Representation.inclusion_restrictSubalgebra` for two nested ones.
> - `Representation.restrictScalars` : the restriction of scalars.
> - `Representation.toAlgHom` : a multiplicative representation of a group as algebra maps.
> - `Representation.EquivariantAlgHom` : an algebra map intertwining two pairs of
>   representations, with `EquivariantAlgHom.id`, `EquivariantAlgHom.comp`,
>   `EquivariantAlgHom.compEquiv`, `EquivariantAlgHom.restrictSubalgebra` and
>   `EquivariantAlgHom.compFst`.
> - `Representation.baseChange` : the base change of a representation, with
>   `Representation.baseChange_naturality`.
> - `Representation.liftEquiv_baseChange` : base change preserves equivariance, and
>   `Representation.EquivariantAlgHom.liftEquivBaseChange` : equivariant maps out of a base
>   change are the equivariant maps over the smaller ring.
> - `AlgHom.map_add_smul_one` : an algebra map on an affine combination `x + z • 1`.

## iv. References

> * None.

## A. Tensor products of multiplicative representations

**`Representation.tprod_apply_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L88).

> The tensor product of two unit-preserving representations preserves the unit.

```lean
lemma tprod_apply_one {k G A B : Type*} [CommSemiring k] [Monoid G]
    [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G)
    (hρ : ρ g 1 = 1) (hσ : σ g 1 = 1) : (ρ.tprod σ) g 1 = 1
```

**`Representation.tprod_apply_one_tmul`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L96).

> On a pure tensor whose left entry is the unit only the right factor moves.

```lean
lemma tprod_apply_one_tmul {k G A B : Type*} [CommSemiring k]
    [Monoid G] [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G)
    (hρ : ρ g 1 = 1) (y : B) :
    (ρ.tprod σ) g ((1 : A) ⊗ₜ[k] y) = (1 : A) ⊗ₜ[k] σ g y
```

**`Representation.tprod_apply_tmul_one`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L104).

> On a pure tensor whose right entry is the unit only the left factor moves.

```lean
lemma tprod_apply_tmul_one {k G A B : Type*} [CommSemiring k]
    [Monoid G] [Ring A] [Algebra k A] [Ring B] [Algebra k B]
    (ρ : Representation k G A) (σ : Representation k G B) (g : G) (x : A)
    (hσ : σ g 1 = 1) :
    (ρ.tprod σ) g (x ⊗ₜ[k] (1 : B)) = ρ g x ⊗ₜ[k] (1 : B)
```

**`Representation.tprod_apply_mul`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L113).

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

**`Representation.restrictSubalgebra`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L140).

> The restriction of a representation to a subalgebra each group element preserves.

```lean
noncomputable def restrictSubalgebra {k A G : Type*} [CommSemiring k]
    [Monoid G] [Semiring A] [Algebra k A] (ρ : Representation k G A) (S : Subalgebra k A)
    (hS : ∀ (g : G) {x : A}, x ∈ S → ρ g x ∈ S) : Representation k G S
```

**`Representation.coe_restrictSubalgebra`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L153).

```lean
lemma coe_restrictSubalgebra {k A G : Type*} [CommSemiring k]
    [Monoid G] [Semiring A] [Algebra k A] (ρ : Representation k G A) (S : Subalgebra k A)
    (hS : ∀ (g : G) {x : A}, x ∈ S → ρ g x ∈ S) (g : G) (x : S) :
    (ρ.restrictSubalgebra S hS g x : A) = ρ g (x : A)
```

**`Representation.inclusion_restrictSubalgebra`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L160).

> The restrictions to two nested invariant subalgebras agree along the inclusion of the
> smaller into the larger.

```lean
lemma inclusion_restrictSubalgebra {k A G : Type*} [CommSemiring k]
    [Monoid G] [Semiring A] [Algebra k A] (ρ : Representation k G A) {S S' : Subalgebra k A}
    (h : S ≤ S') (hS : ∀ (g : G) {x : A}, x ∈ S → ρ g x ∈ S)
    (hS' : ∀ (g : G) {x : A}, x ∈ S' → ρ g x ∈ S') (g : G) (x : S) :
    Subalgebra.inclusion h (ρ.restrictSubalgebra S hS g x)
      = ρ.restrictSubalgebra S' hS' g (Subalgebra.inclusion h x)
```

## C. Restriction of scalars

**`Representation.restrictScalars`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L175).

> The restriction of scalars of a representation: a representation on an `S`-module is a
> representation on the same space as an `R`-module, for `R` acting through `S`.

```lean
def restrictScalars (R : Type*) {S G V : Type*} [CommSemiring R] [CommSemiring S] [Monoid G]
    [AddCommMonoid V] [Module R V] [Module S V] [LinearMap.CompatibleSMul V V R S]
    (ρ : Representation S G V) : Representation R G V
```

**`Representation.restrictScalars_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L183).

```lean
lemma restrictScalars_apply (R : Type*) {S G V : Type*} [CommSemiring R] [CommSemiring S]
    [Monoid G] [AddCommMonoid V] [Module R V] [Module S V] [LinearMap.CompatibleSMul V V R S]
    (ρ : Representation S G V) (g : G) (x : V) : ρ.restrictScalars R g x = ρ g x
```

## D. Multiplicative representations as algebra maps

**`Representation.apply_one_of_mul`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L202).

> A representation of a group acting by multiplicative maps preserves the unit. The
> action of `g` is surjective, its inverse being the action of `g⁻¹`, so `ρ g 1` is a left
> unit on the whole algebra.

```lean
lemma apply_one_of_mul (g : G) : ρ g 1 = 1
```

**`Representation.toAlgHom`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L212).

> A representation of a group acting by multiplicative maps acts by algebra
> endomorphisms.

```lean
noncomputable def toAlgHom (g : G) : A →ₐ[k] A
```

**`Representation.toAlgHom_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L222).

```lean
lemma toAlgHom_apply (g : G) (x : A) : ρ.toAlgHom hρ g x = ρ g x
```

## E. Equivariant algebra maps

**`Representation.EquivariantAlgHom`**, a structure, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L245).

> An algebra map `A →ₐ[k] B` intertwining two pairs of representations, `ρ₁, σ₁` of the
> monoid `G₁` and `ρ₂, σ₂` of the monoid `G₂`, with both target representations multiplicative
> on the whole of `B`. The two pairs are independent: the actions of `G₁` and `G₂` are not
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

**`Representation.EquivariantAlgHom.id`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L265).

> The identity map of an algebra carrying two multiplicative representations.

```lean
def id (h₁ : ∀ (g : G₁) (x y : A), ρ₁ g (x * y) = ρ₁ g x * ρ₁ g y)
    (h₂ : ∀ (g : G₂) (x y : A), ρ₂ g (x * y) = ρ₂ g x * ρ₂ g y) :
    EquivariantAlgHom ρ₁ ρ₁ ρ₂ ρ₂
```

**`Representation.EquivariantAlgHom.id_toAlgHom`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L275).

```lean
lemma id_toAlgHom (h₁ : ∀ (g : G₁) (x y : A), ρ₁ g (x * y) = ρ₁ g x * ρ₁ g y)
    (h₂ : ∀ (g : G₂) (x y : A), ρ₂ g (x * y) = ρ₂ g x * ρ₂ g y) :
    (EquivariantAlgHom.id ρ₁ ρ₂ h₁ h₂).toAlgHom = AlgHom.id k A
```

**`Representation.EquivariantAlgHom.comp`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L282).

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

**`Representation.EquivariantAlgHom.comp_toAlgHom`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L294).

```lean
lemma comp_toAlgHom {A' : Type*} [Semiring A'] [Algebra k A'] {ρ₁' : Representation k G₁ A'}
    {ρ₂' : Representation k G₂ A'} (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : A' →ₐ[k] A)
    (hφ₁ : ∀ (g : G₁) (x : A'), φ (ρ₁' g x) = ρ₁ g (φ x))
    (hφ₂ : ∀ (g : G₂) (x : A'), φ (ρ₂' g x) = ρ₂ g (φ x)) :
    (f.comp φ hφ₁ hφ₂).toAlgHom = f.toAlgHom.comp φ
```

**`Representation.EquivariantAlgHom.compEquiv`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L302).

> Precomposition with an algebra equivalence of the sources intertwining the source
> representations: equivariant maps out of equivalent sources correspond.

```lean
noncomputable def compEquiv {A' : Type*} [Semiring A'] [Algebra k A']
    {ρ₁' : Representation k G₁ A'} {ρ₂' : Representation k G₂ A'} (e : A' ≃ₐ[k] A)
    (he₁ : ∀ (g : G₁) (x : A'), e (ρ₁' g x) = ρ₁ g (e x))
    (he₂ : ∀ (g : G₂) (x : A'), e (ρ₂' g x) = ρ₂ g (e x)) :
    EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂ ≃ EquivariantAlgHom ρ₁' σ₁ ρ₂' σ₂
```

**`Representation.EquivariantAlgHom.compEquiv_toAlgHom`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L319).

```lean
lemma compEquiv_toAlgHom {A' : Type*} [Semiring A'] [Algebra k A']
    {ρ₁' : Representation k G₁ A'} {ρ₂' : Representation k G₂ A'} (e : A' ≃ₐ[k] A)
    (he₁ : ∀ (g : G₁) (x : A'), e (ρ₁' g x) = ρ₁ g (e x))
    (he₂ : ∀ (g : G₂) (x : A'), e (ρ₂' g x) = ρ₂ g (e x))
    (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) :
    (compEquiv e he₁ he₂ f).toAlgHom = f.toAlgHom.comp e.toAlgHom
```

**`Representation.EquivariantAlgHom.compEquiv_symm_toAlgHom`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L327).

```lean
lemma compEquiv_symm_toAlgHom {A' : Type*} [Semiring A'] [Algebra k A']
    {ρ₁' : Representation k G₁ A'} {ρ₂' : Representation k G₂ A'} (e : A' ≃ₐ[k] A)
    (he₁ : ∀ (g : G₁) (x : A'), e (ρ₁' g x) = ρ₁ g (e x))
    (he₂ : ∀ (g : G₂) (x : A'), e (ρ₂' g x) = ρ₂ g (e x))
    (f : EquivariantAlgHom ρ₁' σ₁ ρ₂' σ₂) :
    ((compEquiv e he₁ he₂).symm f).toAlgHom = f.toAlgHom.comp e.symm.toAlgHom
```

**`Representation.EquivariantAlgHom.restrictSubalgebra`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L336).

> The restriction to a subalgebra of the source preserved by both source representations,
> along its inclusion; the target and its two actions are unchanged.

```lean
noncomputable def restrictSubalgebra (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (S : Subalgebra k A)
    (hS₁ : ∀ (g : G₁) {x : A}, x ∈ S → ρ₁ g x ∈ S)
    (hS₂ : ∀ (g : G₂) {x : A}, x ∈ S → ρ₂ g x ∈ S) :
    EquivariantAlgHom (ρ₁.restrictSubalgebra S hS₁) σ₁ (ρ₂.restrictSubalgebra S hS₂) σ₂
```

**`Representation.EquivariantAlgHom.restrictSubalgebra_toAlgHom_apply`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L343).

```lean
lemma restrictSubalgebra_toAlgHom_apply (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (S : Subalgebra k A)
    (hS₁ : ∀ (g : G₁) {x : A}, x ∈ S → ρ₁ g x ∈ S)
    (hS₂ : ∀ (g : G₂) {x : A}, x ∈ S → ρ₂ g x ∈ S) (x : S) :
    (f.restrictSubalgebra S hS₁ hS₂).toAlgHom x = f.toAlgHom x
```

**`Representation.EquivariantAlgHom.compFst`**, a def, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L350).

> The precomposition of the first pair of representations with a monoid map; the algebra
> map is unchanged.

```lean
def compFst {H : Type*} [Monoid H] (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : H →* G₁) :
    EquivariantAlgHom (ρ₁.comp φ) (σ₁.comp φ) ρ₂ σ₂
```

**`Representation.EquivariantAlgHom.compFst_toAlgHom`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L359).

```lean
lemma compFst_toAlgHom {H : Type*} [Monoid H] (f : EquivariantAlgHom ρ₁ σ₁ ρ₂ σ₂) (φ : H →* G₁) :
    (f.compFst φ).toAlgHom = f.toAlgHom
```

## F. Base change of an equivariant algebra map

**`Representation.liftEquiv_baseChange`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L375).

> Base change along `R → S` preserves equivariance: the `S`-algebra map out of `S ⊗[R] A`
> corresponding to an equivariant `R`-algebra map `f` intertwines the base change of the
> source action with the target action.

```lean
lemma liftEquiv_baseChange {R S A B G : Type*} [CommSemiring R] [CommSemiring S] [Algebra R S]
    [Semiring A] [Algebra R A] [Semiring B] [Algebra S B] [Algebra R B] [IsScalarTower R S B]
    [Monoid G] (f : A →ₐ[R] B) (ρ : Representation R G A) (σ : Representation S G B)
    (hf : ∀ (g : G) (x : A), f (ρ g x) = σ g (f x)) (g : G) (x : S ⊗[R] A) :
    AlgHom.liftEquiv R S A B f (LinearMap.baseChange S (ρ g) x)
      = σ g (AlgHom.liftEquiv R S A B f x)
```

**`Representation.baseChange`**, a def, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L389).

> The base change of a representation along `R → S`: the same action on the second factor
> of `S ⊗[R] M`.

```lean
noncomputable def baseChange {R M G : Type*} [CommSemiring R] (S : Type*) [CommSemiring S]
    [Algebra R S] [AddCommMonoid M] [Module R M] [Monoid G] (ρ : Representation R G M) :
    Representation S G (S ⊗[R] M)
```

**`Representation.baseChange_tmul`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L399).

```lean
lemma baseChange_tmul {R M G : Type*} [CommSemiring R] (S : Type*) [CommSemiring S]
    [Algebra R S] [AddCommMonoid M] [Module R M] [Monoid G] (ρ : Representation R G M) (g : G)
    (s : S) (x : M) : baseChange S ρ g (s ⊗ₜ[R] x) = s ⊗ₜ[R] ρ g x
```

**`Representation.baseChange_naturality`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L405).

> Base change is natural: a linear map intertwining two representations base changes to
> one intertwining their base changes.

```lean
lemma baseChange_naturality {R M N G : Type*} [CommSemiring R] (S : Type*) [CommSemiring S]
    [Algebra R S] [AddCommMonoid M] [Module R M] [AddCommMonoid N] [Module R N] [Monoid G]
    {ρ : Representation R G M} {σ : Representation R G N} (f : M →ₗ[R] N)
    (h : ∀ (g : G) (x : M), f (ρ g x) = σ g (f x)) (g : G) (y : S ⊗[R] M) :
    LinearMap.baseChange S f (baseChange S ρ g y)
      = baseChange S σ g (LinearMap.baseChange S f y)
```

**`Representation.eq_baseChange_of_tmul`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L418).

> A representation on a base change acting on the pure tensors through a representation on
> the second factor is that representation's base change.

```lean
lemma eq_baseChange_of_tmul {R S A G : Type*} [CommSemiring R] [CommSemiring S] [Algebra R S]
    [AddCommMonoid A] [Module R A] [Monoid G] (ρ : Representation R G A)
    (ρ' : Representation S G (S ⊗[R] A))
    (h : ∀ (g : G) (s : S) (x : A), ρ' g (s ⊗ₜ[R] x) = s ⊗ₜ[R] ρ g x) (g : G) (y : S ⊗[R] A) :
    ρ' g y = LinearMap.baseChange S (ρ g) y
```

**`Representation.EquivariantAlgHom.liftEquivBaseChange`**, a def, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L431).

> For a target over `S`, the equivariant `R`-algebra maps out of `A` are the equivariant
> `S`-algebra maps out of the base change `S ⊗[R] A`, by `AlgHom.liftEquiv`. The two source
> actions on the base change are recognised by their values on the pure tensors, and the
> target keeps its `S`-actions, restricted to `R` on the left-hand side.

```lean
noncomputable def EquivariantAlgHom.liftEquivBaseChange {R S A B G₁ G₂ : Type*} [CommSemiring R]
    [CommSemiring S] [Algebra R S] [Semiring A] [Algebra R A] [Semiring B] [Algebra S B]
    [Algebra R B] [IsScalarTower R S B] [Monoid G₁] [Monoid G₂]
    {ρ₁ : Representation R G₁ A} {ρ₂ : Representation R G₂ A}
    {ρ₁' : Representation S G₁ (S ⊗[R] A)} {ρ₂' : Representation S G₂ (S ⊗[R] A)}
    {σ₁ : Representation S G₁ B} {σ₂ : Representation S G₂ B}
    (h₁ : ∀ (g : G₁) (s : S) (x : A), ρ₁' g (s ⊗ₜ[R] x) = s ⊗ₜ[R] ρ₁ g x)
    (h₂ : ∀ (g : G₂) (s : S) (x : A), ρ₂' g (s ⊗ₜ[R] x) = s ⊗ₜ[R] ρ₂ g x) :
    EquivariantAlgHom ρ₁ (σ₁.restrictScalars R) ρ₂ (σ₂.restrictScalars R)
      ≃ EquivariantAlgHom ρ₁' σ₁ ρ₂' σ₂
```

## G. Affine combinations under an algebra map

**`AlgHom.map_add_smul_one`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean#L474).

> An algebra map carries an affine combination `x + z • 1` to the same combination of the
> image, the shift being the image of a scalar.

```lean
lemma AlgHom.map_add_smul_one {k A B : Type*} [CommSemiring k] [Semiring A] [Algebra k A]
    [Semiring B] [Algebra k B] (f : A →ₐ[k] B) (x : A) (z : k) :
    f (x + z • (1 : A)) = f x + z • (1 : B)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/AlgebraRepresentation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/AlgebraRepresentation.lean)
