---
declaration: module
origin: cited
lean: Representation.augmentation, Representation.augmentation_single, Representation.augmentation_mapDomainAlgHom, Representation.asAlgebraHom_apply_of_mem_invariants, Representation.map_asAlgebraHom_apply, Representation.asAlgebraHom_comp, Representation.IsReynolds, Representation.IsReynolds.apply_of_mem_invariants
statement: formalized
proof: formalized
---

# Reynolds elements

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Reynolds.Basic`, [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean): 25 declarations, 21 with a docstring.

> Elements of the monoid algebra that project a stable subspace onto its invariants.

## i. Overview

> Let `ρ` be a representation of a monoid `H` on a vector space `V` and `W` a subspace of `V`.
> A Reynolds element for `ρ` on `W` is an element `r` of the monoid algebra `k[H]` whose
> coefficients sum to one, and which maps every vector of `W` to an invariant vector of `W`. For a
> finite group the average `(1/|H|) Σ_h h` is a Reynolds element on all of `V`, and for a compact
> group the Haar average plays the same role on each finite-dimensional stable subspace.
>
> The point of the coefficients summing to one is that `r` then fixes every invariant vector, in any
> representation. This gives the descent property. If `f : V → B` intertwines `ρ` with a
> representation `σ` on `B`, `a ∈ W` and `f a` is `σ`-invariant, then `a' = r • a` is a
> `ρ`-invariant vector with `f a' = r • f a = f a`. So invariants in the image of `f` come from
> invariants in `V`.
>
> Reynolds elements are usually produced as an operator `P` on a finite-dimensional stable subspace
> which projects onto the invariants and lies in `1 + span {ρ h - 1}`. We show that every such
> operator comes from a Reynolds element.
>
> Finally, for two commuting representations, packaged as one representation of `H₁ × H₂`,
> Reynolds elements for each factor multiply to a Reynolds element for the product.

## ii. Key results

> - `Representation.augmentation` is the sum of the coefficients of an element of `k[H]`.
> - `Representation.IsReynolds` is the property of being a Reynolds element on a subspace.
> - `Representation.IsReynolds.of_comp` pushes a Reynolds element forward along a surjective
>   homomorphism of groups.
> - `Representation.IsReynolds.exists_mem_invariants_map_eq` is the descent property along
>   intertwining maps.
> - `Representation.exists_isReynolds_of_sub_one_mem_span` produces a Reynolds element from an
>   operator on a stable subspace in `1 + span {ρ h - 1}` with image in the invariants.
> - `Representation.IsReynolds.mul_mapDomain` multiplies Reynolds elements of the two factors of
>   a representation of `H₁ × H₂`.

## iv. References

> - The Reynolds operator in invariant theory, see for example
>   B. Sturmfels, *Algorithms in Invariant Theory*.

## A. The augmentation

**`Representation.augmentation`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L90).

> The augmentation of the monoid algebra `k[H]`, sending a formal linear combination of
> elements of `H` to the sum of its coefficients.

```lean
noncomputable def augmentation : k[H] →ₐ[k] k
```

**`Representation.augmentation_single`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L95).

```lean
lemma augmentation_single (h : H) (c : k) :
    augmentation k H (MonoidAlgebra.single h c) = c
```

**`Representation.augmentation_mapDomainAlgHom`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L100).

> The augmentation is unchanged by pushing an element along a monoid map.

```lean
lemma augmentation_mapDomainAlgHom {H' : Type*} [Monoid H'] (f : H →* H') (r : k[H]) :
    augmentation k H' (MonoidAlgebra.mapDomainAlgHom k k f r) = augmentation k H r
```

## B. The monoid algebra acting on invariants and through intertwiners

**`Representation.asAlgebraHom_apply_of_mem_invariants`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L119).

> An element of the monoid algebra acts on an invariant vector by its augmentation.

