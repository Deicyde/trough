---
declaration: theorem
origin: cited
lean: Erdos938.erdos_938
statement: formalized
---

# Erdős Problem 938

> *Reference:* [erdosproblems.com/938](https://www.erdosproblems.com/938)

*Quoted from [FormalConjectures/ErdosProblems/938.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/938.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/938](https://www.erdosproblems.com/938).

The file states 1 research or textbook statement: 1 open.

## `Erdos938.erdos_938`

Open: stated without proof.

> Let $A=\{n_1 < n_2 < \cdots\}$ be the sequence of powerful numbers (if $p\mid n$ then $p^2\mid n$).
> Are there only finitely many three-term progressions of consecutive terms $n_k,n_{k+1},n_{k+2}$?

```lean
theorem erdos_938 : {P : Finset ℕ | (P : Set ℕ).IsAPOfLength 3 ∧ ∃ k,
    P = {nth Powerful k, nth Powerful (k + 1), nth Powerful (k + 2)}}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/938.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/938.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/938.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/938.lean)
- [erdosproblems.com/938](https://www.erdosproblems.com/938)
