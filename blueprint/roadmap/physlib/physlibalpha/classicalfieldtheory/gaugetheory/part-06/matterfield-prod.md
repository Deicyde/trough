---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField.prodMapRingHom, GlobalGaugeGroup.MatterField.continuous_prodMapRingHom, GlobalGaugeGroup.MatterField.repProd, GlobalGaugeGroup.MatterField.repProd_apply, GlobalGaugeGroup.MatterField.prod, GlobalGaugeGroup.MatterField.prod_V, GlobalGaugeGroup.MatterField.prod_repLorentz, GlobalGaugeGroup.MatterField.prod_massWeight
statement: formalized
proof: formalized
---

# The direct sum of two matter fields

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Prod`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean): 20 declarations, 12 with a docstring; 2 private, not shown.

> Two matter fields of one mass weight and statistics as a single matter field.

## i. Overview

> Two matter fields of a gauge theory with the same mass weight and the same declared
> statistics combine into one, valued in the product of their value spaces. This is the
> operation that lets a multiplet be described either as one field or as its summands: three
> generations of a fermion type, or the two chiralities of a Dirac field, are the direct sum
> of their pieces.
>
> Every piece of data acts componentwise. The Lorentz representation and the infinitesimal
> gauge action are `LinearMap.prodMap` of the two; the jet gauge action is the pair of the
> two, read through the identification `jetProdEquiv` of the jets of a product with the
> product of the jets. The direct sum is one `MatterField`, with one mass weight and one
> statistic, so it takes as hypotheses that the two fields have the same mass weight and the
> same statistics.
>
> The gauge group acts through `repProd`, a continuous homomorphism into the units of the
> continuous linear maps of the product. The infinitesimal and jet gauge actions of the direct
> sum are derived from it, and what has to be proved is that they are the componentwise ones,
> `prod_repAlgebra` and `prod_repJet`.

## ii. Key results

> - `GlobalGaugeGroup.MatterField.repJetProd` : the jet gauge action of a direct sum.
> - `GlobalGaugeGroup.MatterField.repAlgebraProd` : the infinitesimal gauge action of a direct
>   sum.
> - `GlobalGaugeGroup.MatterField.repCoeff_repJetProd` : its base-point Taylor coefficients are
>   the pair of those of the summands.
> - `GlobalGaugeGroup.MatterField.prod` : the direct sum of two matter fields of the same mass
>   weight and statistics.
> - `FieldDerivSpace.prodEquiv` : the component space of a direct sum splits.

## iv. References

> * None.

## A. The direct sum of two matter fields

> Two matter fields of the same mass weight and statistics combine into one, valued in the
> product of their value spaces. The global gauge group and the Lorentz group act componentwise,
> and the weight and statistics are those of the first summand.

**`GlobalGaugeGroup.MatterField.prodMapRingHom`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L83).

> The pair of continuous linear maps `(f, g)` as the continuous linear map `f × g` of the
> product, a ring homomorphism.

```lean
noncomputable def prodMapRingHom :
    (M.V →L[ℂ] M.V) × (N.V →L[ℂ] N.V) →+* ((M.V × N.V) →L[ℂ] (M.V × N.V))
```

**`GlobalGaugeGroup.MatterField.continuous_prodMapRingHom`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L91).

```lean
lemma continuous_prodMapRingHom : Continuous (prodMapRingHom M N)
```

**`GlobalGaugeGroup.MatterField.repProd`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L95).

> The direct sum `g ↦ ρ_M(g) × ρ_N(g)` of the representations of two matter fields.

```lean
noncomputable def repProd : G.group →ₜ* ((M.V × N.V) →L[ℂ] (M.V × N.V))ˣ
```

**`GlobalGaugeGroup.MatterField.repProd_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L105).

```lean
lemma repProd_apply (g : G.group) :
    ((repProd M N g : ((M.V × N.V) →L[ℂ] (M.V × N.V))ˣ) : (M.V × N.V) →L[ℂ] (M.V × N.V)) =
      ((M.rep g : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V).prodMap
        ((N.rep g : (N.V →L[ℂ] N.V)ˣ) : N.V →L[ℂ] N.V)
```

**`GlobalGaugeGroup.MatterField.prod`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L113).

> The direct sum of two matter fields of the same mass weight and statistics, as one
> field valued in `M.V × N.V`, on which the global gauge group and the Lorentz group act
> componentwise, with the weight and statistics of `M`.

```lean
noncomputable def prod (_h : M.massWeight = N.massWeight) (_hσ : M.statistic = N.statistic) :
    G.MatterField
```

**`GlobalGaugeGroup.MatterField.prod_V`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L124).

```lean
lemma prod_V : (prod M N h hσ).V = (M.V × N.V)
```

**`GlobalGaugeGroup.MatterField.prod_repLorentz`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L127).

```lean
lemma prod_repLorentz : (prod M N h hσ).repLorentz = M.repLorentz.prod N.repLorentz
```

**`GlobalGaugeGroup.MatterField.prod_massWeight`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L130).

```lean
lemma prod_massWeight : (prod M N h hσ).massWeight = M.massWeight
```

**`GlobalGaugeGroup.MatterField.prod_statistic`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L133).

