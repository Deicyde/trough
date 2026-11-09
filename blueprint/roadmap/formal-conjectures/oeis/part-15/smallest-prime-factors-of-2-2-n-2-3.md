---
declaration: theorem
origin: cited
lean: OeisA248802.a_ten_mul_add_two_eq, OeisA248802.a_fifty_eight_mul_add_twenty_six_eq
statement: formalized
---

# Smallest prime factors of $2^{2^n+2} + 3$

> Smallest prime factor of $2^{2^n+2} + 3$.
>
> *References:*
> - [A248802](https://oeis.org/A248802)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/248802.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/248802.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA248802.a_ten_mul_add_two_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/248802.wip.lean#L208](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/248802.wip.lean#L208).

> Conjecture 1: $a(10n+2) = 67$ for $n \ge 0$. - _Chai Wah Wu_, Oct 21 2019
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_ten_mul_add_two_eq (n : ℕ) : a (10 * n + 2) = 67
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/248802.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/248802.lean#L77).

## `OeisA248802.a_fifty_eight_mul_add_twenty_six_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/248802.wip.lean#L982](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/248802.wip.lean#L982).

> Conjecture 4: $a(58n+26) = 1399$ for $n \ge 0$ and when it is not covered by Conjectures 1-3. - _Chai Wah Wu_, Oct 21 2019
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_fifty_eight_mul_add_twenty_six_eq (n : ℕ) :
    (¬CoveredByC1 (58 * n + 26) ∧ ¬CoveredByC2 (58 * n + 26) ∧
    ¬CoveredByC3 (58 * n + 26)) → a (58 * n + 26) = 1399
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/248802.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/248802.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/248802.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/248802.lean)
- [A248802](https://oeis.org/A248802)
