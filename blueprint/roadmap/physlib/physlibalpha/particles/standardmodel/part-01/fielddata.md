---
declaration: module
origin: cited
lean: StandardModel.FermionType, StandardModel.FermionType.matterField, StandardModel.FermionType.matterField_leptonDoublet, StandardModel.FermionType.matterField_leptonSinglet, StandardModel.FermionType.matterField_quarkDoublet, StandardModel.FermionType.matterField_upSinglet, StandardModel.FermionType.matterField_downSinglet, StandardModel.FermionType.matterField_massWeight
statement: formalized
proof: formalized
---

# The field data of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.FieldData`, [PhyslibAlpha/Particles/StandardModel/FieldData.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean): 28 declarations, 21 with a docstring.

## i. Overview

> `GaugeFieldData jets` is the matter content of a gauge theory over a gauge context: a
> family of fermionic species and a family of bosonic species, each given by a
> `MatterField`. The Standard Model has all the pieces — `StandardModel.localGaugeData` with its
> Taylor–Leibniz law, and the five fermion types and the Higgs already packaged as matter
> fields — and this file assembles them into `StandardModel.fieldData`.
>
> The fermionic species are the constructors of `FermionType`: fifteen multiplets, one of
> the five types in one of the three generations, each occurring exactly once. The
> generation index is an argument of each constructor, so the species type is the
> enumeration itself and carries no further factor. The matter field does not depend on the
> generation, three generations being three copies of one multiplet distinguished only by
> their Yukawa couplings, which are not field data. The bosonic family has the single Higgs
> multiplet. The fermions are declared fermionic and the Higgs bosonic, as `GaugeFieldData`
> requires of its two families. The gauge bosons are not a species: their generator space is
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
> - `StandardModel.fieldData_pureJetsActTrivially`,
>   `StandardModel.fieldData_gaugeLorentzCompatible` : the datum satisfies the two
>   conditions of the covariant derivative theory, assembled from the species-wise lemmas
>   `StandardModel.fieldData_fermion_pureJetsActTrivially` and companions.
> - `StandardModel.fieldData_massWeightScaleFermion_inclFermion_basis_tmul` : a fermionic
>   component function `∂_s ψ_α` scales by `c ^ (3 + 2 |s|)`.

## iv. References

> * None.

## A. The fermion species

**`StandardModel.FermionType`**, an inductive, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L78).

> The fifteen fermion species of the Standard Model: each of the five fermion types in
> each of the three generations, the generation `i : Fin 3` carried by the constructor.
> Two generations of one type share a representation package but are distinct species.

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

**`StandardModel.FermionType.matterField`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L96).

> The matter field of a fermion species, one of the five existing adapters. It is the
> same in every generation.

```lean
noncomputable def matterField : FermionType → MatterField localGaugeData
```

**`StandardModel.FermionType.matterField_leptonDoublet`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L104).

```lean
lemma matterField_leptonDoublet (i : Fin 3) :
    matterField (.leptonDoublet i) = LeptonDoubletV.matterField
```

**`StandardModel.FermionType.matterField_leptonSinglet`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L108).

```lean
lemma matterField_leptonSinglet (i : Fin 3) :
    matterField (.leptonSinglet i) = LeptonSinglet.matterField
```

**`StandardModel.FermionType.matterField_quarkDoublet`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L112).

```lean
lemma matterField_quarkDoublet (i : Fin 3) :
    matterField (.quarkDoublet i) = QuarkDoublet.matterField
```

**`StandardModel.FermionType.matterField_upSinglet`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L116).

```lean
lemma matterField_upSinglet (i : Fin 3) :
    matterField (.upSinglet i) = UpSinglet.matterField
```

**`StandardModel.FermionType.matterField_downSinglet`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L120).

```lean
lemma matterField_downSinglet (i : Fin 3) :
    matterField (.downSinglet i) = DownSinglet.matterField
```

**`StandardModel.FermionType.matterField_massWeight`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L125).

> Every Standard Model fermion carries mass weight three, in every generation.

```lean
lemma matterField_massWeight (t : FermionType) : (matterField t).massWeight = 3
```

**`StandardModel.FermionType.matterField_statistic`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L130).

> Every Standard Model fermion is declared fermionic, in every generation.

```lean
lemma matterField_statistic (t : FermionType) : (matterField t).statistic = .fermionic
```

**`StandardModel.FermionType.matterField_pureJetsActTrivially`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L134).

> Pure gauge jets act trivially on every Standard Model fermion at the base point.

```lean
lemma matterField_pureJetsActTrivially (t : FermionType) :
    (matterField t).PureJetsActTrivially
```

**`StandardModel.FermionType.matterField_gaugeLorentzCompatible`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L144).

> The gauge and Lorentz actions on every Standard Model fermion commute.

```lean
lemma matterField_gaugeLorentzCompatible (t : FermionType) :
    (matterField t).GaugeLorentzCompatible
```

## B. The field datum

**`StandardModel.fieldData`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L163).

> The field data of the Standard Model: three generations of each of the five fermion
> types and one Higgs multiplet, over the gauge context `StandardModel.localGaugeData`.

```lean
noncomputable def fieldData : GaugeFieldData localGaugeData
```

**`StandardModel.fieldData_fermionSpecies`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L172).

```lean
lemma fieldData_fermionSpecies : fieldData.FermionSpecies = FermionType
```

**`StandardModel.fieldData_fermion`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L176).

> A fermionic species is the multiplet of its type, whichever generation it is in.

```lean
lemma fieldData_fermion (t : FermionType) : fieldData.fermion t = t.matterField
```

**`StandardModel.fieldData_bosonSpecies`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L179).

