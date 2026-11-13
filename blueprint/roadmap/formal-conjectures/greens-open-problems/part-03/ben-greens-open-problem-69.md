---
declaration: theorem
origin: cited
lean: Green69.green_69, Green69.green_69.variants.elekes_szabo
statement: formalized
---

# Ben Green's Open Problem 69

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.69)
> - [ES13] Elekes, G. and Szabó, E., *On triple lines and cubic curves --- the Orchard problem
>   revisited*. (2013). [arXiv:1302.5777](https://arxiv.org/abs/1302.5777)
> - [GT13] Green, B. and Tao, T., *On sets defining few ordinary lines*. Discrete Comput. Geom. 50
>   (2013), 409--468. [arXiv:1208.4714](https://arxiv.org/abs/1208.4714)

*Quoted from [FormalConjectures/GreensOpenProblems/69.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/69.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 1 API statement, counted here but not shown.

## `Green69.green_69`

Open: stated without proof.

> Fix a number $k$. Let $A \subset \mathbb{R}^2$ be a set of $n$ points, with no more than $k$ on
> any line. Suppose that, for at least $\delta n^2$ pairs of points $(x, y) \in A \times A$, the
> line $xy$ contains a third point of $A$. Is there some cubic curve containing at least $cn$
> points of $A$, for some $c = c(k, \delta) > 0$?
>
> We count ordered pairs of distinct points (`numPairsWithThird`), and a cubic curve is the zero set
> of any nonzero real polynomial of degree at most $3$ (`OnCubic`), reducible ones included. The
> constant $c$ depends only on $k$ and $\delta$. Small $n$ are harmless, since any $9$ points lie on
> a cubic curve. [Gr24] notes that very little is known, except when $\delta = 1 - O(1/n)$, where the
> statement follows from the main results of [GT13].

```lean
theorem green_69 :
    ∀ k : ℕ, ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ A : Finset (ℝ × ℝ), AtMostOnLine k A →
      δ * (#A : ℝ) ^ 2 ≤ numPairsWithThird A → ∃ S ⊆ A, c * #A ≤ #S ∧ OnCubic S
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/69.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/69.lean#L87).

## `Green69.green_69.variants.elekes_szabo`

Open: stated without proof.

> **Elekes–Szabó conjecture.** If a set $H$ of points in the plane has at least $c|H|^2$ triple
> lines (lines containing at least three points of $H$), then ten or more points of $H$ lie on a
> (possibly degenerate) cubic, provided that $|H| > n_0(c)$ [ES13, Conjecture 2.1].
>
> [Gr24] states it with $cn^2$ collinear triples in place of triple lines, and notes that it is much
> weaker than `green_69` but should hold without the assumption of no more than $k$ points on a
> line. The two forms are equivalent: $10$ collinear points lie on a cubic, and otherwise each
> triple line contains at most $\binom{9}{3}$ collinear triples. The bound $n_0(c)$ is needed, since
> a set of fewer than $10$ points can have $c|H|^2$ triple lines for small $c$. For points on an
> irreducible curve of bounded degree, see [ES13, Theorem 2.2].

```lean
theorem green_69.variants.elekes_szabo :
    ∀ c : ℝ, 0 < c → ∃ n₀ : ℕ, ∀ A : Finset (ℝ × ℝ), n₀ < #A →
      c * (#A : ℝ) ^ 2 ≤ (tripleLines A).ncard → ∃ S ⊆ A, #S = 10 ∧ OnCubic S
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/69.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/69.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/69.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/69.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.69)
