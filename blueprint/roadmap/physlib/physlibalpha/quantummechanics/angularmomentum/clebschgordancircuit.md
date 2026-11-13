---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.cgK, PhyslibAlpha.Sl2.cgL, PhyslibAlpha.Sl2.cgMatrix, PhyslibAlpha.Sl2.CH21, PhyslibAlpha.Sl2.cnot_mul_CH21, PhyslibAlpha.Sl2.CH21_mem_unitaryGroup, PhyslibAlpha.Sl2.cgMatrix_mem_unitaryGroup
statement: formalized
proof: formalized
---

# A two-qubit circuit for the Clebsch–Gordan coefficients of two spins ½

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.ClebschGordanCircuit`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean): 7 declarations, 7 with a docstring.

> The change of basis from the product basis to the coupled basis of two spins `1/2` as a
> two-qubit circuit.

## i. Overview

> A spin `1/2` is a qubit with `|↑⟩ = |0⟩` and `|↓⟩ = |1⟩`. The product basis of two spins is
> indexed by `Qubit × Qubit`, in the order `|00⟩, |01⟩, |10⟩, |11⟩ = |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩`; the
> first qubit is the first spin. The coupled basis is indexed by `Qubit × Qubit` as well, the
> columns `(0,0), (0,1), (1,0), (1,1)` being the triplet states `|1, 1⟩, |1, 0⟩, |1, -1⟩` and the
> singlet `|0, 0⟩`. The matrix `cgMatrix` of the change of basis has the Clebsch–Gordan
> coefficients `cgCoefficient 1 1 k l a b` of `ClebschGordanCoefficients` as entries, with
> Condon–Shortley phases.
>
> It is the matrix of the circuit which first applies a Hadamard gate to the first qubit
> controlled by the second (`CH21`), then the CNOT gate with the first qubit as control:
> `CNOT * CH21 = cgMatrix` (`cnot_mul_CH21`). In particular `cgMatrix` is unitary
> (`cgMatrix_mem_unitaryGroup`).

## ii. Key results

> - `cgMatrix`: the Clebsch–Gordan matrix of two spins `1/2`.
> - `CH21`: the controlled Hadamard gate with the second qubit as control.
> - `cnot_mul_CH21`: the circuit `CNOT * CH21` is the Clebsch–Gordan matrix.
> - `cgMatrix_mem_unitaryGroup`: the Clebsch–Gordan matrix is unitary.

## iv. References

> - The Clebsch–Gordan coefficients and their phase convention are those of
>   `ClebschGordanCoefficients`; the gates are those of `QuantumInfo.States.Pure.Qubit`.

## A. The Clebsch–Gordan matrix and the circuit

**`PhyslibAlpha.Sl2.cgK`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L63).

> The label `k` of the coupled state in column `q`: `0` for the triplet, `1` for the singlet
> `q = (1, 1)`.

```lean
def cgK (q : Qubit × Qubit) : ℕ
```

**`PhyslibAlpha.Sl2.cgL`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L67).

> The label `l = J - M` of the coupled state in column `q`: the columns `(0,0), (0,1), (1,0)`
> are the triplet states with `M = 1, 0, -1`, the column `(1,1)` the singlet.

```lean
def cgL (q : Qubit × Qubit) : ℕ
```

**`PhyslibAlpha.Sl2.cgMatrix`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L71).

> The Clebsch–Gordan matrix of two spins `1/2`: the entry in row `(a, b)` and column `q` is
> `⟨½ m₁ ½ m₂ | J M⟩` with `m₁ = ½ - a`, `m₂ = ½ - b` and `J, M` given by `cgK q`, `cgL q`.

```lean
def cgMatrix : Matrix (Qubit × Qubit) (Qubit × Qubit) ℂ
```

**`PhyslibAlpha.Sl2.CH21`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L75).

> The Hadamard gate on the first qubit controlled by the second qubit.

```lean
def CH21 : Matrix (Qubit × Qubit) (Qubit × Qubit) ℂ
```

**`PhyslibAlpha.Sl2.cnot_mul_CH21`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L79).

> The circuit `CH21` followed by `CNOT` is the Clebsch–Gordan matrix of two spins `1/2`.

```lean
lemma cnot_mul_CH21 : CNOT.val * CH21 = cgMatrix
```

**`PhyslibAlpha.Sl2.CH21_mem_unitaryGroup`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L90).

> `CH21` is unitary, as a reindexing of the unitary `C[H]`.

```lean
lemma CH21_mem_unitaryGroup : CH21 ∈ Matrix.unitaryGroup (Qubit × Qubit) ℂ
```

**`PhyslibAlpha.Sl2.cgMatrix_mem_unitaryGroup`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean#L96).

> The Clebsch–Gordan matrix of two spins `1/2` is unitary.

```lean
lemma cgMatrix_mem_unitaryGroup : cgMatrix ∈ Matrix.unitaryGroup (Qubit × Qubit) ℂ
```

## Depends on

- [Clebsch–Gordan coefficients](clebschgordancoefficients.md)
- [Qubits](../../../quantuminfo/states/pure/qubit.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCircuit.lean)
