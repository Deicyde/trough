---
declaration: module
origin: cited
lean: PauliMatrix.IsAnticommuting, PauliMatrix.IsAnticommuting.mul_self, PauliMatrix.IsAnticommuting.mul_comm_of_ne, PauliMatrix.IsAnticommuting.trace_mul, PauliMatrix.IsAnticommuting.trace_eq_zero, PauliMatrix.IsAnticommuting.linearIndependent, PauliMatrix.IsAnticommuting.card_le_three, PauliMatrix.isAnticommuting_pauliMatrix
statement: formalized
proof: formalized
---

# Three anticommuting matrices are the most `2 × 2` can hold

The module `PhyslibAlpha.Relativity.PauliMatrices.Anticommuting`, [PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean): 9 declarations, 7 with a docstring.

## i. Overview

> A family `τ` of `2 × 2` complex matrices is anticommuting when `τ_a τ_b + τ_b τ_a = 2 δ_ab 1`:
> each `τ_a` squares to `1` and two different ones anticommute. Conjugating `τ_a` by another
> member reverses its sign, so every member is traceless, and the trace pairs the members with
> each other and with `1` orthonormally. Together with `1` they are linearly independent in the
> four dimensional space of `2 × 2` matrices, so such a family has at most three members. The
> Pauli matrices `σ1, σ2, σ3` attain the bound: they are a maximal anticommuting family, one for
> each axis of space.

## ii. Key results

> - `IsAnticommuting` : the relation `τ_a τ_b + τ_b τ_a = 2 δ_ab 1`.
> - `IsAnticommuting.trace_mul`, `IsAnticommuting.trace_eq_zero` : the trace pairing.
> - `IsAnticommuting.linearIndependent` : the members together with `1` are independent.
> - `IsAnticommuting.card_le_three` : an anticommuting family has at most three members.
> - `isAnticommuting_pauliMatrix` : the Pauli matrices are anticommuting.
> - `isGreatest_card_isAnticommuting` : the largest anticommuting family has three members.

## iv. References

> * W. Pauli, *Zur Quantenmechanik des magnetischen Elektrons*, Z. Phys. 43 (1927) 601–623.

## A. Anticommuting families

**`PauliMatrix.IsAnticommuting`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L57).

> A family of `2 × 2` matrices with `τ_a τ_b + τ_b τ_a = 2 δ_ab 1`.

```lean
def IsAnticommuting {ι : Type*} [DecidableEq ι] (τ : ι → Matrix (Fin 2) (Fin 2) ℂ) : Prop
```

**`PauliMatrix.IsAnticommuting.mul_self`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L65).

```lean
lemma mul_self (a : ι) : τ a * τ a = 1
```

**`PauliMatrix.IsAnticommuting.mul_comm_of_ne`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L70).

```lean
lemma mul_comm_of_ne {a b : ι} (h : a ≠ b) : τ b * τ a = -(τ a * τ b)
```

**`PauliMatrix.IsAnticommuting.trace_mul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L76).

> The trace pairs the members orthogonally: `tr (τ_a τ_b) = 2 δ_ab`.

```lean
lemma trace_mul (a b : ι) : (τ a * τ b).trace = if a = b then 2 else 0
```

**`PauliMatrix.IsAnticommuting.trace_eq_zero`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L82).

> In a family with at least two members, every member is traceless.

```lean
lemma trace_eq_zero {a b : ι} (hab : b ≠ a) : (τ a).trace = 0
```

## B. At most three members

**`PauliMatrix.IsAnticommuting.linearIndependent`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L96).

> In a family with at least two members, the members together with `1` are linearly
> independent.

```lean
lemma linearIndependent [Fintype ι] [Nontrivial ι] :
    LinearIndependent ℂ (fun o : Option ι => o.elim (1 : Matrix (Fin 2) (Fin 2) ℂ) τ)
```

**`PauliMatrix.IsAnticommuting.card_le_three`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L113).

> **An anticommuting family of `2 × 2` matrices has at most three members.**

```lean
lemma card_le_three [Fintype ι] : Fintype.card ι ≤ 3
```

## C. The Pauli matrices attain the bound

**`PauliMatrix.isAnticommuting_pauliMatrix`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L129).

> The Pauli matrices `σ1, σ2, σ3` are an anticommuting family.

```lean
lemma isAnticommuting_pauliMatrix : IsAnticommuting fun i : Fin 3 => pauliMatrix (Sum.inr i)
```

**`PauliMatrix.isGreatest_card_isAnticommuting`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean#L136).

> **The Pauli matrices are a maximal anticommuting family.** The largest anticommuting family
> of `2 × 2` matrices has three members.

```lean
lemma isGreatest_card_isAnticommuting :
    IsGreatest {n : ℕ | ∃ τ : Fin n → Matrix (Fin 2) (Fin 2) ℂ, IsAnticommuting τ} 3
```

## Depends on

- [Physlib.Relativity.PauliMatrices.Basic](../../../physlib/relativity/paulimatrices/basic.md)

## Sources

- [PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/PauliMatrices/Anticommuting.lean)
