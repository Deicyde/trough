---
declaration: theorem
origin: cited
lean: Green74.green_74, Green74.green_74.variants.order, Green74.green_74.variants.large
statement: formalized
---

# Ben Green's Open Problem 74

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.74)

*Quoted from [FormalConjectures/GreensOpenProblems/74.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/74.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 1 API statement, counted here but not shown.

## `Green74.green_74`

Open: stated without proof.

> What is the largest subset of $[N]^d$ with no $5$ points on a $2$-plane?
>
> Here $[N] = \{1, \dots, N\}$ as in [Gr24], and a $2$-plane is a $2$-dimensional affine subspace of
> $\mathbb{R}^d$. We ask for the size $f(d, N)$ of a largest such subset (`maxNoFiveCoplanar`) as a
> function of $d$ and $N$; for its order of growth in $N$ see `green_74.variants.order`. For
> $d \le 2$ any $5$ points are coplanar, so then $f(d, N) \le 4$.

```lean
theorem green_74 : ∀ d N : ℕ, maxNoFiveCoplanar d N = green_74.answer d N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/74.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/74.lean#L73).

## `Green74.green_74.variants.order`

Open: stated without proof.

> For fixed $d$, what is the order of magnitude of $f(d, N)$, the size of the largest subset of
> $[N]^d$ with no $5$ points on a $2$-plane, as $N \to \infty$?
>
> This asks for `green_74` up to constant factors that may depend on $d$.

```lean
theorem green_74.variants.order :
    ∀ d : ℕ, (fun N ↦ (maxNoFiveCoplanar d N : ℝ)) =Θ[atTop] green_74.variants.order.answer d
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/74.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/74.lean#L85).

## `Green74.green_74.variants.large`

Open: stated without proof.

> [Gr24] writes: "I do not know if there can be such a set of size $N^{d-100}$." We read this as
> the question whether, for every $d$, $f(d, N) \ge N^{d - 100}$ for all sufficiently large $N$.
>
> The exponent uses truncated subtraction, so the case $d \le 100$ is trivial. For $d \ge 2$,
> $[N]^d$ is covered by $N^{d-2}$ parallel coordinate $2$-planes, so $f(d, N) \le 4N^{d-2}$; the
> question is whether the loss in the exponent can be kept at $100$ for every $d$ (Green's $100$
> presumably stands for an absolute constant).

```lean
theorem green_74.variants.large :
    ∀ d : ℕ, ∀ᶠ N in atTop, N ^ (d - 100) ≤ maxNoFiveCoplanar d N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/74.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/74.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/74.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/74.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.74)
