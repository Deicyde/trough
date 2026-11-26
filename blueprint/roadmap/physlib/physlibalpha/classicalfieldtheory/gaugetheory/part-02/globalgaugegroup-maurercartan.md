---
declaration: module
origin: cited
lean: GlobalGaugeGroup.maurerCartan, GlobalGaugeGroup.maurerCartan_val, GlobalGaugeGroup.map_pderiv_eq_maurerCartan_mul, GlobalGaugeGroup.maurerCartan_gaugeJetOfConstant, GlobalGaugeGroup.maurerCartan_one, GlobalGaugeGroup.maurerCartan_mul, GlobalGaugeGroup.maurerCartan_inv, GlobalGaugeGroup.map_pderiv_maurerCartan_sub
statement: formalized
proof: formalized
---

# The Maurer–Cartan form on the jet gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.MaurerCartan`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean): 12 declarations, 10 with a docstring.

> The Lie algebra jet `(∂_μ U) U⁻¹` of a gauge jet `U`, and its transformation laws.

## i. Overview

> Let `G` be a global gauge group. A gauge jet `U`, an element of the jet gauge group, is the
> Taylor series at a point of a smooth map from spacetime into `G`. Its Maurer–Cartan form is
> `ω_μ = (∂_μ U) U⁻¹`, the pull-back of the right-invariant Maurer–Cartan form of `G`. By the
> definition of the jet gauge group it is a Lie algebra jet.
>
> The Maurer–Cartan form vanishes on constant gauge jets. It obeys the cocycle law
> `ω(U V) = ω(U) + U ω(V) U⁻¹` and the inversion law `ω(U⁻¹) = −U⁻¹ ω(U) U`. It also governs
> how conjugation by `U` interacts with derivatives. For a matrix of jets `A`,
> `∂_μ (U⁻¹ A U) = U⁻¹ (∂_μ A − [ω_μ, A]) U`.
>
> A gauge jet with vanishing Maurer–Cartan form has vanishing derivatives, so it is the
> constant jet of its value. Conversely every Lie algebra jet `A` vanishing at the base point
> is the radial component `∑_μ x_μ ω_μ = −A` of the Maurer–Cartan form of a gauge jet. The jet
> is the solution `V` of the radial system `E V = −A V` with `V(0) = 1`, where
> `E = ∑_μ x_μ ∂_μ`. Its Maurer–Cartan form solves the linear radial system
> `E ω_μ + ω_μ = −∂_μ A − A ω_μ + ω_μ A`, so it is a Lie algebra jet. This is the formal version
> of integrating the infinitesimal gauge transformation `A` along rays from the base point.

## ii. Key results

> - `GlobalGaugeGroup.maurerCartan` : the Maurer–Cartan form of a gauge jet.
> - `GlobalGaugeGroup.map_pderiv_eq_maurerCartan_mul` : the derivative `∂_μ U = ω_μ U` of a gauge
>   jet.
> - `GlobalGaugeGroup.maurerCartan_mul` : the cocycle law.
> - `GlobalGaugeGroup.maurerCartan_inv` : the inversion law.
> - `GlobalGaugeGroup.map_pderiv_maurerCartan_sub` : the structure equation
>   `∂_μ ω_ν − ∂_ν ω_μ = [ω_μ, ω_ν]`.
> - `GlobalGaugeGroup.map_pderiv_inv_mul_mul` : the derivative of a conjugate.
> - `GlobalGaugeGroup.eq_gaugeJetOfConstant_of_maurerCartan_eq_zero` : a gauge jet with vanishing
>   Maurer–Cartan form is constant.
> - `GlobalGaugeGroup.exists_sum_X_smul_maurerCartan_eq` : every Lie algebra jet vanishing at
>   the base point is the radial component of the Maurer–Cartan form of a gauge jet.

## iv. References

> * None.

## A. The Maurer–Cartan form

**`GlobalGaugeGroup.maurerCartan`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L80).

> The Maurer–Cartan form `(∂_μ U) U⁻¹` of a gauge jet `U` in the spacetime direction `μ`,
> a Lie algebra jet.

```lean
noncomputable def maurerCartan (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    G.jetLieSubalgebra
```

**`GlobalGaugeGroup.maurerCartan_val`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L86).

```lean
lemma maurerCartan_val (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    (G.maurerCartan U μ : Matrix κ κ SpaceTimeAlgebra) =
      (U.1 : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) *
        (↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.map_pderiv_eq_maurerCartan_mul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L92).

> The derivative of a gauge jet in terms of its Maurer–Cartan form, `∂_ρ U = ω_ρ(U) U`.

```lean
lemma map_pderiv_eq_maurerCartan_mul (U : G.gaugeJetGroup) (ρ : Fin 1 ⊕ Fin 3) :
    (U.1 : Matrix κ κ SpaceTimeAlgebra).map (pderiv ρ) =
      (G.maurerCartan U ρ : Matrix κ κ SpaceTimeAlgebra) * U.1
```

## B. Constant gauge jets

**`GlobalGaugeGroup.maurerCartan_gaugeJetOfConstant`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L105).

> A constant gauge jet has vanishing Maurer–Cartan form.

```lean
lemma maurerCartan_gaugeJetOfConstant (g : G.group) (μ : Fin 1 ⊕ Fin 3) :
    G.maurerCartan (G.gaugeJetOfConstant g) μ = 0
