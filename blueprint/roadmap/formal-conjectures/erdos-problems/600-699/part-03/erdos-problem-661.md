---
declaration: theorem
origin: cited
lean: Erdos661.erdos_661, Erdos661.erdos_661.variants.grid_upper_bound, Erdos661.erdos_661.variants.le_minimalDistinctDistances, Erdos661.erdos_661.variants.little_o_distinct_distances, Erdos661.erdos_661.variants.lenz
statement: formalized
---

# Erdős Problem 661

> *References:*
> - [erdosproblems.com/661](https://www.erdosproblems.com/661)
> - [ErPa90] Erdős, P. and Pach, J., *Variations on the theme of repeated distances*.
>   Combinatorica (1990), 261--269.
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*.
>   Eureka (1992), 44-48.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [Er46] Erdős, Paul, *On sets of distances of $n$ points*. Amer. Math. Monthly 53 (1946),
>   248--250.

*Quoted from [FormalConjectures/ErdosProblems/661.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/661](https://www.erdosproblems.com/661).

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result.

## `Erdos661.erdos_661`

Open: stated without proof.

> Are there, for all large $n$, some points $x_1,\ldots,x_n,y_1,\ldots,y_n\in \mathbb{R}^2$ such that
> the number of distinct distances $d(x_i,y_j)$ is
> $$o\left(\frac{n}{\sqrt{\log n}}\right)?$$
>
> We require all $2n$ points to be distinct; without any distinctness one could take all points
> equal and get a single distance. Writing $F(n)$ for the minimal number of such distances
> (`minimalCrossDistances ℝ² n`), the question asks whether $F(n) = o(n / \sqrt{\log n})$. This is
> equivalent to the existence, for all large $n$, of configurations whose count is at most $g(n)$
> for some fixed $g(n) = o(n / \sqrt{\log n})$, since the infimum is attained.
>
> The source adds that one can also ask this for points in $\mathbb{R}^3$. Taken literally, the
> question is easy there, since a cubic grid of $2n$ points determines only $O(n^{2/3})$ distinct
> distances, so we do not state it.

```lean
theorem erdos_661 :
    (fun n => (minimalCrossDistances ℝ² n : ℝ)) =o[atTop]
      (fun (n : ℕ) => (n : ℝ) / (n : ℝ).log.sqrt)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/661.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean#L74).

## `Erdos661.erdos_661.variants.grid_upper_bound`

Solved: stated here without proof.

> Take $2n$ points of the smallest square grid with at least $2n$ points; by [Er46] they determine
> $O(n / \sqrt{\log n})$ distinct distances. Splitting them into two halves of $n$ points shows
> that $F(n) = O(n / \sqrt{\log n})$. So the question is whether this trivial bound can be
> improved by more than a constant factor.

```lean
theorem erdos_661.variants.grid_upper_bound :
    (fun n => (minimalCrossDistances ℝ² n : ℝ)) =O[atTop]
      (fun (n : ℕ) => (n : ℝ) / (n : ℝ).log.sqrt)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/661.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean#L86).

## `Erdos661.erdos_661.variants.le_minimalDistinctDistances`

Textbook result, proved here.

> Every split of a set of $2n$ points into two halves of $n$ points gives a configuration for
> $F(n)$, and the distances between the halves are among the distances of the whole set. Hence
> $F(n) \leq f(2n)$, where $f(2n)$ is the minimal number of distinct distances determined by $2n$
> points in $\mathbb{R}^2$.

```lean
theorem erdos_661.variants.le_minimalDistinctDistances (n : ℕ) :
    minimalCrossDistances ℝ² n ≤ minimalDistinctDistances ℝ² (2 * n)
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/661.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean#L98).

## `Erdos661.erdos_661.variants.little_o_distinct_distances`

Open: stated without proof.

> Let $F(2n)$ be the minimal number of distinct distances $d(x_i, y_j)$ for $2n$ distinct points
> $x_1,\ldots,x_n,y_1,\ldots,y_n\in \mathbb{R}^2$, and $f(2n)$ the minimal number of distinct
> distances determined by any $2n$ points in $\mathbb{R}^2$. Is $F = o(f)$?
>
> Here $F(2n)$ of erdosproblems.com is `minimalCrossDistances ℝ² n` (indexed by $n$ points on each
> side) and $f(2n)$ is `minimalDistinctDistances ℝ² (2 * n)`. See also Erdős Problem 89.

```lean
theorem erdos_661.variants.little_o_distinct_distances :
    (fun n => (minimalCrossDistances ℝ² n : ℝ)) =o[atTop]
      (fun n => (minimalDistinctDistances ℝ² (2 * n) : ℝ))
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/661.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean#L125).

## `Erdos661.erdos_661.variants.lenz`

Solved: stated here without proof.

> In $\mathbb{R}^4$ Lenz observed (as stated on erdosproblems.com/661) that for every $n$ there are
> $2n$ distinct points $x_1,\ldots,x_n,y_1,\ldots,y_n\in \mathbb{R}^4$ with $d(x_i,y_j)=1$ for all
> $i,j$: take the $x_i$ on the circle of radius $1/\sqrt{2}$ about the origin in the plane of the
> first two coordinates, and the $y_j$ on the circle of radius $1/\sqrt{2}$ about the origin in the
> plane of the last two coordinates.

```lean
theorem erdos_661.variants.lenz (n : ℕ) :
    ∃ A B : Finset (EuclideanSpace ℝ (Fin 4)), #A = n ∧ #B = n ∧ Disjoint A B ∧
      ∀ x ∈ A, ∀ y ∈ B, dist x y = 1
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/661.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/661.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/661.lean)
- [erdosproblems.com/661](https://www.erdosproblems.com/661)
