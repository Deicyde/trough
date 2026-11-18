---
declaration: module
origin: cited
lean: InnerProductSpace.realStdGaussian, InnerProductSpace.gaussian, InnerProductSpace.gaussian_apply, InnerProductSpace.gaussian₀, InnerProductSpace.stdGaussian, InnerProductSpace.exp_mul_gaussian, InnerProductSpace.gaussianExpMul, InnerProductSpace.gaussianExpMul_apply
statement: formalized
proof: formalized
---

# Gaussians in inner product spaces

The module `Physlib.Mathematics.InnerProductSpace.Gaussian`, [Physlib/Mathematics/InnerProductSpace/Gaussian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean): 8 declarations, 7 with a docstring; 2 private, not shown.

> Gaussians and their products with real linear exponentials as Schwartz maps.

## i. Overview

> In this module we define Gaussians as Schwartz maps in general inner product spaces.
>
> The most general Gaussian constructed is `exp (-2⁻¹ * ‖B⁻¹ (x - x₀)‖ ^ 2)` (mean `x₀`
> and covariance `BBᵀ`) as a Schwartz map `𝓢(E, 𝕜)`, where `B : D ≃L[ℝ] E` is a linear equivalence
> of inner product spaces. This is accomplished by first constructing the Gaussian
> `exp (-2⁻¹ * ‖x‖ ^ 2)` as a Schwartz map `𝓢(E, ℝ)` using explicit bounds on the derivatives
> of `‖x‖ ^ 2 = innerSL ℝ x x` and limiting properties of the real exponential,
> then composing with an invertible affine transformation.
>
> The Gaussians are left unnormalized since the appropriate condition will depend on context and
> whether `E` is finite- or infinite-dimensional. For example, the normalization conditions when
> interpreted as a probability density function vs. as a quantum state require different pre-factors.
>
> For some relevant Gaussian integrals see
> `Mathlib/Analysis/SpecialFunctions/Gaussian/FourierTransform`.

## ii. Key results

> - `gaussian 𝕜 B x₀` : Given a linear equivalence `B : D ≃L[ℝ] E` and mean `x₀ : E`,
>     the Gaussian `exp (-2⁻¹ * ‖B⁻¹ (x - x₀)‖ ^ 2)` centered on `x₀` as a Schwartz map `𝓢(E, 𝕜)`.
> - `gaussian₀ 𝕜 B` : Given a linear equivalence `B : D ≃L[ℝ] E` of inner product spaces,
>     the Gaussian `exp (-2⁻¹ * ‖B⁻¹ x‖ ^ 2)` centered on the origin as a Schwartz map `𝓢(E, 𝕜)`.
> - `stdGaussian E 𝕜` : The standard Gaussian `exp (-2⁻¹ * ‖x‖ ^ 2)` as a Schwartz map `𝓢(E, 𝕜)`.
> - `exp_mul_gaussian` : Completing the square for multiplication by `exp ⟪v, x⟫`.
> - `gaussianExpMul 𝕜 B x₀ v` : This product as a Schwartz map when `D` and `E` are complete.

## iv. References

> * None.

## A. Standard, real-valued

**`InnerProductSpace.realStdGaussian`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L141).

> The (unnormalized) real-valued standard Gaussian `exp (-2⁻¹ * ‖x‖ ^ 2)` as a Schwartz map.
>
> This definition is used to construct the general RCLike-valued Gaussian and the preferred version
> to use is `gaussian ℝ B x₀` (or `stdGaussian E ℝ` for mean zero, variance one).

```lean
def realStdGaussian : 𝓢(E, ℝ)
```

## B. General, RCLike-valued

**`InnerProductSpace.gaussian`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L173).

> The (unnormalized) `𝕜`-valued Gaussian `exp (-2⁻¹ * ‖B⁻¹ (x - x₀)‖ ^ 2)` as a Schwartz map.

```lean
def gaussian : 𝓢(E, 𝕜)
```

**`InnerProductSpace.gaussian_apply`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L178).

```lean
lemma gaussian_apply : gaussian 𝕜 B x₀ x = ofReal (rexp (-2⁻¹ * ‖B.symm (x - x₀)‖ ^ 2))
```

**`InnerProductSpace.gaussian₀`**, an abbrev, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L181).

> The (unnormalized) `𝕜`-valued Gaussian `exp (-2⁻¹ * ‖B⁻¹ x‖ ^ 2)` as a Schwartz map.

```lean
abbrev gaussian₀ : 𝓢(E, 𝕜)
```

**`InnerProductSpace.stdGaussian`**, an abbrev, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L185).

> The (unnormalized) `𝕜`-valued standard Gaussian `exp (-2⁻¹ * ‖x‖ ^ 2)` as a Schwartz map.

```lean
abbrev stdGaussian : 𝓢(E, 𝕜)
```

## C. Multiplication by a real linear exponential

> Completeness is assumed to use the adjoint of `B`. The exponential has a real exponent,
> even when the Gaussian is complex-valued.

**`InnerProductSpace.exp_mul_gaussian`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L197).

> Multiplication by a real linear exponential shifts and rescales a general Gaussian.

```lean
lemma exp_mul_gaussian (v : E) :
    (ofReal (rexp (inner ℝ v x)) : 𝕜) * gaussian 𝕜 B x₀ x =
      (ofReal (rexp (inner ℝ v x₀ + 2⁻¹ * ‖B.toContinuousLinearMap.adjoint v‖ ^ 2)) : 𝕜) *
        gaussian 𝕜 B (x₀ + B (B.toContinuousLinearMap.adjoint v)) x
```

**`InnerProductSpace.gaussianExpMul`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L211).

> The product of `gaussian 𝕜 B x₀` with the real exponential `exp ⟪v, x⟫`, as a Schwartz map.
> It has center `x₀ + B (Bᵀ v)` and the same covariance, with scale factor
> `exp (⟪v, x₀⟫ + 2⁻¹ * ‖Bᵀ v‖ ^ 2)`.

```lean
def gaussianExpMul (v : E) : 𝓢(E, 𝕜)
```

**`InnerProductSpace.gaussianExpMul_apply`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean#L217).

> Evaluation of the bundled product agrees with pointwise multiplication by the exponential.

```lean
lemma gaussianExpMul_apply (v : E) :
    gaussianExpMul 𝕜 B x₀ v x = (ofReal (rexp (inner ℝ v x)) : 𝕜) * gaussian 𝕜 B x₀ x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/InnerProductSpace/Gaussian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Gaussian.lean)
