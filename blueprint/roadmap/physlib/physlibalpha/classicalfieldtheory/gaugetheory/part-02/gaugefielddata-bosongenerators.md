---
declaration: module
origin: cited
lean: GaugeFieldData.BosonGenerators, GaugeFieldData.inclBoson, GaugeFieldData.assembleBoson, GaugeFieldData.assembleBoson_inclBoson, GaugeFieldData.bosonGenerators_hom_ext, GaugeFieldData.repLorentzBoson, GaugeFieldData.repLorentzBoson_inclBoson, GaugeFieldData.repJetBoson
statement: formalized
proof: formalized
---

# The bosonic generators of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.BosonGenerators`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean): 27 declarations (2 instances with no name), 21 with a docstring.

## i. Overview

> The bosonic species of a `GaugeFieldData` — its scalars — each carry a component space, the
> span of the symbols `∂_s φ_α` and their conjugates for that multiplet. This file assembles them into
> the **bosonic generator space** of the theory,
>
> `T.BosonGenerators = ⨁ i, JetComponentSpace (T.boson i).V`,
>
> together with the transformation data the species supply: the Lorentz action, the action of
> the jets of gauge transformations, and the mass-weight scaling, each assembled species by
> species. These are the bosonic generators on which
> `GaugeFieldData.LocalFieldAlgebra` builds its symmetric algebra. The gauge bosons are not
> among them: their generator space is fixed by the gauge algebra alone.
>
> The direct sum, rather than a single component space on the product of the value spaces, is
> what lets the species carry different mass weights: the scaling of one component space is
> natural in the value space and so cannot tell the species apart.
>
> Section C shows what happens when the species *do* share a weight, which is the case in any
> theory whose scalars all have the same mass dimension. A physicist does not write each
> multiplet with its own component space; they write one scalar field `φ` valued in the whole
> bosonic module and take its component functions `∂_s φ_α`, a single `JetComponentSpace`
> whose target index `α` runs over everything. For the Standard Model, with its one Higgs
> doublet, the two are trivially the same; for a larger scalar sector they are not.
>
> The two descriptions agree: there is an isomorphism
>
> `T.BosonGenerators ≃ₗ[ℂ] JetComponentSpace T.BosonModule`,
>
> under which the summand of a species is the pullback along the projection onto that
> species, `bosonGeneratorsEquiv_inclBoson`. So the generators of one multiplet sit inside
> the generators of the whole scalar field exactly as its target components sit inside the
> bosonic module. The isomorphism is not merely one of vector spaces: it intertwines the
> Lorentz action and the mass-weight scaling with those of the single matter field
> `T.bosonMatterField w h`, the shared weight `w` being needed for the second of these and
> for nothing else.
>
> The underlying identification is `JetComponentSpace.piEquiv`, composed with the
> identification of a direct sum over a finite index with the product.

## ii. Key results

> - `GaugeFieldData.BosonGenerators` : the bosonic generator space.
> - `GaugeFieldData.inclBoson` : the inclusion of the component space of one species.
> - `GaugeFieldData.assembleBoson`, `GaugeFieldData.bosonGenerators_hom_ext` : the assembly of
>   a species-wise family of linear maps, and the fact that it is the only such map.
> - `GaugeFieldData.repLorentzBoson`, `GaugeFieldData.repJetBoson` : the Lorentz and jet
>   gauge actions assembled on it.
> - `GaugeFieldData.massWeightScaleBoson` : the mass-weight scaling carrying the weight of
>   each species.
> - `GaugeFieldData.jetDerivBoson` : the ordinary derivative shift on the generator space.
> - `GaugeFieldData.bosonGeneratorsEquiv` : with one shared weight, the generator space is
>   the component space of the bosonic matter field.
> - `GaugeFieldData.bosonGeneratorsEquiv_inclBoson` : a species sits inside it as the
>   pullback along the projection onto that species.
> - `GaugeFieldData.bosonGeneratorsEquiv_repLorentzBoson`,
>   `GaugeFieldData.bosonGeneratorsEquiv_repJetBoson`,
>   `GaugeFieldData.bosonGeneratorsEquiv_massWeightScaleBoson`,
>   `GaugeFieldData.bosonGeneratorsEquiv_jetDerivBoson` : the identification carries the
>   Lorentz action, the jet gauge action, the mass-weight scaling and the derivative shift
>   across.

## iv. References

> * None.

## A. The bosonic generator space and its species assembly

**`GaugeFieldData.BosonGenerators`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L123).

