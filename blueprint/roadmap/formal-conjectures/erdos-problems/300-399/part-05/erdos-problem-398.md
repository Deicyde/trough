---
declaration: theorem
origin: cited
lean: Erdos398.erdos_398
statement: formalized
---

# Erdős Problem 398

> *References:*
>  - [erdosproblems.com/398](https://www.erdosproblems.com/398)
>  - [Wikipedia: Brocard's problem](https://en.wikipedia.org/wiki/Brocard%27s_problem)

*Quoted from [FormalConjectures/ErdosProblems/398.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/398.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/398](https://www.erdosproblems.com/398).

The file states 1 research or textbook statement: 1 open.

## `Erdos398.erdos_398`

Open: stated without proof.

> **Brocard's Problem**
> Does $n! + 1 = m^2$ have integer solutions other than $n = 4, 5, 7$?

```lean
theorem erdos_398 : {n | ∃ m, n ! + 1 = m ^ 2} = {4, 5, 7}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/398.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/398.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/398.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/398.lean)
- [erdosproblems.com/398](https://www.erdosproblems.com/398)
