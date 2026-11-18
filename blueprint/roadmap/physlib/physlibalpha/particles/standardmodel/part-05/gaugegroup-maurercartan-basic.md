---
declaration: module
origin: cited
lean: StandardModel.maurerCartanForm, StandardModel.maurerCartanForm_toSU3Matrix, StandardModel.maurerCartanForm_toSU2Matrix, StandardModel.maurerCartanForm_toU1Value, StandardModel.maurerCartanForm_one, StandardModel.maurerCartanForm_ofConstant, StandardModel.maurerCartanForm_cocycle, StandardModel.deriv_zero_of_maurerCartanForm_zero
statement: formalized
proof: formalized
---

# The Maurer–Cartan forms of the jet gauge group

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.MaurerCartan.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean): 12 declarations, 4 with a docstring.

## i. Overview

> The Maurer-Cartan form is a map
> `ω : JetGaugeGroupI → (Fin 1 ⊕ Fin 3) → JetGaugeAlgebra`
> defined as `ω_μ(U) := i (∂_μ U) U†`.
>
> We will use `ω^a_ν` to denote the `a`-th component of the Maurer–Cartan form in the
> basis of the jet Lie algebra, and `f^a_{b c}` to denote the structure constants of the
> jet Lie algebra in that basis.
>
> It satisfies the following properties, proved here from the matrix definition:
> - *Cocycle law*: `ω_μ(UV) = ω_μ(U) + U ω_μ(V) U†`
> - *Value on the identity*: `ω_μ(1) = 0`
> - *Value on constant gauge transformations*: `ω_μ(U₀) = 0`
> - *Structural equation*: `∂_μ ω^a_ν(U) − ∂_ν ω^a_μ(U) = ∑_{b c} f^a_{b c} · ω^b_μ(U) · ω^c_ν(U)`
>
> These four are exactly the Maurer–Cartan laws of a local gauge data package. What follows
> from them alone — the value on inverses, the symmetrized Maurer–Cartan form and the
> determination of `ω` by its symmetrized base-point data — is proved once, for any package,
> in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MaurerCartan`, and read back at
> `StandardModel.localGaugeData` in
> `PhyslibAlpha.Particles.StandardModel.GaugeGroup.LocalGaugeData`. What remains here is what the
> matrix definition itself gives: the vanishing of `ω` exactly on constant jets.

## ii. Key results

> - `maurerCartanForm` : the Maurer–Cartan form `ω_μ(U) := i (∂_μ U) U⁻¹` of the jet gauge group,
>   valued in the jet gauge algebra
> - `maurerCartanForm_toSU3Matrix`
> - `maurerCartanForm_toSU2Matrix`
> - `maurerCartanForm_toU1Value`

## iv. References

> * None.

## A. The Maurer–Cartan form of the jet gauge group

**`StandardModel.maurerCartanForm`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L68).

> The Maurer–Cartan form `ω_μ(U) := i (∂_μ U) U⁻¹` of the jet gauge group, valued
> in the jet gauge algebra.

```lean
noncomputable def maurerCartanForm (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) : JetGaugeAlgebra
```

**`StandardModel.maurerCartanForm_toSU3Matrix`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L77).

```lean
lemma maurerCartanForm_toSU3Matrix (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (maurerCartanForm U μ).toSU3Matrix =
      Complex.I • (U.1.1.map (pderiv μ) * star U.1.1)
```

**`StandardModel.maurerCartanForm_toSU2Matrix`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L82).

```lean
lemma maurerCartanForm_toSU2Matrix (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (maurerCartanForm U μ).toSU2Matrix =
      Complex.I • (U.2.1.1.map (pderiv μ) * star U.2.1.1)
```

**`StandardModel.maurerCartanForm_toU1Value`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L87).

```lean
lemma maurerCartanForm_toU1Value (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (maurerCartanForm U μ).toU1Value =
      Complex.I • (pderiv μ U.2.2.1 * star U.2.2.1)
```

**`StandardModel.maurerCartanForm_one`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L92).

```lean
lemma maurerCartanForm_one : maurerCartanForm (1 : JetGaugeGroupI) = 0
```

**`StandardModel.maurerCartanForm_ofConstant`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L95).

```lean
lemma maurerCartanForm_ofConstant (U₀ : GaugeGroupI) :
    maurerCartanForm (JetGaugeGroupI.ofConstant U₀) = 0
```

**`StandardModel.maurerCartanForm_cocycle`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L99).

```lean
lemma maurerCartanForm_cocycle (U V : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    maurerCartanForm (U * V) μ = maurerCartanForm U μ + adjoint U (maurerCartanForm V μ)
```

**`StandardModel.deriv_zero_of_maurerCartanForm_zero`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L120).

```lean
lemma deriv_zero_of_maurerCartanForm_zero (U : JetGaugeGroupI) (h : maurerCartanForm U = 0) :
    ∀ μ, U.deriv μ = 0
```

**`StandardModel.maurerCartanForm_eq_zero_iff_ofConstant`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L142).

```lean
lemma maurerCartanForm_eq_zero_iff_ofConstant (U : JetGaugeGroupI) :
    maurerCartanForm U = 0 ↔ ∃ c, U = JetGaugeGroupI.ofConstant c
```

## B. The structural equation

**`StandardModel.maurerCartanForm_structure`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L189).

> The structural (Maurer–Cartan) equation, basis-independently: the Maurer–Cartan
> form is flat,
>
> `∂_μ ω_ν − ∂_ν ω_μ + ⁅ω_μ, ω_ν⁆ = 0`.
>
> In components with respect to a basis of the jet gauge algebra this is
> `∂_μ ω^a_ν − ∂_ν ω^a_μ = ∑_{b c} f^a_{b c} · ω^b_μ · ω^c_ν`. On each matrix
> factor the second-derivative terms cancel by symmetry of mixed partials, the
> derivative of `A†` is rewritten through the differentiated unitarity relation,
> and the surviving first-order terms form the commutator; on the abelian `U(1)`
> factor the commutator is absent and only the symmetry of mixed partials
> remains.

```lean
lemma maurerCartanForm_structure (U : JetGaugeGroupI) (μ ν : Fin 1 ⊕ Fin 3) :
    deriv μ (maurerCartanForm U ν) - deriv ν (maurerCartanForm U μ) +
      ⁅maurerCartanForm U μ, maurerCartanForm U ν⁆ = 0
```

## C. The derivative of the adjoint action

**`StandardModel.JetGaugeAlgebra.deriv_ofConstant`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L270).

> The constant inclusion has vanishing formal derivative: constants have no
> spacetime dependence.

```lean
lemma JetGaugeAlgebra.deriv_ofConstant (μ : Fin 1 ⊕ Fin 3) (a : GaugeAlgebra) :
    deriv μ (ofConstant a) = 0
```

**`StandardModel.deriv_adjointMap`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean#L279).

> The formal derivative intertwines the adjoint action through the Maurer–Cartan
> form: `∂_μ (Ad_U x) = Ad_U (∂_μ x) − ⁅ω_μ(U), Ad_U x⁆`. On the matrix factors this
> is the Leibniz rule with the derivative of `U†` rewritten through the
> differentiated unitarity relation; on the abelian `u(1)` factor the adjoint action
> is trivial and the bracket is absent.

```lean
lemma deriv_adjointMap (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) (x : JetGaugeAlgebra) :
    deriv μ (adjointMap U x) =
      adjointMap U (deriv μ x) - ⁅maurerCartanForm U μ, adjointMap U x⁆
```

## Depends on

- [The jet gauge algebra](../part-04/gaugealgebra-jetgaugealgebra.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/MaurerCartan/Basic.lean)
