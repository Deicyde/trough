---
declaration: module
origin: cited
lean: jetOfConstant, jetOfConstant_apply, jetDeriv, jetDeriv_tmul, jetDeriv_comm, jetIteratedDeriv, jetIteratedDeriv_zero, jetIteratedDeriv_cons
statement: formalized
proof: formalized
---

# `V`-valued jets

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Jet`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean): 58 declarations (1 instance with no name), 37 with a docstring; 3 private, not shown.

> The formal Taylor expansions of a field valued in a complex vector space, their derivatives
> and their base-point values.

## i. Overview

> The jets of a field valued in a complex vector space `V` are `SpaceTimeAlgebra ⊗[ℂ] V`. This file
> provides the basic toolkit for them, independent of any gauge group.
>
> * `jetOfConstant` is the inclusion of constants, `v ↦ 1 ⊗ v`.
> * `jetDeriv` and `jetIteratedDeriv` are the formal derivatives, acting on the jet factor.
> * `jetEval` is evaluation at the base point, `f ⊗ v ↦ (constant coefficient of f) • v`.
>
> When `V` is finite-dimensional, a jet is determined by its base-point derivatives
> `jetDerivValue s`, and any family of base-point derivatives is realised, `ofJetDerivValues`.
> The Euler operator `E = ∑_ρ x_ρ ∂_ρ` multiplies the base-point derivative along `s` by `|s|`.
>
> When `V = A` is a finite-dimensional algebra, the jets form an algebra on which the formal
> derivatives are derivations, and the base-point derivatives of a product obey the Leibniz
> rule. A family `Ω_μ` of `A`-valued jets that is flat,
> `∂_μ Ω_ν − ∂_ν Ω_μ = Ω_μ Ω_ν − Ω_ν Ω_μ`, has a unique solution of `∂_μ T = Ω_μ T` with any
> prescribed value. It is the radial transport, the solution of `E T = (∑_μ x_μ Ω_μ) T`, and
> flatness makes it solve each equation and not only their radial combination. This is the
> formal version of integrating a flat connection along rays from the base point.

## ii. Key results

> - `jetOfConstant` : the inclusion of constants into `V`-valued jets, `v ↦ 1 ⊗ v`.
> - `jetDeriv` : the formal derivative on `V`-valued jets in the direction `μ`, acting on the jet
>   factor.
> - `jetIteratedDeriv` : the iterated formal derivative on `V`-valued jets, in the (unordered)
>   directions given by a multiset.
> - `jetEval` : evaluation of a `V`-valued jet at the base point.
> - `jetDerivValue` : the base-point derivative of a jet along a multiset of directions.
> - `jet_ext_of_jetDerivValue` : a jet valued in a finite-dimensional space is determined by its
>   base-point derivatives.
> - `ofJetDerivValues` : the jet with prescribed base-point derivatives.
> - `jetDerivValue_mul` : the Leibniz rule for the base-point derivatives of a product.
> - `exists_jetDeriv_eq_mul` : a flat family `Ω_μ` has a solution of `∂_μ T = Ω_μ T` with any
>   value.
> - `eq_of_jetDeriv_eq_mul` : that solution is unique.

## iv. References

> * None.

## A. `V`-valued jets

**`jetOfConstant`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L89).

> The inclusion of constants into `V`-valued jets, `v ↦ 1 ⊗ v`.

```lean
noncomputable def jetOfConstant : V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetOfConstant_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L93).

```lean
lemma jetOfConstant_apply (v : V) : jetOfConstant v = (1 : SpaceTimeAlgebra) ⊗ₜ[ℂ] v
```

**`jetDeriv`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L97).

> The formal derivative on `V`-valued jets in the direction `μ`, acting on the jet
> factor.

```lean
noncomputable def jetDeriv (μ : Fin 1 ⊕ Fin 3) :
    SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetDeriv_tmul`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L102).

```lean
lemma jetDeriv_tmul (μ : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) (v : V) :
    jetDeriv μ (f ⊗ₜ[ℂ] v) = pderiv μ f ⊗ₜ[ℂ] v
```

**`jetDeriv_comm`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L107).

> Formal derivatives on `V`-valued jets commute, since the partial derivatives of
> jets do.

