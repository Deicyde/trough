---
declaration: theorem
origin: cited
lean: AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion
statement: formalized
proof: formalized
---

# AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion

```lean
open CongruenceSubgroup EisensteinWeightOne
open scoped MatrixGroups ModularForm
theorem AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion
    (Φ : HeckeEigensystem ℚ (ℤ√(-2))) (hΦ : AutomorphicForm.viaCompactCuspNotion.IsCusp ℚ Φ)
    (T : Finset ℕ) :
    ∃ (M : ℕ) (_ : NeZero M), 3 ∣ M ∧ (∀ ℓ ∈ T, ℓ ≠ 0 → ℓ ∣ M) ∧
      ∃ (g : CuspForm (Gamma1 M) 1) (b : ℕ → ℤ√(-2)),
        (∀ γ : SL(2, ℤ), γ ∈ Gamma0 M →
          (⇑g) ∣[(1 : ℤ)] γ = ((chiNegThree (((γ 1 1 : ℤ) : ZMod 3).val) : ℤ) : ℂ) • (⇑g)) ∧
        (∀ n, ModularFormClass.qCoeff (⇑g) n =
          ((b n).re : ℂ) + ((b n).im : ℂ) * ((Real.sqrt 2 : ℂ) * Complex.I)) ∧
        b 0 = 0 ∧
        FormalHecke.IsEigensystem
          (fun ℓ => if ℓ ∣ M then (0 : ℤ√(-2)) else ((chiNegThree ℓ : ℤ) : ℤ√(-2))) b ∧
        ∀ (p : ℕ) (hp : p.Prime), ¬ p ∣ 3 * M → b p = Φ.a (AutomorphicForm.ratPrime ⟨p, hp⟩)
```

*Quoted from [Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean, line 9](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean#L9) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion`, stated in [Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean, line 9](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean#L9) and proved in [P2M/Sol/S_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion` in Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean#L9)
- [Proof of `AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion` in P2M/Sol/S_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_AutomorphicForm_exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion.lean)
- [The repository's documentation page for `AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion)
