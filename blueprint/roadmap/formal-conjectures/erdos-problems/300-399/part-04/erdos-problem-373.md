---
declaration: theorem
origin: cited
lean: Erdos373.erdos_373, Erdos373.erdos_373.variants.of_limit, Erdos373.erdos_373.variants.of_lower_bound, Erdos373.erdos_373.variants.maximal_solution, Erdos373.erdos_373.variants.suranyi
statement: formalized
---

# Erdős Problem 373

> *Reference:* [erdosproblems.com/373](https://www.erdosproblems.com/373)

*Quoted from [FormalConjectures/ErdosProblems/373.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/373](https://www.erdosproblems.com/373).

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Erdos373.erdos_373`

Open: stated without proof.

> Show that the equation `n!=a_1!a_2!···a_k!`, with `n−1 > a_1 ≥ a_2 ≥ ··· ≥ a_k`, has
> only finitely many solutions.

```lean
theorem erdos_373 : S.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/373.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean#L45).

## `Erdos373.erdos_373.variants.of_limit`

Solved: stated here without proof.

> Show that if `P(n(n+1)) / log n → ∞` where `P(m)` denotes the largest prime factor of `m`, then
> the equation `n!=a_1!a_2!···a_k!`, with `n−1 > a_1 ≥ a_2 ≥ ··· ≥ a_k`, has only
> finitely many solutions.

```lean
theorem erdos_373.variants.of_limit
    (H : Filter.atTop.Tendsto (fun (n : ℕ) => (n*(n+1)).maxPrimeFac / (n : ℝ).log) Filter.atTop) :
    S.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/373.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean#L54).

## `Erdos373.erdos_373.variants.of_lower_bound`

Solved: stated here without proof.

> Show that if `P(n(n−1)) > 4 log n` for large enough `n`, where `P(m)` denotes the
> largest prime factor of `m`, then the equation `n!=a_1!a_2!···a_k!`, with
> `n−1 > a_1 ≥ a_2 ≥ ··· ≥ a_k`, has only finitely many solutions.

```lean
theorem erdos_373.variants.of_lower_bound
    (H : ∀ᶠ (n : ℕ) in Filter.atTop, 4*(n : ℝ).log < (n*(n-1 : ℕ)).maxPrimeFac) :
    S.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/373.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean#L71).

## `Erdos373.erdos_373.variants.maximal_solution`

Open: stated without proof.

> Hickerson conjectured the largest solution the equation `n!=a_1!a_2!···a_k!`, with
> `n−1 > a_1 ≥ a_2 ≥ ··· ≥ a_k`, is `16!=14!5!2!`.

```lean
theorem erdos_373.variants.maximal_solution :
    (16, [14, 5, 2]) ∈ S ∧ ∀ s ∈ S, s.fst ≤ 16
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/373.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean#L81).

## `Erdos373.erdos_373.variants.suranyi`

Open: stated without proof.

> Surányi was the first to conjecture that the only non-trivial solution to `a!b!=n!`
> is `6!7!=10!`.

```lean
theorem erdos_373.variants.suranyi :
    {(n, a, b) : ℕ × ℕ × ℕ | n ! = a ! * b ! ∧ 1 < n ∧ 1 < a ∧ 1 < b ∧ b ≤ a ∧ a + 1 ≠ n}
      = {(10, 7, 6)}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/373.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/373.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/373.lean)
- [erdosproblems.com/373](https://www.erdosproblems.com/373)
