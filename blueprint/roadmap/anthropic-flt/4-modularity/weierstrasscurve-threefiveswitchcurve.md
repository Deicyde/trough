---
declaration: theorem
origin: cited
lean: WeierstrassCurve.threeFiveSwitchCurve
statement: formalized
proof: formalized
---

# WeierstrassCurve.threeFiveSwitchCurve

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem WeierstrassCurve.threeFiveSwitchCurve (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (hW : W.IsSemistableModel) (h5 : W.ModRepIsIrreducible 5) : ∃ W' : WeierstrassCurve ℤ, W'.Δ ≠ 0 ∧ W'.IsSemistableModel ∧ W'.ModRepIsIrreducible 3 ∧ ∀ ℓ : ℕ, ℓ.Prime → W.IsGoodPrimeFor ℓ → W'.IsGoodPrimeFor ℓ → ℓ ≠ 5 → (5 : ℤ) ∣ (W'.apOfModel ℓ - W.apOfModel ℓ)
```

*Quoted from [Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean, line 16](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean#L16) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “3-5 switch”, “three-five switch”, “Wiles”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.threeFiveAuxiliaryCurveExists](weierstrasscurve-threefiveauxiliarycurveexists.md)

## Lean

`WeierstrassCurve.threeFiveSwitchCurve`, stated in [Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean, line 16](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean#L16) and proved in [P2M/Sol/S_WeierstrassCurve_threeFiveSwitchCurve.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_threeFiveSwitchCurve.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.threeFiveSwitchCurve` in Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveSwitchCurve.lean#L16)
- [Proof of `WeierstrassCurve.threeFiveSwitchCurve` in P2M/Sol/S_WeierstrassCurve_threeFiveSwitchCurve.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_threeFiveSwitchCurve.lean)
- [The repository's documentation page for `WeierstrassCurve.threeFiveSwitchCurve`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.threeFiveSwitchCurve)
