---
declaration: theorem
origin: cited
lean: Green88.green_88
statement: formalized
---

# Ben Green's Open Problem 88

> *References:*
> - [Gr24] [Ben Green's Open Problem
>   88](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.88)
> - [GoLo21] [The length of an $s$-increasing sequence of
>   $r$-tuples](https://arxiv.org/abs/1609.08688)
>   by W. T. Gowers and J. Long

*Quoted from [FormalConjectures/GreensOpenProblems/88.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/88.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green88.green_88`

Open: stated without proof.

> [Gr24, Problem 88]: Is there an absolute constant $\delta > 0$ such that every pairwise
> $2$-comparable set $S \subseteq [N]^3$ satisfies $|S| \leq N^{2 - \delta}$?

```lean
theorem green_88 :
    ∃ δ > (0 : ℝ), ∀ (N : ℕ) (S : Finset (Fin 3 → Fin N)),
      (S : Set (Fin 3 → Fin N)).Pairwise IsComparable₂ →
        (S.card : ℝ) ≤ (N : ℝ) ^ (2 - δ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/88.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/88.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/88.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/88.lean)
- [Ben Green's Open Problem
  88](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.88)
