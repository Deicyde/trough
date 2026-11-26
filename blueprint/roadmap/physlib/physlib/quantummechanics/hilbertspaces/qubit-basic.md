---
declaration: module
origin: cited
lean: QuantumMechanics.Qubit, QuantumMechanics.Qubit.basis, QuantumMechanics.Qubit.basis_apply, QuantumMechanics.Qubit.finrank_eq_two
statement: formalized
proof: formalized
---

# The qubit

The module `Physlib.QuantumMechanics.HilbertSpaces.Qubit.Basic`, [Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean): 4 declarations, 3 with a docstring.

## i. Overview

> A qubit is a quantum system with two basis states. Its Hilbert space is `𝓗[Fin 2]`, the finite
> target Hilbert space over the two-element type `Fin 2`. The type `Qubit` is an abbreviation for
> it, so the instances of a complex Hilbert space (`QuantumHilbertSpace`) and the lemmas about
> `𝓗[Fin 2]` apply to `Qubit` directly. `Qubit.basis` is its standard orthonormal basis.

## ii. Key results

> - `Qubit` : the Hilbert space of a qubit.
> - `Qubit.basis` : its standard orthonormal basis, indexed by `Fin 2`.
> - `Qubit.finrank_eq_two` : it has dimension two.

## iv. References

> * None.

## A. The qubit and its basis

**`QuantumMechanics.Qubit`**, an abbrev, [line 48](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean#L48).

> The Hilbert space of a qubit, the quantum system with two basis states: `𝓗[Fin 2]`.

```lean
abbrev Qubit : Type
```

**`QuantumMechanics.Qubit.basis`**, an abbrev, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean#L53).

> The standard orthonormal basis of the qubit, indexed by `Fin 2`.

```lean
noncomputable abbrev basis : OrthonormalBasis (Fin 2) ℂ Qubit
```

**`QuantumMechanics.Qubit.basis_apply`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean#L56).

```lean
lemma basis_apply (i : Fin 2) : basis i = ⟨EuclideanSpace.single i 1⟩
```

**`QuantumMechanics.Qubit.finrank_eq_two`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean#L60).

> The Hilbert space of the qubit is two-dimensional.

```lean
lemma finrank_eq_two : Module.finrank ℂ Qubit = 2
```

## Depends on

- [The Hilbert space of a finite target quantum mechanical system](finitetarget-basic.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Qubit/Basic.lean)
