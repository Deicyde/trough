---
declaration: module
origin: cited
lean: ClassicalMechanics.CentralForce, ClassicalMechanics.CentralForce.m_ne_zero, ClassicalMechanics.CentralForce.hamiltonian, ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_momentum, ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_position, ClassicalMechanics.CentralForce.contDiffOn_hamiltonian
statement: formalized
proof: formalized
---

# Central forces

The module `PhyslibAlpha.ClassicalMechanics.CentralForce.Basic`, [PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean): 6 declarations, 6 with a docstring.

> Hamiltonian and partial gradients of a particle in a conservative central potential.

## i. Overview

> This file models a particle of mass `m` in three-dimensional space under a conservative central
> force centred at the origin. The force is derived from a potential `V (‖q‖)` which depends only on
> the distance `‖q‖` from the origin. Its Hamiltonian, as a function of the momentum `p` and the
> position `q`, is
>
> $$H(p, q) = \frac{\langle p, p\rangle}{2m} + V(\|q\|).$$
>
> The Kepler problem, `V r = -k / r`, and the isotropic harmonic oscillator, `V r = k r² / 2`, are
> the most important examples.
>
> The radial potential `V` is represented by a function on all of `ℝ`, with smoothness required
> only for positive radii. Its value at zero is part of this total-function representation; the
> position-gradient and smoothness results apply only when `q ≠ 0`, allowing potentials singular
> at the physical centre.
>
> This file defines the Hamiltonian and computes its partial gradients: the momentum gradient is the
> velocity `p / m`, and away from the centre the position gradient `V'(‖q‖) q / ‖q‖` is parallel to
> the position. The latter is what makes the angular momentum a conserved quantity.

## ii. Key results

> - `CentralForce` : the input data, a mass and a potential smooth away from the centre of force.
> - `CentralForce.hamiltonian` : the Hamiltonian.
> - `CentralForce.hasGradientAt_hamiltonian_momentum`,
>   `CentralForce.hasGradientAt_hamiltonian_position` : its partial gradients.
> - `CentralForce.contDiffOn_hamiltonian` : it is smooth away from the centre of force.

## iv. References

> * H. Goldstein, C. Poole and J. Safko, *Classical Mechanics*, 3rd edition, Chapter 3.

## A. The input data

**`ClassicalMechanics.CentralForce`**, a structure, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L71).

> A particle in three-dimensional space under a conservative central force centred at the origin,
> specified by its mass `m` and a radial potential `V` smooth at positive radii.

```lean
structure CentralForce where
  /-- The mass of the particle. -/
  m : ℝ
  /-- The potential, as a function of the distance from the centre of force. -/
  V : ℝ → ℝ
  /-- The mass of the particle is positive. -/
  m_pos : 0 < m
  /-- The potential is smooth away from the centre of force. -/
  contDiffOn_V : ContDiffOn ℝ ∞ V (Set.Ioi 0)
```

**`ClassicalMechanics.CentralForce.m_ne_zero`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L87).

> The mass of the particle is non-zero.

```lean
lemma m_ne_zero : S.m ≠ 0
```

## B. The Hamiltonian

**`ClassicalMechanics.CentralForce.hamiltonian`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L97).

> The Hamiltonian `H(p, q) = ⟪p, p⟫ / (2 m) + V ‖q‖` of a central-force system, as a function of
> the momentum `p` and the position `q`.

```lean
noncomputable def hamiltonian (p q : EuclideanSpace ℝ (Fin 3)) : ℝ
```

### B.1. Gradients of the Hamiltonian

**`ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_momentum`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L107).

> The momentum gradient of the Hamiltonian of a central-force system is the velocity `p / m`.

```lean
lemma hasGradientAt_hamiltonian_momentum (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun p' => S.hamiltonian p' q) (S.m⁻¹ • p) p
```

**`ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_position`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L116).

> Away from the centre of force, the position gradient of the Hamiltonian of a central-force
> system is `V'(‖q‖) q / ‖q‖`, which is parallel to the position.

```lean
lemma hasGradientAt_hamiltonian_position (p : EuclideanSpace ℝ (Fin 3))
    {q : EuclideanSpace ℝ (Fin 3)} (hq : q ≠ 0) :
    HasGradientAt (fun q' => S.hamiltonian p q') ((deriv S.V ‖q‖ / ‖q‖) • q) q
```

### B.2. Smoothness of the Hamiltonian

**`ClassicalMechanics.CentralForce.contDiffOn_hamiltonian`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L134).

> The Hamiltonian of a central-force system is smooth away from the centre of force.

```lean
lemma contDiffOn_hamiltonian :
    ContDiffOn ℝ ∞ (Function.uncurry S.hamiltonian) {x | x.2 ≠ 0}
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Elementary rules for the gradient](../../../physlib/mathematics/calculus/gradient.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean)
