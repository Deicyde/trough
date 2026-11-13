---
declaration: theorem
origin: cited
lean: EhrhardGaussian.ehrhard_inequality, EhrhardGaussian.gaussian_convexity, EhrhardGaussian.Provider.ehrhardType_representation, EhrhardGaussian.Provider.ehrhardType_weakClosure, EhrhardGaussian.Provider.ehrhardType_momentBounds
statement: formalized
proof: formalized
---

# Ehrhard's inequality and Gaussian log-MGF convexity

> Ehrhard's convex-set inequality for finite-dimensional Gaussian laws, including singular covariance, and convexity at every real order of the normalized logarithmic moment-generating function of a finite convex Gaussian functional with all positive exponential moments. Includes Gaussian interpolation, quantile transport, representation of Ehrhard-type laws as monotone convex Gaussian images, weak closure, and normalized moment bounds.

*Quoted from the card [LeanPool/projects/ehrhard-gaussian-convexity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ehrhard-gaussian-convexity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`EhrhardGaussian.ehrhard_inequality`](https://leanpool.github.io/lean-pool/LeanPool/EhrhardGaussian/Results/EhrhardInequality.html#EhrhardGaussian.ehrhard_inequality) (theorem; a main declaration), declared in [LeanPool/EhrhardGaussian/Results/EhrhardInequality.lean, line 25](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian/Results/EhrhardInequality.lean#L25): “For a finite-dimensional Gaussian law, convex sets A and B, and t in [0,1], Gaussian CDF lower thresholds a and b for their probabilities give the CDF lower threshold (1-t)a+tb for the probability of their Minkowski combination. Singular covariance and unit masses are allowed; a zero-mass set has no finite admissible threshold.”
- [`EhrhardGaussian.gaussian_convexity`](https://leanpool.github.io/lean-pool/LeanPool/EhrhardGaussian/Results/GaussianConvexity.html#EhrhardGaussian.gaussian_convexity) (theorem; a main declaration), declared in [LeanPool/EhrhardGaussian/Results/GaussianConvexity.lean, line 24](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian/Results/GaussianConvexity.lean#L24): “For a finite convex real function of a finite-dimensional Gaussian vector with every positive exponential moment finite, log E[exp(qF)]/q, defined at q=0 by E[F], is convex on the whole real line.”
- [`EhrhardGaussian.Provider.ehrhardType_representation`](https://leanpool.github.io/lean-pool/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.html#EhrhardGaussian.Provider.ehrhardType_representation) (theorem; a main declaration), declared in [LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean#L28): “A real probability law is of Ehrhard type exactly when it is the pushforward of the standard Gaussian law by a finite monotone convex function; constant functions and Dirac laws are included.”
- [`EhrhardGaussian.Provider.ehrhardType_weakClosure`](https://leanpool.github.io/lean-pool/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.html#EhrhardGaussian.Provider.ehrhardType_weakClosure) (theorem; a main declaration), declared in [LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean, line 34](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean#L34): “The weak limit of a sequence of Ehrhard-type real probability laws is again of Ehrhard type.”
- [`EhrhardGaussian.Provider.ehrhardType_momentBounds`](https://leanpool.github.io/lean-pool/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.html#EhrhardGaussian.Provider.ehrhardType_momentBounds) (theorem; a main declaration), declared in [LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean, line 43](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian/Provider/EhrhardTypeCharacterization.lean#L43): “An Ehrhard-type law with integrable exponential and E[exp(X)]=1 has an integrable square, variance at most -2 E[X], and the stated Gaussian negative exponential-moment bounds. A finite second positive exponential moment yields the further normalized moment comparison.”

## Project

- Authors: Scott Armstrong, Ahmed Bou-Rabee.
- Source: *A Gaussian Convexity for Logarithmic Moment Generating Functions with Applications in Spin Glasses*, [arXiv:2311.08351](https://arxiv.org/abs/2311.08351).
- Project repository: [scottnarmstrong/Critical2DKPZ](https://github.com/scottnarmstrong/Critical2DKPZ), at commit [f1c98dac](https://github.com/scottnarmstrong/Critical2DKPZ/tree/f1c98dacb2a83737096bd976019dfa2c5986ee5a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60D05, 60E15, 52A40.
- In Lean Pool: [LeanPool/EhrhardGaussian](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian), from the card [LeanPool/projects/ehrhard-gaussian-convexity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ehrhard-gaussian-convexity.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/ehrhard-gaussian-convexity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ehrhard-gaussian-convexity.yaml)
- [Lean Pool at 701389c0: LeanPool/EhrhardGaussian](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EhrhardGaussian)
