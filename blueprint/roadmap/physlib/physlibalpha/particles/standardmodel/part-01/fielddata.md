---
declaration: module
origin: cited
lean: StandardModel.FermionType, StandardModel.FermionType.matterField, StandardModel.FermionType.matterField_leptonDoublet, StandardModel.FermionType.matterField_leptonSinglet, StandardModel.FermionType.matterField_quarkDoublet, StandardModel.FermionType.matterField_upSinglet, StandardModel.FermionType.matterField_downSinglet, StandardModel.FermionType.matterField_massWeight
statement: formalized
proof: formalized
---

# The field data of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.FieldData`, [PhyslibAlpha/Particles/StandardModel/FieldData.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean): 30 declarations, 25 with a docstring.

> The fifteen fermion species and the Higgs as the field data over the Standard Model global
> gauge group, with their conditions and mass weights.

## i. Overview

> `GaugeFieldData G` is the matter content of a gauge theory over a global gauge group `G`, a
> family of fermionic species and a family of bosonic species, each given by a
> `MatterField`. The Standard Model has all the pieces, the global gauge group
> `StandardModel.globalGaugeGroup` and the five fermion types and the Higgs already packaged as
> matter fields, and this file assembles them into `StandardModel.fieldData`.
>
> The fermionic species are the constructors of `FermionType`, fifteen multiplets, one of
> the five types in one of the three generations, each occurring exactly once. The
> generation index is an argument of each constructor, so the species type is the
> enumeration itself and carries no further factor. The matter field does not depend on the
> generation, three generations being three copies of one multiplet distinguished only by
> their Yukawa couplings, which are not field data. The bosonic family has the single Higgs
> multiplet. The fermions are declared fermionic and the Higgs bosonic, as `GaugeFieldData`
> requires of its two families. The gauge bosons are not a species. Their generator space is
> fixed by the gauge algebra alone, and `GaugeFieldData` supplies it as the connection sector.
>
> From the datum the generic theory produces the generator spaces, the local field algebra
> `fieldData.LocalFieldAlgebra`, the transformation data and the realization arrow, with no
> further Standard Model input.

## ii. Key results

> - `StandardModel.FermionType` : the fifteen fermion species, the five types in each of
>   the three generations.
> - `StandardModel.fieldData` : the field data of the Standard Model.
> - `StandardModel.card_fieldData_fermionSpecies`,
>   `StandardModel.card_fieldData_bosonSpecies` : fifteen fermionic multiplets, one Higgs.
> - `StandardModel.fieldData_lorentzContinuous`, `StandardModel.fieldData_gaugeLorentzCommute` :
>   the Lorentz representations are continuous and commute with the gauge representations.
> - `StandardModel.fieldData_gaugeLorentzCompatible` : the datum satisfies the condition
>   of the covariant derivative theory, derived from `StandardModel.fieldData_gaugeLorentzCommute`.
> - `StandardModel.fieldData_mem_invariants_iff_exists_mem_invariants` : the invariants of any
>   realization of the local field algebra of the Standard Model are the images of the invariants
>   of its covariant field algebra.
> - `StandardModel.fieldData_massWeightScaleFermion_inclFermion_basis_tmul`,
>   `StandardModel.fieldData_massWeightScaleBoson_inclBoson_basis_tmul` : a fermionic component
>   function `∂_s ψ_α` scales by `c ^ (3 + 2 |s|)`, a Higgs component by `c ^ (2 + 2 |s|)`.
> - `StandardModel.massWeightPoly_fieldData_fermionSymbol`,
>   `StandardModel.massWeightPoly_fieldData_bosonSymbol` and their conjugates : the fermion
>   symbols have mass weight `3 + 2 |s|`, the Higgs symbols `2 + 2 |s|`.

## iv. References

> * None.

## A. The fermion species

**`StandardModel.FermionType`**, an inductive, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L95).

> The fifteen fermion species of the Standard Model, each of the five fermion types in
> each of the three generations, the generation `i : Fin 3` carried by the constructor.
> Two generations of one type share a matter field but are distinct species.

