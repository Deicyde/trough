---
declaration: module
origin: cited
lean: ClassicalMechanics.deriv_comp_eq_poissonBracket, ClassicalMechanics.poissonBracket, ClassicalMechanics.poissonBracket_eq_of_hasGradientAt, ClassicalMechanics.poissonBracket_antisymm, ClassicalMechanics.poissonBracket_self, ClassicalMechanics.poissonBracket_add_left, ClassicalMechanics.poissonBracket_const_mul_left, ClassicalMechanics.poissonBracket_add_right
statement: formalized
proof: formalized
---

# The Poisson bracket

The module `Physlib.ClassicalMechanics.HamiltonianMechanics.PoissonBracket`, [Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean): 12 declarations, 12 with a docstring, 1 listed as significant.

> The Poisson bracket of phase-space observables and their Hamiltonian time evolution.

## i. Overview

> The Poisson bracket packages, into a single antisymmetric bilinear operation on phase-space
> functions, the way an observable evolves along a Hamiltonian flow. Following the convention of
> `hamiltonEqOp` in `HamiltonsEquations.lean`, a phase-space function is a function `f : X → X → ℝ`
> read as `f p q` for `p` a momentum and `q` a position, both valued in a real inner product space
> `X`. The bracket of two such functions is
>
> $$\{f, g\} := \left\langle \frac{\partial f}{\partial q}, \frac{\partial g}{\partial p}
>   \right\rangle - \left\langle \frac{\partial f}{\partial p}, \frac{\partial g}{\partial q}
>   \right\rangle,$$
>
> built from the same currying-and-`gradient` idiom `hamiltonEqOp` already uses to express partial
> derivatives on phase space.

## ii. Key results

> - `poissonBracket` : the Poisson bracket of two phase-space functions.
> - `poissonBracket_eq_of_hasGradientAt` : computes the bracket from known partial gradients.
> - `poissonBracket_antisymm` : the bracket is antisymmetric.
> - `poissonBracket_self` : every observable Poisson-commutes with itself.
> - `poissonBracket_add_left`, `poissonBracket_add_right`, `poissonBracket_const_mul_left`,
>   `poissonBracket_const_mul_right` : the bracket is bilinear, that is additive and homogeneous in
>   each argument.
> - `poissonBracket_mul_left`, `poissonBracket_mul_right` : the bracket satisfies the Leibniz rule
>   in each argument.
> - `deriv_comp_eq_inner_gradient_add` : the time derivative of a phase-space function composed with
>   a trajectory is the sum of its gradients paired with the trajectory's velocities.
> - `deriv_comp_eq_poissonBracket` : along a solution of Hamilton's equations, the time derivative of
>   an observable is its Poisson bracket with the Hamiltonian.

## iv. References

> * G. J. Sussman and J. Wisdom, "Structure and Interpretation of Classical Mechanics", Section 3.2.
>   <https://groups.csail.mit.edu/mac/users/gjs/6946/sicm-html/book-Z-H-37.html>.
>   [ref: sussman\_wisdom\_sicm]

## A. The definition of the Poisson bracket

**`ClassicalMechanics.poissonBracket`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L83).

> The Poisson bracket of two phase-space functions `f g : X → X → ℝ`, each read as `f p q` for
> a momentum `p` and a position `q`, at a point `(p, q)` of phase space.

```lean
noncomputable def poissonBracket (f g : X → X → ℝ) (p q : X) : ℝ
```

**`ClassicalMechanics.poissonBracket_eq_of_hasGradientAt`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L89).

> The Poisson bracket of two phase-space functions whose partial gradients at `(p, q)` are
> known.

```lean
lemma poissonBracket_eq_of_hasGradientAt {f g : X → X → ℝ} {p q fp fq gp gq : X}
    (hfp : HasGradientAt (fun p' => f p' q) fp p) (hfq : HasGradientAt (fun q' => f p q') fq q)
    (hgp : HasGradientAt (fun p' => g p' q) gp p) (hgq : HasGradientAt (fun q' => g p q') gq q) :
    poissonBracket f g p q = ⟪fq, gp⟫_ℝ - ⟪fp, gq⟫_ℝ
```

## B. Antisymmetry

**`ClassicalMechanics.poissonBracket_antisymm`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L102).

> The Poisson bracket is antisymmetric.

```lean
lemma poissonBracket_antisymm (f g : X → X → ℝ) (p q : X) :
    poissonBracket f g p q = -poissonBracket g f p q
```

**`ClassicalMechanics.poissonBracket_self`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L109).

> The Poisson bracket of a phase-space function with itself vanishes.

```lean
lemma poissonBracket_self (f : X → X → ℝ) (p q : X) : poissonBracket f f p q = 0
```

## C. Bilinearity

> The bracket is additive and homogeneous under scaling by a constant in each argument. We prove
> this for the first argument; the second-argument versions follow from `poissonBracket_antisymm`.

**`ClassicalMechanics.poissonBracket_add_left`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L124).

> The Poisson bracket is additive in its first argument, for functions differentiable in both
> phase-space directions.

```lean
lemma poissonBracket_add_left (f₁ f₂ g : X → X → ℝ) (p q : X)
    (hf₁p : DifferentiableAt ℝ (fun p' => f₁ p' q) p)
    (hf₂p : DifferentiableAt ℝ (fun p' => f₂ p' q) p)
    (hf₁q : DifferentiableAt ℝ (fun q' => f₁ p q') q)
    (hf₂q : DifferentiableAt ℝ (fun q' => f₂ p q') q) :
    poissonBracket (fun p' q' => f₁ p' q' + f₂ p' q') g p q =
      poissonBracket f₁ g p q + poissonBracket f₂ g p q
```

