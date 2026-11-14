---
declaration: module
origin: cited
lean: Lorentz.lightConeCoeff, Lorentz.lightConeWeight, Lorentz.sum_boostAxis_lightConeCoeff, Lorentz.lightConeCoeffInv, Lorentz.lightConeCoeffInv_two_eq_zero, Lorentz.lightConeCoeffInv_three_eq_zero, Lorentz.sum_lightConeCoeffInv_mul, Lorentz.sum_prod_lightConeCoeff
statement: formalized
proof: formalized
---

# The light-cone basis of an axis

The module `PhyslibAlpha.Relativity.LightConeDeriv`, [PhyslibAlpha/Relativity/LightConeDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean): 9 declarations, 9 with a docstring.

## i. Overview

> A tuple of spacetime directions can be re-read in the light-cone basis along a boost axis:
> `lightConeCoeff` gives the four light-cone directions `D₀ - Dᵢ`, `D₀ + Dᵢ` and the two
> transverse ones, and `lightConeCoeffInv` the inverse change of basis.  The point of the
> change of basis is `sum_boostAxis_lightConeCoeff`: the four directions are eigenvectors of
> the boost along the axis, of weight `lightConeWeight` — `+2` for `D₀ - Dᵢ`, `-2` for
> `D₀ + Dᵢ`, and `0` for the transverse directions.
>
> On a tuple of slots the two coefficient matrices are still inverse to one another
> (`sum_prod_lightConeCoeff`, `sum_prod_lightConeCoeffInv`) and the weights add
> (`sum_prod_lightConeCoeff`).  That is what the classification of the Lorentz invariants in
> `LorentzGroup/Invariants` runs on: it writes a coefficient tensor in this basis and keeps
> only the piece of total weight zero.

## ii. Key results

> - `lightConeCoeff` : the four light-cone directions along the `i`-th axis, written as coefficient
>   vectors on the coordinate directions: `D₀ - Dᵢ`, `D₀ + Dᵢ`, and the two transverse directions
> - `lightConeWeight` : the boost weight carried by each light-cone direction: `+2` for `D₀ - Dᵢ`,
>   `-2` for `D₀ + Dᵢ`, and `0` for the two transverse directions
> - `sum_boostAxis_lightConeCoeff` : the light-cone directions are eigenvectors of the boost
> - `lightConeCoeffInv` : the coordinate directions written back in the light-cone basis: `D₀` and
>   `Dᵢ` are the half-sum and half-difference of `D₀ ∓ Dᵢ`, and the transverse directions are
>   themselves
> - `sum_prod_lightConeCoeff` : the scalar behind `lightConeDeriv_mem`: the boost acts on a light-cone
>   multi-index slot by slot, so the product of the per-slot eigenvalues factors out
> - `sum_prod_lightConeCoeffInv` : the two coefficient matrices are inverse slot by slot, hence
>   inverse on multi-indices; this is `sum_prod_lightConeCoeff` with the two factors the other way
>   round

## iv. References

> * None.

## A. The light-cone basis of an axis

**`Lorentz.lightConeCoeff`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L67).

> The four light-cone directions along the `i`-th axis, written as coefficient vectors on
> the coordinate directions: `D₀ - Dᵢ`, `D₀ + Dᵢ`, and the two transverse directions.

```lean
def lightConeCoeff (i : Fin 3) (κ : Fin 4) (μ : Fin 1 ⊕ Fin 3) : ℂ
```

**`Lorentz.lightConeWeight`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L75).

> The boost weight carried by each light-cone direction: `+2` for `D₀ - Dᵢ`, `-2` for
> `D₀ + Dᵢ`, and `0` for the two transverse directions.

```lean
def lightConeWeight (κ : Fin 4) : ℤ
```

**`Lorentz.sum_boostAxis_lightConeCoeff`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L80).

> **The light-cone directions are eigenvectors of the boost.** Along the `i`-th axis
> `D₀ - Dᵢ` is scaled by `t²`, `D₀ + Dᵢ` by `t⁻²`, and the two transverse directions are
> fixed.

