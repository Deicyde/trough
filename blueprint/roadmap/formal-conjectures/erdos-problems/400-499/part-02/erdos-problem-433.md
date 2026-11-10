---
declaration: theorem
origin: cited
lean: Erdos433.erdos_433
statement: formalized
---

# Erdős Problem 433

> *References:*
> - [Erdős Problem 433](https://www.erdosproblems.com/433)
> - P. Erdős and R. L. Graham, *On a linear Diophantine problem of Frobenius*,
>   Acta Arithmetica 21 (1972), 399–408.
> - J. Dixmier, *Proof of a conjecture by Erdős and Graham on Frobenius' coin problem*,
>   Proceedings of the AMS 109 (1990), 567–577.

*Quoted from [FormalConjectures/ErdosProblems/433.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/433.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/433](https://www.erdosproblems.com/433).

The file states 1 research or textbook statement: 1 solved.

## `Erdos433.erdos_433`

Solved: stated here without proof.

> For every fixed $k \geq 2$, Erdős and Graham conjectured that
>
> $$g(k,n) \sim \frac{n^2}{k-1}.$$
>
> The conjecture was proved by Dixmier [Di90].

```lean
theorem erdos_433 : ∀ k, 2 ≤ k →
    Tendsto (fun n : ℕ => (g k n : ℝ) / ((n : ℝ) ^ 2 / ((k : ℝ) - 1))) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/433.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/433.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/433.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/433.lean)
- [erdosproblems.com/433](https://www.erdosproblems.com/433)
