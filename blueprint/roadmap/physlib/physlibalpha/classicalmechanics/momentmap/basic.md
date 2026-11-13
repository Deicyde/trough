---
declaration: module
origin: cited
lean: ClassicalMechanics.IsSymplecticForm, ClassicalMechanics.AffineSymplecticAction, ClassicalMechanics.coadjoint, ClassicalMechanics.AffineSymplecticAction.vectorField, ClassicalMechanics.AffineSymplecticAction.moment, ClassicalMechanics.AffineSymplecticAction.cocycle, ClassicalMechanics.AffineSymplecticAction.sigma_A_left, ClassicalMechanics.AffineSymplecticAction.sigma_A_right
statement: formalized
proof: formalized
---

# Souriau's moment map on a symplectic vector space

The module `PhyslibAlpha.ClassicalMechanics.MomentMap.Basic`, [PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean): 40 declarations, 38 with a docstring.

> Souriau's moment map, cocycle and Noether theorem for affine actions on a symplectic space.

## i. Overview

> Souriau (Structure des systèmes dynamiques, Dunod 1970, chapter 11) attaches to a Lie group `G`
> acting on a symplectic manifold `V` by symplectomorphisms (a *dynamical group*) a *moment*
> `μ : V → 𝔤*`, defined by `σ(Z_V(x)) = -∇[μ.Z]` for every `Z` in the Lie algebra (11.7). Two moments
> differ by a constant (11.8 a); the moment is constant along the motions (Noether's theorem, 11.12);
> and the moment fails to be equivariant for the coadjoint action by a *symplectic cocycle* `θ` whose
> derivative `f` is a 2-form on `𝔤` satisfying `σ(Z_V)(Z'_V) = μ[Z, Z'] + f(Z)(Z')` (11.17 d) and the
> cyclic identity (11.33). The cohomology class of `θ` is an invariant of the dynamical group; it is
> zero when a `G`-invariant potential of `σ` exists (11.21) and for semisimple groups (11.27).
>
> This file states and proves these results in the setting of Souriau's example (11.2): a real
> finite-dimensional symplectic vector space `E` on which a real Lie algebra `𝔤` acts by *affine*
> infinitesimally symplectic vector fields `Z_E(x) = A Z x + b Z` (the infinitesimal version of the
> affine symplectomorphisms `x ↦ B x + C` of (10.12)). No manifold is involved: the moment is given
> explicitly by `μ.Z (x) = -½ σ(A Z x, x) - σ(b Z, x)`, the cocycle by `f(Z)(Z') = σ(b Z, b Z')`, and
> Noether's theorem is stated for a Hamiltonian flow on `E`.
>
> All signs follow Souriau's printed conventions: the bracket of the Lie algebra is the one for which
> `Z ↦ Z_E` is a homomorphism for the bracket `[Z, Z']_E = Z'_E ∘ Z_E - Z_E ∘ Z'_E` of (11.22 a)
> (opposite to the usual commutator), `Ad(Z)(Z') = [Z, Z']` (6.13 b), and the coadjoint vector
> field is `Z_{𝔤*}(ν) = ν ∘ Ad(Z)` (11.16).

## ii. Key results

> - `AffineSymplecticAction.hasFDerivAt_moment`: (11.7), `σ(Z_E(x)) = -∇[μ.Z]`.
> - `AffineSymplecticAction.moment_unique`: (11.8 a), two moments differ by a constant torsor; this is
>   proved without the alternation of `σ`, from the symmetry of the second derivative of the given
>   moment.
> - `AffineSymplecticAction.sigma_vectorField_vectorField`: (11.17 d),
>   `σ(Z_E)(Z'_E) = μ[Z, Z'] + f(Z)(Z')`.
> - `AffineSymplecticAction.cocycle_cyclic`: (11.33), the cyclic identity of the symplectic cocycle.
> - `AffineSymplecticAction.equivariant_of_coboundary`: (11.27) in this setting, a coboundary cocycle
>   can be absorbed in the moment.
> - `AffineSymplecticAction.noether`: (11.12), `μ.Z` is a first integral of every `Z_E`-invariant
>   Hamiltonian flow.
> - `planeTranslations_not_coboundary`: the translations of the plane have a non-zero cohomology class
>   (the simplest instance of Souriau's "mass" cocycle).

## iv. References

> - J.-M. Souriau, Structure des systèmes dynamiques, Dunod, Paris, 1970, chapter 11,
>   pp. 104-117; English translation: Structure of Dynamical Systems, Birkhäuser, 1997
>   (same equation numbers).
>
> * J.-M. Souriau, *Structure des systèmes dynamiques*, Maîtrises de mathématiques, Dunod,
>   Paris, 1970, chapter 11, pp. 104-117. The equation numbers (11.7),
>   (11.8), (11.12), (11.17), (11.22), (11.27), (11.33) refer to this edition. [ref: Souriau1970]

## A. Symplectic forms

> Souriau's "forme de Lagrange" `σ` is an alternating non-degenerate bilinear form.

**`ClassicalMechanics.IsSymplecticForm`**, a structure, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L95).

> A symplectic form on a real vector space: an alternating non-degenerate bilinear form.

```lean
structure IsSymplecticForm {E : Type} [AddCommGroup E] [Module ℝ E] (σ : LinearMap.BilinForm ℝ E) :
    Prop where
  /-- `σ` is alternating: `σ v v = 0`. -/
  alt : LinearMap.BilinForm.IsAlt σ
  /-- `σ` is non-degenerate. -/
  nondeg : LinearMap.BilinForm.Nondegenerate σ
```

## B. Affine symplectic actions of a Lie algebra

> The infinitesimal version of Souriau's example (11.2) with the affine symplectomorphisms of (10.12):
> each `Z` of the Lie algebra acts on `E` by the affine vector field `Z_E(x) = A Z x + b Z`, with
> `A Z` infinitesimally symplectic ((10.28)-(10.32)), and the bracket is Souriau's (6.12 b),
> (11.22 a): `[Z, Z']_E = Z'_E ∘ Z_E - Z_E ∘ Z'_E`, extended to affine vector fields by the formula
> `[X, X'](x) = DX'(x)(X(x)) - DX(x)(X'(x))`.

**`ClassicalMechanics.AffineSymplecticAction`**, a structure, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L116).

