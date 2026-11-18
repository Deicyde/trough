---
declaration: module
origin: cited
lean: Qubit.X_Y_anticomm, Qubit.Y_Z_anticomm, Qubit.Z_X_anticomm, Qubit, Qubit.Z, Qubit.X, Qubit.Y, Qubit.H
statement: formalized
proof: formalized
---

# Qubits

The module `QuantumInfo.States.Pure.Qubit`, [QuantumInfo/States/Pure/Qubit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean): 32 declarations, 13 with a docstring, 3 listed as significant.

## i. Overview

> A qubit is a two-level quantum system. In this module the computational basis of a qubit is
> indexed by `Qubit`, an abbreviation for `Fin 2`, and a gate on a qubit is an element of
> `𝐔[Qubit]`, the group of unitary `2 × 2` complex matrices. The standard single-qubit gates are
> defined by their matrices in the computational basis, and the basic identities between them are
> proved. For a unitary matrix `g` indexed by a finite type `k`, the controlled gate `C[g]` acts on
> `Qubit × k`: it is the identity when the `Qubit` component, the control, is `0`, and applies `g`
> when it is `1`. The CNOT gate is `C[X]`.
>
> Most proofs use the tactic `matrix_expand`, defined at the start of the module, which reduces an
> equality of small matrices to its entries and tries to close them with `simp`, `norm_num`,
> `field_simp` and `ring_nf`.

## ii. Key results

> - `Qubit` : the index type `Fin 2` of the computational basis of a qubit.
> - `matrix_expand` : a tactic reducing an equality of small matrices to its entries and
>   simplifying them.
> - `Qubit.X`, `Qubit.Y`, `Qubit.Z` : the Pauli gates.
> - `Qubit.H`, `Qubit.S`, `Qubit.T` : the Hadamard gate and the gates `S = diag(1, i)` and
>   `T = diag(1, (1 + i) / √2)`.
> - `Qubit.X_Y_anticomm`, `Qubit.Y_Z_anticomm`, `Qubit.Z_X_anticomm` : the Pauli gates
>   anticommute.
> - `Qubit.controllize` : the controlled gate `C[g]` of a unitary `g`.
> - `Qubit.CNOT`, `Qubit.CNOT_matrix` : the CNOT gate and its `4 × 4` matrix, with `Fin 2 × Fin 2`
>   reindexed by `finProdFinEquiv`.
> - `Qubit.X_controllize_X` : conjugating `C[g]` by `X` on the control qubit gives
>   `(1 ⊗ᵤ g) * C[g⁻¹]`.

## iv. References

> * M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge
>   University Press (2010). [ref: nielsen\_chuang\_qci]

## A. The qubit index type and the `matrix_expand` tactic

**`Qubit`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L68).

> The index type of the computational basis of a qubit.

```lean
abbrev Qubit
```

## B. The single-qubit gates

**`Qubit.Z`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L112).

> The Pauli Z gate on a qubit.

```lean
def Z : 𝐔[Qubit]
```

**`Qubit.X`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L116).

> The Pauli X gate on a qubit.

```lean
def X : 𝐔[Qubit]
```

**`Qubit.Y`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L120).

> The Pauli Y gate on a qubit.

```lean
def Y : 𝐔[Qubit]
```

**`Qubit.H`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L124).

> The H gate, a Hadamard gate, on a qubit.

```lean
noncomputable def H : 𝐔[Qubit]
```

**`Qubit.S`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L128).

> The S gate, or Rz(π/2) rotation on a qubit.

```lean
def S : 𝐔[Qubit]
```

**`Qubit.T`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L132).

> The T gate, or Rz(π/4) rotation on a qubit.

```lean
noncomputable def T : 𝐔[Qubit]
```

## C. Identities between the single-qubit gates

**`Qubit.Z_sq`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L142).

```lean
lemma Z_sq : Z * Z = 1
```

