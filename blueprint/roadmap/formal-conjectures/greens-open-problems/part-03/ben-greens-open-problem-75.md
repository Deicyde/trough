---
declaration: theorem
origin: cited
lean: Green75.green_75, Green75.green_75.variants.exists_constant, Green75.green_75.variants.pinchasi, Green75.green_75.variants.alon
statement: formalized
---

# Ben Green's Open Problem 75

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.75)
> - [CL25] Conlon, D. and Lim, J., *Everywhere unbalanced configurations*. Adv. Math. 480 (2025),
>   Paper No. 110445. [arXiv:2308.02466](https://arxiv.org/abs/2308.02466)
> - [Pi03] Pinchasi, R., *Lines with many points on both sides*. Discrete Comput. Geom. 30 (2003),
>   415-435. [doi:10.1007/s00454-003-2826-8](https://doi.org/10.1007/s00454-003-2826-8)

*Quoted from [FormalConjectures/GreensOpenProblems/75.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Green75.green_75`

Open: stated without proof.

> Let $X \subset \mathbb{R}^2$ be a set of $n$ points. Does there exist a line $\ell$ through at
> least two points of $X$ such that the numbers of points on either side of $\ell$ differ by at
> most $100$?
>
> This is a form of the Kupitz-Perles conjecture [Gr24]. We take $n \geq 2$, since a line through
> two points of $X$ needs two points. If all points of $X$ are collinear, the line through them has
> no points on either side.

```lean
theorem green_75 :
    ∀ X : Finset (ℝ × ℝ), 2 ≤ #X → ∃ p ∈ X, ∃ q ∈ X, p ≠ q ∧ imbalance X p q ≤ 100
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/75.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean#L71).

## `Green75.green_75.variants.exists_constant`

Open: stated without proof.

> Is there a constant $C$ such that every finite set $X \subset \mathbb{R}^2$ with at least two
> points has a line through two points of $X$ whose sides differ by at most $C$? This is the
> question of Kupitz in the form of [CL25, Section 1], where the constant is not specified.
>
> `green_75` implies it with $C = 100$.

```lean
theorem green_75.variants.exists_constant :
    ∃ C : ℕ, ∀ X : Finset (ℝ × ℝ), 2 ≤ #X →
      ∃ p ∈ X, ∃ q ∈ X, p ≠ q ∧ imbalance X p q ≤ C
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/75.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean#L83).

## `Green75.green_75.variants.pinchasi`

Solved: stated here without proof.

> Pinchasi [Pi03] proved that the answer to `green_75` is yes if $100$ is replaced by
> $C \log \log n$ for an absolute constant $C$, where $n = |X|$ [Gr24]. This is the best known bound.
> [CL25, Theorem 1.1] states Pinchasi's theorem for generalised configurations (points with
> pseudolines); sets of points with lines are a special case. The hypothesis $n \geq 3$ ensures
> that $\log \log n > 0$.

```lean
theorem green_75.variants.pinchasi :
    ∃ C : ℝ, ∀ X : Finset (ℝ × ℝ), 3 ≤ #X → ∃ p ∈ X, ∃ q ∈ X, p ≠ q ∧
      (imbalance X p q : ℝ) ≤ C * Real.log (Real.log #X)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/75.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean#L96).

## `Green75.green_75.variants.alon`

Solved: stated here without proof.

> Kupitz conjectured that one can take the difference to be at most $1$ [CL25, Section 1]. Alon
> showed that this is false: there are finite point sets for which, for every line through two of
> its points, the numbers of points on the two sides differ by at least $2$ [CL25, Section 1].
> [Gr24] phrases this as: the answer to `green_75` is no if $100$ is replaced by $2$. Since the
> sets in [CL25] have differences of at least $2$, they show that $100$ cannot be replaced by $1$.
> We state the form given in [CL25].

```lean
theorem green_75.variants.alon :
    ∃ X : Finset (ℝ × ℝ), 2 ≤ #X ∧ ∀ p ∈ X, ∀ q ∈ X, p ≠ q → 2 ≤ imbalance X p q
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/75.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/75.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/75.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.75)
