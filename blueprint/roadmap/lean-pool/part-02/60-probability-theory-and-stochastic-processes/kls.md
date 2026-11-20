---
declaration: theorem
origin: cited
lean: FunctionalInequalities.KLS.kls, KLSOpenAI.kls, KLSOpenAI.kls_locallyLipschitz
statement: formalized
proof: formalized
---

# The dimension-free Kannan–Lovász–Simonovits bound

> Formalizes the dimension-free Poincaré bound of Bizeul, Klartag and Lehec via cutoff stochastic localization. The project includes the covariance-normalized bound and two density formulations.

*Quoted from the card [LeanPool/projects/kls.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/kls.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FunctionalInequalities.KLS.kls`](https://leanpool.github.io/lean-pool/LeanPool/KLS/FunctionalInequalities/KLS/Target.html#FunctionalInequalities.KLS.kls) (theorem; a main declaration), declared in [LeanPool/KLS/FunctionalInequalities/KLS/Target.lean, line 38](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KLS/FunctionalInequalities/KLS/Target.lean#L38): “The Poincaré constant of a finite-dimensional log-concave probability measure with finite second moment is bounded by a universal constant times the operator norm of its covariance, including on singular affine supports.” Its source, as the card gives it: “P. Bizeul, B. Klartag and J. Lehec, arXiv:2610.05474v1, Theorem 1.1.”
- [`KLSOpenAI.kls`](https://leanpool.github.io/lean-pool/LeanPool/KLS/KLSOpenAI/Target.html#KLSOpenAI.kls) (theorem; a main declaration), declared in [LeanPool/KLS/KLSOpenAI/Target.lean, line 19](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KLS/KLSOpenAI/Target.lean#L19): “One Poincaré constant works for isotropic log-concave probability densities in all positive dimensions and smooth compactly supported test functions.” Its source, as the card gives it: “OpenAI KLS model at commit adc7f1241b42e322a6451854ab7e4b4c146bf78a.”
- [`KLSOpenAI.kls_locallyLipschitz`](https://leanpool.github.io/lean-pool/LeanPool/KLS/KLSOpenAI/Target.html#KLSOpenAI.kls_locallyLipschitz) (theorem; a main declaration), declared in [LeanPool/KLS/KLSOpenAI/Target.lean, line 23](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KLS/KLSOpenAI/Target.lean#L23): “One Poincaré constant works for isotropic log-concave probability densities in all positive dimensions and locally Lipschitz square-integrable test functions, with extended gradient energy.” Its source, as the card gives it: “P. Bizeul, B. Klartag and J. Lehec, arXiv:2610.05474v1, Theorem 1.1.”

## Project

- Authors: kls-lean contributors.
- Source: [arXiv:2610.05474v1](https://arxiv.org/abs/2610.05474v1).
- Project repository: [human-ai-mathematics/kls-lean](https://github.com/human-ai-mathematics/kls-lean), at commit [f280ffb3](https://github.com/human-ai-mathematics/kls-lean/tree/f280ffb3949e275593bb68b9356a70f92d52d1ee).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60E15, 46E35, 52A23.
- In Lean Pool: [LeanPool/KLS](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KLS), from the card [LeanPool/projects/kls.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/kls.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/kls.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/kls.yaml)
- [Lean Pool at 307e3125: LeanPool/KLS](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KLS)
