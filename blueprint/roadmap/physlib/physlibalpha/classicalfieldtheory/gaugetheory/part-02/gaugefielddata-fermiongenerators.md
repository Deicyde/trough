---
declaration: module
origin: cited
lean: GaugeFieldData.FermionGenerators, GaugeFieldData.inclFermion, GaugeFieldData.assembleFermion, GaugeFieldData.assembleFermion_inclFermion, GaugeFieldData.fermionGenerators_hom_ext, GaugeFieldData.repLorentzFermion, GaugeFieldData.repLorentzFermion_inclFermion, GaugeFieldData.repJetFermion
statement: formalized
proof: formalized
---

# The fermionic generators of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.FermionGenerators`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean): 27 declarations (2 instances with no name), 21 with a docstring.

## i. Overview

> The fermionic species of a `GaugeFieldData` each carry a component space, the span of the
> symbols `∂_s ψ_α` and their conjugates for that multiplet. This file assembles them into
> the **fermionic generator space** of the theory,
>
> `T.FermionGenerators = ⨁ i, JetComponentSpace (T.fermion i).V`,
>
> together with the transformation data the species supply: the Lorentz action, the action of
> the jets of gauge transformations, and the mass-weight scaling, each assembled species by
> species. These are the fermionic generators on which
> `GaugeFieldData.LocalFieldAlgebra` builds its exterior algebra.
>
> The direct sum, rather than a single component space on the product of the value spaces, is
> what lets the species carry different mass weights: the scaling of one component space is
> natural in the value space and so cannot tell the species apart.
>
> Section C shows what happens when the species *do* share a weight, which is the case in
> every theory of Weyl fermions and in particular in the Standard Model. A physicist does not
> write fifteen multiplets with their own component spaces; they write one fermion field `ψ`
> valued in the whole fermionic module and take its component functions `∂_s ψ_α`, a single
> `JetComponentSpace` whose target index `α` runs over everything. The two agree: there is an
> isomorphism
>
> `T.FermionGenerators ≃ₗ[ℂ] JetComponentSpace T.FermionModule`,
>
> under which the summand of a species is the pullback along the projection onto that
> species, `fermionGeneratorsEquiv_inclFermion`. So the generators of one multiplet sit inside
> the generators of the whole fermion field exactly as its target components sit inside the
> fermionic module. The isomorphism is not merely one of vector spaces: it intertwines the
> Lorentz action and the mass-weight scaling with those of the single matter field
> `T.fermionMatterField w h`, the shared weight `w` being needed for the second of these and
> for nothing else.
>
> The underlying identification is `JetComponentSpace.piEquiv`, composed with the
> identification of a direct sum over a finite index with the product.

## ii. Key results

> - `GaugeFieldData.FermionGenerators` : the fermionic generator space.
> - `GaugeFieldData.inclFermion` : the inclusion of the component space of one species.
> - `GaugeFieldData.assembleFermion`, `GaugeFieldData.fermionGenerators_hom_ext` : the assembly of
>   a species-wise family of linear maps, and the fact that it is the only such map.
> - `GaugeFieldData.repLorentzFermion`, `GaugeFieldData.repJetFermion` : the Lorentz and jet
>   gauge actions assembled on it.
> - `GaugeFieldData.massWeightScaleFermion` : the mass-weight scaling carrying the weight of
>   each species.
> - `GaugeFieldData.jetDerivFermion` : the ordinary derivative shift on the generator space.
> - `GaugeFieldData.fermionGeneratorsEquiv` : with one shared weight, the generator space is
>   the component space of the fermionic matter field.
> - `GaugeFieldData.fermionGeneratorsEquiv_inclFermion` : a species sits inside it as the
>   pullback along the projection onto that species.
> - `GaugeFieldData.fermionGeneratorsEquiv_repLorentzFermion`,
>   `GaugeFieldData.fermionGeneratorsEquiv_repJetFermion`,
>   `GaugeFieldData.fermionGeneratorsEquiv_massWeightScaleFermion`,
>   `GaugeFieldData.fermionGeneratorsEquiv_jetDerivFermion` : the identification carries the
>   Lorentz action, the jet gauge action, the mass-weight scaling and the derivative shift
>   across.

## iv. References

> * None.

## A. The fermionic generator space and its species assembly

**`GaugeFieldData.FermionGenerators`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L120).

> The fermionic generator space of the datum, holding the component functions `∂_s ψ_α`
> and their conjugates of every fermionic species at once, as a direct sum over the species.
> A component function of the theory is a finitely supported family of component functions
> of the species.
>
> The direct sum, rather than a single component space on the product of the value spaces,
> is what lets the species carry different mass weights: the scaling of one component space
> is natural in the value space — `JetComponentSpace.comap_comp_massWeightScale` — and so
> cannot tell the species apart. When the weights do agree the two descriptions coincide,
> which is section C below.
>
> This `def` and its explicit instances reduce instance-term expansion in the exterior
> algebra and tensor products built on it. Use the inclusion, assembly and extensionality
> API in downstream proofs; unfold the direct-sum representation explicitly when necessary.

