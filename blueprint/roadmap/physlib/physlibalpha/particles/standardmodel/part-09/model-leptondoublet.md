---
declaration: module
origin: cited
lean: StandardModel.Model.leptonDoublet_toMatterField_eq
statement: formalized
proof: formalized
---

# The lepton doublet of the Standard Model table

The module `PhyslibAlpha.Particles.StandardModel.Model.LeptonDoublet`, [PhyslibAlpha/Particles/StandardModel/Model/LeptonDoublet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/LeptonDoublet.lean): 1 declaration, 1 with a docstring.

## i. Overview

> The lepton doublet of the Standard Model is the datum `StandardModel.Model.leptonDoublet`,
> `(.L, .singlet, .fund, -3)`, of `Physlib.Particles.StandardModel.GaugeGroup.Basic`. The species
> `StandardModel.LeptonDoubletV` is its target space, and the species' weak matrix, action
> matrix, Lorentz, global gauge, jet and gauge-algebra actions and matter field are the ones
> the general theory derives from the datum. This file records the identities, all of which
> hold by definition.
>
>
> - `StandardModel.Model.leptonDoublet_toMatterField_eq` : the matter field of the datum is
>   `LeptonDoubletV.matterField`.

## ii. Key results

> - `leptonDoublet_toMatterField_eq` : the matter field of the datum is the matter field of the
>   species: the table's description and the species' description of the lepton doublet are one
>   definition

## iv. References

> * None.

## A. The lepton doublet of the table

**`StandardModel.Model.leptonDoublet_toMatterField_eq`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/LeptonDoublet.lean#L72).

> **The matter field of the datum is the matter field of the species**: the table's
> description and the species' description of the lepton doublet are one definition.

```lean
lemma leptonDoublet_toMatterField_eq :
    leptonDoublet.toMatterField = LeptonDoubletV.matterField
```

## Depends on

- [The Standard Model fermions as matter fields](../part-03/fermions-matterfield.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Model/LeptonDoublet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/LeptonDoublet.lean)
