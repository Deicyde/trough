---
declaration: theorem
origin: cited
lean: Erdos2.erdos_2
statement: formalized
---

# Erdős Problem 2

> *References:*
> - [erdosproblems.com/2](https://www.erdosproblems.com/2)
> - [Ho15] Hough, B., *Solution of the minimum modulus problem for covering systems*. Ann. of Math.
>   (2) **181** (2015), 361-382.
> - [BBMST22] Balister, P., Bollobás, B., Morris, R., Sahasrabudhe, J. and Tiba, M., *On the Erdős
>   Covering Problem: the density of the uncovered set*. Invent. Math. **228** (2022), 377-414.
> - [PALOMAR-2026-10-05-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-05-000002&version=1)
>
> Erdős asked whether the smallest modulus in a distinct covering system can be arbitrarily large.
> Hough [Ho15] proved that the answer is no, and Balister, Bollobás, Morris, Sahasrabudhe, and Tiba
> [BBMST22] later gave a simpler proof with an improved explicit upper bound.

*Quoted from [FormalConjectures/ErdosProblems/2.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/2.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/2](https://www.erdosproblems.com/2).

The file states 1 research or textbook statement: 1 solved.

## `Erdos2.erdos_2`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/7caa4144741e10f96cf79d6f7313a0efd9a18b67/erdos-2/Solution.lean#L44](https://github.com/linrock/math-proofs/blob/7caa4144741e10f96cf79d6f7313a0efd9a18b67/erdos-2/Solution.lean#L44).

> Can the smallest modulus of a covering system be arbitrarily large?
>
> This problem has a negative answer: there is a universal bound on the least modulus of any
> distinct covering system.

```lean
theorem erdos_2 :
    ¬ ∀ B : ℕ, ∃ c : StrictCoveringSystem ℤ, ∀ i, ∃ m : ℕ,
      c.moduli i = Ideal.span {(m : ℤ)} ∧ B < m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/2.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/2.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/2.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/2.lean)
- [erdosproblems.com/2](https://www.erdosproblems.com/2)
