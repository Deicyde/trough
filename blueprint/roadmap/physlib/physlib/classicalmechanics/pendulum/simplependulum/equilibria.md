---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.equationOfMotion_const_zero, ClassicalMechanics.SimplePendulum.isSolution_const_zero, ClassicalMechanics.SimplePendulum.equationOfMotion_const_pi, ClassicalMechanics.SimplePendulum.isSolution_const_pi, ClassicalMechanics.SimplePendulum.equationOfMotion_const_iff, ClassicalMechanics.SimplePendulum.separatrixEnergy, ClassicalMechanics.SimplePendulum.separatrixEnergy_eq, ClassicalMechanics.SimplePendulum.separatrixEnergy_pos
statement: formalized
proof: formalized
---

# Equilibria and energy regimes of the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Equilibria`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean): 15 declarations, 15 with a docstring.

## i. Overview

> The equation of motion of the simple gravity pendulum, `I θ̈ = -m g ℓ sin θ` in the lifted
> formulation of `SimplePendulum.Basic`, has two elementary consequences that follow from the
> vanishing of the torque and from energy conservation alone, before any non-constant solution is
> constructed. The first is the equilibria: the torque of gravity vanishes exactly where `sin θ`
> does, so the constant lifts at the angle `0` — the bob hanging at rest below the pivot — and at
> the angle `π` — the bob balanced above it — solve the equation of motion, and conversely a
> constant lift is a solution only at the multiples of `π`. The second is the division of the
> smooth motions into regimes by the value of the conserved energy. The threshold is the energy
> `2 m g ℓ` of the inverted equilibrium, the separatrix energy: below it the potential energy
> cannot reach its value at the top of the swing, so the bob never gets there — classically the
> regime of libration, the bob swinging back and forth; above it the kinetic energy never
> vanishes, so the bob never halts — classically the regime of rotation, the pendulum circulating
> over the top. This is the phase portrait of the pendulum drawn in Arnold §4, whose level curves
> of the energy are closed ovals below the threshold and unbounded waves above it.
>
> As in `SimplePendulum.Basic`, the motion is written on the Euclidean lift
> `Time → EuclideanSpace ℝ (Fin 1)` of the angle. Only the bounds characteristic of each regime
> are proved here: the librating and rotating motions themselves, and the instability of the
> inverted equilibrium, are statements about non-constant solutions and are not constructed in
> this module.

## ii. Key results

> - `SimplePendulum.equationOfMotion_const_zero` and `SimplePendulum.equationOfMotion_const_pi`
>   are the hanging and the inverted equilibrium, packaged as the simplest explicit solutions of
>   the pendulum by `SimplePendulum.isSolution_const_zero` and `SimplePendulum.isSolution_const_pi`,
>   and `SimplePendulum.equationOfMotion_const_iff` shows that the constant solutions are exactly
>   the equilibria.
> - `SimplePendulum.separatrixEnergy` is the energy `2 m g ℓ` of the inverted equilibrium
>   (`SimplePendulum.energy_const_pi`), the threshold between libration and rotation.
> - `SimplePendulum.neg_one_lt_cos_of_energy_lt`: below the threshold the bob never reaches the
>   top of the swing. `SimplePendulum.deriv_ne_zero_of_energy_gt`: above it the angular velocity
>   never vanishes. `SimplePendulum.potentialEnergy_eq_energy_of_deriv_eq_zero`: at a turning
>   point the potential energy equals the total energy.

## iv. References

> References for the equilibria and the energy regimes of the simple pendulum include:
>
> * Landau & Lifshitz, Mechanics, 3rd ed., §11 (motion in one dimension: the turning points, and
>   finite and infinite motion according to the energy). [ref: landau\_mechanics]
> * Arnold, Mathematical Methods of Classical Mechanics, 2nd ed., §4 (the phase portrait of the
>   pendulum). [ref: arnold\_mechanics]

## A. Equilibria

> The two configurations at which the torque of gravity vanishes — the bob hanging at rest below
> the pivot and the bob balanced above it — give constant solutions of the equation of motion, the
> simplest explicit solutions of the pendulum. This section verifies the two, and proves the
> converse: a constant lift solves the equation of motion only where the torque vanishes, that is
> only at the angles `π n`. The constant solutions are exactly the equilibria.

### A.1. The hanging equilibrium