```lean
lemma fieldData_bosonSpecies : fieldData.BosonSpecies = Unit
```

**`StandardModel.fieldData_boson`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L183).

> The one bosonic species is the Higgs multiplet.

```lean
lemma fieldData_boson (j : fieldData.BosonSpecies) :
    fieldData.boson j = HiggsVec.matterField
```

**`StandardModel.card_fieldData_fermionSpecies`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L188).

> Fifteen fermionic multiplets: each of the five types in each of the three
> generations, exactly once.

```lean
lemma card_fieldData_fermionSpecies : Nat.card fieldData.FermionSpecies = 15
```

**`StandardModel.card_fieldData_bosonSpecies`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L194).

> Exactly one bosonic multiplet, the Higgs.

```lean
lemma card_fieldData_bosonSpecies : Nat.card fieldData.BosonSpecies = 1
```

## C. The conditions of the covariant derivative theory

> Every species of the Standard Model satisfies the two conditions
> `MatterField.PureJetsActTrivially` and `MatterField.GaugeLorentzCompatible`, species by
> species, and the datum therefore satisfies the conjunctions
> `GaugeFieldData.PureJetsActTrivially` and `GaugeFieldData.GaugeLorentzCompatible`.

**`StandardModel.fieldData_fermion_pureJetsActTrivially`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L210).

> Pure gauge jets act trivially on every fermionic species of the Standard Model.

```lean
lemma fieldData_fermion_pureJetsActTrivially (t : FermionType) :
    (fieldData.fermion t).PureJetsActTrivially
```

**`StandardModel.fieldData_boson_pureJetsActTrivially`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L215).

> Pure gauge jets act trivially on the bosonic species of the Standard Model.

```lean
lemma fieldData_boson_pureJetsActTrivially (j : fieldData.BosonSpecies) :
    (fieldData.boson j).PureJetsActTrivially
```

**`StandardModel.fieldData_fermion_gaugeLorentzCompatible`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L221).

> The gauge and Lorentz actions commute on every fermionic species of the Standard
> Model.

```lean
lemma fieldData_fermion_gaugeLorentzCompatible (t : FermionType) :
    (fieldData.fermion t).GaugeLorentzCompatible
```

**`StandardModel.fieldData_boson_gaugeLorentzCompatible`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L226).

> The gauge and Lorentz actions commute on the bosonic species of the Standard Model.

```lean
lemma fieldData_boson_gaugeLorentzCompatible (j : fieldData.BosonSpecies) :
    (fieldData.boson j).GaugeLorentzCompatible
```

**`StandardModel.fieldData_pureJetsActTrivially`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L231).

> Pure gauge jets act trivially on every species of the Standard Model.

```lean
lemma fieldData_pureJetsActTrivially : fieldData.PureJetsActTrivially
```

**`StandardModel.fieldData_gaugeLorentzCompatible`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L235).

> The gauge and Lorentz actions commute on every species of the Standard Model.

```lean
lemma fieldData_gaugeLorentzCompatible : fieldData.GaugeLorentzCompatible
```

## D. The mass weights

> A Standard Model fermion carries mass weight three and the Higgs weight two, in the units
> in which a derivative has weight two. The first two are read off the matter fields, the
> third is already built into the generator spaces.

**`StandardModel.fieldData_fermion_massWeight`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L250).

> Every fermionic species of the datum carries mass weight three.

```lean
lemma fieldData_fermion_massWeight (j : fieldData.FermionSpecies) :
    (fieldData.fermion j).massWeight = 3
```

**`StandardModel.fieldData_boson_massWeight`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L256).

> The Higgs multiplet carries mass weight two.

```lean
lemma fieldData_boson_massWeight (j : fieldData.BosonSpecies) :
    (fieldData.boson j).massWeight = 2
```

**`StandardModel.fieldData_massWeightScaleFermion_inclFermion_basis_tmul`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L261).

> A fermionic component function `∂_s ψ_α` scales by `c ^ (3 + 2 |s|)`, whichever
> species it belongs to.

```lean
lemma fieldData_massWeightScaleFermion_inclFermion_basis_tmul (c : ℂ)
    (j : fieldData.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (fieldData.FermionValue j)) :
    fieldData.massWeightScaleFermion c (fieldData.inclFermion j
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
          JetComponentSpace (fieldData.fermion j)))
      = c ^ (3 + 2 * Multiset.card s) • fieldData.inclFermion j
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
            JetComponentSpace (fieldData.fermion j))
```

**`StandardModel.fieldData_massWeightScaleBoson_inclBoson_basis_tmul`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean#L275).

> A Higgs component function `∂_s H_α` scales by `c ^ (2 + 2 |s|)`.

```lean
lemma fieldData_massWeightScaleBoson_inclBoson_basis_tmul (c : ℂ)
    (j : fieldData.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (fieldData.BosonValue j)) :
    fieldData.massWeightScaleBoson c (fieldData.inclBoson j
        ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
          JetComponentSpace (fieldData.boson j)))
      = c ^ (2 + 2 * Multiset.card s) • fieldData.inclBoson j
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
            JetComponentSpace (fieldData.boson j))
```

## Depends on

- [The bosonic generators of a gauge theory](../../../classicalfieldtheory/gaugetheory/part-02/gaugefielddata-bosongenerators.md)
- [The fermionic generators of a gauge theory](../../../classicalfieldtheory/gaugetheory/part-02/gaugefielddata-fermiongenerators.md)
- [The Standard Model fermions as matter fields](../part-03/fermions-matterfield.md)
- [The Standard Model Higgs field as a matter field](../part-05/higgsboson-matterfield.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/FieldData.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/FieldData.lean)
