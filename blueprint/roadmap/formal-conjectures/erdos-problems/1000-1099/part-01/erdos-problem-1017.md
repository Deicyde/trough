---
declaration: theorem
origin: cited
lean: Erdos1017.erdos_1017.lower_bound, Erdos1017.erdos_1017.upper_bound
statement: formalized
---

# Erdős Problem 1017

> *References:*
> - [erdosproblems.com/1017](https://www.erdosproblems.com/1017)
> - [EGP66] Erdős, Paul and Goodman, A. W. and Pósa, Lajos,
>   *The representation of a graph by set intersections*. Canadian J. Math. (1966), 106–112.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97–109.
> - [GyKe17] Győri, Ervin and Keszegh, Balázs,
>   *On the number of edge-disjoint triangles in $K_4$-free graphs*.
>   Combinatorica (2017), 1113–1124.
> - [Lo68] Lovász, L., *On covering of graphs*.
>   Theory of Graphs (Proc. Colloq., Tihany, 1966) (1968), 231–236.

*Quoted from [FormalConjectures/ErdosProblems/1017.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1017.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1017](https://www.erdosproblems.com/1017).

The file states 2 research or textbook statements: 2 open. It also has 2 test statements and 3 API statements, counted here but not shown.

## `Erdos1017.erdos_1017.lower_bound`

Open: stated without proof.

> Let $f(n,k)$ be such that every graph on $n$ vertices and $k$ edges can be partitioned
> into at most $f(n,k)$ edge-disjoint complete graphs. Estimate $f(n,k)$ for $k>n^2/4$.

```lean
theorem erdos_1017.lower_bound :
    ∀ n k : ℕ, k ≤ n.choose 2 → n * n < 4 * k →
      erdos_1017.lower_bound.answer n k ≤ f n k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1017.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1017.lean#L108).

## `Erdos1017.erdos_1017.upper_bound`

Open: stated without proof.

> Estimate an upper bound for $f(n,k)$, the worst-case number of complete subgraphs
> needed to partition the edges of an $n$-vertex, $k$-edge graph, for
> $n^2/4 < k \le \binom{n}{2}$.

```lean
theorem erdos_1017.upper_bound :
    ∀ n k : ℕ, k ≤ n.choose 2 → n * n < 4 * k →
      f n k ≤ erdos_1017.upper_bound.answer n k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1017.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1017.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1017.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1017.lean)
- [erdosproblems.com/1017](https://www.erdosproblems.com/1017)