```lean
lemma jetDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (jetDeriv (V := V) μ).comp (jetDeriv ν) = (jetDeriv ν).comp (jetDeriv μ)
```

**An instance with no name**, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L115).

> Post-composition with `jetDeriv` is right-commutative, which is what allows
> iterated derivatives to be indexed by a `Multiset` of directions.

```lean
instance : RightCommutative (fun (L : SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V)
    (μ : Fin 1 ⊕ Fin 3) => L.comp (jetDeriv μ))
```

**`jetIteratedDeriv`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L125).

> The iterated formal derivative on `V`-valued jets, in the (unordered) directions
> given by the multiset `μs`.

```lean
noncomputable def jetIteratedDeriv (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetIteratedDeriv_zero`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L130).

```lean
lemma jetIteratedDeriv_zero :
    jetIteratedDeriv (V := V) (0 : Multiset (Fin 1 ⊕ Fin 3)) = LinearMap.id
```

**`jetIteratedDeriv_cons`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L134).

```lean
lemma jetIteratedDeriv_cons (μ : Fin 1 ⊕ Fin 3) (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    jetIteratedDeriv (V := V) (μ ::ₘ μs) = (jetDeriv μ).comp (jetIteratedDeriv μs)
```

**`jetIteratedDeriv_add`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L150).

> The iterated derivative is additive in the multiset of directions.

```lean
lemma jetIteratedDeriv_add (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    jetIteratedDeriv (V := V) (s + t) =
      (jetIteratedDeriv s).comp (jetIteratedDeriv t)
```

**`jetIteratedDeriv_singleton`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L160).

```lean
lemma jetIteratedDeriv_singleton (μ : Fin 1 ⊕ Fin 3) :
    jetIteratedDeriv (V := V) ({μ} : Multiset (Fin 1 ⊕ Fin 3)) = jetDeriv μ
```

**`jetEval`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L168).

> Evaluation of a `V`-valued jet at the base point,
> `f ⊗ v ↦ (constant coefficient of f) • v`. This is a retraction of
> `jetOfConstant`.

```lean
noncomputable def jetEval : SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] V
```

**`jetEval_tmul`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L172).

```lean
lemma jetEval_tmul (f : SpaceTimeAlgebra) (v : V) :
    jetEval (f ⊗ₜ[ℂ] v) = constantCoeff f • v
```

**`jetEval_jetOfConstant`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L175).

```lean
lemma jetEval_jetOfConstant (v : V) : jetEval (jetOfConstant v) = v
```

**`jetEval_smul`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L180).

> Evaluation at the base point is semilinear over the jet ring, since a scalar jet acts through
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

**`jetProdEquiv`**, an abbrev, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L204).

> The jets of a product are the product of the jets, as `SpaceTimeAlgebra ⊗ (V × W)` splits as
> `(SpaceTimeAlgebra ⊗ V) × (SpaceTimeAlgebra ⊗ W)`, the jet-ring factor being shared.

```lean
noncomputable abbrev jetProdEquiv :
    SpaceTimeAlgebra ⊗[ℂ] (V × W) ≃ₗ[ℂ] (SpaceTimeAlgebra ⊗[ℂ] V) × (SpaceTimeAlgebra ⊗[ℂ] W)
```

**`jetProdEquiv_jetOfConstant`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L209).

```lean
lemma jetProdEquiv_jetOfConstant (v : V) (w : W) :
    jetProdEquiv (jetOfConstant (v, w)) = (jetOfConstant v, jetOfConstant w)
```

**`jetProdEquiv_jetDeriv`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L212).

```lean
lemma jetProdEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (jetDeriv μ z) =
      (jetDeriv μ (jetProdEquiv z).1, jetDeriv μ (jetProdEquiv z).2)
```

**`jetProdEquiv_jetIteratedDeriv`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L220).

```lean
lemma jetProdEquiv_jetIteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3))
    (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (jetIteratedDeriv s z) =
      (jetIteratedDeriv s (jetProdEquiv z).1, jetIteratedDeriv s (jetProdEquiv z).2)
```

**`jetProdEquiv_smul`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L233).

> The identification is `SpaceTimeAlgebra`-linear, so multiplication by a scalar jet acts on both
> components.

```lean
lemma jetProdEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] (V × W)) :
    jetProdEquiv (χ • z) = (χ • (jetProdEquiv z).1, χ • (jetProdEquiv z).2)
```

