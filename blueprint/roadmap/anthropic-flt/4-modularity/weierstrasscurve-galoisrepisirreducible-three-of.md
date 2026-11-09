---
declaration: theorem
origin: cited
lean: WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero
statement: formalized
proof: formalized
---

# WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero

```lean
open WeierstrassCurve
theorem WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero (V : WeierstrassCurve ℚ) (hΔ : V.Δ ≠ 0) (h : ∀ x : ℚ, V.Ψ₃.eval x ≠ 0) : Affine.Point.GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ V 3
```

*Quoted from [Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean, line 9](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean#L9) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero`, stated in [Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean, line 9](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean#L9) and proved in [P2M/Sol/S_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero` in Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean#L9)
- [Proof of `WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero` in P2M/Sol/S_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero.lean)
- [The repository's documentation page for `WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero)