```

**`GlobalGaugeGroup.maurerCartan_one`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L112).

```lean
lemma maurerCartan_one (μ : Fin 1 ⊕ Fin 3) : G.maurerCartan 1 μ = 0
```

## C. The cocycle and inversion laws and the structure equation

**`GlobalGaugeGroup.maurerCartan_mul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L123).

> The cocycle law `ω(U V) = ω(U) + U ω(V) U⁻¹` of the Maurer–Cartan form `ω` on the
> product of two gauge jets `U` and `V`.

```lean
lemma maurerCartan_mul (U V : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    (G.maurerCartan (U * V) μ : Matrix κ κ SpaceTimeAlgebra) =
      G.maurerCartan U μ + (U.1 : Matrix κ κ SpaceTimeAlgebra) *
        G.maurerCartan V μ * (↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.maurerCartan_inv`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L132).

> The inversion law `ω(U⁻¹) = −U⁻¹ ω(U) U` of the Maurer–Cartan form `ω` on the inverse
> of a gauge jet `U`.

```lean
lemma maurerCartan_inv (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    (G.maurerCartan U⁻¹ μ : Matrix κ κ SpaceTimeAlgebra) =
      -((↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra) * G.maurerCartan U μ * U.1)
```

**`GlobalGaugeGroup.map_pderiv_maurerCartan_sub`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L141).

> The Maurer–Cartan structure equation `∂_μ ω_ν − ∂_ν ω_μ = [ω_μ, ω_ν]` for the
> Maurer–Cartan form `ω` of a gauge jet. The curl of `ω` is its commutator.

```lean
lemma map_pderiv_maurerCartan_sub (U : G.gaugeJetGroup) (μ ν : Fin 1 ⊕ Fin 3) :
    (G.maurerCartan U ν : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) -
        (G.maurerCartan U μ : Matrix κ κ SpaceTimeAlgebra).map (pderiv ν) =
      (G.maurerCartan U μ : Matrix κ κ SpaceTimeAlgebra) * G.maurerCartan U ν -
        (G.maurerCartan U ν : Matrix κ κ SpaceTimeAlgebra) * G.maurerCartan U μ
```

## D. The derivative of a conjugate

**`GlobalGaugeGroup.map_pderiv_inv_mul_mul`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L166).

> The derivative of the conjugate `U⁻¹ A U` of a matrix of jets by a gauge jet, in terms of
> the Maurer–Cartan form `ω_μ` of `U`, `∂_μ (U⁻¹ A U) = U⁻¹ (∂_μ A − [ω_μ, A]) U`.

```lean
lemma map_pderiv_inv_mul_mul (U : G.gaugeJetGroup) (A : Matrix κ κ SpaceTimeAlgebra)
    (μ : Fin 1 ⊕ Fin 3) :
    ((↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra) * A * U.1).map (pderiv μ) =
      (↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra) * (A.map (pderiv μ) -
        ((G.maurerCartan U μ : Matrix κ κ SpaceTimeAlgebra) * A -
          A * G.maurerCartan U μ)) * U.1
```

## E. Gauge jets with vanishing Maurer–Cartan form

**`GlobalGaugeGroup.eq_gaugeJetOfConstant_of_maurerCartan_eq_zero`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L182).

> A gauge jet with vanishing Maurer–Cartan form is the constant gauge jet of its value, since
> its derivatives `∂_μ U = ω_μ U` vanish.

```lean
lemma eq_gaugeJetOfConstant_of_maurerCartan_eq_zero {U : G.gaugeJetGroup}
    (h : ∀ μ, G.maurerCartan U μ = 0) : U = G.gaugeJetOfConstant (G.evalGaugeJet U)
```

## F. Integrating a Lie algebra jet radially

**`GlobalGaugeGroup.mem_gaugeJetGroup_of_eulerTransport`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L205).

> Radially integrating a Lie algebra jet gives a gauge jet. An invertible matrix of jets with
> value one at the base point which solves the radial system `E V = −A V`, for a Lie algebra
> jet `A` vanishing at the base point, is a gauge jet. Here `E` is the Euler operator, which
> multiplies the part of each degree by that degree.

```lean
lemma mem_gaugeJetGroup_of_eulerTransport {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (hA0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A = 0)
    {V : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hV0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (V : Matrix κ κ SpaceTimeAlgebra) = 1)
    (hEV : ∑ μ, (X μ : SpaceTimeAlgebra) • (V : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) =
      -A * V) :
    V ∈ G.gaugeJetGroup
```

**`GlobalGaugeGroup.exists_sum_X_smul_maurerCartan_eq`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean#L224).

> Every Lie algebra jet vanishing at the base point is, up to sign, the radial component of
> the Maurer–Cartan form of a gauge jet with value one. In symbols, `∑_μ x_μ (∂_μ U) U⁻¹ = −A`
> for the Lie algebra jet `A`. The gauge jet is the solution `U` of the radial system
> `E U = −A U` with `U(0) = 1`, where `E` is the Euler operator.

```lean
lemma exists_sum_X_smul_maurerCartan_eq {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (hA0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A = 0) :
    ∃ U : G.gaugeJetGroup, G.evalGaugeJet U = 1 ∧
      ∑ μ, (X μ : SpaceTimeAlgebra) • (G.maurerCartan U μ : Matrix κ κ SpaceTimeAlgebra) = -A
```

## Depends on

- [The jet gauge group of a global gauge group](globalgaugegroup-gaugejetgroup.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/MaurerCartan.lean)
