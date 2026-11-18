---
declaration: module
origin: cited
lean: MState.fidelity_self_eq_one, MState.fidelity_eq_traceNorm_sqrt_mul_sqrt, MState.fidelity_eq_one_iff_self, MState.fidelity_symm, MState.fidelity, MState.fidelity_ge_zero, MState.fidelity_le_one, MState.fidelity_prob
statement: formalized
proof: formalized
---

# QuantumInfo.States.Mixed.Fidelity

The module `QuantumInfo.States.Mixed.Fidelity`, [QuantumInfo/States/Mixed/Fidelity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean): 8 declarations, 6 with a docstring, 4 listed as significant.

**`MState.fidelity`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L25).

> The fidelity of two quantum states. This is the quantum version of the Bhattacharyya
> coefficient.

```lean
def fidelity (ρ σ : MState d) : ℝ
```

**`MState.fidelity_ge_zero`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L28).

```lean
lemma fidelity_ge_zero : 0 ≤ fidelity ρ σ
```

**`MState.fidelity_le_one`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L32).

```lean
lemma fidelity_le_one : fidelity ρ σ ≤ 1
```

**`MState.fidelity_prob`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L51).

> The fidelity, as a `Prob` probability with value between 0 and 1.

```lean
def fidelity_prob : Prob
```

**`MState.fidelity_self_eq_one`**, a theorem, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L55). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A state has perfect fidelity with itself.

```lean
theorem fidelity_self_eq_one : fidelity ρ ρ = 1
```

**`MState.fidelity_eq_traceNorm_sqrt_mul_sqrt`**, a theorem, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L70). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Fidelity can be rewritten as the trace norm of the product of square roots.

```lean
theorem fidelity_eq_traceNorm_sqrt_mul_sqrt (ρ σ : MState d) :
    fidelity ρ σ = (σ.M.sqrt.mat * ρ.M.sqrt.mat).traceNorm
```

**`MState.fidelity_eq_one_iff_self`**, a theorem, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L82). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The fidelity is 1 if and only if the two states are the same.

```lean
theorem fidelity_eq_one_iff_self : fidelity ρ σ = 1 ↔ ρ = σ
```

**`MState.fidelity_symm`**, a theorem, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean#L116). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The fidelity is a symmetric quantity.

```lean
theorem fidelity_symm : fidelity ρ σ = fidelity σ ρ
```

## Depends on

- [Physlib.Meta.Informal.Basic](../../../physlib/meta/informal/basic.md)
- [QuantumInfo.States.Mixed.MState](mstate.md)

## Proof depends on

- [Schatten norms](../../formathlib/hermitianmat/schatten.md)

## Sources

- [QuantumInfo/States/Mixed/Fidelity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/Fidelity.lean)
