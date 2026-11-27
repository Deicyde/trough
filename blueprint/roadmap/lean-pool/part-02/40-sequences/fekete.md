---
declaration: theorem
origin: cited
lean: NearlySubadditive.tendsto_atBot_or_exists_tendsto, NearlySubadditive.tendsto_lim, NearlySubadditive.tendsto_atBot_or_exists_tendsto_of_summable, summable_div_sq_iff_forall_not_tendsto_atTop, Supermultiplicative.exists_nonneg_not_tendsto_rpow_inv
statement: formalized
proof: formalized
---

# Nearly subadditive sequences and Fekete's lemma beyond Mathlib

> Extends Mathlib's Fekete lemma for real sequences on ℕ. Proves the Füredi–Ruzsa window theorem (subadditivity only on N ≤ m ≤ n ≤ μm with μ > 1 gives u n / n → -∞ or a real limit, identified as an infimum), the de Bruijn–Erdős theorem with a monotone error f satisfying ∑ f n / n² < ∞ (extended from f ≥ 0 to errors of any sign), and its sharpness (for monotone f ≥ 0 the summability is equivalent to the absence of a nearly f-subadditive sequence with u n / n → ∞). Also packages corollaries of Mathlib's Subadditive API (the unbounded case of Fekete's lemma, Fekete for superadditive and positive supermultiplicative sequences, bounded-defect and almost-additive versions) and a counterexample showing that positivity cannot be weakened to nonnegativity for supermultiplicative sequences.

*Quoted from the card [LeanPool/projects/fekete.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fekete.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NearlySubadditive.tendsto_atBot_or_exists_tendsto`](https://leanpool.github.io/lean-pool/LeanPool/Fekete/Window.html#NearlySubadditive.tendsto_atBot_or_exists_tendsto) (theorem; a main declaration), declared in [LeanPool/Fekete/Window.lean, line 281](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete/Window.lean#L281): “If 1 < μ and u (m + n) ≤ u m + u n whenever N ≤ m ≤ n ≤ μ m, then u n / n tends to -∞ or to a real limit.” Its source, as the card gives it: “Füredi–Ruzsa, Nearly subadditive sequences, Theorem 2 (same number in the journal version and arXiv:1810.11723); the source takes N ≥ 1, while the Lean statement also allows N = 0.”
- [`NearlySubadditive.tendsto_lim`](https://leanpool.github.io/lean-pool/LeanPool/Fekete/Window.html#NearlySubadditive.tendsto_lim) (theorem; a main declaration), declared in [LeanPool/Fekete/Window.lean, line 373](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete/Window.lean#L373): “Under the same window hypothesis, if u n / n is bounded below then it converges to the infimum of u k / k over k ≥ max N 1.” Its source, as the card gives it: “Limit identification as in Füredi–Ruzsa Theorem 1 (de Bruijn–Erdős, ratio 2), here for every ratio μ > 1; upstream Fekete/Window.lean.”
- [`NearlySubadditive.tendsto_atBot_or_exists_tendsto_of_summable`](https://leanpool.github.io/lean-pool/LeanPool/Fekete/DeBruijnErdos.html#NearlySubadditive.tendsto_atBot_or_exists_tendsto_of_summable) (theorem; a main declaration), declared in [LeanPool/Fekete/DeBruijnErdos.lean, line 118](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete/DeBruijnErdos.lean#L118): “If 1 < μ, u (m + n) ≤ u m + u n + f (m + n) for N ≤ m ≤ n ≤ μ m, f is monotone and ∑ f n / n² is summable, then u n / n tends to -∞ or to a real limit. No sign condition on f is assumed.” Its source, as the card gives it: “Füredi–Ruzsa, Theorem 3 of the journal version (Theorem 5 of arXiv:1810.11723), generalizing de Bruijn–Erdős (1952). The sources assume f ≥ 0; the signed version is an extension, reduced to the nonnegative case through max f 0.”
- [`summable_div_sq_iff_forall_not_tendsto_atTop`](https://leanpool.github.io/lean-pool/LeanPool/Fekete/Sharpness.html#summable_div_sq_iff_forall_not_tendsto_atTop) (theorem; a main declaration), declared in [LeanPool/Fekete/Sharpness.lean, line 128](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete/Sharpness.lean#L128): “For a nonnegative monotone f, ∑ f n / n² is summable if and only if no sequence with u (m + n) ≤ u m + u n + f (m + n) for all m, n has u n / n → ∞.” Its source, as the card gives it: “Combines a variant of Füredi–Ruzsa Claim 7 (the witness keeps the f 1 term and index 0) with journal Theorem 3 (arXiv Theorem 5).”
- [`Supermultiplicative.exists_nonneg_not_tendsto_rpow_inv`](https://leanpool.github.io/lean-pool/LeanPool/Fekete/SupermultiplicativeCounterexample.html#Supermultiplicative.exists_nonneg_not_tendsto_rpow_inv) (theorem; a main declaration), declared in [LeanPool/Fekete/SupermultiplicativeCounterexample.lean, line 69](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete/SupermultiplicativeCounterexample.lean#L69): “Some nonnegative supermultiplicative sequence u has no limit of u n ^ (1 / n), so positivity is needed in the supermultiplicative Fekete lemma.” Its source, as the card gives it: “Upstream Fekete/SupermultiplicativeCounterexample.lean.”

## Project

- Authors: Brian Sanders.
- Source: *Nearly subadditive sequences* by Zoltán Füredi, Imre Z. Ruzsa, [doi:10.1007/s10474-020-01071-0](https://doi.org/10.1007/s10474-020-01071-0), [arXiv:1810.11723](https://arxiv.org/abs/1810.11723).
- Project repository: [Egly443/lean-fekete](https://github.com/Egly443/lean-fekete), at commit [5faa67a2](https://github.com/Egly443/lean-fekete/tree/5faa67a2cbcf0d670bf2b8353336bab5818d6026).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 40A05, 39B62.
- In Lean Pool: [LeanPool/Fekete](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete), from the card [LeanPool/projects/fekete.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fekete.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/fekete.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fekete.yaml)
- [Lean Pool at bb99e52c: LeanPool/Fekete](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Fekete)
