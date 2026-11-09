---
declaration: theorem
origin: cited
lean: PrimeTuplesConjecture.prime_tuples_conjecture
statement: formalized
---

# Prime Tuples Conjecture

> *Reference:* [FLC07] Friedlander, J. B. and Luca, F. and Stoiciu, M., On the irrationality of a
> divisor function series. Integers (2007).

*Quoted from [FormalConjectures/Paper/PrimeTuples.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PrimeTuples.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `PrimeTuplesConjecture.prime_tuples_conjecture`

Open: stated without proof.

> For any `k ≥ 2`, let `a₁,...,aₖ` and `b₁,...,bₖ` be integers with `aᵢ > 0`. Suppose that for
> every prime `p` there exists an integer `n` such that `p ∤ ∏ i, (aᵢ n + bᵢ)`. Then there exist
> infinitely many `n` such that `aᵢ n + bᵢ` is prime for all `i`.

```lean
theorem prime_tuples_conjecture {k : ℕ} (hk : 2 ≤ k) (a : Fin k → ℕ+) (b : Fin k → ℕ)
    (hab : ∀ p, p.Prime → ∃ n, ¬ p ∣ ∏ i, (a i * n + b i)) :
    Set.Infinite {n | ∀ i : Fin k, (a i * n + b i).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/PrimeTuples.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PrimeTuples.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/PrimeTuples.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/PrimeTuples.lean)
