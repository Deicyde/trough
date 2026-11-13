---
declaration: module
origin: cited
lean: LocalGaugeData.U1Factor, LocalGaugeData.SUFactor, LocalGaugeData.Factor, LocalGaugeData.Factors, LocalGaugeData.U1Factor.comap, LocalGaugeData.SUFactor.comap, LocalGaugeData.Factor.comap, LocalGaugeData.Factors.comap
statement: formalized
proof: formalized
---

# The factors of a gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Factor`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean): 8 declarations, 8 with a docstring.

## i. Overview

> A gauge group is presented, as in a model-building table, by its factors: `U(1)` factors
> and `SU(n)` factors. This file says what a factor of a local gauge data package is, without
> reference to matter:
>
> * `LocalGaugeData.U1Factor` : a unitary jet `u U` attached to each gauge jet, with the
>   matching components `φ`, `φJ` of the gauge algebra and its jets, related by the
>   Maurer–Cartan form `φJ (ω_μ U) = i (∂_μ u) u⁻¹` and invariant under the adjoint action;
> * `LocalGaugeData.SUFactor` : a unitary matrix of jets `u U` attached to each gauge jet,
>   with the matching matrix components `φ`, `φJ`, related by the Maurer–Cartan form
>   `φJ (ω_μ U) = i (∂_μ u) u⁻¹` and transforming by conjugation under the adjoint action;
> * `LocalGaugeData.Factor`, `Factors` : a factor of either kind, and a gauge group as a
>   list of factors.
>
> Factors pull back along a morphism of local gauge data, `LocalGaugeData.Hom`
> (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Basic`). The projections of a
> product are such morphisms
> (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Prod`), which is how a factor of
> one side becomes a factor of the product.
>
> The canonical factors of the concrete packages are `LocalGaugeData.u1Factor` and
> `LocalGaugeData.suFactor`, and the representations
> a factor names (the charge twist, the fundamental) are built in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Factors`.

## ii. Key results

> - `LocalGaugeData.U1Factor` : a `U(1)` factor of the local gauge data.
> - `LocalGaugeData.SUFactor` : an `SU(n)` factor of the local gauge data.
> - `LocalGaugeData.Factor`, `LocalGaugeData.Factors` : a gauge group presented by its factors.
> - `LocalGaugeData.Factors.comap` : pulling factors back along a morphism.

## iv. References

> * None.

## A. `U(1)` factors

**`LocalGaugeData.U1Factor`**, a structure, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L78).

> **A `U(1)` factor** of the local gauge data: a unitary jet `u U` attached to each gauge
> jet, with the corresponding components `φ c` of the gauge algebra and `φJ a` of its jets,
> related by the Maurer–Cartan form `φJ (ω_μ U) = i (∂_μ u) u⁻¹` and invariant under the
> adjoint action.

```lean
structure U1Factor (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) where
  /-- The unitary jet of a gauge jet. -/
  u : GJ →* unitary SpaceTimeAlgebra
  /-- The `u(1)` component of a gauge algebra element. -/
  φ : 𝔤 →ₗ[ℝ] ℂ
  /-- The `u(1)` component of a jet of gauge algebra elements. -/
  φJ : 𝔤J → SpaceTimeAlgebra
  φJ_ofConstantLie : ∀ c, φJ (jets.ofConstantLie c) = C (φ c)
  φJ_cc_foldl : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J),
    constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p (φJ a))
      = φ (jets.evalLie (jets.iteratedDeriv p a))
  φJ_maurerCartan : ∀ (U : GJ) (μ : Fin 1 ⊕ Fin 3),
    φJ (jets.maurerCartan U μ)
      = Complex.I • (pderiv μ (u U : SpaceTimeAlgebra) * star (u U : SpaceTimeAlgebra))
  φJ_adjoint : ∀ (U : GJ) (c : 𝔤),
    φJ (jets.adjointJ U (jets.ofConstantLie c)) = φJ (jets.ofConstantLie c)
