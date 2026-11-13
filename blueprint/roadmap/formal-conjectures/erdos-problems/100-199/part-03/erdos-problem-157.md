---
declaration: theorem
origin: cited
lean: Erdos157.erdos_157
statement: formalized
---

# Erdős Problem 157

> *References:*
> - [erdosproblems.com/157](https://www.erdosproblems.com/157)
> - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., *On sum sets of Sidon sets, I*. Journal of Number
>   Theory (1994), 329-347.
> - [Er94b] Erdős, Paul, *Some problems in number theory, combinatorics and combinatorial geometry*.
>   Math. Pannon. (1994), 261-269.
> - [Pi23] Pilatte, C., *A solution to the Erdős–Sárközy–Sós problem on asymptotic Sidon bases of
>   order 3*. Compositio Math. (2024), 1418-1432.

*Quoted from [FormalConjectures/ErdosProblems/157.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/157.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/157](https://www.erdosproblems.com/157).

The file states 1 research or textbook statement: 1 solved.

## `Erdos157.erdos_157`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos157/Unconditional.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos157/Unconditional.lean).

> Does there exist an infinite Sidon set which is an asymptotic basis of order $3$?
>
> Yes, as shown by Pilatte [Pi23].

```lean
theorem erdos_157 :
    ∃ A : Set ℕ, A.Infinite ∧ IsSidon A ∧ A.IsAsymptoticAddBasisOfOrder 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/157.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/157.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/157.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/157.lean)
- [erdosproblems.com/157](https://www.erdosproblems.com/157)