```lean
inductive FermionType where
  /-- The lepton doublet of generation `i`, `(1, 2)_{-3}`. -/
  | leptonDoublet (i : Fin 3) : FermionType
  /-- The charged-lepton singlet of generation `i`, `(1, 1)_{-6}`. -/
  | leptonSinglet (i : Fin 3) : FermionType
  /-- The quark doublet of generation `i`, `(3, 2)_{1}`. -/
  | quarkDoublet (i : Fin 3) : FermionType
  /-- The up-type quark singlet of generation `i`, `(3, 1)_{4}`. -/
  | upSinglet (i : Fin 3) : FermionType
  /-- The down-type quark singlet of generation `i`, `(3, 1)_{-2}`. -/
  | downSinglet (i : Fin 3) : FermionType

deriving DecidableEq, Fintype
```

**`StandardModel.FermionType.matterField`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L113).

> The matter field of a fermion species, that of its type. It is the same in every
> generation.

```lean
noncomputable def matterField : FermionType → globalGaugeGroup.MatterField
```

**`StandardModel.FermionType.matterField_leptonDoublet`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L121).

```lean
lemma matterField_leptonDoublet (i : Fin 3) :
    matterField (.leptonDoublet i) = LeptonDoubletV.matterField
```

**`StandardModel.FermionType.matterField_leptonSinglet`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L125).

```lean
lemma matterField_leptonSinglet (i : Fin 3) :
    matterField (.leptonSinglet i) = LeptonSinglet.matterField
```

**`StandardModel.FermionType.matterField_quarkDoublet`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L129).

```lean
lemma matterField_quarkDoublet (i : Fin 3) :
    matterField (.quarkDoublet i) = QuarkDoublet.matterField
```

**`StandardModel.FermionType.matterField_upSinglet`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L133).

```lean
lemma matterField_upSinglet (i : Fin 3) :
    matterField (.upSinglet i) = UpSinglet.matterField
```

**`StandardModel.FermionType.matterField_downSinglet`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L137).

```lean
lemma matterField_downSinglet (i : Fin 3) :
    matterField (.downSinglet i) = DownSinglet.matterField
```

**`StandardModel.FermionType.matterField_massWeight`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L142).

> Every Standard Model fermion carries mass weight three, in every generation.

```lean
lemma matterField_massWeight (t : FermionType) : (matterField t).massWeight = 3
```

**`StandardModel.FermionType.matterField_statistic`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L147).

> Every Standard Model fermion is declared fermionic, in every generation.

```lean
lemma matterField_statistic (t : FermionType) : (matterField t).statistic = .fermionic
```

## B. The field datum

**`StandardModel.fieldData`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L160).

> The field data of the Standard Model, three generations of each of the five fermion
> types and one Higgs multiplet, over the global gauge group `StandardModel.globalGaugeGroup`.

```lean
noncomputable def fieldData : GaugeFieldData globalGaugeGroup
```

**`StandardModel.fieldData_fermionSpecies`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L170).

> The fermionic species are the fifteen fermion types.

```lean
lemma fieldData_fermionSpecies : fieldData.FermionSpecies = FermionType
```

**`StandardModel.fieldData_fermion`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L174).

> A fermionic species is the multiplet of its type, whichever generation it is in.

```lean
lemma fieldData_fermion (t : FermionType) : fieldData.fermion t = t.matterField
```

**`StandardModel.fieldData_bosonSpecies`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L178).

> There is one bosonic species.

```lean
lemma fieldData_bosonSpecies : fieldData.BosonSpecies = Unit
```

**`StandardModel.fieldData_boson`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L182).

> The one bosonic species is the Higgs multiplet.

```lean
lemma fieldData_boson (j : fieldData.BosonSpecies) :
    fieldData.boson j = HiggsVec.matterField
```

**`StandardModel.card_fieldData_fermionSpecies`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L187).

> There are fifteen fermionic multiplets, each of the five types in each of the three
> generations, exactly once.

```lean
lemma card_fieldData_fermionSpecies : Nat.card fieldData.FermionSpecies = 15
```

**`StandardModel.card_fieldData_bosonSpecies`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L193).

> Exactly one bosonic multiplet, the Higgs.

```lean
lemma card_fieldData_bosonSpecies : Nat.card fieldData.BosonSpecies = 1
```