```lean
lemma asAlgebraHom_apply_of_mem_invariants (ρ : Representation k H V) (r : k[H]) {v : V}
    (hv : v ∈ ρ.invariants) : ρ.asAlgebraHom r v = augmentation k H r • v
```

**`Representation.map_asAlgebraHom_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L128).

> A linear map intertwining two representations also intertwines the actions of the monoid
> algebra.

```lean
lemma map_asAlgebraHom_apply (ρ : Representation k H V) (σ : Representation k H B)
    (f : V →ₗ[k] B) (hf : ∀ h v, f (ρ h v) = σ h (f v)) (r : k[H]) (v : V) :
    f (ρ.asAlgebraHom r v) = σ.asAlgebraHom r (f v)
```

**`Representation.asAlgebraHom_comp`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L138).

> Restricting a representation along a monoid homomorphism corresponds to pushing elements of
> the monoid algebra forward along it.

```lean
lemma asAlgebraHom_comp {H' : Type*} [Group H'] (ρ : Representation k H' V) (f : H →* H')
    (r : k[H]) :
    asAlgebraHom (ρ.comp f) r = ρ.asAlgebraHom (MonoidAlgebra.mapDomainAlgHom k k f r)
```

## C. Reynolds elements

### C.1. The definition

**`Representation.IsReynolds`**, a structure, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L158).

> An element `r` of the monoid algebra is a Reynolds element for the representation on the
> subspace `W` if its coefficients sum to one and it maps every vector of `W` to an invariant
> vector of `W`. By `IsReynolds.apply_of_mem_invariants` it then fixes every invariant vector,
> so it acts on `W` as a projection onto the invariants of `W`.

```lean
structure IsReynolds (ρ : Representation k H V) (W : Submodule k V) (r : k[H]) : Prop where
  /-- The coefficients of the Reynolds element sum to one. -/
  augmentation_eq_one : augmentation k H r = 1
  /-- The Reynolds element maps the subspace into itself. -/
  apply_mem : ∀ w ∈ W, ρ.asAlgebraHom r w ∈ W
  /-- The Reynolds element maps the subspace into the invariants. -/
  apply_mem_invariants : ∀ w ∈ W, ρ.asAlgebraHom r w ∈ ρ.invariants
```

**`Representation.IsReynolds.apply_of_mem_invariants`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L171).

> A Reynolds element fixes every invariant vector, inside or outside the subspace.

```lean
lemma apply_of_mem_invariants (hr : ρ.IsReynolds W r) {v : V} (hv : v ∈ ρ.invariants) :
    ρ.asAlgebraHom r v = v
```

**`Representation.IsReynolds.apply_mem_inf`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L176).

> A Reynolds element maps the subspace onto its invariant vectors.

```lean
lemma apply_mem_inf (hr : ρ.IsReynolds W r) {w : V} (hw : w ∈ W) :
    ρ.asAlgebraHom r w ∈ W ⊓ ρ.invariants
```

**`Representation.IsReynolds.mono`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L181).

> A Reynolds element for a subspace is one for every smaller subspace stable under it.

```lean
lemma mono {W' : Submodule k V} (hr : ρ.IsReynolds W r) (hW : W' ≤ W)
    (hW' : ∀ w ∈ W', ρ.asAlgebraHom r w ∈ W') : ρ.IsReynolds W' r
```

**`Representation.IsReynolds.of_comp`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L187).

> A Reynolds element for a representation restricted along a surjective homomorphism `f` pushes
> forward along `f` to a Reynolds element for the representation.

```lean
lemma of_comp {H' : Type*} [Group H'] {f : H' →* H} (hf : Function.Surjective f) {r : k[H']}
    (hr : IsReynolds (ρ.comp f) W r) : ρ.IsReynolds W (MonoidAlgebra.mapDomainAlgHom k k f r)
