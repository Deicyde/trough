---
declaration: module
origin: cited
lean: ClassicalMechanics.Lagrangian.IsTotalTimeDerivative, ClassicalMechanics.Lagrangian.isTotalTimeDerivative_explicit, ClassicalMechanics.Lagrangian.isTotalTimeDerivative_neg, ClassicalMechanics.Lagrangian.totalTimeDerivative_contDiff, ClassicalMechanics.Lagrangian.totalTimeDerivative_hasZeroVarGradient, ClassicalMechanics.Lagrangian.totalTimeDerivative_hasVarGradientAt_equivalence, ClassicalMechanics.Lagrangian.totalTimeDerivative_varGradient_equivalenvce, ClassicalMechanics.Lagrangian.totalTimeDerivative_eulerLagrange_equivalenvce
statement: formalized
proof: formalized
---

# Equivalent Lagrangians under Total Derivatives

The module `Physlib.ClassicalMechanics.Lagrangian.TotalDerivativeEquivalence`, [Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean): 9 declarations, 8 with a docstring.

## i. Overview

> Two Lagrangians are physically equivalent if they differ by a total time derivative
> d/dt F(q, t). This is because the Euler-Lagrange equations depend only on extremizing
> the action integral, and total derivatives don't affect which paths are extremal.
>
> This module defines the key concept of a function being a total time derivative,
> which is essential for analyzing symmetries like Galilean invariance.
>
> Note: Some authors call this "gauge equivalence" by analogy with gauge transformations
> in field theory, but we avoid that terminology here since no gauge fields are involved.

## ii. Key insight

> A general function δL(t, q, dₜ q) is a total time derivative if there exists a function
> F(t, q) (independent of velocity) such that:
>   δL(t, q, dₜ q) = d/dt F(t, q) = fderiv ℝ F (t q) (v, 1)
>
> By the chain rule, this expands to:
>   δL(t, q, dₜ q) = ∂F/∂t + ⟨∇ᵣF, dₜ q⟩
>
> For the special case where δL depends only on velocity dₜ q (not position or time),
> this implies a strong constraint:
>   δL(dₜ q) = ⟨g, dₜ q⟩ for some constant vector g
>
> This is because:
> 1. d/dt F(t, q) = ∂F/∂t + ⟨∇F, dₜ q⟩
> 2. For δL to be q-independent, ∇F must be q-independent
> 3. For δL to be t-independent, the time-dependent part must vanish
> 4. The result is δL = ⟨g, dₜ q⟩ for constant g

## iii. Key definitions

> - `IsTotalTimeDerivative`: General case for δL(t, q, dₜ q)
> - `IsTotalTimeDerivativeVelocity`: Velocity-only case, equivalent to δL(dₜ q) = ⟨g, dₜ q⟩

## iv. References

> * Landau & Lifshitz, "Mechanics", §2 (The principle of least action). [ref: landau\_mechanics]
> * Landau & Lifshitz, "Mechanics", §4 (The Lagrangian for a free particle). [ref: landau\_mechanics]

## A. General Total Time Derivative

**`ClassicalMechanics.Lagrangian.IsTotalTimeDerivative`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L78).

> A function δL(t, q, dₜ q) is a total time derivative if it can be written as d/dt F(r, t)
>     for some function F that depends on position and time but not velocity,
>
> δL(t, q, dₜ q) = (d/dt) F(t, q)
>
>     This is the most general form of Lagrangian equivalence under total derivatives.
>     The key point is that F must be independent of velocity.

```lean
def IsTotalTimeDerivative
    (δL : Time → X → X → ℝ) : Prop
```

**`ClassicalMechanics.Lagrangian.isTotalTimeDerivative_explicit`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L91).

> Explicit reformulation (by the chain rule):
> δL(t, q, dₜ q) = ∂F/∂t(t, q) + ⟨∇ᵣF(t, q), dₜ q⟩
>
> or
>
> δL(t, q, dₜ q) = fderiv ℝ F (t, q) (1, dₜ q)

```lean
lemma isTotalTimeDerivative_explicit {δL : Time → X → X → ℝ} :
    IsTotalTimeDerivative δL ↔  (∃ (F : Time → X → ℝ) (_ : ContDiff ℝ ∞ ↿F),
    ∀ t q v, δL t q v = fderiv ℝ ↿F (t, q) ((1 : Time), v))
```

**`ClassicalMechanics.Lagrangian.isTotalTimeDerivative_neg`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L191).

> Elementary fact: if δL is a time derivative, then so is -δL.

```lean
lemma isTotalTimeDerivative_neg {δL : Time → X → X → ℝ} (h :  IsTotalTimeDerivative δL) :
    IsTotalTimeDerivative (- δL)
```

