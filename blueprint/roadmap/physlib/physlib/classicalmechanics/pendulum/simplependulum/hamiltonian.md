---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.canonicalMomentum, ClassicalMechanics.SimplePendulum.canonicalMomentum_eq, ClassicalMechanics.SimplePendulum.hamiltonian, ClassicalMechanics.SimplePendulum.hamiltonian_eq, ClassicalMechanics.SimplePendulum.hamiltonian_contDiff, ClassicalMechanics.SimplePendulum.gradient_hamiltonian_position_eq, ClassicalMechanics.SimplePendulum.gradient_hamiltonian_momentum_eq, ClassicalMechanics.SimplePendulum.hamiltonian_eq_energy
statement: formalized
proof: formalized
---

# The Hamiltonian formulation of the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Hamiltonian`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean): 11 declarations, 11 with a docstring.

## i. Overview

> This module gives the Hamiltonian formulation of the simple gravity pendulum, on the same
> one-dimensional Euclidean lift of the angle as `SimplePendulum.Basic`. The canonical momentum
> conjugate to the angle is the gradient of the Lagrangian in the angular velocity, the angular
> momentum `p = I θ̇` about the pivot; since the moment of inertia is positive, taking the
> canonical momentum is a linear equivalence between velocities and momenta. The Hamiltonian is
> the Legendre transform `H = ⟪p, θ̇⟫ - L` of the Lagrangian, which works out to the energy
> written on momentum-angle phase space, `H(t, p, θ) = ½ (1/I) ‖p‖² + V(θ)`; along any lift of
> the angle it is the energy of the lift. Hamilton's equations for the pendulum are packaged, as
> for the harmonic oscillator, into the vanishing of an operator on phase space, and for a smooth
> lift of the angle they are equivalent to the equation of motion of `SimplePendulum.Basic`.

## ii. Key results

> - `SimplePendulum.canonicalMomentum` is the canonical momentum `p = ∂L/∂θ̇ = I θ̇`, as a
>   linear equivalence between velocities and momenta, with its value recorded by
>   `canonicalMomentum_eq`.
> - `SimplePendulum.hamiltonian` is the Legendre transform of the Lagrangian, computed by
>   `hamiltonian_eq` to be `½ (1/I) ‖p‖² + V(θ)`, smooth by `hamiltonian_contDiff`, with the
>   two partial gradients `gradient_hamiltonian_position_eq` and
>   `gradient_hamiltonian_momentum_eq`.
> - `SimplePendulum.hamiltonian_eq_energy` identifies the Hamiltonian, evaluated along any lift
>   of the angle on its canonical momentum, with the energy of the lift.
> - `SimplePendulum.hamiltonEqOp` is the operator on momentum-angle phase space whose vanishing
>   is Hamilton's equations, and `SimplePendulum.equationOfMotion_iff_hamiltonEqOp_eq_zero`
>   proves that, for a smooth lift of the angle, Hamilton's equations are equivalent to the
>   equation of motion.
> - `SimplePendulum.equationOfMotion_tfae` gathers the formulations into a single equivalence:
>   for a smooth lift of the angle the equation of motion, its scalar form `θ̈ + ω² sin θ = 0`,
>   Hamilton's equations, and the Lagrangian and Hamiltonian variational principles are all
>   equivalent.

## iv. References

