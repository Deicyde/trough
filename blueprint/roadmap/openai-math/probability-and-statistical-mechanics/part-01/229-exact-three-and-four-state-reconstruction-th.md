---
declaration: section
origin: cited
lean: OAI.ThreeState.TreeClauses.Tree.regular_reconstructs_above_KS, OAI.ThreeState.TreeClauses.Tree.poisson_reconstructs_above_KS
statement: formalized
---

# 229. Exact three- and four-state reconstruction thresholds and four-state tree capacity

3 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the exact reconstruction threshold $d\lambda^2\gt 1$, with nonreconstruction at equality, for three-state symmetric and four-state ferromagnetic broadcasting on regular trees (*d* ≥ 2) and observed Poisson trees (mean *d* > 1 and *d* > 0, respectively), with Poisson advantage averaged without conditioning on survival. The three-state theorem allows both signs of *λ* and gives the exact weak-recovery threshold for the symmetric three-community stochastic block model.

## The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model

We establish the exact Kesten–Stigum reconstruction threshold for the ferromagnetic four-state Potts broadcast model on every regular *d*-ary tree with *d* ≥ 2 and every Poisson Galton–Watson tree of mean *d* > 0. Reconstruction occurs exactly when $d\lambda^2\gt 1$; we prove nonreconstruction at and below the threshold, including equality. In the Poisson model the whole tree is observed and the reconstruction advantage is averaged without conditioning on survival. The proof uses reproducible exact-arithmetic verification of polynomial inequalities.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf).

## A Capacity Criterion for Four-State Potts Reconstruction on Trees

For the ferromagnetic four-state broadcast model with $0\lt \lambda\lt 1$, we prove that reconstruction on a bounded-degree deterministic rooted tree occurs exactly when its $L^{3}$ capacity with edge resistances $\lambda^{-2|e|}$ is positive. This gives an exact criterion without regularity or growth-rate assumptions on the tree, including at the exponential critical boundary.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf).

## The exact reconstruction threshold for the three-state symmetric channel

We determine the exact reconstruction threshold for the symmetric three-state broadcast process on every regular *b*-ary tree, *b* ≥ 2, and every observed Poisson Galton–Watson tree of mean *d* > 1. Reconstruction occurs exactly when $d\lambda^2\gt 1$, with *d* = *b* in the regular model; there is non-reconstruction at equality for either sign of the channel parameter. The Poisson advantage is averaged over trees and spins without conditioning on survival. This resolves the all-degree three-state regular-tree prediction. Combining the Poisson theorem with known tree-to-graph and algorithmic results gives the exact weak-recovery threshold for the symmetric three-community sparse stochastic block model with independent uniform labels, fixed within- and between-community rates $a,b\gt 0$, and mean degree $(a+2b)/3\gt 1$: recovery is possible exactly when $(a-b)^2\gt 3(a+2b)$. Above this threshold it is achievable in $O(n\log n)$ time; at or below it, weak recovery is information-theoretically impossible.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the supercritical direction of reconstruction for the symmetric three-state broadcast channel, whose parameter satisfies $-1/2\le\lambda\le1$. On a regular $b$-ary tree, reconstruction holds when $b\lambda^2>1$; on an observed Poisson Galton–Watson tree of mean $d$, it holds when $d\lambda^2>1$. In each case the root-estimation advantage converges to a positive limit, with the Poisson advantage averaged over trees and spins.

The selected statements cover reconstruction above the Kesten–Stigum threshold. Non-reconstruction at or below the threshold and the stochastic-block-model consequences in the paper are outside them.

## Lean: Supercritical reconstruction on regular and Poisson trees

Stated in [ThreeStateSupercritical.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThreeStateSupercritical.lean).

```lean
theorem regular_supercritical (b : ℕ) (hb : 2 ≤ b) (lam : ℝ) (h : Admissible lam)
    (hcrit : 1 < (b : ℝ) * lam ^ 2) : Reconstructs (regularAdvantage b lam h)
```

Its proof is in [lean/OAI/Probability/ThreeState/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThreeState/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem poisson_supercritical (d : ℝ) (hd : 1 < d) (lam : ℝ) (h : Admissible lam)
    (hcrit : 1 < d * lam ^ 2) : Reconstructs (poissonAdvantage d hd lam h)
```

Its proof is in [lean/OAI/Probability/ThreeState/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThreeState/Main.lean) or a file it imports further down, which this chapter does not read.

## Lean: Three-state reconstruction above the Kesten–Stigum threshold

Stated in [ThreeStateTreeClauses.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThreeStateTreeClauses.lean).

```lean
theorem regular_reconstructs_above_KS (b : ℕ) (lam : ℝ) (hlam : Admissible lam)
    (hKS : 1 < (b:ℝ)*lam^2) : Reconstructs lam hlam (PMF.pure b)
```

Proved in [lean/OAI/Probability/ThreeStateClauses/RegularReconstruction.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThreeStateClauses/RegularReconstruction.lean#L103).

```lean
theorem poisson_reconstructs_above_KS (d : ℝ≥0) (lam : ℝ) (hlam : Admissible lam)
    (hKS : 1 < (d:ℝ)*lam^2) : Reconstructs lam hlam (poissonPMF d)
```

Proved in [lean/OAI/Probability/ThreeStateClauses/PoissonReconstruction.lean, line 192](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThreeStateClauses/PoissonReconstruction.lean#L192).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/229.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/229.md)
