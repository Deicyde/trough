---
declaration: module
origin: cited
lean: jetOfConstant, jetOfConstant_apply, jetDeriv, jetDeriv_tmul, jetDeriv_comm, jetIteratedDeriv, jetIteratedDeriv_zero, jetIteratedDeriv_cons
statement: formalized
proof: formalized
---

# `V`-valued jets

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.Jet`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean): 31 declarations (1 instance with no name), 14 with a docstring.

## i. Overview

> The jets of a field valued in a complex vector space `V` are `SpaceTimeAlgebra ⊗[ℂ] V`. This file
> provides the basic toolkit for them, independent of any gauge group:
>
> * `jetOfConstant` — the inclusion of constants, `v ↦ 1 ⊗ v`;
> * `jetDeriv`/`jetIteratedDeriv` — the formal derivative, acting on the jet factor;
> * `jetEval` — evaluation at the base point, `f ⊗ v ↦ (constant coefficient of f) • v`.

## ii. Key results

> - `jetOfConstant` : the inclusion of constants into `V`-valued jets: `v ↦ 1 ⊗ v`
> - `jetDeriv` : the formal derivative on `V`-valued jets in the direction `μ`, acting on the jet
>   factor
> - `jetIteratedDeriv` : the iterated formal derivative on `V`-valued jets, in the (unordered)
>   directions given by the multiset `μs`
> - `jetEval`

## iv. References

> * None.

## A. `V`-valued jets

**`jetOfConstant`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L61).

> The inclusion of constants into `V`-valued jets: `v ↦ 1 ⊗ v`.

```lean
noncomputable def jetOfConstant : V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetOfConstant_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L65).

```lean
lemma jetOfConstant_apply (v : V) : jetOfConstant v = (1 : SpaceTimeAlgebra) ⊗ₜ[ℂ] v
```

**`jetDeriv`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L69).

> The formal derivative on `V`-valued jets in the direction `μ`, acting on the jet
> factor.

```lean
noncomputable def jetDeriv (μ : Fin 1 ⊕ Fin 3) :
    SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetDeriv_tmul`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L74).

```lean
lemma jetDeriv_tmul (μ : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) (v : V) :
    jetDeriv μ (f ⊗ₜ[ℂ] v) = pderiv μ f ⊗ₜ[ℂ] v
```

**`jetDeriv_comm`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L79).

> Formal derivatives on `V`-valued jets commute, since the partial derivatives of
> jets do.

```lean
lemma jetDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (jetDeriv (V := V) μ).comp (jetDeriv ν) = (jetDeriv ν).comp (jetDeriv μ)
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L87).

> Post-composition with `jetDeriv` is right-commutative, which is what allows
> iterated derivatives to be indexed by a `Multiset` of directions.

```lean
instance : RightCommutative (fun (L : SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V)
    (μ : Fin 1 ⊕ Fin 3) => L.comp (jetDeriv μ))
```

**`jetIteratedDeriv`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L97).

> The iterated formal derivative on `V`-valued jets, in the (unordered) directions
> given by the multiset `μs`.

```lean
noncomputable def jetIteratedDeriv (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetIteratedDeriv_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L102).

```lean
lemma jetIteratedDeriv_zero :
    jetIteratedDeriv (V := V) (0 : Multiset (Fin 1 ⊕ Fin 3)) = LinearMap.id
```

**`jetIteratedDeriv_cons`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L106).

```lean
lemma jetIteratedDeriv_cons (μ : Fin 1 ⊕ Fin 3) (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    jetIteratedDeriv (V := V) (μ ::ₘ μs) = (jetDeriv μ).comp (jetIteratedDeriv μs)
```

**`jetIteratedDeriv_add`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L122).

> The iterated derivative is additive in the multiset of directions.

```lean
lemma jetIteratedDeriv_add (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    jetIteratedDeriv (V := V) (s + t) =
      (jetIteratedDeriv s).comp (jetIteratedDeriv t)
```

**`jetIteratedDeriv_singleton`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L132).

```lean
lemma jetIteratedDeriv_singleton (μ : Fin 1 ⊕ Fin 3) :
    jetIteratedDeriv (V := V) ({μ} : Multiset (Fin 1 ⊕ Fin 3)) = jetDeriv μ
```

**`jetEval`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L140).

> Evaluation of a `V`-valued jet at the base point:
> `f ⊗ v ↦ (constant coefficient of f) • v`. This is a retraction of
> `jetOfConstant`.

```lean
noncomputable def jetEval : SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] V
```

**`jetEval_tmul`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L144).

```lean
lemma jetEval_tmul (f : SpaceTimeAlgebra) (v : V) :
    jetEval (f ⊗ₜ[ℂ] v) = constantCoeff f • v
```

**`jetEval_jetOfConstant`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L147).

```lean
lemma jetEval_jetOfConstant (v : V) : jetEval (jetOfConstant v) = v
```

**`jetEval_smul`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L152).

> Evaluation at the base point is semilinear over the jet ring: a scalar jet acts through
> its constant coefficient.

```lean
lemma jetEval_smul (f : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEval (f • z) = constantCoeff f • jetEval z
```

## B. The jets of a product of value spaces

> A field valued in `V × W` is a pair of fields, one valued in `V` and one in `W`, and the
> identification `jetProdEquiv` of its jets with the pair of their jets intertwines every
> piece of the jet toolkit: the inclusion of constants, the formal derivative and the
> base-point evaluation all act componentwise.

**`jetProdEquiv`**, an abbrev, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L176).