**`jetProdEquiv_symm_smul`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L240).

```lean
lemma jetProdEquiv_symm_smul (χ : SpaceTimeAlgebra) (a : SpaceTimeAlgebra ⊗[ℂ] V)
    (b : SpaceTimeAlgebra ⊗[ℂ] W) :
    (jetProdEquiv (V := V) (W := W)).symm (χ • a, χ • b)
      = χ • (jetProdEquiv (V := V) (W := W)).symm (a, b)
```

**`jetEval_prod`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L247).

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

**`jetPiEquiv`**, an abbrev, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L277).

> The jets of a finite product are the product of the jets, as
> `SpaceTimeAlgebra ⊗ (∀ i, E i)` splits as `∀ i, SpaceTimeAlgebra ⊗ E i`, the jet-ring factor being
> shared.

```lean
noncomputable abbrev jetPiEquiv :
    SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i) ≃ₗ[ℂ] ∀ i, SpaceTimeAlgebra ⊗[ℂ] E i
```

**`jetPiEquiv_jetDeriv`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L281).

```lean
lemma jetPiEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (jetDeriv μ z) i = jetDeriv μ (jetPiEquiv E z i)
```

**`jetPiEquiv_jetIteratedDeriv`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L287).

```lean
lemma jetPiEquiv_jetIteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3))
    (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (jetIteratedDeriv s z) i = jetIteratedDeriv s (jetPiEquiv E z i)
```

**`jetPiEquiv_smul`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L298).

> The identification is `SpaceTimeAlgebra`-linear, so multiplication by a scalar jet acts on every
> component.

```lean
lemma jetPiEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E (χ • z) i = χ • (jetPiEquiv E z i)
```

**`jetPiEquiv_symm_smul`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L304).

```lean
lemma jetPiEquiv_symm_smul (χ : SpaceTimeAlgebra) (a : ∀ i, SpaceTimeAlgebra ⊗[ℂ] E i) :
    (jetPiEquiv E).symm (fun i => χ • a i) = χ • (jetPiEquiv E).symm a
```

**`jetEval_pi`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L309).

```lean
lemma jetEval_pi (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetEval z i = jetEval (jetPiEquiv E z i)
```

**`jetPiEquiv_eq_lTensor_proj`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L320).

> The component of the splitting is the projection on the value factor. Reading off
> the summand `i` of a jet of a `(∀ i, E i)`-valued field is applying the projection onto
> that summand to the value factor, the jet-ring factor being untouched. This is the form
> in which the splitting meets the naturality statements, which are all phrased in terms of
> linear maps of value spaces.

```lean
lemma jetPiEquiv_eq_lTensor_proj (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, E i)) (i : ι) :
    jetPiEquiv E z i = LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i) z
```

## D. Base-point derivatives of `V`-valued jets

**`jetDerivValue`**, a def, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L337).

> The base-point value `(∂^s z)(0)` of the iterated derivative of a `V`-valued jet.

```lean
noncomputable def jetDerivValue (s : Multiset (Fin 1 ⊕ Fin 3)) :
    SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] V
```

**`jetIteratedDeriv_tmul`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L341).

```lean
lemma jetIteratedDeriv_tmul (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) (v : V) :
    jetIteratedDeriv s (f ⊗ₜ[ℂ] v) = SpaceTimeAlgebra.iteratedPDeriv s f ⊗ₜ[ℂ] v
```

**`jetDerivValue_tmul`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L350).

```lean
lemma jetDerivValue_tmul (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) (v : V) :
    jetDerivValue s (f ⊗ₜ[ℂ] v) = constantCoeff (SpaceTimeAlgebra.iteratedPDeriv s f) • v
```

**`jetDerivValue_zero`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L355).

```lean
lemma jetDerivValue_zero : jetDerivValue (V := V) 0 = jetEval
```

**`jetDerivValue_cons`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L359).

> The base-point derivative along `μ :: s` is that along `s` of the derivative `∂_μ`.

```lean
lemma jetDerivValue_cons (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetDerivValue (μ ::ₘ s) z = jetDerivValue s (jetDeriv μ z)
```

**`jetDerivValue_jetOfConstant`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L367).

> The base-point derivatives of the jet of a constant vanish, except its value.

