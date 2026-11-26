---
declaration: module
origin: cited
lean: GlobalGaugeGroup.instCompleteSpaceW, GlobalGaugeGroup.derivRepFun, GlobalGaugeGroup.derivRep_oneParameterSubgroup, GlobalGaugeGroup.derivRep_oneParameterSubgroup_inv, GlobalGaugeGroup.derivRepFun_eq, GlobalGaugeGroup.derivRepFun_smul, GlobalGaugeGroup.derivRepFun_add, GlobalGaugeGroup.derivRepLinear
statement: formalized
proof: formalized
---

# The derivative of a representation of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.DerivRep`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean): 25 declarations, 22 with a docstring.

> A continuous representation `ρ : G → GL(W)` of a global gauge group differentiates to a
> representation `dρ` of its Lie algebra by linear maps on `W`.

## i. Overview

> A continuous representation `ρ` of the global gauge group `G` on a finite-dimensional complex
> normed space `W` is differentiated to the corresponding representation of the Lie algebra, which
> is how gauge fields act on matter. For a generator `X` of `G` this is the derivative
> `dρ(X) = d/dt ρ (exp (t X))` at `t = 0`, a linear map on `W`. The matter field `M` of a gauge
> theory carries such a representation `M.rep`, and its Lie algebra representation is the
> derivative of `M.rep`.
>
> The linear maps `W →L[ℂ] W` form a Banach algebra, and the image `t ↦ ρ (exp (t X))` of a
> one-parameter subgroup is a continuous one-parameter subgroup of it. So it is
> `t ↦ exp (t dρ(X))`, by `OneParameterSubgroup.apply_eq_exp_smul_deriv`, and `dρ(X)` is the
> only linear map with this property, by `OneParameterSubgroup.generator_unique`. The map `dρ`
> is a homomorphism of Lie algebras.
>
> * It is real-linear. Compatibility with scalars is a reparametrisation of `t`, and
>   additivity follows by applying `ρ` to the Lie product formula
>   `exp (t (X + Y)) = lim (exp (t X / n) exp (t Y / n)) ^ n`.
> * It intertwines the adjoint actions, `dρ(g X g⁻¹) = ρ(g) dρ(X) ρ(g)⁻¹`, since `ρ` maps
>   the one-parameter subgroup of `g X g⁻¹` to the conjugate of that of `X`.
> * It preserves the commutator. With `g = exp (s X)`, the intertwining property reads
>   `dρ(exp (s X) Y exp (−s X)) = exp (s dρ(X)) dρ(Y) exp (−s dρ(X))`. Both sides are
>   differentiable in `s`, `dρ` being linear on a finite-dimensional space. Their derivatives
>   at `s = 0` are `dρ(X Y − Y X)` and `dρ(X) dρ(Y) − dρ(Y) dρ(X)`.
>
> The one-parameter subgroups `GlobalGaugeGroup.oneParameterSubgroup` and the adjoint action
> `GlobalGaugeGroup.adjoint` of `G` are set up in the `LieAlgebra` directory.

## ii. Key results

> - `GlobalGaugeGroup.derivRepFun` : the derivative `dρ(X)` of a representation along a
>   generator.
> - `GlobalGaugeGroup.derivRep` : the Lie algebra representation.
> - `GlobalGaugeGroup.apply_eq_exp_derivRep` : `ρ (exp (t X)) = exp (t dρ(X))`.
> - `GlobalGaugeGroup.derivRep_eq_of` : `dρ(X)` is the unique linear map with this property.
> - `GlobalGaugeGroup.derivRep_adjoint` : `dρ` intertwines the adjoint actions.
> - `GlobalGaugeGroup.commute_derivRep` : a linear map commuting with `ρ` commutes with `dρ`.
> - `GlobalGaugeGroup.MatterField.lieAlgebraRep` : the Lie algebra representation of a matter
>   field, the derivative of its representation.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

**`GlobalGaugeGroup.instCompleteSpaceW`**, an instance, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L84).

> A finite-dimensional complex normed space is complete.