> **The jets of a product are the product of the jets**: `SpaceTimeAlgebra ⊗ (V × W)` splits as
> `(SpaceTimeAlgebra ⊗ V) × (SpaceTimeAlgebra ⊗ W)`, the jet-ring factor being shared.

```lean
noncomputable abbrev jetProdEquiv :
    SpaceTimeAlgebra ⊗[ℂ] (V × W) ≃ₗ[ℂ] (SpaceTimeAlgebra ⊗[ℂ] V) × (SpaceTimeAlgebra ⊗[ℂ] W)
```

**`jetProdEquiv_jetOfConstant`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L181).

```lean
lemma jetProdEquiv_jetOfConstant (v : V) (w : W) :
    jetProdEquiv (jetOfConstant (v, w)) = (jetOfConstant v, jetOfConstant w)
```

**`jetProdEquiv_jetDeriv`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L184).

```lean
lemma jetProdEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (jetDeriv μ z) =
      (jetDeriv μ (jetProdEquiv z).1, jetDeriv μ (jetProdEquiv z).2)
```

**`jetProdEquiv_jetIteratedDeriv`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L192).

```lean
lemma jetProdEquiv_jetIteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3))
    (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (jetIteratedDeriv s z) =
      (jetIteratedDeriv s (jetProdEquiv z).1, jetIteratedDeriv s (jetProdEquiv z).2)
```

**`jetProdEquiv_smul`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L205).

> The identification is `SpaceTimeAlgebra`-linear: multiplication by a scalar jet acts on both
> components.

```lean
lemma jetProdEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (χ • z) = (χ • (jetProdEquiv z).1, χ • (jetProdEquiv z).2)
```

**`jetProdEquiv_symm_smul`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L212).

```lean
lemma jetProdEquiv_symm_smul (χ : SpaceTimeAlgebra) (a : SpaceTimeAlgebra ⊗[ℂ] V)
    (b : SpaceTimeAlgebra ⊗[ℂ] W) :
    (jetProdEquiv (V := V) (W := W)).symm (χ • a, χ • b)
      = χ • (jetProdEquiv (V := V) (W := W)).symm (a, b)
```

**`jetEval_prod`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L219).

```lean
lemma jetEval_prod (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetEval z = (jetEval (jetProdEquiv z).1, jetEval (jetProdEquiv z).2)
```

## C. The jets of an indexed product of value spaces

> A field valued in a finite product `∀ i, E i` is a family of fields, one for each index,
> and `jetPiEquiv` identifies its jets with the family of their jets. It intertwines the
> whole jet toolkit index by index, exactly as `jetProdEquiv` does in the binary case. The
> index type has to be finite for the identification to exist at all: a jet of a field
> valued in an infinite product need not have all but finitely many of its components
> constant, so `TensorProduct.piRightHom` is only an equivalence in the finite case.

**`jetPiEquiv`**, an abbrev, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L249).

> **The jets of a finite product are the product of the jets**:
> `SpaceTimeAlgebra ⊗ (∀ i, E i)` splits as `∀ i, SpaceTimeAlgebra ⊗ E i`, the jet-ring factor being
> shared.

```lean
noncomputable abbrev jetPiEquiv :
    SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i) ≃ₗ[ℂ] ∀ i, SpaceTimeAlgebra ⊗[ℂ] E i
```

**`jetPiEquiv_jetOfConstant`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L253).

```lean
lemma jetPiEquiv_jetOfConstant (v : ∀ i, E i) :
    jetPiEquiv E (jetOfConstant v) = fun i => jetOfConstant (v i)
```

**`jetPiEquiv_jetDeriv`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L256).

```lean
lemma jetPiEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (jetDeriv μ z) i = jetDeriv μ (jetPiEquiv E z i)
```

**`jetPiEquiv_jetIteratedDeriv`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L262).

```lean
lemma jetPiEquiv_jetIteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3))
    (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (jetIteratedDeriv s z) i = jetIteratedDeriv s (jetPiEquiv E z i)
```

**`jetPiEquiv_smul`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L273).

> The identification is `SpaceTimeAlgebra`-linear: multiplication by a scalar jet acts on every
> component.

```lean
lemma jetPiEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (χ • z) i = χ • (jetPiEquiv E z i)
```

**`jetPiEquiv_symm_smul`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L279).

```lean
lemma jetPiEquiv_symm_smul (χ : SpaceTimeAlgebra) (a : ∀ i, SpaceTimeAlgebra ⊗[ℂ] E i) :
    (jetPiEquiv E).symm (fun i => χ • a i) = χ • (jetPiEquiv E).symm a
```

**`jetEval_pi`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L284).

```lean
lemma jetEval_pi (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetEval z i = jetEval (jetPiEquiv E z i)
```

**`jetPiEquiv_eq_lTensor_proj`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L295).

> The component of the splitting is the projection on the value factor. Reading off
> the summand `i` of a jet of a `(∀ i, E i)`-valued field is applying the projection onto
> that summand to the value factor, the jet-ring factor being untouched. This is the form
> in which the splitting meets the naturality statements, which are all phrased in terms of
> linear maps of value spaces.

```lean
lemma jetPiEquiv_eq_lTensor_proj (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E z i = LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i) z
```

**`jetPi_hom_ext`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean#L304).

> Two maps into the jets of a product agree as soon as their species components do.
> The splitting is an equivalence, so a jet of a `(∀ i, E i)`-valued field is determined by
> its summands.

```lean
lemma jetPi_hom_ext {N : Type} [AddCommGroup N] [Module ℂ N]
    {A B : N →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)}
    (h : ∀ i, (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i)).comp A
      = (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i)).comp B) : A = B
```

## Depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/Jet.lean)