> An affine infinitesimally symplectic action of a Lie algebra `g` on `E`, in Souriau's
> conventions: `Z_E(x) = A Z x + b Z`.

```lean
structure AffineSymplecticAction {E : Type} [AddCommGroup E] [Module ℝ E]
    (σ : LinearMap.BilinForm ℝ E) (g : Type) [LieRing g] [LieAlgebra ℝ g] where
  /-- The linear part `Z ↦ A Z` of the vector fields. -/
  A : g →ₗ[ℝ] (E →ₗ[ℝ] E)
  /-- The constant part `Z ↦ b Z` of the vector fields. -/
  b : g →ₗ[ℝ] E
  /-- Each `A Z` is infinitesimally symplectic: `σ (A Z v) w + σ v (A Z w) = 0`. -/
  infinitesimallySymplectic : ∀ Z v w, σ (A Z v) w + σ v (A Z w) = 0
  /-- Souriau's bracket (11.22 a) on the linear parts: `A [Z, Z'] = A Z' ∘ A Z - A Z ∘ A Z'`. -/
  map_bracket_A : ∀ Z Z', A ⁅Z, Z'⁆ = A Z' ∘ₗ A Z - A Z ∘ₗ A Z'
  /-- Souriau's bracket on the constant parts: `b [Z, Z'] = A Z' (b Z) - A Z (b Z')`. -/
  map_bracket_b : ∀ Z Z', b ⁅Z, Z'⁆ = A Z' (b Z) - A Z (b Z')
```

**`ClassicalMechanics.coadjoint`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L132).

> (11.16) with (6.13 b): the coadjoint vector field `Z_{𝔤*}(ν) = ν ∘ Ad(Z)`,
> `Ad(Z)(Z') = [Z, Z']`, for a torsor `ν` given as a function; this is also the coboundary
> `δ(ν)(Z)` of (11.24).

```lean
def coadjoint {g : Type} [LieRing g] (Z : g) (ν : g → ℝ) (Z' : g) : ℝ
```

**`ClassicalMechanics.AffineSymplecticAction.vectorField`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L141).

> (6.11): the affine vector field `Z_E` associated with `Z`.

```lean
def vectorField (Z : g) (x : E) : E
```

**`ClassicalMechanics.AffineSymplecticAction.moment`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L145).

