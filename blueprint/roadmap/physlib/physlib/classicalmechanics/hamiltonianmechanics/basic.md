---
declaration: module
origin: cited
lean: ClassicalMechanics.HamiltonianSystem, ClassicalMechanics.HamiltonianSystem.ofCoordinates, ClassicalMechanics.HamiltonianSystem.ofNormedSpace, ClassicalMechanics.HamiltonianSystem.mem_domain_ofNormedSpace, ClassicalMechanics.HamiltonianSystem.hamiltonian_ofNormedSpace, ClassicalMechanics.HamiltonianSystem.ofInnerProductSpace, ClassicalMechanics.HamiltonianSystem.mem_domain_ofInnerProductSpace, ClassicalMechanics.HamiltonianSystem.hamiltonian_ofInnerProductSpace
statement: formalized
proof: formalized
---

# Hamiltonian systems

The module `Physlib.ClassicalMechanics.HamiltonianMechanics.Basic`, [Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean): 8 declarations, 8 with a docstring.

> Smooth time-dependent Hamiltonians on open domains of cotangent phase space.

## i. Overview

> A Hamiltonian system specifies a Hamiltonian and an open domain in the phase space of a
> configuration space. Smoothness is required on that domain, allowing potentials which are
> singular elsewhere, as in central-force systems away from the centre of force.
>
> The coordinate constructors use the global phase-space diffeomorphisms. They preserve the
> momentum-first convention `(p, q)` of the existing Hamilton equations and Poisson brackets.
> Time retains its affine manifold structure, so constructing a system does not choose a time origin.

## ii. Key results

> - `HamiltonianSystem` : a smooth Hamiltonian with an open phase-space domain.
> - `HamiltonianSystem.ofCoordinates` : a system from global phase-space coordinates.
> - `HamiltonianSystem.ofNormedSpace` : a system from covector-position coordinates.
> - `HamiltonianSystem.ofInnerProductSpace` : a system from momentum-vector-position coordinates.

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]

## A. Hamiltonian systems and their domains

**`ClassicalMechanics.HamiltonianSystem`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L60).

> A time-dependent Hamiltonian smooth on an open domain of the cotangent phase space.
> The Hamiltonian is represented by a total function, with smoothness required on the domain.

```lean
structure HamiltonianSystem where
  /-- The phase-space domain on which the system is defined. -/
  domain : Set (PhaseSpace I Q)
  /-- The phase-space domain is open. -/
  isOpen_domain : IsOpen domain
  /-- The Hamiltonian as a function of time and phase-space state. -/
  hamiltonian : Time × PhaseSpace I Q → ℝ
  /-- The Hamiltonian is smooth in time and state on its domain. -/
  contMDiffOn_hamiltonian : ContMDiffOn
    (𝓘(ℝ, ℝ).prod (I.prod 𝓘(ℝ, E →L[ℝ] ℝ))) 𝓘(ℝ, ℝ) ∞ hamiltonian (Set.univ ×ˢ domain)
```

## B. Coordinate constructors

**`ClassicalMechanics.HamiltonianSystem.ofCoordinates`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L85).

> Pull a Hamiltonian and its domain back along global phase-space coordinates.

```lean
def ofCoordinates {P : Type*} [NormedAddCommGroup P] [NormedSpace ℝ P]
    (e : PhaseSpace I Q ≃ₘ^∞ ⟮I.prod 𝓘(ℝ, E →L[ℝ] ℝ), 𝓘(ℝ, P)⟯ P)
    (U : Set P) (hU : IsOpen U) (H : Time × P → ℝ)
    (hH : ContMDiffOn (𝓘(ℝ, ℝ).prod 𝓘(ℝ, P)) 𝓘(ℝ, ℝ) ∞ H (Set.univ ×ˢ U)) :
    HamiltonianSystem I Q
```

**`ClassicalMechanics.HamiltonianSystem.ofNormedSpace`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L104).

> The Hamiltonian system on a normed space given by `H(t, p, q)` on an open domain `U`,
> with momentum `p` in the continuous dual.

```lean
def ofNormedSpace : HamiltonianSystem 𝓘(ℝ, E) ⟨E⟩
```

**`ClassicalMechanics.HamiltonianSystem.mem_domain_ofNormedSpace`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L109).

> The coordinate constructor preserves membership in the Hamiltonian's domain.

```lean
lemma mem_domain_ofNormedSpace (p : E →L[ℝ] ℝ) (q : E) :
    PhaseSpace.ofNormedSpace p q ∈ (ofNormedSpace U hU H hH).domain ↔ (p, q) ∈ U
```

**`ClassicalMechanics.HamiltonianSystem.hamiltonian_ofNormedSpace`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L117).

> The coordinate constructor preserves the value of the Hamiltonian.

```lean
lemma hamiltonian_ofNormedSpace (t : Time) (p : E →L[ℝ] ℝ) (q : E) :
    (ofNormedSpace U hU H hH).hamiltonian (t, PhaseSpace.ofNormedSpace p q) = H (t, p, q)
```

**`ClassicalMechanics.HamiltonianSystem.ofInnerProductSpace`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L134).

> The Hamiltonian system on a real Hilbert space given by `H(t, p, q)` on an open domain `U`,
> with momentum represented by a vector using the Riesz map.

```lean
def ofInnerProductSpace : HamiltonianSystem 𝓘(ℝ, E) ⟨E⟩
```

**`ClassicalMechanics.HamiltonianSystem.mem_domain_ofInnerProductSpace`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L139).

> The vector-coordinate constructor preserves membership in the Hamiltonian's domain.

```lean
lemma mem_domain_ofInnerProductSpace (p q : E) :
    PhaseSpace.ofInnerProductSpace p q ∈ (ofInnerProductSpace U hU H hH).domain ↔ (p, q) ∈ U
```

**`ClassicalMechanics.HamiltonianSystem.hamiltonian_ofInnerProductSpace`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean#L147).

> The vector-coordinate constructor preserves the value of the Hamiltonian.

```lean
lemma hamiltonian_ofInnerProductSpace (t : Time) (p q : E) :
    (ofInnerProductSpace U hU H hH).hamiltonian (t, PhaseSpace.ofInnerProductSpace p q) =
      H (t, p, q)
```

## Depends on

- [Canonical phase spaces](../phasespace/basic.md)
- [Time](../../spaceandtime/time/basic.md)

## Sources

- [Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/HamiltonianMechanics/Basic.lean)
