---
declaration: theorem
origin: cited
lean: Erdos410.erdos_410
statement: formalized
---

# Erdős Problem 410

> *Reference:* [erdosproblems.com/410](https://www.erdosproblems.com/410)

*Quoted from [FormalConjectures/ErdosProblems/410.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/410.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/410](https://www.erdosproblems.com/410).

The file states 1 research or textbook statement: 1 open.

## `Erdos410.erdos_410`

Open: stated without proof.

> Let $σ_1(n) = σ(n)$, the sum of divisors function, and $σ_k(n) = σ(σ_{k-1}(n))$.
>
> Is it true that $\lim_{k → ∞} σ_k(n)^{\frac 1 k} = ∞$?
>
> This is problem (iii) from
> Erdos, Granville, Pomerance, Spiro
> "On the normal behavior of the iterates of some arithmetical functions"
> (page 169 of the book "Analytic Number Theory", 1990).

```lean
theorem erdos_410 : ∀ n > 1,
    Tendsto (fun k : ℕ ↦ ((sigma 1)^[k] n : ℝ) ^ (1 / (k : ℝ))) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/410.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/410.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/410.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/410.lean)
- [erdosproblems.com/410](https://www.erdosproblems.com/410)
