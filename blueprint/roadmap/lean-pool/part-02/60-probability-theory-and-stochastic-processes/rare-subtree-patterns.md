---
declaration: theorem
origin: cited
lean: PoissonDeclumping.poissonApproximation, PoissonDeclumping.poissonApproximation2, PoissonDeclumping.maxString, PoissonDeclumping.maxLeafHeight
statement: formalized
proof: formalized
---

# Rare subtree patterns in conditioned Bienaymé trees

> Proves marked Poisson approximation, root declumping, maximal complete non-fringe r-ary height and maximum leaf-height for critical Bienaymé trees conditioned on their size, under the stated stable-domain, marking, cutoff and non-clustering hypotheses. Periodic offspring laws are included through admissible-size limits. Single-point phase refinements are formulated along phase-separated admissible subsequences. The dependency closure preserves tree coding, Chen–Stein bounds, regular variation, stable densities and lattice local limit estimates, with concrete offspring examples and direct consequences.

*Quoted from the card [LeanPool/projects/rare-subtree-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rare-subtree-patterns.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PoissonDeclumping.poissonApproximation`](https://leanpool.github.io/lean-pool/LeanPool/RareSubtreePatterns/MainTheorems.html#PoissonDeclumping.poissonApproximation) (theorem; a main declaration), declared in [LeanPool/RareSubtreePatterns/MainTheorems.lean, line 44](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns/MainTheorems.lean#L44): “Under the critical stable-domain assumption, microscopicity and non-clustering with a common sublinear divergent cutoff give Poisson approximation for bounded expected marked counts, and a law of large numbers when the expected count diverges, along admissible tree sizes.”
- [`PoissonDeclumping.poissonApproximation2`](https://leanpool.github.io/lean-pool/LeanPool/RareSubtreePatterns/MainTheorems.html#PoissonDeclumping.poissonApproximation2) (theorem; a main declaration), declared in [LeanPool/RareSubtreePatterns/MainTheorems.lean, line 48](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns/MainTheorems.lean#L48): “For a root-degree set B with positive finite weight c_B, structural microscopicity of the original marks and non-clustering of the root-declumped marks yield Poisson approximation with the c_B-adjusted parameter when expected counts are bounded, and divergence in probability when they grow, along admissible tree sizes.”
- [`PoissonDeclumping.maxString`](https://leanpool.github.io/lean-pool/LeanPool/RareSubtreePatterns/MainTheorems.html#PoissonDeclumping.maxString) (theorem; a main declaration), declared in [LeanPool/RareSubtreePatterns/MainTheorems.lean, line 52](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns/MainTheorems.lean#L52): “For critical offspring laws in a stable domain, the maximum non-fringe complete r-ary height has a lattice-Gumbel law for unary strings and two-point localization for r at least two, with the stated offspring probabilities and single-point refinements along phase-separated admissible subsequences.”
- [`PoissonDeclumping.maxLeafHeight`](https://leanpool.github.io/lean-pool/LeanPool/RareSubtreePatterns/MainTheorems.html#PoissonDeclumping.maxLeafHeight) (theorem; a main declaration), declared in [LeanPool/RareSubtreePatterns/MainTheorems.lean, line 56](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns/MainTheorems.lean#L56): “The maximum leaf-height has the stated lattice-Gumbel behavior when the unary offspring probability is positive, and the two-point behavior when it is zero, with single-point refinements along phase-separated admissible subsequences and the stated nondegeneracy and stable-domain conditions.”

## Project

- Authors: Igor Kortchemski.
- Source: [arXiv:2607.22291v1](https://arxiv.org/abs/2607.22291v1).
- Project repository: [igor-kortchemski/rare-subtree-patterns](https://github.com/igor-kortchemski/rare-subtree-patterns), at commit [fc5ef722](https://github.com/igor-kortchemski/rare-subtree-patterns/tree/fc5ef722392b1af41e8b9d5fc45d5a521b7823dd).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60J80, 60G50, 05C05, 05C80.
- In Lean Pool: [LeanPool/RareSubtreePatterns](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns), from the card [LeanPool/projects/rare-subtree-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rare-subtree-patterns.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/rare-subtree-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rare-subtree-patterns.yaml)
- [Lean Pool at 701389c0: LeanPool/RareSubtreePatterns](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RareSubtreePatterns)
