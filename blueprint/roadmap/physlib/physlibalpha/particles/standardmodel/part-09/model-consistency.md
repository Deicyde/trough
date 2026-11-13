---
declaration: module
origin: cited
lean: StandardModel.Model.localGaugeData_eq, StandardModel.Model.quarkDoublet_rep_mat
statement: formalized
proof: formalized
---

# Consistency of the Standard Model table with the existing formalisation

The module `PhyslibAlpha.Particles.StandardModel.Model.Consistency`, [PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean): 2 declarations, 2 with a docstring.

## i. Overview

> The Standard Model of `Physlib.Particles.StandardModel.GaugeGroup.Basic` is built from its table
> alone. This file checks it against the hand-built formalisation: the local gauge data
> assembled from the factors is the existing `StandardModel.localGaugeData`, and the quark
> row acts by the existing colour–weak matrix of the quark doublet.
>
>
> - `StandardModel.Model.localGaugeData_eq` : the gauge data of the table is the existing
>   local gauge data of the Standard Model.
> - `StandardModel.Model.quarkDoublet_rep_mat` : the quark doublet reproduces
>   `QuarkDoublet.jetGaugeMatrix`, on the same index type.

## ii. Key results

> - `localGaugeData_eq` : the local gauge data assembled from the factors of the table is the existing
>   local gauge data of the Standard Model
> - `quarkDoublet_rep_mat`

## iv. References

> * None.

## A. Consistency with the existing formalisation

**`StandardModel.Model.localGaugeData_eq`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean#L57).

> The local gauge data assembled from the factors of the table is the existing local
> gauge data of the Standard Model.

```lean
lemma localGaugeData_eq : StandardModel.localGaugeData = gaugeData
```

**`StandardModel.Model.quarkDoublet_rep_mat`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean#L65).

> The quark doublet acts on its colour–weak index by the existing matrix `u · (U₃ ⊗ U₂)`
> of the quark doublet.

```lean
lemma quarkDoublet_rep_mat (U : JetGaugeGroupI) :
    quarkDoublet.rep.mat U = QuarkDoublet.jetGaugeMatrix U
```

## Depends on

- [The type corresponding to quark doublets](../part-03/fermions-quarkdoublet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Model/Consistency.lean)