> The moment (11.7), (11.9) of the action, as a function of the point `x` and of `Z`:
> `μ.Z (x) = -½ σ(A Z x, x) - σ(b Z, x)`. Its sign is fixed by (11.7).

```lean
def moment (x : E) (Z : g) : ℝ
```

**`ClassicalMechanics.AffineSymplecticAction.cocycle`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L148).

> (11.17 c): Souriau's cocycle `f(Z)(Z') = σ(b Z, b Z')`, a 2-form on `g`.

```lean
def cocycle (Z Z' : g) : ℝ
```

**`ClassicalMechanics.AffineSymplecticAction.sigma_A_left`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L151).

> `infinitesimallySymplectic` in the form `σ (A Z v) w = -σ v (A Z w)`.

```lean
lemma sigma_A_left (Z : g) (v w : E) : σ (ρ.A Z v) w = -σ v (ρ.A Z w)
```

**`ClassicalMechanics.AffineSymplecticAction.sigma_A_right`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L155).

> `infinitesimallySymplectic` in the form `σ v (A Z w) = -σ (A Z v) w`.

```lean
lemma sigma_A_right (Z : g) (v w : E) : σ v (ρ.A Z w) = -σ (ρ.A Z v) w
```

**`ClassicalMechanics.AffineSymplecticAction.sigma_A_symm`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L159).

> For an alternating `σ`, `σ (A Z v) w` is symmetric in `v`, `w`.

```lean
lemma sigma_A_symm (hσ : IsSymplecticForm σ) (Z : g) (v w : E) :
    σ (ρ.A Z v) w = σ (ρ.A Z w) v
```

**`ClassicalMechanics.AffineSymplecticAction.moment_add`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L164).

> The moment is a torsor: `μ.(Z + Z') = μ.Z + μ.Z'`.

```lean
lemma moment_add (x : E) (Z Z' : g) : ρ.moment x (Z + Z') = ρ.moment x Z + ρ.moment x Z'
```

**`ClassicalMechanics.AffineSymplecticAction.moment_smul`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L169).

> The moment is a torsor: `μ.(c Z) = c μ.Z`.

```lean
lemma moment_smul (x : E) (c : ℝ) (Z : g) : ρ.moment x (c • Z) = c * ρ.moment x Z
```

## C. The Souriau cocycle

> (11.17 d, ♯), (11.30), (11.33), the Lie algebra cocycle identity (11.22)/(11.24), the change of
> moment (11.18), the coboundary case (11.27) and the linear case (11.21). Everything here is algebra:
> only the bilinearity and the alternation of `σ` and the axioms of the action are used.

**`ClassicalMechanics.AffineSymplecticAction.sigma_vectorField_vectorField`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L184).

> (11.17 d, ♯): `σ(Z_E(x))(Z'_E(x)) = μ[Z, Z'](x) + f(Z)(Z')`.

```lean
lemma sigma_vectorField_vectorField (hσ : IsSymplecticForm σ) (Z Z' : g) (x : E) :
    σ (ρ.vectorField Z x) (ρ.vectorField Z' x) = ρ.moment x ⁅Z, Z'⁆ + ρ.cocycle Z Z'
```

**`ClassicalMechanics.AffineSymplecticAction.cocycle_antisymm`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L199).

> (11.30): the cocycle is antisymmetric.

```lean
lemma cocycle_antisymm (hσ : IsSymplecticForm σ) (Z Z' : g) :
    ρ.cocycle Z' Z = -ρ.cocycle Z Z'
```

**`ClassicalMechanics.AffineSymplecticAction.cocycle_cyclic`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L205).

> (11.33): the cyclic identity `f(Z)([Z', Z'']) + f(Z')([Z'', Z]) + f(Z'')([Z, Z']) = 0`.

```lean
lemma cocycle_cyclic (hσ : IsSymplecticForm σ) (Z Z' Z'' : g) :
    ρ.cocycle Z ⁅Z', Z''⁆ + ρ.cocycle Z' ⁅Z'', Z⁆ + ρ.cocycle Z'' ⁅Z, Z'⁆ = 0
```

**`ClassicalMechanics.AffineSymplecticAction.cocycle_lie`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L220).

> (11.22)/(11.24) for the coadjoint representation: `f` is a Lie algebra cocycle,
> `f([Z, Z']) = Z'_{𝔤*}(f(Z)) - Z_{𝔤*}(f(Z'))`, evaluated on `Z''`.

