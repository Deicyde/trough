---
declaration: module
origin: cited
lean: ClassicalMechanics.CentralForce, ClassicalMechanics.CentralForce.m_ne_zero, ClassicalMechanics.CentralForce.hamiltonian, ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_momentum, ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_position, ClassicalMechanics.CentralForce.contDiffOn_hamiltonian, ClassicalMechanics.CentralForce.toHamiltonianSystem, ClassicalMechanics.CentralForce.mem_domain_toHamiltonianSystem
statement: formalized
proof: formalized
---

# Central forces

The module `PhyslibAlpha.ClassicalMechanics.CentralForce.Basic`, [PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean): 9 declarations, 9 with a docstring.

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

**`ClassicalMechanics.CentralForce`**, a structure, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L73).

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

**`ClassicalMechanics.CentralForce.m_ne_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L89).

> The mass of the particle is non-zero.

```lean
lemma m_ne_zero : S.m ≠ 0
```

## B. The Hamiltonian

**`ClassicalMechanics.CentralForce.hamiltonian`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L99).

> The Hamiltonian `H(p, q) = ⟪p, p⟫ / (2 m) + V ‖q‖` of a central-force system, as a function of
> the momentum `p` and the position `q`.

```lean
noncomputable def hamiltonian (p q : EuclideanSpace ℝ (Fin 3)) : ℝ
```

### B.1. Gradients of the Hamiltonian

**`ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_momentum`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L109).

> The momentum gradient of the Hamiltonian of a central-force system is the velocity `p / m`.

```lean
lemma hasGradientAt_hamiltonian_momentum (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun p' => S.hamiltonian p' q) (S.m⁻¹ • p) p
```

**`ClassicalMechanics.CentralForce.hasGradientAt_hamiltonian_position`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L118).

> Away from the centre of force, the position gradient of the Hamiltonian of a central-force
> system is `V'(‖q‖) q / ‖q‖`, which is parallel to the position.

```lean
lemma hasGradientAt_hamiltonian_position (p : EuclideanSpace ℝ (Fin 3))
    {q : EuclideanSpace ℝ (Fin 3)} (hq : q ≠ 0) :
    HasGradientAt (fun q' => S.hamiltonian p q') ((deriv S.V ‖q‖ / ‖q‖) • q) q
```

### B.2. Smoothness of the Hamiltonian

**`ClassicalMechanics.CentralForce.contDiffOn_hamiltonian`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L136).

> The Hamiltonian of a central-force system is smooth away from the centre of force.

```lean
lemma contDiffOn_hamiltonian :
    ContDiffOn ℝ ∞ (Function.uncurry S.hamiltonian) {x | x.2 ≠ 0}
```

### B.3. The Hamiltonian system

**`ClassicalMechanics.CentralForce.toHamiltonianSystem`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L151).

> The Hamiltonian system of a central force, defined away from the centre of force.

```lean
noncomputable def toHamiltonianSystem :
    HamiltonianSystem 𝓘(ℝ, EuclideanSpace ℝ (Fin 3)) ⟨EuclideanSpace ℝ (Fin 3)⟩
```

**`ClassicalMechanics.CentralForce.mem_domain_toHamiltonianSystem`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L159).

> A coordinate state belongs to the central-force domain exactly when its position is nonzero.

```lean
lemma mem_domain_toHamiltonianSystem (p q : EuclideanSpace ℝ (Fin 3)) :
    PhaseSpace.ofInnerProductSpace p q ∈ S.toHamiltonianSystem.domain ↔ q ≠ 0
```

**`ClassicalMechanics.CentralForce.toHamiltonianSystem_hamiltonian`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean#L165).

> The bundled central-force system has the existing central-force Hamiltonian in coordinates.

```lean
lemma toHamiltonianSystem_hamiltonian (t : Time) (p q : EuclideanSpace ℝ (Fin 3)) :
    S.toHamiltonianSystem.hamiltonian (t, PhaseSpace.ofInnerProductSpace p q) =
      S.hamiltonian p q
```

## Depends on

- [Hamiltonian systems](../../../physlib/classicalmechanics/hamiltonianmechanics/basic.md)

## Proof depends on

- [Elementary rules for the gradient](../../../physlib/mathematics/calculus/gradient.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/CentralForce/Basic.lean)
