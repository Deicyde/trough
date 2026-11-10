---
declaration: theorem
origin: cited
lean: PolyTime.isPolyTime_primeFactorsList
statement: formalized
---

# Polynomial-time computability of factoring

> This file formalizes the open problem of whether natural number / integer factorization can be computed in
> polynomial time on a deterministic classical Turing machine.
>
> More precisely, it formalizes the following statement:
> Can the prime factorization of a natural number be computed in polynomial time
> (on a deterministic classical Turing machine)?
>
> *References:*
> - [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)
> - [Wikipedia: Integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)

*Quoted from [FormalConjectures/Wikipedia/IntegerFactorization.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IntegerFactorization.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `PolyTime.isPolyTime_primeFactorsList`

Open: stated without proof.

> **The integer factorization problem**: Can the prime factorization of a positive integer
> be computed in polynomial time?
>
> We state the problem by asking if `Nat.primeFactorsList` is polynomial-time computable
> (assuming typical encodings of ℕ and List ℕ into bitstrings).
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Integer_factorization)

```lean
theorem isPolyTime_primeFactorsList : IsPolyTime Nat.primeFactorsList
```

Category `research open`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/IntegerFactorization.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IntegerFactorization.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/IntegerFactorization.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IntegerFactorization.lean)
- [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)
