---
declaration: module
origin: cited
lean: ClassicalMechanics.AffineSymplecticGroup, ClassicalMechanics.AffineSymplecticGroup.mul_linear, ClassicalMechanics.AffineSymplecticGroup.mul_translation, ClassicalMechanics.AffineSymplecticGroup.one_linear, ClassicalMechanics.AffineSymplecticGroup.one_translation, ClassicalMechanics.AffineSymplecticGroup.inv_linear, ClassicalMechanics.AffineSymplecticGroup.inv_translation, ClassicalMechanics.AffineSymplecticGroup.ext
statement: formalized
proof: formalized
---

# The cohomology class of the affine symplectic group

The module `PhyslibAlpha.ClassicalMechanics.MomentMap.Cohomology`, [PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean): 38 declarations (8 instances with no name), 18 with a docstring.

> The moment cocycle of the affine symplectic group has a non-zero cohomology class.

## i. Overview

> Souriau (Structure des systemes dynamiques, Dunod 1970, chapter 11) attaches to a dynamical group
> `G` acting on a connected symplectic (or presymplectic) manifold `V` with moment `μ` a map
> `θ : G → 𝔤*`, `θ(a) = μ(a_V(x)) - a_{𝔤*}(μ(x))` (11.17 a), which by connectedness does not depend
> on `x` and satisfies the cocycle identity `θ(a × b) = θ(a) + a_{𝔤*}(θ(b))` (11.17 b). Its
> cohomology class does not depend on the choice of the moment (11.18), (11.20), and it vanishes
> when a `G`-invariant potential exists (11.21).
>
> This file proves the following for the group of Souriau's example (10.12), the affine symplectic
> group `Sp(E) ⋉ E` of a real symplectic vector space `E`, acting by `x ↦ B x + C`, with the moment
> `moment` of (11.7): the defect `θ(a)` does not depend on `x` and equals `μ(C)` (a computation here,
> not a consequence of connectedness), `θ` is a 1-cocycle of the coadjoint action, its derivative
> at the identity along a curve is the Lie algebra cocycle of
> `PhyslibAlpha.ClassicalMechanics.MomentMap.Basic`, and its cohomology class is not zero. It does NOT
> prove (11.18), (11.20) or (11.21): by (11.21) the non-zero class means that no potential of `σ` is
> invariant under this group, but that implication is Souriau's and is not formalised here.
>
> The Lie algebra is the space of pairs `(A, b)` with `A` infinitesimally symplectic, acting by the
> affine vector fields `Z_E(x) = A x + b`; only its module structure is used, and no Lean term
> relates it to `AffineSymplecticAction` (the link with its cocycle is by formula). The adjoint
> action is given by the formula of `adjoint` and characterised by the identity `vectorField_adjoint`
> of (6.25); the coadjoint action `a_{𝔤*}(μ) = μ ∘ Ad(a⁻¹)` of (11.15) is a `MulAction` on the
> dual.
>
> The cocycle notions are Mathlib's: `θ` is a `groupCohomology.IsCocycle₁` for the coadjoint action,
> and "the class is non-zero" is `¬ groupCohomology.IsCoboundary₁`. Souriau's differentiability
> requirement on `θ` is not formalised: the group here carries no manifold structure, and `θ` is
> given by a closed formula.

## ii. Key results

> - `vectorField_adjoint`: (6.25), `(Ad(a) Z)_E (a_E x) = B (Z_E x)`, which characterises `adjoint`
>   together with `vectorField_injective`.
> - `moment_smul_sub_smul_moment`: (11.17 a) in closed form, `μ(a_E(x)) - a_{𝔤*}(μ(x)) = μ(C)`: the
>   defect `θ(a)` does not depend on `x`, and is the moment at the point `a_E(0) = C`.
> - `isCocycle₁_moment_translation`: (11.17 b), `θ` is a 1-cocycle of the coadjoint action.
> - `hasDerivAt_moment_translation`: part of (11.17 c), the derivative of `θ` at the identity along a
>   curve whose translation part has velocity `b'` is `σ (b', b Z)`, the value of
>   `AffineSymplecticAction.cocycle` (the 2-form property and ♣ of (11.17 c) are not proved here).
> - `not_isCoboundary₁_moment_translation`: the cohomology class of the affine symplectic group is
>   non-zero as soon as `E ≠ 0`.

## iv. References

> - J.-M. Souriau, Structure des systemes dynamiques, Dunod, Paris, 1970: chapter 11,
>   pp. 104-117, for (11.7), (11.15)-(11.21) and (11.28); (6.24)-(6.25) and (10.12),
>   (10.28)-(10.32) for the adjoint action and the affine symplectic group.
>
> * J.-M. Souriau, *Structure des systèmes dynamiques*, Maîtrises de mathématiques, Dunod,
>   Paris, 1970, chapter 11, pp. 104-117, and (6.24)-(6.25), (10.12). The
>   equation numbers refer to this edition. [ref: Souriau1970]

