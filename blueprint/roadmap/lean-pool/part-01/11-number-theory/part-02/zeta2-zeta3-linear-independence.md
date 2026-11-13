---
declaration: theorem
origin: cited
lean: Zeta32.one_zeta_two_zeta_three_linearIndependent
statement: formalized
proof: formalized
---

# Linear independence of 1, zeta(2), and zeta(3)

> Proves that 1, the Riemann zeta function at 2, and its value at 3 are linearly independent over the rationals, using integer polynomial approximation, p-adic coefficient bounds, prime-edge nonvanishing, and logarithmic potential energy estimates for Hankel determinants. Includes reusable irrationality criteria, contour integration, Andreief identities, Newton-basis valuation bounds, and energy inequalities for finite measures. The cited source is the completed Lean proof; independent novelty of the informal argument is not claimed.

*Quoted from the card [LeanPool/projects/zeta2-zeta3-linear-independence.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta2-zeta3-linear-independence.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Zeta32.one_zeta_two_zeta_three_linearIndependent`](https://leanpool.github.io/lean-pool/LeanPool/Zeta32/Final.html#Zeta32.one_zeta_two_zeta_three_linearIndependent) (theorem; a main declaration), declared in [LeanPool/Zeta32/Final.lean, line 56](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta32/Final.lean#L56): “The three complex numbers 1, riemannZeta 2, and riemannZeta 3 are linearly independent over the rational numbers.” Its source, as the card gives it: “Upstream Zeta32/Final.lean and Solution.lean at the pinned commit. First public proof release: 2026-09-30 03:47:38 UTC, commit ec4fcb5617126b0a861f9e0c16f95425b32d4638. The upstream README and NOTICE disclose substantial AI assistance. The polynomial argument is credited upstream to Fauzan; this card cites the Lean artifact, not a separately verified paper.”
- [`Zeta32Acceptance.one_zeta_two_zeta_three_linearIndependent_series`](https://leanpool.github.io/lean-pool/LeanPool/Zeta32/Results.html#Zeta32Acceptance.one_zeta_two_zeta_three_linearIndependent_series) (theorem), declared in [LeanPool/Zeta32/Results.lean, line 19](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta32/Results.lean#L19): “For rational a, b, and c, if a plus b times the real sum of 1/(k+1)^2 plus c times the real sum of 1/(k+1)^3 is zero, then all three coefficients are zero; both sums range over natural numbers k.”
- [`Zeta32.zeta3_sub_rat_mul_zeta2_irrational`](https://leanpool.github.io/lean-pool/LeanPool/Zeta32/Final.html#Zeta32.zeta3_sub_rat_mul_zeta2_irrational) (theorem), declared in [LeanPool/Zeta32/Final.lean, line 51](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta32/Final.lean#L51): “For every rational r, the real series for zeta(3) minus r times the real series for zeta(2) is irrational.”

## Project

- Authors: Qian Tang.
- Source: *Linear independence of 1, zeta(2), and zeta(3), Lean formalization*.
- Project repository: [dtq1997/zeta2-zeta3-linear-independence](https://github.com/dtq1997/zeta2-zeta3-linear-independence), at commit [669c92bf](https://github.com/dtq1997/zeta2-zeta3-linear-independence/tree/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11J72, 11M06.
- In Lean Pool: [LeanPool/Zeta32](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta32), from the card [LeanPool/projects/zeta2-zeta3-linear-independence.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta2-zeta3-linear-independence.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/zeta2-zeta3-linear-independence.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta2-zeta3-linear-independence.yaml)
- [Lean Pool at 701389c0: LeanPool/Zeta32](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta32)
