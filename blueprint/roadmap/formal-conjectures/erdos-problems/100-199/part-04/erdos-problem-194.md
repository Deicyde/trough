---
declaration: theorem
origin: cited
lean: Erdos194.erdos_194
statement: formalized
---

# Erdős Problem 194

> *References:*
> - [erdosproblems.com/194](https://www.erdosproblems.com/194)
> - [ABJ11] Ardal, H. and Brown, T. and Jungić, V., Chaotic orderings of the rationals and reals. Amer. Math. Monthly (2011), 921-925.

*Quoted from [FormalConjectures/ErdosProblems/194.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/194](https://www.erdosproblems.com/194).

The file states 1 research or textbook statement: 1 solved.

## `Erdos194.erdos_194`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/ster-oc/ffe9e4fa1b813111f40c0e417bbe8be0/raw/6f748a76e55d47e24ca319a9c00fd20ab79422bb/Erdos194.lean](https://gist.githubusercontent.com/ster-oc/ffe9e4fa1b813111f40c0e417bbe8be0/raw/6f748a76e55d47e24ca319a9c00fd20ab79422bb/Erdos194.lean).

> Let $k\geq 3$. Must any ordering of $\mathbb{R}$ contain a monotone $k$-term arithmetic progression,
> that is, some $x_1 \lt \cdots < x_k$ which forms an increasing or decreasing $k$-term arithmetic
> progression?
>
> The answer is no, even for $k=3$, as shown by Ardal, Brown, and Jungić [ABJ11].
> -

```lean
theorem erdos_194 :
  ¬ ∀ k ≥ 3, ∀ r : ℝ → ℝ → Prop, IsStrictTotalOrder ℝ r →
    ∃ s : List ℝ, s.IsAPOfLength k ∧ (s.Pairwise r ∨ s.Pairwise (flip r))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/194.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/194.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/194.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/194.lean)
- [erdosproblems.com/194](https://www.erdosproblems.com/194)
