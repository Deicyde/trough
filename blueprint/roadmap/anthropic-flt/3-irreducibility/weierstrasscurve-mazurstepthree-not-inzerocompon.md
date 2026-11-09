---
declaration: theorem
origin: cited
lean: WeierstrassCurve.mazurStepThree_not_inZeroComponentAt
statement: formalized
proof: formalized
---

# WeierstrassCurve.mazurStepThree_not_inZeroComponentAt

```lean
open WeierstrassCurve WeierstrassCurve.Affine
theorem WeierstrassCurve.mazurStepThree_not_inZeroComponentAt
    {p : ℕ} (hp : p.Prime) (hp' : p ∉ ({2, 3, 5, 7, 13} : Finset ℕ))
    (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0)
    (Q : ((W.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point)
    (hQfix : ∀ σ : AlgebraicClosure ℚ ≃ₐ[ℚ] AlgebraicClosure ℚ, σ • Q = Q)
    (hQord : addOrderOf Q = p)
    (h2Δ : (2 : ℤ) ∣ W.Δ) (h2c₄ : ¬ (2 : ℤ) ∣ W.c₄)
    (h2 : ∀ A : ValuationSubring (AlgebraicClosure ℚ), A.LiesOverPrime 2 → ¬ W.InZeroComponentAt A Q)
    (h3Δ : (3 : ℤ) ∣ W.Δ) (h3c₄ : ¬ (3 : ℤ) ∣ W.c₄)
    (h3 : ∀ A : ValuationSubring (AlgebraicClosure ℚ), A.LiesOverPrime 3 → ¬ W.InZeroComponentAt A Q)
    {ℓ : ℕ} (hℓ : ℓ.Prime) (hℓp : ℓ ≠ p) (hℓΔ : (ℓ : ℤ) ∣ W.Δ) (hℓc₄ : ¬ (ℓ : ℤ) ∣ W.c₄)
    (A : ValuationSubring (AlgebraicClosure ℚ)) (hA : A.LiesOverPrime ℓ) :
    ¬ W.InZeroComponentAt A Q
```

*Quoted from [Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean, line 65](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean#L65) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Mazur Step 3”.

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar](modularcurve-eisensteinquotientinvariantsfinitea.md)
- [ModularCurve.mazurQuotientSpecialization_heckeModuleBar](modularcurve-mazurquotientspecialization-heckemo.md)

## Lean

`WeierstrassCurve.mazurStepThree_not_inZeroComponentAt`, stated in [Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean, line 65](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean#L65) and proved in [P2M/Sol/S_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.mazurStepThree_not_inZeroComponentAt` in Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean#L65)
- [Proof of `WeierstrassCurve.mazurStepThree_not_inZeroComponentAt` in P2M/Sol/S_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_mazurStepThree_not_inZeroComponentAt.lean)
- [The repository's documentation page for `WeierstrassCurve.mazurStepThree_not_inZeroComponentAt`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.mazurStepThree_not_inZeroComponentAt)
