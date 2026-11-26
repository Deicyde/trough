---
declaration: module
origin: cited
lean: ClassicalMechanics.LiouvilleIntegrableOn, ClassicalMechanics.HamiltonianSystem.LiouvilleIntegrabilityData, ClassicalMechanics.HamiltonianSystem.IsLiouvilleIntegrableOn, ClassicalMechanics.LiouvilleIntegrableOn.deriv_comp_eq_zero, ClassicalMechanics.LiouvilleIntegrableOn.oneDegreeOfFreedom
statement: formalized
proof: formalized
---

# Liouville integrable systems

The module `PhyslibAlpha.ClassicalMechanics.LiouvilleIntegrable.Basic`, [PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean): 5 declarations, 5 with a docstring.

> Liouville integrability on an open dense domain and conservation along Hamiltonian trajectories.

## i. Overview

> A Hamiltonian system on a `2d`-dimensional phase space is *Liouville integrable* when it carries
> `d` conserved quantities, one per degree of freedom, that are
>
> - smooth,
> - pairwise Poisson-commuting ("in involution"), and
> - functionally independent, i.e. their phase-space gradients are linearly independent.
>
> Functional independence need not hold at every point of phase space: the
> gradient of the Hamiltonian of the harmonic oscillator vanishes at the equilibrium, and the Kepler
> Hamiltonian is singular at the origin of position space. The definition therefore asks for the
> conditions on an open *domain* `U` of phase space, which must be dense so that the conditions hold
> generically. Without density the empty domain would make every Hamiltonian integrable.
>
> These are the integrability conditions used in the Liouville–Arnold theorem. …
>
> With one degree of freedom the conditions collapse: the Hamiltonian is the only conserved quantity,
> involution is automatic, and independence says only that the gradient of the Hamiltonian does not
> vanish. `LiouvilleIntegrableOn.oneDegreeOfFreedom` records this, and is how the harmonic oscillator
> and the simple pendulum are shown to be integrable.
>
> Following the convention of `poissonBracket`, a phase-space function `f : X → X → ℝ` is read as
> `f p q` for a momentum `p` and a position `q`. Since PhysLib has no existing precedent for a
> `FiniteDimensional`/`Module.finrank` hypothesis on an abstract phase space, position space is fixed
> concretely as `EuclideanSpace ℝ (Fin d)` for an explicit `d : ℕ`, matching the indexing convention
> already used for e.g. `RigidBody (d : ℕ)`.

## ii. Key results

> - `LiouvilleIntegrableOn` : the structure of a Liouville integrable system for a Hamiltonian `H`
>   on an open dense domain `U` of phase space.
> - `HamiltonianSystem.LiouvilleIntegrabilityData` : an autonomous coordinate Hamiltonian and its
>   integrability data, related to a Hamiltonian system on a coordinate domain.
> - `HamiltonianSystem.IsLiouvilleIntegrableOn` : coordinate integrability for a Hamiltonian system,
>   including agreement with an autonomous Hamiltonian on the integrability domain.
> - `LiouvilleIntegrableOn.deriv_comp_eq_zero` : each conserved quantity has zero time derivative
>   along a solution of Hamilton's equations for `H` which stays in `U`.
> - `LiouvilleIntegrableOn.oneDegreeOfFreedom` : a system with one degree of freedom is Liouville
>   integrable wherever its Hamiltonian is smooth with non-vanishing gradient.

## iv. References

> * V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd edition, Chapter 10.

## A. The definition of Liouville integrability

**`ClassicalMechanics.LiouvilleIntegrableOn`**, a structure, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean#L94).

> A Liouville integrable system for a Hamiltonian `H` on an open dense domain `U` of the
> `2d`-dimensional phase space `EuclideanSpace ℝ (Fin d) × EuclideanSpace ℝ (Fin d)`, whose points
> are read as `(p, q)`: `d` smooth conserved quantities, one per degree of freedom, that are pairwise
> in involution and functionally independent at every point of `U`.

```lean
structure LiouvilleIntegrableOn {d : ℕ}
    (U : Set (EuclideanSpace ℝ (Fin d) × EuclideanSpace ℝ (Fin d)))
    (H : EuclideanSpace ℝ (Fin d) → EuclideanSpace ℝ (Fin d) → ℝ) where
  /-- The domain on which the system is integrable is open. -/
  isOpen : IsOpen U
  /-- The domain on which the system is integrable is dense, i.e. integrability holds
  generically. -/
  dense : Dense U
  /-- The `d` conserved quantities, one per degree of freedom. -/
  f : Fin d → EuclideanSpace ℝ (Fin d) → EuclideanSpace ℝ (Fin d) → ℝ
  /-- The conserved quantities are smooth on `U`. -/
  contDiffOn : ∀ i, ContDiffOn ℝ ∞ (Function.uncurry (f i)) U
  /-- The Hamiltonian itself is one of the conserved quantities. -/
  exists_hamiltonian : ∃ i, f i = H
  /-- The conserved quantities pairwise Poisson-commute on `U`, i.e. are in involution. -/
  involutive : ∀ i j, ∀ x ∈ U, poissonBracket (f i) (f j) x.1 x.2 = 0
  /-- The conserved quantities are functionally independent on `U`: their phase-space gradients
  (the `p`- and `q`-partials together) are linearly independent. -/
  independent : ∀ x ∈ U, LinearIndependent ℝ
    (fun i => (gradient (fun p' => f i p' x.2) x.1, gradient (fun q' => f i x.1 q') x.2))
```