```

### C.2. Descent along intertwining maps

**`Representation.IsReynolds.exists_mem_invariants_map_eq`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L207).

> The descent property of Reynolds elements. If `f` intertwines `ρ` with `σ`, the vector `a`
> lies in a subspace with a Reynolds element, and `f a` is `σ`-invariant, then `f a` is the image of
> a `ρ`-invariant vector of that subspace, namely the Reynolds element applied to `a`.

```lean
lemma exists_mem_invariants_map_eq (hr : ρ.IsReynolds W r) {σ : Representation k H B}
    {f : V →ₗ[k] B} (hf : ∀ h v, f (ρ h v) = σ h (f v)) {a : V} (ha : a ∈ W)
    (hfa : f a ∈ σ.invariants) : ∃ a' ∈ W ⊓ ρ.invariants, f a' = f a
```

## D. Reynolds elements from operators on stable subspaces

### D.1. Operators in one plus the span of the group image

**`Representation.exists_asAlgebraHom_eq_of_sub_one_mem_span`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L226).

> An operator in `1 + span {σ h - 1}` is the action of an element of the monoid algebra whose
> coefficients sum to one.

```lean
lemma exists_asAlgebraHom_eq_of_sub_one_mem_span (σ : Representation k H V)
    {P : Module.End k V} (hP : P - 1 ∈ Submodule.span k (Set.range fun h => σ h - 1)) :
    ∃ r : k[H], augmentation k H r = 1 ∧ σ.asAlgebraHom r = P
```

### D.2. Subrepresentations

**`Representation.coe_asAlgebraHom_toRepresentation_apply`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L253).

> The monoid algebra acts on a subrepresentation by the restriction of its action on the
> ambient space.

```lean
lemma coe_asAlgebraHom_toRepresentation_apply (W : Subrepresentation ρ) (r : k[H])
    (w : W.toSubmodule) : (W.toRepresentation.asAlgebraHom r w : V) = ρ.asAlgebraHom r w
```

**`Representation.mem_invariants_toRepresentation_iff`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L259).

> A vector of a subrepresentation is invariant there exactly when it is invariant in the
> ambient space.

```lean
lemma mem_invariants_toRepresentation_iff (W : Subrepresentation ρ) (w : W.toSubmodule) :
    w ∈ W.toRepresentation.invariants ↔ (w : V) ∈ ρ.invariants
```

**`Representation.isReynolds_of_toRepresentation`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L265).

> An element of the monoid algebra whose coefficients sum to one, and which maps a
> subrepresentation into its invariants, is a Reynolds element on it.

```lean
lemma isReynolds_of_toRepresentation (W : Subrepresentation ρ) {r : k[H]}
    (hr : augmentation k H r = 1)
    (hinv : ∀ w, W.toRepresentation.asAlgebraHom r w ∈ W.toRepresentation.invariants) :
    ρ.IsReynolds W.toSubmodule r
```

**`Representation.exists_isReynolds_of_sub_one_mem_span`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L282).

> An operator on a subrepresentation which lies in `1 + span {ρ h - 1}` and maps into the
> invariants comes from a Reynolds element. This is the form in which Reynolds elements are
> produced on finite-dimensional stable subspaces, for example by averaging over a compact group or
> from Casimir operators.

```lean
lemma exists_isReynolds_of_sub_one_mem_span (W : Subrepresentation ρ)
    {P : Module.End k W.toSubmodule}
    (hP : P - 1 ∈ Submodule.span k (Set.range fun h => W.toRepresentation h - 1))
    (hinv : ∀ w, P w ∈ W.toRepresentation.invariants) :
    ∃ r : k[H], ρ.IsReynolds W.toSubmodule r ∧
      ∀ w : W.toSubmodule, ρ.asAlgebraHom r w = P w
```

## E. Reynolds elements for products

### E.1. Commuting representations

**`Representation.prodOfCommute`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L304).

> The representation of `H₁ × H₂` built from two representations on the same space whose
> actions commute.

```lean
noncomputable def prodOfCommute (ρ₁ : Representation k H₁ V) (ρ₂ : Representation k H₂ V)
    (h : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) : Representation k (H₁ × H₂) V
