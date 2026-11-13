---
declaration: theorem
origin: cited
lean: Erdos885.erdos_885, Erdos885.erdos_885.variants.k_eq_2, Erdos885.erdos_885.variants.k_eq_3, Erdos885.erdos_885.variants.k_eq_4
statement: formalized
---

# Erdős Problem 885

> *References:*
> - [erdosproblems.com/885](https://www.erdosproblems.com/885)
> - [ErRo97] Erdős, P. and Rosenfeld, M., The factor-difference set of integers. (1997)
> - [Ji99] Jiménez-Urroz, J., A note on a conjecture of Erdős and {R}osenfeld. (1999)
> - [Br19] Bremner, A., On a problem of Erdős related to common factor differences. (2019)

*Quoted from [FormalConjectures/ErdosProblems/885.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/885](https://www.erdosproblems.com/885).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 2 API statements, counted here but not shown.

## `Erdos885.erdos_885`

Open: stated without proof.

> Is it true that, for every $k \geq 1$, there exist integers $N_1 < \dots < N_k$ such that
> $|\cap_i D(N_i)| \geq k$?

```lean
theorem erdos_885 : ∀ k ≥ 1,
    ∃ Ns : Finset ℕ,
      (∀ n ∈ Ns, 1 ≤ n) ∧
      Ns.card = k ∧
      (⋂ n ∈ Ns, factorDifferenceSet n).ncard ≥ k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/885.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean#L65).

## `Erdos885.erdos_885.variants.k_eq_2`

Proved here.

> Erdős and Rosenfeld [ErRo97] proved this is true for $k=2$.

```lean
theorem erdos_885.variants.k_eq_2 :
    ∃ Ns : Finset ℕ,
      (∀ n ∈ Ns, 1 ≤ n) ∧
      Ns.card = 2 ∧
      (⋂ n ∈ Ns, factorDifferenceSet n).ncard ≥ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/885.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean#L76).

## `Erdos885.erdos_885.variants.k_eq_3`

Proved here.

> Jiménez-Urroz [Ji99] proved this for $k=3$.

```lean
theorem erdos_885.variants.k_eq_3 :
    ∃ Ns : Finset ℕ,
      (∀ n ∈ Ns, 1 ≤ n) ∧
      Ns.card = 3 ∧
      (⋂ n ∈ Ns, factorDifferenceSet n).ncard ≥ 3
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/885.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean#L100).

## `Erdos885.erdos_885.variants.k_eq_4`

Proved here.

> Bremner [Br19] proved this for $k=4$.

```lean
theorem erdos_885.variants.k_eq_4 :
    ∃ Ns : Finset ℕ,
      (∀ n ∈ Ns, 1 ≤ n) ∧
      Ns.card = 4 ∧
      (⋂ n ∈ Ns, factorDifferenceSet n).ncard ≥ 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/885.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/885.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/885.lean)
- [erdosproblems.com/885](https://www.erdosproblems.com/885)
