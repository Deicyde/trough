---
declaration: theorem
origin: cited
lean: Erdos392.erdos_392, Erdos392.erdos_392.variants.lower, Erdos392.erdos_392.variants.implication
statement: formalized
---

# Erdős Problem 392

> *Reference:* [erdosproblems.com/392](https://www.erdosproblems.com/392)

*Quoted from [FormalConjectures/ErdosProblems/392.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/392.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/392](https://www.erdosproblems.com/392).

The file states 3 research or textbook statements: 3 solved.

## `Erdos392.erdos_392`

Solved: stated here; a Lean proof is at [https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/d82a35ecc798ada27f82a88b559f25b753f63a73/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/d82a35ecc798ada27f82a88b559f25b753f63a73/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean).

> Let $A(n)$ denote the least value of $t$ such that
>
> $$
>   n! = a_1 \cdots a_t
> $$
>
> with $a_1 \leq \cdots \leq a_t\leq n^2$. Then
>
> $$
>   A(n) = \frac{n}{2} - \frac{n}{2\log n} + o\left(\frac{n}{\log n}\right).
> $$

```lean
theorem erdos_392 (A : ℕ → ℕ) (h : ∀ n > 0,
    IsLeast { t + 1 | (t) (_ : ∃ a : Fin (t + 1) → ℕ, (n)! = ∏ i, a i ∧
      Monotone a ∧ a (Fin.last t) ≤ n ^ 2) } (A n)) :
    ((fun (n : ℕ) => (A n - n / 2 + n / (2 * Real.log n) : ℝ)) =o[atTop] fun n => n / Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/392.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/392.lean#L46).

## `Erdos392.erdos_392.variants.lower`

Solved: stated here without proof.

> If we change the condition to $a_t \leq n$ it can be shown that
>
> $$
>   A(n) = n - \frac{n}{\log n} + o\left(\frac{n}{\log n}\right)
> $$

```lean
theorem erdos_392.variants.lower (A : ℕ → ℕ)
    (hA : ∀ n > 0, IsLeast
      { t + 1 | (t) (_ : ∃ a : Fin (t + 1) → ℕ, (n)! = ∏ i, a i ∧
        Monotone a ∧ a (Fin.last t) ≤ n) } (A n)) :
    (fun (n : ℕ) => (A n - n + n / Real.log n : ℝ)) =o[atTop] fun n => n / Real.log n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/392.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/392.lean#L60).

## `Erdos392.erdos_392.variants.implication`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos392_erdos_392_variants_implication.lean#L177](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos392_erdos_392_variants_implication.lean#L177).

> Cambie has observed that a positive answer follows from the result above with $a_t \leq n$, simply
> by pairing variables together, e.g. taking $a'_i = a_{2i-1}a_{2i}$ (and the lower bound follows from
> Stirling's approximation).

```lean
theorem erdos_392.variants.implication (h : type_of% erdos_392.variants.lower) :
    type_of% erdos_392
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/392.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/392.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/392.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/392.lean)
- [erdosproblems.com/392](https://www.erdosproblems.com/392)
