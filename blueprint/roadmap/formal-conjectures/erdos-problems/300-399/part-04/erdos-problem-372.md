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

*Quoted from [FormalConjectures/ErdosProblems/372.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/372.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

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

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/372.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/372.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/372.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/372.lean)
- [erdosproblems.com/372](https://www.erdosproblems.com/372)