```lean
lemma prod_statistic : (prod M N h hσ).statistic = M.statistic
```

## B. The componentwise gauge actions

> Every other piece of data acts componentwise. The infinitesimal gauge action is
> `LinearMap.prodMap` of the two, and the jet gauge action is read through the identification
> `jetProdEquiv` of the jets of a product with the product of the jets. What has to be checked
> is the last field, that the componentwise algebra action still generates the componentwise
> jet action.

**`GlobalGaugeGroup.MatterField.repJetProd`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L164).

> The jet gauge action of a direct sum, the two actions read through the
> identification of the jets of `M.V × N.V` with the pair of jets.

```lean
noncomputable def repJetProd :
    Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] (M.V × N.V))
```

**`GlobalGaugeGroup.MatterField.repJetProd_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L170).

```lean
lemma repJetProd_apply (U : G.gaugeJetGroup) (z : SpaceTimeAlgebra ⊗[ℂ] (M.V × N.V)) :
    repJetProd M N U z =
      jetProdEquiv.symm (M.repJet U (jetProdEquiv z).1, N.repJet U (jetProdEquiv z).2)
```

**`GlobalGaugeGroup.MatterField.repAlgebraProd`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L175).

> The infinitesimal action of a direct sum, the two actions on the two summands.

```lean
noncomputable def repAlgebraProd : G.lieSubalgebra →ₗ[ℝ] (M.V × N.V) →ₗ[ℂ] (M.V × N.V)
```

**`GlobalGaugeGroup.MatterField.repAlgebraProd_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L183).

```lean
lemma repAlgebraProd_apply (c : G.lieSubalgebra) :
    repAlgebraProd M N c = (M.repAlgebra c).prodMap (N.repAlgebra c)
```

**`GlobalGaugeGroup.MatterField.repCoeff_repJetProd`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L189).

> The base-point Taylor coefficients of the summed jet action are the pair of the
> coefficients of the summands, since `jetOfConstant`, `jetIteratedDeriv` and `jetEval` all act
> componentwise through `jetProdEquiv`.

```lean
lemma repCoeff_repJetProd (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GlobalGaugeGroup.repCoeff (repJetProd M N) U x =
      (GlobalGaugeGroup.repCoeff M.repJet U x).prodMap
        (GlobalGaugeGroup.repCoeff N.repJet U x)
```

**`GlobalGaugeGroup.MatterField.repJetProd_smul`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L203).

> The componentwise jet action is fibrewise.

```lean
lemma repJetProd_smul (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] (M.V × N.V)) : repJetProd M N U (χ • z) = χ • repJetProd M N
      U z
```

**`GlobalGaugeGroup.MatterField.isInfinitesimalActionOf_repAlgebraProd`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L213).

> The componentwise algebra action generates the componentwise jet action. Both laws
> of `IsInfinitesimalActionOf` are the corresponding laws of the summands, read through
> `repCoeff_repJetProd`, since `prodMap` is additive in both slots at once and composes
> componentwise.

```lean
lemma isInfinitesimalActionOf_repAlgebraProd :
    G.IsInfinitesimalActionOf (repAlgebraProd M N) (repJetProd M N)
```

## C. The derived actions of the direct sum

> The Lie algebra action and the jet gauge action that the direct sum inherits from its
> representation are the componentwise ones.

**`GlobalGaugeGroup.MatterField.lieAlgebraRep_prod`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L241).

> The Lie algebra acts on a direct sum componentwise, since the exponential of `dρ_M(X) × dρ_N(X)`
> is the pair of exponentials.

```lean
lemma lieAlgebraRep_prod (X : G.lieSubalgebra) :
    lieAlgebraRep (prod M N h hσ) X = (lieAlgebraRep M X).prodMap (lieAlgebraRep N X)
```

**`GlobalGaugeGroup.MatterField.prod_repAlgebra`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L258).

> The Lie algebra of a direct sum acts componentwise.

```lean
lemma prod_repAlgebra : (prod M N h hσ).repAlgebra = repAlgebraProd M N
```

**`GlobalGaugeGroup.MatterField.prod_repJet`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L266).

> The gauge jets act on a direct sum componentwise, since both actions are generated by the
> componentwise action of the Lie algebra, and agree at the base point.

```lean
lemma prod_repJet : (prod M N h hσ).repJet = repJetProd M N
```

## D. The component space of a direct sum

**`FieldDerivSpace.prodEquiv`**, a def, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L288).

> The component space of a direct sum splits. The component functions of the direct
> sum `M.prod N h hσ` are those of `M` together with those of `N`, since the dual and the conjugate
> both distribute over the finite product, and the derivative label is untouched. Only the
> value spaces enter, so the hypotheses `h` and `hσ` are carried along and not used.

```lean
noncomputable def _root_.FieldDerivSpace.prodEquiv (M N : G.MatterField)
    (h : M.massWeight = N.massWeight) (hσ : M.statistic = N.statistic) :
    FieldDerivSpace (M.prod N h hσ) ≃ₗ[ℂ] FieldDerivSpace M × FieldDerivSpace N
```

## Depends on

- [The field-derivative space of a matter field](matterfield-fieldderivspace-basic.md)
- [The infinitesimal action underlying a matter representation](matterfield-infinitesimalaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean)
