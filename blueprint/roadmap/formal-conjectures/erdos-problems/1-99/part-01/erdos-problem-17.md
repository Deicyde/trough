---
declaration: theorem
origin: cited
lean: Erdos17.erdos_17, Erdos17.erdos_17.variants.upper_BES, Erdos17.erdos_17.variants.upper_Elsholtz
statement: formalized
---

# Erdős Problem 17

> *Reference:* [erdosproblems.com/17](https://www.erdosproblems.com/17)

*Quoted from [FormalConjectures/ErdosProblems/17.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/17.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/17](https://www.erdosproblems.com/17).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos17.erdos_17`

Open: stated without proof.

> **Erdős Problem 17.** Are there infinitely many cluster primes?

```lean
theorem erdos_17 : {p : ℕ | IsClusterPrime p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/17.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/17.lean#L42).

## `Erdos17.erdos_17.variants.upper_BES`

Solved: stated here without proof.

> In 1999 Blecksmith, Erdős, and Selfridge [BES99] proved the upper bound
>
> $$\pi^{\mathcal{C}}(x) \ll_A x(\log x)^{-A}$$
>
> for every real $A > 0$.
>
> [BES99] Blecksmith, Richard and Erd\H os, Paul and Selfridge, J. L., Cluster primes. Amer. Math. Monthly (1999), 43--48.

```lean
theorem erdos_17.variants.upper_BES {A : ℝ} (hA : 0 < A) :
  (fun x ↦ (clusterPrimeCount x : ℝ)) =O[atTop] fun x ↦ x / (log x) ^ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/17.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/17.lean#L56).

## `Erdos17.erdos_17.variants.upper_Elsholtz`

Solved: stated here without proof.

> In 2003, Elsholtz [El03] refined the upper bound to
>
> $$\pi^{\mathcal{C}}(x) \ll x\,\exp\!\bigl(-c(\log\log x)^2\bigr)$$
>
> for every real $0 < c < 1/8$.
>
> [El03] Elsholtz, Christian, On cluster primes. Acta Arith. (2003), 281--284.

```lean
theorem erdos_17.variants.upper_Elsholtz :
  ∃ C : ℝ, 0 < C ∧
    ∀ c ∈ Set.Ioo 0 (1 / 8),
      IsBigOWith C atTop (fun x ↦ (clusterPrimeCount x : ℝ))
        (fun x ↦ x * exp (-c * (log (log x)) ^ 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/17.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/17.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/17.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/17.lean)
- [erdosproblems.com/17](https://www.erdosproblems.com/17)
