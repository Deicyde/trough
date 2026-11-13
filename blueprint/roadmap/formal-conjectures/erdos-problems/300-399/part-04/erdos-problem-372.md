---
declaration: theorem
origin: cited
lean: Erdos372.erdos_372
statement: formalized
---

# Erdős Problem 372

> *Reference:* [erdosproblems.com/372](https://www.erdosproblems.com/372)
>
> Conjectured by Erdős and Pomerance. Proved by Balog, who showed the stronger quantitative result
> that this holds for $\gg \sqrt{x}$ many $n\leq x$, for all large $x$.

*Quoted from [FormalConjectures/ErdosProblems/372.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/372.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/372](https://www.erdosproblems.com/372).

The file states 1 research or textbook statement: 1 solved.

## `Erdos372.erdos_372`

Solved: stated here without proof.

> Let $P(n)$ denote the largest prime factor of $n$. There are infinitely many $n$ such that
> $P(n)>P(n+1)>P(n+2)$.

```lean
theorem erdos_372 :
    {n : ℕ | Nat.maxPrimeFac n > Nat.maxPrimeFac (n + 1) ∧
      Nat.maxPrimeFac (n + 1) > Nat.maxPrimeFac (n + 2)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/372.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/372.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/372.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/372.lean)
- [erdosproblems.com/372](https://www.erdosproblems.com/372)
