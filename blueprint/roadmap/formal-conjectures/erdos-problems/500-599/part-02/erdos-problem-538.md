---
declaration: theorem
origin: cited
lean: Erdos538.erdos_538, Erdos538.erdos_538.matching_order
statement: formalized
---

# Erdős Problem 538

> *Reference:* [erdosproblems.com/538](https://www.erdosproblems.com/538)

*Quoted from [FormalConjectures/ErdosProblems/538.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/538.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/538](https://www.erdosproblems.com/538).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos538.erdos_538`

Open: stated without proof.

> Let $r\geq 2$ and suppose that $A\subseteq\{1,\ldots,N\}$ is such that, for any
> $m$, there are at most $r$ solutions to $m=pa$ where $p$ is prime and $a\in A$.
> Give the best possible upper bound for $\sum_{n\in A}\frac{1}{n}$.
>
> Erdős observed that $\sum_{n\in A}\frac{1}{n}\ll r\frac{\log N}{\log\log N}$, and the
> order `Θ_r(log N / loglog N)` is known (see `erdos_538.matching_order`). The best possible
> upper bound is the asymptotic size of the largest reciprocal sum `maxMass r N` over
> admissible `A`.

```lean
theorem erdos_538 :
    ∀ r : ℕ, 2 ≤ r → maxMass r ~[atTop] erdos_538.answer r
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/538.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/538.lean#L61).

## `Erdos538.erdos_538.matching_order`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-538/Research/FinalMatchingOrder.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-538/Research/FinalMatchingOrder.lean).

> The reciprocal sum has matching order `Θ_r(log N / loglog N)`: an explicit
> upper bound for every admissible `A`, together with a witnessing construction
> achieving the same order. This pins the order (up to the one iterated-logarithm
> factor) but not the best possible upper bound asked for in `erdos_538`.

```lean
theorem erdos_538.matching_order (r N : ℕ) (hr : 2 ≤ r) (hN : 2 ≤ N) :
    (∀ A : Finset ℕ, Admissible r N A →
      Real.log (Real.log (N + 1)) * (reciprocalMass A : ℝ) ≤
        2 * r * (1 + Real.log (N * N))) ∧
    (∃ A : Finset ℕ, Admissible r N A ∧
      Real.log (N + 1) ≤
        4 + (8192 * (Nat.log 2 (Nat.log 2 N) + 1) : ℝ) * (reciprocalMass A : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/538.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/538.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/538.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/538.lean)
- [erdosproblems.com/538](https://www.erdosproblems.com/538)