```lean
local instance instCompleteSpaceW : CompleteSpace W
```

## A. The derivative of a representation along a generator

**`GlobalGaugeGroup.derivRepFun`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L94).

> The derivative `dρ(X) = d/dt ρ (exp (t X))` at `t = 0` of the representation along a
> generator `X` of the global gauge group, a linear map on the target space.

```lean
noncomputable def derivRepFun (X : G.lieAlgebra) : W →L[ℂ] W
```

**`GlobalGaugeGroup.derivRep_oneParameterSubgroup`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L100).

> The representation maps the one-parameter subgroup of a generator `X` to that of its
> derivative `dρ(X)`, `ρ (exp (t X)) = exp (t dρ(X))`.

```lean
lemma derivRep_oneParameterSubgroup (X : G.lieAlgebra) (t : ℝ) :
    ((ρ (G.oneParameterSubgroup X t) : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) =
      exp (t • derivRepFun ρ X)
```

**`GlobalGaugeGroup.derivRep_oneParameterSubgroup_inv`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L109).

> The inverse of the image of a one-parameter subgroup, `ρ (exp (t X))⁻¹ = exp (−t dρ(X))`.

```lean
lemma derivRep_oneParameterSubgroup_inv (X : G.lieAlgebra) (t : ℝ) :
    (↑(ρ (G.oneParameterSubgroup X t) : (W →L[ℂ] W)ˣ)⁻¹ : W →L[ℂ] W) =
      exp (t • -derivRepFun ρ X)
```

**`GlobalGaugeGroup.derivRepFun_eq`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L119).

> The derivative `dρ(X)` is the unique linear map `Z` with `ρ (exp (t X)) = exp (t Z)` for
> all `t`.

```lean
lemma derivRepFun_eq {X : G.lieAlgebra} {Z : W →L[ℂ] W}
    (hZ : ∀ t : ℝ, ((ρ (G.oneParameterSubgroup X t) : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) =
      exp (t • Z)) : derivRepFun ρ X = Z
```

## B. Linearity

**`GlobalGaugeGroup.derivRepFun_smul`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L132).

```lean
lemma derivRepFun_smul (r : ℝ) (X : G.lieAlgebra) :
    derivRepFun ρ (r • X) = r • derivRepFun ρ X
```

**`GlobalGaugeGroup.derivRepFun_add`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L142).

> The derivative of a representation is additive. Applying the representation to the Lie
> product formula for `exp (t (X + Y))` gives the Lie product formula for
> `exp (t dρ(X) + t dρ(Y))`.

```lean
lemma derivRepFun_add (X Y : G.lieAlgebra) :
    derivRepFun ρ (X + Y) = derivRepFun ρ X + derivRepFun ρ Y
```

**`GlobalGaugeGroup.derivRepLinear`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L184).

> The derivative of the representation, as a real-linear map on the Lie algebra.

```lean
noncomputable def derivRepLinear : G.lieAlgebra →ₗ[ℝ] W →L[ℂ] W
```

## C. The adjoint action and the commutator

**`GlobalGaugeGroup.derivRepFun_adjoint`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L197).

> The derivative of the representation intertwines the adjoint actions,
> `dρ(g X g⁻¹) = ρ(g) dρ(X) ρ(g)⁻¹`.

```lean
lemma derivRepFun_adjoint (g : G.group) (X : G.lieAlgebra) :
    derivRepFun ρ (G.adjoint g X) =
      ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) * derivRepFun ρ X *
        (↑(ρ g : (W →L[ℂ] W)ˣ)⁻¹ : W →L[ℂ] W)
```

**`GlobalGaugeGroup.derivRepFun_commutator`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L209).

> The derivative of the representation preserves the commutator. Differentiating the
> intertwining property `dρ(exp (s X) Y exp (−s X)) = exp (s dρ(X)) dρ(Y) exp (−s dρ(X))` at
> `s = 0` gives `dρ(X Y − Y X) = dρ(X) dρ(Y) − dρ(Y) dρ(X)`.

