---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Copula.exists_sklarCopula
statement: formalized
proof: formalized
---

# Finite-dimensional copulas and Sklar's theorem

> Constructs copulas as probability measures with uniform coordinate marginals, proves Sklar's theorem for arbitrary finite-dimensional real laws, and proves uniqueness for continuous marginals and equality on marginal CDF ranges in general. Establishes the equivalence with the classical normalized, grounded, uniform-margin, rectangle-increasing CDF conditions without assuming continuity. Includes compact quantile sampling, randomized inverse disintegration, general lifting of joint laws, Lipschitz bounds, and finite atomic approximation.

*Quoted from the card [LeanPool/projects/finite-dimensional-copulas.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-dimensional-copulas.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ProbabilityTheory.Copula.exists_sklarCopula`](https://leanpool.github.io/lean-pool/LeanPool/Copula/Sklar/General.html#ProbabilityTheory.Copula.exists_sklarCopula) (theorem; a main declaration), declared in [LeanPool/Copula/Sklar/General.lean, line 29](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula/Sklar/General.lean#L29): “Every probability measure on a finite-dimensional real vector space admits a copula whose CDF, evaluated at the marginal CDFs, equals the joint CDF. Atoms, singular joint laws, and dimension zero are allowed.” Its source, as the card gives it: “Upstream Copula/Sklar/General.lean. Completed in commit eaee4eab6931066921870358c0f4bc0b8bd32068 on 2026-09-18 at 13:15:59 UTC; publicly released as v0.1.0 on 2026-09-19 at 07:05:23 UTC at https://github.com/Corrram/copula/releases/tag/v0.1.0.”
- [`ProbabilityTheory.Copula.existsUnique_sklarCopula_of_continuous`](https://leanpool.github.io/lean-pool/LeanPool/Copula/Sklar/Continuous.html#ProbabilityTheory.Copula.existsUnique_sklarCopula_of_continuous) (theorem), declared in [LeanPool/Copula/Sklar/Continuous.lean, line 132](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula/Sklar/Continuous.lean#L132): “If each marginal CDF is continuous, the Sklar copula exists and is unique on the entire closed unit cube; strict monotonicity is unnecessary.” Its source, as the card gives it: “Upstream Copula/Sklar/Continuous.lean.”
- [`ProbabilityTheory.Copula.IsSklarCopula.cdf_eq_on_ranges`](https://leanpool.github.io/lean-pool/LeanPool/Copula/Sklar/Continuous.html#ProbabilityTheory.Copula.IsSklarCopula.cdf_eq_on_ranges) (theorem), declared in [LeanPool/Copula/Sklar/Continuous.lean, line 101](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula/Sklar/Continuous.lean#L101): “Any two Sklar copulas for the same real joint law have equal CDFs whenever every coordinate belongs to the range of the corresponding marginal CDF.” Its source, as the card gives it: “Upstream Copula/Sklar/Continuous.lean.”
- [`ProbabilityTheory.Copula.isClassical_iff_existsUnique`](https://leanpool.github.io/lean-pool/LeanPool/Copula/Classical/Characterization.html#ProbabilityTheory.Copula.isClassical_iff_existsUnique) (theorem), declared in [LeanPool/Copula/Classical/Characterization.lean, line 122](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula/Classical/Characterization.lean#L122): “A real function on the finite unit cube is normalized, grounded, has uniform one-dimensional margins, and has nonnegative ordered rectangle increments if and only if it is the CDF of exactly one copula probability measure. Continuity follows from these conditions and is not an extra hypothesis.” Its source, as the card gives it: “Upstream Copula/Classical/Characterization.lean, completed in commit 5578d2b62ad948570a3edce60330d012e6b5c97b on 2026-09-18 at 13:58:11 UTC.”
- [`ProbabilityTheory.Copula.exists_lift`](https://leanpool.github.io/lean-pool/LeanPool/Copula/Sklar/Lift.html#ProbabilityTheory.Copula.exists_lift) (theorem), declared in [LeanPool/Copula/Sklar/Lift.lean, line 22](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula/Sklar/Lift.lean#L22): “A joint probability law on a finite power of a standard Borel space lifts to a copula through any measurable coordinate sampling maps from the uniform unit interval whose pushforwards are the given marginal laws.” Its source, as the card gives it: “Upstream Copula/Sklar/Lift.lean.”

## Project

- Authors: Marcus Rockel, Gaëtan Serré, Rémy Degenne.
- Source: *Copula — finite-dimensional copulas in Lean 4* by Marcus Rockel.
- Project repository: [Corrram/copula](https://github.com/Corrram/copula), at commit [fe53ea2f](https://github.com/Corrram/copula/tree/fe53ea2f3e6af41da8541e7d0aa2edc38ed0dcc8).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 60E05, 60B05.
- In Lean Pool: [LeanPool/Copula](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula), from the card [LeanPool/projects/finite-dimensional-copulas.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-dimensional-copulas.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/finite-dimensional-copulas.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-dimensional-copulas.yaml)
- [Lean Pool at 307e3125: LeanPool/Copula](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Copula)
