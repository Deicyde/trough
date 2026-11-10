---
declaration: theorem
origin: cited
lean: EuclidNumbers.infinite_prime_euclid_numbers, EuclidNumbers.euclid_numbers_are_square_free
statement: formalized
---

# Euclid Numbers conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Euclid_number)

*Quoted from [FormalConjectures/Wikipedia/Euclid.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Euclid.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `EuclidNumbers.infinite_prime_euclid_numbers`

Open: stated without proof.

> It is not known whether there is an infinite number of prime Euclid numbers.

```lean
theorem infinite_prime_euclid_numbers : {n | (Euclid n).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Euclid.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Euclid.lean#L39).

## `EuclidNumbers.euclid_numbers_are_square_free`

Open: stated without proof.

> It is not known whether every Euclid number is a square-free number.

```lean
theorem euclid_numbers_are_square_free : (∀ n, Squarefree (Euclid n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Euclid.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Euclid.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Euclid.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Euclid.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Euclid_number)