```lean
def FermionGenerators : Type
```

**An instance with no name**, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L122).

```lean
instance : AddCommGroup T.FermionGenerators
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L125).

```lean
instance : Module ℂ T.FermionGenerators
```

**`GaugeFieldData.inclFermion`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L130).

> The inclusion of the component space of one fermionic species into the fermionic generator
> space.

```lean
def inclFermion (i : T.FermionSpecies) :
    JetComponentSpace (T.fermion i) →ₗ[ℂ] T.FermionGenerators
```

**`GaugeFieldData.assembleFermion`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L140).

> The assembly of a species-wise family of linear maps out of the fermionic generator space
> into a common target.

```lean
def assembleFermion (f : ∀ i, JetComponentSpace (T.fermion i) →ₗ[ℂ] N) :
    T.FermionGenerators →ₗ[ℂ] N
```

**`GaugeFieldData.assembleFermion_inclFermion`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L147).

```lean
lemma assembleFermion_inclFermion (f : ∀ i, JetComponentSpace (T.fermion i) →ₗ[ℂ] N)
    (i : T.FermionSpecies) (x : JetComponentSpace (T.fermion i)) :
    T.assembleFermion f (T.inclFermion i x) = f i x
```

**`GaugeFieldData.fermionGenerators_hom_ext`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L154).

> Two linear maps out of the fermionic generator space agreeing on every species are
> equal.

```lean
lemma fermionGenerators_hom_ext {F F' : T.FermionGenerators →ₗ[ℂ] N}
    (h : ∀ i x, F (T.inclFermion i x) = F' (T.inclFermion i x)) : F = F'
```

## B. The transformation data on the generator space

> The datum supplies, per species, a Lorentz representation and a fibrewise action of the
> gauge jets. Both act on the generator space one summand at a time, so both are assembled
> from the species-wise actions and the representation laws follow from
> `fermionGenerators_hom_ext` alone, with no relation between the species used. Nothing here
> asserts that the two actions commute, since Lorentz transformations act on nonconstant
> gauge jets, and nothing extends them to the algebra `J(T)`.

### B.1. The Lorentz action

**`GaugeFieldData.repLorentzFermion`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L179).

> The Lorentz action on the fermionic generator space, acting on each species through the
> Lorentz representation of its matter field.

```lean
noncomputable def repLorentzFermion : Representation ℂ SL(2,ℂ) T.FermionGenerators
```

**`GaugeFieldData.repLorentzFermion_inclFermion`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L188).

```lean
lemma repLorentzFermion_inclFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.repLorentzFermion Λ (T.inclFermion i x)
      = T.inclFermion i (JetComponentSpace.repLorentzGroup (T.fermion i) Λ x)
```

### B.2. The jet gauge action

**`GaugeFieldData.repJetFermion`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L206).

> The action of the jet gauge group on the fermionic generator space, acting on each
> species through the fibrewise jet action of its matter field. Both the fibrewise
> hypothesis and the finite dimensionality of the value space that
> `JetComponentSpace.repJet` needs are already fields of `MatterField`.

```lean
noncomputable def repJetFermion : Representation ℂ GJ T.FermionGenerators
```

**`GaugeFieldData.repJetFermion_inclFermion`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L215).

```lean
lemma repJetFermion_inclFermion (U : GJ) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.repJetFermion U (T.inclFermion i x)
      = T.inclFermion i
        (JetComponentSpace.repJet (T.fermion i) U x)
```

### B.3. The mass weights

> The mass weight is a property of a species, not of the theory, a fermion carrying weight
> `3` and a scalar weight `2`. The generator space records one weight per species, and the
> scaling acts on the summand of a species through that species' weight alone.

**`GaugeFieldData.massWeightScaleFermion`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L237).

> The mass-weight scaling on the fermionic generator space, with the weight of each species
> taken from its matter field. Species of different weight scale differently, which is the
> property the direct-sum generator space was chosen to have.

```lean
noncomputable def massWeightScaleFermion (c : ℂ) :
    T.FermionGenerators →ₗ[ℂ] T.FermionGenerators
```

**`GaugeFieldData.massWeightScaleFermion_inclFermion`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L247).

> On the summand of a species the scaling is that species' own mass-weight scaling, with
> the weight recorded in its matter field.

```lean
lemma massWeightScaleFermion_inclFermion (c : ℂ) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.massWeightScaleFermion c (T.inclFermion i x)
      = T.inclFermion i
        (JetComponentSpace.massWeightScale (T.fermion i).massWeight c x)
```

**`GaugeFieldData.massWeightScaleFermion_inclFermion_basis_tmul`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L257).

> A component function `∂_s ψ_α` of a species scales by `c ^ (w + 2 |s|)`, where `w` is
> the mass weight of that species. There is one factor of `c` per unit of mass dimension of
> the field and two per derivative.

```lean
lemma massWeightScaleFermion_inclFermion_basis_tmul (c : ℂ) (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.massWeightScaleFermion c (T.inclFermion i
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace (T.fermion i)))
      = c ^ ((T.fermion i).massWeight + 2 * Multiset.card s) • T.inclFermion i
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace (T.fermion i))
```

**`GaugeFieldData.massWeightScaleFermion_inclFermion_basis_tmul_conj`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L270).

> The conjugate component functions of a species scale with the same weight as its
> unconjugated ones.

```lean
lemma massWeightScaleFermion_inclFermion_basis_tmul_conj (c : ℂ) (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.massWeightScaleFermion c (T.inclFermion i
        ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace (T.fermion i)))
      = c ^ ((T.fermion i).massWeight + 2 * Multiset.card s) • T.inclFermion i
          ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace (T.fermion i))
