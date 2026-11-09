---
declaration: theorem
origin: cited
lean: Erdos506.erdos_506, Erdos506.erdos_506.variants.large_n, Erdos506.erdos_506.variants.small_n, Erdos506.erdos_506.variants.segre_n_eq_eight
statement: formalized
---

# Erdős Problem 506

> *References:*
> - [erdosproblems.com/506](https://www.erdosproblems.com/506)
> - [El67] Elliott, P. D. T. A., *On the number of circles determined by $n$ points*, Acta Math.
>   Acad. Sci. Hungar. (1967), 181–188.
> - [BaBa94] Bálintová, A. and Bálint, V., *On the number of circles determined by $n$ points in the
>   Euclidean plane*, Acta Math. Hungar. (1994), 283–289.
> - [PuSm] Purdy and Smith. No reference found.

*Quoted from [FormalConjectures/ErdosProblems/506.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/506](https://www.erdosproblems.com/506).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos506.erdos_506`

Open: stated without proof.

> What is the minimum number of circles determined by any $n$ points in $\mathbb{R}^2$, not all on a
> circle?
>
> There is clearly some non-degeneracy condition intended here - probably either that not all the
> points are on a line, or the stronger condition that no three points are on a line.
>
> The answer is known for $n > 393$ (see `erdos_506.variants.large_n`) but the problem appears to
> remain open for small $n$ (see `erdos_506.variants.small_n`).

```lean
theorem erdos_506 (n : ℕ) (hn : 4 ≤ n) :
    IsLeast { k : ℕ | ∃ P : Finset ℝ²,
        P.card = n ∧ ¬ Collinear ℝ (P : Set ℝ²) ∧ ¬ Cospherical (P : Set ℝ²) ∧
        numCircles (P : Set ℝ²) = k }
      erdos_506.answer
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/506.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean#L66).

## `Erdos506.erdos_506.variants.large_n`

Solved: stated here without proof.

> For $n > 393$ the answer is $\binom{n-1}{2} + 1 - \left\lfloor \frac{n-1}{2} \right\rfloor$
> (Elliott [El67], with the correction of Purdy and Smith [PuSm], also reported in [BaBa94]): this is
> both a lower bound for every such configuration and is attained, e.g. by a circle with $n - 1$
> points together with a single point off the circle.

```lean
theorem erdos_506.variants.large_n (n : ℕ) (hn : 393 < n) :
    IsLeast { k : ℕ | ∃ P : Finset ℝ²,
        P.card = n ∧ ¬ Collinear ℝ (P : Set ℝ²) ∧ ¬ Cospherical (P : Set ℝ²) ∧
        numCircles (P : Set ℝ²) = k }
      (erdos_506.variants.large_n.answer n)
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/506.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean#L82).

## `Erdos506.erdos_506.variants.small_n`

Open: stated without proof.

> The problem appears to remain open for small $n$: Elliott's answer is established only for
> $n > 393$, so the minimum number of circles determined by $n$ points, not all on a line and not all
> on a circle, is unknown for $n \le 393$.

```lean
theorem erdos_506.variants.small_n (n : ℕ) (hn : 4 ≤ n) (hn' : n ≤ 393) :
    IsLeast { k : ℕ | ∃ P : Finset ℝ²,
        P.card = n ∧ ¬ Collinear ℝ (P : Set ℝ²) ∧ ¬ Cospherical (P : Set ℝ²) ∧
        numCircles (P : Set ℝ²) = k }
      erdos_506.variants.small_n.answer
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/506.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean#L97).

## `Erdos506.erdos_506.variants.segre_n_eq_eight`

Solved: stated here without proof.

> Segre's observation: the lower bound $\binom{n-1}{2}$ (without the correction of [PuSm]) is
> already false for $n = 8$, as witnessed by the projection of a cube onto a plane. Hence the minimum
> number of circles determined by $8$ such points is strictly less than $\binom{7}{2} = 21$.

```lean
theorem erdos_506.variants.segre_n_eq_eight :
    ∃ P : Finset ℝ²,
      P.card = 8 ∧ ¬ Collinear ℝ (P : Set ℝ²) ∧ ¬ Cospherical (P : Set ℝ²) ∧
      numCircles (P : Set ℝ²) < (8 - 1).choose 2
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/506.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/506.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/506.lean)
- [erdosproblems.com/506](https://www.erdosproblems.com/506)
