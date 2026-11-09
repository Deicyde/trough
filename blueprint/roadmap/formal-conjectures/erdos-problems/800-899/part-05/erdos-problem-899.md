---
declaration: theorem
origin: cited
lean: Erdos899.erdos_899
statement: formalized
---

# Erdős Problem 899

> *Reference:* [erdosproblems.com/899](https://www.erdosproblems.com/899)

*Quoted from [FormalConjectures/ErdosProblems/899.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/899.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/899](https://www.erdosproblems.com/899).

The file states 1 research or textbook statement: 1 solved.

## `Erdos899.erdos_899`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos899.lean#L793](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos899.lean#L793).

> Let $A\subseteq\mathbb{N}$ be an infinite set such that $|A\cap \{1, ..., N\}| = o(N)$.
> Is it true that
>
> $$
> \limsup_{N\to\infty}\frac{|(A - A)\cap \{1, ..., N\}|}{|A \cap \{1, ..., N\}|} = \infty?
> $$
>
> The answer is yes, proved by Ruzsa [Ru78].
>
> [Ru78] Ruzsa, I. Z., _On the cardinality of {$A+A$}\ and {$A-A$}_. (1978), 933--938.

```lean
theorem erdos_899 : ∀ (A : Set ℕ), A.Infinite →
    Tendsto (fun N => (A ∩ Icc 1 N |>.ncard : ℝ) / N) atTop (𝓝 0) →
    atTop.limsup (fun N => ((A - A : Set ℕ) ∩ Icc 1 N |>.ncard : EReal) /
      (A ∩ Icc 1 N).ncard) = ⊤
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/899.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/899.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/899.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/899.lean)
- [erdosproblems.com/899](https://www.erdosproblems.com/899)
