---
declaration: theorem
origin: cited
lean: Erdos68.erdos_68, Erdos68.sum_factorial_inv_eq_geometric
statement: formalized
---

# Erdős Problem 68

> *Reference:* [erdosproblems.com/68](https://www.erdosproblems.com/68)

*Quoted from [FormalConjectures/ErdosProblems/68.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/68.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/68](https://www.erdosproblems.com/68).

The file states 2 research or textbook statements: 1 open and 1 textbook result.

## `Erdos68.erdos_68`

Open: stated without proof.

> Is
> $$\sum_{n=2}^\infty \frac{1}{n!-1}$$
> irrational?

```lean
theorem erdos_68 :
    Irrational (∑' n : ℕ, 1 / ((n + 2).factorial - 1 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/68.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/68.lean#L36).

## `Erdos68.sum_factorial_inv_eq_geometric`

Textbook result, proved here.

> $$\sum_{n=2}^\infty \frac{1}{n!-1} = \sum_{n=2}^\infty \sum_{k=1}^\infty \frac{1}{(n!)^k}$$

```lean
theorem sum_factorial_inv_eq_geometric :
    let f (n k : ℕ) : ℝ := 1 / ((n + 2).factorial : ℝ) ^ (k + 1)
    ∑' n : ℕ, (1 : ℝ) / ((n + 2).factorial - 1) = ∑' n : ℕ, ∑' k : ℕ, f n k
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/68.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/68.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/68.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/68.lean)
- [erdosproblems.com/68](https://www.erdosproblems.com/68)