```lean
lemma jetDerivValue_jetOfConstant (s : Multiset (Fin 1 ⊕ Fin 3)) (v : V) :
    jetDerivValue s (jetOfConstant v) = if s = 0 then v else 0
```

**`jet_ext_of_jetDerivValue`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L406).

> A jet valued in a finite-dimensional space is determined by its base-point
> derivatives.

```lean
lemma jet_ext_of_jetDerivValue {z w : SpaceTimeAlgebra ⊗[ℂ] V}
    (h : ∀ s, jetDerivValue s z = jetDerivValue s w) : z = w
```

**`ofJetDerivValues`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L415).

> The jet valued in a finite-dimensional space with prescribed base-point derivatives.

```lean
noncomputable def ofJetDerivValues (c : Multiset (Fin 1 ⊕ Fin 3) → V) :
    SpaceTimeAlgebra ⊗[ℂ] V
```

**`jetDerivValue_ofJetDerivValues`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L421).

```lean
lemma jetDerivValue_ofJetDerivValues (c : Multiset (Fin 1 ⊕ Fin 3) → V)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : jetDerivValue s (ofJetDerivValues c) = c s
```

## E. The Euler operator on `V`-valued jets

**`jetDeriv_X_smul`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L438).

> The derivative of a jet multiplied by a coordinate,
> `∂_μ (x_ν z) = δ_{μν} z + x_ν ∂_μ z`.

```lean
lemma jetDeriv_X_smul (μ ν : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetDeriv μ ((X ν : SpaceTimeAlgebra) • z) =
      (if μ = ν then z else 0) + (X ν : SpaceTimeAlgebra) • jetDeriv μ z
```

**`jetDerivValue_euler`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L456).

> The Euler operator `E = ∑_ρ x_ρ ∂_ρ` multiplies the base-point derivative along `s` by the
> order `|s|` of `s`.

```lean
lemma jetDerivValue_euler (s : Multiset (Fin 1 ⊕ Fin 3)) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetDerivValue s (∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ z) =
      (s.card : ℂ) • jetDerivValue s z
```

**`jetDeriv_sum_X_smul`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L470).

> The derivative of a radial combination, `∂_μ (∑_ν x_ν F_ν) = F_μ + ∑_ν x_ν ∂_μ F_ν`.

```lean
lemma jetDeriv_sum_X_smul (μ : Fin 1 ⊕ Fin 3) (F : Fin 1 ⊕ Fin 3 → SpaceTimeAlgebra ⊗[ℂ] V) :
    jetDeriv μ (∑ ν, (X ν : SpaceTimeAlgebra) • F ν) =
      F μ + ∑ ν, (X ν : SpaceTimeAlgebra) • jetDeriv μ (F ν)
```

**`jetDeriv_euler`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L478).

> The derivative `∂_μ` and the Euler operator commute up to `∂_μ` itself,
> `∂_μ (E z) = E (∂_μ z) + ∂_μ z`.

```lean
lemma jetDeriv_euler (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetDeriv μ (∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ z) =
      ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ (jetDeriv μ z) + jetDeriv μ z
```

## F. Jets valued in an algebra

> The jets of a field valued in a complex algebra `E` form the algebra `SpaceTimeAlgebra ⊗[ℂ] E`.
> The formal derivatives are derivations of it, evaluation at the base point is multiplicative,
> and the base-point derivatives of a product obey the Leibniz rule. When `E` is
> finite-dimensional, the radial system `E T = R T` has a solution with `T(0) = 1`, and solutions
> of the homogeneous radial systems vanish.

**`jetDeriv_mul`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L507).

> The formal derivatives are derivations of the algebra of `A`-valued jets.

```lean
lemma jetDeriv_mul (μ : Fin 1 ⊕ Fin 3) (x y : SpaceTimeAlgebra ⊗[ℂ] A) :
    jetDeriv μ (x * y) = jetDeriv μ x * y + x * jetDeriv μ y
```

**`jetEval_mul`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L525).

> Evaluation at the base point is multiplicative on `A`-valued jets.

```lean
lemma jetEval_mul (x y : SpaceTimeAlgebra ⊗[ℂ] A) : jetEval (x * y) = jetEval x * jetEval y
```

**`jetEval_one`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L536).

