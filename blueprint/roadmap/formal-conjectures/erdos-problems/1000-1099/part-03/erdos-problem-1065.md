---
declaration: theorem
origin: cited
lean: Erdos1065.erdos_1065.parts.i, Erdos1065.erdos_1065.parts.ii
statement: formalized
---

# Erdős Problem 1065

> *Reference:* [erdosproblems.com/1065](https://www.erdosproblems.com/1065)

*Quoted from [FormalConjectures/ErdosProblems/1065.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1065.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1065](https://www.erdosproblems.com/1065).

The file states 2 research or textbook statements: 2 open.

## `Erdos1065.erdos_1065.parts.i`

Open: stated without proof.

> Are there infinitely many primes $p$ such that $p = 2^k * q + 1$
> for some prime $q$ and $k ≥ 0$?
>
> This is mentioned as B46
> in [Unsolved Problems in Number Theory](https://doi.org/10.1007/978-0-387-26677-0)
> by *Richard K. Guy*

```lean
theorem erdos_1065.parts.i :
    Set.Infinite {p | ∃ q k, p.Prime ∧ q.Prime ∧ p = 2^k * q + 1}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1065.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1065.lean#L39).

## `Erdos1065.erdos_1065.parts.ii`

Open: stated without proof.

> Are there infinitely many primes $p$ such that $p = 2^k 3^l q + 1$
> for some prime $q$ and $k ≥ 0$, $l ≥ 0$?

```lean
theorem erdos_1065.parts.ii :
    Set.Infinite {p | ∃ q k l, p.Prime ∧ q.Prime ∧ p = 2^k * 3^l * q + 1}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1065.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1065.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1065.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1065.lean)
- [erdosproblems.com/1065](https://www.erdosproblems.com/1065)
