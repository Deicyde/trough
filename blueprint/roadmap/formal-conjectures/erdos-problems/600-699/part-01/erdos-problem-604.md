---
declaration: theorem
origin: cited
lean: Erdos604.erdos_604, Erdos604.erdos_604.variants.sqrt_log, Erdos604.erdos_604.variants.grid_upper_bound, Erdos604.erdos_604.variants.katz_tardos, Erdos604.erdos_604.variants.average
statement: formalized
---

# Erdős Problem 604

> *References:*
> - [erdosproblems.com/604](https://www.erdosproblems.com/604)
> - [OAI26] OpenAI, [*The weak pinned planar distance theorem*](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf) (2026).
> - [Er46] Erdős, Paul, *On sets of distances of $n$ points*. Amer. Math. Monthly (1946), 248--250.
> - [Er57] Erdős, Paul, *Some unsolved problems*. Michigan Math. J. (1957), 291-300.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat. Pura
>   Appl. (4) (1975), 99-108.
> - [Er83c] Erdős, Paul, *Combinatorial problems in geometry*. Math. Chronicle (1983), 35-54.
> - [Er85] Erdős, P., *Problems and results in combinatorial geometry*. Discrete geometry and
>   convexity (New York, 1982) (1985), 1-11.
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*. Intuitive geometry
>   (Siófok, 1985) (1987), 167-177.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [KaTa04] Katz, Nets Hawk and Tardos, Gábor, *A new entropy inequality for the Erdős distance
>   problem*. Towards a theory of geometric graphs (2004), 119-126.

*Quoted from [FormalConjectures/ErdosProblems/604.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/604](https://www.erdosproblems.com/604).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos604.erdos_604`

Solved: stated here; a Lean proof is at [https://github.com/MendozaLab/erdos-experiments/blob/09f72c57ed2d98906b9cf03bff2091f6fe73807f/proofs/erdos604/Erdos604Proof/ExternalApplication.lean#L17](https://github.com/MendozaLab/erdos-experiments/blob/09f72c57ed2d98906b9cf03bff2091f6fe73807f/proofs/erdos604/Erdos604Proof/ExternalApplication.lean#L17).

> Given $n$ distinct points $A\subset\mathbb{R}^2$, must there be a point $x\in A$ such that
> $$\#\{ d(x,y) : y \in A\} \gg n^{1-o(1)}?$$
>
> This is the pinned distance problem, a stronger form of Problem 89. Here $n^{1-o(1)}$ means: for
> every $\varepsilon > 0$ and all large $n$, the bound is at least $n^{1-\varepsilon}$. We do not
> count the distance $d(x, x) = 0$; this changes the count by one.
>
> This weak formulation was proved by OpenAI [OAI26].

```lean
theorem erdos_604 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ (1 - ε) ≤ (pinnedDistinctDistances n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/604.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean#L82).

## `Erdos604.erdos_604.variants.sqrt_log`

Open: stated without proof.

> Given $n$ distinct points $A\subset\mathbb{R}^2$, must there be a point $x\in A$ such that
> $$\#\{ d(x,y) : y \in A\} \gg \frac{n}{\sqrt{\log n}}?$$

```lean
theorem erdos_604.variants.sqrt_log :
    (fun n : ℕ => (n : ℝ) / (n : ℝ).log.sqrt) =O[atTop]
      (fun n => (pinnedDistinctDistances n : ℝ))
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/604.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean#L92).

## `Erdos604.erdos_604.variants.grid_upper_bound`

Solved: stated here without proof.

> The integer grid shows that $\frac{n}{\sqrt{\log n}}$ would be best possible: there are sets of
> $n$ points in $\mathbb{R}^2$ in which every point has $O(\frac{n}{\sqrt{\log n}})$ distinct
> distances to the other points. This follows from the bound of Erdős [Er46] on the total number of
> distinct distances in the grid (see Erdős Problem 89), since the number of distances from one point
> is at most the total number of distances. For $n$ that is not a square, take $n$ points of the
> smallest square grid with at least $n$ points.

```lean
theorem erdos_604.variants.grid_upper_bound :
    (fun n => (pinnedDistinctDistances n : ℝ)) =O[atTop]
      (fun n : ℕ => (n : ℝ) / (n : ℝ).log.sqrt)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/604.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean#L106).

## `Erdos604.erdos_604.variants.katz_tardos`

Solved: stated here without proof.

> Katz and Tardos [KaTa04] proved that some point of $A$ has $\gg n^{c-o(1)}$ distinct distances to
> the other points of $A$, where
> $$c=\frac{48-14e}{55-16e}=0.864137\cdots.$$

```lean
theorem erdos_604.variants.katz_tardos :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ ((48 - 14 * Real.exp 1) / (55 - 16 * Real.exp 1) - ε) ≤
        (pinnedDistinctDistances n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/604.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean#L117).

## `Erdos604.erdos_604.variants.average`

Open: stated without proof.

> Let $d(x)$ be the number of distinct distances from $x$ to the other points of $A$. Erdős [Er75f]
> conjectured that
> $$\sum_{x\in A}d(x) \gg \frac{n^2}{\sqrt{\log n}}$$
> for every set $A\subset\mathbb{R}^2$ of $n$ points.
>
> The sum is at most $n$ times the largest $d(x)$, so this conjecture implies a positive answer to
> `Erdos604.erdos_604.variants.sqrt_log`.

```lean
theorem erdos_604.variants.average :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n →
      C * (n : ℝ) ^ 2 / (n : ℝ).log.sqrt ≤ ((∑ x ∈ A, distinctDistancesFrom A x : ℕ) : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/604.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean#L133).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/604.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/604.lean)
- [erdosproblems.com/604](https://www.erdosproblems.com/604)
