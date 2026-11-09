---
declaration: theorem
origin: cited
lean: AmicableNumbers.relatively_prime_amicable, AmicableNumbers.infinitely_many_amicable, AmicableNumbers.opposite_parity_amicable
statement: formalized
---

# Amicable numbers

> Two distinct positive integers form an amicable pair if each equals the sum of the
> proper divisors of the other. Equivalently, $(a, b)$ is an amicable pair if
> $\sigma(a) = a + b$ and $\sigma(b) = a + b$, where $\sigma(n)$ denotes the sum of
> all positive divisors of $n$.
>
> Several open problems about amicable numbers are formalised here:
>
> * Do there exist relatively prime amicable numbers?
> * Are there infinitely many amicable pairs?
> * Do there exist amicable numbers with opposite parity (one even, one odd)?
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers)
> - [MathWorld](https://mathworld.wolfram.com/AmicableNumbers.html)
> - [OEIS A063990](https://oeis.org/A063990)

*Quoted from [FormalConjectures/Wikipedia/AmicableNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AmicableNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 2 test statements, counted here but not shown.

## `AmicableNumbers.relatively_prime_amicable`

Open: stated without proof.

> **Relatively prime amicable numbers conjecture.**
> Do there exist amicable numbers $(a, b)$ with $\gcd(a, b) = 1$?
>
> All known amicable pairs share a common factor. It is an open question
> whether a pair of relatively prime amicable numbers can exist.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers)

```lean
theorem relatively_prime_amicable :
    ∃ a b : ℕ, IsAmicable a b ∧ a ≠ b ∧ a.Coprime b
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AmicableNumbers.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AmicableNumbers.lean#L66).

## `AmicableNumbers.infinitely_many_amicable`

Open: stated without proof.

> **Infinitely many amicable numbers conjecture.**
>
> Are there infinitely many pairs of amicable numbers?
>
> While many amicable pairs are known, it remains open whether there are infinitely many.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers),
> [erdosproblems.com/830](https://www.erdosproblems.com/830)

```lean
theorem infinitely_many_amicable : type_of% Erdos830.erdos_830.parts.i
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AmicableNumbers.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AmicableNumbers.lean#L81).

## `AmicableNumbers.opposite_parity_amicable`

Open: stated without proof.

> **Amicable numbers with opposite parity conjecture.**
> Do there exist amicable numbers $(a, b)$ where one is even and the other is odd?
>
> All known amicable pairs are either both even or both odd. It is widely believed
> that mixed-parity amicable pairs do not exist, but this remains open.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers)

```lean
theorem opposite_parity_amicable :
    ∃ a b : ℕ, IsAmicable a b ∧ (Even a ↔ Odd b)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/AmicableNumbers.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AmicableNumbers.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AmicableNumbers.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AmicableNumbers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Amicable_numbers)