> At the angle `0` the bob hangs at rest at the bottom of its swing. The lift is constant, so the
> angular momentum does not change, and the torque vanishes with `sin 0`: both sides of the
> equation of motion are zero.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_const_zero`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L106).

> The constant lift at the angle `0` — the bob hanging at rest at the bottom of its swing —
> satisfies the equation of motion of the simple pendulum.

```lean
lemma equationOfMotion_const_zero :
    S.EquationOfMotion (fun _ => (0 : EuclideanSpace ℝ (Fin 1)))
```

**`ClassicalMechanics.SimplePendulum.isSolution_const_zero`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L118).

> The hanging equilibrium is a solution of the simple pendulum: the constant lift at the angle
> `0` is smooth and satisfies the equation of motion. It is the simplest explicit solution of the
> pendulum.

```lean
lemma isSolution_const_zero : S.IsSolution (fun _ => 0)
```

### A.2. The inverted equilibrium

> At the angle `π` the bob is balanced directly above the pivot, where the torque vanishes with
> `sin π`; the pendulum stays there. That this balance is unstable — neighbouring solutions run
> away from it — is a statement about non-constant solutions, and is not proved here.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_const_pi`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L133).

> The constant lift at the angle `π` — the bob balanced directly above the pivot — satisfies
> the equation of motion of the simple pendulum.

```lean
lemma equationOfMotion_const_pi :
    S.EquationOfMotion (fun _ => EuclideanSpace.single 0 Real.pi)
```

**`ClassicalMechanics.SimplePendulum.isSolution_const_pi`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L144).

> The inverted equilibrium is a solution of the simple pendulum: the constant lift at the
> angle `π` is smooth and satisfies the equation of motion.

```lean
lemma isSolution_const_pi : S.IsSolution (fun _ => EuclideanSpace.single 0 Real.pi)
```

### A.3. The constant solutions are the equilibria

