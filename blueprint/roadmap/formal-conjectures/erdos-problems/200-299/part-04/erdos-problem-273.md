---
declaration: theorem
origin: cited
lean: Erdos273.erdos_273, Erdos273.erdos_273.variants.three
statement: formalized
---

# Erdős Problem 273

> *Reference:* [erdosproblems.com/273](https://www.erdosproblems.com/273)

*Quoted from [FormalConjectures/ErdosProblems/273.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/273.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/273](https://www.erdosproblems.com/273).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos273.erdos_273`

Open: stated without proof.

> Is there a covering system all of whose moduli are of the form $p-1$ for some primes $p \geq 5$?

```lean
theorem erdos_273 : ∃ c : StrictCoveringSystem ℤ, ∀ i, ∃ (p : ℕ), p.Prime ∧ 5 ≤ p ∧
    c.moduli i = Ideal.span {↑(p - 1)}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/273.lean, line 33](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/273.lean#L33).

## `Erdos273.erdos_273.variants.three`

Solved: stated here without proof.

> Is there a covering system all of whose moduli are of the form $p-1$ for some primes $p \geq 3$?

```lean
theorem erdos_273.variants.three : ∃ c : StrictCoveringSystem ℕ, ∀ i, ∃ p, p.Prime ∧ 3 ≤ p ∧
    c.moduli i = Ideal.span {↑(p - 1)}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/273.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/273.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/273.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/273.lean)
- [erdosproblems.com/273](https://www.erdosproblems.com/273)
