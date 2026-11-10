---
declaration: theorem
origin: cited
lean: Erdos985.erdos_985, Erdos985.erdos_985.variants.two_three_five_primitive_root
statement: formalized
---

# Erdős Problem 985

> *Reference:* [erdosproblems.com/985](https://www.erdosproblems.com/985)

*Quoted from [FormalConjectures/ErdosProblems/985.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/985.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/985](https://www.erdosproblems.com/985).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos985.erdos_985`

Open: stated without proof.

> Is it true that, for every prime $p$, there is a prime $q \leq p$ which is a primitive root modulo $p$?

```lean
theorem erdos_985 : ∀ᵉ (p : ℕ) (hp_prime : p.Prime) (hp_nontrivial : p ≠ 2),
    ∃ q, q.Prime ∧ q < p ∧ orderOf (q : ZMod p) = p - 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/985.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/985.lean#L34).

## `Erdos985.erdos_985.variants.two_three_five_primitive_root`

Solved: stated here without proof.

> Heath-Brown proved that at least one of 2, 3, or 5 is a primitive root for infinitely many primes $p$.

```lean
theorem erdos_985.variants.two_three_five_primitive_root :
    Set.Infinite
      {p : ℕ | p.Prime ∧
      (orderOf (2 : ZMod p) = p - 1 ∨
       orderOf (3 : ZMod p) = p - 1 ∨
       orderOf (5 : ZMod p) = p - 1)}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/985.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/985.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/985.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/985.lean)
- [erdosproblems.com/985](https://www.erdosproblems.com/985)
