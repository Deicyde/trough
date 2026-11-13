---
declaration: module
origin: cited
lean: StandardModel.Model.gauge, StandardModel.Model.gaugeData, StandardModel.Model.factors, StandardModel.Model.quarkDoublet, StandardModel.Model.leptonDoublet, StandardModel.Model.upSinglet, StandardModel.Model.downSinglet, StandardModel.Model.leptonSinglet
statement: formalized
proof: formalized
---

# The Standard Model

The module `PhyslibAlpha.Particles.StandardModel.Basic`, [PhyslibAlpha/Particles/StandardModel/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean): 15 declarations (1 instance with no name), 14 with a docstring.

## i. Overview

> The Standard Model as a model table: the gauge group `SU(3) × SU(2) × U(1)` named by its
> factors, each field as its Lorentz label and its charges, and the table assigning each
> field its number of generations. Everything else is derived: the local gauge data of the
> gauge group is assembled from the factors by `LocalGaugeData.ofFactors`, and the table
> compiles, through `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Table`,
> to the field content `StandardModel.Model.fieldData : GaugeFieldData gaugeData`, from
> which the general theory derives the algebra of field operators and the gauge and Lorentz
> actions.
>
> The charges are listed in the order of the factors: the `SU(3)` label, the `SU(2)` label
> and the hypercharge. Hypercharges are integers, six times the conventional `Y`, so that
> the gauge group acting is the honest `U(1)` of unitary jets. The right-handed singlets are
> right-handed Weyl spinors in the fundamental of colour rather than conjugate left-handed
> fields.

## ii. Key results

> - `StandardModel.Model.gauge` : the gauge group, as a list of factors.
> - `StandardModel.Model.gaugeData` : its local gauge data.
> - `StandardModel.Model.quarkDoublet`, `leptonDoublet`, `upSinglet`, `downSinglet`,
>   `leptonSinglet`, `higgs` : the fields, as their Lorentz label and charges.
> - `StandardModel.Model.table` : the table, each field with its number of generations.
> - `StandardModel.Model.fieldData` : the field content of the Standard Model.

## iv. References

> * None.

## A. The gauge group

**`StandardModel.Model.gauge`**, an abbrev, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L66).

> The gauge group `SU(3) × SU(2) × U(1)`, as a list of factors.

```lean
abbrev gauge : List FactorSpec
```

**`StandardModel.Model.gaugeData`**, an abbrev, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L70).

> The local gauge data of the Standard Model gauge group: jets of `SU(3) × SU(2) × U(1)`
> gauge transformations with their Lie algebra of jets.

```lean
noncomputable abbrev gaugeData
```

**`StandardModel.Model.factors`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L73).

> The factors of the gauge group, as what the rows are charged under.

```lean
noncomputable abbrev factors : Factors gaugeData
```

## B. The fields

> Each field is its Lorentz label and its charges in the order of the factors: the `SU(3)`
> label, the `SU(2)` label and the hypercharge.

**`StandardModel.Model.quarkDoublet`**, an abbrev, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L85).

> The quark doublet `q ∼ (3, 2)_{1}`.

```lean
abbrev quarkDoublet : MatterFieldData factors
```

**`StandardModel.Model.leptonDoublet`**, an abbrev, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L88).

> The lepton doublet `l ∼ (1, 2)_{-3}`.

```lean
abbrev leptonDoublet : MatterFieldData factors
```

**`StandardModel.Model.upSinglet`**, an abbrev, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L91).

> The up-type quark singlet `u ∼ (3, 1)_{4}`.

```lean
abbrev upSinglet : MatterFieldData factors
```

**`StandardModel.Model.downSinglet`**, an abbrev, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L94).

> The down-type quark singlet `d ∼ (3, 1)_{-2}`.

```lean
abbrev downSinglet : MatterFieldData factors
```

**`StandardModel.Model.leptonSinglet`**, an abbrev, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L97).

> The charged-lepton singlet `e ∼ (1, 1)_{-6}`.

```lean
abbrev leptonSinglet : MatterFieldData factors
```

**`StandardModel.Model.higgs`**, an abbrev, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L100).

> The Higgs `H ∼ (1, 2)_{3}`.

```lean
abbrev higgs : MatterFieldData factors
```

**`StandardModel.Model.Fields`**, an inductive, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L103).

> The fields of the Standard Model.

```lean
inductive Fields
  /-- The quark doublet. -/
  | q
  /-- The lepton doublet. -/
  | l
  /-- The up-type quark singlet. -/
  | u
  /-- The down-type quark singlet. -/
  | d
  /-- The charged-lepton singlet. -/
  | e
  /-- The Higgs. -/
  | H
  deriving DecidableEq, Repr
```

**An instance with no name**, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L118).

```lean
instance : Fintype Fields
```

## C. The field content

**`StandardModel.Model.table`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L128).

> **The Standard Model table**: each field with its number of generations, three for the
> fermions and one for the Higgs.

```lean
def table : FieldData factors Fields
```

**`StandardModel.Model.fieldData`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L138).

> **The field content of the Standard Model**: the fifteen fermionic species (five fields
> in three generations) and the Higgs, as matter fields of `gaugeData`.

```lean
noncomputable def fieldData : GaugeFieldData gaugeData
```

**`StandardModel.Model.card_fermionSpecies`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L141).

> The Standard Model has fifteen fermionic species.

```lean
lemma card_fermionSpecies : Fintype.card fieldData.FermionSpecies = 15
```

**`StandardModel.Model.card_bosonSpecies`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean#L144).

> The Standard Model has one bosonic species.

```lean
lemma card_bosonSpecies : Fintype.card fieldData.BosonSpecies = 1
```

## Depends on

- [Local gauge data from a list of factors](../../../classicalfieldtheory/gaugetheory/part-04/localgaugedata-offactors.md)
- [Model tables](../../../classicalfieldtheory/gaugetheory/part-06/matterfield-matrixrep-table.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Basic.lean)
