---
declaration: theorem
origin: cited
lean: Erdos209.erdos_209
statement: formalized
---

# Erdős Problem 209

> *References:*
> - [erdosproblems.com/209](https://www.erdosproblems.com/209)
> - [Er84] Erdős, P., *Research problems*. Period. Math. Hungar. (1984), 101-103.
> - [ErPu95b] Erdős, Paul and Purdy, George, *Extremal problems in combinatorial geometry*.
>   Handbook of combinatorics, Vol. 1, 2 (1995), 809-874.
> - [FuPa84] Füredi, Z. and Palásti, I., *Arrangements of lines with a large number of triangles*.
>   Proc. Amer. Math. Soc. (1984), 561-566.
> - [Es16] Escudero, Juan García, *Gallai triangles in configurations of lines in the projective
>   plane*. C. R. Math. Acad. Sci. Paris (2016), 551-554.

*Quoted from [FormalConjectures/ErdosProblems/209.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/209.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/209](https://www.erdosproblems.com/209).

The file states 1 research or textbook statement: 1 solved.

## `Erdos209.erdos_209`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/209/Erdos209.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/209/Erdos209.lean).

> Let $A$ be a finite collection of $d\geq 4$ non-parallel lines in $\mathbb{R}^2$ such that
> there are no points where at least four lines from $A$ meet. Must there exist a 'Gallai
> triangle' (or 'ordinary triangle'): three lines from $A$ which intersect in three points, and
> each of these intersection points only intersects two lines from $A$?
>
> Füredi and Palásti [FuPa84] showed this is false when $d\geq 4$ is not divisible by $9$.
> Escudero [Es16] showed this is false for all $d\geq 4$.

```lean
theorem erdos_209 :
    ¬ ∀ d : ℕ, 4 ≤ d → ∀ A : Finset (AffineSubspace ℝ ℝ²), A.card = d →
      (∀ L ∈ A, IsLine L) →
      ((A : Set (AffineSubspace ℝ ℝ²)).Pairwise fun L₁ L₂ => ¬ L₁ ∥ L₂) →
      (∀ p : ℝ², pointMultiplicity A p ≤ 3) →
      HasGallaiTriangle A
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/209.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/209.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/209.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/209.lean)
- [erdosproblems.com/209](https://www.erdosproblems.com/209)
