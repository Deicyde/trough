---
declaration: theorem
origin: cited
lean: Erdos1101.erdos_1101.parts.i, Erdos1101.erdos_1101.parts.ii
statement: formalized
---

# Erdős Problem 1101

> *Reference:* [erdosproblems.com/1101](https://www.erdosproblems.com/1101)

*Quoted from [FormalConjectures/ErdosProblems/1101.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1101.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1101](https://www.erdosproblems.com/1101).

The file states 2 research or textbook statements: 2 open.

## `Erdos1101.erdos_1101.parts.i`

Open: stated without proof.

> 1. There is NO good sequence with polynomial growth.

```lean
theorem erdos_1101.parts.i :
    ¬ ∃ u, IsGood u ∧ ∃ k : ℕ, (fun n => (u n : ℝ)) =O[atTop] (fun n => (n : ℝ) ^ k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1101.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1101.lean#L61).

## `Erdos1101.erdos_1101.parts.ii`

Open: stated without proof.

> 2. There is a good sequence with sub-exponential growth.

```lean
theorem erdos_1101.parts.ii :
    ∃ u, IsGood u ∧ (fun n => Real.log (u n : ℝ)) =o[atTop] (fun n => (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1101.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1101.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1101.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1101.lean)
- [erdosproblems.com/1101](https://www.erdosproblems.com/1101)
