---
declaration: module
origin: cited
lean: Lorentz.Velocity.minkowskiProduct_eq_zero_of_hasDerivAt, Lorentz.Velocity.hasDerivAt_ofSpatialPart
statement: formalized
proof: formalized
---

# Derivatives of Lorentz velocities

The module `Physlib.Relativity.Tensors.RealTensor.Velocity.Deriv`, [Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean): 2 declarations, 2 with a docstring.

> Derivatives of unit four-velocity curves and the spatial-part constructor.

## i. Overview

> Differentiating the normalization of a curve in `Lorentz.Velocity` gives orthogonality
> of its value and derivative. The spatial-part constructor has an explicit derivative,
> obtained from the squared Euclidean norm and the square-root chain rule. Derivatives are
> taken in the ambient Lorentz vector space. For a worldline's four-velocity parametrized
> by proper time, the derivative is four-acceleration.

## ii. Key results

> - `Lorentz.Velocity.minkowskiProduct_eq_zero_of_hasDerivAt`: the derivative of a curve of
>   unit four-velocities is Minkowski orthogonal to its value.
> - `Lorentz.Velocity.hasDerivAt_ofSpatialPart`: the ambient derivative of the unit
>   four-velocity determined by a differentiable spatial-part curve.

## iv. References

> The proofs use the bilinear derivative rule from `Mathlib.Analysis.Calculus.Deriv.Mul`
> and the squared-norm derivative from `Mathlib.Analysis.InnerProductSpace.Calculus`.

## A. Derivative orthogonality

**`Lorentz.Velocity.minkowskiProduct_eq_zero_of_hasDerivAt`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean#L55).

> The derivative of a curve of unit future-directed four-velocities is Minkowski
> orthogonal to its value.

```lean
lemma minkowskiProduct_eq_zero_of_hasDerivAt {d : ℕ} {u : ℝ → Velocity d}
    {a : Vector d} {t : ℝ} (hu : HasDerivAt (fun s => (u s).1) a t) :
    ⟪(u t).1, a⟫ₘ = 0
```

## B. Derivative of the spatial-part constructor

**`Lorentz.Velocity.hasDerivAt_ofSpatialPart`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean#L70).

> The ambient derivative of the unit future-directed four-velocity determined by
> a differentiable spatial-part curve.

```lean
lemma hasDerivAt_ofSpatialPart {d : ℕ} {p : ℝ → EuclideanSpace ℝ (Fin d)}
    {p' : EuclideanSpace ℝ (Fin d)} {t : ℝ} (hp : HasDerivAt p p' t) :
    HasDerivAt (fun s => (ofSpatialPart (p s)).1)
      (Vector.ofTemporalComponent (inner ℝ (p t) p' / Real.sqrt (1 + ‖p t‖ ^ 2)) +
        Vector.ofSpatialComponent p') t
```

## Depends on

- [Lorentz Velocities](realtensor-velocity-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Deriv.lean)
