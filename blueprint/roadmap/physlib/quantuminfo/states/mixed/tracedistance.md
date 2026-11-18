---
declaration: module
origin: cited
lean: TrDistance.symm, TrDistance.eq_abs_eigenvalues, TrDistance, TrDistance.ge_zero, TrDistance.le_one, TrDistance.prob
statement: formalized
proof: formalized
---

# QuantumInfo.States.Mixed.TraceDistance

The module `QuantumInfo.States.Mixed.TraceDistance`, [QuantumInfo/States/Mixed/TraceDistance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean): 6 declarations, 4 with a docstring, 2 listed as significant.

**`TrDistance`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L24).

> The trace distance between two quantum states: half the trace norm of the difference (ρ - σ).

```lean
def TrDistance (ρ σ : MState d) : ℝ
```

**`TrDistance.ge_zero`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L31).

```lean
lemma ge_zero : 0 ≤ TrDistance ρ σ
```

**`TrDistance.le_one`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L35).

```lean
lemma le_one : TrDistance ρ σ ≤ 1
```

**`TrDistance.prob`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L42).

> The trace distance, as a `Prob` probability with value between 0 and 1.

```lean
def prob : Prob
```

**`TrDistance.symm`**, a theorem, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L46). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace distance is a symmetric quantity.

```lean
theorem symm : TrDistance ρ σ = TrDistance σ ρ
```

**`TrDistance.eq_abs_eigenvalues`**, a theorem, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean#L51). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace distance is equal to half the 1-norm of the eigenvalues of their difference .

```lean
theorem eq_abs_eigenvalues : TrDistance ρ σ = (1/2:ℝ) *
    ∑ i, abs ((ρ.Hermitian.sub σ.Hermitian).eigenvalues i)
```

## Depends on

- [QuantumInfo.States.Mixed.MState](mstate.md)

## Sources

- [QuantumInfo/States/Mixed/TraceDistance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/TraceDistance.lean)