> For a constant lift the angular momentum does not change, so the equation of motion reduces to
> the vanishing of the torque, that is to `sin θ = 0`, which holds exactly at the multiples of
> `π`. The constant solutions are therefore exactly the equilibria: the hanging equilibrium, the
> inverted equilibrium, and their copies shifted by whole turns.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_const_iff`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L161).

> A constant lift satisfies the equation of motion of the simple pendulum if and only if the
> sine of its angle vanishes — classically, the angles straight down and straight up: the
> constant solutions are exactly the equilibria.

```lean
lemma equationOfMotion_const_iff (x : EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion (fun _ => x) ↔ Real.sin (x 0) = 0
```

## B. Energy regimes

> Energy conservation divides the smooth motions of the pendulum into regimes according to the
> value of the conserved energy, the threshold being the energy `2 m g ℓ` of the inverted
> equilibrium. Below the threshold the potential energy cannot reach its value at the top of the
> swing, so the bob never reaches the top; classically this is the regime of libration, the bob
> swinging back and forth. Above the threshold the kinetic energy can never vanish, so the bob
> never halts; classically this is the regime of rotation, the pendulum circulating over the top.
> This is the phase portrait of the pendulum drawn in Arnold §4, whose level curves of the energy
> are closed ovals below the threshold and unbounded waves above it. This section proves the
> below- and above-threshold bounds characteristic of each regime, from two elementary bounds
> relating the energies — the librating and rotating motions themselves are not constructed
> here — and characterizes the turning points, the instants at which the velocity vanishes and
> the potential energy exhausts the total energy.

### B.1. The separatrix energy

> The threshold between the regimes is the energy of the inverted equilibrium: no kinetic energy,
> and the potential energy `2 m g ℓ` of the top of the swing. It is called the separatrix energy
> after the curve it names in the phase portrait, the level set of the energy separating the
> closed orbits of libration from the unbounded orbits of rotation. Only the threshold value is
> used in this file: the separatrix motions themselves — the non-constant solutions asymptotic to
> the inverted equilibrium — are not constructed here.

**`ClassicalMechanics.SimplePendulum.separatrixEnergy`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L208).

> The separatrix energy of the simple pendulum is `2 m g ℓ`, the energy of the inverted
> equilibrium. It is the threshold separating the two regimes of the motion, libration below it
> and rotation above it.

```lean
def separatrixEnergy : ℝ
```

**`ClassicalMechanics.SimplePendulum.separatrixEnergy_eq`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L211).

> The separatrix energy of the simple pendulum, written out.

```lean
lemma separatrixEnergy_eq : S.separatrixEnergy = 2 * (S.m * S.g * S.ℓ)
```

**`ClassicalMechanics.SimplePendulum.separatrixEnergy_pos`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L214).

> The separatrix energy of the simple pendulum is positive.

```lean
lemma separatrixEnergy_pos : 0 < S.separatrixEnergy
```

**`ClassicalMechanics.SimplePendulum.energy_const_pi`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L219).

> The energy of the simple pendulum along the inverted equilibrium is the separatrix energy:
> the bob balanced at the top has no kinetic energy and the full potential energy `2 m g ℓ`.

```lean
lemma energy_const_pi :
    S.energy (fun _ => EuclideanSpace.single 0 Real.pi) = fun _ => S.separatrixEnergy
```

### B.2. Energy bounds

> Two elementary bounds drive the regime theorems: the kinetic energy is non-negative, so the
> potential energy is at most the total energy; and the potential energy is non-negative, so
> `I θ̇²` is at most twice the total energy. None of the bounds of this subsection uses the
> equation of motion — they hold along every lift of the angle.

**`ClassicalMechanics.SimplePendulum.kineticEnergy_nonneg`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L238).

> The kinetic energy of the simple pendulum is non-negative along every lift of the angle.

```lean
lemma kineticEnergy_nonneg (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    0 ≤ S.kineticEnergy θ t
```

**`ClassicalMechanics.SimplePendulum.inertia_mul_inner_deriv_le`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L245).

> The moment of inertia times the square of the angular speed, `I θ̇²`, is at most twice the
> total energy, along every lift of the angle.

```lean
lemma inertia_mul_inner_deriv_le (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.inertia * ⟪∂ₜ θ t, ∂ₜ θ t⟫_ℝ ≤ 2 * S.energy θ t
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_le_energy`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L255).

> The potential energy of the simple pendulum is at most the total energy along every lift of
> the angle.

```lean
lemma potentialEnergy_le_energy (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.potentialEnergy (θ t) ≤ S.energy θ t
```

### B.3. Libration and rotation

> Along a smooth solution with energy below the separatrix energy, the potential energy — being
> at most the conserved total energy — stays strictly below `2 m g ℓ`, so the cosine of the angle
> stays strictly above `-1`: the bob never reaches the top of the swing, and the motion is a
> libration, swinging back and forth — though only the bound is proved here. Along a smooth
> solution with energy above the separatrix energy the angular velocity can never vanish, for at
> such an instant the whole energy would be potential, and the potential energy never exceeds
> `2 m g ℓ`; the velocity being continuous, it keeps a fixed sign, and the motion is a rotation
> over the top — though only the non-vanishing is proved here.

**`ClassicalMechanics.SimplePendulum.neg_one_lt_cos_of_energy_lt`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L280).

> Libration: along a smooth lift of the angle satisfying the equation of motion, with energy
> below the separatrix energy, the cosine of the angle stays strictly above `-1` — the bob
> never reaches the top of the swing.

```lean
lemma neg_one_lt_cos_of_energy_lt (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ)
    (hE : S.energy θ 0 < S.separatrixEnergy) (t : Time) : -1 < Real.cos (θ t 0)
```

**`ClassicalMechanics.SimplePendulum.deriv_ne_zero_of_energy_gt`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L293).

> Rotation: along a smooth lift of the angle satisfying the equation of motion, with energy
> above the separatrix energy, the angular velocity never vanishes — the bob never halts.

```lean
lemma deriv_ne_zero_of_energy_gt (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ)
    (hE : S.separatrixEnergy < S.energy θ 0) (t : Time) : ∂ₜ θ t ≠ 0
```

### B.4. Turning points

> At an instant where the angular velocity vanishes the kinetic energy vanishes with it, and the
> conserved total energy is purely potential. These are the turning points of the motion, where a
> librating bob halts at the extremes of its arc before swinging back; by the rotation theorem of
> B.3 they can occur only at energies not above the separatrix energy.

**`ClassicalMechanics.SimplePendulum.potentialEnergy_eq_energy_of_deriv_eq_zero`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean#L321).

> Turning points: along a smooth lift of the angle satisfying the equation of motion, at an
> instant where the angular velocity vanishes, the potential energy equals the conserved total
> energy.

```lean
lemma potentialEnergy_eq_energy_of_deriv_eq_zero (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ) (t : Time) (h0 : ∂ₜ θ t = 0) :
    S.potentialEnergy (θ t) = S.energy θ 0
```

## Depends on

- [The simple gravity pendulum](basic.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Equilibria.lean)
