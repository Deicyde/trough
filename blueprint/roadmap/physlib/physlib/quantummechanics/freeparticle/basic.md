---
declaration: module
origin: cited
lean: QuantumMechanics.FreeParticle, QuantumMechanics.FreeParticle.m_pos, QuantumMechanics.FreeParticle.m_nonneg, QuantumMechanics.FreeParticle.m_ne_zero, QuantumMechanics.FreeParticle.HS, QuantumMechanics.FreeParticle.hamiltonian
statement: formalized
proof: formalized
---

# The free particle on `Space d`

The module `Physlib.QuantumMechanics.FreeParticle.Basic`, [Physlib/QuantumMechanics/FreeParticle/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean): 6 declarations, 3 with a docstring.

## i. Overview

> The free quantum particle is one of the simplest quantum systems.
> States for a particle of mass `m` are elements of `SpaceDHilbertSpace d` and evolve according
> to the Hamiltonian `p²/2m` with no potential.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.FreeParticle`**, a structure, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L40).

> A free, spinless quantum particle with mass `m > 0` in `Space d`.

```lean
structure FreeParticle (d : ℕ) where
  /-- The mass (positive). -/
  m : ℝ
  hm : 0 < m
```

## A. Basic properties

**`QuantumMechanics.FreeParticle.m_pos`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L54).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.FreeParticle.m_nonneg`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L57).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.FreeParticle.m_ne_zero`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L60).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

## B. Hilbert space

**`QuantumMechanics.FreeParticle.HS`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L68).

> The Hilbert space for the free particle.

```lean
abbrev HS (_ : FreeParticle d) : Type _
```

## C. Hamiltonian

**`QuantumMechanics.FreeParticle.hamiltonian`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean#L75).

> The Hamiltonian, `p²/(2m)`.

```lean
def hamiltonian : Q.HS →ₗ.[ℂ] Q.HS
```

## D. As a quantum system

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Momentum operators](../operators/momentum.md)

## Sources

- [Physlib/QuantumMechanics/FreeParticle/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/FreeParticle/Basic.lean)