> References for the Hamiltonian formulation of the simple pendulum include:
>
> * Landau & Lifshitz, Mechanics, 3rd ed., §40, for the canonical momentum, the Hamiltonian as the
>   Legendre transform of the Lagrangian, and Hamilton's equations. [ref: landau\_mechanics]
> * The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Basic`, whose Lagrangian, energy
>   and equation of motion this module reformulates.

## A. The canonical momentum and the Hamiltonian

> We now turn to the Hamiltonian formulation of the simple pendulum. We define the canonical
> momentum and the Hamiltonian, relate the Hamiltonian to the energy, and show that the equation
> of motion is equivalent to Hamilton's equations.

### A.1. The canonical momentum

> We define the canonical momentum as the gradient of the Lagrangian with respect to the angular
> velocity. By `gradient_lagrangian_velocity_eq` this is the angular momentum `I θ̇` about the
> pivot, and since the moment of inertia is positive it is a linear equivalence between
> velocities and momenta.

**`ClassicalMechanics.SimplePendulum.canonicalMomentum`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L104).

> The canonical momentum of the simple pendulum, `p = ∂L/∂θ̇ = I θ̇`, as a linear
> equivalence between velocities and momenta in the angular chart.

```lean
noncomputable def canonicalMomentum (t : Time) (x : EuclideanSpace ℝ (Fin 1)) :
    EuclideanSpace ℝ (Fin 1) ≃ₗ[ℝ] EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.SimplePendulum.canonicalMomentum_eq`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L115).

> The canonical momentum of the simple pendulum is the angular momentum `I θ̇` about the
> pivot.

```lean
lemma canonicalMomentum_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    S.canonicalMomentum t x v = S.inertia • v
```

### A.2. The Hamiltonian

> The Hamiltonian is defined as a function of time, canonical momentum and angle, as the
> Legendre transform
> ```
> H = ⟪p, θ̇⟫ - L(t, θ, θ̇)
> ```
> where the angular velocity `θ̇` is a function of `p` and `θ` through the inverse of the
> canonical momentum.

**`ClassicalMechanics.SimplePendulum.hamiltonian`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L136).

> The Hamiltonian of the simple pendulum as a function of time, momentum and angle: the
> Legendre transform `H(t, p, θ) = ⟪p, θ̇⟫ - L(t, θ, θ̇)` of the Lagrangian, the angular
> velocity `θ̇` being recovered from the momentum by inverting the canonical momentum.

```lean
noncomputable def hamiltonian (t : Time) (p x : EuclideanSpace ℝ (Fin 1)) : ℝ
```

#### A.2.1. Equality for the Hamiltonian

> We prove a simple equality for the Hamiltonian, to help in computations: it is the kinetic
> energy written in terms of the momentum, plus the potential energy.

**`ClassicalMechanics.SimplePendulum.hamiltonian_eq`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L151).

> The Hamiltonian of the simple pendulum is the kinetic energy written in terms of the
> momentum, `½ (1/I) ‖p‖²`, plus the potential energy.

```lean
lemma hamiltonian_eq :
    S.hamiltonian = fun _ p x =>
      (1 / (2 : ℝ)) * (1 / S.inertia) * ⟪p, p⟫_ℝ + S.potentialEnergy x
```

#### A.2.2. Smoothness of the Hamiltonian

> We show that the Hamiltonian is smooth in all its arguments jointly.

**`ClassicalMechanics.SimplePendulum.hamiltonian_contDiff`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L171).

> The Hamiltonian of the simple pendulum is a smooth function of the time, the momentum and
> the angle jointly.

```lean
lemma hamiltonian_contDiff (n : WithTop ℕ∞) : ContDiff ℝ n ↿S.hamiltonian
```

#### A.2.3. Gradients of the Hamiltonian

> We now write down the gradients of the Hamiltonian with respect to the angle and the momentum.
> These are the two sides of Hamilton's equations.

**`ClassicalMechanics.SimplePendulum.gradient_hamiltonian_position_eq`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L186).

> The gradient of the Hamiltonian of the simple pendulum in the angle is the gradient of the
> potential energy, that is minus the torque.

```lean
lemma gradient_hamiltonian_position_eq (t : Time) (x p : EuclideanSpace ℝ (Fin 1)) :
    gradient (S.hamiltonian t p) x = gradient S.potentialEnergy x
```

**`ClassicalMechanics.SimplePendulum.gradient_hamiltonian_momentum_eq`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L199).

> The gradient of the Hamiltonian of the simple pendulum in the momentum is the angular
> velocity `(1/I) p` recovered from the momentum.

```lean
lemma gradient_hamiltonian_momentum_eq (t : Time) (x p : EuclideanSpace ℝ (Fin 1)) :
    gradient (S.hamiltonian t · x) p = (1 / S.inertia) • p
