---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd
statement: formalized
proof: formalized
---

# WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd

```lean
set_option autoImplicit false

theorem
WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd
    (W : WeierstrassCurve ℤ) (hss : W.IsSemistableModel) (N : ℕ)
    (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (hirr : W.ModRepIsIrreducible p)
    (hp2N : ¬ p ^ 2 ∣ N)
    (hN : W.IsModularModelOfLevel N) (hbad : ∀ ℓ : ℕ, ℓ.Prime → (ℓ : ℤ) ∣ W.Δ → ℓ ∣ N)
    (hN3 : ∀ q : ℕ, q.Prime → ¬ q ^ 3 ∣ N) :
    W.IsModularModelOfLevel W.conductorLevel
```

*Quoted from [Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean, line 86](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean#L86) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [CuspForm.newformBadPrimeCoeff](../5-level-lowering/cuspform-newformbadprimecoeff.md)
- [ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd](residualgaloisrep-isabsolutelyirreducible-of-isi.md)

## Lean

`WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd`, stated in [Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean, line 86](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean#L86) and proved in [P2M/Sol/S_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd` in Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean#L86)
- [Proof of `WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd` in P2M/Sol/S_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd.lean)
- [The repository's documentation page for `WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd)
