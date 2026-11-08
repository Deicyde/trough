---
declaration: theorem
origin: cited
lean: LCAnalysis.ContDiffMBOn.comp, LCAnalysis.ContDiffMBOn.exists_iteratedDMB_multilinear, LCAnalysis.smoothMBOn_iff_contDiffOn, LCAnalysis.exists_hasWeakIntegral, LCAnalysis.mackeyComplete_iff_integratesLipschitzCurves, LCAnalysis.ContDiffMBOn.of_comp_of_boundedBelow
statement: formalized
proof: formalized
---

# Michal–Bastiani Calculus on Locally Convex Spaces

> Develops real Michal–Bastiani calculus on Hausdorff locally convex spaces, with the chain rule, continuous symmetric higher differentials, and Taylor's formula in weak form. It proves equivalence with smooth Fréchet calculus on open subsets of normed spaces. Weak integrals exist for continuous curves in sequentially complete spaces and for continuously differentiable curves in Mackey complete spaces; Mackey completeness is characterized by weak integrability of Lipschitz curves. A smooth map from a Banach space to a normed space with derivative uniformly bounded below reflects finite differentiability of continuous maps from open locally convex domains.

*Quoted from the card [LeanPool/projects/lc-analysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lc-analysis.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LCAnalysis.ContDiffMBOn.comp`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/MichalBastiani.html#LCAnalysis.ContDiffMBOn.comp) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/MichalBastiani.lean, line 512](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/MichalBastiani.lean#L512): “Composing two real Michal–Bastiani C^k maps between open subsets of Hausdorff locally convex spaces preserves C^k regularity, provided the inner map takes the first domain into the second.”
- [`LCAnalysis.ContDiffMBOn.exists_iteratedDMB_multilinear`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/Higher.html#LCAnalysis.ContDiffMBOn.exists_iteratedDMB_multilinear) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/Higher.lean, line 599](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/Higher.lean#L599): “At every point of its open domain, the kth differential of a Michal–Bastiani C^k map is a continuous symmetric k-linear map.”
- [`LCAnalysis.smoothMBOn_iff_contDiffOn`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/MBFrechet.html#LCAnalysis.smoothMBOn_iff_contDiffOn) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/MBFrechet.lean, line 382](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/MBFrechet.lean#L382): “On open subsets of real normed spaces, Michal–Bastiani smoothness is equivalent to Fréchet smoothness.”
- [`LCAnalysis.exists_hasWeakIntegral`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/IntegralExistence.html#LCAnalysis.exists_hasWeakIntegral) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/IntegralExistence.lean, line 333](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/IntegralExistence.lean#L333): “A continuous curve on the closed interval between any two real endpoints has a weak integral in every sequentially complete Hausdorff locally convex target space.”
- [`LCAnalysis.mackeyComplete_iff_integratesLipschitzCurves`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/MackeyLipschitz.html#LCAnalysis.mackeyComplete_iff_integratesLipschitzCurves) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/MackeyLipschitz.lean, line 528](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/MackeyLipschitz.lean#L528): “In a Hausdorff locally convex real space, convergence of Mackey–Cauchy sequences is equivalent to existence of weak integrals for all curves whose difference quotients form a bounded set on every nondegenerate compact real interval.”
- [`LCAnalysis.ContDiffMBOn.of_comp_of_boundedBelow`](https://leanpool.github.io/lean-pool/LeanPool/LCAnalysis/BoundedBelow.html#LCAnalysis.ContDiffMBOn.of_comp_of_boundedBelow) (theorem; a main declaration), declared in [LeanPool/LCAnalysis/BoundedBelow.lean, line 291](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis/BoundedBelow.lean#L291): “Let j be a smooth map from an open subset U of a real Banach space to a real normed space, with a fixed m > 0 such that every x in U and every vector v satisfy norm(dj(x)v) >= m \* norm(v). If gamma maps an open locally convex domain continuously into U and j composed with gamma is C^k in the sense of Michal–Bastiani, then gamma is C^k.”

## Project

- Authors: Gabriel Larotonda.
- Source: *Infinite-Dimensional Lie Groups* by Helge Glöckner, Karl-Hermann Neeb, [arXiv:2602.12362](https://arxiv.org/abs/2602.12362).
- Project repository: [glaroton/LCAnalysis](https://github.com/glaroton/LCAnalysis), at commit [c7c5a228](https://github.com/glaroton/LCAnalysis/tree/c7c5a228221bba0313e7caee62ca0f9b1e2e5c0f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46T20, 46A03, 58B10.
- In Lean Pool: [LeanPool/LCAnalysis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis), from the card [LeanPool/projects/lc-analysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lc-analysis.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lc-analysis.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lc-analysis.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LCAnalysis](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LCAnalysis)
