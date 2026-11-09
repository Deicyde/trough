---
declaration: theorem
origin: cited
lean: OeisA193279.a_eq_self_of_perfect_of_even, OeisA193279.conjecture
statement: formalized
---

# Number of distinct sums of distinct proper divisors of $n$

> The sequence $a(n)$ counts the number of distinct sums of non-empty subsets of the proper divisors
> of $n$.
>
> *References:*
> - [A193279](https://oeis.org/A193279)

*Quoted from [FormalConjectures/OEIS/193279.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/193279.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 solved and 1 textbook result. It also has 6 test statements, counted here but not shown.

## `OeisA193279.a_eq_self_of_perfect_of_even`

Textbook result, stated without proof.

> If $n$ is an even perfect number, then $a(n) = n$.
> - _Michael Engling_, Jul 20 2011

```lean
theorem a_eq_self_of_perfect_of_even (n : ℕ) (hperf : n.Perfect) (heven : Even n) :
    a n = n
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/193279.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/193279.lean#L63).

## `OeisA193279.conjecture`

Solved: stated here without proof.

> Is the converse true, i.e., if $a(n) = n$, is $n$ necessarily an even perfect number?
> - _Michael Engling_, Jul 20 2011
>
> The answer is no: for example, $n = 492 = 2^2 \cdot 3 \cdot 41$ and
> $n = 1652 = 2^2 \cdot 7 \cdot 59$ satisfy $a(n) = n$ but are abundant rather than perfect.

```lean
theorem conjecture : ¬ ∀ n : ℕ, 0 < n → a n = n → n.Perfect ∧ Even n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/193279.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/193279.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/193279.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/193279.lean)
- [A193279](https://oeis.org/A193279)
