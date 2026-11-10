---
declaration: theorem
origin: cited
lean: Erdos652.erdos_652, Erdos652.erdos_652.variants.first, Erdos652.erdos_652.variants.product, Erdos652.erdos_652.variants.elekes, Erdos652.erdos_652.variants.mathialagan, Erdos652.erdos_652.variants.kth_lower_bound, Erdos652.erdos_652.variants.order_sqrt
statement: formalized
---

# Erdős Problem 652

> *References:*
> - [erdosproblems.com/652](https://www.erdosproblems.com/652)
> - [Ma21] Mathialagan, Surya, *On bipartite distinct distances in the plane*.
>   Electron. J. Combin. **28** (2021), no. 4, Paper No. 4.33, 25 pp.
>   [doi:10.37236/9687](https://doi.org/10.37236/9687)
> - [Discussion](https://www.erdosproblems.com/forum/thread/652)

*Quoted from [FormalConjectures/ErdosProblems/652.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/652](https://www.erdosproblems.com/652).

The file states 7 research or textbook statements: 7 solved. It also has 1 test statement, counted here but not shown.

## `Erdos652.erdos_652`

Solved: stated here without proof.

> Let $x_1,\ldots,x_n\in \mathbb{R}^2$ and let
> $R(x_i)=\#\{ \lvert x_j-x_i\rvert : j\neq i\}$, where the points are ordered such that
>
> $$R(x_1)\leq \cdots \leq R(x_n).$$
>
> Let $\alpha_k$ be minimal such that, for all large enough $n$, there exists a set of $n$ points
> with $R(x_k)\lt \alpha_kn^{1/2}$. Is it true that $\alpha_k\to \infty$ as $k\to \infty$?
>
> Mathialagan [Ma21] proved that given a set $P$ of $k$ points and a set $Q$ of $n$ points,
> with $2\leq k\leq n^{1/3}$, there exists a point in $P$ which determines
> $\gg (kn)^{1/2}$ distances to points in $Q$.

```lean
theorem erdos_652 : Tendsto alpha atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L69).

## `Erdos652.erdos_652.variants.first`

Solved: stated here without proof.

> It is trivial that $R(x_1)=1$ is possible.
> We require $n\geq 2$ because a singleton determines no distances to other points.

```lean
theorem erdos_652.variants.first (n : ℕ) (hn : 2 ≤ n) :
    ∃ points : Finset ℝ², points.card = n ∧
      ∃ point ∈ points, distinctDistancesFrom points point = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L75).

## `Erdos652.erdos_652.variants.product`

Solved: stated here without proof.

> We always have $R(x_1)R(x_2)\gg n$.
> Equivalently, the same bound holds for any two distinct points of the set.

```lean
theorem erdos_652.variants.product :
    ∃ c : ℝ, 0 < c ∧ ∀ points : Finset ℝ²,
      ∀ p ∈ points, ∀ q ∈ points, p ≠ q →
        c * points.card ≤
          (distinctDistancesFrom points p : ℝ) * distinctDistancesFrom points q
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L83).

## `Erdos652.erdos_652.variants.elekes`

Solved: stated here without proof.

> Elekes proved that for every $k$ and $n$ sufficiently large there exists some set of
> $n$ points with $R(x_k)\ll_k n^{1/2}$.

```lean
theorem erdos_652.variants.elekes :
    ∀ k : ℕ, ∃ a : ℝ, AdmissibleConstant k a
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L93).

## `Erdos652.erdos_652.variants.mathialagan`

Solved: stated here without proof.

> Mathialagan [Ma21, Theorem 14] proved that given a set $P$ of $k$ points and a set $Q$
> of $n$ points, with $2\leq k\leq n^{1/3}$, there exists a point in $P$ which determines
> $\gg (kn)^{1/2}$ distances to points in $Q$.

```lean
theorem erdos_652.variants.mathialagan :
    ∃ c : ℝ, 0 < c ∧ ∀ P Q : Finset ℝ²,
      2 ≤ P.card → P.card ^ 3 ≤ Q.card →
        ∃ p ∈ P, c * Real.sqrt ((P.card : ℝ) * Q.card) ≤
          (Q.image fun q => dist p q).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L102).

## `Erdos652.erdos_652.variants.kth_lower_bound`

Solved: stated here without proof.

> Mathialagan's bound immediately implies $R(x_k)\gg (kn)^{1/2}$ for
> $2\leq k\leq n^{1/3}$: fewer than $k$ points have distance count below the bound.

```lean
theorem erdos_652.variants.kth_lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∀ points : Finset ℝ², ∀ k : ℕ,
      2 ≤ k → k ^ 3 ≤ points.card →
        (points.filter fun point => (distinctDistancesFrom points point : ℝ) <
          c * Real.sqrt ((k : ℝ) * points.card)).card < k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L113).

## `Erdos652.erdos_652.variants.order_sqrt`

Solved: stated here without proof.

> Elekes' construction and Mathialagan's lower bound give
> $\alpha_k=\Theta(\sqrt k)$, as noted by Zach Hunter in the discussion.

```lean
theorem erdos_652.variants.order_sqrt :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∀ᶠ k : ℕ in atTop,
      c * Real.sqrt k ≤ alpha k ∧ alpha k ≤ C * Real.sqrt k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/652.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/652.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/652.lean)
- [erdosproblems.com/652](https://www.erdosproblems.com/652)
