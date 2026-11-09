---
declaration: theorem
origin: cited
lean: Erdos260.erdos_260
statement: formalized
---

# Erdős Problem 260

> *References:*
> - [erdosproblems.com/260](https://www.erdosproblems.com/260)
> - [Wang, *Sparse Polynomial-Weighted Expansions*]
>   (https://arxiv.org/abs/2606.24972)

*Quoted from [FormalConjectures/ErdosProblems/260.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/260.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/260](https://www.erdosproblems.com/260).

The file states 1 research or textbook statement: 1 solved.

## `Erdos260.erdos_260`

Solved: stated here; a Lean proof is at [https://github.com/Hanziwww/erdos260/blob/1f2baf4547f2c2805cdd160611b0b983f43941aa/Erdos260/DeepMind.lean#L92-L132](https://github.com/Hanziwww/erdos260/blob/1f2baf4547f2c2805cdd160611b0b983f43941aa/Erdos260/DeepMind.lean#L92-L132).

> Let $a_1 < a_2 < \cdots$ be an increasing sequence such that $\frac{a_n}{n} \to \infty$.
> Is the sum $\sum_{n}^{\infty} \frac{a_n}{2^{a_n}}$ irrational?
>
> For a proof, see [Wang, *Sparse Polynomial-Weighted Expansions*]
> (https://arxiv.org/abs/2606.24972).

```lean
theorem erdos_260 :
                  ∀ a : ℕ → ℤ, ∀ s : ℝ,
                  StrictMono a →
                  Tendsto (fun n => (a n : ℝ ) / n ) atTop atTop →
                  HasSum (fun n => (a n : ℝ ) / 2 ^ a n) s → Irrational s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/260.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/260.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/260.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/260.lean)
- [erdosproblems.com/260](https://www.erdosproblems.com/260)
