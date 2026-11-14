---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV.matterField, StandardModel.LeptonDoubletV.matterField_V, StandardModel.LeptonDoubletV.matterField_repLorentz, StandardModel.LeptonDoubletV.matterField_repJet, StandardModel.LeptonDoubletV.matterField_repAlgebra, StandardModel.LeptonDoubletV.matterField_massWeight, StandardModel.LeptonDoubletV.matterField_pureJetsActTrivially, StandardModel.LeptonDoubletV.matterField_gaugeLorentzCompatible
statement: formalized
proof: formalized
---

# The Standard Model fermions as matter fields

The module `PhyslibAlpha.Particles.StandardModel.Fermions.MatterField`, [PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean): 40 declarations, 15 with a docstring.

## i. Overview

> `MatterField jets` bundles the value space of one field of a gauge theory over a gauge
> context `jets`, its Lorentz representation, the fibrewise action of the jets of gauge
> transformations on the jets of the field, its mass weight and its declared statistics. The
> five Standard Model fermion types already carry the first four, and this file collects
> them, each declared fermionic. Nothing is redefined and no convention is changed. The
> chirality, the gauge representation, the hypercharge normalization `6Y` and the
> fibrewise-linearity proof are the ones already in the species files.
>
> There is one adapter per fermion type, not per type and generation, since `FermionSpace`
> carries `Fin 3` copies of each type and a matter field describes one multiplet.
>
> Mass weight three is the fermionic weight already fixed by
> `FermionJetAlgebra.massWeightScale`, in the units in which a derivative has weight two.

## ii. Key results

> - `StandardModel.LeptonDoubletV.matterField` : the lepton doublet as a matter field.
> - `StandardModel.LeptonSinglet.matterField` : the charged-lepton singlet as a matter field.
> - `StandardModel.QuarkDoublet.matterField` : the quark doublet as a matter field.
> - `StandardModel.UpSinglet.matterField` : the up-type singlet as a matter field.
> - `StandardModel.DownSinglet.matterField` : the down-type singlet as a matter field.
>
> Each comes with the four projection rules `…matterField_V`, `…matterField_repLorentz`,
> `…matterField_repJet` and `…matterField_massWeight` identifying its fields with the
> existing Standard Model definitions, and with the two conditions
> `…matterField_pureJetsActTrivially` and `…matterField_gaugeLorentzCompatible` consumed by
> the covariant derivative theory, restated from the species files.

## iv. References

> * None.

## A. The lepton sector

### A.1. The lepton doublet

**`StandardModel.LeptonDoubletV.matterField`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L79).

> The lepton doublet as a matter field of `StandardModel.localGaugeData`, in the `(1, 2)_{-3}`
> representation with its left-handed Lorentz action: the matter field the general theory
> derives from the table's datum `StandardModel.Model.leptonDoublet`.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.LeptonDoubletV.matterField_V`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L97).

```lean
lemma matterField_V : matterField.V = LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.matterField_repLorentz`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L100).

```lean
lemma matterField_repLorentz : matterField.repLorentz = repLorentzGroup
```

**`StandardModel.LeptonDoubletV.matterField_repJet`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L103).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.LeptonDoubletV.matterField_repAlgebra`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L106).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.LeptonDoubletV.matterField_massWeight`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L109).

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.LeptonDoubletV.matterField_pureJetsActTrivially`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L112).

> Pure gauge jets act trivially on the lepton doublet at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.LeptonDoubletV.matterField_gaugeLorentzCompatible`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L116).

> The gauge and Lorentz actions on the lepton doublet commute.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

### A.2. The charged-lepton singlet

**`StandardModel.LeptonSinglet.matterField`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L131).

> The charged-lepton singlet as a matter field of `StandardModel.localGaugeData`, in the
> `(1, 1)_{-6}` representation with its right-handed Lorentz action.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.LeptonSinglet.matterField_V`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L142).

```lean
lemma matterField_V : matterField.V = LeptonSinglet
```

**`StandardModel.LeptonSinglet.matterField_repLorentz`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L145).

```lean
lemma matterField_repLorentz : matterField.repLorentz = repLorentzGroup
```

**`StandardModel.LeptonSinglet.matterField_repJet`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L148).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.LeptonSinglet.matterField_repAlgebra`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L151).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.LeptonSinglet.matterField_massWeight`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L154).

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.LeptonSinglet.matterField_pureJetsActTrivially`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L157).

