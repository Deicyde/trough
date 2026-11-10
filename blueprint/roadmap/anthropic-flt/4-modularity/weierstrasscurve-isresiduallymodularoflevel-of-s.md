---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isResiduallyModularOfLevel_of_switch
statement: formalized
proof: formalized
---

# WeierstrassCurve.isResiduallyModularOfLevel_of_switch

```lean
theorem WeierstrassCurve.isResiduallyModularOfLevel_of_switch {W W' : WeierstrassCurve ℤ} {N : ℕ}
    (hmod : W'.IsModularModelOfLevel N)
    (hND : ∀ ℓ : ℕ, ℓ.Prime → (ℓ : ℤ) ∣ W'.Δ → ℓ ∣ N)
    (hcong : ∀ ℓ : ℕ, ℓ.Prime → W.IsGoodPrimeFor ℓ → W'.IsGoodPrimeFor ℓ → ℓ ≠ 5 →
      (5 : ℤ) ∣ (W'.apOfModel ℓ - W.apOfModel ℓ)) :
    W.IsResiduallyModularOfLevel 5 N
```

*Quoted from [Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean, line 5](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean#L5) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “3-5 switch”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`WeierstrassCurve.isResiduallyModularOfLevel_of_switch`, stated in [Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean, line 5](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean#L5) and proved in [P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.isResiduallyModularOfLevel_of_switch` in Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean#L5)
- [Proof of `WeierstrassCurve.isResiduallyModularOfLevel_of_switch` in P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_of_switch.lean)
- [The repository's documentation page for `WeierstrassCurve.isResiduallyModularOfLevel_of_switch`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.isResiduallyModularOfLevel_of_switch)
