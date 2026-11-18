---
declaration: module
origin: cited
lean: MatterField.repJetProd, MatterField.repJetProd_apply, MatterField.repAlgebraProd, MatterField.repAlgebraProd_apply, MatterField.repCoeff_repJetProd, MatterField.isInfinitesimalActionOf_repAlgebraProd, MatterField.prod, MatterField.prod_V
statement: formalized
proof: formalized
---

# The direct sum of two matter fields

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Prod`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean): 15 declarations, 7 with a docstring; 2 private, not shown.

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
> What has to be proved is the last field of the structure — that the componentwise
> infinitesimal action still generates the componentwise jet action.

## ii. Key results

> - `MatterField.repJetProd` : the jet gauge action of a direct sum.
> - `MatterField.repAlgebraProd` : the infinitesimal gauge action of a direct sum.
> - `MatterField.repCoeff_repJetProd` : its base-point Taylor coefficients are the pair of
>   those of the summands.
> - `MatterField.prod` : the direct sum of two matter fields of the same mass weight and
>   statistics.
> - `JetComponentSpace.prodEquiv` : the component space of a direct sum splits.

## iv. References

> * None.

## A. The direct sum of two matter fields

> Two matter fields of the same mass weight combine into one, valued in the product of their
> value spaces. Every piece of data acts componentwise: the Lorentz and gauge algebra
> actions by `LinearMap.prodMap`, and the jet gauge action through the identification
> `jetProdEquiv` of the jets of a product with the product of the jets. What has to be
> checked is the last field — that the componentwise algebra action still generates the
> componentwise jet action.

**`MatterField.repJetProd`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L95).

> **The jet gauge action of a direct sum**: the two actions, read through the
> identification of the jets of `M.V × N.V` with the pair of jets.

```lean
noncomputable def repJetProd :
    Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] (M.V × N.V))
```

**`MatterField.repJetProd_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L101).

```lean
lemma repJetProd_apply (U : GJ) (z : SpaceTimeAlgebra ⊗[ℂ] (M.V × N.V)) :
    repJetProd M N U z =
      jetProdEquiv.symm (M.repJet U (jetProdEquiv z).1, N.repJet U (jetProdEquiv z).2)
```

**`MatterField.repAlgebraProd`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L106).

> **The infinitesimal action of a direct sum**: the two actions on the two summands.

```lean
noncomputable def repAlgebraProd : 𝔤 →ₗ[ℝ] (M.V × N.V) →ₗ[ℂ] (M.V × N.V)
```

**`MatterField.repAlgebraProd_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L114).

```lean
lemma repAlgebraProd_apply (c : 𝔤) :
    repAlgebraProd M N c = (M.repAlgebra c).prodMap (N.repAlgebra c)
```

**`MatterField.repCoeff_repJetProd`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L120).

> The base-point Taylor coefficients of the summed jet action are the pair of the
> coefficients of the summands: `jetOfConstant`, `jetIteratedDeriv` and `jetEval` all act
> componentwise through `jetProdEquiv`.

```lean
lemma repCoeff_repJetProd (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff (repJetProd M N) U x =
      (GaugeAlgebraRealization.repCoeff M.repJet U x).prodMap
        (GaugeAlgebraRealization.repCoeff N.repJet U x)
```

**`MatterField.isInfinitesimalActionOf_repAlgebraProd`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L137).

> **The componentwise algebra action generates the componentwise jet action**: both laws
> of `IsInfinitesimalActionOf` are the corresponding laws of the summands, read through
> `repCoeff_repJetProd`, since `prodMap` is additive in both slots at once and composes
> componentwise.

```lean
lemma isInfinitesimalActionOf_repAlgebraProd :
    jets.IsInfinitesimalActionOf (repAlgebraProd M N) (repJetProd M N)
```

**`MatterField.prod`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L157).

> **The direct sum of two matter fields** of the same mass weight and statistics, one field
> valued in `M.V × N.V` with every action acting componentwise and with the weight and
> statistics of `M`.

```lean
noncomputable def prod (_h : M.massWeight = N.massWeight) (_hσ : M.statistic = N.statistic) :
    MatterField jets
```

**`MatterField.prod_V`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L173).

```lean
lemma prod_V : (prod M N h hσ).V = (M.V × N.V)
```

**`MatterField.prod_repJet`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L176).

```lean
lemma prod_repJet : (prod M N h hσ).repJet = repJetProd M N
```

**`MatterField.prod_repAlgebra`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L179).

```lean
lemma prod_repAlgebra : (prod M N h hσ).repAlgebra = repAlgebraProd M N
```

**`MatterField.prod_repLorentz`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L182).

```lean
lemma prod_repLorentz : (prod M N h hσ).repLorentz = M.repLorentz.prod N.repLorentz
```

**`MatterField.prod_massWeight`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L185).

```lean
lemma prod_massWeight : (prod M N h hσ).massWeight = M.massWeight
```

**`MatterField.prod_massWeight_right`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L189).

> The shared weight, read off the second summand: this is what the hypothesis of `prod`
> buys — the direct sum has one weight, and it is the weight of either summand.

```lean
lemma prod_massWeight_right : (prod M N h hσ).massWeight = N.massWeight
```

**`MatterField.prod_statistic`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L192).

```lean
lemma prod_statistic : (prod M N h hσ).statistic = M.statistic
```

## B. The component space of a direct sum

**`JetComponentSpace.prodEquiv`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean#L206).

> **The component space of a direct sum splits.** The component functions of the direct
> sum `M.prod N h hσ` are those of `M` together with those of `N`: the dual and the conjugate
> both distribute over the finite product, and the derivative label is untouched. Only the
> value spaces enter, so the hypotheses `h` and `hσ` are carried along and not used.

```lean
noncomputable def _root_.JetComponentSpace.prodEquiv (M N : MatterField jets)
    (h : M.massWeight = N.massWeight) (hσ : M.statistic = N.statistic) :
    JetComponentSpace (M.prod N h hσ) ≃ₗ[ℂ] JetComponentSpace M × JetComponentSpace N
```

## Depends on

- [The jet component space of a matter field](matterfield-jetcomponent-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Prod.lean)
