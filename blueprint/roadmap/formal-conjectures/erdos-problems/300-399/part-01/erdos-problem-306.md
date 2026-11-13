---
declaration: theorem
origin: cited
lean: Erdos306.erdos_306, Erdos306.erdos_306.variants.integer_three_primes
statement: formalized
---

# Erdős Problem 306

> *References:*
> - [erdosproblems.com/306](https://www.erdosproblems.com/306)
> - [Li26] S. Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős
>   Problem 306*. arXiv:2609.32140 (2026).
> - [Ta26] [Tang, Yuren, *A Lean 4 formalisation of Erdős Problem
>   306*](https://github.com/Yuren-Tang/erdos-306), a proof modulo two Rosser–Schoenfeld axioms.

*Quoted from [FormalConjectures/ErdosProblems/306.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/306.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/306](https://www.erdosproblems.com/306).

The file states 2 research or textbook statements: 2 solved.

## `Erdos306.erdos_306`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/e1a5e2a3317007f0e31b98bf2e80383187b31238/erdos-306/Solution.lean#L34](https://github.com/linrock/math-proofs/blob/e1a5e2a3317007f0e31b98bf2e80383187b31238/erdos-306/Solution.lean#L34).

> Let $\frac a b\in \mathbb{Q}_{>0}$ with $b$ squarefree. Are there integers $1 < n_1 < \dots < n_k$,
> each the product of two distinct primes, such that $\frac{a}{b}=\frac{1}{n_1}+\cdots+\frac{1}{n_k}$?
>
> The answer is yes [Li26].

```lean
theorem erdos_306 : ∀ (q : ℚ), 0 < q → Squarefree q.den →
    ∃ k : ℕ, ∃ (n : Fin (k + 1) → ℕ), n 0 = 1 ∧ StrictMono n ∧
    (∀ i ∈ Finset.Icc 1 (Fin.last k), ω (n i) = 2 ∧ Ω (n i) = 2) ∧
    q = ∑ i ∈ Finset.Icc 1 (Fin.last k), (1 : ℚ) / (n i)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/306.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/306.lean#L48).

## `Erdos306.erdos_306.variants.integer_three_primes`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/e1a5e2a3317007f0e31b98bf2e80383187b31238/erdos-306/Solution.lean#L48](https://github.com/linrock/math-proofs/blob/e1a5e2a3317007f0e31b98bf2e80383187b31238/erdos-306/Solution.lean#L48).

> Every positive integer can be expressed as an Egyptian fraction where each denominator is the
> product of three distinct primes.

```lean
theorem erdos_306.variants.integer_three_primes (m : ℕ) (h : 0 < m) :
    ∃ k > (0 : ℕ), ∃ (n : Fin (k + 1) → ℕ), n 0 = 1 ∧
    ∀ i, (hik : i < k) → n ⟨i, by omega⟩ < n ⟨(i + 1), by omega⟩ ∧
    (∀ i ∈ Finset.Icc 1 (Fin.last k), ω (n i) = 3 ∧ Ω (n i) = 3) ∧
    m = ∑ i ∈ Finset.Icc 1 (Fin.last k), (1 : ℚ) / (n i)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/306.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/306.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/306.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/306.lean)
- [erdosproblems.com/306](https://www.erdosproblems.com/306)
