---
declaration: theorem
origin: cited
lean: OeisA83753.conjecture
statement: formalized
---

# Smallest palindrome with exactly $n$ divisors

> The sequence $a(n)$ is the smallest palindromic number with exactly $n$ divisors, or $0$
> if no such number exists.
>
> *References:*
> - [A083753](https://oeis.org/A083753)

*Quoted from [FormalConjectures/OEIS/83753.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/83753.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA83753.conjecture`

Open: stated without proof.

> There are no palindromic numbers greater than 1 which are the fifth or higher power of a natural
> number.

```lean
theorem conjecture (m k : ℕ) (hm : 1 < m) (hpal : IsDecimalPalindrome m) (hk : 5 ≤ k) :
    ¬ ∃ x : ℕ, m = x ^ k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/83753.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/83753.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/83753.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/83753.lean)
- [A083753](https://oeis.org/A083753)