```

### B.4. The ordinary derivative

> The formal total derivative shifts the derivative label of a component function,
> `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α`. Unlike the two actions it takes no data from the species at
> all, the label being blind to the value space, so on the generator space it too is
> species-diagonal and the same assembly serves. It is recorded here so that the generator
> space carries every operation the local field algebra is built from.

**`GaugeFieldData.jetDerivFermion`**, a def, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L301).

> The ordinary derivative shift on the fermionic generator space, acting on each species'
> component functions by appending `∂_μ` to the derivative label.

```lean
noncomputable def jetDerivFermion (μ : Fin 1 ⊕ Fin 3) :
    T.FermionGenerators →ₗ[ℂ] T.FermionGenerators
```

**`GaugeFieldData.jetDerivFermion_inclFermion`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L308).

```lean
lemma jetDerivFermion_inclFermion (μ : Fin 1 ⊕ Fin 3) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.jetDerivFermion μ (T.inclFermion i x)
      = T.inclFermion i (JetComponentSpace.jetDeriv μ x)
```

**`GaugeFieldData.jetDerivFermion_comm`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L316).

> Mixed partials agree on the fermionic generator space, because they do on each
> species.

```lean
lemma jetDerivFermion_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (T.jetDerivFermion μ).comp (T.jetDerivFermion ν)
      = (T.jetDerivFermion ν).comp (T.jetDerivFermion μ)
