---
declaration: module
origin: cited
lean: HasGradientAt.add, HasGradientAt.sub, HasGradientAt.mul, HasGradientAt.const_mul, gradient_add_const, gradient_add, gradient_const_mul, HasDerivAt.comp_hasGradientAt
statement: formalized
proof: formalized
---

# Elementary rules for the gradient

The module `Physlib.Mathematics.Calculus.Gradient`, [Physlib/Mathematics/Calculus/Gradient.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean): 17 declarations, 17 with a docstring.

> Algebraic and chain rules for gradients of classical-mechanical observables.

## i. Overview

> Mathlib defines the gradient `∇ f x` of a real-valued function on a real Hilbert space as the
> Riesz representative of its Fréchet derivative, but records no rules for the algebraic operations
> on `f` beyond constants. This file collects the elementary rules used throughout the classical
> mechanics of Physlib: algebraic and chain rules, together with the gradients of scalar products,
> quadratic forms, the norm, and coordinate functionals on Euclidean space.
>
> These are the rules needed to differentiate Lagrangians and Hamiltonians of the form
> `kinetic − potential` with respect to positions and velocities.
>
> The `HasGradientAt` rules establish differentiability and the value of the gradient together.
> They allow the gradients of conserved quantities in central-force systems, built from
> `⟪p, p⟫`, `⟪q, q⟫`, `⟪q, p⟫` and `‖q‖`, to be computed compositionally.
>
> These are rules for Mathlib's `gradient` on an abstract real Hilbert space. They are distinct from
> `Physlib.SpaceAndTime.Space.Derivatives.Grad`, whose `Space.grad` is a coordinate-valued operator on
> the structure `Space d`; nothing there applies to `EuclideanSpace ℝ (Fin 1)` or to a general inner
> product space. The file is deliberately real: two of its rules (`gradient_const_mul` and
> `gradient_inner_self`) are specific to real scalars, so the remaining ones are stated over
> `ℝ` as well.

## ii. Key results

> - `HasGradientAt.add`, `HasGradientAt.sub`, `HasGradientAt.mul`, `HasGradientAt.const_mul` :
>   algebraic rules for differentiable observables.
> - `HasDerivAt.comp_hasGradientAt` : the chain rule for a real function of an observable.
> - `hasGradientAt_inner_left`, `hasGradientAt_inner_right`, `hasGradientAt_inner_self`,
>   `hasGradientAt_norm`, `hasGradientAt_coord` : the basic gradients with differentiability.
> - `gradient_add_const` : `∇ (f + c) = ∇ f`.
> - `gradient_add` : `∇ (f + g) = ∇ f + ∇ g` for differentiable `f` and `g`.
> - `gradient_const_mul` : `∇ (c * f) = c • ∇ f` for differentiable `f`.
> - `gradient_inner_self` : `∇ (fun y => ⟪y, y⟫) x = 2 • x`.
> - `gradient_const_mul_inner_self` : `∇ (fun y => c * ⟪y, y⟫) x = (2 * c) • x`.
> - `gradient_coord` : `∇ (fun y => y i) x = EuclideanSpace.single i 1`.
> - `gradient_comp_coord` : `∇ (fun y => f (y i)) x = f' • EuclideanSpace.single i 1` when
>   `HasDerivAt f f' (x i)`.

## iv. References

> * Mathlib, `Mathlib.Analysis.Calculus.Gradient.Basic`.

## A. Algebraic rules

> Adding a constant does not change the Fréchet derivative, hence not the gradient; the gradient is
> additive over differentiable functions, multiplying by a constant scales it, and products satisfy
> the Leibniz rule.

**`HasGradientAt.add`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L87).

> The gradient of a sum is the sum of the gradients.

```lean
lemma HasGradientAt.add (hf : HasGradientAt f f' x) (hg : HasGradientAt g g' x) :
    HasGradientAt (fun y => f y + g y) (f' + g') x
```

**`HasGradientAt.sub`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L94).

> The gradient of a difference is the difference of the gradients.

```lean
lemma HasGradientAt.sub (hf : HasGradientAt f f' x) (hg : HasGradientAt g g' x) :
    HasGradientAt (fun y => f y - g y) (f' - g') x
```

**`HasGradientAt.mul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L101).

> The gradient of a product is given by the Leibniz rule.

```lean
lemma HasGradientAt.mul (hf : HasGradientAt f f' x) (hg : HasGradientAt g g' x) :
    HasGradientAt (fun y => f y * g y) (f x • g' + g x • f') x
```

**`HasGradientAt.const_mul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L108).

> The gradient of a constant multiple is the constant multiple of the gradient.

```lean
lemma HasGradientAt.const_mul (c : ℝ) (hf : HasGradientAt f f' x) :
    HasGradientAt (fun y => c * f y) (c • f') x
```

**`gradient_add_const`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L115).

> Adding a constant to a function does not change its gradient.

```lean
lemma gradient_add_const {f : F → ℝ} (c : ℝ) (x : F) :
    gradient (fun y => f y + c) x = gradient f x
```

**`gradient_add`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L121).