```lean
lemma derivRepFun_commutator (X Y : G.lieAlgebra) :
    derivRepFun ρ ⟨X.1 * Y.1 - Y.1 * X.1, commutator_mem_lieAlgebraOfIsClosed X.2 Y.2⟩ =
      derivRepFun ρ X * derivRepFun ρ Y -
        derivRepFun ρ Y * derivRepFun ρ X
```

## D. The Lie algebra representation

**`GlobalGaugeGroup.derivRep`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L254).

> The Lie algebra representation `dρ : 𝔤 → 𝔤𝔩(W)` of the continuous representation
> `ρ : G → GL(W)` of with `ρ (exp (t X)) = exp (t dρ(X))`.

```lean
noncomputable def derivRep : G.lieSubalgebra →ₗ⁅ℝ⁆ W →L[ℂ] W
```

**`GlobalGaugeGroup.apply_eq_exp_derivRep`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L264).

> The representation maps the one-parameter subgroup of a generator `X` to that of `dρ(X)`,
> `ρ (exp (t X)) = exp (t dρ(X))`.

```lean
lemma apply_eq_exp_derivRep {X : G.lieSubalgebra} {t : ℝ} {g : G.group}
    (hg : ((g : GeneralLinearGroup κ ℂ) : Matrix κ κ ℂ) = exp (t • (X : Matrix κ κ ℂ))) :
    ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) = exp (t • derivRep ρ X)
```

**`GlobalGaugeGroup.derivRep_eq_of`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L272).

> The Lie algebra representation at a generator `X` is the unique linear map `Z` with
> `ρ (exp (t X)) = exp (t Z)` for all `t`.

```lean
lemma derivRep_eq_of {X : G.lieSubalgebra} {Z : W →L[ℂ] W}
    (hZ : ∀ (t : ℝ) (g : G.group),
      ((g : GeneralLinearGroup κ ℂ) : Matrix κ κ ℂ) = exp (t • (X : Matrix κ κ ℂ)) →
        ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) = exp (t • Z)) :
    derivRep ρ X = Z
```

**`GlobalGaugeGroup.derivRep_adjoint`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L281).

> The Lie algebra representation intertwines the adjoint actions,
> `dρ(g X g⁻¹) = ρ(g) dρ(X) ρ(g)⁻¹`.

```lean
lemma derivRep_adjoint (g : G.group) (X : G.lieSubalgebra) :
    derivRep ρ ⟨(g.1 : Matrix κ κ ℂ) * X * (↑g.1⁻¹ : Matrix κ κ ℂ),
      conj_mem_lieAlgebraOfIsClosed (hH := G.isClosed) g X.2⟩ =
      ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) * derivRep ρ X *
        (↑(ρ g : (W →L[ℂ] W)ˣ)⁻¹ : W →L[ℂ] W)
```

**`GlobalGaugeGroup.commute_derivRep`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L291).

> A linear map commuting with every `ρ(g)` commutes with every `dρ(X)`. Both
> `exp (t dρ(X)) L` and `L exp (t dρ(X))` are the same function of `t`, and their derivatives at
> `t = 0` are `dρ(X) L` and `L dρ(X)`.

```lean
lemma commute_derivRep {L : W →L[ℂ] W}
    (hL : ∀ g, Commute ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) L) (X : G.lieSubalgebra) :
    Commute (derivRep ρ X) L
```

## E. Matter fields

> The Lie algebra representation of a matter field is the derivative of its representation.

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L319).

> The derivative `dρ(X) = d/dt ρ (exp (t X))` at `t = 0` of the representation of a matter
> field along a generator `X` of the global gauge group.

```lean
noncomputable def lieAlgebraRepFun (X : G.lieAlgebra) : M.V →L[ℂ] M.V
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun_smul`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L321).

```lean
lemma lieAlgebraRepFun_smul (r : ℝ) (X : G.lieAlgebra) :
    lieAlgebraRepFun M (r • X) = r • lieAlgebraRepFun M X
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun_add`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L325).