```

### A.3. Relation between Hamiltonian and energy

> We show that the Hamiltonian, evaluated along any lift of the angle on the canonical momentum
> of the lift, is the energy. This is independent of whether the lift satisfies the equation of
> motion or not.

**`ClassicalMechanics.SimplePendulum.hamiltonian_eq_energy`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L223).

> Along any lift of the angle, the Hamiltonian of the simple pendulum evaluated on the
> canonical momentum of the lift is the energy of the lift. This holds whether or not the lift
> satisfies the equation of motion.

```lean
lemma hamiltonian_eq_energy (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    (fun t => S.hamiltonian t (S.canonicalMomentum t (θ t) (∂ₜ θ t)) (θ t)) = S.energy θ
```

### A.4. Hamilton equation operator

> We define the operator on momentum-angle phase space whose vanishing is equivalent to
> Hamilton's equations.

**`ClassicalMechanics.SimplePendulum.hamiltonEqOp`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L244).

> The Hamilton-equations operator of the Hamiltonian of the simple pendulum, on
> momentum-angle phase space; its vanishing is equivalent to Hamilton's equations for the
> momentum and the angle.

```lean
noncomputable def hamiltonEqOp (p θ : Time → EuclideanSpace ℝ (Fin 1))
```

### A.5. Equation of motion if and only if Hamilton's equations

> We show that, for a smooth lift of the angle, the equation of motion is equivalent to
> Hamilton's equations for the lift and its canonical momentum, that is to the vanishing of the
> Hamilton equation operator on the pair. The equation for the angle recovers the angular
> velocity, and the equation for the momentum is the balance of the rate of change of the
> angular momentum against the torque.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_iff_hamiltonEqOp_eq_zero`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L262).

> For a smooth lift of the angle the equation of motion of the simple pendulum holds if and
> only if Hamilton's equations hold for the lift and its canonical momentum, that is if and
> only if the Hamilton-equations operator vanishes on the pair.

```lean
lemma equationOfMotion_iff_hamiltonEqOp_eq_zero (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) :
    S.EquationOfMotion θ ↔
      S.hamiltonEqOp (fun t => S.canonicalMomentum t (θ t) (∂ₜ θ t)) θ = 0
```

## B. Equivalences between the formulations

> We gather the formulations of the dynamics of the simple pendulum into a single equivalence.
> For a smooth lift of the angle the equation of motion, its scalar form, Hamilton's equations,
> the Lagrangian variational principle and the Hamiltonian variational principle are all
> equivalent. The equation of motion is itself the Newtonian formulation: the pointwise law is
> the rotational form of Newton's second law, so, unlike for the harmonic oscillator, no
> separate entry restates it. The equivalence of the equation of motion with the vanishing of
> the variational derivative of the action lives in section G.1 of the `Basic` module; the
> fourth entry states the same variational principle through the variational calculus directly.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_tfae`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean#L301).

> For a smooth lift of the angle the following formulations of the dynamics of the simple
> pendulum are equivalent:
> 1. the equation of motion, the pointwise rotational Newton law balancing the rate of change
>   of the angular momentum against the torque;
> 2. the scalar mass-independent form `θ̈ + ω² sin θ = 0` of the equation of motion;
> 3. Hamilton's equations for the lift and its canonical momentum, as the vanishing of the
>   Hamilton-equations operator;
> 4. the Lagrangian variational principle, the vanishing of the variational gradient of the
>   action integral of the Lagrangian, written through the variational calculus directly; the
>   same principle, through the variational derivative of the action, is recorded standalone
>   as `equationOfMotion_iff_gradLagrangian_zero` in the `Basic` module;
> 5. the Hamiltonian variational principle, the vanishing of the variational gradient of the
>   phase-space action on the pair of the canonical momentum and the lift.

```lean
lemma equationOfMotion_tfae (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    List.TFAE [S.EquationOfMotion θ,
      ∀ t, ∂ₜ (∂ₜ θ) t 0 + S.ω ^ 2 * Real.sin (θ t 0) = 0,
      S.hamiltonEqOp (fun t => S.canonicalMomentum t (θ t) (∂ₜ θ t)) θ = 0,
      (δ (q':=θ), ∫ t, S.lagrangian t (q' t) (fderiv ℝ q' t 1)) = 0,
      (δ (pq':= fun t => (S.canonicalMomentum t (θ t) (∂ₜ θ t), θ t)),
        ∫ t, ⟪(pq' t).1, ∂ₜ (Prod.snd ∘ pq') t⟫_ℝ -
          S.hamiltonian t (pq' t).1 (pq' t).2) = 0]
```

## Depends on

- [Hamilton's equations](../../hamiltonianmechanics/hamiltonsequations.md)
- [The simple gravity pendulum](basic.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Hamiltonian.lean)
