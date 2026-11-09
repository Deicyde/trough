---
declaration: theorem
origin: cited
lean: OeisA363102.a_eq_one_or_prime
statement: formalized
---

# Primality of continued fraction denominators $a(n)$ for $n \ge 3$

> Auxiliary sequence A051403, defined as
>
> $$\frac{(n+2) \sum_{k=0}^n k!}{2}$$
>
> Denominator of the continued fraction $1/(2-3/(3-4/(4-5/(...(n-1)-n/(-2)))))$.
> The sequence is defined by the formula:
>
> $$a(n) = \frac{n^2 - 2}{\gcd(n^2 - 2, 2 \cdot A051403(n-3) + n \cdot A051403(n-4))}$$
>
> The formula is valid for $n \ge 3$.
>
> *References:*
> - [A363102](https://oeis.org/A363102)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A051403](https://oeis.org/A051403)

*Quoted from [FormalConjectures/OEIS/363102.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/363102.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA363102.a_eq_one_or_prime`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/363102.wip.lean#L283](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/363102.wip.lean#L283).

> Conjecture: The sequence contains only 1's and primes.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_eq_one_or_prime : ∀ n : ℕ, 3 ≤ n → a n = 1 ∨ Nat.Prime (a n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/363102.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/363102.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/363102.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/363102.lean)
- [A363102](https://oeis.org/A363102)
