---
declaration: theorem
origin: cited
lean: Erdos1086.erdos_1086, Erdos1086.erdos_1086.variants.erdos_purdy_lower, Erdos1086.erdos_1086.variants.raz_sharir
statement: formalized
---

# Erdős Problem 1086

> *References:*
> - [erdosproblems.com/1086](https://www.erdosproblems.com/1086)
> - [ErPu71] Erdős, P. and Purdy, G., *Some extremal problems in geometry*. J. Combinatorial Theory
>   Ser. A 10 (1971), 246-252.
> - [RaSh17] Raz, O. E. and Sharir, M., *The number of unit-area triangles in the plane: theme and
>   variations*. Combinatorica 37 (2017), 1221-1240.
>   [arXiv:1501.00379](https://arxiv.org/abs/1501.00379)

*Quoted from [FormalConjectures/ErdosProblems/1086.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1086.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1086](https://www.erdosproblems.com/1086).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1086.erdos_1086`

Open: stated without proof.

> Let $g(n)$ be minimal such that any set of $n$ points in $\mathbb{R}^2$ contains the vertices of
> at most $g(n)$ many triangles with the same area. Estimate $g(n)$.
>
> Only triangles of positive area are counted.

```lean
theorem erdos_1086 : (fun n : ℕ ↦ (g n : ℝ)) =Θ[atTop] erdos_1086.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1086.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1086.lean#L78).

## `Erdos1086.erdos_1086.variants.erdos_purdy_lower`

Solved: stated here without proof.

> Erdős and Purdy [ErPu71] proved
> $$n^2\log\log n \ll g(n) \ll n^{5/2}.$$
>
> This is the lower bound.

```lean
theorem erdos_1086.variants.erdos_purdy_lower :
    (fun n : ℕ ↦ (n : ℝ) ^ 2 * Real.log (Real.log n)) =O[atTop] fun n : ℕ ↦ (g n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1086.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1086.lean#L88).

## `Erdos1086.erdos_1086.variants.raz_sharir`

Solved: stated here without proof.

> The upper bound of Erdős and Purdy [ErPu71] has been improved a number of times. The best known
> bound is $g(n) \ll n^{20/9}$ by Raz and Sharir [RaSh17].

```lean
theorem erdos_1086.variants.raz_sharir :
    (fun n : ℕ ↦ (g n : ℝ)) =O[atTop] fun n : ℕ ↦ (n : ℝ) ^ (20 / 9 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1086.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1086.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1086.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1086.lean)
- [erdosproblems.com/1086](https://www.erdosproblems.com/1086)