```lean
lemma cocycle_lie (hσ : IsSymplecticForm σ) (Z Z' Z'' : g) :
    ρ.cocycle ⁅Z, Z'⁆ Z'' = ρ.cocycle Z ⁅Z', Z''⁆ - ρ.cocycle Z' ⁅Z, Z''⁆
```

**`ClassicalMechanics.AffineSymplecticAction.sigma_vectorField_vectorField_shift`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L232).

> (11.18): changing the moment into `μ - μ₀` (`μ₀` a constant torsor) keeps (11.17 d) with the
> cocycle `f + Z_{𝔤*}(μ₀)`, i.e. `f(Z)(Z') + μ₀ [Z, Z']`.

```lean
lemma sigma_vectorField_vectorField_shift (hσ : IsSymplecticForm σ) (μ₀ : Dual ℝ g) (Z Z' : g)
    (x : E) :
    σ (ρ.vectorField Z x) (ρ.vectorField Z' x) =
      (ρ.moment x ⁅Z, Z'⁆ - μ₀ ⁅Z, Z'⁆) + (ρ.cocycle Z Z' + coadjoint Z μ₀ Z')
```

**`ClassicalMechanics.AffineSymplecticAction.equivariant_of_coboundary`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L242).

> (11.27) in this setting: if the cocycle is a coboundary, `f(Z)(Z') = μ₀ [Z, Z']`, then the
> moment `μ + μ₀` is exactly equivariant.

```lean
lemma equivariant_of_coboundary (hσ : IsSymplecticForm σ) (μ₀ : Dual ℝ g)
    (h : ∀ Z Z', ρ.cocycle Z Z' = coadjoint Z μ₀ Z') (Z Z' : g) (x : E) :
    σ (ρ.vectorField Z x) (ρ.vectorField Z' x) = ρ.moment x ⁅Z, Z'⁆ + μ₀ ⁅Z, Z'⁆
```

**`ClassicalMechanics.AffineSymplecticAction.cocycle_eq_zero_of_linear`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L250).

> (11.21) in this setting: a linear action (`b = 0`, the case (11.2) of `Sp(E)`) has a zero
> cocycle.

```lean
lemma cocycle_eq_zero_of_linear (hb : ρ.b = 0) (Z Z' : g) : ρ.cocycle Z Z' = 0
```

**`ClassicalMechanics.IsSymplecticGradient`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L257).

> The symplectic gradient (9.16) in the convention of (11.7) and (10.32): `X` is the symplectic
> gradient of `u` when `σ (X x) v = -Du(x)(v)` for all `x`, `v`.

```lean
def IsSymplecticGradient {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (σ : LinearMap.BilinForm ℝ E) (u : E → ℝ) (X : E → E) : Prop
```

## D. The moment map

> (11.7), (11.9) and (11.8 a), then the infinitesimal equivariance (11.17 d, ♠) and the identity
> (11.8 c). The derivative of `y ↦ σ (A y) y` is computed by viewing `y ↦ σ (A y)` as a continuous
> linear map into `E →L[ℝ] ℝ`.

**`ClassicalMechanics.AffineSymplecticAction.sigmaA`**, a def, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L278).

> `y ↦ σ (A Z y)` as a continuous linear map from `E` to `E →L[ℝ] ℝ`.

```lean
def sigmaA (Z : g) : E →L[ℝ] (E →L[ℝ] ℝ)
```

**`ClassicalMechanics.AffineSymplecticAction.sigmaA_apply`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L283).

```lean
lemma sigmaA_apply (Z : g) (y v : E) : ρ.sigmaA Z y v = σ (ρ.A Z y) v
```

**`ClassicalMechanics.AffineSymplecticAction.sigmaB`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L287).

> The constant linear form `σ (b Z)` as a continuous linear map.

```lean
def sigmaB (Z : g) : E →L[ℝ] ℝ
```

**`ClassicalMechanics.AffineSymplecticAction.sigmaB_apply`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L290).

```lean
lemma sigmaB_apply (Z : g) (v : E) : ρ.sigmaB Z v = σ (ρ.b Z) v
```

**`ClassicalMechanics.AffineSymplecticAction.hasFDerivAt_quad`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L294).

> The derivative of `y ↦ σ (A Z y) y` at `x` is `v ↦ σ (A Z v) x + σ (A Z x) v`.

