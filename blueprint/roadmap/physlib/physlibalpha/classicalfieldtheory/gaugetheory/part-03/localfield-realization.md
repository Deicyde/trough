---
declaration: module
origin: cited
lean: GaugeFieldData.Realization, GaugeFieldData.Realization.id, GaugeFieldData.Realization.id_toAlgHom, GaugeFieldData.Realization.ext_generators, GaugeFieldData.Realization.map_repJet, GaugeFieldData.Realization.map_repLorentz, GaugeFieldData.Realization.repJet_mul, GaugeFieldData.Realization.repLorentz_mul
statement: formalized
proof: formalized
---

# Realizations of the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean): 32 declarations, 21 with a docstring.

## i. Overview

> A complex algebra `B` carries the fields of a gauge-field datum when the local field
> algebra `J(T)` maps into it by a complex algebra map equivariant for the jet gauge group
> and the Lorentz group, both acting on `B` by algebra endomorphisms:
> `GaugeFieldData.Realization`. The generator images are not stored: they are read off the
> map as `Realization.toAssignment`, the connection factor as `Realization.gaugeRealization`
> and the matter symbols as `Realization.fermionSymbol` and companions.
>
> By the universal property of `J(T)` a realization is the same thing as a compatible
> assignment of the generators satisfying the six generator-level transformation laws of
> `GaugeFieldData.Assignment.IsEquivariant`, the connection law being affine: a jet moves a
> connection generator by the transport of its inverse plus the Maurer–Cartan shift.

## ii. Key results

> - `GaugeFieldData.Realization` : an algebra carrying the fields of a datum.
> - `GaugeFieldData.Realization.gaugeRealization` : the gauge bosons of a realization, with
>   `toAlgHom_covDerivFieldStrength` identifying the realized field-strength tower.
> - `GaugeFieldData.Realization.toAlgHom_covDerivFermion` and companions : the realized
>   covariant matter towers are the towers of the realized symbols.
> - `GaugeFieldData.Assignment.IsEquivariant` : the generator-level equivariance of an
>   assignment, with `IsEquivariant.toRealization` and
>   `GaugeFieldData.realizationEquivAssignment`.

## iv. References

> * None.

## A. Realizations

**`GaugeFieldData.Realization`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L77).

> A complex algebra `B` carrying the fields of the datum `T`: a complex algebra map out
> of the local field algebra, equivariant for the jet gauge group and the Lorentz group,
> both acting on the whole of `B` by algebra endomorphisms. No commutativity, injectivity
> or surjectivity is assumed, and no derivative operator on `B` is involved. It is built
> from the fields `toAlgHom`, `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of
> `Representation.EquivariantAlgHom`, which the lemmas `map_repJet`, `map_repLorentz`,
> `repJet_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (T : GaugeFieldData jets) (B : Type) [Ring B] [Algebra ℂ B]
    (repJet : Representation ℂ GJ B) (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.Realization.id`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L89).

> The local field algebra realized in itself, by the identity.

```lean
noncomputable def id : Realization T T.LocalFieldAlgebra T.repJet T.repLorentzGroup
```

**`GaugeFieldData.Realization.id_toAlgHom`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L94).

```lean
lemma id_toAlgHom : (id T).toAlgHom = AlgHom.id ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.Realization.ext_generators`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L98).

> Two realizations agreeing on the generators of every species and on the connection
> generators are equal.

```lean
lemma ext_generators {h₁ h₂ : Realization T B repJet repLorentz}
    (hf : ∀ i x, h₁.toAlgHom (T.ιFermion i x) = h₂.toAlgHom (T.ιFermion i x))
    (hb : ∀ j y, h₁.toAlgHom (T.ιBoson j y) = h₂.toAlgHom (T.ιBoson j y))
    (ha : ∀ v, h₁.toAlgHom (T.ιConnection v) = h₂.toAlgHom (T.ιConnection v)) : h₁ = h₂
```

**`GaugeFieldData.Realization.map_repJet`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L107).

> The map is equivariant for the jet gauge group.

```lean
lemma map_repJet (U : GJ) (x : T.LocalFieldAlgebra) :
    h.toAlgHom (T.repJet U x) = repJet U (h.toAlgHom x)
```

**`GaugeFieldData.Realization.map_repLorentz`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L112).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : T.LocalFieldAlgebra) :
    h.toAlgHom (T.repLorentzGroup Λ x) = repLorentz Λ (h.toAlgHom x)
```

**`GaugeFieldData.Realization.repJet_mul`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L118).

