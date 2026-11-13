---
declaration: theorem
origin: cited
lean: Erdos16.erdos_16, Erdos16.erdos_16.variant.romanoff, Erdos16.erdos_16.variant.erdos
statement: formalized
---

# Erdős Problem 16

> *References:*
> - [erdosproblems.com/16](https://www.erdosproblems.com/16)
> - [Ch23] Chen, Yong-Gao, A conjecture of Erdős on $p+2^k$. arXiv:2312.04120 (2023).
> - [Er50] Erdős, P., On integers of the form $2^k+p$ and some related problems. Summa Brasil. Math.
>   (1950), 113-123.
> - [Ro34] Romanoff, N. P., Über einige Sätze der additiven Zahlentheorie. Math. Ann. (1934), 668-678.

*Quoted from [FormalConjectures/ErdosProblems/16.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/16.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/16](https://www.erdosproblems.com/16).

The file states 3 research or textbook statements: 3 solved.

## `Erdos16.erdos_16`

Solved: stated here; a Lean proof is at [https://github.com/danielchin/proofs/blob/main/Proofs/ErdosProblems/Erdos16.lean](https://github.com/danielchin/proofs/blob/main/Proofs/ErdosProblems/Erdos16.lean).

> Is the set of odd integers not of the form $2^k+p$ the union of an infinite arithmetic progression
> and a set of density $0$?
>
> Erdős called this conjecture "rather silly".
>
> Chen [Ch23] has proved the answer is no.
>
> This was formalized in Lean by Chin using Aristotle.

```lean
theorem erdos_16 :
    ¬ ∃ A B : Set ℕ, Erdos16Set = A ∪ B ∧
      (∃ a d : ℕ, d > 0 ∧ A = { x | ∃ m : ℕ, x = a + m * d }) ∧
      density_zero B
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/16.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/16.lean#L63).

## `Erdos16.erdos_16.variant.romanoff`

Solved: stated here without proof.

> Romanoff [Ro34] showed that the set of odd integers of this form has positive density.

```lean
theorem erdos_16.variant.romanoff :
    let S := { n : ℕ | Odd n ∧ ∃ k p : ℕ, p.Prime ∧ n = 2 ^ k + p }
    positive_lower_density S
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/16.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/16.lean#L80).

## `Erdos16.erdos_16.variant.erdos`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos16_erdos_16_variant_erdos.lean#L103](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos16_erdos_16_variant_erdos.lean#L103).

> Using covering congruences Erdős [Er50] proved that the set of odd integers which are not of this
> form contains an infinite arithmetic progression.

```lean
theorem erdos_16.variant.erdos :
    ∃ a d : ℕ, d > 0 ∧ { x | ∃ m : ℕ, x = a + m * d } ⊆ Erdos16Set
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/16.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/16.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/16.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/16.lean)
- [erdosproblems.com/16](https://www.erdosproblems.com/16)