```lean
lemma jetEval_one : jetEval (1 : SpaceTimeAlgebra ⊗[ℂ] A) = 1
```

**`jetDerivValue_mul`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L542).

> The Leibniz rule for the base-point derivatives of a product of `A`-valued jets. The
> derivative along `s` of `x y` is the sum over the splittings `s = t₁ + t₂` of the products of
> the derivatives along `t₁` and `t₂`.

```lean
lemma jetDerivValue_mul (s : Multiset (Fin 1 ⊕ Fin 3)) (x y : SpaceTimeAlgebra ⊗[ℂ] A) :
    jetDerivValue s (x * y) =
      (s.antidiagonal.map fun p => jetDerivValue p.1 x * jetDerivValue p.2 y).sum
```

**`jetDerivValue_commutator`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L554).

> The Leibniz rule for the base-point derivatives of a commutator of `A`-valued jets, which
> are sums of commutators of base-point derivatives.

```lean
lemma jetDerivValue_commutator (s : Multiset (Fin 1 ⊕ Fin 3)) (x y : SpaceTimeAlgebra ⊗[ℂ] A) :
    jetDerivValue s (x * y - y * x) = (s.antidiagonal.map fun p =>
      jetDerivValue p.1 x * jetDerivValue p.2 y -
        jetDerivValue p.2 y * jetDerivValue p.1 x).sum
```

**`jetDerivValue_mul_jetOfConstant`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L564).

> The base-point derivatives of a jet times a constant.

```lean
lemma jetDerivValue_mul_jetOfConstant (s : Multiset (Fin 1 ⊕ Fin 3)) (x : SpaceTimeAlgebra ⊗[ℂ] A)
    (a : A) : jetDerivValue s (x * jetOfConstant a) = jetDerivValue s x * a
```

**`jetDerivValue_mul_eq_zero`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L574).

> The base-point derivative of `R z` along `s` vanishes when `R` vanishes at the base point and
> the base-point derivatives of `z` of lower order vanish.

```lean
lemma jetDerivValue_mul_eq_zero {R z : SpaceTimeAlgebra ⊗[ℂ] A} (hR : jetEval R = 0)
    {s : Multiset (Fin 1 ⊕ Fin 3)} (hz : ∀ t : Multiset (Fin 1 ⊕ Fin 3), t.card < s.card →
      jetDerivValue t z = 0) : jetDerivValue s (R * z) = 0
```

**`eq_zero_of_euler_eq_mul`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L592).

> The vanishing principle for the Euler operator. An `A`-valued jet `z` vanishing at the base
> point with `E z = R z`, for `R` vanishing at the base point, is zero.

```lean
lemma eq_zero_of_euler_eq_mul {R z : SpaceTimeAlgebra ⊗[ℂ] A} (hR : jetEval R = 0)
    (h0 : jetEval z = 0) (h : ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ z = R * z) : z = 0
```

**`eq_zero_of_euler_add_eq_mul`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L606).

> The vanishing principle for the shifted Euler operator. An `A`-valued jet `z` with
> `E z + z = R z`, for `R` vanishing at the base point, is zero.

```lean
lemma eq_zero_of_euler_add_eq_mul {R z : SpaceTimeAlgebra ⊗[ℂ] A} (hR : jetEval R = 0)
    (h : ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ z + z = R * z) : z = 0
```

**`exists_euler_eq_mul`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L623).

> The radial (Euler) transport. For an `A`-valued jet `R` vanishing at the base point, the
> radial system `E T = R T` has a solution with `T(0) = 1`. Its base-point derivatives are
> fixed order by order, the derivative along `s ≠ 0` being `1/|s|` times the sum over the
> splittings `s = t₁ + t₂` of `(∂^{t₁} R)(0) (∂^{t₂} T)(0)`, which involves only lower orders of
> `T`.

```lean
lemma exists_euler_eq_mul (R : SpaceTimeAlgebra ⊗[ℂ] A) (hR : jetEval R = 0) :
    ∃ T : SpaceTimeAlgebra ⊗[ℂ] A, jetEval T = 1 ∧
      ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ T = R * T
```

## G. Flat connections on jets