> The bosonic generator space of the datum, holding the component functions `∂_s φ_α`
> and their conjugates of every bosonic species at once, as a direct sum over the species.
> A component function of the theory is a finitely supported family of component functions
> of the species.
>
> The direct sum, rather than a single component space on the product of the value spaces,
> is what lets the species carry different mass weights: the scaling of one component space
> is natural in the value space — `JetComponentSpace.comap_comp_massWeightScale` — and so
> cannot tell the species apart. When the weights do agree the two descriptions coincide,
> which is section C below.
>
> This `def` and its explicit instances reduce instance-term expansion in the symmetric
> algebra and tensor products built on it. Use the inclusion, assembly and extensionality
> API in downstream proofs; unfold the direct-sum representation explicitly when necessary.

```lean
def BosonGenerators : Type
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L125).

```lean
instance : AddCommGroup T.BosonGenerators
```

**An instance with no name**, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L128).

```lean
instance : Module ℂ T.BosonGenerators
```

**`GaugeFieldData.inclBoson`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L133).

> The inclusion of the component space of one bosonic species into the bosonic generator
> space.

```lean
def inclBoson (i : T.BosonSpecies) :
    JetComponentSpace (T.boson i) →ₗ[ℂ] T.BosonGenerators
```

**`GaugeFieldData.assembleBoson`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L143).

> The assembly of a species-wise family of linear maps out of the bosonic generator space
> into a common target.

```lean
def assembleBoson (f : ∀ i, JetComponentSpace (T.boson i) →ₗ[ℂ] N) :
    T.BosonGenerators →ₗ[ℂ] N
```

**`GaugeFieldData.assembleBoson_inclBoson`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L150).

```lean
lemma assembleBoson_inclBoson (f : ∀ i, JetComponentSpace (T.boson i) →ₗ[ℂ] N)
    (i : T.BosonSpecies) (x : JetComponentSpace (T.boson i)) :
    T.assembleBoson f (T.inclBoson i x) = f i x
```

**`GaugeFieldData.bosonGenerators_hom_ext`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L157).

> Two linear maps out of the bosonic generator space agreeing on every species are
> equal.

```lean
lemma bosonGenerators_hom_ext {F F' : T.BosonGenerators →ₗ[ℂ] N}
    (h : ∀ i x, F (T.inclBoson i x) = F' (T.inclBoson i x)) : F = F'
```

## B. The transformation data on the generator space

> The datum supplies, per species, a Lorentz representation and a fibrewise action of the
> gauge jets. Both act on the generator space one summand at a time, so both are assembled
> from the species-wise actions and the representation laws follow from
> `bosonGenerators_hom_ext` alone, with no relation between the species used. Nothing here
> asserts that the two actions commute, since Lorentz transformations act on nonconstant
> gauge jets, and nothing extends them to the algebra `J(T)`.

### B.1. The Lorentz action

**`GaugeFieldData.repLorentzBoson`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L182).

> The Lorentz action on the bosonic generator space, acting on each species through the
> Lorentz representation of its matter field.

```lean
noncomputable def repLorentzBoson : Representation ℂ SL(2,ℂ) T.BosonGenerators
```

**`GaugeFieldData.repLorentzBoson_inclBoson`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L191).

```lean
lemma repLorentzBoson_inclBoson (Λ : SL(2,ℂ)) (i : T.BosonSpecies)
    (x : JetComponentSpace (T.boson i)) :
    T.repLorentzBoson Λ (T.inclBoson i x)
      = T.inclBoson i (JetComponentSpace.repLorentzGroup (T.boson i) Λ x)
```

### B.2. The jet gauge action

**`GaugeFieldData.repJetBoson`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L209).

> The action of the jet gauge group on the bosonic generator space, acting on each
> species through the fibrewise jet action of its matter field. Both the fibrewise
> hypothesis and the finite dimensionality of the value space that
> `JetComponentSpace.repJet` needs are already fields of `MatterField`.

```lean
noncomputable def repJetBoson : Representation ℂ GJ T.BosonGenerators
```

**`GaugeFieldData.repJetBoson_inclBoson`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L218).

```lean
lemma repJetBoson_inclBoson (U : GJ) (i : T.BosonSpecies)
    (x : JetComponentSpace (T.boson i)) :
    T.repJetBoson U (T.inclBoson i x)
      = T.inclBoson i
        (JetComponentSpace.repJet (T.boson i) U x)
```

### B.3. The mass weights

> The mass weight is a property of a species, not of the theory, a fermion carrying weight
> `3` and a scalar weight `2`. The generator space records one weight per species, and the
> scaling acts on the summand of a species through that species' weight alone.

**`GaugeFieldData.massWeightScaleBoson`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L240).

> The mass-weight scaling on the bosonic generator space, with the weight of each species
> taken from its matter field. Species of different weight scale differently, which is the
> property the direct-sum generator space was chosen to have.

```lean
noncomputable def massWeightScaleBoson (c : ℂ) :
    T.BosonGenerators →ₗ[ℂ] T.BosonGenerators
```

**`GaugeFieldData.massWeightScaleBoson_inclBoson`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L250).

> On the summand of a species the scaling is that species' own mass-weight scaling, with
> the weight recorded in its matter field.

```lean
lemma massWeightScaleBoson_inclBoson (c : ℂ) (i : T.BosonSpecies)
    (x : JetComponentSpace (T.boson i)) :
    T.massWeightScaleBoson c (T.inclBoson i x)
      = T.inclBoson i
        (JetComponentSpace.massWeightScale (T.boson i).massWeight c x)
```

**`GaugeFieldData.massWeightScaleBoson_inclBoson_basis_tmul`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L260).

> A component function `∂_s φ_α` of a species scales by `c ^ (w + 2 |s|)`, where `w` is
> the mass weight of that species. There is one factor of `c` per unit of mass dimension of
> the field and two per derivative.

```lean
lemma massWeightScaleBoson_inclBoson_basis_tmul (c : ℂ) (i : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue i)) :
    T.massWeightScaleBoson c (T.inclBoson i
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace (T.boson i)))
      = c ^ ((T.boson i).massWeight + 2 * Multiset.card s) • T.inclBoson i
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace (T.boson i))
```

**`GaugeFieldData.massWeightScaleBoson_inclBoson_basis_tmul_conj`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L273).

> The conjugate component functions of a species scale with the same weight as its
> unconjugated ones.

```lean
lemma massWeightScaleBoson_inclBoson_basis_tmul_conj (c : ℂ) (i : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue i))) :
    T.massWeightScaleBoson c (T.inclBoson i
        ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace (T.boson i)))
      = c ^ ((T.boson i).massWeight + 2 * Multiset.card s) • T.inclBoson i
          ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace (T.boson i))
