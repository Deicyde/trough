---
declaration: theorem
origin: cited
lean: Erdos743.erdos_743, Erdos743.erdos_743.variants.stars_or_paths, Erdos743.erdos_743.variants.all_but_two_stars, Erdos743.erdos_743.variants.fishburn, Erdos743.erdos_743.variants.bollobas, Erdos743.erdos_743.variants.bounded_degree, Erdos743.erdos_743.variants.almost_linear_degree, Erdos743.erdos_743.variants.largest_trees
statement: formalized
---

# Erdős Problem 743

> *References:*
> - [erdosproblems.com/743](https://www.erdosproblems.com/743)
> - [ABCHPT21] Allen, Peter and Böttcher, Julia and Clemens, Dennis and Hladký, Jan and Piguet,
>   Diana and Taraz, Anusch, *The tree packing conjecture for trees of almost linear maximum
>   degree*. arXiv:2106.11720 (2021).
> - [Bo83] Bollobás, Béla, *Some remarks on packing trees*. Discrete Math. (1983), 203-204.
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.
> - [Fi83] Fishburn, P. C., *Balanced integer arrays: a matrix packing theorem*. J. Combin. Theory
>   Ser. A (1983), 98-101.
> - [Fi83b] Fishburn, P. C., *Packing graphs with odd and even trees*. J. Graph Theory (1983),
>   369-383.
> - [GyLe78] Gyárfás, A. and Lehel, J., *Packing trees of different order into $K_n$*.
>   Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Colloq. Math. Soc. János Bolyai
>   18 (1978), 463-469.
> - [JKKO19] Joos, Felix and Kim, Jaehoon and Kühn, Daniela and Osthus, Deryk, *Optimal packings
>   of bounded degree trees*. J. Eur. Math. Soc. (JEMS) (2019), 3573-3647.
> - [JaMo24] Janzer, Barnabás and Montgomery, Richard, *Packing the largest trees in the tree
>   packing conjecture*. arXiv:2403.10515 (2024).

*Quoted from [FormalConjectures/ErdosProblems/743.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/743](https://www.erdosproblems.com/743).

The file states 8 research or textbook statements: 1 open and 7 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos743.erdos_743`

Open: stated without proof.

> Let $T_2,\ldots,T_n$ be a collection of trees such that $T_k$ has $k$ vertices. Can we always
> write $K_n$ as the edge disjoint union of the $T_k$?
>
> A conjecture of Gyárfás, known as the tree packing conjecture. We state it as a packing. For
> every $n$ and all trees $T_k$ on the vertex set `Fin k`, $2 \leq k \leq n$, there are injective
> maps
> $f_k : \{0, \ldots, k - 1\} \to \{0, \ldots, n - 1\}$ such that the graphs $f_k(T_k)$ are
> pairwise edge-disjoint (see `IsPacking`). Every tree with $k$ vertices is isomorphic to a tree
> on `Fin k`, so this covers every collection of trees.
>
> A tree with $k$ vertices has $k - 1$ edges, and $\sum_{k=2}^{n} (k - 1) = \binom{n}{2}$ is the
> number of edges of $K_n$. Hence the copies $f_k(T_k)$ of a packing cover every edge of $K_n$.
> So a packing is the same as a decomposition of $K_n$ into copies of $T_2, \ldots, T_n$.

```lean
theorem erdos_743 :
    ∀ n : ℕ, ∀ T : (k : ℕ) → SimpleGraph (Fin k),
      (∀ k ∈ Set.Icc 2 n, (T k).IsTree) → IsPacking n (Set.Icc 2 n) T
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L101).

## `Erdos743.erdos_743.variants.stars_or_paths`

Solved: stated here without proof.

> Gyárfás and Lehel [GyLe78] proved that this holds if all but at most $2$ of the trees are stars,
> or if all the trees are stars or paths. This variant is the second case: each tree is a star or a
> path.
>
> Here a star on `Fin k` is `starGraph c` for a centre `c`, and a path is a graph isomorphic to
> `pathGraph k`.

```lean
theorem erdos_743.variants.stars_or_paths (n : ℕ) (T : (k : ℕ) → SimpleGraph (Fin k))
    (hT : ∀ k ∈ Set.Icc 2 n, (T k).IsTree ∧
      ((∃ c : Fin k, T k = starGraph c) ∨ Nonempty (T k ≃g pathGraph k))) :
    IsPacking n (Set.Icc 2 n) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L115).

## `Erdos743.erdos_743.variants.all_but_two_stars`

Solved: stated here without proof.

> Gyárfás and Lehel [GyLe78] proved that this holds if all but at most $2$ of the trees are stars,
> or if all the trees are stars or paths. This variant is the first case.
>
> Here a star on `Fin k` is `starGraph c` for a centre `c`. The two trees that may fail to be
> stars are $T_a$ and $T_b$.

```lean
theorem erdos_743.variants.all_but_two_stars (n : ℕ) (T : (k : ℕ) → SimpleGraph (Fin k))
    (hT : ∀ k ∈ Set.Icc 2 n, (T k).IsTree)
    (hstar : ∃ a b : ℕ, ∀ k ∈ Set.Icc 2 n, k ≠ a → k ≠ b → ∃ c : Fin k, T k = starGraph c) :
    IsPacking n (Set.Icc 2 n) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L129).

