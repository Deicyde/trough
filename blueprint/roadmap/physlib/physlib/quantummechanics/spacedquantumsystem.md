---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDQuantumSystem, QuantumMechanics.SpaceDQuantumSystem.HS, QuantumMechanics.SpaceDQuantumSystem.m_pos, QuantumMechanics.SpaceDQuantumSystem.m_nonneg, QuantumMechanics.SpaceDQuantumSystem.m_ne_zero, QuantumMechanics.SpaceDQuantumSystem.kineticCLM, QuantumMechanics.SpaceDQuantumSystem.kineticCLM_eq, QuantumMechanics.SpaceDQuantumSystem.kineticOperator
statement: formalized
proof: formalized
---

# Single-particle quantum system on `Space d`

The module `Physlib.QuantumMechanics.SpaceDQuantumSystem`, [Physlib/QuantumMechanics/SpaceDQuantumSystem.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean): 22 declarations, 9 with a docstring.

## i. Overview

> In this module we introduce the general notion of a single-particle quantum system on `Space d`.
>
> The structure `SpaceDQuantumSystem` encompasses the basic information needed to specify the system,
> namely the number of spatial dimensions, the particle's mass and the potential function.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.SpaceDQuantumSystem`**, a structure, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L49).

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

**`QuantumMechanics.SpaceDQuantumSystem.HS`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L62).

> The Hilbert space, `SpaceDHilbertSpace d`.

```lean
abbrev HS (_ : SpaceDQuantumSystem d)
```

## A. Basic properties

**`QuantumMechanics.SpaceDQuantumSystem.m_pos`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L69).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.SpaceDQuantumSystem.m_nonneg`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L72).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.SpaceDQuantumSystem.m_ne_zero`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L75).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

## B. Operators

### B.1. Kinetic energy

**`QuantumMechanics.SpaceDQuantumSystem.kineticCLM`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L90).

> The kinetic operator `(2m)⁻¹𝐩²` as a continuous linear map on Schwartz space.

```lean
def kineticCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticCLM_eq`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L92).

```lean
lemma kineticCLM_eq : Q.kineticCLM = (2 * Q.m)⁻¹ • (𝐩 ⬝ᵥ 𝐩)
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticOperator`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L95).

> The kinetic operator as an unbounded operator with domain `schwartzSubmodule Q.d`.

```lean
def kineticOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.kineticOperator_eq`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L97).

```lean
lemma kineticOperator_eq : Q.kineticOperator = ofReal (2 * Q.m)⁻¹ • momentumSqOperator
```

### B.2. Potential energy

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L105).

> The potential operator as a continuous linear map on Schwartz space,
> where `Q.potential` is a function of temperate growth.

```lean
def potentialCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_eq`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L107).

```lean
lemma potentialCLM_eq : Q.potentialCLM = smulLeftCLM ℂ (ofReal ∘ Q.potential)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L109).

```lean
lemma potentialCLM_apply (h_HTG : Q.potential.HasTemperateGrowth) (ψ : 𝓢(Space d, ℂ)) :
    Q.potentialCLM ψ = fun x ↦ Q.potential x • ψ x
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialCLM_apply_apply`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L115).

```lean
lemma potentialCLM_apply_apply
    (h_HTG : Q.potential.HasTemperateGrowth) (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    Q.potentialCLM ψ x = Q.potential x • ψ x
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L122).

> The potential operator as a self-adjoint, unbounded multiplication operator
> with domain `{ψ ∈ Q.HS | Q.potential • ψ ∈ Q.HS}`.

```lean
def potentialOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_eq`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L124).

```lean
lemma potentialOperator_eq : Q.potentialOperator = 𝓜 volume (ofReal ∘ Q.potential)
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_isSelfAdjoint`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L126).

```lean
lemma potentialOperator_isSelfAdjoint (h_AESM : AEStronglyMeasurable Q.potential) :
    IsSelfAdjoint Q.potentialOperator
```

**`QuantumMechanics.SpaceDQuantumSystem.potentialOperator_domain_ge`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L130).

```lean
lemma potentialOperator_domain_ge (h_HTG : Q.potential.HasTemperateGrowth) :
    SchwartzSubmodule d ≤ Q.potentialOperator.domain
```

### B.3. Hamiltonian

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianCLM`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L140).

> The Hamiltonian operator as a continuous linear map on Schwartz space,
> where `Q.potential` is a function of temperate growth.

```lean
def hamiltonianCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianCLM_eq`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L142).

```lean
lemma hamiltonianCLM_eq : Q.hamiltonianCLM = Q.kineticCLM + Q.potentialCLM
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianOperator`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L145).

> The Hamilontian operator as a symmetric unbounded operator.

```lean
def hamiltonianOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.SpaceDQuantumSystem.hamiltonianOperator_eq`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L147).

```lean
lemma hamiltonianOperator_eq : Q.hamiltonianOperator = Q.kineticOperator + Q.potentialOperator
```

## C. Reflectionless systems in one dimension

**`QuantumMechanics.SpaceDQuantumSystem.IsReflectionless`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean#L164).

> A system in one dimension is reflectionless if for every wavenumber `k ≠ 0` there is a
> generalized eigenvector `⟨Ψ|` of the Hamiltonian in the strong dual of the Schwartz space, with
> energy `ℏ² k² / (2 m)`, which looks like a non-zero multiple of the plane wave bra `⟨k|` at both
> ends. Far away is probed by translating a test function by `a`:
> `e^{i k a} ⟨Ψ|τₐ φ⟩ → T ⟨k|φ⟩` as `a → ∞`, and likewise with `T'` as `a → -∞`. A reflected wave
> `e^{-i k x}` would add a term oscillating like `e^{2 i k a}`, so the limits would not exist.

```lean
def IsReflectionless (Q : SpaceDQuantumSystem 1) : Prop
```

## Depends on

- [Momentum states](hilbertspaces/spaced/momentumstates.md)
- [Multiplication operators on `SpaceDHilbertSpace`](operators/spaced-multiplication.md)
- [Translations on space](../spaceandtime/space/part-01/translations.md)

## Sources

- [Physlib/QuantumMechanics/SpaceDQuantumSystem.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/SpaceDQuantumSystem.lean)
