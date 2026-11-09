---
declaration: theorem
origin: cited
lean: Erdos1214.erdos_1214
statement: formalized
---

# Erdős Problem 1214

> *References:*
> - [erdosproblems.com/1214](https://www.erdosproblems.com/1214)
> - [CoSc97] Corrales-Rodrigáñez, Capi and Schoof, René, The support problem and its
>   elliptic analogue. J. Number Theory (1997) [Volume 64, Issue 2], 276--290.

*Quoted from [FormalConjectures/ErdosProblems/1214.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1214.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1214](https://www.erdosproblems.com/1214).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1214.erdos_1214`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1214.lean#L948](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1214.lean#L948).

> Let $x,y\geq 1$ be integers such that, for all $n\geq 1$, the set of primes dividing $x^{n}-1$ is
> equal to the set of primes dividing $y^n-1$. Must $x=y$?
>
> Erdős asked this at a 1988 number theory conference in Banff.
>
> A positive answer was given by Corrales-Rodrigáñez and Schoof [CoSc97].

```lean
theorem erdos_1214 :
    ∀ x y : ℕ, x ≥ 1 → y ≥ 1 →
      (∀ n : ℕ, n ≥ 1 → { p : ℕ | p.Prime ∧ p ∣ x ^ n - 1 } = { p : ℕ | p.Prime ∧ p ∣ y ^ n - 1 }) →
      x = y
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1214.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1214.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1214.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1214.lean)
- [erdosproblems.com/1214](https://www.erdosproblems.com/1214)