## `Erdos743.erdos_743.variants.fishburn`

Solved: stated here without proof.

> Fishburn [Fi83b] proved this for $n\leq 9$.

```lean
theorem erdos_743.variants.fishburn (n : ℕ) (hn : n ≤ 9) (T : (k : ℕ) → SimpleGraph (Fin k))
    (hT : ∀ k ∈ Set.Icc 2 n, (T k).IsTree) :
    IsPacking n (Set.Icc 2 n) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L139).

## `Erdos743.erdos_743.variants.bollobas`

Solved: stated here without proof.

> Bollobás [Bo83] proved that the smallest $\lfloor n/\sqrt{2}\rfloor$ many trees can always be
> packed greedily into $K_n$.
>
> The smallest trees are $T_1, \ldots, T_m$ with $m = \lfloor n/\sqrt{2} \rfloor$. The tree $T_1$ is
> a single vertex, so we only pack $T_2, \ldots, T_m$.

```lean
theorem erdos_743.variants.bollobas (n : ℕ) (T : (k : ℕ) → SimpleGraph (Fin k))
    (hT : ∀ k ∈ Set.Icc 2 ⌊(n : ℝ) / Real.sqrt 2⌋₊, (T k).IsTree) :
    IsPacking n (Set.Icc 2 ⌊(n : ℝ) / Real.sqrt 2⌋₊) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L152).

## `Erdos743.erdos_743.variants.bounded_degree`

Solved: stated here without proof.

> Joos, Kim, Kühn, and Osthus [JKKO19] proved that this conjecture holds when the trees have
> bounded maximum degree. That is, for every $d$ there is $N$ such that for all $n \geq N$ the
> following holds. If $T_k$ is a tree with $k$ vertices and maximum degree at most $d$ for
> $2 \leq k \leq n$, then $K_n$ decomposes into $T_2, \ldots, T_n$.
>
> They even allow the first $o(n)$ trees to have arbitrary maximum degree.

```lean
theorem erdos_743.variants.bounded_degree (d : ℕ) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n → ∀ T : (k : ℕ) → SimpleGraph (Fin k),
      (∀ k ∈ Set.Icc 2 n, (T k).IsTree ∧ (T k).maxDegree ≤ d) →
        IsPacking n (Set.Icc 2 n) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 167](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L167).

## `Erdos743.erdos_743.variants.almost_linear_degree`

Solved: stated here without proof.

> Allen, Böttcher, Clemens, Hladký, Piguet, and Taraz [ABCHPT21] proved that this conjecture holds
> when all the trees have maximum degree $\leq c\frac{n}{\log n}$ for some constant $c>0$. That is,
> there is $c > 0$ such that for all sufficiently large $n$ the following holds. If $T_k$ is a tree
> with $k$ vertices and maximum degree at most $cn/\log n$ for $2 \leq k \leq n$, then $K_n$
> decomposes into $T_2, \ldots, T_n$.

```lean
theorem erdos_743.variants.almost_linear_degree :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, ∀ T : (k : ℕ) → SimpleGraph (Fin k),
      (∀ k ∈ Set.Icc 2 n,
        (T k).IsTree ∧ ((T k).maxDegree : ℝ) ≤ c * (n : ℝ) / Real.log (n : ℝ)) →
        IsPacking n (Set.Icc 2 n) T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L182).

## `Erdos743.erdos_743.variants.largest_trees`

Solved: stated here without proof.

> Janzer and Montgomery [JaMo24] have proved that there exists some $c>0$ such that the largest $cn$
> trees can be packed into $K_n$.
>
> We state this for all sufficiently large $n$. The trees are $T_k$ with $n - cn < k \leq n$, and
> we also require $2 \leq k$.

```lean
theorem erdos_743.variants.largest_trees :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, ∀ T : (k : ℕ) → SimpleGraph (Fin k),
      (∀ k : ℕ, 2 ≤ k → k ≤ n → (n : ℝ) - c * n < k → (T k).IsTree) →
        IsPacking n {k : ℕ | 2 ≤ k ∧ k ≤ n ∧ (n : ℝ) - c * n < k} T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/743.lean, line 197](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean#L197).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/743.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/743.lean)
- [erdosproblems.com/743](https://www.erdosproblems.com/743)
