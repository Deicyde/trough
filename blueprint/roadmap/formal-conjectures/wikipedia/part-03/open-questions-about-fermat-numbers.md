---
declaration: theorem
origin: cited
lean: Fermat.fermat_number_are_composite, Fermat.infinite_fermat_primes, Fermat.infinite_fermat_composite, Fermat.exists_fermat_not_squarefree
statement: formalized
---

# Open questions about Fermat numbers

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Fermat_number)

*Quoted from [FormalConjectures/Wikipedia/Fermat.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open.

## `Fermat.fermat_number_are_composite`

Open: stated without proof.

> Are Fermat numbers composite for all `n > 4`?

```lean
theorem fermat_number_are_composite : ∀ n > 4, ¬Prime n.fermatNumber
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fermat.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean#L34).

## `Fermat.infinite_fermat_primes`

Open: stated without proof.

> Are there infinitely many Fermat primes?

```lean
theorem infinite_fermat_primes : Infinite {n : ℕ | Prime n.fermatNumber}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fermat.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean#L41).

## `Fermat.infinite_fermat_composite`

Open: stated without proof.

> Are there infinitely many composite Fermat numbers?

```lean
theorem infinite_fermat_composite : Infinite {n : ℕ | ¬Prime n.fermatNumber}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fermat.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean#L48).

## `Fermat.exists_fermat_not_squarefree`

Open: stated without proof.

> Does a Fermat number exist that is not square-free?

```lean
theorem exists_fermat_not_squarefree : ∃ n : ℕ, ¬Squarefree n.fermatNumber
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fermat.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Fermat.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Fermat.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Fermat_number)
