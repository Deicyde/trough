---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.matterField, StandardModel.HiggsVec.matterField_V, StandardModel.HiggsVec.matterField_repLorentz, StandardModel.HiggsVec.matterField_repJet, StandardModel.HiggsVec.matterField_repAlgebra, StandardModel.HiggsVec.matterField_massWeight, StandardModel.HiggsVec.matterField_pureJetsActTrivially, StandardModel.HiggsVec.matterField_gaugeLorentzCompatible
statement: formalized
proof: formalized
---

# The Standard Model Higgs field as a matter field

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.MatterField`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean): 8 declarations, 3 with a docstring.

## i. Overview

> `MatterField jets` bundles the value space of one field of a gauge theory over a gauge
> context `jets`, its Lorentz representation, the fibrewise action of the jets of gauge
> transformations, its mass weight and its declared statistics. The Higgs already carries the
> first four, and this file collects them, declared bosonic, as
> `PhyslibAlpha.Particles.StandardModel.Fermions.MatterField` does for the five fermion types.
> Nothing is redefined and no convention is changed: the `2_{3}` jet action and its
> fibrewise-linearity proof are the ones in
> `PhyslibAlpha.Particles.StandardModel.HiggsBoson.JetAlgebra.Basic`, the Higgs is a Lorentz
> scalar, and mass weight two is the weight already fixed by
> `HiggsJetAlgebra.massWeightScale`.

## ii. Key results

> - `StandardModel.HiggsVec.matterField` : the Higgs field as a matter field, with the four
>   projection rules identifying its fields with the existing definitions.
> - `StandardModel.HiggsVec.matterField_pureJetsActTrivially`,
>   `StandardModel.HiggsVec.matterField_gaugeLorentzCompatible` : the two conditions consumed
>   by the covariant derivative theory, restated from the Higgs files.

## iv. References

> * None.

## A. The Higgs as a matter field

**`StandardModel.HiggsVec.matterField`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L60).

> The Higgs field as a matter field of `StandardModel.localGaugeData`, valued in
> `HiggsVec`, in the `2_{3}` representation of the gauge group, a Lorentz scalar, of mass
> weight two, declared bosonic.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.HiggsVec.matterField_V`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L71).

```lean
lemma matterField_V : matterField.V = HiggsVec
```

**`StandardModel.HiggsVec.matterField_repLorentz`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L74).

```lean
lemma matterField_repLorentz :
    matterField.repLorentz = Representation.trivial ℂ SL(2,ℂ) HiggsVec
```

**`StandardModel.HiggsVec.matterField_repJet`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L78).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.HiggsVec.matterField_repAlgebra`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L81).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.HiggsVec.matterField_massWeight`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L84).

```lean
lemma matterField_massWeight : matterField.massWeight = 2
```

**`StandardModel.HiggsVec.matterField_pureJetsActTrivially`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L87).

> Pure gauge jets act trivially on the Higgs at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.HiggsVec.matterField_gaugeLorentzCompatible`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean#L91).

> The gauge action on the Higgs commutes with its (trivial) Lorentz action.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

## Depends on

- [The infinitesimal gauge action on the Higgs doublet](higgsboson-gaugealgebraaction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/MatterField.lean)
