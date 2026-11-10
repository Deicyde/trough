---
declaration: theorem
origin: cited
lean: ModularForm.S2_Gamma0_2_eq_zero
statement: formalized
proof: formalized
---

# S₂(Γ₀(2)) = 0

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem ModularForm.S2_Gamma0_2_eq_zero (f : CuspForm (CongruenceSubgroup.Gamma0 2) 2) : f = 0
```

*Quoted from [Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean, line 13](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean#L13) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “S2(Gamma0(2)) = 0”, “no weight 2 level 2 cusp forms”.

PROOF-PATH.md names it in [6. S₂(Γ₀(2)) = 0](README.md), as the theorem that carries step 6.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`ModularForm.S2_Gamma0_2_eq_zero`, stated in [Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean, line 13](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean#L13) and proved in [P2M/Sol/S_ModularForm_S2_Gamma0_2_eq_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ModularForm_S2_Gamma0_2_eq_zero.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `ModularForm.S2_Gamma0_2_eq_zero` in Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularForm_S2_Gamma0_2_eq_zero.lean#L13)
- [Proof of `ModularForm.S2_Gamma0_2_eq_zero` in P2M/Sol/S_ModularForm_S2_Gamma0_2_eq_zero.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ModularForm_S2_Gamma0_2_eq_zero.lean)
- [The repository's documentation page for `ModularForm.S2_Gamma0_2_eq_zero`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#ModularForm.S2_Gamma0_2_eq_zero)
