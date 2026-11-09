---
declaration: theorem
origin: cited
lean: PrimeTriplets.prime_triplets
statement: formalized
---

# Prime Triplet Conjecture

> *Reference:* [Prime Triplet Wikipedia Page](https://en.wikipedia.org/wiki/Prime_triplet#Conjecture_on_prime_triplets)

*Quoted from [FormalConjectures/Wikipedia/PrimeTriplets.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimeTriplets.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `PrimeTriplets.prime_triplets`

Open: stated without proof.

> Are there infinitely many tuples of three consecutive primes $(p, q, r)$ such that $r - p = 6$?

```lean
theorem prime_triplets :
    {p : ℕ | Prime p ∧ (Prime (p + 2) ∨ Prime (p + 4)) ∧ Prime (p + 6)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimeTriplets.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimeTriplets.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PrimeTriplets.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimeTriplets.lean)
- [Prime Triplet Wikipedia Page](https://en.wikipedia.org/wiki/Prime_triplet#Conjecture_on_prime_triplets)
