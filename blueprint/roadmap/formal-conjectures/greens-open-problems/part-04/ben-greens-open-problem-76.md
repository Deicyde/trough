---
declaration: theorem
origin: cited
lean: Green76.green_76, Green76.green_76.variants.exists_constant, Green76.green_76.variants.weak_net, Green76.green_76.variants.subset, Green76.green_76.variants.subset_log_log
statement: formalized
---

# Ben Green's Open Problem 76

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.76)
> - [AES10] Aronov, Boris, Esther Ezra, and Micha Sharir. "Small-size $\varepsilon$-nets for
>   axis-parallel rectangles and boxes." SIAM Journal on Computing 39.7 (2010): 3248-3282.
>   [doi:10.1137/090762968](https://doi.org/10.1137/090762968)
> - [PT11] Pach, János. "Boxes and the art of $\varepsilon$-net maintenance." Invited problems,
>   2nd Emléktábla Workshop (2011), Problem 5 (Pach and Tardos).
>   [PDF](https://www.renyi.hu/~emlektab/emlektabla2withresults.pdf)
> - [PT13] Pach, János, and Gábor Tardos. "Tight lower bounds for the size of epsilon-nets."
>   Journal of the American Mathematical Society 26.3 (2013): 645-658.
>   [doi:10.1090/S0894-0347-2012-00759-0](https://doi.org/10.1090/S0894-0347-2012-00759-0),
>   [arXiv:1012.1240](https://arxiv.org/abs/1012.1240)

*Quoted from [FormalConjectures/GreensOpenProblems/76.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 solved. It also has 1 test statement and 3 API statements, counted here but not shown.

## `Green76.green_76`

Open: stated without proof.

> Let $A$ be a set of $n$ points in the plane. Can one select a set $A'$ of $n/2$ points, with the
> property that any axis-parallel rectangle containing $1000$ points of $A$ contains at least one
> point of $A'$?
>
> We read "a set of $n/2$ points" as at most $\lfloor n/2 \rfloor$ points, and "containing $1000$
> points" as containing at least $1000$ points. The points of $A'$ need not lie in $A$. If
> $A' \subseteq A$ is required, then the answer is no; see `green_76.variants.subset`.

```lean
theorem green_76 :
    ∀ A : Finset (ℝ × ℝ), ∃ A', #A' ≤ #A / 2 ∧ HitsRichRectangles 1000 A A'
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/76.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean#L64).

## `Green76.green_76.variants.exists_constant`

Open: stated without proof.

> Is there a constant $k$ such that the answer to `green_76` is yes with $1000$ replaced by $k$?
> [PT11, Problem 5] asks this in an equivalent form, with $k = C + 1$: is there a constant $C$ such
> that every set of $n$ points in the plane has a set $Y$ of $n/2$ points such that every
> axis-parallel rectangle disjoint from $Y$ contains at most $C$ of the $n$ points?
>
> Each of `green_76` and `green_76.variants.weak_net` implies this.

```lean
theorem green_76.variants.exists_constant :
    ∃ k : ℕ, ∀ A : Finset (ℝ × ℝ), ∃ A', #A' ≤ #A / 2 ∧ HitsRichRectangles k A A'
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/76.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean#L77).

## `Green76.green_76.variants.weak_net`

Open: stated without proof.

> Do weak $\varepsilon$-nets of size $O(1/\varepsilon)$ exist for axis-parallel rectangles in the
> plane? [Gr24] believes that `green_76` is an instance of this question, which he states for
> axis-parallel boxes. With $k = \varepsilon n$: is there a constant $C$ such that, for every
> $k \ge 1$, every set $A$ of $n$ points in the plane has a set $A'$ of at most $Cn/k$ points that
> meets every axis-parallel rectangle containing at least $k$ points of $A$?
>
> A positive answer implies `green_76.variants.exists_constant`, and it implies `green_76` if the
> constant $C$ is at most $500$. [AES10, Theorem 2.2] gives such sets of size
> $O(\varepsilon^{-1} \log \log \varepsilon^{-1})$, even with $A' \subseteq A$. When
> $A' \subseteq A$ is required, this size is optimal [PT13, Theorem 4].

```lean
theorem green_76.variants.weak_net :
    ∃ C : ℝ, ∀ k : ℕ, 0 < k → ∀ A : Finset (ℝ × ℝ),
      ∃ A', #A' ≤ C * #A / k ∧ HitsRichRectangles k A A'
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/76.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean#L94).

## `Green76.green_76.variants.subset`

Solved: stated here without proof.

> If $A'$ is required to be a subset of $A$, then the answer to `green_76` is no, even with $1000$
> replaced by any constant. [Gr24] attributes this remark to Alon. It follows from
> [PT13, Lemma 4.1], which [Gr24] cites as Lemma 3.1, its number in the arXiv version.

```lean
theorem green_76.variants.subset :
    ¬ ∃ k : ℕ, ∀ A : Finset (ℝ × ℝ), ∃ A' ⊆ A, #A' ≤ #A / 2 ∧ HitsRichRectangles k A A'
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/76.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean#L105).

## `Green76.green_76.variants.subset_log_log`

Solved: stated here without proof.

> The answer to `green_76` is yes if $1000$ is replaced by $C \log \log n$ [Gr24]. This follows
> from [AES10, Theorem 2.2], which gives $\varepsilon$-nets of size
> $O(\varepsilon^{-1} \log \log \varepsilon^{-1})$ for axis-parallel rectangles. These nets are
> subsets of $A$. The hypothesis $n \ge 3$ ensures that $\log \log n > 0$.

```lean
theorem green_76.variants.subset_log_log :
    ∃ C : ℝ, ∀ A : Finset (ℝ × ℝ), 3 ≤ #A → ∃ A' ⊆ A,
      #A' ≤ #A / 2 ∧ HitsRichRectangles ⌈C * Real.log (Real.log #A)⌉₊ A A'
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/76.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/76.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/76.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.76)
