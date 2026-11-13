---
declaration: theorem
origin: cited
lean: Erdos1108.erdos_1108.parts.i, Erdos1108.erdos_1108.parts.ii
statement: formalized
---

# Erdős Problem 1108

> *Reference:* [erdosproblems.com/1108](https://www.erdosproblems.com/1108)

*Quoted from [FormalConjectures/ErdosProblems/1108.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1108.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1108](https://www.erdosproblems.com/1108).

The file states 2 research or textbook statements: 2 open.

## `Erdos1108.erdos_1108.parts.i`

Open: stated without proof.

> For each $k \geq 2$, does the set $A = \left\{ \sum_{n\in S}n! : S\subset \mathbb{N}_{\geq 1}\text{ finite}\right\}$ of all finite sums of distinct factorials contain only finitely many $k$-th powers?

```lean
theorem erdos_1108.parts.i : ∀ k ≥ 2,
    Set.Finite { a | a ∈ FactorialSums ∧ ∃ m : ℕ, m ^ k = a }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1108.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1108.lean#L44).

## `Erdos1108.erdos_1108.parts.ii`

Open: stated without proof.

> Does the set $A = \left\{ \sum_{n\in S}n! : S\subset \mathbb{N}_{\geq 1}\text{ finite}\right\}$ of all finite sums of distinct factorials contain only finitely many powerful numbers
> (`Nat.Powerful`)?

```lean
theorem erdos_1108.parts.ii :
     {a ∈ FactorialSums | a.Powerful}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1108.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1108.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1108.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1108.lean)
- [erdosproblems.com/1108](https://www.erdosproblems.com/1108)
