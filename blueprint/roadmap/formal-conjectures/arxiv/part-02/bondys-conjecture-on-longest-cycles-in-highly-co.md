---
declaration: theorem
origin: cited
lean: Arxiv.«2606.03696».bondy_conjecture, Arxiv.«2606.03696».bondy_conjecture.variants.one, Arxiv.«2606.03696».bondy_conjecture.variants.two, Arxiv.«2606.03696».bondy_conjecture.variants.three, Arxiv.«2606.03696».bondy_conjecture.variants.large_explicit, Arxiv.«2606.03696».bondy_conjecture.variants.large
statement: formalized
---

# Bondy's conjecture on longest cycles in highly connected graphs

> *References:*
> - [arxiv/2606.03696](https://arxiv.org/abs/2606.03696)
>   **Longest cycles and Dirac-type results in highly connected graphs**
>   by *Jie Ma, Bo Ning, Ziyuan Zhao*, where this is Conjecture 1.
> - [Bo80] Bondy, J. A., Longest paths and cycles in graphs of high degree. (1980).
>
> Take a `k`-connected graph with a large minimum degree. Bondy says that the graph outside any
> longest cycle holds no long path.
>
> The case `k = 1` is Dirac's theorem and the case `k = 2` is the theorem of Nash-Williams. The
> case `k = 3` is proved. The cases `k ≥ 4` are open.

*Quoted from [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved.

## `Arxiv.«2606.03696».bondy_conjecture`

Open: stated without proof.

> **Conjecture 1 (Bondy, 1980).** Let $k \geq 1$ and let $G$ be a $k$-connected graph on $n$
> vertices. If $\delta(G) \geq \frac{n + k(k-1)}{k+1}$, then for every longest cycle $C$ of $G$,
> every path in $G - V(C)$ has at most $k-1$ vertices.
>
> The bound on the number of vertices of a path is written as `+ 1 ≤ k` rather than `≤ k - 1`,
> because subtraction on `ℕ` is truncated. The two forms agree for `k ≥ 1`.
>
> A longest cycle is a cycle whose length is the circumference of `G`.

```lean
theorem bondy_conjecture :
    ∀ (k : ℕ), 1 ≤ k → ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], IsKConnected G k →
      ((Fintype.card V : ℝ) + k * (k - 1)) / (k + 1) ≤ G.minDegree →
      ∀ (a : V) (C : G.Walk a a), C.IsCycle → C.length = G.circumference →
      ∀ (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v), P.IsPath →
        P.support.length + 1 ≤ k
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L60).

## `Arxiv.«2606.03696».bondy_conjecture.variants.one`

Solved: stated here without proof.

> The case $k = 1$ is Dirac's theorem. The condition reads $\delta(G) \geq n/2$, and no path in
> $G - V(C)$ can hold a vertex, so a longest cycle covers every vertex.

```lean
theorem bondy_conjecture.variants.one {G : SimpleGraph V} [DecidableRel G.Adj]
    (hG : IsKConnected G 1) (hd : ((Fintype.card V : ℝ)) / 2 ≤ G.minDegree)
    {a : V} (C : G.Walk a a) (hC : C.IsCycle) (hlong : C.length = G.circumference)
    (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v) (hP : P.IsPath) :
    P.support.length + 1 ≤ 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L74).

## `Arxiv.«2606.03696».bondy_conjecture.variants.two`

Solved: stated here without proof.

> The case $k = 2$ is the theorem of Nash-Williams.

```lean
theorem bondy_conjecture.variants.two {G : SimpleGraph V} [DecidableRel G.Adj]
    (hG : IsKConnected G 2) (hd : ((Fintype.card V : ℝ) + 2) / 3 ≤ G.minDegree)
    {a : V} (C : G.Walk a a) (hC : C.IsCycle) (hlong : C.length = G.circumference)
    (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v) (hP : P.IsPath) :
    P.support.length + 1 ≤ 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L85).

## `Arxiv.«2606.03696».bondy_conjecture.variants.three`

Solved: stated here without proof.

> The case $k = 3$ is proved.

```lean
theorem bondy_conjecture.variants.three {G : SimpleGraph V} [DecidableRel G.Adj]
    (hG : IsKConnected G 3) (hd : ((Fintype.card V : ℝ) + 6) / 4 ≤ G.minDegree)
    {a : V} (C : G.Walk a a) (hC : C.IsCycle) (hlong : C.length = G.circumference)
    (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v) (hP : P.IsPath) :
    P.support.length + 1 ≤ 3
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L96).

## `Arxiv.«2606.03696».bondy_conjecture.variants.large_explicit`

Solved: stated here without proof.

> **Theorem 1.1 (Ma-Ning-Zhao, 2026), explicit threshold.** Bondy's conjecture holds when
> $n \geq 5k^2 + 7k$. This value of $n_k$ is given after Theorem 1.1 and in its reduction
> from Theorem 2.2.

```lean
theorem bondy_conjecture.variants.large_explicit :
    ∀ k : ℕ, 1 ≤ k → ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj],
      5 * k ^ 2 + 7 * k ≤ Fintype.card V → IsKConnected G k →
      ((Fintype.card V : ℝ) + k * (k - 1)) / (k + 1) ≤ G.minDegree →
      ∀ (a : V) (C : G.Walk a a), C.IsCycle → C.length = G.circumference →
      ∀ (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v), P.IsPath →
        P.support.length + 1 ≤ k
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L109).

## `Arxiv.«2606.03696».bondy_conjecture.variants.large`

Proved here.

> **Theorem 1.1 (Ma-Ning-Zhao, 2026).** The conjecture holds for every graph with enough
> vertices. The full conjecture, for graphs of every size, stays open.

```lean
theorem bondy_conjecture.variants.large :
    ∀ k : ℕ, 1 ≤ k → ∃ N : ℕ, ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], N ≤ Fintype.card V → IsKConnected G k →
      ((Fintype.card V : ℝ) + k * (k - 1)) / (k + 1) ≤ G.minDegree →
      ∀ (a : V) (C : G.Walk a a), C.IsCycle → C.length = G.circumference →
      ∀ (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v), P.IsPath →
        P.support.length + 1 ≤ k
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2606.03696/BondyLongestCycles.lean)
- [arxiv/2606.03696](https://arxiv.org/abs/2606.03696)
