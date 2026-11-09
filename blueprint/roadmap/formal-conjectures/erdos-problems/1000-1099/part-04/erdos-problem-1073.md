---
declaration: theorem
origin: cited
lean: Erdos1073.erdos_1073
statement: formalized
---

# Erdős Problem 1073

> *Reference:* [erdosproblems.com/1073](https://www.erdosproblems.com/1073)

*Quoted from [FormalConjectures/ErdosProblems/1073.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1073.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1073](https://www.erdosproblems.com/1073).

The file states 1 research or textbook statement: 1 open.

## `Erdos1073.erdos_1073`

Open: stated without proof.

> Is it true that $A(x) \le x^{o(1)}$?

```lean
theorem erdos_1073 :
    ∃ (o : ℕ → ℝ), o =o[atTop] (1 : ℕ → ℝ) ∧ ∀ x, A x ≤ x ^ (o x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1073.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1073.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1073.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1073.lean)
- [erdosproblems.com/1073](https://www.erdosproblems.com/1073)
