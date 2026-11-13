---
declaration: theorem
origin: cited
lean: LeanPool.HansonWright.hanson_wright_inequality_hdp
statement: formalized
proof: formalized
---

# The Hanson-Wright inequality for sub-Gaussian quadratic forms

> Proves the finite-dimensional Hanson-Wright concentration inequality for quadratic forms of independent mean-zero sub-Gaussian real random variables whose maximum least global-MGF sub-Gaussian scale is positive, for matrices with positive Frobenius and operator norms. The bound uses the fixed universal coefficient 1 / (256 \* exp(1)^2). This is the MGF normalization of the usual result; no formal identification with an Orlicz psi-2 norm is claimed. The development derives the required moment-generating-function certificate instead of assuming it, and contributes reusable scalar Bernstein, Chernoff, cumulant, sub-Gaussian-process, and finite-maximum infrastructure.

*Quoted from the card [LeanPool/projects/hanson-wright.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hanson-wright.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.HansonWright.hanson_wright_inequality_hdp`](https://leanpool.github.io/lean-pool/LeanPool/HansonWright/Probability/Concentration/HansonWright.html#LeanPool.HansonWright.hanson_wright_inequality_hdp) (theorem; a main declaration), declared in [LeanPool/HansonWright/Probability/Concentration/HansonWright.lean, line 3923](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HansonWright/Probability/Concentration/HansonWright.lean#L3923): “For independent mean-zero real random variables with finite least global-MGF sub-Gaussian scales and positive maximum coordinate MGF scale, and a matrix with positive Frobenius and operator norms, the centered quadratic form satisfies the Hanson-Wright two-regime exponential tail bound with the fixed universal coefficient 1 / (256 \* exp(1)^2).”
- [`LeanPool.HansonWright.hasHansonWrightMGF_of_subgaussian`](https://leanpool.github.io/lean-pool/LeanPool/HansonWright/Probability/Concentration/HansonWright.html#LeanPool.HansonWright.hasHansonWrightMGF_of_subgaussian) (theorem), declared in [LeanPool/HansonWright/Probability/Concentration/HansonWright.lean, line 3669](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HansonWright/Probability/Concentration/HansonWright.lean#L3669): “Given positive K and operator norm and C at least 64 \* exp(1)^2, independent coordinates with global-MGF sub-Gaussian parameter K^2 satisfy the local quadratic cumulant-generating-function estimate needed for Hanson-Wright.”
- [`LeanPool.bernstein_inequality`](https://leanpool.github.io/lean-pool/LeanPool/HansonWright/Probability/Concentration/Bernstein.html#LeanPool.bernstein_inequality) (theorem), declared in [LeanPool/HansonWright/Probability/Concentration/Bernstein.lean, line 581](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HansonWright/Probability/Concentration/Bernstein.lean#L581): “A finite family of independent, centered, uniformly bounded real random variables satisfies the classical scalar Bernstein tail inequality.”

## Project

- Authors: Yuanhe Zhang, Jason D. Lee, Fanghui Liu.
- Source: *High-Dimensional Probability (second edition)* by Roman Vershynin, [doi:10.1017/9781009490672](https://doi.org/10.1017/9781009490672), [https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html).
- Project repository: [Lean-MoDS/StatsMLlib](https://github.com/Lean-MoDS/StatsMLlib), at commit [37286c3d](https://github.com/Lean-MoDS/StatsMLlib/tree/37286c3d2c7e17642fbe26988be40f3ff982f944).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 60E15, 60B20, 62H12.
- In Lean Pool: [LeanPool/HansonWright](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HansonWright), from the card [LeanPool/projects/hanson-wright.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hanson-wright.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/hanson-wright.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hanson-wright.yaml)
- [Lean Pool at 701389c0: LeanPool/HansonWright](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HansonWright)
