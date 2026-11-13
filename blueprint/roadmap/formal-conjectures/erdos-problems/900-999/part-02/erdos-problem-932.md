---
declaration: theorem
origin: cited
lean: Erdos932.erdos_932, Erdos932.erdos_932.variants.one_le
statement: formalized
---

# Erdős Problem 932

> *Reference:* [erdosproblems.com/932](https://www.erdosproblems.com/932)

*Quoted from [FormalConjectures/ErdosProblems/932.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/932.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/932](https://www.erdosproblems.com/932).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos932.erdos_932`

Open: stated without proof.

> Let $p_k$ denote the $k$th prime. For infinitely many $r$ there are at least two
> integers $p_r < n < p_{r+1}$ all of whose prime factors are $< p_{r + 1} - p_r$.

```lean
theorem erdos_932 :
    { r : ℕ | 2 ≤ (Finset.Ioo (r.nth Nat.Prime) (r.succ.nth Nat.Prime) |>.filter
      (fun m => m.maxPrimeFac < r.succ.nth Nat.Prime - r.nth Nat.Prime)).card }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/932.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/932.lean#L35).

## `Erdos932.erdos_932.variants.one_le`

Solved: stated here without proof.

> Erdős could show that the density of $r$ such that at least one such $n$ exists is $0$.

```lean
theorem erdos_932.variants.one_le :
    { r : ℕ | 1 ≤ (Finset.Ioo (r.nth Nat.Prime) (r.succ.nth Nat.Prime) |>.filter
      (fun m => m.maxPrimeFac < r.succ.nth Nat.Prime - r.nth Nat.Prime)).card }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/932.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/932.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/932.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/932.lean)
- [erdosproblems.com/932](https://www.erdosproblems.com/932)