**`ClassicalMechanics.poissonBracket_const_mul_left`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L137).

> The Poisson bracket is homogeneous of degree one in its first argument, for a function
> differentiable in both phase-space directions.

```lean
lemma poissonBracket_const_mul_left (c : ℝ) (f g : X → X → ℝ) (p q : X)
    (hfp : DifferentiableAt ℝ (fun p' => f p' q) p)
    (hfq : DifferentiableAt ℝ (fun q' => f p q') q) :
    poissonBracket (fun p' q' => c * f p' q') g p q = c * poissonBracket f g p q
```

**`ClassicalMechanics.poissonBracket_add_right`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L146).

> The Poisson bracket is additive in its second argument.

```lean
lemma poissonBracket_add_right (f g₁ g₂ : X → X → ℝ) (p q : X)
    (hg₁p : DifferentiableAt ℝ (fun p' => g₁ p' q) p)
    (hg₂p : DifferentiableAt ℝ (fun p' => g₂ p' q) p)
    (hg₁q : DifferentiableAt ℝ (fun q' => g₁ p q') q)
    (hg₂q : DifferentiableAt ℝ (fun q' => g₂ p q') q) :
    poissonBracket f (fun p' q' => g₁ p' q' + g₂ p' q') p q =
      poissonBracket f g₁ p q + poissonBracket f g₂ p q
```

**`ClassicalMechanics.poissonBracket_const_mul_right`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L158).

> The Poisson bracket is homogeneous of degree one in its second argument.

```lean
lemma poissonBracket_const_mul_right (c : ℝ) (f g : X → X → ℝ) (p q : X)
    (hgp : DifferentiableAt ℝ (fun p' => g p' q) p)
    (hgq : DifferentiableAt ℝ (fun q' => g p q') q) :
    poissonBracket f (fun p' q' => c * g p' q') p q = c * poissonBracket f g p q
```

## D. The Leibniz rule

**`ClassicalMechanics.poissonBracket_mul_left`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L173).

> The Poisson bracket satisfies the Leibniz rule in its first argument.

```lean
lemma poissonBracket_mul_left (f₁ f₂ g : X → X → ℝ) (p q : X)
    (hf₁p : DifferentiableAt ℝ (fun p' => f₁ p' q) p)
    (hf₂p : DifferentiableAt ℝ (fun p' => f₂ p' q) p)
    (hf₁q : DifferentiableAt ℝ (fun q' => f₁ p q') q)
    (hf₂q : DifferentiableAt ℝ (fun q' => f₂ p q') q) :
    poissonBracket (fun p' q' => f₁ p' q' * f₂ p' q') g p q =
      poissonBracket f₁ g p q * f₂ p q + f₁ p q * poissonBracket f₂ g p q
```

**`ClassicalMechanics.poissonBracket_mul_right`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L187).

> The Poisson bracket satisfies the Leibniz rule in its second argument.

```lean
lemma poissonBracket_mul_right (f g₁ g₂ : X → X → ℝ) (p q : X)
    (hg₁p : DifferentiableAt ℝ (fun p' => g₁ p' q) p)
    (hg₂p : DifferentiableAt ℝ (fun p' => g₂ p' q) p)
    (hg₁q : DifferentiableAt ℝ (fun q' => g₁ p q') q)
    (hg₂q : DifferentiableAt ℝ (fun q' => g₂ p q') q) :
    poissonBracket f (fun p' q' => g₁ p' q' * g₂ p' q') p q =
      poissonBracket f g₁ p q * g₂ p q + g₁ p q * poissonBracket f g₂ p q
```

## E. Time evolution along a Hamiltonian flow

### E.1. The chain rule for a phase-space function along a trajectory

**`ClassicalMechanics.deriv_comp_eq_inner_gradient_add`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L212).

> The time derivative of a phase-space function `f` composed with trajectories `p q : Time → X`
> is the sum of the gradients of `f` paired with the velocities `∂ₜ p` and `∂ₜ q`.

```lean
lemma deriv_comp_eq_inner_gradient_add (f : X → X → ℝ) (p q : Time → X) (t : Time)
    (hp : DifferentiableAt ℝ p t) (hq : DifferentiableAt ℝ q t)
    (hf : DifferentiableAt ℝ (Function.uncurry f) (p t, q t)) :
    ∂ₜ (fun t => f (p t) (q t)) t =
      ⟪gradient (fun p' => f p' (q t)) (p t), ∂ₜ p t⟫_ℝ +
      ⟪gradient (fun q' => f (p t) q') (q t), ∂ₜ q t⟫_ℝ
```

### E.2. Time evolution as the Poisson bracket with the Hamiltonian

**`ClassicalMechanics.deriv_comp_eq_poissonBracket`**, a theorem, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean#L242). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Along a solution of Hamilton's equations for a Hamiltonian `H`, the time derivative of a
> phase-space observable `f` is its Poisson bracket with `H t`.

```lean
theorem deriv_comp_eq_poissonBracket (H : Time → X → X → ℝ) (p q : Time → X) (f : X → X → ℝ)
    (t : Time) (heq : hamiltonEqOp H p q = 0)
    (hp : DifferentiableAt ℝ p t) (hq : DifferentiableAt ℝ q t)
    (hf : DifferentiableAt ℝ (Function.uncurry f) (p t, q t)) :
    ∂ₜ (fun t => f (p t) (q t)) t = poissonBracket f (H t) (p t) (q t)
```

## Depends on

- [Hamilton's equations](hamiltonsequations.md)

## Proof depends on

- [Elementary rules for the gradient](../../mathematics/calculus/gradient.md)

## Sources

- [Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/PoissonBracket.lean)