```

**`Representation.prodOfCommute_apply`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L309).

```lean
lemma prodOfCommute_apply (ρ₁ : Representation k H₁ V) (ρ₂ : Representation k H₂ V)
    (h : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) (x : H₁ × H₂) :
    prodOfCommute ρ₁ ρ₂ h x = ρ₁ x.1 * ρ₂ x.2
```

**`Representation.prodOfCommute_comp_inl`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L314).

```lean
lemma prodOfCommute_comp_inl (ρ₁ : Representation k H₁ V) (ρ₂ : Representation k H₂ V)
    (h : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) :
    (prodOfCommute ρ₁ ρ₂ h).comp (MonoidHom.inl H₁ H₂) = ρ₁
```

**`Representation.prodOfCommute_comp_inr`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L320).

```lean
lemma prodOfCommute_comp_inr (ρ₁ : Representation k H₁ V) (ρ₂ : Representation k H₂ V)
    (h : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) :
    (prodOfCommute ρ₁ ρ₂ h).comp (MonoidHom.inr H₁ H₂) = ρ₂
```

**`Representation.mem_invariants_iff_comp_inl_inr`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L327).

> A vector is invariant under a representation of `H₁ × H₂` exactly when it is invariant under
> both factors.

```lean
lemma mem_invariants_iff_comp_inl_inr (ρ : Representation k (H₁ × H₂) V) (v : V) :
    v ∈ ρ.invariants ↔ v ∈ invariants (ρ.comp (MonoidHom.inl H₁ H₂)) ∧
      v ∈ invariants (ρ.comp (MonoidHom.inr H₁ H₂))
```

**`Representation.mem_invariants_prodOfCommute_iff`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L338).

> A vector is invariant under the representation built from two commuting representations
> exactly when it is invariant under both.

```lean
lemma mem_invariants_prodOfCommute_iff (ρ₁ : Representation k H₁ V)
    (ρ₂ : Representation k H₂ V) (h : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) (v : V) :
    v ∈ (prodOfCommute ρ₁ ρ₂ h).invariants ↔ v ∈ ρ₁.invariants ∧ v ∈ ρ₂.invariants
```

### E.2. The product of Reynolds elements

**`Representation.comp_inr_apply_asAlgebraHom_comp_inl`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L351).

> The action of the second factor commutes with the action of the monoid algebra of the first
> factor.

```lean
lemma comp_inr_apply_asAlgebraHom_comp_inl (ρ : Representation k (H₁ × H₂) V) (b : H₂)
    (r : k[H₁]) (v : V) :
    ρ (1, b) (asAlgebraHom (ρ.comp (MonoidHom.inl H₁ H₂)) r v) =
      asAlgebraHom (ρ.comp (MonoidHom.inl H₁ H₂)) r (ρ (1, b) v)
```

**`Representation.IsReynolds.mul_mapDomain`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean#L361).

> Reynolds elements for the two factors of a representation of `H₁ × H₂` on the same subspace
> multiply to a Reynolds element for the representation of the product.

```lean
lemma IsReynolds.mul_mapDomain {ρ : Representation k (H₁ × H₂) V} {W : Submodule k V}
    {r₁ : k[H₁]} {r₂ : k[H₂]} (hr₁ : IsReynolds (ρ.comp (MonoidHom.inl H₁ H₂)) W r₁)
    (hr₂ : IsReynolds (ρ.comp (MonoidHom.inr H₁ H₂)) W r₂) :
    ρ.IsReynolds W (MonoidAlgebra.mapDomainAlgHom k k (MonoidHom.inl H₁ H₂) r₁ *
      MonoidAlgebra.mapDomainAlgHom k k (MonoidHom.inr H₁ H₂) r₂)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Basic.lean)
