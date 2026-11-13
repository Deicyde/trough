---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.IterateLipschitzNullFixedPointWanted.exists_fixedPoint_of_iterate_lipschitz_tendsto_zero, MathlibExt.Analysis.FunctionalAnalysis.MarkovKakutani.markovKakutani_commonFixedPoint
statement: formalized
---

# Fixed-point theory: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/index.html).

Fixed points of nonexpansive, Lipschitz and affine maps: the Browder–Göhde–Kirk theorem and Kirk's normal structure, Markov–Kakutani, Browder's demiclosedness principle, maps with contracting iterates.

## Fixed points of maps whose iterates have null Lipschitz constants

Let $X$ be a nonempty
complete metric space, let $f : X \to X$, and write $f^n$ for the $n$-th iterate of $f$. Let
$(q_n)_{n \in \mathbb{N}}$ be a sequence of nonnegative real numbers with $q_n \to 0$ such that
$d(f^n(x), f^n(y)) \le q_n \, d(x, y)$ for every $n \ge 1$ and all $x, y \in X$. Then $f$ has a
fixed point: there is $x \in X$ with $f(x) = x$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Operator theory; Nonlinear operators and their properties), problem `ma_proofbench_l1_74`.

Stated but not proved: `MathlibExt.Analysis.Calculus.IterateLipschitzNullFixedPointWanted.exists_fixedPoint_of_iterate_lipschitz_tendsto_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/IterateLipschitzNullFixedPointWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/IterateLipschitzNullFixedPointWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/index.html#exists-fixed-point-of-iterate-lipschitz).

## Markov–Kakutani fixed-point theorem

Let $K$ be a nonempty compact convex subset of a real
normed space $E$, and let $(F_i)_{i \in I}$ be a family of continuous affine maps $E \to E$ such
that each $F_i$ maps $K$ into $K$ and $F_i(F_j(x)) = F_j(F_i(x))$ for all $i, j \in I$ and all
$x \in E$. Then there is $x \in K$ with $F_i(x) = x$ for every $i \in I$.

Commutation is required on all of $E$, not only on $K$.

## Sources

- A. Markov, C. R. Acad. Sci. URSS 1936 and S. Kakutani, Proc. Imp. Acad. Tokyo 14 (1938) 242-245, Markov-Kakutani fixed-point theorem; Lean states real normed nonempty compact convex case with globally commuting `E →ᴬ[ℝ] E` family.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MarkovKakutani.markovKakutani_commonFixedPoint`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MarkovKakutani.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/MarkovKakutani.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/index.html#markov-kakutani-common-fixed-point).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed-point theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/fixed-point-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/fixed-point-theory)
