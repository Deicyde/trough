---
declaration: theorem
origin: cited
lean: Erdos234.erdos_234
statement: formalized
---

# Erdős Problem 234

> *Reference:* [erdosproblems.com/234](https://www.erdosproblems.com/234)

*Quoted from [FormalConjectures/ErdosProblems/234.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/234.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/234](https://www.erdosproblems.com/234).

The file states 1 research or textbook statement: 1 open.

## `Erdos234.erdos_234`

Open: stated without proof.

> Is it true that for all `c ≥ 0`, the density `f c` of integers for which
> `(p (n + 1) - p n) / log n < c` exists and is a continuous function of `c`?

```lean
theorem erdos_234 : ∃ f : ℝ≥0 → ℝ, Continuous f ∧
    ∀ c : ℝ≥0, HasDensity {n : ℕ | primeGap n / log n < c} (f c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/234.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/234.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/234.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/234.lean)
- [erdosproblems.com/234](https://www.erdosproblems.com/234)