```

**`GaugeFieldData.repLorentzFermion_jetDerivFermion`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L327).

> The derivative shift is a Lorentz vector on the fermionic generator space: it is
> one on each species, and both operations are species-diagonal.

```lean
lemma repLorentzFermion_jetDerivFermion (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (x : T.FermionGenerators) :
    T.repLorentzFermion Λ (T.jetDerivFermion μ x)
      = ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
          T.jetDerivFermion a (T.repLorentzFermion Λ x)
```

**`GaugeFieldData.massWeightScaleFermion_jetDerivFermion`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L347).

> The derivative carries mass weight two on the fermionic generator space, whatever
> the weights of the species: the shift adds two units of mass dimension to every
> component function alike.

```lean
lemma massWeightScaleFermion_jetDerivFermion (c : ℂ) (μ : Fin 1 ⊕ Fin 3) :
    (T.massWeightScaleFermion c).comp (T.jetDerivFermion μ)
      = c ^ 2 • (T.jetDerivFermion μ).comp (T.massWeightScaleFermion c)
```

## C. The fermionic generators as one component space

**`GaugeFieldData.fermionGeneratorsEquiv`**, a def, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L372).

> **The fermionic generator space is the component space of the fermionic matter field.** The
> direct sum over the species of their component spaces is, the species type being finite,
> the same thing as the space of component functions of the single field
> `T.fermionMatterField w h` — the presentation of the fermion content used in writing a theory
> down. The shared weight `w` enters only because a component space is now taken of a
> matter field, and the only matter field on `T.FermionModule` is that one; the underlying
> identification does not use it.

```lean
noncomputable def fermionGeneratorsEquiv (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    T.FermionGenerators ≃ₗ[ℂ] JetComponentSpace (T.fermionMatterField w h)
```

### C.1. The species as pullbacks

**`GaugeFieldData.fermionGeneratorsEquiv_inclFermion`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L390).

> **A species sits inside the fermionic generators as the pullback along the projection
> onto it.** A component function of the multiplet `i` becomes the component function of
> the whole field whose target covector is supported on that multiplet.

```lean
lemma fermionGeneratorsEquiv_inclFermion (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    (i : T.FermionSpecies) (x : JetComponentSpace (T.fermion i)) :
    T.fermionGeneratorsEquiv w h (T.inclFermion i x)
      = JetComponentSpace.comap
        (T.projFermionField w h i) x
```

**`GaugeFieldData.fermionFieldComponents_hom_ext`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L408).

> Two linear maps out of the component space of the fermionic matter field agree as soon as
> they agree on every species, the species pullbacks spanning it. This is the counterpart,
> on the single-field side of the identification, of `fermionGenerators_hom_ext`.

```lean
lemma fermionFieldComponents_hom_ext {N : Type} [AddCommGroup N] [Module ℂ N]
    (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    {F F' : JetComponentSpace (T.fermionMatterField w h) →ₗ[ℂ] N}
    (hs : ∀ i x, F (JetComponentSpace.comap
        (T.projFermionField w h i) x)
      = F' (JetComponentSpace.comap
        (T.projFermionField w h i) x)) : F = F'
```

### C.2. The identification of the transformation data

**`GaugeFieldData.fermionGeneratorsEquiv_repLorentzFermion`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L434).

> **The identification is Lorentz-equivariant.** The species-diagonal Lorentz action on
> the generator space is the Lorentz action on the component functions of the single field:
> each species is a subrepresentation of the fermionic matter field, so pulling back along the
> projection onto it commutes with the two actions.

```lean
lemma fermionGeneratorsEquiv_repLorentzFermion (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    (Λ : SL(2,ℂ)) (y : T.FermionGenerators) :
    T.fermionGeneratorsEquiv w h (T.repLorentzFermion Λ y)
      = JetComponentSpace.repLorentzGroup (T.fermionMatterField w h) Λ
        (T.fermionGeneratorsEquiv w h y)
```

**`GaugeFieldData.fermionGeneratorsEquiv_repJetFermion`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L462).

> The identification is equivariant for the jet gauge action. The species-diagonal
> action of the jets of gauge transformations on the generator space is the action on the
> component functions of the single fermion field: each species is a subrepresentation of
> the fermionic module, so pulling back along the projection onto it commutes with the two
> actions.
>
> The common mass weight enters only through the packaging of the fermionic module as the
> matter field `T.fermionMatterField w h`; the gauge action itself is `repJetFermionModule`,
> which exists whatever the weights are. Both halves of the component space are covered,
> the conjugate one included, and every derivative label with them: this is
> `JetComponentSpace.comap_comp_repJet` at the species projection.

```lean
lemma fermionGeneratorsEquiv_repJetFermion (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    (U : GJ) (y : T.FermionGenerators) :
    T.fermionGeneratorsEquiv w h (T.repJetFermion U y)
      = JetComponentSpace.repJet (T.fermionMatterField w h) U
        (T.fermionGeneratorsEquiv w h y)
```

**`GaugeFieldData.fermionGeneratorsEquiv_massWeightScaleFermion`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L484).

> **The identification carries the species-wise mass-weight scaling to a single
> scaling.** With one weight `w` shared by every species, the scaling that acts on each
> species through its own weight is the scaling of weight `w` on the component functions of
> the one field: `comap` is natural in the value space, so it does not see which species a
> generator came from.

```lean
lemma fermionGeneratorsEquiv_massWeightScaleFermion (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (c : ℂ) (y : T.FermionGenerators) :
    T.fermionGeneratorsEquiv w h (T.massWeightScaleFermion c y)
      = JetComponentSpace.massWeightScale w c (T.fermionGeneratorsEquiv w h y)
```

**`GaugeFieldData.fermionGeneratorsEquiv_jetDerivFermion`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean#L505).

> The identification carries the derivative shift across. The species-diagonal shift
> of the derivative label on the generator space is the shift on the component functions of
> the single fermion field: `comap` is natural in the value space, and the shift touches
> only the derivative label, so neither operation sees which species a generator came from.
> The common mass weight enters only through the packaging of the fermionic module as a
> matter field.

```lean
lemma fermionGeneratorsEquiv_jetDerivFermion (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    (μ : Fin 1 ⊕ Fin 3) (y : T.FermionGenerators) :
    T.fermionGeneratorsEquiv w h (T.jetDerivFermion μ y)
      = JetComponentSpace.jetDeriv μ (T.fermionGeneratorsEquiv w h y)
```

## Depends on

- [The fermionic matter field of a gauge theory](gaugefielddata-fermionmatterfield.md)
- [The gauge action on the jet component space](../part-06/matterfield-jetcomponent-gaugeaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionGenerators.lean)
