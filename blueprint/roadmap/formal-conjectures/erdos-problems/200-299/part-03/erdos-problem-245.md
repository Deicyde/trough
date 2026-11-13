---
declaration: theorem
origin: cited
lean: Erdos245.erdos_245, Erdos245.erdos_245.variants.two
statement: formalized
---

# Erdős Problem 245

> *Reference:* [erdosproblems.com/245](https://www.erdosproblems.com/245)

*Quoted from [FormalConjectures/ErdosProblems/245.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/245.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/245](https://www.erdosproblems.com/245).

The file states 2 research or textbook statements: 2 solved.

## `Erdos245.erdos_245`

Solved: stated here without proof.

> Let $A\subseteq\mathbb{N}$ be an infinite set such that $|A\cap \{1, ..., N\}| = o(N)$.
> Is it true that
>
> $$
> \limsup_{N\to\infty}\frac{|(A + A)\cap \{1, ..., N\}|}{|A \cap \{1, ..., N\}|} \geq 3?
> $$
>
> The answer is yes, proved by Freiman [Fr73].
>
> [Fr73] Fre\u{\i}man, G. A., _Foundations of a structural theory of set addition_. (1973), vii+108.

```lean
theorem erdos_245 :
    ∀ (A : Set ℕ), A.Infinite →
      atTop.Tendsto (fun N ↦ (A ∩ Icc 1 ⌊N⌋₊ |>.ncard : ℝ) / N) (𝓝 0) →
      3 ≤ atTop.limsup
        fun N : ℝ ↦ ((A + A) ∩ Icc 1 ⌊N⌋₊ |>.ncard : EReal)
          / (A ∩ Icc 1 ⌊N⌋₊).ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/245.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/245.lean#L46).

## `Erdos245.erdos_245.variants.two`

Solved: stated here without proof.

> Let $A\subseteq\mathbb{N}$ be an infinite set such that $|A\cap \{1, ..., N\}| = o(N)$.
> Then
>
> $$
> \limsup_{N\to\infty}\frac{|(A + A)\cap \{1, ..., N\}|}{|A \cap \{1, ..., N\}|} \geq 2.
> $$

```lean
theorem erdos_245.variants.two (A : Set ℕ) (h_inf : A.Infinite)
    (hf : atTop.Tendsto (fun N ↦ (A ∩ Icc 1 ⌊N⌋₊ |>.ncard : ℝ) / N) (𝓝 0)) :
    2 ≤ atTop.limsup
      fun N : ℝ ↦ ((A + A) ∩ Icc 1 ⌊N⌋₊ |>.ncard : EReal)
        / (A ∩ Icc 1 ⌊N⌋₊).ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/245.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/245.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/245.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/245.lean)
- [erdosproblems.com/245](https://www.erdosproblems.com/245)
