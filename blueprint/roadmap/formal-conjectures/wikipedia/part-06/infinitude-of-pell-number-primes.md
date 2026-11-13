---
declaration: theorem
origin: cited
lean: PellNumbers.pellNumber_sq_add_pellNumber_succ_sq, PellNumbers.coe_pellNumber_eq, PellNumbers.infinite_pellNumber_primes
statement: formalized
---

# Infinitude of Pell number primes

> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Pell_number#Primes_and_squares)
>  - [A86383](https://oeis.org/A86383)
>
> The Pell numbers $P_n$ are defined by $P_0 = 0$,
> $P_1 = 1$, $P_{n+2} = 2*P_{n+1} + P_n$. [OEIS A129](https://oeis.org/A129)
>
> The conjecture says that there are infinitely many prime Pell numbers.

*Quoted from [FormalConjectures/Wikipedia/Pell.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Pell.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 textbook results. It also has 4 test statements, counted here but not shown.

## `PellNumbers.pellNumber_sq_add_pellNumber_succ_sq`

Textbook result, proved here.

> Similar to Fibonacci numbers, there exist numerous identities around Pell numbers, i.e.
> P_{2n+1} = P_n ^ 2 + P_{n+1} ^ 2

```lean
theorem pellNumber_sq_add_pellNumber_succ_sq (n : ℕ) :
    pellNumber (2 * n + 1) = pellNumber n ^ 2 + pellNumber (n + 1) ^ 2
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Pell.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Pell.lean#L62).

## `PellNumbers.coe_pellNumber_eq`

Textbook result, proved here.

> An explicit formula for Pell numbers, similar to Binet's formula

```lean
theorem coe_pellNumber_eq : ∀ n, (pellNumber n : ℝ) = ((1 + √2) ^ n - (1 - √2) ^ n) / (2 * √2)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Pell.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Pell.lean#L98).

## `PellNumbers.infinite_pellNumber_primes`

Open: stated without proof.

> There are infinitely many prime Pell numbers

```lean
theorem infinite_pellNumber_primes : Infinite {n : ℕ | Prime (pellNumber n)}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Pell.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Pell.lean#L148).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Pell.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Pell.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Pell_number#Primes_and_squares)
