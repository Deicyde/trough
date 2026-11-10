---
declaration: theorem
origin: cited
lean: Erdos1213.erdos_1213, Erdos1213.erdos_1213.variants.hegyvari
statement: formalized
---

# Erdős Problem 1213

> *References:*
> - [erdosproblems.com/1213](https://www.erdosproblems.com/1213)
> - [He86] Hegyvári, N., *On consecutive sums in sequences*. Acta Math. Hungar. (1986), 193-200.

*Quoted from [FormalConjectures/ErdosProblems/1213.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1213.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1213](https://www.erdosproblems.com/1213).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1213.erdos_1213`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1213.lean#L495](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1213.lean#L495).

> Let $a,K\geq 1$. Does there exist $f(a,K)$ such that if $a=a_1\lt \cdots \lt a_s$ is a sequence of
> integers with $a_s> f(a,K)$ and with bounded gaps $a_{i+1}-a_i\leq K$ then there are two distinct
> intervals $I$ and $J$ such that
>
> $$\sum_{i\in I}a_i=\sum_{j\in J}a_j?$$
>
> Hegyvári [He86] has proved the answer is yes, and gives an explicit bound of the shape
> $f(a,K) \ll ae^{O(K)}$. Hegyvári believes that the exponential dependence on $K$ here is not best
> possible.

```lean
theorem erdos_1213 : ∀ a K : ℕ, 1 ≤ a → 1 ≤ K → ∃ f : ℕ,
    ∀ (s : ℕ) (A : ℕ → ℕ), 0 < s → A 0 = a → StrictMonoOn A (Set.Iio s) →
      (∀ i, i + 1 < s → A (i + 1) - A i ≤ K) → f < A (s - 1) → HasEqualIntervalSums A s
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1213.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1213.lean#L53).

## `Erdos1213.erdos_1213.variants.hegyvari`

Solved: stated here without proof.

> Hegyvári [He86] proved that one can take $f(a,K) \ll ae^{O(K)}$.

```lean
theorem erdos_1213.variants.hegyvari : ∃ C : ℝ, 0 < C ∧ ∀ a K : ℕ, 1 ≤ a → 1 ≤ K →
    ∀ (s : ℕ) (A : ℕ → ℕ), 0 < s → A 0 = a → StrictMonoOn A (Set.Iio s) →
      (∀ i, i + 1 < s → A (i + 1) - A i ≤ K) → C * a * Real.exp (C * K) < A (s - 1) →
        HasEqualIntervalSums A s
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1213.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1213.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1213.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1213.lean)
- [erdosproblems.com/1213](https://www.erdosproblems.com/1213)
