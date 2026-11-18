---
declaration: module
origin: cited
lean: PhyslibAlpha.Qubit.ry, PhyslibAlpha.Qubit.ry_apply, PhyslibAlpha.Qubit.blockDiagonal_mem_unitaryGroup, PhyslibAlpha.Qubit.multiplex, PhyslibAlpha.Qubit.multiplex_apply
statement: formalized
proof: formalized
---

# Real rotations of a qubit and multiplexed gates

The module `PhyslibAlpha.QuantumMechanics.QubitGates`, [PhyslibAlpha/QuantumMechanics/QubitGates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean): 5 declarations, 3 with a docstring.

> The rotation `Ry` of a qubit given by its cosine and sine, and gates controlled by the value of a
> register.

## i. Overview

> For real `c`, `s` with `c² + s² = 1` the matrix `!![c, -s; s, c]` is a unitary gate on a qubit,
> `ry c s h`. With `c = cos (θ/2)` and `s = sin (θ/2)` it is the rotation by `θ` about the `y`-axis;
> giving it by `c` and `s` avoids trigonometric functions when the entries are square roots.
>
> For a family of unitary gates `g r` on `k`, indexed by the values `r` of a register `ι`, the
> multiplexed gate `multiplex g` on `ι × k` applies `g r` when the register is in the state `|r⟩`:
> `Σ_r |r⟩⟨r| ⊗ g r`. Up to the order of the factors it is the block-diagonal matrix
> `Matrix.blockDiagonal` of the `g r`, which is unitary since each block is.

## ii. Key results

> - `ry`: the rotation `!![c, -s; s, c]` as a unitary gate for `c² + s² = 1`.
> - `blockDiagonal_mem_unitaryGroup`: a block-diagonal matrix of unitary blocks is unitary.
> - `multiplex`, `multiplex_apply`: the gate `Σ_r |r⟩⟨r| ⊗ g r` and its entries.

## iv. References

> - The gates and the notation `𝐔[·]` are those of `QuantumInfo.States.Pure.Qubit`.

## A. The rotation `Ry`

**`PhyslibAlpha.Qubit.ry`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean#L56).

> The rotation `!![c, -s; s, c]` of a qubit, for real `c`, `s` with `c² + s² = 1`.

```lean
def ry (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : 𝐔[Qubit]
```

**`PhyslibAlpha.Qubit.ry_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean#L65).

```lean
lemma ry_apply (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    (ry c s h : Matrix Qubit Qubit ℂ) = !![(c : ℂ), -s; s, c]
```

## B. Multiplexed gates

**`PhyslibAlpha.Qubit.blockDiagonal_mem_unitaryGroup`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean#L77).

> A block-diagonal matrix whose blocks are unitary is unitary.

```lean
lemma blockDiagonal_mem_unitaryGroup (g : ι → 𝐔[k]) :
    blockDiagonal (fun r => (g r : Matrix k k ℂ)) ∈ unitaryGroup (k × ι) ℂ
```

**`PhyslibAlpha.Qubit.multiplex`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean#L86).

> The multiplexed gate `Σ_r |r⟩⟨r| ⊗ g r` on `ι × k`: the gate `g r` on `k`, controlled by the
> value `r` of the register `ι`.

```lean
def multiplex (g : ι → 𝐔[k]) : 𝐔[ι × k]
```

**`PhyslibAlpha.Qubit.multiplex_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean#L94).

```lean
lemma multiplex_apply (g : ι → 𝐔[k]) (r r' : ι) (q q' : k) :
    (multiplex g : Matrix (ι × k) (ι × k) ℂ) (r, q) (r', q') =
      if r = r' then (g r : Matrix k k ℂ) q q' else 0
```

## Depends on

- [Qubits](../../quantuminfo/states/pure/qubit.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/QubitGates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/QubitGates.lean)