## A. The affine symplectic group

> The affine symplectomorphisms `x ↦ B x + C` of (10.12), with `B` linear symplectic.

**`ClassicalMechanics.AffineSymplecticGroup`**, a structure, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L97).

> The affine symplectic group of a bilinear form `σ` on `E`: the affine maps `x ↦ B x + C` with
> `B` a linear equivalence preserving `σ` (Souriau (10.12)).

```lean
structure AffineSymplecticGroup {E : Type} [AddCommGroup E] [Module ℝ E]
    (σ : LinearMap.BilinForm ℝ E) where
  /-- The linear part `B`. -/
  linear : E ≃ₗ[ℝ] E
  /-- The translation part `C`. -/
  translation : E
  /-- The linear part preserves `σ`. -/
  map_symplecticForm : ∀ v w, σ (linear v) (linear w) = σ v w
```

**An instance with no name**, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L110).

```lean
instance : Mul (AffineSymplecticGroup σ)
```

**An instance with no name**, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L114).

```lean
instance : One (AffineSymplecticGroup σ)
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L116).

```lean
instance : Inv (AffineSymplecticGroup σ)
```

**`ClassicalMechanics.AffineSymplecticGroup.mul_linear`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L122).

```lean
lemma mul_linear (a b : AffineSymplecticGroup σ) : (a * b).linear = b.linear.trans a.linear
```

**`ClassicalMechanics.AffineSymplecticGroup.mul_translation`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L125).

```lean
lemma mul_translation (a b : AffineSymplecticGroup σ) :
    (a * b).translation = a.linear b.translation + a.translation
```

**`ClassicalMechanics.AffineSymplecticGroup.one_linear`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L129).

```lean
lemma one_linear : (1 : AffineSymplecticGroup σ).linear = LinearEquiv.refl ℝ E
```

**`ClassicalMechanics.AffineSymplecticGroup.one_translation`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L132).

```lean
lemma one_translation : (1 : AffineSymplecticGroup σ).translation = 0
```

**`ClassicalMechanics.AffineSymplecticGroup.inv_linear`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L135).

```lean
lemma inv_linear (a : AffineSymplecticGroup σ) : a⁻¹.linear = a.linear.symm
```

**`ClassicalMechanics.AffineSymplecticGroup.inv_translation`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L138).

```lean
lemma inv_translation (a : AffineSymplecticGroup σ) :
    a⁻¹.translation = -(a.linear.symm a.translation)
```

**`ClassicalMechanics.AffineSymplecticGroup.ext`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L143).

> Two elements with the same linear and translation parts are equal.

```lean
lemma ext {a b : AffineSymplecticGroup σ} (hl : a.linear = b.linear)
    (ht : a.translation = b.translation) : a = b
```

**An instance with no name**, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L149).

```lean
instance : Group (AffineSymplecticGroup σ)
```

**An instance with no name**, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L166).

> The affine symplectic group acts on `E` by `a_E(x) = B x + C` (10.12).

```lean
instance : MulAction (AffineSymplecticGroup σ) E
```

**`ClassicalMechanics.AffineSymplecticGroup.smul_def`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L176).

```lean
lemma smul_def (a : AffineSymplecticGroup σ) (x : E) : a • x = a.linear x + a.translation
```

## B. Its Lie algebra and the adjoint action

> The pairs `(A, b)` with `A` infinitesimally symplectic, acting by the affine vector fields
> `Z_E(x) = A x + b` of `AffineSymplecticAction`; the adjoint action of (6.24) is characterised by
> (6.25). Only the module structure is used here: the Lie bracket of Souriau's (11.22 a) lives on
> the abstract Lie algebra of `AffineSymplecticAction`.

**`ClassicalMechanics.affineSymplecticAlgebra`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L195).

> The Lie algebra of the affine symplectic group: the pairs `(A, b)` with `A` infinitesimally
> symplectic ((10.28)-(10.32)).

```lean
def affineSymplecticAlgebra (σ : LinearMap.BilinForm ℝ E) : Submodule ℝ ((E →ₗ[ℝ] E) × E)
```

**`ClassicalMechanics.mem_affineSymplecticAlgebra`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L214).

```lean
lemma mem_affineSymplecticAlgebra {Z : (E →ₗ[ℝ] E) × E} :
    Z ∈ affineSymplecticAlgebra σ ↔ ∀ v w, σ (Z.1 v) w + σ v (Z.1 w) = 0
