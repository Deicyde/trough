---
declaration: theorem
origin: cited
lean: MetricCodes.Johnson.main_binary_theorem
statement: formalized
proof: formalized
---

# Improved asymptotic bounds for binary and spherical codes

> Formalizes asymptotic coding bounds obtained from multilevel harmonic analysis, branching rules, and spectral decompositions. The development proves a binary-code exponent strictly below the MRRW rate, constructs a strict hierarchy of spherical-code bounds, and derives the published 0.39661 asymptotic kissing-number exponent. This import incorporates substantial proof and performance optimizations by Dean Cureton.

*Quoted from the card [LeanPool/projects/metric-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/metric-codes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MetricCodes.Johnson.main_binary_theorem`](https://leanpool.github.io/lean-pool/LeanPool/MetricCodes/Conclusion.html#MetricCodes.Johnson.main_binary_theorem) (theorem; a main declaration), declared in [LeanPool/MetricCodes/Conclusion.lean, line 7342](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes/Conclusion.lean#L7342): “For every relative distance strictly between zero and one half, the combined variational upper bound on the asymptotic binary-code rate is valid and is strictly smaller than the MRRW rate.”
- [`MetricCodes.Spherical.HigherHierarchy.main_general`](https://leanpool.github.io/lean-pool/LeanPool/MetricCodes/Conclusion.html#MetricCodes.Spherical.HigherHierarchy.main_general) (theorem), declared in [LeanPool/MetricCodes/Conclusion.lean, line 7299](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes/Conclusion.lean#L7299): “Every feasible finite interlacing certificate gives an eventual exponential upper bound for spherical codes, while the spherical-code rate is bounded by the closed hierarchy's variational rate.”
- [`MetricCodes.Spherical.HigherHierarchy.strict_hierarchy`](https://leanpool.github.io/lean-pool/LeanPool/MetricCodes/Conclusion.html#MetricCodes.Spherical.HigherHierarchy.strict_hierarchy) (theorem), declared in [LeanPool/MetricCodes/Conclusion.lean, line 7308](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes/Conclusion.lean#L7308): “At every angle parameter strictly between zero and one, successive levels of both the global and localized hierarchies improve strictly, with the localized hierarchy also strictly improving the row and classical bounds.”
- [`MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published`](https://leanpool.github.io/lean-pool/LeanPool/MetricCodes/Conclusion.html#MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published) (theorem), declared in [LeanPool/MetricCodes/Conclusion.lean, line 7353](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes/Conclusion.lean#L7353): “In all sufficiently large dimensions, the kissing number is at most 2 raised to 0.39661 times the dimension.”

## Project

- Authors: OpenAI, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 94B65, 52C17, 41A60.
- In Lean Pool: [LeanPool/MetricCodes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes), from the card [LeanPool/projects/metric-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/metric-codes.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/metric-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/metric-codes.yaml)
- [Lean Pool at 701389c0: LeanPool/MetricCodes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MetricCodes)
