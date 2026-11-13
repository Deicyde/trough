---
declaration: theorem
origin: cited
lean: Erdos286.erdos_286
statement: formalized
---

# Erdős Problem 286

> *References:*
> - [erdosproblems.com/286](https://www.erdosproblems.com/286)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Cr01] Croot, III, Ernest S., *On unit fractions with denominators in short intervals*. Acta
>   Arith. (2001), 99-114.

*Quoted from [FormalConjectures/ErdosProblems/286.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/286.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/286](https://www.erdosproblems.com/286).

The file states 1 research or textbook statement: 1 solved.

## `Erdos286.erdos_286`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos286.lean#L163](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos286.lean#L163).

> Let $k\geq 2$. Is it true that there exists an interval $I$ of width $(e-1+o(1))k$ and integers
> $n_1\lt \cdots\lt n_k\in I$ such that
>
> $$1=\frac{1}{n_1}+\cdots+\frac{1}{n_k}?$$
>
> The answer is yes, proved by Croot [Cr01].

```lean
theorem erdos_286 : ∃ o : ℕ → ℝ, Tendsto o atTop (nhds 0) ∧
    ∀ᶠ k : ℕ in atTop, ∃ a b : ℝ, b - a = (exp 1 - 1 + o k) * k ∧
      ∃ S : Finset ℕ, S.card = k ∧ 0 ∉ S ∧ ∑ n ∈ S, (1 : ℝ) / n = 1 ∧
        ∀ n ∈ S, (n : ℝ) ∈ Set.Icc a b
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/286.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/286.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/286.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/286.lean)
- [erdosproblems.com/286](https://www.erdosproblems.com/286)
