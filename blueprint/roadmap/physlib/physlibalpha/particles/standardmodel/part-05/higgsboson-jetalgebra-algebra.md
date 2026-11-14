---
declaration: module
origin: cited
lean: StandardModel.HiggsJetAlgebra, StandardModel.HiggsJetAlgebra.ofHiggs, StandardModel.HiggsJetAlgebra.ofConjHiggs, StandardModel.HiggsJetAlgebra.repLorentzGroup, StandardModel.HiggsJetAlgebra.repJetGaugeGroupI, StandardModel.HiggsJetAlgebra.repGaugeGroupI, StandardModel.HiggsJetAlgebra.massWeightScale, StandardModel.HiggsJetAlgebra.massWeightScale_ofHiggs
statement: formalized
proof: formalized
---

# The jet algebra of the Higgs field (Algebra)

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.JetAlgebra.Algebra`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean): 9 declarations, 9 with a docstring.

## i. Overview

> The jet algebra of the Higgs field is the bosonic algebra of the Higgs matter field: the
> symmetric algebra on its component functions `∂_s H_α` and `∂_s H̄_α`, which commute
> because the Higgs is a boson. This file carries the algebra and the actions on it — the
> Lorentz action, the jet and global gauge actions, and the mass-dimension scaling — each
> obtained by applying the generic bosonic-algebra construction to `HiggsVec.matterField`.
>
> The file is separate from
> `PhyslibAlpha.Particles.StandardModel.HiggsBoson.JetAlgebra.Basic`, which builds the gauge
> action on the *jets* of the field, because the matter field is assembled from that action
> and the algebra is then built on the matter field: the three steps are a chain, not a
> single file.

## ii. Key results

> - `StandardModel.HiggsJetAlgebra` : the bosonic algebra of the Higgs matter field.
> - `StandardModel.HiggsJetAlgebra.repLorentzGroup`,
>   `StandardModel.HiggsJetAlgebra.repJetGaugeGroupI`,
>   `StandardModel.HiggsJetAlgebra.repGaugeGroupI` : the actions on it.
> - `StandardModel.HiggsJetAlgebra.massWeightScale` : the mass-dimension scaling.

## iv. References

> * None.

## A. The jet algebra of the Higgs field

**`StandardModel.HiggsJetAlgebra`**, an abbrev, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L61).

> **The jet algebra of the Higgs field**: the bosonic algebra of the `HiggsVec`-valued
> Higgs field. Its generators are the component functions `∂_s H_α` and `∂_s H̄_α`, and
> they commute — the Higgs is a boson.

```lean
abbrev HiggsJetAlgebra : Type
```

### A.1. The component functions

**`StandardModel.HiggsJetAlgebra.ofHiggs`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L76).

> The component functions of the Higgs field inside its jet algebra.

```lean
noncomputable def ofHiggs : Module.Dual ℂ HiggsVec →ₗ[ℂ] HiggsJetAlgebra
```

**`StandardModel.HiggsJetAlgebra.ofConjHiggs`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L80).

> The conjugate component functions of the Higgs field inside its jet algebra.

```lean
noncomputable def ofConjHiggs :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] HiggsJetAlgebra
```

### A.2. The Lorentz action

**`StandardModel.HiggsJetAlgebra.repLorentzGroup`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L94).

> The Lorentz action on the jet algebra of the Higgs field: the Higgs is a Lorentz
> scalar, so the Lorentz group acts on the component functions only through their
> derivative labels.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) HiggsJetAlgebra
```

### A.3. The jet gauge action

**`StandardModel.HiggsJetAlgebra.repJetGaugeGroupI`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L105).

> The jet gauge action on the jet algebra of the Higgs field, lifted from the fibrewise
> action on its jets.

```lean
noncomputable def repJetGaugeGroupI : Representation ℂ JetGaugeGroupI HiggsJetAlgebra
```

**`StandardModel.HiggsJetAlgebra.repGaugeGroupI`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L110).

> The action of the constant — global — gauge transformations on the jet algebra of the
> Higgs field.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI HiggsJetAlgebra
```

### A.4. The mass-dimension scaling

**`StandardModel.HiggsJetAlgebra.massWeightScale`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L121).

> The mass-dimension scaling on the jet algebra of the Higgs field: the Higgs has mass
> dimension one, that is mass weight two, and each derivative adds mass weight two.

```lean
noncomputable def massWeightScale (c : ℂ) : HiggsJetAlgebra →ₐ[ℂ] HiggsJetAlgebra
```

**`StandardModel.HiggsJetAlgebra.massWeightScale_ofHiggs`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L126).

> The Higgs field carries mass weight two — mass dimension one.

```lean
lemma massWeightScale_ofHiggs (c : ℂ) (φ : Module.Dual ℂ HiggsVec) :
    massWeightScale c (ofHiggs φ) = c ^ 2 • ofHiggs φ
```

**`StandardModel.HiggsJetAlgebra.massWeightScale_jetDeriv`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean#L131).

> A derivative of the Higgs field adds mass weight two.

```lean
lemma massWeightScale_jetDeriv (c : ℂ) (μ : Fin 1 ⊕ Fin 3) (x : HiggsJetAlgebra) :
    massWeightScale c (BosonicAlgebra.jetDeriv μ x)
      = c ^ 2 • BosonicAlgebra.jetDeriv μ (massWeightScale c x)
```

## Depends on

- [The Standard Model Higgs field as a matter field](higgsboson-matterfield.md)
- [The gauge action on the bosonic algebra](../part-08/matter-bosonic-gaugeaction.md)
- [The Lorentz action on the bosonic algebra](../part-08/matter-bosonic-lorentzaction.md)
- [Mass dimension on the bosonic algebra](../part-08/matter-bosonic-massdim.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Algebra.lean)