**`Qubit.X_sq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L146).

```lean
lemma X_sq : X * X = 1
```

**`Qubit.Y_sq`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L150).

```lean
lemma Y_sq : Y * Y = 1
```

**`Qubit.H_sq`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L154).

```lean
lemma H_sq : H * H = 1
```

**`Qubit.S_sq`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L158).

```lean
lemma S_sq : S * S = Z
```

**`Qubit.T_sq`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L162).

```lean
lemma T_sq : T * T = S
```

**`Qubit.X_Y_anticomm`**, a theorem, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L168). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The anticommutator `{X,Y}` is zero. Marked simp as to put Pauli products in a canonical Y-X-Z
> order.

```lean
theorem X_Y_anticomm : X * Y = -Y * X
```

**`Qubit.Y_Z_anticomm`**, a theorem, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L172). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The anticommutator `{Y,Z}` is zero.

```lean
theorem Y_Z_anticomm : Z * Y = -Y * Z
```

**`Qubit.Z_X_anticomm`**, a theorem, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L176). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The anticommutator `{Z,X}` is zero.

```lean
theorem Z_X_anticomm : Z * X = -X * Z
```

**`Qubit.H_mul_X_eq_Z_mul_H`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L180).

```lean
lemma H_mul_X_eq_Z_mul_H : H * X = Z * H
```

**`Qubit.H_mul_Z_eq_X_mul_H`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L184).

```lean
lemma H_mul_Z_eq_X_mul_H : H * Z = X * H
```

**`Qubit.S_Z_comm`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L188).

```lean
lemma S_Z_comm : Z * S = S * Z
```

**`Qubit.T_Z_comm`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L192).

```lean
lemma T_Z_comm : Z * T = T * Z
```

**`Qubit.S_T_comm`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L196).

```lean
lemma S_T_comm : S * T = T * S
```

## D. Controlled gates

**`Qubit.controllize`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L207).

> The controlled version `C[g]` of a unitary matrix `g` indexed by `k`, acting on `Qubit × k`:
> the identity when the `Qubit` component, the control, is `0`, and `g` when it is `1`.

```lean
def controllize (g : 𝐔[k]) : 𝐔[Qubit × k]
```

**`Qubit.CNOT`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L227).

> Controlled-NOT gate on two qubits.
> The first qubit is the control and the second qubit is the target.

```lean
def CNOT : 𝐔[Fin 2 × Fin 2]
```

**`Qubit.CNOT_matrix`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L230).

> The matrix representation of CNOT is the standard 4×4 permutation matrix.

```lean
lemma CNOT_matrix :
    Matrix.reindex finProdFinEquiv finProdFinEquiv CNOT.val =
      ![![(1:ℂ), 0, 0, 0],
        ![0, 1, 0, 0],
        ![0, 0, 0, 1],
        ![0, 0, 1, 0]]
```

**`Qubit.controllize_apply_zero_zero`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L243).

```lean
lemma controllize_apply_zero_zero : C[g] (0, j₁) (0, j₂) = (1 : 𝐔[k]) j₁ j₂
```

**`Qubit.controllize_apply_zero_one`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L247).

```lean
lemma controllize_apply_zero_one : C[g] (0, j₁) (1, j₂) = 0
```

**`Qubit.controllize_apply_one_zero`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L251).

```lean
lemma controllize_apply_one_zero : C[g] (1, j₁) (0, j₂) = 0
```

**`Qubit.controllize_apply_one_one`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L255).

```lean
lemma controllize_apply_one_one : C[g] (1, j₁) (1, j₂) = g j₁ j₂
```

**`Qubit.controllize_mul`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L259).

```lean
lemma controllize_mul (g₁ g₂ : 𝐔[k]) : C[g₁] * C[g₂] = C[g₁ * g₂]
```

**`Qubit.controllize_one`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L263).

```lean
lemma controllize_one : C[(1 : 𝐔[k])] = 1
```

**`Qubit.controllize_mul_inv`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L266).

```lean
lemma controllize_mul_inv : C[g] * C[g⁻¹] = 1
```

**`Qubit.X_controllize_X`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean#L271).

```lean
lemma X_controllize_X : (X ⊗ᵤ 1) * C[g] * (X ⊗ᵤ 1) = (1 ⊗ᵤ g) * C[g⁻¹]
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Unitary](../../formathlib/hermitianmat/unitary.md)

## Sources

- [QuantumInfo/States/Pure/Qubit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Qubit.lean)
