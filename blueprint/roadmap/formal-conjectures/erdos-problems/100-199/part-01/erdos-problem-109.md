---
declaration: theorem
origin: cited
lean: Erdos109.erdos_109
statement: formalized
---

# Erdős Problem 109

> *References:*
> - [erdosproblems.com/109](https://www.erdosproblems.com/109)
> - [MRR19] J. Moreira, F.K. Richter, and D. Robertson, A proof of a sumset conjecture of Erdős,
>   Annals of Math. 189 (2019), 605-652.

*Quoted from [FormalConjectures/ErdosProblems/109.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/109.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/109](https://www.erdosproblems.com/109).

The file states 1 research or textbook statement: 1 solved.

## `Erdos109.erdos_109`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos109.lean#L9074](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos109.lean#L9074).

> Any $A\subseteq \mathbb{N}$ of positive upper density contains a sumset $B+C$ where both $B$ and $C$
> are infinite.
>
> The Erdős sumset conjecture. Proved by Moreira, Richter, and Robertson [MRR19].

```lean
theorem erdos_109 (A : Set ℕ) (h : A.upperDensity > 0) :
    ∃ B C : Set ℕ, B.Infinite ∧ C.Infinite ∧ B + C ⊆ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/109.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/109.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/109.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/109.lean)
- [erdosproblems.com/109](https://www.erdosproblems.com/109)
