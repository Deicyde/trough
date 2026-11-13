---
declaration: theorem
origin: cited
lean: DimdPolyShowcaseChallenge.stable_phase_retrieval
statement: formalized
proof: formalized
---

# Stable phase retrieval for Hermite-Fock expansions

> Formalizes stable phase retrieval for finite Hermite-Fock polynomials and their Gaussian L2 closure in d complex dimensions, together with the quantitative one-dimensional Fock-space local stability estimate that underlies it.

*Quoted from the card [LeanPool/projects/phaseretrieval.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/phaseretrieval.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DimdPolyShowcaseChallenge.stable_phase_retrieval`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/DimdPoly.html#DimdPolyShowcaseChallenge.stable_phase_retrieval) (theorem; a main declaration), declared in [LeanPool/PhaseRetrieval/DimdPoly.lean, line 126](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/DimdPoly.lean#L126): “Proves stable phase retrieval for the Gaussian L2 closure of finite d-dimensional Hermite-Fock polynomials at a fixed level, giving a uniform stability constant bounding the phase-aligned L2 distance by the L2 distance of magnitudes.” Its source, as the card gives it: “R. Balan, P. Casazza, D. Edidin, On signal reconstruction without phase, Appl. Comput. Harmon. Anal. 20 (2006), 345-356, doi:10.1016/j.acha.2005.07.001.”
- [`FockSPR.orthogonalReduction_exists_phase`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/Constant.html#FockSPR.orthogonalReduction_exists_phase) (theorem), declared in [LeanPool/PhaseRetrieval/Constant.lean, line 61](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/Constant.lean#L61): “Proves the phase-aligned one-dimensional Fock-space local stability estimate, producing a unit phase for which the L2 distance to one is controlled by the magnitude defect.”
- [`FockSPR.orthogonalReduction_core`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/Constant.html#FockSPR.orthogonalReduction_core) (theorem), declared in [LeanPool/PhaseRetrieval/Constant.lean, line 49](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/Constant.lean#L49): “Proves the quantitative centered core estimate bounding the Gaussian Fock norm of a polynomial with small norm by the magnitude defect against one.”
- [`FockSPR.LocalFockSPR`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/Constant/Internal/MainTheorem.html#FockSPR.LocalFockSPR) (theorem), declared in [LeanPool/PhaseRetrieval/Constant/Internal/MainTheorem.lean, line 784](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/Constant/Internal/MainTheorem.lean#L784): “Proves the local Fock-space stable phase retrieval coercivity estimate for centered polynomials.”
- [`DimdPolyShowcaseChallenge.HermitePoly`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/DimdPoly.html#DimdPolyShowcaseChallenge.HermitePoly) (def), declared in [LeanPool/PhaseRetrieval/DimdPoly.lean, line 60](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/DimdPoly.lean#L60): “Defines the normalized one-variable complex Hermite-Fock basis polynomial.”
- [`DimdPolyShowcaseChallenge.TrueHermiteFunctions`](https://leanpool.github.io/lean-pool/LeanPool/PhaseRetrieval/DimdPoly.html#DimdPolyShowcaseChallenge.TrueHermiteFunctions) (def), declared in [LeanPool/PhaseRetrieval/DimdPoly.lean, line 116](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval/DimdPoly.lean#L116): “Defines the Gaussian L2 closure of finite Hermite-Fock polynomials at a fixed level.”

## Project

- Authors: Susanna Bertolini, Jaume de Dios Pont.
- Source: *Stable phase retrieval for Hermite-Fock expansions* by Susanna Bertolini, Jaume de Dios Pont.
- Project repository: [susannabertolini/PhaseRetrieval](https://github.com/susannabertolini/PhaseRetrieval).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42C05, 46E22, 94A12.
- In Lean Pool: [LeanPool/PhaseRetrieval](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval), from the card [LeanPool/projects/phaseretrieval.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/phaseretrieval.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/phaseretrieval.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/phaseretrieval.yaml)
- [Lean Pool at 701389c0: LeanPool/PhaseRetrieval](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PhaseRetrieval)
