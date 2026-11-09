---
declaration: theorem
origin: cited
lean: Erdos654.erdos_654.parts.i, Erdos654.erdos_654.parts.ii, Erdos654.erdos_654.variants.trivial_bound, Erdos654.erdos_654.variants.feng, Erdos654.erdos_654.variants.general_position, Erdos654.erdos_654.variants.general_position_one_sub_eps, Erdos654.erdos_654.variants.erdos_pach
statement: formalized
---

# Erdős Problem 654

> *References:*
> - [erdosproblems.com/654](https://www.erdosproblems.com/654)
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*. Intuitive geometry
>   (Siófok, 1985) (1987), 167-177.
> - [ErPa90] Erdős, P. and Pach, J., *Variations on the theme of repeated distances*.
>   Combinatorica (1990), 261--269.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Fe26] T. Feng et al, *Semi-Autonomous Mathematics Discovery with Gemini: A Case Study on the
>   Erdős Problems*. arXiv:2601.22401 (2026).

*Quoted from [FormalConjectures/ErdosProblems/654.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/654](https://www.erdosproblems.com/654).

The file states 7 research or textbook statements: 4 open, 2 solved and 1 textbook result.

## `Erdos654.erdos_654.parts.i`

Solved: stated here without proof.

> Let $f(n)$ be such that, given any $x_1,\ldots,x_n\in \mathbb{R}^2$ with no four points on a
> circle, there exists some $x_i$ with at least $f(n)$ many distinct distances to the other $x_j$.
> Is it true that $f(n) > (1-o(1))n$?
>
> Erdős asks this in [Er97e]. The answer is no: Aletheia [Fe26] constructed, for every $m \geq 10$,
> a set of $n = 4m$ points with no four on a circle such that every point has fewer than
> $\frac{3}{4}n$ distinct distances to the other points. This gives infinitely many $n$, which is
> enough to refute the statement with $\varepsilon = 1/8$. See `Erdos654.erdos_654.variants.feng`.

```lean
theorem erdos_654.parts.i :
    ¬ ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n → NoFourConcyclic A →
      ∃ x ∈ A, (1 - ε) * (n : ℝ) < (distinctDistancesFrom A x : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L51).

## `Erdos654.erdos_654.parts.ii`

Open: stated without proof.

> Let $f(n)$ be as in `erdos_654.parts.i`. Is it true that $f(n) > (\frac{1}{3}+c)n$ for some
> constant $c>0$ and all large $n$?

```lean
theorem erdos_654.parts.ii :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n → NoFourConcyclic A →
      ∃ x ∈ A, (1 / 3 + c) * (n : ℝ) < (distinctDistancesFrom A x : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L61).

## `Erdos654.erdos_654.variants.trivial_bound`

Textbook result, proved here.

> It is trivial that $f(n) \geq \frac{n-1}{3}$.
>
> In fact every point $x$ has at least $\frac{n-1}{3}$ distinct distances to the other points: a
> circle centred at $x$ contains at most three other points, since four would lie on a common
> circle.

```lean
theorem erdos_654.variants.trivial_bound (A : Finset ℝ²) (hA : NoFourConcyclic A) :
    ∀ x ∈ A, ((#A : ℝ) - 1) / 3 ≤ (distinctDistancesFrom A x : ℝ)
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L74).

## `Erdos654.erdos_654.variants.feng`

Solved: stated here without proof.

> Aletheia [Fe26] showed that for every $m \geq 10$ there is a set of $n = 4m$ points in
> $\mathbb{R}^2$, no four on a circle, such that every point has fewer than $\frac{3}{4}n = 3m$
> distinct distances to the other points.
>
> The construction places $2m$ points on each of two perpendicular lines, so it is not in general
> position. Each point has at most $3m - 1$ distinct distances to the other points.

```lean
theorem erdos_654.variants.feng (m : ℕ) (hm : 10 ≤ m) :
    ∃ A : Finset ℝ², #A = 4 * m ∧ NoFourConcyclic A ∧
      ∀ x ∈ A, distinctDistancesFrom A x < 3 * m
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L107).

## `Erdos654.erdos_654.variants.general_position`

Open: stated without proof.

> Erdős [Er87b] and Erdős and Pach [ErPa90] ask the question of `erdos_654.parts.ii` under the
> additional assumption that no three points are on a line. Let $x_1,\ldots,x_n\in \mathbb{R}^2$ with
> no three points on a line and no four points on a circle. Is there some $x_i$ with at least
> $(\frac{1}{3}+c)n$ distinct distances to the other $x_j$, for some constant $c>0$ and all large
> $n$?

```lean
theorem erdos_654.variants.general_position :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n → InGeneralPosition A →
      ∃ x ∈ A, (1 / 3 + c) * (n : ℝ) < (distinctDistancesFrom A x : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L120).

## `Erdos654.erdos_654.variants.general_position_one_sub_eps`

Open: stated without proof.

> Let $x_1,\ldots,x_n\in \mathbb{R}^2$ with no three points on a line and no four points on a
> circle. Is there some $x_i$ with at least $(1-o(1))n$ distinct distances to the other $x_j$?
>
> This is the general-position analogue of `Erdos654.erdos_654.parts.i`. The remark on
> erdosproblems.com notes that the construction of [Fe26], which has all points on two lines, does
> not settle the version in general position.

```lean
theorem erdos_654.variants.general_position_one_sub_eps :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n → InGeneralPosition A →
      ∃ x ∈ A, (1 - ε) * (n : ℝ) < (distinctDistancesFrom A x : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L134).

## `Erdos654.erdos_654.variants.erdos_pach`

Open: stated without proof.

> Erdős and Pach [ErPa90] suggest that the bound $(1-o(1))n$ holds under the assumption that every
> circle centred at a point $x_i$ contains at most $2$ other points $x_j$. We state this for points
> in general position (no three on a line and no four on a circle [Er87b, p. 167]), the setting in
> which [Er87b] and [ErPa90] ask the weaker question. Without the assumption of no three points on a
> line the statement is false: the sets of [Fe26] satisfy the circle condition.

```lean
theorem erdos_654.variants.erdos_pach :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℝ², #A = n → InGeneralPosition A →
      AtMostTwoPerCircle A → ∃ x ∈ A, (1 - ε) * (n : ℝ) < (distinctDistancesFrom A x : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/654.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean#L152).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/654.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/654.lean)
- [erdosproblems.com/654](https://www.erdosproblems.com/654)