```

### B.4. The ordinary derivative

> The formal total derivative shifts the derivative label of a component function,
> `∂_s φ_α ↦ ∂_{s + {μ}} φ_α`. Unlike the two actions it takes no data from the species at
> all, the label being blind to the value space, so on the generator space it too is
> species-diagonal and the same assembly serves. It is recorded here so that the generator
> space carries every operation the local field algebra is built from.

**`GaugeFieldData.jetDerivBoson`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L304).

> The ordinary derivative shift on the bosonic generator space, acting on each species'
> component functions by appending `∂_μ` to the derivative label.

```lean
noncomputable def jetDerivBoson (μ : Fin 1 ⊕ Fin 3) :
    T.BosonGenerators →ₗ[ℂ] T.BosonGenerators
```

**`GaugeFieldData.jetDerivBoson_inclBoson`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L311).

```lean
lemma jetDerivBoson_inclBoson (μ : Fin 1 ⊕ Fin 3) (i : T.BosonSpecies)
    (x : JetComponentSpace (T.boson i)) :
    T.jetDerivBoson μ (T.inclBoson i x)
      = T.inclBoson i (JetComponentSpace.jetDeriv μ x)
```

**`GaugeFieldData.jetDerivBoson_comm`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L319).

> Mixed partials agree on the bosonic generator space, because they do on each
> species.

```lean
lemma jetDerivBoson_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (T.jetDerivBoson μ).comp (T.jetDerivBoson ν)
      = (T.jetDerivBoson ν).comp (T.jetDerivBoson μ)
