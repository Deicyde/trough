---
declaration: module
origin: cited
lean: ClassicalMechanics.CentralForce.angularMomentum, ClassicalMechanics.CentralForce.angularMomentum_apply_zero, ClassicalMechanics.CentralForce.angularMomentum_apply_one, ClassicalMechanics.CentralForce.angularMomentum_apply_two, ClassicalMechanics.CentralForce.angularMomentumSq, ClassicalMechanics.CentralForce.angularMomentumZ, ClassicalMechanics.CentralForce.angularMomentumSq_eq_sum, ClassicalMechanics.CentralForce.angularMomentumSq_eq
statement: formalized
proof: formalized
---

# Angular-momentum observables under a central force

The module `PhyslibAlpha.ClassicalMechanics.CentralForce.AngularMomentum`, [PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean): 19 declarations, 19 with a docstring.

> Squared angular momentum, its axial component, and their Poisson brackets for central forces.

## i. Overview

> The angular momentum of a particle at position `q` with momentum `p` is `L = q × p`. This file
> defines it on phase space, together with the two functions of it which Poisson-commute: its squared
> magnitude `L² = ‖L‖²` and its component `L_z` along the z-axis. Their gradients follow from
> Lagrange's identity `‖q × p‖² = ⟪q, q⟫ ⟪p, p⟫ - ⟪q, p⟫²` and the explicit form
> `L_z = q₀ p₁ - q₁ p₀`.
>
> We show that `L²` and `L_z` are in involution, and that both Poisson-commute with any Hamiltonian
> whose momentum gradient is parallel to the momentum and whose position gradient is parallel to the
> position. By `CentralForce.hasGradientAt_hamiltonian_momentum` and
> `CentralForce.hasGradientAt_hamiltonian_position`, this includes the Hamiltonian of every
> central-force system away from the centre of force, so `L²` and `L_z` are conserved by the motion.

## ii. Key results

> - `CentralForce.angularMomentum` : the angular momentum `L = q × p`.
> - `CentralForce.angularMomentumSq`, `CentralForce.angularMomentumZ` : `L²` and `L_z`.
> - `CentralForce.angularMomentumSq_eq` : Lagrange's identity for `L²`.
> - `CentralForce.poissonBracket_angularMomentumSq_angularMomentumZ` : `{L², L_z} = 0`.
> - `CentralForce.poissonBracket_angularMomentumSq_hamiltonian`,
>   `CentralForce.poissonBracket_angularMomentumZ_hamiltonian` : `L²` and `L_z` Poisson-commute with
>   the Hamiltonian of a central-force system.

## iv. References

> * H. Goldstein, C. Poole and J. Safko, *Classical Mechanics*, 3rd edition,
>   Section 9.7 (Poisson bracket relations for angular momentum) and Chapter 3 (central forces).

## A. The angular momentum

**`ClassicalMechanics.CentralForce.angularMomentum`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L74).

> The angular momentum `L = q × p` of a particle at position `q` with momentum `p`.

```lean
noncomputable def angularMomentum (p q : EuclideanSpace ℝ (Fin 3)) : EuclideanSpace ℝ (Fin 3)
```

**`ClassicalMechanics.CentralForce.angularMomentum_apply_zero`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L78).

> The x-component of the angular momentum is `q₁ p₂ - q₂ p₁`.

```lean
lemma angularMomentum_apply_zero (p q : EuclideanSpace ℝ (Fin 3)) :
    angularMomentum p q 0 = q 1 * p 2 - q 2 * p 1
```

**`ClassicalMechanics.CentralForce.angularMomentum_apply_one`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L83).

> The y-component of the angular momentum is `q₂ p₀ - q₀ p₂`.

```lean
lemma angularMomentum_apply_one (p q : EuclideanSpace ℝ (Fin 3)) :
    angularMomentum p q 1 = q 2 * p 0 - q 0 * p 2
```

**`ClassicalMechanics.CentralForce.angularMomentum_apply_two`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L88).

> The z-component of the angular momentum is `q₀ p₁ - q₁ p₀`.

