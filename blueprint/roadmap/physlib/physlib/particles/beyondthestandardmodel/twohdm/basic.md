---
declaration: module
origin: cited
lean: TwoHiggsDoublet, TwoHiggsDoublet.ext_of_fst_snd, TwoHiggsDoublet.gaugeGroupI_smul_fst, TwoHiggsDoublet.gaugeGroupI_smul_snd
statement: formalized
proof: formalized
---

# The Two Higgs Doublet Model

The module `Physlib.Particles.BeyondTheStandardModel.TwoHDM.Basic`, [Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean): 6 declarations (2 instances with no name), 1 with a docstring.

> The two Higgs doublet model is the standard model plus an additional Higgs doublet.

## i. Overview

> The two Higgs doublet model (2HDM) is an extension of the Standard Model which adds a second Higgs
> doublet.

## References

> * https://arxiv.org/abs/hep-ph/0605184. [ref: arxiv\_hep\_ph\_0605184]
> * https://arxiv.org/abs/1605.03237. [ref: arxiv\_1605\_03237]

## A. The configuration space

**`TwoHiggsDoublet`**, a structure, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L38).

> The configuration space of the two Higgs doublet model.
> In otherwords, the underlying vector space associated with the model.

```lean
structure TwoHiggsDoublet where
  /-- The first Higgs doublet. -/
  Φ1 : HiggsVec
  /-- The second Higgs doublet. -/
  Φ2 : HiggsVec
```

**`TwoHiggsDoublet.ext_of_fst_snd`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L49).

```lean
lemma ext_of_fst_snd {H1 H2 : TwoHiggsDoublet}
    (h1 : H1.Φ1 = H2.Φ1) (h2 : H1.Φ2 = H2.Φ2) : H1 = H2
```

## B. Gauge group actions

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L59).

```lean
noncomputable instance : SMul StandardModel.GaugeGroupI TwoHiggsDoublet
```

**`TwoHiggsDoublet.gaugeGroupI_smul_fst`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L65).

```lean
lemma gaugeGroupI_smul_fst (g : StandardModel.GaugeGroupI) (H : TwoHiggsDoublet) :
    (g • H).Φ1 = StandardModel.HiggsVec.repGaugeGroupI g H.Φ1
```

**`TwoHiggsDoublet.gaugeGroupI_smul_snd`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L69).

```lean
lemma gaugeGroupI_smul_snd (g : StandardModel.GaugeGroupI) (H : TwoHiggsDoublet) :
    (g • H).Φ2 = StandardModel.HiggsVec.repGaugeGroupI g H.Φ2
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean#L72).

```lean
noncomputable instance : MulAction StandardModel.GaugeGroupI TwoHiggsDoublet
```

## Depends on

- [The Higgs field](../../standardmodel/higgsboson/basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Basic.lean)