```

**`GaugeFieldData.repLorentzBoson_jetDerivBoson`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L330).

> The derivative shift is a Lorentz vector on the bosonic generator space: it is one
> on each species, and both operations are species-diagonal.

```lean
lemma repLorentzBoson_jetDerivBoson (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (x : T.BosonGenerators) :
    T.repLorentzBoson Λ (T.jetDerivBoson μ x)
      = ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
          T.jetDerivBoson a (T.repLorentzBoson Λ x)
```

**`GaugeFieldData.massWeightScaleBoson_jetDerivBoson`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L350).

> The derivative carries mass weight two on the bosonic generator space, whatever the
> weights of the species: the shift adds two units of mass dimension to every component
> function alike.

```lean
lemma massWeightScaleBoson_jetDerivBoson (c : ℂ) (μ : Fin 1 ⊕ Fin 3) :
    (T.massWeightScaleBoson c).comp (T.jetDerivBoson μ)
      = c ^ 2 • (T.jetDerivBoson μ).comp (T.massWeightScaleBoson c)
```

## C. The bosonic generators as one component space

**`GaugeFieldData.bosonGeneratorsEquiv`**, a def, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L375).

> **The bosonic generator space is the component space of the bosonic matter field.** The
> direct sum over the species of their component spaces is, the species type being finite,
> the same thing as the space of component functions of the single field
> `T.bosonMatterField w h` — the presentation of the boson content used in writing a theory
> down. The shared weight `w` enters only because a component space is now taken of a
> matter field, and the only matter field on `T.BosonModule` is that one; the underlying
> identification does not use it.

```lean
noncomputable def bosonGeneratorsEquiv (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    T.BosonGenerators ≃ₗ[ℂ] JetComponentSpace (T.bosonMatterField w h)
```

### C.1. The species as pullbacks

**`GaugeFieldData.bosonGeneratorsEquiv_inclBoson`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L393).

> **A species sits inside the bosonic generators as the pullback along the projection
> onto it.** A component function of the multiplet `i` becomes the component function of
> the whole field whose target covector is supported on that multiplet.

```lean
lemma bosonGeneratorsEquiv_inclBoson (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    (i : T.BosonSpecies) (x : JetComponentSpace (T.boson i)) :
    T.bosonGeneratorsEquiv w h (T.inclBoson i x)
      = JetComponentSpace.comap
        (T.projBosonField w h i) x
```

**`GaugeFieldData.bosonFieldComponents_hom_ext`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L411).

> Two linear maps out of the component space of the bosonic matter field agree as soon as
> they agree on every species, the species pullbacks spanning it. This is the counterpart,
> on the single-field side of the identification, of `bosonGenerators_hom_ext`.

```lean
lemma bosonFieldComponents_hom_ext {N : Type} [AddCommGroup N] [Module ℂ N]
    (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    {F F' : JetComponentSpace (T.bosonMatterField w h) →ₗ[ℂ] N}
    (hs : ∀ i x, F (JetComponentSpace.comap
        (T.projBosonField w h i) x)
      = F' (JetComponentSpace.comap
        (T.projBosonField w h i) x)) : F = F'
```

### C.2. The identification of the transformation data

**`GaugeFieldData.bosonGeneratorsEquiv_repLorentzBoson`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L437).

> **The identification is Lorentz-equivariant.** The species-diagonal Lorentz action on
> the generator space is the Lorentz action on the component functions of the single field:
> each species is a subrepresentation of the bosonic matter field, so pulling back along the
> projection onto it commutes with the two actions.

```lean
lemma bosonGeneratorsEquiv_repLorentzBoson (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    (Λ : SL(2,ℂ)) (y : T.BosonGenerators) :
    T.bosonGeneratorsEquiv w h (T.repLorentzBoson Λ y)
      = JetComponentSpace.repLorentzGroup (T.bosonMatterField w h) Λ
        (T.bosonGeneratorsEquiv w h y)
```

**`GaugeFieldData.bosonGeneratorsEquiv_repJetBoson`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L460).

> The identification is equivariant for the jet gauge action. The species-diagonal
> action of the jets of gauge transformations on the generator space is the action on the
> component functions of the single boson field, for the same reason as in the fermionic
> case: each species is a subrepresentation of the bosonic module. The common mass weight
> enters only through the packaging of the bosonic module as a matter field; both halves
> of the component space, with every derivative label, are covered.

```lean
lemma bosonGeneratorsEquiv_repJetBoson (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    (U : GJ) (y : T.BosonGenerators) :
    T.bosonGeneratorsEquiv w h (T.repJetBoson U y)
      = JetComponentSpace.repJet (T.bosonMatterField w h) U
        (T.bosonGeneratorsEquiv w h y)
```

**`GaugeFieldData.bosonGeneratorsEquiv_massWeightScaleBoson`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L482).

> **The identification carries the species-wise mass-weight scaling to a single
> scaling.** With one weight `w` shared by every species, the scaling that acts on each
> species through its own weight is the scaling of weight `w` on the component functions of
> the one field: `comap` is natural in the value space, so it does not see which species a
> generator came from.

```lean
lemma bosonGeneratorsEquiv_massWeightScaleBoson (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (c : ℂ) (y : T.BosonGenerators) :
    T.bosonGeneratorsEquiv w h (T.massWeightScaleBoson c y)
      = JetComponentSpace.massWeightScale w c (T.bosonGeneratorsEquiv w h y)
```

**`GaugeFieldData.bosonGeneratorsEquiv_jetDerivBoson`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean#L503).

> The identification carries the derivative shift across. The species-diagonal shift
> of the derivative label on the generator space is the shift on the component functions of
> the single boson field: `comap` is natural in the value space, and the shift touches only
> the derivative label, so neither operation sees which species a generator came from. The
> common mass weight enters only through the packaging of the bosonic module as a matter
> field.

```lean
lemma bosonGeneratorsEquiv_jetDerivBoson (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    (μ : Fin 1 ⊕ Fin 3) (y : T.BosonGenerators) :
    T.bosonGeneratorsEquiv w h (T.jetDerivBoson μ y)
      = JetComponentSpace.jetDeriv μ (T.bosonGeneratorsEquiv w h y)
```

## Depends on

- [The bosonic matter field of a gauge theory](gaugefielddata-bosonmatterfield.md)
- [The gauge action on the jet component space](../part-06/matterfield-jetcomponent-gaugeaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonGenerators.lean)
