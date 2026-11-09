---
declaration: theorem
origin: cited
lean: Erdos203.erdos_203
statement: formalized
---

# Erdős Problem 203

> *Reference:* [erdosproblems.com/203](https://www.erdosproblems.com/203)

*Quoted from [FormalConjectures/ErdosProblems/203.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/203.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/203](https://www.erdosproblems.com/203).

The file states 1 research or textbook statement: 1 open.

## `Erdos203.erdos_203`

Open: stated without proof.

> Is there an integer $m$ with $(m, 6) = 1$ such that none of $2^k \cdot 3^\ell \cdot m + 1$ are prime,
> for any $k, \ell \ge 0$?

```lean
theorem erdos_203 : ∃ m, m.Coprime 6 ∧ ∀ k l, ¬ (2^k * 3^l * m + 1).Prime
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/203.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/203.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/203.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/203.lean)
- [erdosproblems.com/203](https://www.erdosproblems.com/203)