> The gradient of a sum of differentiable functions is the sum of their gradients.

```lean
lemma gradient_add {f g : F → ℝ} {x : F} (hf : DifferentiableAt ℝ f x)
    (hg : DifferentiableAt ℝ g x) :
    gradient (fun y => f y + g y) x = gradient f x + gradient g x
```

**`gradient_const_mul`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L128).

> The gradient of a constant multiple of a differentiable function is the constant multiple of
> the gradient.

```lean
lemma gradient_const_mul {f : F → ℝ} {x : F} (c : ℝ) (hf : DifferentiableAt ℝ f x) :
    gradient (fun y => c * f y) x = c • gradient f x
```

## B. The chain rule

**`HasDerivAt.comp_hasGradientAt`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L140).

> The gradient of `y ↦ φ (f y)` is `φ'` times the gradient of `f`, for `φ'` the derivative of
> `φ` at `f x`.

```lean
lemma HasDerivAt.comp_hasGradientAt {φ : ℝ → ℝ} {φ' : ℝ} (hf : HasGradientAt f f' x)
    (hφ : HasDerivAt φ φ' (f x)) : HasGradientAt (fun y => φ (f y)) (φ' • f') x
```

## C. Scalar products and quadratic forms

> The quadratic form `y ↦ ⟪y, y⟫` has derivative `v ↦ 2 ⟪x, v⟫` at `x`, whose Riesz representative
> is `2 • x`.

**`hasGradientAt_inner_left`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L156).

> The gradient of `y ↦ ⟪a, y⟫` is `a`.

```lean
lemma hasGradientAt_inner_left (a x : F) : HasGradientAt (fun y : F => ⟪a, y⟫_ℝ) a x
```

**`hasGradientAt_inner_right`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L161).

> The gradient of `y ↦ ⟪y, a⟫` is `a`.

```lean
lemma hasGradientAt_inner_right (a x : F) : HasGradientAt (fun y : F => ⟪y, a⟫_ℝ) a x
```

**`gradient_inner_self`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L166).

> The gradient of `y ↦ ⟪y, y⟫` at `x` is `2 • x`.

```lean
lemma gradient_inner_self (x : F) : gradient (fun y : F => ⟪y, y⟫_ℝ) x = (2 : ℝ) • x
```

**`hasGradientAt_inner_self`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L174).

> The gradient of `y ↦ ⟪y, y⟫` is `2 • y`.

```lean
lemma hasGradientAt_inner_self (x : F) : HasGradientAt (fun y : F => ⟪y, y⟫_ℝ) ((2 : ℝ) • x) x
```

**`gradient_const_mul_inner_self`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L179).

> The gradient of `y ↦ c * ⟪y, y⟫` at `x` is `(2 * c) • x`.

```lean
lemma gradient_const_mul_inner_self (c : ℝ) (x : F) :
    gradient (fun y : F => c * ⟪y, y⟫_ℝ) x = (2 * c) • x
```

## D. The norm

**`hasGradientAt_norm`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L191).

> Away from the origin, the gradient of the norm is the unit vector `‖x‖⁻¹ • x`.

```lean
lemma hasGradientAt_norm (hx : x ≠ 0) : HasGradientAt (fun y : F => ‖y‖) (‖x‖⁻¹ • x) x
```

## E. Coordinate functionals on Euclidean space

> The coordinate functional `y ↦ y i` on `EuclideanSpace ℝ ι` is the continuous linear map
> `EuclideanSpace.proj i`, whose Riesz representative is the basis vector `EuclideanSpace.single i 1`.

**`gradient_coord`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L211).

> The gradient of the `i`-th coordinate functional on Euclidean space is the `i`-th basis
> vector.

```lean
lemma gradient_coord {ι : Type*} [Fintype ι] [DecidableEq ι] (i : ι) (x : EuclideanSpace ℝ ι) :
    gradient (fun y : EuclideanSpace ℝ ι => y i) x = EuclideanSpace.single i 1
```

**`hasGradientAt_coord`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L221).

> The gradient of the `i`-th coordinate functional on Euclidean space is the `i`-th basis
> vector.

```lean
lemma hasGradientAt_coord {ι : Type*} [Fintype ι] [DecidableEq ι] (i : ι)
    (x : EuclideanSpace ℝ ι) :
    HasGradientAt (fun y : EuclideanSpace ℝ ι => y i) (EuclideanSpace.single i 1) x
```

**`gradient_comp_coord`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean#L229).

> Chain rule for a function of one coordinate: the gradient of `y ↦ f (y i)` at `x` is
> `f' • EuclideanSpace.single i 1`, where `f'` is the derivative of `f` at `x i`.

```lean
lemma gradient_comp_coord {ι : Type*} [Fintype ι] [DecidableEq ι] {f : ℝ → ℝ} {f' : ℝ}
    (i : ι) (x : EuclideanSpace ℝ ι) (hf : HasDerivAt f f' (x i)) :
    gradient (fun y : EuclideanSpace ℝ ι => f (y i)) x = f' • EuclideanSpace.single i 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Calculus/Gradient.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Gradient.lean)