## C. The conditions on the species

> The global gauge group of the Standard Model is compact, and on every species the Lorentz
> representation is continuous and commutes with the gauge representation. These are the
> hypotheses under which the invariants of a realization of the local field algebra descend to
> the covariant field algebra. The commutation implies its infinitesimal form
> `GaugeFieldData.GaugeLorentzCompatible`, the condition of the covariant derivative theory.

**`StandardModel.fieldData_fermion_lorentzContinuous`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L210).

> The Lorentz action on every fermionic species of the Standard Model is continuous.

```lean
lemma fieldData_fermion_lorentzContinuous (t : FermionType) :
    (fieldData.fermion t).LorentzContinuous
```

**`StandardModel.fieldData_lorentzContinuous`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L220).

> The Lorentz action on every species of the Standard Model is continuous.

```lean
lemma fieldData_lorentzContinuous : fieldData.LorentzContinuous
```

**`StandardModel.fieldData_fermion_gaugeLorentzCommute`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L225).

> The gauge and Lorentz representations of every fermionic species of the Standard Model
> commute.

```lean
lemma fieldData_fermion_gaugeLorentzCommute (t : FermionType) :
    (fieldData.fermion t).GaugeLorentzCommute
```

**`StandardModel.fieldData_gaugeLorentzCommute`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L235).

> The gauge and Lorentz representations of every species of the Standard Model commute.

```lean
lemma fieldData_gaugeLorentzCommute : fieldData.GaugeLorentzCommute
```

**`StandardModel.fieldData_gaugeLorentzCompatible`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L240).

> The infinitesimal gauge action commutes with the Lorentz action on every species of the
> Standard Model.

```lean
lemma fieldData_gaugeLorentzCompatible : fieldData.GaugeLorentzCompatible
```

**`StandardModel.fieldData_mem_invariants_iff_exists_mem_invariants`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L247).

> The invariants of a realization of the local field algebra of the Standard Model are the
> images of the invariants of its covariant field algebra. An element `k x` is invariant under
> the jet gauge group and the Lorentz group exactly when it is the image of a covariant
> expression invariant under the ordinary gauge group and the Lorentz group.

```lean
lemma fieldData_mem_invariants_iff_exists_mem_invariants {B : Type} [Ring B] [Algebra ℂ B]
    {repJet : Representation ℂ globalGaugeGroup.gaugeJetGroup B}
    {repLorentz : Representation ℂ SL(2,ℂ) B}
    (k : GaugeFieldData.Realization fieldData B repJet repLorentz)
    (x : fieldData.LocalFieldAlgebra) :
    k.toAlgHom x ∈ repJet.invariants ∧ k.toAlgHom x ∈ repLorentz.invariants ↔
      ∃ a' : fieldData.LocalCovFieldAlgebra,
        a' ∈ (GaugeFieldData.LocalCovFieldAlgebra.repValue fieldData).invariants ∧
        a' ∈ (GaugeFieldData.LocalCovFieldAlgebra.repLorentzGroup fieldData
          fieldData_gaugeLorentzCompatible).invariants ∧
        k.toAlgHom (a' : fieldData.LocalFieldAlgebra) = k.toAlgHom x
```

## D. The mass weights

> A Standard Model fermion carries mass weight three and the Higgs weight two, in the units
> in which a derivative has weight two. The first two are read off the matter fields, the
> third is already built into the generator spaces.

**`StandardModel.fieldData_fermion_massWeight`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L273).

> Every fermionic species of the datum carries mass weight three.

```lean
lemma fieldData_fermion_massWeight (j : fieldData.FermionSpecies) :
    (fieldData.fermion j).massWeight = 3
```

**`StandardModel.fieldData_boson_massWeight`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L279).

> The Higgs multiplet carries mass weight two.

```lean
lemma fieldData_boson_massWeight (j : fieldData.BosonSpecies) :
    (fieldData.boson j).massWeight = 2
```

**`StandardModel.fieldData_massWeightScaleFermion_inclFermion_basis_tmul`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L284).

> A fermionic component function `∂_s ψ_α` scales by `c ^ (3 + 2 |s|)`, whichever
> species it belongs to.

