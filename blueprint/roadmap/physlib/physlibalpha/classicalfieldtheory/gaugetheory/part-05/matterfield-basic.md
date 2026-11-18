---
declaration: module
origin: cited
lean: MatterField, MatterField.PureJetsActTrivially, MatterField.GaugeLorentzCompatible
statement: formalized
proof: formalized
---

# Matter fields of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean): 3 declarations, 3 with a docstring.

## i. Overview

> A matter field of a gauge theory is specified by the data a physicist writes down: a
> finite-dimensional complex vector space `V` in which the field takes its values, the
> representation of the Lorentz group on `V`, the action of the jets of gauge
> transformations on the jets of the field — which must be *fibrewise*, that is act on the
> values of the field over the identity of spacetime — the mass weight of the field, and the
> statistics, bosonic or fermionic, that the field is declared to obey. All of this is
> relative to a gauge context `jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J`: the jet gauge group
> `GJ` the field's jet action is a representation of, and the global group `G₀`, Lie
> algebras `𝔤`, `𝔤J` and structure maps that make `GJ` the jets of `G₀` rather than an
> unrelated group. Fixing `jets` rather than `GJ` alone is what lets the global gauge action
> `repConstant` below be taken along the *canonical* inclusion `jets.ofConstant`, instead of
> an arbitrary homomorphism supplied by hand.
>
> `MatterField jets` bundles this data. The statistics is declared once, where the field is
> defined, and separately from the Lorentz representation. `GaugeFieldData` requires the
> declaration of each matter field it includes to agree with the collection, fermionic or
> bosonic, to which that field is assigned. From the other data the general theory produces,
> on the bosonic and fermionic algebras of the field, the jet gauge action, the global gauge
> action, the Lorentz action and the mass-weight scaling, in
> `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.Basic`,
> `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.Basic` and the files beside them.

## ii. Key results

> - `MatterField` : the data of a matter field.
> - `MatterField.PureJetsActTrivially`, `MatterField.GaugeLorentzCompatible` : two conditions
>   on a matter field used by the covariant derivative theory.

## iv. References

> * None.

## A. The data of a matter field

**`MatterField`**, a structure, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean#L70).

> **A matter field** of a gauge theory over the gauge context `jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J`:
> a finite-dimensional complex target space `V`, the Lorentz representation on `V`, a
> fibrewise action of `GJ` on the jets `SpaceTimeAlgebra ⊗[ℂ] V` of the field, the infinitesimal
> action of the gauge algebra generating it, the mass weight of the field (in the units
> in which a derivative has weight `2`), and its declared statistics.

```lean
structure MatterField {G₀ : Type} [Group G₀] {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {GJ : Type} [Group GJ] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) where
  /-- The target space of the field. -/
  V : Type
  [instAddCommGroup : AddCommGroup V]
  [instModule : Module ℂ V]
  [instFree : Module.Free ℂ V]
  [instFinite : Module.Finite ℂ V]
  /-- The representation of the Lorentz group on the target space. -/
  repLorentz : Representation ℂ SL(2,ℂ) V
  /-- The action of the jets of gauge transformations on the jets of the field. -/
  repJet : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V)
  /-- The action of the gauge algebra. -/
  repAlgebra : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V
  /-- The gauge action is fibrewise: it commutes with multiplication by scalar jets. -/
  repJet_smul : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), repJet U (χ • z) =
      χ • repJet U z
  /-- The action of the gauge algebra generates the action of the jets of gauge
    transformations: it is the infinitesimal action underlying `repJet`, the physicists'
    `i dρ(T^a)`. This is what makes the covariant derivative of the field transform
    covariantly. -/
  repAlgebra_isInfinitesimalAction : jets.IsInfinitesimalActionOf repAlgebra repJet
  /-- The mass weight of the field. -/
  massWeight : ℕ
  /-- The statistics the field is declared to obey, bosonic or fermionic. `GaugeFieldData`
    requires it to agree with the collection the field is assigned to; the single-field
    algebras `StandardModel.FermionicAlgebra M` and `StandardModel.BosonicAlgebra M` are
    defined for every `M`, whatever its declared statistics. -/
  statistic : FieldStatistic
```

## B. Conditions on a matter field

> Two properties the data of a matter field does not in general imply: the transformation
> laws constrain the base-point coefficient of a pure jet only to commute with the
> infinitesimal action (a scalar twist by a character of the jet group nontrivial on pure
> jets preserves every field of the structure), and they do not relate the gauge and Lorentz
> actions at all. Both hold for the matter fields of the physical theories, and they are
> recorded as conditions rather than as fields, to be assumed where the covariant derivative
> theory needs them: the first for the factorization of the jet action through evaluation,
> the second for the Lorentz law of the covariant derivatives.

**`MatterField.PureJetsActTrivially`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean#L128).

> Pure gauge jets act trivially at the base point: a jet with trivial value has identity
> zeroth Taylor coefficient on the value space. With the fibrewise law, the base-point
> value of the jet action is then a function of the value of the jet.

```lean
def PureJetsActTrivially : Prop
```

**`MatterField.GaugeLorentzCompatible`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean#L133).

> The infinitesimal gauge action commutes with the Lorentz representation on the value
> space.

```lean
def GaugeLorentzCompatible : Prop
```

## Depends on

- [Field statistics](../../../../physlib/qft/perturbationtheory/part-01/fieldstatistics-basic.md)
- [The infinitesimal action underlying a matter representation](matterfield-infinitesimalaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean)
