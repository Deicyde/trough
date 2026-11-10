---
declaration: theorem
origin: cited
lean: Erdos745.erdos_745, Erdos745.erdos_745.variants.supercritical, Erdos745.erdos_745.variants.noncritical_asymptotic
statement: formalized
---

# Erdős Problem 745: Second-largest component of a random graph

> *Reference:* [erdosproblems.com/745](https://www.erdosproblems.com/745)
>
> At the stated parameter $p=1/n$, the second-largest component has order
> $n^{2/3}$ in probability. The logarithmic bound applies to fixed
> $p=\lambda/n$ with $\lambda>1$.
>
> [Al97] Aldous, D., Brownian excursions, critical random graphs and the multiplicative
> coalescent. Ann. Probab. 25 (1997), 812–854.
>
> [KSS80] Komlós, J., Sulyok, M. and Szemerédi, E., Second largest component in a random
> graph. Studia Sci. Math. Hungar. 15 (1980), 391–395.

*Quoted from [FormalConjectures/ErdosProblems/745.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/745.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/745](https://www.erdosproblems.com/745).

The file states 3 research or textbook statements: 3 solved.

## `Erdos745.erdos_745`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean).

> In $G(n,1/n)$ the second-largest component has order $n^{2/3}$ in probability.
> The two positive constants may depend on the probability tolerance.

```lean
theorem erdos_745 :
    ∀ ε : ℝ, 0 < ε → ∃ c C : ℝ, 0 < c ∧ c < C ∧
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
        1 - ε ≤ criticalProbability n (fun G ↦
          c * (n : ℝ) ^ (2 / 3 : ℝ) ≤ (secondLargestComponentOrder G : ℝ) ∧
          (secondLargestComponentOrder G : ℝ) ≤ C * (n : ℝ) ^ (2 / 3 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/745.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/745.lean#L93).

## `Erdos745.erdos_745.variants.supercritical`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean).

> For fixed $\lambda>1$, every constant above
> $(\lambda-1-\log\lambda)^{-1}$ gives a logarithmic upper bound with high probability.

```lean
theorem erdos_745.variants.supercritical (lam : ℝ) (hlam : 1 < lam) (A : ℝ)
    (hA : 1 / (lam - 1 - Real.log lam) < A) :
    Filter.Tendsto (fun n : ℕ ↦ probability lam n (fun G ↦
      (secondLargestComponentOrder G : ℝ) ≤ A * Real.log (n : ℝ)))
      Filter.atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/745.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/745.lean#L106).

## `Erdos745.erdos_745.variants.noncritical_asymptotic`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos745.lean).

> For each fixed $\lambda>0$ with $\lambda\ne1$, the second-largest component size,
> divided by $\log n$, converges in probability to $(\lambda-1-\log\lambda)^{-1}$.

```lean
theorem erdos_745.variants.noncritical_asymptotic
    (lam : ℝ) (hlam : 0 < lam) (hne : lam ≠ 1) :
    ∀ ε : ℝ, 0 < ε → Filter.Tendsto (fun n : ℕ ↦ probability lam n (fun G ↦
      |(secondLargestComponentOrder G : ℝ) / Real.log (n : ℝ) -
        1 / (lam - 1 - Real.log lam)| < ε)) Filter.atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/745.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/745.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/745.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/745.lean)
- [erdosproblems.com/745](https://www.erdosproblems.com/745)