```

## B. `SU(n)` factors

**`LocalGaugeData.SUFactor`**, a structure, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L105).

> **An `SU(n)` factor** of the local gauge data: a unitary matrix of jets `u U` attached
> to each gauge jet, with the corresponding matrix components `φ c` of the gauge algebra
> and `φJ a` of its jets, related by the Maurer–Cartan form `φJ (ω_μ U) = i (∂_μ u) u⁻¹`
> and transforming by conjugation under the adjoint action.

```lean
structure SUFactor (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (n : Type) [Fintype n] [DecidableEq n]
    where
  /-- The unitary matrix of jets of a gauge jet. -/
  u : GJ →* Matrix n n SpaceTimeAlgebra
  u_unitary : ∀ U, star (u U) * u U = 1
  /-- The matrix component of a gauge algebra element. -/
  φ : 𝔤 →ₗ[ℝ] Matrix n n ℂ
  /-- The matrix component of a jet of gauge algebra elements. -/
  φJ : 𝔤J → Matrix n n SpaceTimeAlgebra
  φJ_ofConstantLie : ∀ c, φJ (jets.ofConstantLie c) = (φ c).map (C : ℂ → SpaceTimeAlgebra)
  φJ_cc_foldl : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J),
    ((φJ a).map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = φ (jets.evalLie (jets.iteratedDeriv p a))
  φJ_maurerCartan : ∀ (U : GJ) (μ : Fin 1 ⊕ Fin 3),
    φJ (jets.maurerCartan U μ)
      = Complex.I • (((u U).map fun f => pderiv μ f) * star (u U))
  φJ_adjoint : ∀ (U : GJ) (c : 𝔤),
    φJ (jets.adjointJ U (jets.ofConstantLie c)) = u U * φJ (jets.ofConstantLie c) * star (u U)
```

## C. A gauge group as a list of factors

**`LocalGaugeData.Factor`**, an inductive, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L132).

> **A factor of the gauge group**, presented in the local gauge data: a `U(1)` factor or
> an `SU(n)` factor.

```lean
inductive Factor (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J)
  /-- A `U(1)` factor. -/
  | U1 (F : U1Factor jets)
  /-- An `SU(n)` factor. -/
  | SU {n : ℕ} (F : SUFactor jets (Fin n))
```

**`LocalGaugeData.Factors`**, an abbrev, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L139).

> **A gauge group presented by its factors.**

```lean
abbrev Factors (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) : Type
```

## D. Pulling factors back along a morphism

**`LocalGaugeData.U1Factor.comap`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L153).

> A `U(1)` factor pulled back along a morphism.

```lean
noncomputable def U1Factor.comap (F : U1Factor jets') (h : Hom jets jets') : U1Factor jets
```

**`LocalGaugeData.SUFactor.comap`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L166).

> An `SU(n)` factor pulled back along a morphism.

```lean
noncomputable def SUFactor.comap {n : Type} [Fintype n] [DecidableEq n] (F : SUFactor jets' n)
    (h : Hom jets jets') : SUFactor jets n
```

**`LocalGaugeData.Factor.comap`**, an abbrev, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L182).

> A factor pulled back along a morphism.

```lean
noncomputable abbrev Factor.comap (h : Hom jets jets') : Factor jets' → Factor jets
```

**`LocalGaugeData.Factors.comap`**, an abbrev, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean#L189).

> A list of factors pulled back along a morphism. Written by recursion rather than as
> `List.map`, so that it unfolds at reducible transparency, as the charge tuples of a table
> over `Factors.factors` require.

```lean
noncomputable abbrev Factors.comap (h : Hom jets jets') : Factors jets' → Factors jets
```

## Depends on

- [Local gauge data](../../../../physlib/classicalfieldtheory/gaugetheory/localgaugedata-basic.md)
- [Complex conjugation in the spacetime algebra](../../../../physlib/spaceandtime/spacetime/spacetimealgebra-star.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Factor.lean)
