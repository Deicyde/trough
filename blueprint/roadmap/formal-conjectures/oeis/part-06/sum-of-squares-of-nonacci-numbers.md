---
declaration: theorem
origin: cited
lean: OeisA107247.known_prime_and_semiprimes, OeisA107247.conjecture
statement: formalized
---

# Sum of squares of nonacci numbers

> Sum of squares of nonacci numbers (Fibonacci 9-step numbers).
>
> *References:*
> - [A107247](https://oeis.org/A107247)

*Quoted from [FormalConjectures/OEIS/107247.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/107247.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA107247.known_prime_and_semiprimes`

Textbook result, stated without proof.

> Primes in this sequence include: $a(8) = 2$.
> Semiprimes in this sequence include: $a(9) = 6 = 2 * 3$, $a(10) = 22 = 2 * 11$,
> $a(11) = 86 = 2 * 43$, $a(13) = 1366 = 2 * 683$, $a(14) = 5462 = 2 * 2731$,
> $a(16) = 87382 = 2 * 43691$, $a(17) = 348503 = 37 * 9419$,
> $a(27) = 358201316657 = 71 * 5045088967$.
> (Note: The OEIS comment uses 1-based indexing, so their indices are shifted by +1 compared
> to this formalization).

```lean
theorem known_prime_and_semiprimes :
  (a 8).Prime ∧
  (a 9).IsSemiprime ∧
  (a 10).IsSemiprime ∧
  (a 11).IsSemiprime ∧
  (a 13).IsSemiprime ∧
  (a 14).IsSemiprime ∧
  (a 16).IsSemiprime ∧
  (a 17).IsSemiprime ∧
  (a 27).IsSemiprime
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/107247.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/107247.lean#L78).

## `OeisA107247.conjecture`

Open: stated without proof.

> Primes in this sequence include: $a(8) = 2$, which is next?

```lean
theorem conjecture :
    conjecture.answer = a (sInf {n : ℕ | 8 < n ∧ (a n).Prime})
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/107247.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/107247.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/107247.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/107247.lean)
- [A107247](https://oeis.org/A107247)
