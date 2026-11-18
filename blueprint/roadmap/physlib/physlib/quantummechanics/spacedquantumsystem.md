---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDQuantumSystem, QuantumMechanics.SpaceDQuantumSystem.HS, QuantumMechanics.SpaceDQuantumSystem.m_pos, QuantumMechanics.SpaceDQuantumSystem.m_nonneg, QuantumMechanics.SpaceDQuantumSystem.m_ne_zero, QuantumMechanics.SpaceDQuantumSystem.kineticCLM, QuantumMechanics.SpaceDQuantumSystem.kineticCLM_eq, QuantumMechanics.SpaceDQuantumSystem.kineticOperator
statement: formalized
proof: formalized
---

# Single-particle quantum system on `Space d`

The module `Physlib.QuantumMechanics.SpaceDQuantumSystem`, [Physlib/QuantumMechanics/SpaceDQuantumSystem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean): 21 declarations, 8 with a docstring.

## i. Overview

> In this module we introduce the general notion of a single-particle quantum system on `Space d`.
>
> The structure `SpaceDQuantumSystem` encompasses the basic information needed to specify the system,
> namely the number of spatial dimensions, the particle's mass and the potential function.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.SpaceDQuantumSystem`**, a structure, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L47).

> A single-particle quantum system with Hilbert space `SpaceDHilbertSpace d`,
> characterized by the particle's mass `m > 0` and potential function `potential : Space d → ℝ`.

```lean
structure SpaceDQuantumSystem (d : ℕ) where
  /-- The mass (positive). -/
  m : ℝ
  hm : 0 < m
  /-- The potential function. -/
  potential : Space d → ℝ
```

**`QuantumMechanics.SpaceDQuantumSystem.HS`**, an abbrev, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L60).

> The Hilbert space, `SpaceDHilbertSpace d`.

```lean
abbrev HS (_ : SpaceDQuantumSystem d)
```

## A. Basic properties

**`QuantumMechanics.SpaceDQuantumSystem.m_pos`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L67).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.SpaceDQuantumSystem.m_nonneg`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L70).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.SpaceDQuantumSystem.m_ne_zero`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L73).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

## B. Operators

### B.1. Kinetic energy

**`QuantumMechanics.SpaceDQuantumSystem.kineticCLM`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L88).

> The kinetic operator `(2m)⁻¹𝐩²` as a continuous linear map on Schwartz space.

```lean
def kineticCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticCLM_eq`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L90).

```lean
lemma kineticCLM_eq : Q.kineticCLM = (2 * Q.m)⁻¹ • (𝐩 ⬝ᵥ 𝐩)
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticOperator`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L93).

> The kinetic operator as an unbounded operator with domain `schwartzSubmodule Q.d`.

```lean
def kineticOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticOperator_eq`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L95).

```lean
lemma kineticOperator_eq : Q.kineticOperator = ofReal (2 * Q.m)⁻¹ • momentumSqOperator
```

### B.2. Potential energy

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L103).

> The potential operator as a continuous linear map on Schwartz space,
> where `Q.potential` is a function of temperate growth.

```lean
def potentialCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_eq`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L105).

```lean
lemma potentialCLM_eq : Q.potentialCLM = smulLeftCLM ℂ (ofReal ∘ Q.potential)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L107).

```lean
lemma potentialCLM_apply (h_HTG : Q.potential.HasTemperateGrowth) (ψ : 𝓢(Space d, ℂ)) :
    Q.potentialCLM ψ = fun x ↦ Q.potential x • ψ x
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_apply_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L113).

```lean
lemma potentialCLM_apply_apply
    (h_HTG : Q.potential.HasTemperateGrowth) (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    Q.potentialCLM ψ x = Q.potential x • ψ x
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L120).

> The potential operator as a self-adjoint, unbounded multiplication operator
> with domain `{ψ ∈ Q.HS | Q.potential • ψ ∈ Q.HS}`.

```lean
def potentialOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_eq`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L122).

```lean
lemma potentialOperator_eq : Q.potentialOperator = 𝓜 volume (ofReal ∘ Q.potential)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_isSelfAdjoint`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L124).

```lean
lemma potentialOperator_isSelfAdjoint (h_AESM : AEStronglyMeasurable Q.potential) :
    IsSelfAdjoint Q.potentialOperator
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_domain_ge`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L128).

```lean
lemma potentialOperator_domain_ge (h_HTG : Q.potential.HasTemperateGrowth) :
    SchwartzSubmodule d ≤ Q.potentialOperator.domain
```

### B.3. Hamiltonian

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianCLM`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L138).

> The Hamiltonian operator as a continuous linear map on Schwartz space,
> where `Q.potential` is a function of temperate growth.

```lean
def hamiltonianCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianCLM_eq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L140).

```lean
lemma hamiltonianCLM_eq : Q.hamiltonianCLM = Q.kineticCLM + Q.potentialCLM
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianOperator`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L143).

> The Hamilontian operator as a symmetric unbounded operator.

```lean
def hamiltonianOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianOperator_eq`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L145).

```lean
lemma hamiltonianOperator_eq : Q.hamiltonianOperator = Q.kineticOperator + Q.potentialOperator
```

## Depends on

- [Momentum operators](operators/momentum.md)
- [Multiplication operators on `SpaceDHilbertSpace`](operators/multiplication.md)

## Sources

- [Physlib/QuantumMechanics/SpaceDQuantumSystem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean)