> The jet gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repJet_mul (U : GJ) (b₁ b₂ : B) : repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
```

**`GaugeFieldData.Realization.repLorentz_mul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L123).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. The assignment of a realization

**`GaugeFieldData.Realization.toAssignment`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L135).

> The generator images of a realization, as a compatible assignment: the inverse of the
> universal property applied to its algebra map.

```lean
noncomputable def toAssignment : T.Assignment B
```

**`GaugeFieldData.Realization.toAssignment_fermion`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L137).

```lean
lemma toAssignment_fermion (i : T.FermionSpecies) (x : JetComponentSpace (T.fermion i)) :
    h.toAssignment.fermion i x = h.toAlgHom (T.ιFermion i x)
```

**`GaugeFieldData.Realization.toAssignment_boson`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L140).

```lean
lemma toAssignment_boson (j : T.BosonSpecies) (y : JetComponentSpace (T.boson j)) :
    h.toAssignment.boson j y = h.toAlgHom (T.ιBoson j y)
```

**`GaugeFieldData.Realization.toAssignment_connection`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L143).

```lean
lemma toAssignment_connection (v : GaugeBoson.JetComponentSpace 𝔤) :
    h.toAssignment.connection v = h.toAlgHom (T.ιConnection v)
```

**`GaugeFieldData.Realization.lift_toAssignment`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L147).

```lean
lemma lift_toAssignment : h.toAssignment.lift = h.toAlgHom
```

## C. The gauge bosons of a realization

**`GaugeFieldData.Realization.gaugeRealization`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L158).

> The gauge bosons of a realization: the connection factor of `J(T)` carried into `B`,
> so that the gauge-boson symbol theory applies to the images.

```lean
noncomputable def gaugeRealization : GaugeAlgebraRealization jets B repJet repLorentz
```

**`GaugeFieldData.Realization.gaugeRealization_A`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L170).

```lean
lemma gaugeRealization_A (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    h.gaugeRealization.A s μ φ = h.toAlgHom (T.gaugeRealization.A s μ φ)
```

**`GaugeFieldData.Realization.id_gaugeRealization_A`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L175).

```lean
lemma id_gaugeRealization_A : (id T).gaugeRealization.A = T.gaugeRealization.A
```

**`GaugeFieldData.Realization.toAlgHom_covDerivFieldStrength`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L179).

> The map of a realization carries the included field-strength tower to the covariant
> tower of the realized gauge-boson symbols.

```lean
lemma toAlgHom_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    h.toAlgHom (T.covDerivFieldStrength l μ ν φ)
      = GaugeAlgebraRealization.iteratedCovDerivAdjoint h.gaugeRealization.A l
        (GaugeAlgebraRealization.fieldStrength h.gaugeRealization.A μ ν) 0 φ
```

## D. The matter symbols and towers of a realization

**`GaugeFieldData.Realization.fermionSymbol`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L196).

> The realized derivative symbols of a fermionic species.

```lean
noncomputable def fermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] B
```

**`GaugeFieldData.Realization.conjFermionSymbol`**, a def, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L201).

> The realized conjugate derivative symbols of a fermionic species.

```lean
noncomputable def conjFermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] B
```

**`GaugeFieldData.Realization.bosonSymbol`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L206).

> The realized derivative symbols of a bosonic species.

```lean
noncomputable def bosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] B
```