```lean
lemma lieAlgebraRepFun_add (X Y : G.lieAlgebra) :
    lieAlgebraRepFun M (X + Y) = lieAlgebraRepFun M X + lieAlgebraRepFun M Y
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepLinear`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L330).

> The derivative of the representation, as a real-linear map on the Lie algebra.

```lean
noncomputable def lieAlgebraRepLinear : G.lieAlgebra →ₗ[ℝ] M.V →L[ℂ] M.V
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun_adjoint`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L335).

> The derivative of the representation intertwines the adjoint actions,
> `dρ(g X g⁻¹) = ρ(g) dρ(X) ρ(g)⁻¹`.

```lean
lemma lieAlgebraRepFun_adjoint (g : G.group) (X : G.lieAlgebra) :
    lieAlgebraRepFun M (G.adjoint g X) =
      ((M.rep g : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V) * lieAlgebraRepFun M X *
        (↑(M.rep g : (M.V →L[ℂ] M.V)ˣ)⁻¹ : M.V →L[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun_commutator`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L342).

> The derivative of the representation preserves the commutator.

```lean
lemma lieAlgebraRepFun_commutator (X Y : G.lieAlgebra) :
    lieAlgebraRepFun M ⟨X.1 * Y.1 - Y.1 * X.1, commutator_mem_lieAlgebraOfIsClosed X.2 Y.2⟩ =
      lieAlgebraRepFun M X * lieAlgebraRepFun M Y -
        lieAlgebraRepFun M Y * lieAlgebraRepFun M X
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRep`**, a def, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L350).

> The Lie algebra representation `dρ : 𝔤 → 𝔤𝔩(V)` of the continuous representation
> `ρ : G → GL(V)` of a matter field, with `ρ (exp (t X)) = exp (t dρ(X))`.

```lean
noncomputable def lieAlgebraRep : G.lieSubalgebra →ₗ⁅ℝ⁆ M.V →L[ℂ] M.V
```

**`GlobalGaugeGroup.MatterField.rep_eq_exp_lieAlgebraRep`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L354).

> The representation maps the one-parameter subgroup of a generator `X` to that of `dρ(X)`,
> `ρ (exp (t X)) = exp (t dρ(X))`.

```lean
lemma rep_eq_exp_lieAlgebraRep {X : G.lieSubalgebra} {t : ℝ} {g : G.group}
    (hg : ((g : GeneralLinearGroup κ ℂ) : Matrix κ κ ℂ) = exp (t • (X : Matrix κ κ ℂ))) :
    ((M.rep g : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V) = exp (t • lieAlgebraRep M X)
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRep_eq_of`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L361).

> The Lie algebra representation at a generator `X` is the unique linear map `Z` with
> `ρ (exp (t X)) = exp (t Z)` for all `t`.

```lean
lemma lieAlgebraRep_eq_of {X : G.lieSubalgebra} {Z : M.V →L[ℂ] M.V}
    (hZ : ∀ (t : ℝ) (g : G.group),
      ((g : GeneralLinearGroup κ ℂ) : Matrix κ κ ℂ) = exp (t • (X : Matrix κ κ ℂ)) →
        ((M.rep g : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V) = exp (t • Z)) :
    lieAlgebraRep M X = Z
```

**`GlobalGaugeGroup.MatterField.commute_lieAlgebraRep`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean#L370).

> A linear map commuting with the representation of every group element commutes with the
> Lie algebra representation.

```lean
lemma commute_lieAlgebraRep {L : M.V →L[ℂ] M.V}
    (hL : ∀ g, Commute ((M.rep g : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V) L) (X : G.lieSubalgebra) :
    Commute (lieAlgebraRep M X) L
```

## Depends on

- [The adjoint action of a global gauge group on its Lie algebra](../part-03/globalgaugegroup-liealgebra-adjoint.md)
- [Matter fields of a global gauge group](matterfield-basic.md)

## Proof depends on

- [One-parameter subgroups of real Banach algebras](../../../../physlib/mathematics/formathlib/part-02/oneparametersubgroups-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/DerivRep.lean)
