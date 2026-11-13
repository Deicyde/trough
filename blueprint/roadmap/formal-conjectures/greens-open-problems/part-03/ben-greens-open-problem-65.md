---
declaration: theorem
origin: cited
lean: Green65.green_65, Green65.green_65.variants.prime_minus_one
statement: formalized
---

# Ben Green's Open Problem 65

> *References:*
> - [Gr26] [Ben Green's Open Problem 65](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.65)
> - [Gr22] [Green, Ben. "On Sárközy's theorem for shifted primes."](https://arxiv.org/abs/2206.08001)

*Quoted from [FormalConjectures/GreensOpenProblems/65.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/65.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Green65.green_65`

Open: stated without proof.

> Is there $c > 0$ such that every sufficiently large subset $A \subseteq [N]$ of size at least
> $N^{1-c}$ has a difference that is a nonzero square?

```lean
theorem green_65 :
    LargeDifferencePattern IsNonzeroSquare
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/65.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/65.lean#L76).

## `Green65.green_65.variants.prime_minus_one`

Solved: stated here without proof.

> Green asks the analogous question with a nonzero square replaced by $p - 1$ for a prime $p$.
> Green [Gr22, Theorem 1.1] solved this positively.

```lean
theorem green_65.variants.prime_minus_one :
    LargeDifferencePattern IsPrimeMinusOne
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/65.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/65.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/65.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/65.lean)
- [Ben Green's Open Problem 65](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.65)