**`GaugeFieldData.Realization.conjBosonSymbol`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L211).

> The realized conjugate derivative symbols of a bosonic species.

```lean
noncomputable def conjBosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] B
```

**`GaugeFieldData.Realization.toAlgHom_covDerivFermion`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L218).

> The realized covariant tower of a fermionic species is the covariant tower of its
> realized symbols, computed against the realized gauge-boson symbols. No derivative
> operator on `B` is involved: both sides are the same finite algebraic expression.

```lean
lemma toAlgHom_covDerivFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    h.toAlgHom (T.covDerivFermion i l φ)
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A (T.fermion i).repAlgebra
        (h.fermionSymbol i) n l 0 φ
```

**`GaugeFieldData.Realization.toAlgHom_covDerivConjFermion`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L227).

```lean
lemma toAlgHom_covDerivConjFermion (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    h.toAlgHom (T.covDerivConjFermion i l φ)
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A
        (LocalGaugeData.actionConj (T.fermion i).repAlgebra) (h.conjFermionSymbol i) n l 0 φ
```

**`GaugeFieldData.Realization.toAlgHom_covDerivBoson`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L236).

```lean
lemma toAlgHom_covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    h.toAlgHom (T.covDerivBoson j l φ)
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A (T.boson j).repAlgebra
        (h.bosonSymbol j) n l 0 φ
```

**`GaugeFieldData.Realization.toAlgHom_covDerivConjBoson`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L245).

```lean
lemma toAlgHom_covDerivConjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    h.toAlgHom (T.covDerivConjBoson j l φ)
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A
        (LocalGaugeData.actionConj (T.boson j).repAlgebra) (h.conjBosonSymbol j) n l 0 φ
```

## E. Equivariant assignments

**`GaugeFieldData.Assignment.IsEquivariant`**, a structure, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L267).

> The generator-level transformation laws of an assignment: each matter species
> transforms by the jet action of its own component space, and the connection generators
> transform affinely, by the transport of the inverse jet plus its Maurer–Cartan shift.
> The Lorentz laws are all linear. These are the laws the generators of `J(T)` themselves
> satisfy.

```lean
structure Assignment.IsEquivariant {B : Type} [Ring B] [Algebra ℂ B] (d : T.Assignment B)
    (repJet : Representation ℂ GJ B) (repLorentz : Representation ℂ SL(2,ℂ) B) : Prop where
  /-- A jet acts on the generators of a fermionic species by the action of its component
    space. -/
  repJet_fermion : ∀ (U : GJ) (i : T.FermionSpecies) (x : JetComponentSpace (T.fermion i)),
    repJet U (d.fermion i x) = d.fermion i (JetComponentSpace.repJet (T.fermion i) U x)
  /-- A jet acts on the generators of a bosonic species by the action of its component
    space. -/
  repJet_boson : ∀ (U : GJ) (j : T.BosonSpecies) (y : JetComponentSpace (T.boson j)),
    repJet U (d.boson j y) = d.boson j (JetComponentSpace.repJet (T.boson j) U y)
  /-- A jet acts affinely on the connection generators. -/
  repJet_connection : ∀ (U : GJ) (v : GaugeBoson.JetComponentSpace 𝔤),
    repJet U (d.connection v) = d.connection (LocalGaugeFieldAlgebra.transport jets U⁻¹ v)
      + (LocalGaugeFieldAlgebra.mcShift jets U⁻¹ v : ℂ) • (1 : B)
  /-- A Lorentz transformation acts on the generators of a fermionic species by the action
    of its component space. -/
  repLorentz_fermion : ∀ (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)), repLorentz Λ (d.fermion i x)
      = d.fermion i (JetComponentSpace.repLorentzGroup (T.fermion i) Λ x)
  /-- A Lorentz transformation acts on the generators of a bosonic species by the action of
    its component space. -/
  repLorentz_boson : ∀ (Λ : SL(2,ℂ)) (j : T.BosonSpecies)
    (y : JetComponentSpace (T.boson j)), repLorentz Λ (d.boson j y)
      = d.boson j (JetComponentSpace.repLorentzGroup (T.boson j) Λ y)
  /-- A Lorentz transformation acts linearly on the connection generators. -/
  repLorentz_connection : ∀ (Λ : SL(2,ℂ)) (v : GaugeBoson.JetComponentSpace 𝔤),
    repLorentz Λ (d.connection v)
      = d.connection (GaugeBoson.JetComponentSpace.repLorentzGroup 𝔤 Λ v)
```

