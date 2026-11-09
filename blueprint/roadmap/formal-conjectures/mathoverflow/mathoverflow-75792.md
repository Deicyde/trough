---
declaration: theorem
origin: cited
lean: Mathoverflow75792.complexity_five_pow, Mathoverflow75792.complexity_three_pow, Mathoverflow75792.complexity_two_pow
statement: formalized
---

# Mathoverflow 75792

> Various questions about integer complexity, which is the minimum number of `1`s needed to express a natural number using addition, multiplication, and parentheses.
>
> Let `‖n‖` denote the integer complexity of `n > 0`.
> * It is known that `‖3^n‖ = 3n` for `n > 0`.
> * Is it true that `‖2^n‖ = 2n` for `n > 0`?
> * The corresponding conjecture for `5` is false, because
>   `5^6 = 15625 = 1 + 2^3 * 3^2 * (1 + 2^3 * 3^3)`!
>
> We have chosen to formalise this using an inductive type.
>
> *References:*
>  - [mathoverflow/75792](https://mathoverflow.net/a/75792) by user [Harry Altman](https://mathoverflow.net/users/5583)
>  - http://arxiv.org/abs/1203.6462 by Jānis Iraids, Kaspars Balodis, Juris Čerņenoks, Mārtiņš Opmanis, Rihards Opmanis, Kārlis Podnieks
>  - http://arxiv.org/abs/1207.4841 by Harry Altman, Joshua Zelinsky
>  - https://oeis.org/A5245 : Mahler-Popken complexity.

*Quoted from [FormalConjectures/Mathoverflow/75792.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/75792.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 15 test statements, counted here but not shown.

## `Mathoverflow75792.complexity_five_pow`

Proved here.

> Is `5n` the complexity of `5^n` for `0 < n`? Answer: No.

```lean
theorem complexity_five_pow : ¬ ∀ n : ℕ, 0 < n → complexity (5 ^ n) = 5 * n
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Mathoverflow/75792.lean, line 204](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/75792.lean#L204).

## `Mathoverflow75792.complexity_three_pow`

Solved: stated here without proof.

> Is `3n` the complexity of `3^n` for `0 < n`? Answer: Yes, by John Selfridge.
>
> Reference: https://arxiv.org/abs/1207.4841

```lean
theorem complexity_three_pow : ∀ n : ℕ, 0 < n → complexity (3 ^ n) = 3 * n
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Mathoverflow/75792.lean, line 213](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/75792.lean#L213).

## `Mathoverflow75792.complexity_two_pow`

Open: stated without proof.

> Is `2n` the complexity of `2^n` for `0 < n`?

```lean
theorem complexity_two_pow : ∀ n : ℕ, 0 < n → complexity (2 ^ n) = 2 * n
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Mathoverflow/75792.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/75792.lean#L218).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/75792.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/75792.lean)
- [mathoverflow/75792](https://mathoverflow.net/a/75792)
