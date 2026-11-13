---
declaration: theorem
origin: cited
lean: Green70.green_70, Green70.green_70.variants.five_visible, Green70.green_70.variants.empty_pentagon
statement: formalized
---

# Ben Green's Open Problem 70

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.70)
> - [ABBCDHKLPW11] Abel, Z., Ballinger, B., Bose, P., Collette, S., Dujmović, V., Hurtado, F.,
>   Kominers, S. D., Langerman, S., Pór, A. and Wood, D. R., *Every large point set contains many
>   collinear points or an empty pentagon*. Graphs Combin. 27 (2011), 47-60.
>   [arXiv:0904.0262](https://arxiv.org/abs/0904.0262)
> - [KPW05] Kára, J., Pór, A. and Wood, D. R., *On the chromatic number of the visibility graph of
>   a set of points in the plane*. Discrete Comput. Geom. 34 (2005), 497-506.
>   [doi:10.1007/s00454-005-1177-z](https://doi.org/10.1007/s00454-005-1177-z)
> - [PoWo10] Pór, A. and Wood, D. R., *On visibility and blockers*. J. Comput. Geom. 1 (2010),
>   29-40. [arXiv:0912.1150](https://arxiv.org/abs/0912.1150)

*Quoted from [FormalConjectures/GreensOpenProblems/70.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/70.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 2 API statements, counted here but not shown.

## `Green70.green_70`

Open: stated without proof.

> Fix integers $k, \ell$. Is it true that, given a set of $n \geq n_0(k, \ell)$ points in
> $\mathbb{R}^2$, either some $k$ of them lie on a line, or some $\ell$ of them are 'mutually
> visible', that is to say that line segment joining them contains no other point from the set?
>
> This question was first raised by Kára, Pór and Wood [KPW05]. It is called the big-line-big-clique
> conjecture [PoWo10, Conjecture 1]. We read "mutually visible" as "pairwise visible". The cases
> $k \leq 3$ are trivial: a set with no three collinear points has all pairs visible. For the
> cases $\ell \leq 5$, see `green_70.variants.five_visible`.

```lean
theorem green_70 :
    ∀ k ℓ : ℕ, ∃ n₀ : ℕ, ∀ P : Finset (ℝ × ℝ),
      n₀ ≤ #P → HasCollinear k P ∨ HasMutuallyVisible ℓ P
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/70.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/70.lean#L81).

## `Green70.green_70.variants.five_visible`

Solved: stated here without proof.

> The answer to `green_70` is yes for $\ell \leq 5$ [Gr24]: for every $k$, every sufficiently large
> planar set contains $k$ collinear points or $5$ mutually visible points. The case $\ell = 5$ is
> [ABBCDHKLPW11, Theorem 5], and it implies the cases $\ell \leq 4$ (see
> `HasMutuallyVisible.mono`). According to [ABBCDHKLPW11, Section 1.4], the case $\ell = 4$ was
> proved in [KPW05]. In [ABBCDHKLPW11] and [PoWo10] the letters $k$ and $\ell$ are interchanged.

```lean
theorem green_70.variants.five_visible :
    ∀ k : ℕ, ∃ n₀ : ℕ, ∀ P : Finset (ℝ × ℝ),
      n₀ ≤ #P → HasCollinear k P ∨ HasMutuallyVisible 5 P
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/70.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/70.lean#L94).

## `Green70.green_70.variants.empty_pentagon`

Solved: stated here without proof.

> Generalised empty pentagon theorem [ABBCDHKLPW11, Theorem 3]: for every integer $k \geq 2$,
> every sufficiently large finite set of points in the plane contains $k$ collinear points or an
> empty pentagon. By `HasEmptyPentagon.hasMutuallyVisible`, this implies
> `green_70.variants.five_visible`, which is [ABBCDHKLPW11, Theorem 5].

```lean
theorem green_70.variants.empty_pentagon :
    ∀ k : ℕ, 2 ≤ k → ∃ n₀ : ℕ, ∀ P : Finset (ℝ × ℝ),
      n₀ ≤ #P → HasCollinear k P ∨ HasEmptyPentagon P
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/70.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/70.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/70.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/70.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.70)
