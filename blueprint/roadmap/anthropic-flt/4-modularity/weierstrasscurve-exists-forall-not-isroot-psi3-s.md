---
declaration: theorem
origin: cited
lean: WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization
statement: formalized
proof: formalized
---

# WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization

```lean
open Polynomial
theorem WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization (a b : Polynomial ℚ) (ha : a.natDegree ≤ 20) (hb : b.natDegree ≤ 30) (hinf : 4 * a.coeff 20 ^ 3 + 27 * b.coeff 30 ^ 2 ≠ 0) (hroot : ∀ g : Polynomial ℚ, (⟨0, 0, 0, a, b⟩ : WeierstrassCurve (Polynomial ℚ)).Ψ₃.eval g ≠ 0) (M : ℕ) (hM : M ≠ 0) (m₀ : ℕ) : ∃ m : ℕ, m₀ ≤ m ∧ ∀ x : ℚ, ¬ (⟨0, 0, 0, a.eval ((M : ℚ) * m), b.eval ((M : ℚ) * m)⟩ : WeierstrassCurve ℚ).Ψ₃.IsRoot x
```

*Quoted from [Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean#L6) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization`, stated in [Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean#L6) and proved in [P2M/Sol/S_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization` in Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean#L6)
- [Proof of `WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization` in P2M/Sol/S_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_exists_forall_not_isRoot_Psi3_specialization.lean)
- [The repository's documentation page for `WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization)