```lean
lemma hasFDerivAt_quad (Z : g) (x : E) :
    HasFDerivAt (fun y => σ (ρ.A Z y) y)
      ((ρ.sigmaA Z x).comp (ContinuousLinearMap.id ℝ E) + (ρ.sigmaA Z).flip x) x
```

**`ClassicalMechanics.AffineSymplecticAction.hasFDerivAt_moment_of_symm`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L304).

> (11.7) under the sole symmetry `σ (A Z v) w = σ (A Z w) v`.

```lean
lemma hasFDerivAt_moment_of_symm (Z : g) (hsym : ∀ v w, σ (ρ.A Z v) w = σ (ρ.A Z w) v) (x : E) :
    HasFDerivAt (fun y => ρ.moment y Z)
      (-(LinearMap.toContinuousLinearMap (σ (ρ.vectorField Z x)))) x
```

**`ClassicalMechanics.AffineSymplecticAction.hasFDerivAt_moment`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L318).

> (11.7): `σ(Z_E(x)) = -∇[μ.Z]`, the derivative of `x ↦ μ.Z` at `x` is `v ↦ -σ (Z_E x) v`.

```lean
lemma hasFDerivAt_moment (hσ : IsSymplecticForm σ) (Z : g) (x : E) :
    HasFDerivAt (fun y => ρ.moment y Z)
      (-(LinearMap.toContinuousLinearMap (σ (ρ.vectorField Z x)))) x
```

**`ClassicalMechanics.AffineSymplecticAction.vectorField_isSymplecticGradient`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L324).

> (11.9): `Z_E` is the symplectic gradient of `μ.Z`.

```lean
lemma vectorField_isSymplecticGradient (hσ : IsSymplecticForm σ) (Z : g) :
    IsSymplecticGradient σ (fun y => ρ.moment y Z) (ρ.vectorField Z)
```

**`ClassicalMechanics.AffineSymplecticAction.hasFDerivAt_negSigmaVectorField`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L331).

> The derivative of the affine map `x ↦ -σ (Z_E x)` (with values in `E →L[ℝ] ℝ`) is `-sigmaA`.

```lean
lemma hasFDerivAt_negSigmaVectorField (Z : g) (x : E) :
    HasFDerivAt (fun y => -(LinearMap.toContinuousLinearMap (σ (ρ.vectorField Z y))))
      (-(ρ.sigmaA Z)) x
```

**`ClassicalMechanics.AffineSymplecticAction.moment_unique`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L343).

> (11.8 a): two moments of the same action differ by a constant torsor (`E` is connected). Any `ψ`
> satisfying (11.7) equals `μ + c`, `Z` by `Z`. No alternation of `σ` is needed: the symmetry of the
> second derivative of `ψ` gives `σ (A Z v) w = σ (A Z w) v`.

```lean
lemma moment_unique (ψ : E → g → ℝ)
    (hψ : ∀ Z x, HasFDerivAt (fun y => ψ y Z)
      (-(LinearMap.toContinuousLinearMap (σ (ρ.vectorField Z x)))) x) (Z : g) :
    ∃ c : ℝ, ∀ x, ψ x Z = ρ.moment x Z + c
```

**`ClassicalMechanics.AffineSymplecticAction.fderiv_moment_vectorField`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L365).

> (11.17 d, ♠): `D(ψ)(x)(Z_E(x)) = ψ(x).ad(Z) + f(Z)`, evaluated on `Z'`: the infinitesimal
> equivariance of the moment, up to the cocycle.

```lean
lemma fderiv_moment_vectorField (hσ : IsSymplecticForm σ) (Z Z' : g) (x : E) :
    fderiv ℝ (fun y => ρ.moment y Z') x (ρ.vectorField Z x) =
      coadjoint Z (ρ.moment x) Z' + ρ.cocycle Z Z'
```

**`ClassicalMechanics.AffineSymplecticAction.sigma_vectorField_bracket`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L376).

> (11.8 c): `σ([Z, Z']_E(x)) = -∇[σ(Z_E(x))(Z'_E(x))]`, an identity valid for every dynamical
> group.

```lean
lemma sigma_vectorField_bracket (hσ : IsSymplecticForm σ) (Z Z' : g) (x v : E) :
    σ (ρ.vectorField ⁅Z, Z'⁆ x) v =
      -(fderiv ℝ (fun y => σ (ρ.vectorField Z y) (ρ.vectorField Z' y)) x v)
```