**`ClassicalMechanics.Lagrangian.totalTimeDerivative_contDiff`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L209).

> If δL is a total time derivative (of a smooth function), then it is smooth

```lean
lemma totalTimeDerivative_contDiff {δL : Time → X → X → ℝ} (h : IsTotalTimeDerivative δL):
    ContDiff ℝ ∞ ↿δL
```

## B. Total time derivative do not affect the physical content

> The total time derivative does not affect the Euler-Lagrange equations, because its variational
>   derivative is zero:
>   ∫d/dt F(t, q)= F(t₁,q₁) - F(t₀,q₀)
>   is fixed by the boundary conditions.

**`ClassicalMechanics.Lagrangian.totalTimeDerivative_hasZeroVarGradient`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L240).

> Total time derivative has a variational derivative, which is zero

```lean
lemma totalTimeDerivative_hasZeroVarGradient [CompleteSpace X] {δL : Time → X → X → ℝ}
    (h : IsTotalTimeDerivative δL) (q : Time → X) (hq : ContDiff ℝ ∞ q):
     HasVarGradientAt (fun q' t => δL t (q' t) (∂ₜ q' t)) (fun _ => 0) q
```

**`ClassicalMechanics.Lagrangian.totalTimeDerivative_hasVarGradientAt_equivalence`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L272).

> If two lagrangians, L and L', differ by a total time derivative, and L has a variational derivative
> grad, then so does L'.

```lean
lemma totalTimeDerivative_hasVarGradientAt_equivalence [CompleteSpace X] (L δL : Time → X → X → ℝ)
    (hδL : IsTotalTimeDerivative δL)
    (q : Time → X)    (hq : ContDiff ℝ ∞ q) (grad : Time → X)
    (hgrad :  HasVarGradientAt (fun q' t => L t (q' t) (fderiv ℝ  q' t 1)) grad q) :
    HasVarGradientAt (fun q' t => (L + δL) t (q' t) (fderiv ℝ q' t 1)) grad q
```

**`ClassicalMechanics.Lagrangian.totalTimeDerivative_varGradient_equivalenvce`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L291).

```lean
lemma totalTimeDerivative_varGradient_equivalenvce [CompleteSpace X] (L L' : Time → X → X → ℝ)
    (htot : IsTotalTimeDerivative (L' - L))
    (q : Time → X) (hq : ContDiff ℝ ∞ q):
    (δ (q':=q), ∫ t, L' t (q' t) (fderiv ℝ q' t 1)) =
       (δ (q':=q), ∫ t, L t (q' t) (fderiv ℝ q' t 1))
```

**`ClassicalMechanics.Lagrangian.totalTimeDerivative_eulerLagrange_equivalenvce`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L326).

> Corollary: If L and L' differ by a total time derivative, then the corresponding Euler-Lagrange
> operators coincide

```lean
lemma totalTimeDerivative_eulerLagrange_equivalenvce [CompleteSpace X] (L L' : Time → X → X → ℝ)
    (htot : IsTotalTimeDerivative (L' - L)) (hContDiff : (ContDiff ℝ ∞ ↿L) ∨ (ContDiff ℝ ∞ ↿L'))
    (q : Time → X) (hq : ContDiff ℝ ∞ q) : eulerLagrangeOp L q = eulerLagrangeOp L' q
```

## C. Velocity-Only Total Time Derivative

> When δL depends only on velocity (the free particle case), the condition simplifies.

**`ClassicalMechanics.Lagrangian.isTotalTimeDerivativeVelocity`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean#L383).

> A velocity-only function that is a total time derivative must be linear in velocity.
>
> If δL depends only on velocity and equals d/dt F(t, q) for some F,
> then δL(dₜ q) = ⟨g, dₜ q⟩ for some constant vector g.
>
> This characterization comes from the requirement that:
> - d/dt F(t, q) = ∂F/∂t + ⟨∇F, dₜ q⟩ = ∂F/∂t + ⟨∇F, dₜ q⟩
> - For the result to be independent of q and t, we need ∇F = g (constant) and ∂F/∂t = 0
> - Thus δL(dₜ q) = ⟨g, dₜ q⟩
>
> WLOG, we assume `δL 0 = 0` since constants are total derivatives (c = d/dt(c·t))
> and can be absorbed without affecting the equations of motion.

```lean
lemma isTotalTimeDerivativeVelocity  [CompleteSpace X]
    (δL : X → ℝ)
    (hδL0 : δL 0 = 0)
    (h : IsTotalTimeDerivative (fun _ _ v => δL v)) :
    ∃ g : X, ∀ v, δL v = ⟪g, v⟫_ℝ
```

## Depends on

- [A. Euler–Lagrange equations](../eulerlagrange.md)

## Sources

- [Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/TotalDerivativeEquivalence.lean)