### A.1. Integrability of Hamiltonian systems

**`ClassicalMechanics.HamiltonianSystem.LiouvilleIntegrabilityData`**, a structure, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean#L121).

> An autonomous coordinate Hamiltonian and its Liouville integrability data, related to a
> Hamiltonian system on a coordinate domain.

```lean
structure HamiltonianSystem.LiouvilleIntegrabilityData {d : ℕ}
    (S : HamiltonianSystem 𝓘(ℝ, EuclideanSpace ℝ (Fin d)) ⟨EuclideanSpace ℝ (Fin d)⟩)
    (U : Set (EuclideanSpace ℝ (Fin d) × EuclideanSpace ℝ (Fin d))) where
  /-- The autonomous Hamiltonian in momentum-position coordinates. -/
  coordinateHamiltonian : EuclideanSpace ℝ (Fin d) → EuclideanSpace ℝ (Fin d) → ℝ
  /-- The system agrees with the coordinate Hamiltonian on the domain at every time. -/
  hamiltonian_eq : ∀ t p q, (p, q) ∈ U →
    S.hamiltonian (t, PhaseSpace.ofInnerProductSpace p q) = coordinateHamiltonian p q
  /-- Coordinate states in the integrability domain belong to the system's domain. -/
  domain_subset : ∀ p q, (p, q) ∈ U → PhaseSpace.ofInnerProductSpace p q ∈ S.domain
  /-- The coordinate Hamiltonian has the Liouville integrability data. -/
  integrable : LiouvilleIntegrableOn U coordinateHamiltonian
```

**`ClassicalMechanics.HamiltonianSystem.IsLiouvilleIntegrableOn`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean#L137).

> A Hamiltonian system is Liouville integrable on a coordinate domain when that domain lies
> inside the system's domain and, for every time, the system agrees there with an autonomous
> coordinate Hamiltonian satisfying the Liouville integrability conditions.

```lean
def HamiltonianSystem.IsLiouvilleIntegrableOn {d : ℕ}
    (S : HamiltonianSystem 𝓘(ℝ, EuclideanSpace ℝ (Fin d)) ⟨EuclideanSpace ℝ (Fin d)⟩)
    (U : Set (EuclideanSpace ℝ (Fin d) × EuclideanSpace ℝ (Fin d))) : Prop
```

## B. Conservation along the flow

**`ClassicalMechanics.LiouvilleIntegrableOn.deriv_comp_eq_zero`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean#L150).

> Each conserved quantity of a Liouville integrable system has zero time derivative along a
> solution of Hamilton's equations for `H` which lies in the domain `U` at time `t`.

```lean
lemma LiouvilleIntegrableOn.deriv_comp_eq_zero {d : ℕ}
    {U : Set (EuclideanSpace ℝ (Fin d) × EuclideanSpace ℝ (Fin d))}
    {H : EuclideanSpace ℝ (Fin d) → EuclideanSpace ℝ (Fin d) → ℝ}
    (LI : LiouvilleIntegrableOn U H)
    (p q : Time → EuclideanSpace ℝ (Fin d)) (t : Time) (i : Fin d)
    (heq : hamiltonEqOp (fun _ => H) p q = 0)
    (hp : DifferentiableAt ℝ p t) (hq : DifferentiableAt ℝ q t) (hU : (p t, q t) ∈ U) :
    ∂ₜ (fun t => LI.f i (p t) (q t)) t = 0
```

## C. Systems with one degree of freedom

**`ClassicalMechanics.LiouvilleIntegrableOn.oneDegreeOfFreedom`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean#L176).

> A Hamiltonian system with one degree of freedom is Liouville integrable, with the Hamiltonian as
> its single conserved quantity, on any open dense domain on which the Hamiltonian is smooth and has
> non-vanishing phase-space gradient.

```lean
def LiouvilleIntegrableOn.oneDegreeOfFreedom
    {U : Set (EuclideanSpace ℝ (Fin 1) × EuclideanSpace ℝ (Fin 1))}
    {H : EuclideanSpace ℝ (Fin 1) → EuclideanSpace ℝ (Fin 1) → ℝ}
    (hU : IsOpen U) (hdense : Dense U) (hH : ContDiffOn ℝ ∞ (Function.uncurry H) U)
    (hgrad : ∀ x ∈ U,
      (gradient (fun p' => H p' x.2) x.1, gradient (fun q' => H x.1 q') x.2) ≠ 0) :
    LiouvilleIntegrableOn U H
```

## Depends on

- [Hamiltonian systems](../../../physlib/classicalmechanics/hamiltonianmechanics/basic.md)
- [The Poisson bracket](../../../physlib/classicalmechanics/hamiltonianmechanics/poissonbracket.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/LiouvilleIntegrable/Basic.lean)