```lean
lemma fieldData_massWeightScaleFermion_inclFermion_basis_tmul (c : ℂ)
    (j : fieldData.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (fieldData.FermionValue j)) :
    fieldData.massWeightScaleFermion c (fieldData.inclFermion j
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
          FieldDerivSpace (fieldData.fermion j)))
      = c ^ (3 + 2 * Multiset.card s) • fieldData.inclFermion j
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
            FieldDerivSpace (fieldData.fermion j))
```

**`StandardModel.fieldData_massWeightScaleBoson_inclBoson_basis_tmul`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L298).

> A Higgs component function `∂_s H_α` scales by `c ^ (2 + 2 |s|)`.

```lean
lemma fieldData_massWeightScaleBoson_inclBoson_basis_tmul (c : ℂ)
    (j : fieldData.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (fieldData.BosonValue j)) :
    fieldData.massWeightScaleBoson c (fieldData.inclBoson j
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
          FieldDerivSpace (fieldData.boson j)))
      = c ^ (2 + 2 * Multiset.card s) • fieldData.inclBoson j
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
            FieldDerivSpace (fieldData.boson j))
```

**`StandardModel.massWeightPoly_fieldData_fermionSymbol`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L313).

> The symbols of every fermionic species of the field datum have mass weight
> `3 + 2 |s|`, every fermion having mass dimension `3/2`.

```lean
lemma massWeightPoly_fieldData_fermionSymbol (t : FermionType) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (fieldData.FermionValue t)) :
    fieldData.massWeightPoly (fieldData.fermionSymbol t s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (fieldData.fermionSymbol t s φ)
```

**`StandardModel.massWeightPoly_fieldData_conjFermionSymbol`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L323).

> The conjugate symbols of every fermionic species of the field datum have mass weight
> `3 + 2 |s|`.

```lean
lemma massWeightPoly_fieldData_conjFermionSymbol (t : FermionType)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (fieldData.FermionValue t))) :
    fieldData.massWeightPoly (fieldData.conjFermionSymbol t s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (fieldData.conjFermionSymbol t s φ)
```

**`StandardModel.massWeightPoly_fieldData_bosonSymbol`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L333).

> The symbols of the Higgs, the one bosonic species of the field datum, have mass weight
> `2 + 2 |s|`, the Higgs field having mass dimension one.

```lean
lemma massWeightPoly_fieldData_bosonSymbol (j : fieldData.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (fieldData.BosonValue j)) :
    fieldData.massWeightPoly (fieldData.bosonSymbol j s φ)
      = Polynomial.monomial (2 + 2 * Multiset.card s) (fieldData.bosonSymbol j s φ)
```

**`StandardModel.massWeightPoly_fieldData_conjBosonSymbol`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L342).

> The conjugate symbols of the Higgs have mass weight `2 + 2 |s|`.

```lean
lemma massWeightPoly_fieldData_conjBosonSymbol (j : fieldData.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (fieldData.BosonValue j))) :
    fieldData.massWeightPoly (fieldData.conjBosonSymbol j s φ)
      = Polynomial.monomial (2 + 2 * Multiset.card s) (fieldData.conjBosonSymbol j s φ)
```

## Depends on

- [The covariant field algebra of a gauge theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-basic.md)
- [The mass-weight filtration and the invariants of a local field algebra](../../../classicalfieldtheory/gaugetheory/part-04/localfieldalgebra-massweight.md)
- [Realizations of the local field algebra](../../../classicalfieldtheory/gaugetheory/part-04/localfieldalgebra-realization.md)
- [The down-type singlet as a matter field](fermions-downsinglet-matterfield.md)
- [The lepton doublet as a matter field](fermions-leptondoublet-matterfield.md)
- [The charged-lepton singlet as a matter field](fermions-leptonsinglet-matterfield.md)
- [The quark doublet as a matter field](fermions-quarkdoublet-matterfield.md)
- [The up-type singlet as a matter field](fermions-upsinglet-matterfield.md)
- [The Higgs field as a matter field](../part-02/higgsboson-matterfield.md)

## Proof depends on

- [Invariants descend along realizations](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/FieldData.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/FieldData.lean)
