---
declaration: theorem
origin: cited
lean: Erdos663.erdos_663
statement: formalized
---

# Erdős Problem 663

> *References:*
> - [erdosproblems.com/663](https://www.erdosproblems.com/663)
> - [BEGL96] Burr, S. A., Erdős, P., Graham, R. L., and Li, W. W.-C.,
>   *Complete sequences of sets of integer powers*. Acta Arith. (1996), 133–138.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*.
>   Math. Japon. (1997), 527–537.

*Quoted from [FormalConjectures/ErdosProblems/663.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/663.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/663](https://www.erdosproblems.com/663).

The file states 1 research or textbook statement: 1 open.

## `Erdos663.erdos_663`

Open: stated without proof.

> Let $k \geq 2$, and let $q(n,k)$ denote the least prime which does not divide
> $\prod_{1 \leq i \leq k}(n+i)$. Is it true that, if $k$ is fixed and $n$ is sufficiently
> large, then $q(n,k) < (1+o(1))\log n$?

```lean
theorem erdos_663 : ∀ k ≥ 2, ∃ error : ℕ → ℝ,
    error =o[atTop] (fun _ ↦ (1 : ℝ)) ∧ ∀ᶠ n in atTop,
      let P : ℕ := ∏ i ∈ Finset.Icc 1 k, (n + i)
      ∃ q : ℕ, q.Prime ∧ ¬ q ∣ P ∧ (∀ p : ℕ, p.Prime → ¬ p ∣ P → q ≤ p) ∧
        (q : ℝ) < (1 + error n) * Real.log n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/663.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/663.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/663.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/663.lean)
- [erdosproblems.com/663](https://www.erdosproblems.com/663)
