---
declaration: module
origin: cited
lean: GlobalGaugeGroup.gaugeJetGroup, GlobalGaugeGroup.mem_gaugeJetGroup, GlobalGaugeGroup.evalGaugeJet, GlobalGaugeGroup.evalGaugeJet_val, GlobalGaugeGroup.unitsOfConstant_mem_gaugeJetGroup, GlobalGaugeGroup.gaugeJetOfConstant, GlobalGaugeGroup.gaugeJetOfConstant_val, GlobalGaugeGroup.evalGaugeJet_gaugeJetOfConstant
statement: formalized
proof: formalized
---

# The jet gauge group of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.GaugeJetGroup`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean): 10 declarations (1 instance with no name), 7 with a docstring.

> The Taylor series at a point of the gauge transformations.

## i. Overview

> A gauge transformation with global gauge group `G` is a smooth map from spacetime into `G`.
> Its jet at the base point is an invertible matrix of jets `U` with value `U (0)` in `G`.
> A map into `GL(κ, ℂ)` starting in `G` stays in `G` exactly when `(∂_μ U) U⁻¹` takes values
> in the Lie algebra. The jet gauge group is therefore made of the invertible matrices of jets
> with value in `G` and `(∂_μ U) U⁻¹` a Lie algebra jet. On the jet gauge group this is the
> Maurer–Cartan form, of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.MaurerCartan`.
>
> That these form a group rests on conjugation by `U` preserving the Lie algebra jets, from
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Jet`,
> together with the Leibniz rule for `(∂_μ (U V)) (U V)⁻¹` and `(∂_μ U⁻¹) U`. Evaluation at
> the base point is a homomorphism onto `G`, split by the constant gauge transformations.

## ii. Key results

> - `GlobalGaugeGroup.gaugeJetGroup` : the jet gauge group.
> - `GlobalGaugeGroup.evalGaugeJet` : evaluation of a gauge jet at the base point.
> - `GlobalGaugeGroup.gaugeJetOfConstant` : the jet of a constant gauge transformation.
> - `GlobalGaugeGroup.adjoint_mem_jetLieAlgebra` : the jet gauge group acts by conjugation on
>   the Lie algebra jets.

## iv. References

> * None.

## A. The jet gauge group

**`GlobalGaugeGroup.gaugeJetGroup`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L67).

> The jet gauge group, the invertible matrices of jets `U` with value in the group and
> `(∂_μ U) U⁻¹` a Lie algebra jet. These are the Taylor series at a point of smooth maps from
> spacetime into the group, the gauge transformations seen to all orders. This is not the jet
> group of diffeomorphisms of differential geometry.

```lean
def gaugeJetGroup : Subgroup (GeneralLinearGroup κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_gaugeJetGroup`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L81).

```lean
lemma mem_gaugeJetGroup {U : GeneralLinearGroup κ SpaceTimeAlgebra} :
    U ∈ G.gaugeJetGroup ↔ unitsEval U ∈ G.group ∧ ∀ μ,
      (U : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) * (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra)
        ∈ G.jetLieAlgebra
```

## B. Evaluation and constant gauge jets

**`GlobalGaugeGroup.evalGaugeJet`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L94).

> The value of a gauge jet at the base point, as a homomorphism to the group.

```lean
noncomputable def evalGaugeJet : G.gaugeJetGroup →* G.group
```

**`GlobalGaugeGroup.evalGaugeJet_val`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L100).

```lean
lemma evalGaugeJet_val (U : G.gaugeJetGroup) :
    ((G.evalGaugeJet U).1 : Matrix κ κ ℂ) =
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U.1
```

**`GlobalGaugeGroup.unitsOfConstant_mem_gaugeJetGroup`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L105).

> The jet of a constant gauge transformation is a gauge jet.

```lean
lemma unitsOfConstant_mem_gaugeJetGroup {g : GeneralLinearGroup κ ℂ} (hg : g ∈ G.group) :
    unitsOfConstant g ∈ G.gaugeJetGroup
```

**`GlobalGaugeGroup.gaugeJetOfConstant`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L112).

> The jet of a constant gauge transformation, as a homomorphism from the group.

```lean
noncomputable def gaugeJetOfConstant : G.group →* G.gaugeJetGroup
```

**`GlobalGaugeGroup.gaugeJetOfConstant_val`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L118).

```lean
lemma gaugeJetOfConstant_val (g : G.group) :
    ((G.gaugeJetOfConstant g).1 : Matrix κ κ SpaceTimeAlgebra) =
      (C : ℂ →+* SpaceTimeAlgebra).mapMatrix g.1
```

**`GlobalGaugeGroup.evalGaugeJet_gaugeJetOfConstant`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L124).

> A constant gauge jet has the constant as its value.

```lean
lemma evalGaugeJet_gaugeJetOfConstant (g : G.group) :
    G.evalGaugeJet (G.gaugeJetOfConstant g) = g
```

## C. The adjoint action on the Lie algebra jets

**`GlobalGaugeGroup.adjoint_mem_jetLieAlgebra`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L135).

> Conjugation `A ↦ U A U⁻¹` by a gauge jet preserves the Lie algebra jets.

```lean
lemma adjoint_mem_jetLieAlgebra (U : G.gaugeJetGroup) {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) :
    (U.1 : Matrix κ κ SpaceTimeAlgebra) * A * (↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra)
      ∈ G.jetLieAlgebra
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean#L143).

> The group structure of the gauge jets, recorded directly so that instance search does not
> pass through the units of the matrices of jets.

```lean
noncomputable instance : Group G.gaugeJetGroup
```

## Depends on

- [The Lie algebra jets of a global gauge group](../part-03/globalgaugegroup-liealgebra-jet.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/GaugeJetGroup.lean)
