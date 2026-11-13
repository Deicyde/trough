---
declaration: module
origin: cited
lean: LocalGaugeData.prod, LocalGaugeData.prod_eval, LocalGaugeData.prod_ofConstant, LocalGaugeData.prod_evalLie, LocalGaugeData.prod_ofConstantLie, LocalGaugeData.prod_deriv, LocalGaugeData.prod_adjointJ, LocalGaugeData.prod_maurerCartan
statement: formalized
proof: formalized
---

# The product of local gauge data

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Prod`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean): 16 declarations, 7 with a docstring.

## i. Overview

> The local gauge data of a product of gauge groups: every structure map acts
> componentwise, and every law holds componentwise. The projections are morphisms of local
> gauge data, so a factor of either side pulls back to the product, and the product of two
> faithful (free) packages
> is faithful (free).

## ii. Key results

> - `LocalGaugeData.prod` : the product of two local gauge data.
> - `LocalGaugeData.Hom.fst`, `LocalGaugeData.Hom.snd` : the projections, as morphisms.
> - `LocalGaugeData.instFaithfulProd` : the product of faithful packages is faithful.
> - `LocalGaugeData.instFreeProd` : the product of free packages is free.

## iv. References

> * None.

## A. The product

**`LocalGaugeData.prod`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L60).

> **The product of two local gauge data**: every structure map acts componentwise.

```lean
noncomputable def prod : LocalGaugeData (G₀₁ × G₀₂) (𝔤₁ × 𝔤₂) (G₁ × G₂) (𝔤J₁ × 𝔤J₂)
```

**`LocalGaugeData.prod_eval`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L94).

```lean
lemma prod_eval (U : G₁ × G₂) : (j₁.prod j₂).eval U = (j₁.eval U.1, j₂.eval U.2)
```

**`LocalGaugeData.prod_ofConstant`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L97).

```lean
lemma prod_ofConstant (g : G₀₁ × G₀₂) :
    (j₁.prod j₂).ofConstant g = (j₁.ofConstant g.1, j₂.ofConstant g.2)
```

**`LocalGaugeData.prod_evalLie`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L101).

```lean
lemma prod_evalLie (a : 𝔤J₁ × 𝔤J₂) : (j₁.prod j₂).evalLie a = (j₁.evalLie a.1, j₂.evalLie a.2)
```

**`LocalGaugeData.prod_ofConstantLie`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L105).

```lean
lemma prod_ofConstantLie (a : 𝔤₁ × 𝔤₂) :
    (j₁.prod j₂).ofConstantLie a = (j₁.ofConstantLie a.1, j₂.ofConstantLie a.2)
```

**`LocalGaugeData.prod_deriv`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L109).

```lean
lemma prod_deriv (μ : Fin 1 ⊕ Fin 3) (a : 𝔤J₁ × 𝔤J₂) :
    (j₁.prod j₂).deriv μ a = (j₁.deriv μ a.1, j₂.deriv μ a.2)
```

**`LocalGaugeData.prod_adjointJ`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L113).

```lean
lemma prod_adjointJ (U : G₁ × G₂) (a : 𝔤J₁ × 𝔤J₂) :
    (j₁.prod j₂).adjointJ U a = (j₁.adjointJ U.1 a.1, j₂.adjointJ U.2 a.2)
```

**`LocalGaugeData.prod_maurerCartan`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L117).

```lean
lemma prod_maurerCartan (U : G₁ × G₂) (μ : Fin 1 ⊕ Fin 3) :
    (j₁.prod j₂).maurerCartan U μ = (j₁.maurerCartan U.1 μ, j₂.maurerCartan U.2 μ)
```

**`LocalGaugeData.prod_iteratedDeriv`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L121).

```lean
lemma prod_iteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J₁ × 𝔤J₂) :
    (j₁.prod j₂).iteratedDeriv s a = (j₁.iteratedDeriv s a.1, j₂.iteratedDeriv s a.2)
```

## B. The projections

> The two projections of a product are morphisms of local gauge data, so a factor of either
> side pulls back to a factor of the product (`Factor.comap`, `Factors.comap`).

**`LocalGaugeData.Hom.fst`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L141).

> The first projection, as a morphism of local gauge data.

```lean
noncomputable def Hom.fst : Hom (j₁.prod j₂) j₁
```

**`LocalGaugeData.Hom.snd`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L156).

> The second projection, as a morphism of local gauge data.

```lean
noncomputable def Hom.snd : Hom (j₁.prod j₂) j₂
```

## C. Faithfulness

**`LocalGaugeData.instFaithfulProd`**, an instance, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L177).

> The product of two faithful packages is faithful.

```lean
instance instFaithfulProd [j₁.Faithful] [j₂.Faithful] : (j₁.prod j₂).Faithful
```

## D. Freeness

**`LocalGaugeData.prod_mulCoord`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L199).

```lean
lemma prod_mulCoord (μ : Fin 1 ⊕ Fin 3) (a : 𝔤J₁ × 𝔤J₂) :
    (j₁.prod j₂).mulCoord μ a = (j₁.mulCoord μ a.1, j₂.mulCoord μ a.2)
```

**`LocalGaugeData.prod_radial`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L205).

> The radial component of the Maurer–Cartan form of a product jet is the pair of the
> radial components of its factors.

```lean
lemma prod_radial (U : G₁ × G₂) :
    (j₁.prod j₂).radial U = (j₁.radial U.1, j₂.radial U.2)
```

**`LocalGaugeData.mem_prod_truncationKer_iff`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L210).

> A product jet lies in the `n`-th truncation kernel exactly when both of its factors do.

```lean
lemma mem_prod_truncationKer_iff (n : ℕ) (U : G₁ × G₂) :
    U ∈ (j₁.prod j₂).truncationKer n ↔
      U.1 ∈ j₁.truncationKer n ∧ U.2 ∈ j₂.truncationKer n
```

**`LocalGaugeData.instFreeProd`**, an instance, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean#L223).

> The product of two free packages is free: Taylor data and radial components are
> realized factor by factor and paired.

```lean
instance instFreeProd [j₁.Free] [j₂.Free] : (j₁.prod j₂).Free
```

## Depends on

- [The truncation filtration of the jet gauge group](localgaugedata-truncation.md)
- [The componentwise representation of a product group](../../../mathematics/part-01/representationprodmap.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Prod.lean)
