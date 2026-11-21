---
declaration: module
origin: cited
lean: ClassicalMechanics.CentralForce.integrabilityDomain, ClassicalMechanics.CentralForce.integrabilityDomain_eq, ClassicalMechanics.CentralForce.isOpen_integrabilityDomain, ClassicalMechanics.CentralForce.dense_integrabilityDomain, ClassicalMechanics.CentralForce.snd_ne_zero_of_mem_integrabilityDomain, ClassicalMechanics.CentralForce.linearIndependent_gradients, ClassicalMechanics.CentralForce.linearIndependent_conservedQuantities, ClassicalMechanics.CentralForce.liouvilleIntegrable
statement: formalized
proof: formalized
---

# Central-force systems are Liouville integrable

The module `PhyslibAlpha.ClassicalMechanics.CentralForce.LiouvilleIntegrable`, [PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean): 9 declarations, 9 with a docstring.

> Independence and involution of the Hamiltonian, squared angular momentum and axial component.

## i. Overview

> The Hamiltonian `H`, squared angular momentum `L²` and axial component `L_z` are independent
> and in involution on the open dense domain where the radial momentum is non-zero and the
> angular momentum is not parallel to the z-axis. This proves Liouville integrability for every
> central-force system. The domain is sufficient; no maximality claim is made.
>
> Independence follows by pairing a vanishing combination of gradients with radial changes of
> momentum, infinitesimal rotations and momentum scaling, successively eliminating its coefficients.

## ii. Key results

> - `CentralForce.integrabilityDomain` : the chosen domain in phase space.
> - `CentralForce.isOpen_integrabilityDomain`, `CentralForce.dense_integrabilityDomain` : it is
>   open and dense.
> - `CentralForce.snd_ne_zero_of_mem_integrabilityDomain` : it excludes the centre of force.
> - `CentralForce.linearIndependent_conservedQuantities` : the observables are independent there.
> - `CentralForce.liouvilleIntegrable` : the resulting Liouville-integrability construction.
> - `CentralForce.toHamiltonianSystem_isLiouvilleIntegrableOn` : the shared Hamiltonian system is
>   integrable on the same coordinate domain.

## iv. References

> * V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd edition,
>   Chapter 10. [ref: arnold\_mechanics]

## A. The domain of integrability

**`ClassicalMechanics.CentralForce.integrabilityDomain`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L65).

> The phase-space domain where the radial momentum is non-zero and the angular momentum
> is not parallel to the z-axis, used to establish central-force integrability.

```lean
def integrabilityDomain : Set (EuclideanSpace ℝ (Fin 3) × EuclideanSpace ℝ (Fin 3))
```

**`ClassicalMechanics.CentralForce.integrabilityDomain_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L69).

> The domain is the non-vanishing set of a polynomial in the phase-space coordinates.

```lean
lemma integrabilityDomain_eq : integrabilityDomain =
    {x | (x.1 0 * x.2 0 + x.1 1 * x.2 1 + x.1 2 * x.2 2) *
      ((x.2 1 * x.1 2 - x.2 2 * x.1 1) ^ 2 + (x.2 2 * x.1 0 - x.2 0 * x.1 2) ^ 2) ≠ 0}
```

**`ClassicalMechanics.CentralForce.isOpen_integrabilityDomain`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L78).

> The chosen central-force domain is open.

```lean
lemma isOpen_integrabilityDomain : IsOpen integrabilityDomain
```

**`ClassicalMechanics.CentralForce.dense_integrabilityDomain`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L83).

> The chosen central-force domain is dense.

```lean
lemma dense_integrabilityDomain : Dense integrabilityDomain
```

**`ClassicalMechanics.CentralForce.snd_ne_zero_of_mem_integrabilityDomain`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L99).

> The chosen domain excludes the centre of force.

```lean
lemma snd_ne_zero_of_mem_integrabilityDomain
    {x : EuclideanSpace ℝ (Fin 3) × EuclideanSpace ℝ (Fin 3)} (hx : x ∈ integrabilityDomain) :
    x.2 ≠ 0
```

## B. Functional independence

**`ClassicalMechanics.CentralForce.linearIndependent_gradients`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L117).

> On the domain of integrability, a phase-space function whose momentum gradient is a non-zero
> multiple `a • p` of the momentum and whose position gradient is a multiple `c • q` of the
> position, such as the Hamiltonian of a central-force system, is functionally independent of `L²`
> and `L_z`: the three phase-space gradients are linearly independent.

```lean
lemma linearIndependent_gradients {p q : EuclideanSpace ℝ (Fin 3)} {a c : ℝ} (ha : a ≠ 0)
    (hx : (p, q) ∈ integrabilityDomain) :
    LinearIndependent ℝ ![(a • p, c • q),
      ((2 * ⟪q, q⟫_ℝ) • p - (2 * ⟪q, p⟫_ℝ) • q, (2 * ⟪p, p⟫_ℝ) • q - (2 * ⟪q, p⟫_ℝ) • p),
      (q 0 • EuclideanSpace.single 1 1 - q 1 • EuclideanSpace.single 0 1,
        p 1 • EuclideanSpace.single 0 1 - p 0 • EuclideanSpace.single 1 1)]
```

**`ClassicalMechanics.CentralForce.linearIndependent_conservedQuantities`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L169).

> On the domain of integrability, the conserved quantities of a central-force system are
> functionally independent: their phase-space gradients are linearly independent.

```lean
lemma linearIndependent_conservedQuantities
    {x : EuclideanSpace ℝ (Fin 3) × EuclideanSpace ℝ (Fin 3)} (hx : x ∈ integrabilityDomain) :
    LinearIndependent ℝ (fun i => (gradient (fun p' => S.conservedQuantities i p' x.2) x.1,
      gradient (fun q' => S.conservedQuantities i x.1 q') x.2))
```

## C. Liouville integrability

**`ClassicalMechanics.CentralForce.liouvilleIntegrable`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L185).

> Every central-force system is Liouville integrable on the domain of integrability, with the
> Hamiltonian, the squared magnitude of the angular momentum and its z-component as conserved
> quantities.

```lean
noncomputable def liouvilleIntegrable :
    LiouvilleIntegrableOn integrabilityDomain S.hamiltonian
```

**`ClassicalMechanics.CentralForce.toHamiltonianSystem_isLiouvilleIntegrableOn`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean#L202).

> The Hamiltonian system associated with a central force is Liouville integrable on the
> coordinate domain of integrability.

```lean
lemma toHamiltonianSystem_isLiouvilleIntegrableOn :
    S.toHamiltonianSystem.IsLiouvilleIntegrableOn integrabilityDomain
```

## Depends on

- [Conserved quantities for central forces](conservedquantities.md)
- [Liouville integrable systems](../liouvilleintegrable/basic.md)

## Proof depends on

- [Analyticity and dense non-vanishing sets](../../../physlib/mathematics/formathlib/part-01/analytic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/LiouvilleIntegrable.lean)
