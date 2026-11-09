---
declaration: theorem
origin: cited
lean: Erdos943.erdos_943
statement: formalized
---

# Erdős Problem 943

> *Reference:* [erdosproblems.com/943](https://www.erdosproblems.com/943)

*Quoted from [FormalConjectures/ErdosProblems/943.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/943.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/943](https://www.erdosproblems.com/943).

The file states 1 research or textbook statement: 1 open.

## `Erdos943.erdos_943`

Open: stated without proof.

> Let $A$ be the set of powerful numbers. Is is true that $1_A\ast 1_A(n)=n^{o(1)}$ for every $n$?

```lean
theorem erdos_943 :
    ∃ (o : ℕ → ℝ), o =o[atTop] (1 : ℕ → ℝ) ∧ ∀ᶠ n in atTop, (sumRep Powerful n) ≤ (n : ℝ)^(o n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/943.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/943.lean#L36).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/943.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/943.lean)
- [erdosproblems.com/943](https://www.erdosproblems.com/943)
