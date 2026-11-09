---
declaration: theorem
origin: cited
lean: Green19.green_19, Green19.green_19.lower, Green19.green_19.upper
statement: formalized
---

# Ben Green's Open Problem 19

> *References:*
> - [Gr26] [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.19)
> - [FSS20] Fox, Jacob, et al. "Triforce and corners." Mathematical Proceedings of the Cambridge
>   Philosophical Society. Vol. 169. No. 1. Cambridge University Press, 2020.
> - [Ma21] Mandache, Matei. "A variant of the Corners theorem." Mathematical Proceedings of the
>   Cambridge Philosophical Society. Vol. 171. No. 3. Cambridge University Press, 2021.
> - [Ch11] Chu, Qing. "Multiple recurrence for two commuting transformations." Ergodic Theory and
>   Dynamical Systems 31.3 (2011): 771-792.

*Quoted from [FormalConjectures/GreensOpenProblems/19.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/19.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Green19.green_19`

Solved: stated here without proof.

> What is $C$, the infimum of all exponents $c$ for which the following is true, uniformly for
> $0 < \alpha < 1$? Suppose that $A \subset \mathbb{F}_2^n \times \mathbb{F}_2^n$ is a set of density
> $\alpha$. Write $N := 2^n$. Then there is some $d \neq 0$ such that $A$ contains $\gg \alpha^c N^2$
> corners $(x,y), (x,y+d), (x+d,y)$.
>
> This question has been resolved by [FSS20], showing that $C = 4$.

```lean
theorem green_19 : C = 4
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/19.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/19.lean#L83).

## `Green19.green_19.lower`

Proved here.

> [Ma21] showed that $3.13 \leq C$. This also follows from `green_19`.

```lean
theorem green_19.lower : C >= 3.13
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/19.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/19.lean#L88).

## `Green19.green_19.upper`

Proved here.

> [Ma21] showed that $C \leq 4$. This also follows from `green_19`.

```lean
theorem green_19.upper : C <= 4
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/19.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/19.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/19.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/19.lean)
- [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.19)
