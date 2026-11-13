---
declaration: theorem
origin: cited
lean: Green37.green_37, Green37.green_37_asymptotic, Green37.green_37_theta, Green37.green_37_lower_bound
statement: formalized
---

# Ben Green's Open Problem 37

> What is the smallest subset of `ℕ` containing, for each `d = 1, …, N`,
> an arithmetic progression of length `k` with common difference `d`?
>
> *References:*
> - [Ben Green's Open Problem 37](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.37)
> - [Green & Tao, *The primes contain arbitrarily long arithmetic progressions* (arXiv:math/0404188)](https://arxiv.org/abs/math/0404188)

*Quoted from [FormalConjectures/GreensOpenProblems/37.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 1 API statement, counted here but not shown.

## `Green37.green_37`

Open: stated without proof.

> Given a natural number `N`, what is the smallest size of a subset of `ℕ` that contains, for each `d = 1, …, N`,
> an arithmetic progression of length `k` with common difference `d`.

```lean
theorem green_37 (N k : ℕ) :
    IsLeast { m | ∃ A : Finset ℕ, A.card = m ∧ IsAPCover (A : Set ℕ) N k }
      (green_37.answer N k)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/37.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean#L53).

## `Green37.green_37_asymptotic`

Open: stated without proof.

> Asymptotic version: determine the asymptotic behavior of `m(N, k)` as `N` grows.
> The solver should determine a function `f : ℕ → ℕ → ℝ` such that, for each `k`,
> `f k` eventually equals `(fun N ↦ (m N k : ℝ))`.

```lean
theorem green_37_asymptotic (k : ℕ) :
    ∀ᶠ N in atTop, (m N k : ℝ) = green_37_asymptotic.answer k N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/37.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean#L66).

## `Green37.green_37_theta`

Open: stated without proof.

> Determine, for each `k`, the asymptotic equivalence class (theta) of `m(N, k)` as `N` grows.

```lean
theorem green_37_theta (k : ℕ) :
    (fun N ↦ (m N k : ℝ)) =Θ[atTop] green_37_theta.answer k
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/37.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean#L74).

## `Green37.green_37_lower_bound`

Open: stated without proof.

> Writing `F_k(N)` for `m(N, k)`, Green conjectures that `F_k(N) ≫_k N^(1 - c_k)` for some
> sequence `c_k` with `c_k → 0` as `k → ∞`.
> The restriction to `0 < k` excludes the degenerate case `m(N, 0) = 0`.

```lean
theorem green_37_lower_bound :
    ∃ c : ℕ → ℝ, Tendsto c atTop (nhds 0) ∧
      ∀ k, 0 < k → (fun N : ℕ ↦ (N : ℝ) ^ (1 - c k)) =O[atTop] fun N ↦ (m N k : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/37.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/37.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/37.lean)
- [Ben Green's Open Problem 37](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.37)