```

**`ClassicalMechanics.vectorField`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L218).

> The affine vector field `Z_E(x) = A x + b` of `Z = (A, b)`, as in `AffineSymplecticAction`.

```lean
def vectorField (Z : affineSymplecticAlgebra σ) (x : E) : E
```

**`ClassicalMechanics.adjoint`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L221).

> The adjoint action (6.24): `Ad(a)(A, b) = (B A B⁻¹, B b - B A B⁻¹ C)` for `a = (B, C)`.

```lean
def adjoint (a : AffineSymplecticGroup σ) :
    affineSymplecticAlgebra σ →ₗ[ℝ] affineSymplecticAlgebra σ
```

**`ClassicalMechanics.adjoint_one`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L243).

```lean
lemma adjoint_one : adjoint (1 : AffineSymplecticGroup σ) = LinearMap.id
```

**`ClassicalMechanics.adjoint_mul`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L248).

```lean
lemma adjoint_mul (a b : AffineSymplecticGroup σ) :
    adjoint (a * b) = adjoint a ∘ₗ adjoint b
```

**`ClassicalMechanics.vectorField_adjoint`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L262).

> (6.25): the adjoint action is the one for which `(Ad(a) Z)_E (a_E x) = B (Z_E x)`. With
> `vectorField_injective` this characterises `adjoint`.

```lean
lemma vectorField_adjoint (a : AffineSymplecticGroup σ) (Z : affineSymplecticAlgebra σ) (x : E) :
    vectorField (adjoint a Z) (a • x) = a.linear (vectorField Z x)
