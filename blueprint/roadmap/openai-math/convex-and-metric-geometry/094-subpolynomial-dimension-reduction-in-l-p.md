---
declaration: section
origin: cited
lean: OAI.SubpolynomialLp.source_main
statement: formalized
proof: formalized
---

# 094. Subpolynomial dimension reduction in $L_{p}$

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed $1\lt p\lt \infty$ and distortion *D* > 1, every *n*-point subset of real $L_{p}$ embeds into $\ell_p^d$ with distortion at most *D* and dimension $d=n^{o(1)}$, answering Naor's sublinear-dimension question for *p* ≠ 2. In contrast, exact embeddings require worst-case dimension $\Theta(n^2)$ when *p* ≠ 2.

## Subpolynomial dimension reduction in Lp

For every fixed $1\lt p\lt \infty$ and *D* > 1, every *n*-point subset of a real $L_{p}$ space embeds into $\ell_p^d$ with distortion at most *D* and subpolynomial dimension $d=n^{o(1)}$. The target has the same exponent *p*, and the embedding need not be linear.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

For $p>1$, $p\ne2$, the formalization bounds the least dimension needed to embed every $n$-point subset of real $L_p$ with distortion $D$. For each fixed $D>1$, there is a constant $C=C(p,D)$ such that this dimension lies between $\log n/\log(1+2D)$ and $\exp(C(\log n)^{\gamma(p)})$ for every $n\ge2$, where $\gamma(p)=2-p$ for $p<2$ and $1-2/p$ for $p>2$. At distortion $1$ and $n\ge9$, it lies between $\lfloor(n-1)/4\rfloor^2$ and $\binom n2$. The least dimension is attained, and its logarithm divided by $\log n$ tends to $0$ for $D>1$ and to $2$ for $D=1$.

## Lean: Dimension reduction in $L_p$

Stated in [SubpolynomialLp.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SubpolynomialLp.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem source_main (p : ℝ) (hp : 1 < p) (hp2 : p ≠ 2) :
    (∀ D : ℝ, 1 < D → ∃ C : ℝ, ∀ n : ℕ, 2 ≤ n →
      GoodDimension.{u} p n D (dimension.{u} p n D) ∧
      Real.log (n : ℝ) / Real.log (1 + 2 * D) ≤ (dimension.{u} p n D : ℝ) ∧
      (dimension.{u} p n D : ℝ) ≤ Real.exp (C * Real.log (n : ℝ) ^ gamma p)) ∧
    (∀ n : ℕ, 9 ≤ n →
      GoodDimension.{u} p n 1 (dimension.{u} p n 1) ∧
      ((n - 1) / 4) ^ 2 ≤ dimension.{u} p n 1 ∧
      dimension.{u} p n 1 ≤ n.choose 2) ∧
    (∀ D : ℝ, 1 ≤ D →
      Tendsto (fun n : ℕ => Real.log (dimension.{u} p n D : ℝ) / Real.log (n : ℝ))
        atTop (𝓝 (if 1 < D then 0 else 2)))
```

Proved in [lean/OAI/Analysis/LpDimension/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LpDimension/Main.lean#L13).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/094.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/094.md)
