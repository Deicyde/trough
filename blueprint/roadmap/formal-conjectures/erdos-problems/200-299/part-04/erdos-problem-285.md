---
declaration: theorem
origin: cited
lean: Erdos285.erdos_285, Erdos285.erdos_285.variants.lb
statement: formalized
---

# Erdős Problem 285

> *Reference:* [erdosproblems.com/285](https://www.erdosproblems.com/285)

*Quoted from [FormalConjectures/ErdosProblems/285.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/285.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/285](https://www.erdosproblems.com/285).

The file states 2 research or textbook statements: 2 solved.

## `Erdos285.erdos_285`

Solved: stated here without proof.

> Let $f(k)$ be the minimal value of $n_k$ such that there exist $n_1 < n_2 < \dots < n_k$ with
>
> $$
>   1 = \frac{1}{n_1} + \cdots + \frac{1}{n_k}.
> $$
>
> Is it true that
>
> $$
>   f(k) = (1 + o(1)) \frac{e}{e - 1} k ?
> $$
>
> Proved by Martin [Ma00].
>
> [Ma00] Martin, Greg, _Denser Egyptian fractions_. Acta Arith. (2000), 231-260.

```lean
theorem erdos_285 :
    ∀ᵉ (f : ℕ → ℕ)
    (S : Set ℕ)
    (hS : S = {k | ∃ (n : Fin k.succ → ℕ), StrictMono n ∧ 0 ∉ Set.range n ∧
      1 = ∑ i, (1 : ℝ) / n i })
    (h : ∀ k ∈ S,
      IsLeast
        { n (Fin.last k) | (n : Fin k.succ → ℕ) (_ : StrictMono n) (_ : 0 ∉ Set.range n)
          (_ : 1 = ∑ i, (1 : ℝ) / n i) }
        (f k)),
    ∃ (o : ℕ → ℝ) (_ : o =o[atTop] (1 : ℕ → ℝ)),
      ∀ k ∈ S, f k = (1 + o k) * rexp 1 / (rexp 1 - 1) * (k + 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/285.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/285.lean#L49).

## `Erdos285.erdos_285.variants.lb`

Solved: stated here without proof.

> It is trivial that $f(k)\geq (1 + o(1)) \frac{e}{e - 1}k$.

```lean
theorem erdos_285.variants.lb (f : ℕ → ℕ)
    (S : Set ℕ)
    (hS : S = {k | ∃ (n : Fin k.succ → ℕ), StrictMono n ∧ 0 ∉ Set.range n ∧
      1 = ∑ i, (1 : ℝ) / n i })
    (h : ∀ k ∈ S,
      IsLeast
        { n (Fin.last k) | (n : Fin k.succ → ℕ) (_ : StrictMono n) (_ : 0 ∉ Set.range n)
          (_ : 1 = ∑ i, (1 : ℝ) / n i) }
        (f k)) :
    ∃ (o : ℕ → ℝ) (_ : o =o[atTop] (1 : ℕ → ℝ)),
      ∀ k ∈ S, (1 + o k) * rexp 1 / (rexp 1 - 1) * (k + 1) ≤ f k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/285.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/285.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/285.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/285.lean)
- [erdosproblems.com/285](https://www.erdosproblems.com/285)