```lean
lemma sum_boostAxis_lightConeCoeff (i : Fin 3) (κ : Fin 4) (ν : Fin 1 ⊕ Fin 3)
    {t : ℝ} (ht : t ≠ 0) :
    ∑ μ : Fin 1 ⊕ Fin 3,
        (((SL2C.toLorentzGroup (SL2C.boostAxis i t ht)).1 ν μ : ℝ) : ℂ) * lightConeCoeff i κ μ
      = ((t : ℝ) : ℂ) ^ (lightConeWeight κ) * lightConeCoeff i κ ν
```

**`Lorentz.lightConeCoeffInv`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L104).

> The coordinate directions written back in the light-cone basis: `D₀` and `Dᵢ` are the
> half-sum and half-difference of `D₀ ∓ Dᵢ`, and the transverse directions are themselves.

```lean
noncomputable def lightConeCoeffInv (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) (κ : Fin 4) : ℂ
```

**`Lorentz.lightConeCoeffInv_two_eq_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L111).

> The inverse coefficient toward the first transverse direction vanishes off it.

```lean
lemma lightConeCoeffInv_two_eq_zero (i : Fin 3) {μ : Fin 1 ⊕ Fin 3}
    (hμ : μ ≠ Sum.inr (i + 1)) : lightConeCoeffInv i μ 2 = 0
```

**`Lorentz.lightConeCoeffInv_three_eq_zero`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L116).

> The inverse coefficient toward the second transverse direction vanishes off it.

```lean
lemma lightConeCoeffInv_three_eq_zero (i : Fin 3) {μ : Fin 1 ⊕ Fin 3}
    (hμ : μ ≠ Sum.inr (i + 2)) : lightConeCoeffInv i μ 3 = 0
```

**`Lorentz.sum_lightConeCoeffInv_mul`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L124).

> The light-cone basis is a basis: the two coefficient matrices are inverse.

```lean
lemma sum_lightConeCoeffInv_mul (i : Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    ∑ κ : Fin 4, lightConeCoeffInv i μ κ * lightConeCoeff i κ ν = if μ = ν then 1 else 0
```

**`Lorentz.sum_prod_lightConeCoeff`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L143).

> The scalar behind `lightConeDeriv_mem`: the boost acts on a light-cone multi-index
> slot by slot, so the product of the per-slot eigenvalues factors out.

```lean
lemma sum_prod_lightConeCoeff (i : Fin 3) {n : ℕ} (c : Fin n → Fin 4)
    (a : Fin n → Fin 1 ⊕ Fin 3) {t : ℝ} (ht : t ≠ 0) :
    ∑ d : Fin n → Fin 1 ⊕ Fin 3, (∏ j, lightConeCoeff i (c j) (d j)) *
        (∏ j, (((SL2C.toLorentzGroup (SL2C.boostAxis i t ht)).1 (a j) (d j) : ℝ) : ℂ))
      = ((t : ℝ) : ℂ) ^ (∑ j, lightConeWeight (c j)) * ∏ j, lightConeCoeff i (c j) (a j)
```

**`Lorentz.sum_prod_lightConeCoeffInv`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean#L174).

> The two coefficient matrices are inverse slot by slot, hence inverse on multi-indices;
> this is `sum_prod_lightConeCoeff` with the two factors the other way round.

```lean
lemma sum_prod_lightConeCoeffInv (i : Fin 3) {n : ℕ} (d e : Fin n → Fin 1 ⊕ Fin 3) :
    ∑ c : Fin n → Fin 4, (∏ j, lightConeCoeffInv i (d j) (c j)) *
        (∏ j, lightConeCoeff i (c j) (e j)) = if d = e then 1 else 0
```

## Depends on

- [Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group](../../physlib/relativity/lorentzgroup/boosts-axis.md)

## Sources

- [PhyslibAlpha/Relativity/LightConeDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LightConeDeriv.lean)
