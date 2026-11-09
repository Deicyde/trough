---
declaration: theorem
origin: cited
lean: Erdos251.erdos_251
statement: formalized
---

# Erdős Problem 251

> *Reference:* [erdosproblems.com/251](https://www.erdosproblems.com/251)

*Quoted from [FormalConjectures/ErdosProblems/251.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/251.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/251](https://www.erdosproblems.com/251).

The file states 1 research or textbook statement: 1 open.

## `Erdos251.erdos_251`

Open: stated without proof.

> Is $\sum_{n=1}^\infty \frac{p_n}{2^n}$ irrational? Here $p_n$ is the $n$-th prime ($p_1=2, p_2=3, \dots$).

```lean
theorem erdos_251 : Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n) / (2 ^ n))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/251.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/251.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/251.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/251.lean)
- [erdosproblems.com/251](https://www.erdosproblems.com/251)
