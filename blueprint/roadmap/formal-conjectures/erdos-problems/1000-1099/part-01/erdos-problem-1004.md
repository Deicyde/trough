---
declaration: theorem
origin: cited
lean: Erdos1004.erdos_1004, Erdos1004.erdos_1004.variants.le_of_isDistinctTotientRun
statement: formalized
---

# Erdős Problem 1004

> *Reference:* [erdosproblems.com/1004](https://www.erdosproblems.com/1004)

*Quoted from [FormalConjectures/ErdosProblems/1004.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1004.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1004](https://www.erdosproblems.com/1004).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1004.erdos_1004`

Open: stated without proof.

> For any fixed c > 0, if x is sufficiently large then there exists n ≤ x such that
> the values of φ(n+k) are all distinct for 1 ≤ k ≤ (log x)^c.
> This is an open problem.

```lean
theorem erdos_1004 :
    ∀ c > (0 : ℝ), ∀ᶠ x in atTop, ∃ n ≤ x,
      IsDistinctTotientRun n ⌊(Real.log (x : ℝ)) ^ c⌋₊
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1004.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1004.lean#L42).

## `Erdos1004.erdos_1004.variants.le_of_isDistinctTotientRun`

Solved: stated here without proof.

> Erdős, Pomerance, and Sárközy [EPS87] proved that if φ(n+k) are all distinct for 1 ≤ k ≤ K then
> K ≤ n / exp(c (log n)^{1/3}) for some constant c > 0.
> Here we state the existence of such a constant c.

```lean
theorem erdos_1004.variants.le_of_isDistinctTotientRun :
    ∃ (c : ℝ) (hc : c > 0),
      ∀ᶠ n in atTop, ∀ (K : ℕ), IsDistinctTotientRun n K →
        (K : ℝ) ≤ (n : ℝ) / Real.exp (c * (Real.log n) ^ (1/3 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1004.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1004.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1004.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1004.lean)
- [erdosproblems.com/1004](https://www.erdosproblems.com/1004)
