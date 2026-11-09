---
declaration: theorem
origin: cited
lean: Green22.green_22, Green22.green_22.variants.green_sawhney_bound, Green22.green_22.variants.moreira_infinite, Green22.green_22.variants.lower_nine
statement: formalized
---

# Green's Open Problem 22

> *References:*
> - [Gr26] [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.22)
> - [Mo17] Moreira, Joel. "Monochromatic sums and products in N." Annals of Mathematics 185.3 (2017):
>   1069-1090.
> - [GrSa25] Green, Ben, and Mehtaab Sawhney. "Bounds for monochromatic solutions to
>   $\{x+ y, xy\} $." arXiv preprint arXiv:2511.09365 (2025).
> - [Ri25] Richter, Florian K. "Sums and products in sets of positive density." arXiv preprint
>   arXiv:2507.00515 (2025).
> - [BoSa24] Bowen, Matt, and Marcin Sabok. "Monochromatic products and sums in the rationals." Forum
>   of Mathematics, Pi. Vol. 12. Cambridge University Press, 2024.
> - [Bo25] Bowen, Matt. "Monochromatic products and sums in 2-colorings of N." Advances in Mathematics
>   462 (2025): 110095.
> - [Al23] Alweiss, Ryan. "Monochromatic Sums and Products over $\mathbb {Q} $." arXiv preprint
>   arXiv:2307.08901 (2023).

*Quoted from [FormalConjectures/GreensOpenProblems/22.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Green22.green_22`

Open: stated without proof.

> If $\{1, \ldots, N\}$ is $r$-coloured then, for $N \geqslant N_0(r)$, there are integers
> $x, y \geqslant 3$ such that $x + y, xy$ have the same colour.
>
> Find reasonable bounds for $N_0(r)$. The goal is to improve upon the Green-Sawhney bound.

```lean
theorem green_22 :
    ∀ᶠ r in atTop, N₀ r ≤ green_22.answer r ∧
    green_22.answer =o[atTop] GreenSawhneyBound
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/22.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean#L76).

## `Green22.green_22.variants.green_sawhney_bound`

Solved: stated here without proof.

> [GrSa25, Theorem 1.1] found a permissible upper bound.

```lean
theorem green_22.variants.green_sawhney_bound :
    ∀ᶠ r in atTop, N₀ r ≤ GreenSawhneyBound r
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/22.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean#L85).

## `Green22.green_22.variants.moreira_infinite`

Solved: stated here without proof.

> [Mo17, Corollary 1.5] For any finite coloring of $\mathbb{N}$ there exist (infinitely many)
> $x, y \in \mathbb{N}$ such that $\{xy, x + y\}$ is monochromatic.
>
> This guarantees that $N_0(r)$ is well-defined.
>
> Note: [Mo17] also establishes that $x$ is of the same colour.

```lean
theorem green_22.variants.moreira_infinite :
    ∀ (r : ℕ) (coloring : ℕ → Fin r),
    Set.Infinite { p : ℕ × ℕ |
      0 < p.1 ∧ 0 < p.2 ∧
      coloring p.1 = coloring (p.1 * p.2) ∧
      coloring p.1 = coloring (p.1 + p.2) }
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/22.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean#L98).

## `Green22.green_22.variants.lower_nine`

Solved: stated here without proof.

> Since $x, y \geq 3$, we must have $xy \geq 9$, so every $N$ such that all $r$-colourings of
> $\{1, \ldots, N\}$ have the monochromatic sum-product property is at least $9$. In particular
> $N_0(r) \geq 9$ once $N_0(r)$ is well-defined, which follows from [Mo17].
>
> The bound is stated for every such $N$ and not as `9 ≤ N₀ r`: since `sInf ∅ = 0` in `ℕ`, the
> latter is equivalent to the existence of such an $N$.

```lean
theorem green_22.variants.lower_nine : ∀ r : ℕ, r ≠ 0 →
    ∀ N : ℕ, (∀ c : Icc 1 N → Fin r, HasMonochromaticSumProduct N r c) → 9 ≤ N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/22.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/22.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/22.lean)
- [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.22)