```

**`ClassicalMechanics.vectorField_injective`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L277).

> An element of the Lie algebra is determined by its vector field.

```lean
lemma vectorField_injective {Z Z' : affineSymplecticAlgebra σ}
    (h : ∀ x, vectorField Z x = vectorField Z' x) : Z = Z'
```

## C. The coadjoint action and the moment

> The coadjoint action of (11.15), `a_{𝔤*}(μ) = μ ∘ Ad(a⁻¹)`, and the moment of (11.7), which is the
> moment of `AffineSymplecticAction` read on the pairs `(A, b)`.

**An instance with no name**, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L297).

> (11.15): the coadjoint action `a_{𝔤*}(μ) = μ.a_𝔤⁻¹`, that is `μ ∘ Ad(a⁻¹)`.

```lean
instance : SMul (AffineSymplecticGroup σ) (Dual ℝ (affineSymplecticAlgebra σ))
```

**`ClassicalMechanics.coadjoint_smul_apply`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L301).

```lean
lemma coadjoint_smul_apply (a : AffineSymplecticGroup σ) (μ : Dual ℝ (affineSymplecticAlgebra σ))
    (Z : affineSymplecticAlgebra σ) : (a • μ) Z = μ (adjoint a⁻¹ Z)
```

**An instance with no name**, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L304).

```lean
instance : MulAction (AffineSymplecticGroup σ) (Dual ℝ (affineSymplecticAlgebra σ))
```

**An instance with no name**, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L312).

```lean
instance : DistribMulAction (AffineSymplecticGroup σ) (Dual ℝ (affineSymplecticAlgebra σ))
```

**`ClassicalMechanics.moment`**, a def, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L322).

> (11.7): the moment of the affine symplectic action, `μ(x)(A, b) = -½ σ(A x, x) - σ(b, x)`, the
> moment of `AffineSymplecticAction` read on the pairs `(A, b)`.

```lean
def moment (σ : LinearMap.BilinForm ℝ E) (x : E) : Dual ℝ (affineSymplecticAlgebra σ)
```

**`ClassicalMechanics.moment_apply`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L333).

```lean
lemma moment_apply (x : E) (Z : affineSymplecticAlgebra σ) :
    moment σ x Z = -(1 / 2 : ℝ) * σ (Z.1.1 x) x - σ Z.1.2 x
```

**`ClassicalMechanics.moment_zero`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L337).

```lean
lemma moment_zero : moment σ (0 : E) = 0
```

## D. The cohomology class

> (11.17 a) in closed form, (11.17 b), (11.17 c) and the non-vanishing of the class.

**`ClassicalMechanics.moment_smul_sub_smul_moment`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L352).

> (11.17 a) in closed form: for this moment, the defect `θ(a) = μ(a_E(x)) - a_{𝔤*}(μ(x))` does
> not depend on the point `x`, and equals the moment at `a_E(0) = C`. The terms in `x` cancel by the
> infinitesimal symplecticity of `A` and the alternation of `σ`.

```lean
lemma moment_smul_sub_smul_moment (hσ : IsSymplecticForm σ) (x : E)
    (a : AffineSymplecticGroup σ) :
    moment σ (a • x) - a • moment σ x = moment σ a.translation
```

**`ClassicalMechanics.isCocycle₁_moment_translation`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L373).

> (11.17 b): `θ(a) = μ(C)` is a 1-cocycle of the coadjoint action,
> `θ(a × b) = θ(a) + a_{𝔤*}(θ(b))`.

```lean
lemma isCocycle₁_moment_translation (hσ : IsSymplecticForm σ) :
    groupCohomology.IsCocycle₁ (fun a : AffineSymplecticGroup σ => moment σ a.translation)
```

**`ClassicalMechanics.sigmaLinear`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L387).

> `y ↦ σ (A y)` as a continuous linear map from `E` to `E →L[ℝ] ℝ`, used to differentiate the
> quadratic part of the moment.

```lean
def sigmaLinear {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
    (σ : LinearMap.BilinForm ℝ E) (A : E →ₗ[ℝ] E) : E →L[ℝ] (E →L[ℝ] ℝ)
```

**`ClassicalMechanics.sigmaLinear_apply`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L393).

```lean
lemma sigmaLinear_apply {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E] (σ : LinearMap.BilinForm ℝ E) (A : E →ₗ[ℝ] E) (y v : E) :
    sigmaLinear σ A y v = σ (A y) v
```

**`ClassicalMechanics.hasFDerivAt_quad`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L399).

> The derivative of `y ↦ σ (A y) y` at `x` is `v ↦ σ (A v) x + σ (A x) v`.

```lean
lemma hasFDerivAt_quad {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E] (σ : LinearMap.BilinForm ℝ E) (A : E →ₗ[ℝ] E) (x : E) :
    HasFDerivAt (fun y => σ (A y) y)
      ((sigmaLinear σ A x).comp (ContinuousLinearMap.id ℝ E) + (sigmaLinear σ A).flip x) x
```

**`ClassicalMechanics.hasFDerivAt_moment`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L409).

> (11.7) for the affine symplectic group: `σ(Z_E(x)) = -∇[μ.Z]`.

```lean
lemma hasFDerivAt_moment {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E] {σ : LinearMap.BilinForm ℝ E} (hσ : IsSymplecticForm σ)
    (Z : affineSymplecticAlgebra σ) (x : E) :
    HasFDerivAt (fun y => moment σ y Z)
      (-(LinearMap.toContinuousLinearMap (σ (vectorField Z x)))) x
```

**`ClassicalMechanics.hasDerivAt_moment_translation`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L430).

> Part of (11.17 c): along any curve of the group issued from the identity whose translation part
> has velocity `b'`, the derivative of `θ = μ(C)` at the identity is `σ (b', b Z)`, which is the value
> of `AffineSymplecticAction.cocycle` on the corresponding pairs (a relation by formula: no Lean term
> relates the two Lie algebras).

```lean
lemma hasDerivAt_moment_translation {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E] {σ : LinearMap.BilinForm ℝ E} (hσ : IsSymplecticForm σ)
    (γ : ℝ → AffineSymplecticGroup σ) (hγ : γ 0 = 1) (b' : E)
    (hC : HasDerivAt (fun t => (γ t).translation) b' 0) (Z : affineSymplecticAlgebra σ) :
    HasDerivAt (fun t => moment σ (γ t).translation Z) (σ b' Z.1.2) 0
```

**`ClassicalMechanics.not_isCoboundary₁_moment_translation`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L448).

> The cohomology class of the affine symplectic group of a non-zero symplectic vector space is
> NOT zero: `θ` is not a coboundary. On the translations `(id, C)` the coadjoint action fixes the
> elements `(0, b)` of the Lie algebra, so every coboundary vanishes on them, whereas
> `θ((id, C))(0, b) = -σ (b, C)`, which is non-zero for a suitable `b` by non-degeneracy. (By
> Souriau's (11.21) this forbids a potential of `σ` invariant under the group; that implication is
> not formalised here.)

```lean
lemma not_isCoboundary₁_moment_translation (hσ : IsSymplecticForm σ) (hE : ∃ v : E, v ≠ 0) :
    ¬ groupCohomology.IsCoboundary₁
      (fun a : AffineSymplecticGroup σ => moment σ a.translation)
```

## E. The plane

> The simplest instance: the standard symplectic plane, whose affine symplectic group has a non-zero
> cohomology class. This is the group-level counterpart of `planeTranslations_not_coboundary`.

**`ClassicalMechanics.planeForm_not_isCoboundary₁`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean#L481).

> The affine symplectic group of the symplectic plane has a non-zero cohomology class.

```lean
lemma planeForm_not_isCoboundary₁ :
    ¬ groupCohomology.IsCoboundary₁
      (fun a : AffineSymplecticGroup planeForm => moment planeForm a.translation)
```

## Depends on

- [Souriau's moment map on a symplectic vector space](basic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Cohomology.lean)