> A family `Ω_μ` of `A`-valued jets is flat when `∂_μ Ω_ν − ∂_ν Ω_μ = Ω_μ Ω_ν − Ω_ν Ω_μ`. The
> system `∂_μ T = Ω_μ T` then has a unique solution with any prescribed value: the radial
> transport of `R = ∑_μ x_μ Ω_μ` solves its radial combination, and flatness makes the defect
> `∂_μ T − Ω_μ T` solve `E D + D = R D`, so vanish.

**`euler_mul`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L688).

> The Euler operator is a derivation of the algebra of `A`-valued jets.

```lean
lemma euler_mul (x y : SpaceTimeAlgebra ⊗[ℂ] A) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ (x * y) =
      (∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ x) * y +
        x * ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ y
```

**`jetDeriv_mul_sub_mul`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L698).

> The derivative of a conjugation defect `a J − J b`, for `J` with `∂_μ J = Ω J` and `a`
> with `∂_μ a = a' + [Ω, a]`, is `(a' J − J ∂_μ b) + Ω (a J − J b)`.

```lean
lemma jetDeriv_mul_sub_mul {a a' b J Ω : SpaceTimeAlgebra ⊗[ℂ] A} (μ : Fin 1 ⊕ Fin 3)
    (ha : jetDeriv μ a = a' + (Ω * a - a * Ω)) (hJ : jetDeriv μ J = Ω * J) :
    jetDeriv μ (a * J - J * b) = (a' * J - J * jetDeriv μ b) + Ω * (a * J - J * b)
```

**`jetDeriv_eq_mul_of_euler`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L709).

> The radial transport solves every equation `∂_μ T = Ω_μ T` of a flat family, not only
> their radial combination.

```lean
lemma jetDeriv_eq_mul_of_euler
    (hΩ : ∀ μ ν, jetDeriv μ (Ω ν) - jetDeriv ν (Ω μ) = Ω μ * Ω ν - Ω ν * Ω μ)
    {T : SpaceTimeAlgebra ⊗[ℂ] A}
    (hT : ∑ ρ, (X ρ : SpaceTimeAlgebra) • jetDeriv ρ T =
      (∑ ν, (X ν : SpaceTimeAlgebra) • Ω ν) * T) (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv μ T = Ω μ * T
```

**`exists_jetDeriv_eq_mul`**, a lemma, [line 747](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L747).

> A flat family `Ω_μ` of `A`-valued jets has, for every `a`, a solution of
> `∂_μ T = Ω_μ T` with value `a`, the radial transport of `∑_μ x_μ Ω_μ` times the constant
> `a`.

```lean
lemma exists_jetDeriv_eq_mul
    (hΩ : ∀ μ ν, jetDeriv μ (Ω ν) - jetDeriv ν (Ω μ) = Ω μ * Ω ν - Ω ν * Ω μ) (a : A) :
    ∃ T : SpaceTimeAlgebra ⊗[ℂ] A, jetEval T = a ∧ ∀ μ, jetDeriv μ T = Ω μ * T
```

**`eq_of_jetDeriv_eq_mul`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L760).

> A solution of `∂_μ T = Ω_μ T` is determined by its value, since the difference of two solutions
> vanishes at the base point and solves the radial system `E D = R D`.

```lean
lemma eq_of_jetDeriv_eq_mul {Y Z : SpaceTimeAlgebra ⊗[ℂ] A}
    (hY : ∀ μ, jetDeriv μ Y = Ω μ * Y) (hZ : ∀ μ, jetDeriv μ Z = Ω μ * Z)
    (h0 : jetEval Y = jetEval Z) : Y = Z
```

**`eq_zero_of_jetDeriv_eq_add_mul`**, a lemma, [line 774](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean#L774).

> A family `F i` of `A`-valued jets vanishing at the base point, whose derivatives are
> `∂_μ F i = F (d_μ i) + Ω_μ F i`, vanishes, since its base-point derivatives vanish by induction on
> their order.

```lean
lemma eq_zero_of_jetDeriv_eq_add_mul {ι : Type} (F : ι → SpaceTimeAlgebra ⊗[ℂ] A)
    (d : Fin 1 ⊕ Fin 3 → ι → ι) (hF : ∀ μ i, jetDeriv μ (F i) = F (d μ i) + Ω μ * F i)
    (h0 : ∀ i, jetEval (F i) = 0) (i : ι) : F i = 0
```

## Depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Jet.lean)
