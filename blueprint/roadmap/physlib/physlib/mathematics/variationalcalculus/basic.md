---
declaration: module
origin: cited
lean: fundamental_theorem_of_variational_calculus', fundamental_theorem_of_variational_calculus
statement: formalized
proof: formalized
---

# Fundamental lemma of the calculus of variations

The module `Physlib.Mathematics.VariationalCalculus.Basic`, [Physlib/Mathematics/VariationalCalculus/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Basic.lean): 2 declarations, 1 with a docstring.

> The key took in variational calculus is:
> ```
> ∀ h, ∫ x, f x * h x = 0 → f = 0
> ```
> which allows use to go from reasoning about integrals to reasoning about functions.

## Overview of variational calculus

> The variational calculus API in Physlib is designed to match and formalize the physicists intuition
> of variational calculus. It is not designed to be a general API for variational calculus.
>
> Within variational caclulus we are interested in function transformations, `F : (X → U) → (Y → V)`.
> In physics this functional is often of the form `L : (Time → U) → Time → ℝ`,
> which represents the Lagrangian of a system. We will use this to explain the formalization
> within this API.
>
> The action is nominally given by
>
> $$S[u] = \int L(u, t) dt,$$
>
> however it is convenient to
> introduce another function `φ` and define the action as
>
> $$S[u] = \int φ(t) L(u, t) dt.$$
>
> In the end we will set `φ := fun _ => 1`.
>
> We now consider
>
> $$\frac{\partial}{\partial s} S[u + s * \delta u]$$
>
> at `s = 0`,
> which is the variational derivative of `S` at `u` in the direction `δu`.
> This is equal to
>
> $$
> \int φ(t) * \left. \frac{\partial}{\partial s} L(u + s * \delta u, t)\right|_{s = 0}dt
> $$
>
> Let us denote the function
>
> $$
> \delta u,\, t \mapsto \left. \frac{\partial}{\partial s} L(u + s * \delta u, t)\right|_{s = 0}
> $$
>
> as `Lᵤ : (Time → U) → (Time → ℝ)`.
> Then the variational derivative is
>
> $$\int φ (t) Lᵤ(δu, t) dt.$$
>
> It may then be possible to find a function `Gᵤ : (Time → ℝ) → Time → U`
> such that
>
> $$
> \int φ(t) Lᵤ(δu, t) dt = \int \langle Gᵤ(φ, t), δu(t)\rangle dt
> $$
>
> This is usually done by integration by parts.
>
> We now set `φ := fun _ => 1` and get `grad u := Gᵤ (fun _ => 1)`, which is the
> variational gradient at `u`. The Euler–Lagrange equations, for example, are then `grad u = 0`.
>
> In our API, the relationship between
> - `Lᵤ` and `Gᵤ` is captured by the `HasVarAdjoint`.
> - `L` and `Gᵤ` by `HasVarAdjDeriv`.
> - `L` and `grad u` by `HasVarGradientAt`.
>
> In practice we assume that `L` has a certain locality property
> `IsLocalizedFunctionTransform`, which allows us to work with functions
> `φ` and `δu` which have compact support.
>
> This API assumes that `U` is an inner-product space. This can be considered as the full
> configuration space, or a local chart thereof.

## References

> * https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/Variational.20Calculus/with/529022834.

**`fundamental_theorem_of_variational_calculus'`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Basic.lean#L97).

> A version of `fundamental_theorem_of_variational_calculus'` for `Continuous f`.
> The proof uses assumption that source of `f` is finite-dimensional
> inner-product space, so that a bump function with compact support exists via
> `ContDiffBump.hasCompactSupport` from `Analysis.Calculus.BumpFunction.Basic`.
>
> The proof is by contradiction, assume that there is `x₀` such that `f x₀ ≠ 0` then one construct
> construct `g` test function *supported* on the neighborhood of `x₀` such that `⟪f x, g x⟫ ≥ 0`
> and `⟪f x, g x⟫ > 0` on a neighborhood of x₀.
>
> Using `Y` for the theorem below to make use of bump functions in InnerProductSpaces. `Y` is
> a finite dimensional measurable space over `ℝ` with (standard) inner product.

```lean
lemma fundamental_theorem_of_variational_calculus' {f : Y → V}
    (μ : Measure Y) [IsFiniteMeasureOnCompacts μ] [μ.IsOpenPosMeasure]
    [OpensMeasurableSpace Y]
    (hf : Continuous f) (hg : ∀ g, IsTestFunction g → ∫ x, ⟪f x, g x⟫_ℝ ∂μ = 0) :
    f = 0
```

**`fundamental_theorem_of_variational_calculus`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Basic.lean#L229).

```lean
lemma fundamental_theorem_of_variational_calculus {f : X → V}
    (μ : Measure X) [IsFiniteMeasureOnCompacts μ] [μ.IsOpenPosMeasure]
    [OpensMeasurableSpace X]
    (hf : IsTestFunction f) (hg : ∀ g, IsTestFunction g → ∫ x, ⟪f x, g x⟫_ℝ ∂μ = 0) :
    f = 0
```

## Depends on

- [Test functions](istestfunction.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Basic.lean)