## E. Noether's theorem

> (11.12) states that a moment is constant on each leaf of the presymplectic evolution space. On `E`,
> for a Hamiltonian flow `γ' = X ∘ γ` with `X` the symplectic gradient of an `H` invariant under
> `Z_E`, this says that `μ.Z ∘ γ` is constant.

**`ClassicalMechanics.AffineSymplecticAction.noether`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L414).

> (11.12), Noether's theorem: along a motion of a Hamiltonian `H` invariant under `Z_E`, the
> component `μ.Z` of the moment has zero derivative.

```lean
lemma noether (hσ : IsSymplecticForm σ) (H : E → ℝ) (X : E → E) (hX : IsSymplecticGradient σ H X)
    (Z : g) (hinv : ∀ x, fderiv ℝ H x (ρ.vectorField Z x) = 0)
    (γ : ℝ → E) (hγ : ∀ t, HasDerivAt γ (X (γ t)) t) (t : ℝ) :
    HasDerivAt (fun s => ρ.moment (γ s) Z) 0 t
```

**`ClassicalMechanics.AffineSymplecticAction.noether_const`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L429).

> (11.12) as a conservation law: `μ.Z` takes the same value at any two instants of a motion.

```lean
lemma noether_const (hσ : IsSymplecticForm σ) (H : E → ℝ) (X : E → E)
    (hX : IsSymplecticGradient σ H X) (Z : g) (hinv : ∀ x, fderiv ℝ H x (ρ.vectorField Z x) = 0)
    (γ : ℝ → E) (hγ : ∀ t, HasDerivAt γ (X (γ t)) t) (t s : ℝ) :
    ρ.moment (γ t) Z = ρ.moment (γ s) Z
```

## F. The plane: translations and a non-trivial cohomology class

> The standard symplectic form of `ℝ × ℝ` and the translations `x ↦ x + Z`, whose vector fields are
> constant, `Z_E(x) = Z`: their cocycle is `σ(Z, Z')` itself, which is not a coboundary (the Lie
> algebra is abelian, so every coboundary vanishes). This is the simplest instance of (11.20)-(11.21):
> no invariant potential exists, and no moment of the translations is equivariant.

**`ClassicalMechanics.instLieRingPlane`**, an instance, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L451).

> `ℝ × ℝ` as an abelian Lie ring (the commutator bracket of the product ring, which vanishes).

```lean
instance instLieRingPlane : LieRing (ℝ × ℝ)
```

**`ClassicalMechanics.instLieAlgebraPlane`**, an instance, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L454).

> `ℝ × ℝ` as an abelian real Lie algebra.

```lean
instance instLieAlgebraPlane : LieAlgebra ℝ (ℝ × ℝ)
```

**`ClassicalMechanics.planeForm`**, a def, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L457).

> The standard symplectic form of the plane, `σ((a, b), (c, d)) = a d - b c`.

```lean
def planeForm : LinearMap.BilinForm ℝ (ℝ × ℝ)
```

**`ClassicalMechanics.planeTranslations`**, a def, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L465).

> The translations `x ↦ x + Z` of the plane: `A = 0`, `b = id`, so `Z_E(x) = Z`.

```lean
def planeTranslations : AffineSymplecticAction planeForm (ℝ × ℝ)
```

**`ClassicalMechanics.isSymplecticForm_planeForm`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L473).

> `planeForm` is symplectic.

```lean
lemma isSymplecticForm_planeForm : IsSymplecticForm planeForm
```

**`ClassicalMechanics.planeTranslations_cocycle`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L489).

> (11.17 c), (11.20): for the translations of the plane the cocycle is `σ(Z, Z')`, so
> `f((1, 0))((0, 1)) = 1`.

```lean
lemma planeTranslations_cocycle : planeTranslations.cocycle (1, 0) (0, 1) = 1
```

**`ClassicalMechanics.planeTranslations_not_coboundary`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean#L494).

> (11.21): the cocycle of the translations is not a coboundary: the cohomology class of the
> translations of the plane is not zero.

```lean
lemma planeTranslations_not_coboundary :
    ¬ ∃ μ₀ : Dual ℝ (ℝ × ℝ), ∀ Z Z', planeTranslations.cocycle Z Z' = coadjoint Z μ₀ Z'
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/Basic.lean)