**`GaugeFieldData.Realization.toAssignment_isEquivariant`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L303).

> The assignment of a realization is equivariant: the laws are those of the generators of
> `J(T)`, transported along the map.

```lean
lemma _root_.GaugeFieldData.Realization.toAssignment_isEquivariant
    (h : Realization T B repJet repLorentz) :
    h.toAssignment.IsEquivariant repJet repLorentz
```

**`GaugeFieldData.Assignment.IsEquivariant.lift_comp_repJetAlgHom`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L328).

> The lift of an equivariant assignment intertwines the jet gauge actions, as an equality
> of algebra maps: both sides agree on the generators of every species and on the
> connection generators.

```lean
lemma IsEquivariant.lift_comp_repJetAlgHom {d : T.Assignment B}
    (hd : d.IsEquivariant repJet repLorentz)
    (hJ : ∀ (U : GJ) (b₁ b₂ : B), repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂) (U : GJ) :
    d.lift.comp (T.repJetAlgHom U) = (repJet.toAlgHom hJ U).comp d.lift
```

**`GaugeFieldData.Assignment.IsEquivariant.lift_comp_repLorentzAlgHom`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L343).

> The lift of an equivariant assignment intertwines the Lorentz actions, as an equality of
> algebra maps.

```lean
lemma IsEquivariant.lift_comp_repLorentzAlgHom {d : T.Assignment B}
    (hd : d.IsEquivariant repJet repLorentz)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂) (Λ : SL(2,ℂ)) :
    d.lift.comp (T.repLorentzAlgHom Λ) = (repLorentz.toAlgHom hL Λ).comp d.lift
```

**`GaugeFieldData.Assignment.IsEquivariant.toRealization`**, a def, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L361).

> An equivariant assignment lifts to a realization: each equivariance law is an equality
> of two algebra maps agreeing on the generators, so it follows from the generator laws by
> the universal property.

```lean
noncomputable def IsEquivariant.toRealization {d : T.Assignment B}
    (hd : d.IsEquivariant repJet repLorentz)
    (hJ : ∀ (U : GJ) (b₁ b₂ : B), repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂) :
    Realization T B repJet repLorentz
```

**`GaugeFieldData.Assignment.IsEquivariant.toRealization_toAlgHom`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L374).

```lean
lemma IsEquivariant.toRealization_toAlgHom {d : T.Assignment B}
    (hd : d.IsEquivariant repJet repLorentz)
    (hJ : ∀ (U : GJ) (b₁ b₂ : B), repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂) :
    (hd.toRealization hJ hL).toAlgHom = d.lift
```

**`GaugeFieldData.realizationEquivAssignment`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean#L387).

> The mapping-out universal property of `J(T)` in equivariant form: for target actions by
> algebra endomorphisms, realizations of `T` in `B` are exactly the equivariant compatible
> assignments of its generators.

```lean
noncomputable def realizationEquivAssignment {B : Type} [Ring B] [Algebra ℂ B]
    {repJet : Representation ℂ GJ B} {repLorentz : Representation ℂ SL(2,ℂ) B}
    (hJ : ∀ (U : GJ) (b₁ b₂ : B), repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂) :
    {d : T.Assignment B // d.IsEquivariant repJet repLorentz}
      ≃ Realization T B repJet repLorentz
```

## Depends on

- [The covariant derivatives in the local field algebra](localfield-covariantderiv.md)
- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Realization.lean)