```lean
lemma angularMomentum_apply_two (p q : EuclideanSpace ℝ (Fin 3)) :
    angularMomentum p q 2 = q 0 * p 1 - q 1 * p 0
```

### A.1. The squared magnitude and the z-component

**`ClassicalMechanics.CentralForce.angularMomentumSq`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L100).

> The squared magnitude `L² = ‖q × p‖²` of the angular momentum, as a function on phase
> space.

```lean
noncomputable def angularMomentumSq (p q : EuclideanSpace ℝ (Fin 3)) : ℝ
```

**`ClassicalMechanics.CentralForce.angularMomentumZ`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L104).

> The component `L_z` of the angular momentum along the z-axis, as a function on phase space.

```lean
noncomputable def angularMomentumZ (p q : EuclideanSpace ℝ (Fin 3)) : ℝ
```

**`ClassicalMechanics.CentralForce.angularMomentumSq_eq_sum`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L108).

> The squared magnitude of the angular momentum is the sum of the squares of its components.

```lean
lemma angularMomentumSq_eq_sum (p q : EuclideanSpace ℝ (Fin 3)) :
    angularMomentumSq p q =
      angularMomentum p q 0 ^ 2 + angularMomentum p q 1 ^ 2 + angularMomentum p q 2 ^ 2
```

**`ClassicalMechanics.CentralForce.angularMomentumSq_eq`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L116).

> Lagrange's identity: the squared magnitude of the angular momentum `q × p` is
> `⟪q, q⟫ ⟪p, p⟫ - ⟪q, p⟫²`.

```lean
lemma angularMomentumSq_eq (p q : EuclideanSpace ℝ (Fin 3)) :
    angularMomentumSq p q = ⟪q, q⟫_ℝ * ⟪p, p⟫_ℝ - ⟪q, p⟫_ℝ ^ 2
```

### A.2. Smoothness

**`ClassicalMechanics.CentralForce.contDiff_angularMomentumSq`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L130).

> The squared magnitude of the angular momentum is a smooth function on phase space.

```lean
lemma contDiff_angularMomentumSq : ContDiff ℝ ∞ (Function.uncurry angularMomentumSq)
```

**`ClassicalMechanics.CentralForce.contDiff_angularMomentumZ`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L140).

> The z-component of the angular momentum is a smooth function on phase space.

```lean
lemma contDiff_angularMomentumZ : ContDiff ℝ ∞ (Function.uncurry angularMomentumZ)
```

## B. Gradients

**`ClassicalMechanics.CentralForce.hasGradientAt_angularMomentumSq_momentum`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L155).

> The momentum gradient of `L²` is `2 ⟪q, q⟫ p - 2 ⟪q, p⟫ q`.

```lean
lemma hasGradientAt_angularMomentumSq_momentum (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun p' => angularMomentumSq p' q)
      ((2 * ⟪q, q⟫_ℝ) • p - (2 * ⟪q, p⟫_ℝ) • q) p
```

**`ClassicalMechanics.CentralForce.hasGradientAt_angularMomentumSq_position`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L164).

> The position gradient of `L²` is `2 ⟪p, p⟫ q - 2 ⟪q, p⟫ p`.

```lean
lemma hasGradientAt_angularMomentumSq_position (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun q' => angularMomentumSq p q')
      ((2 * ⟪p, p⟫_ℝ) • q - (2 * ⟪q, p⟫_ℝ) • p) q
```

**`ClassicalMechanics.CentralForce.hasGradientAt_angularMomentumZ_momentum`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L173).

> The momentum gradient of `L_z` is `q₀ e₁ - q₁ e₀`.

```lean
lemma hasGradientAt_angularMomentumZ_momentum (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun p' => angularMomentumZ p' q)
      (q 0 • EuclideanSpace.single 1 1 - q 1 • EuclideanSpace.single 0 1) p
```

**`ClassicalMechanics.CentralForce.hasGradientAt_angularMomentumZ_position`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L181).

> The position gradient of `L_z` is `p₁ e₀ - p₀ e₁`.

