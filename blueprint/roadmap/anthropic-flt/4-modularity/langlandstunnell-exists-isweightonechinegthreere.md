---
declaration: theorem
origin: cited
lean: LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift
statement: formalized
proof: formalized
---

# LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift

```lean
set_option autoImplicit false

open AutomorphicForm FLT.ExplicitLift EisensteinWeightOne open WeierstrassCurve hiding cusp
open scoped MatrixGroups

local notation "Γℚ" => (AlgebraicClosure ℚ ≃ₐ[ℚ] AlgebraicClosure ℚ)

theorem LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift
    (ρ : Γℚ →* GL (Fin 2) (ZMod 3)) (hρ : Continuous ρ) (hsurj : Function.Surjective ρ)
    (hdet : ∀ σ : Γℚ, Matrix.GeneralLinearGroup.det (ρ σ) = modThreeCyclotomicChar σ)
    (Ψ : GL (Fin 2) (ZMod 3) →* GL (Fin 2) (ℤ√(-2)))
    (hΨ : ∀ g, Matrix.GeneralLinearGroup.map red (Ψ g) = g) :
    ∃ (N : ℕ) (_ : NeZero N) (b : ℕ → ℤ√(-2)),
      FormalHecke.IsEigensystem
        (fun ℓ => if ℓ ∣ N then 0 else ((chiNegThree ℓ : ℤ) : ℤ√(-2))) b ∧
      CuspForm.IsWeightOneChiNegThreeRealized N b ∧
      ∀ p : ℕ, p.Prime → ¬ p ∣ 3 * N →
        ∀ A : ValuationSubring (AlgebraicClosure ℚ), A.LiesOverPrime p →
          ∀ σ : Γℚ, A.IsFrobeniusAt σ p →
            b p = ((Ψ (ρ σ) : GL (Fin 2) (ℤ√(-2))) : Matrix (Fin 2) (Fin 2) (ℤ√(-2))).trace
```

*Quoted from [Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean, line 56](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean#L56) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Langlands-Tunnell”, “Tunnell”, “octahedral”, “weight one form”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion](automorphicform-exists-weightone-cuspform-of-isc.md)

## Lean

`LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift`, stated in [Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean, line 56](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean#L56) and proved in [P2M/Sol/S_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift` in Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean#L56)
- [Proof of `LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift` in P2M/Sol/S_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_LanglandsTunnell_exists_isWeightOneChiNegThreeRealized_eq_trace_lift.lean)
- [The repository's documentation page for `LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift)
