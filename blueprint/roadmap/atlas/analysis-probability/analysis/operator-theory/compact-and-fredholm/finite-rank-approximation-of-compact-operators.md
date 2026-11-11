---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CompactFiniteRankApprox.exists_finiteRank_approx, MathlibExt.Analysis.InnerProductSpace.CompactFiniteRankApprox.exists_tendsto_finiteRank_approx
statement: formalized
proof: formalized
---

# Finite-rank approximation of compact operators

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/finite-rank-approximation-of-compact-operators/index.html).

## Finite-rank approximation of compact operators

Let $H$ be an inner product space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ ($H$ need not be complete),
and let $T$ be a compact bounded linear operator on $H$. For every real $\varepsilon > 0$ there
is a bounded linear operator $F$ on $H$ with finite-dimensional range such that
$\|T - F\| \le \varepsilon$.

The approximant is the composition of $T$ with the orthogonal projection onto the span of a
finite $\varepsilon$-net for the image of the closed unit ball.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactFiniteRankApprox.exists_finiteRank_approx`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactFiniteRankApprox.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactFiniteRankApprox.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/finite-rank-approximation-of-compact-operators/index.html#exists-finite-rank-approx).

## Compact operators are norm limits of finite-rank operators

Let $H$ be an inner product
space over $\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ ($H$ need not be
complete), and let $T$ be a compact bounded linear operator on $H$. Then there is a sequence
$(F_n)_{n \in \mathbb{N}}$ of bounded linear operators on $H$, each with finite-dimensional
range, such that $\|T - F_n\| \to 0$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactFiniteRankApprox.exists_tendsto_finiteRank_approx`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactFiniteRankApprox.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactFiniteRankApprox.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/finite-rank-approximation-of-compact-operators/index.html#exists-tendsto-finite-rank-approx).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite-rank approximation of compact operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/finite-rank-approximation-of-compact-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/finite-rank-approximation-of-compact-operators)
