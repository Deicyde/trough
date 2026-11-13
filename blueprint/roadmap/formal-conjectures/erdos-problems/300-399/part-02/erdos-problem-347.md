---
declaration: theorem
origin: cited
lean: Erdos347.erdos_347
statement: formalized
---

# Erdős Problem 347

> *Reference:* [erdosproblems.com/347](https://www.erdosproblems.com/347)

*Quoted from [FormalConjectures/ErdosProblems/347.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/347.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/347](https://www.erdosproblems.com/347).

The file states 1 research or textbook statement: 1 solved.

## `Erdos347.erdos_347`

Solved: stated here; a Lean proof is at [https://github.com/ebarschkis/ErdosProblem/blob/main/Problem347/Formalization.lean](https://github.com/ebarschkis/ErdosProblem/blob/main/Problem347/Formalization.lean).

> Is there a sequence $A=\{a_1\leq a_2\leq \cdots\}$ of integers with
>
> $$\lim \frac{a_{n+1}}{a_n}=2$$
>
> such that
>
> $$P(A')= \left\{\sum_{n\in B}n : B\subseteq A'\textrm{ finite }\right\}$$
>
> has density $1$ for every cofinite subsequence $A'$ of $A$?
>
> This has been solved in the affirmative by ebarschkis in the comments (based on idea of Tao and
> van Doorn, also in the comments).
>
> This was formalized in Lean by Barschkis using Aristotle.

```lean
theorem erdos_347 :
    ∃ a : ℕ → ℕ, (Monotone a) ∧
      (Tendsto (fun n ↦ (a (n + 1) : ℝ) / (a n : ℝ)) atTop (𝓝 2)) ∧
      (∀ ι : ℕ → ℕ, (range ι)ᶜ.Finite → HasDensity (𝓟 (range (a ∘ ι))) 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/347.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/347.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/347.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/347.lean)
- [erdosproblems.com/347](https://www.erdosproblems.com/347)
