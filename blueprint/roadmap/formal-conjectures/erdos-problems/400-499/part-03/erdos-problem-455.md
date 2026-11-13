---
declaration: theorem
origin: cited
lean: Erdos455.erdos_455, Erdos455.erdos_455.variants.liminf
statement: formalized
---

# Erdős Problem 455

> *References:*
>  - [erdosproblems.com/455](https://www.erdosproblems.com/455)
>  - [Ri76] Richter, Bernd, Über die Monotonie von Differenzenfolgen. Acta Arith. (1976), 225-227.

*Quoted from [FormalConjectures/ErdosProblems/455.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/455.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/455](https://www.erdosproblems.com/455).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos455.erdos_455`

Open: stated without proof.

> Let `q : ℕ → ℕ` be a strictly increasing sequence of primes such that
> `q (n + 2) - q (n + 1) ≥ q (n + 1) - q n`. Must `lim q n / (n ^ 2) = ∞`?

```lean
theorem erdos_455: ∀ q : ℕ → ℕ, StrictMono q →
    (∀ n, (q n).Prime ∧ q (n + 2) - q (n + 1) ≥ q (n + 1) - q n) →
    Tendsto (fun n : ℕ => (q n : ℝ) / n ^ 2) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/455.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/455.lean#L36).

## `Erdos455.erdos_455.variants.liminf`

Solved: stated here without proof.

> Let `q : ℕ → ℕ` be a strictly increasing sequence of primes such that
> `q (n + 2) - q (n + 1) ≥ q (n + 1) - q n`. Then `liminf q n / (n ^ 2) > 0.352`, and this is proved in
> [Ri76].

```lean
theorem erdos_455.variants.liminf : ∀ q : ℕ → ℕ, StrictMono q →
    (∀ n, (q n).Prime ∧ q (n + 2) - q (n + 1) ≥ q (n + 1) - q n) →
    liminf (fun n : ℕ => (q n : ℝ≥0∞) / n ^ 2) atTop > 0.352
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/455.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/455.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/455.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/455.lean)
- [erdosproblems.com/455](https://www.erdosproblems.com/455)
