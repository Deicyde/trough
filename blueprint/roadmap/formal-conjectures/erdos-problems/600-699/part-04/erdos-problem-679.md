---
declaration: theorem
origin: cited
lean: Erdos679.erdos_679.parts.i, Erdos679.erdos_679.parts.ii
statement: formalized
---

# Erdős Problem 679

> *References:*
> - [erdosproblems.com/679](https://www.erdosproblems.com/679)
> - [Er79d] P. Erdős, Some unconventional problems in number theory.
>   Acta Math. Acad. Sci. Hungar. 33 (1979), 71–80.

*Quoted from [FormalConjectures/ErdosProblems/679.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/679.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/679](https://www.erdosproblems.com/679).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos679.erdos_679.parts.i`

Open: stated without proof.

> Let $\epsilon>0$ and $\omega(n)$ count the number of distinct prime factors of $n$.
> Are there infinitely many values of $n$ such that
>
> $$\omega(n-k) < (1+\epsilon)\frac{\log k}{\log\log k}$$
>
> for all $k\lt n$ which are sufficiently large depending on $\epsilon$ only?

```lean
theorem erdos_679.parts.i :
    ∀ ε : ℝ, 0 < ε → ∃ K : ℕ, ∃ᶠ n : ℕ in atTop,
      ∀ k : ℕ, K < k → k < n →
        (ArithmeticFunction.cardDistinctFactors (n - k) : ℝ) <
          (1 + ε) * log k / log (log k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/679.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/679.lean#L42).

## `Erdos679.erdos_679.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/AItoBit/erdos-679-additive-refutation/blob/4a53d358d1b7ade35d6f696f501c99b4d88c9e4c/Solution.lean](https://github.com/AItoBit/erdos-679-additive-refutation/blob/4a53d358d1b7ade35d6f696f501c99b4d88c9e4c/Solution.lean).

> Can one show the stronger version with
>
> $$\omega(n-k) < \frac{\log k}{\log\log k}+O(1)$$
>
> is false?
>
> DottedCalculator disproved this strengthening. For every additive constant $C$ and cutoff $K$,
> all sufficiently large $n$ admit $K\lt k\lt n$ violating the bound.

```lean
theorem erdos_679.parts.ii (C : ℝ) (K : ℕ) :
    ∀ᶠ n : ℕ in atTop, ∃ k < n, K < k ∧
      log (k : ℝ) / log (log k) + C ≤
        (ArithmeticFunction.cardDistinctFactors (n - k) : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/679.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/679.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/679.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/679.lean)
- [erdosproblems.com/679](https://www.erdosproblems.com/679)
