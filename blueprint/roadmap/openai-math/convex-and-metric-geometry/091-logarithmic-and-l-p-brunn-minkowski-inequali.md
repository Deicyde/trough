---
declaration: section
origin: cited
lean: OAI.LogBrunnMinkowski.main
statement: formalized
proof: formalized
---

# 091. Logarithmic and $L_{p}$ Brunn–Minkowski inequalities and the B-conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the logarithmic Brunn–Minkowski inequality for origin-symmetric convex bodies in every dimension, and the scalar-dilation B-conjecture for all even log-concave Radon measures. For Lebesgue volume it also proves the additive $L_{p}$ Brunn–Minkowski inequality for full-dimensional origin-symmetric convex bodies throughout $0\lt p\lt 1$.

## The logarithmic Brunn–Minkowski conjecture

We prove the logarithmic Brunn–Minkowski conjecture for arbitrary origin-symmetric convex bodies in every dimension. The theorem also gives the symmetric $L_{p}$ Brunn–Minkowski inequality for every $0\lt p\lt 1$. Combined with Saroglou's transfer theorem and a support-subspace reduction, it yields the logarithmic inequality for every even log-concave Radon measure and the scalar-dilation $(B)$-conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The logarithmic Brunn–Minkowski conjecture asserts that logarithmic interpolation of origin-symmetric convex bodies preserves the geometric-mean lower bound for volume. The formalized result proves, for every dimension $n\ge1$, such bodies $K,L\subset\mathbb R^n$, and $0\le t\le1$, that their logarithmic Wulff combination has volume at least $|K|^{1-t}|L|^t$. It assumes neither boundary smoothness nor coordinatewise unconditionality.

## Lean: Logarithmic Brunn–Minkowski inequality

```lean
theorem main (n : ℕ) (hn : 1 ≤ n) (K L : Set (Space n))
    (hK : IsConvexBody K) (hL : IsConvexBody L)
    (hsK : OriginSymmetric K) (hsL : OriginSymmetric L)
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    (volume K) ^ (1 - t) * (volume L) ^ t ≤ volume (logCombination K L t)
```

Stated in [LogBrunnMinkowski.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LogBrunnMinkowski.lean#L30). Proved in [lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean, line 24481](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean#L24481). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/091.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/091.md)
