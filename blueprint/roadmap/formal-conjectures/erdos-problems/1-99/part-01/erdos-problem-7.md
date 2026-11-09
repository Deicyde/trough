---
declaration: theorem
origin: cited
lean: Erdos7.erdos_7
statement: formalized
---

# Erdős Problem 7

> *Reference:* [erdosproblems.com/7](https://www.erdosproblems.com/7)

*Quoted from [FormalConjectures/ErdosProblems/7.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/7.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/7](https://www.erdosproblems.com/7).

The file states 1 research or textbook statement: 1 open.

## `Erdos7.erdos_7`

Open: stated without proof.

> Is there a covering system all of whose moduli are odd (and greater than 1)?

```lean
theorem erdos_7 :
    ∃ (C : StrictCoveringSystem ℤ), ∀ i,
      ¬ C.moduli i ≤ Ideal.span {2} ∧ C.moduli i ≠ ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/7.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/7.lean#L36).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/7.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/7.lean)
- [erdosproblems.com/7](https://www.erdosproblems.com/7)