> Pure gauge jets act trivially on the charged-lepton singlet at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.LeptonSinglet.matterField_gaugeLorentzCompatible`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L161).

> The gauge and Lorentz actions on the charged-lepton singlet commute.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

## B. The quark sector

### B.1. The quark doublet

**`StandardModel.QuarkDoublet.matterField`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L178).

> The quark doublet as a matter field of `StandardModel.localGaugeData`, in the `(3, 2)_{1}`
> representation with its left-handed Lorentz action.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.QuarkDoublet.matterField_V`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L189).

```lean
lemma matterField_V : matterField.V = QuarkDoublet
```

**`StandardModel.QuarkDoublet.matterField_repLorentz`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L192).

```lean
lemma matterField_repLorentz : matterField.repLorentz = repLorentzGroup
```

**`StandardModel.QuarkDoublet.matterField_repJet`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L195).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.QuarkDoublet.matterField_repAlgebra`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L198).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.QuarkDoublet.matterField_massWeight`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L201).

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.QuarkDoublet.matterField_pureJetsActTrivially`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L204).

> Pure gauge jets act trivially on the quark doublet at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.QuarkDoublet.matterField_gaugeLorentzCompatible`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L208).

> The gauge and Lorentz actions on the quark doublet commute.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

### B.2. The up-type singlet

**`StandardModel.UpSinglet.matterField`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L223).

> The up-type quark singlet as a matter field of `StandardModel.localGaugeData`, in the
> `(3, 1)_{4}` representation with its right-handed Lorentz action.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.UpSinglet.matterField_V`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L234).

```lean
lemma matterField_V : matterField.V = UpSinglet
```

**`StandardModel.UpSinglet.matterField_repLorentz`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L237).

```lean
lemma matterField_repLorentz : matterField.repLorentz = repLorentzGroup
```

**`StandardModel.UpSinglet.matterField_repJet`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L240).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.UpSinglet.matterField_repAlgebra`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L243).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.UpSinglet.matterField_massWeight`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L246).

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.UpSinglet.matterField_pureJetsActTrivially`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L249).

> Pure gauge jets act trivially on the up-type singlet at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.UpSinglet.matterField_gaugeLorentzCompatible`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L253).

> The gauge and Lorentz actions on the up-type singlet commute.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

### B.3. The down-type singlet

**`StandardModel.DownSinglet.matterField`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L268).

> The down-type quark singlet as a matter field of `StandardModel.localGaugeData`, in the
> `(3, 1)_{-2}` representation with its right-handed Lorentz action.

```lean
noncomputable def matterField : MatterField localGaugeData
```

**`StandardModel.DownSinglet.matterField_V`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L279).

```lean
lemma matterField_V : matterField.V = DownSinglet
```

**`StandardModel.DownSinglet.matterField_repLorentz`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L282).

```lean
lemma matterField_repLorentz : matterField.repLorentz = repLorentzGroup
```

**`StandardModel.DownSinglet.matterField_repJet`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L285).

```lean
lemma matterField_repJet : matterField.repJet = repJetGaugeGroupI
```

**`StandardModel.DownSinglet.matterField_repAlgebra`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L288).

```lean
lemma matterField_repAlgebra : matterField.repAlgebra = gaugeAlgebraAction
```

**`StandardModel.DownSinglet.matterField_massWeight`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L291).

```lean
lemma matterField_massWeight : matterField.massWeight = 3
```

**`StandardModel.DownSinglet.matterField_pureJetsActTrivially`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L294).

> Pure gauge jets act trivially on the down-type singlet at the base point.

```lean
lemma matterField_pureJetsActTrivially : matterField.PureJetsActTrivially
```

**`StandardModel.DownSinglet.matterField_gaugeLorentzCompatible`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean#L298).

> The gauge and Lorentz actions on the down-type singlet commute.

```lean
lemma matterField_gaugeLorentzCompatible : matterField.GaugeLorentzCompatible
```

## Depends on

- [The infinitesimal gauge action on the down-type singlet](fermions-downsinglet-gaugealgebraaction.md)
- [The infinitesimal gauge action on the lepton doublet](fermions-leptondoublet-gaugealgebraaction.md)
- [The gauge-algebra action on the charged-lepton singlet](fermions-leptonsinglet-gaugealgebraaction.md)
- [The infinitesimal gauge action on the quark doublet](fermions-quarkdoublet-gaugealgebraaction.md)
- [The infinitesimal gauge action on the up-type singlet](fermions-upsinglet-gaugealgebraaction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/MatterField.lean)
