---
declaration: module
origin: cited
lean: GlobalGaugeGroup.IsGaugeJet, GlobalGaugeGroup.inv_mul_mul_mem_jetLieAlgebra, GlobalGaugeGroup.isGaugeJet_inv, GlobalGaugeGroup.mul_mul_inv_mem_jetLieAlgebra, GlobalGaugeGroup.isGaugeJet_mul, GlobalGaugeGroup.isGaugeJet_unitsOfConstant, GlobalGaugeGroup.gaugeJetGroup, GlobalGaugeGroup.mem_gaugeJetGroup
statement: formalized
proof: formalized
---

# The gauge jets of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.GaugeJetGroup`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean): 8 declarations, 7 with a docstring.

> The Taylor series at a point of the gauge transformations.

## i. Overview

> A gauge transformation with global gauge group `G` is a smooth map from spacetime into `G`.
> Its jet at the base point is an invertible matrix of jets `U` with value `U (0)` in `G`.
> Since a map into `GL(κ, ℂ)` starting in `G` stays in `G` exactly when its Maurer–Cartan
> form takes values in the Lie algebra, the gauge jets are the invertible matrices of jets
> with value in `G` and Maurer–Cartan form `(∂_μ U) U⁻¹` a Lie algebra jet.
>
> That the gauge jets form a group rests on conjugation `A ↦ U⁻¹ A U` preserving the Lie
> algebra jets. Its derivative is `U⁻¹ (∂_μ A − [ω_μ, A]) U` with `ω_μ = (∂_μ U) U⁻¹`, again
> of the same form, so every base-point derivative reduces to a value `g⁻¹ a g` with `g ∈ G`
> and `a ∈ 𝔤`.

## ii. Key results

> - `GlobalGaugeGroup.IsGaugeJet` : the condition for an invertible matrix of jets to be a
>   gauge jet.
> - `GlobalGaugeGroup.inv_mul_mul_mem_jetLieAlgebra` : conjugation by a gauge jet preserves
>   the Lie algebra jets.
> - `GlobalGaugeGroup.gaugeJetGroup` : the group of gauge jets.

## iv. References

> * None.

## A. Gauge jets

**`GlobalGaugeGroup.IsGaugeJet`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L63).

> An invertible matrix of jets is a gauge jet when its value lies in the group and its
> Maurer–Cartan form `(∂_μ U) U⁻¹` is a Lie algebra jet.

```lean
def IsGaugeJet (U : GeneralLinearGroup κ SpaceTimeAlgebra) : Prop
```

## B. Conjugation of Lie algebra jets

**`GlobalGaugeGroup.inv_mul_mul_mem_jetLieAlgebra`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L76).

> Conjugation `A ↦ U⁻¹ A U` by a gauge jet preserves the Lie algebra jets. At the base
> point it is the adjoint action of the group, and the derivative of `U⁻¹ A U` is again of
> this form, `U⁻¹ (∂_μ A − [ω_μ, A]) U`.

```lean
lemma inv_mul_mul_mem_jetLieAlgebra {U : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hU : G.IsGaugeJet U) {A : Matrix κ κ SpaceTimeAlgebra} (hA : A ∈ G.jetLieAlgebra) :
    (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra) * A * U ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.isGaugeJet_inv`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L96).

> The inverse of a gauge jet is a gauge jet: its Maurer–Cartan form is
> `−U⁻¹ ((∂_μ U) U⁻¹) U`.

```lean
lemma isGaugeJet_inv {U : GeneralLinearGroup κ SpaceTimeAlgebra} (hU : G.IsGaugeJet U) :
    G.IsGaugeJet U⁻¹
```

**`GlobalGaugeGroup.mul_mul_inv_mem_jetLieAlgebra`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L104).

> Conjugation `A ↦ U A U⁻¹` by a gauge jet preserves the Lie algebra jets.

```lean
lemma mul_mul_inv_mem_jetLieAlgebra {U : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hU : G.IsGaugeJet U) {A : Matrix κ κ SpaceTimeAlgebra} (hA : A ∈ G.jetLieAlgebra) :
    (U : Matrix κ κ SpaceTimeAlgebra) * A * (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra)
      ∈ G.jetLieAlgebra
```

## C. The group of gauge jets

**`GlobalGaugeGroup.isGaugeJet_mul`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L118).

> The product of gauge jets is a gauge jet, by the cocycle law of the Maurer–Cartan form.

```lean
lemma isGaugeJet_mul {U V : GeneralLinearGroup κ SpaceTimeAlgebra} (hU : G.IsGaugeJet U)
    (hV : G.IsGaugeJet V) : G.IsGaugeJet (U * V)
```

**`GlobalGaugeGroup.isGaugeJet_unitsOfConstant`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L125).

> The jet of a constant gauge transformation is a gauge jet.

```lean
lemma isGaugeJet_unitsOfConstant {g : GeneralLinearGroup κ ℂ} (hg : g ∈ G.group) :
    G.IsGaugeJet (unitsOfConstant g)
```

**`GlobalGaugeGroup.gaugeJetGroup`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L135).

> The group of gauge jets: the invertible matrices of jets with value in the group and
> Maurer–Cartan form a Lie algebra jet. These are the Taylor series of smooth maps from
> spacetime into the group, the analogue of `JetSU` and `JetU1`, and not the jet group of
> diffeomorphisms of differential geometry.

```lean
def gaugeJetGroup : Subgroup (GeneralLinearGroup κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_gaugeJetGroup`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L142).

```lean
lemma mem_gaugeJetGroup {U : GeneralLinearGroup κ SpaceTimeAlgebra} :
    U ∈ G.gaugeJetGroup ↔ G.IsGaugeJet U
```

## Depends on

- [The Lie algebra jets of a global gauge group](globalgaugegroup-jetliealgebra.md)
- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean)
