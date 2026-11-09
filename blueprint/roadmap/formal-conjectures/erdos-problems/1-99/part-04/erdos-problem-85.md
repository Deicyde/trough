---
declaration: theorem
origin: cited
lean: Erdos85.erdos_85
statement: formalized
---

# Erdős Problem 85

> *Reference:* [erdosproblems.com/85](https://www.erdosproblems.com/85)

*Quoted from [FormalConjectures/ErdosProblems/85.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/85.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/85](https://www.erdosproblems.com/85).

The file states 1 research or textbook statement: 1 open.

## `Erdos85.erdos_85`

Open: stated without proof.

> Is it true that, for all large $n$, $f(n + 1) \ge f(n)$?

```lean
theorem erdos_85 : ∀ᶠ n in atTop, f n ≤ f (n + 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/85.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/85.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/85.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/85.lean)
- [erdosproblems.com/85](https://www.erdosproblems.com/85)