```lean
lemma hasGradientAt_angularMomentumZ_position (p q : EuclideanSpace ℝ (Fin 3)) :
    HasGradientAt (fun q' => angularMomentumZ p q')
      (p 1 • EuclideanSpace.single 0 1 - p 0 • EuclideanSpace.single 1 1) q
```

## C. Poisson brackets

### C.1. The squared magnitude and the z-component are in involution

**`ClassicalMechanics.CentralForce.poissonBracket_angularMomentumSq_angularMomentumZ`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L202).

> The squared magnitude of the angular momentum and its z-component are in involution.

```lean
lemma poissonBracket_angularMomentumSq_angularMomentumZ (p q : EuclideanSpace ℝ (Fin 3)) :
    poissonBracket angularMomentumSq angularMomentumZ p q = 0
```

### C.2. Poisson brackets for radial partial gradients

> At a phase-space point where the momentum gradient of a Hamiltonian is parallel to the momentum
> and its position gradient is parallel to the position, its Poisson brackets with `L²` and `L_z`
> vanish. These sufficient conditions apply to the central-force Hamiltonian away from the centre.

**`ClassicalMechanics.CentralForce.poissonBracket_angularMomentumSq_eq_zero_of_hasGradientAt`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L223).

> `L²` Poisson-commutes with any phase-space function whose momentum gradient is parallel to the
> momentum and whose position gradient is parallel to the position.

```lean
lemma poissonBracket_angularMomentumSq_eq_zero_of_hasGradientAt
    {H : EuclideanSpace ℝ (Fin 3) → EuclideanSpace ℝ (Fin 3) → ℝ}
    {p q : EuclideanSpace ℝ (Fin 3)} {a c : ℝ}
    (hp : HasGradientAt (fun p' => H p' q) (a • p) p)
    (hq : HasGradientAt (fun q' => H p q') (c • q) q) :
    poissonBracket angularMomentumSq H p q = 0
```

**`ClassicalMechanics.CentralForce.poissonBracket_angularMomentumZ_eq_zero_of_hasGradientAt`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L236).

> `L_z` Poisson-commutes with any phase-space function whose momentum gradient is parallel to
> the momentum and whose position gradient is parallel to the position.

```lean
lemma poissonBracket_angularMomentumZ_eq_zero_of_hasGradientAt
    {H : EuclideanSpace ℝ (Fin 3) → EuclideanSpace ℝ (Fin 3) → ℝ}
    {p q : EuclideanSpace ℝ (Fin 3)} {a c : ℝ}
    (hp : HasGradientAt (fun p' => H p' q) (a • p) p)
    (hq : HasGradientAt (fun q' => H p q') (c • q) q) :
    poissonBracket angularMomentumZ H p q = 0
```

### C.3. Conservation under a central force

**`ClassicalMechanics.CentralForce.poissonBracket_angularMomentumSq_hamiltonian`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L258).

> Away from the centre of force, the squared magnitude of the angular momentum Poisson-commutes
> with the Hamiltonian of a central-force system, so is conserved by the motion.

```lean
lemma poissonBracket_angularMomentumSq_hamiltonian (p : EuclideanSpace ℝ (Fin 3))
    {q : EuclideanSpace ℝ (Fin 3)} (hq : q ≠ 0) :
    poissonBracket angularMomentumSq S.hamiltonian p q = 0
```

**`ClassicalMechanics.CentralForce.poissonBracket_angularMomentumZ_hamiltonian`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean#L266).

> Away from the centre of force, the z-component of the angular momentum Poisson-commutes with
> the Hamiltonian of a central-force system, so is conserved by the motion.

```lean
lemma poissonBracket_angularMomentumZ_hamiltonian (p : EuclideanSpace ℝ (Fin 3))
    {q : EuclideanSpace ℝ (Fin 3)} (hq : q ≠ 0) :
    poissonBracket angularMomentumZ S.hamiltonian p q = 0
```

## Depends on

- [The Poisson bracket](../../../physlib/classicalmechanics/hamiltonianmechanics/poissonbracket.md)
- [Central forces](basic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/CentralForce/AngularMomentum.lean)
