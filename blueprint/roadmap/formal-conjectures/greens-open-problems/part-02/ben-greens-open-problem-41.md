---
declaration: theorem
origin: cited
lean: Green41.minCopies_set_nonempty, Green41.green_41, Green41.green_41.variants.double_exponential_bound, Green41.green_41.variants.polynomial_bound, Green41.green_41.variants.kravitz_leng
statement: formalized
---

# Ben Green's Open Problem 41

> *References*
> - [Gr24] [Ben Green's Open Problem 41](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.41)
> - [Ma15] Manners, Freddie. "A solution to the pyjama problem." Inventiones mathematicae 202.1 (2015): 239-270.
> - [KrLe25] Kravitz, Noah, and James Leng. "Quantitative pyjama." arXiv preprint arXiv:2510.17744 (2025).

*Quoted from [FormalConjectures/GreensOpenProblems/41.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Green41.minCopies_set_nonempty`

Solved: stated here without proof.

> [Ma15] proved that for any $\varepsilon > 0$, finitely many rotations of the pyjama set of width
> $\varepsilon$ cover the plane. This implies that the set we are taking the infimum over in `minCopies`
> is non-empty.

```lean
theorem minCopies_set_nonempty (ε : ℝ) (hε : 0 < ε) :
    (coveringCopies ε).Nonempty
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/41.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean#L58).

## `Green41.green_41`

Open: stated without proof.

> How many rotated (about the origin) copies of the 'pyjama set'
> $\\{(x, y) \in \mathbb{R}^2 : \text{dist}(x, \mathbb{Z}) \leq \varepsilon\\}$ are needed to cover
> $\mathbb{R}^2$?
>
> That is, determine the minimal number of rotations as a function of $\varepsilon > 0$.

```lean
theorem green_41 : ∀ ε > 0, minCopies ε = green_41.answer ε
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/41.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean#L72).

## `Green41.green_41.variants.double_exponential_bound`

Open: stated without proof.

> Can the triple-exponential bound of [KrLe25] be improved by one exponential? That is, do
> $\exp\exp(\varepsilon^{-C})$ rotations suffice for some $C$ and all sufficiently small
> $\varepsilon > 0$? [KrLe25, Section 8.1] discusses where the three exponentials are lost and
> which of them one might hope to save.

```lean
theorem green_41.variants.double_exponential_bound :
    ∃ C : ℝ, ∃ ε₀ > 0, ∀ ε ∈ Ioc 0 ε₀, (minCopies ε : ℝ) ≤ Real.exp (Real.exp (ε ^ (-C)))
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/41.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean#L82).

## `Green41.green_41.variants.polynomial_bound`

Open: stated without proof.

> Is $\varepsilon^{-C}$ rotations enough?

```lean
theorem green_41.variants.polynomial_bound :
    ∃ C : ℝ, ∃ ε₀ > 0, ∀ ε ∈ Ioc 0 ε₀, (minCopies ε : ℝ) ≤ ε ^ (-C)
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/41.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean#L88).

## `Green41.green_41.variants.kravitz_leng`

Solved: stated here without proof.

> [KrLe25] have established the first quantitative bound, showing via an analysis of [Ma15]'s method
> that $\exp\exp\exp(\varepsilon^{-C})$ rotations suffice.

```lean
theorem green_41.variants.kravitz_leng :
    ∃ C : ℝ, ∃ ε₀ > 0, ∀ ε ∈ Ioc 0 ε₀, (minCopies ε : ℝ) ≤ Real.exp (Real.exp (Real.exp (ε ^ (-C))))
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/41.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/41.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/41.lean)
- [Ben Green's Open Problem 41](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.41)
