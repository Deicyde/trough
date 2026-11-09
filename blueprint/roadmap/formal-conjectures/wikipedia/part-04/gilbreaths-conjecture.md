---
declaration: theorem
origin: cited
lean: Gilbreath.gilbreath_conjecture
statement: formalized
---

# Gilbreath's conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Gilbreath.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Gilbreath.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Gilbreath.gilbreath_conjecture`

Open: stated without proof.

> **Gilbreath's conjecture**
> Gilbreath's conjecture states that every term in the sequence $d^k_0$ for $k > 0$ is equal to 1.

```lean
theorem gilbreath_conjecture (k : ℕ+) : d k 0 = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Gilbreath.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Gilbreath.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Gilbreath.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Gilbreath.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture)
