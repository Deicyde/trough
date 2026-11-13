---
declaration: theorem
origin: cited
lean: Erdos316.erdos_316, Erdos316.erdos_316.variants.multiset, Erdos316.erdos_316.variants.generalized
statement: formalized
---

# Erdős Problem 316

> *References:*
> - [erdosproblems.com/316](https://www.erdosproblems.com/316)
> - [Sa97] Sándor, Csaba, On a problem of Erdős. J. Number Theory (1997), 203-210.

*Quoted from [FormalConjectures/ErdosProblems/316.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/316.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/316](https://www.erdosproblems.com/316).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos316.erdos_316`

Proved here.

> Is it true that if $A \subseteq \mathbb{N}\setminus\{1\}$ is a finite set with
> $\sum_{n \in A} \frac{1}{n} < 2$ then there is a partition $A=A_1 \sqcup A_2$
> such that $\sum_{n \in A_i} \frac{1}{n} < 1$ for $i=1,2$?
>
> This is not true in general, as shown by Sándor [Sa97].
>
> The minimal counterexample is $\{2,3,4,5,6,7,10,11,13,14,15\}$, found by Tom Stobart.
>
> This was formalized in Lean by Mehta.

```lean
theorem erdos_316 : ¬ ∀ A : Finset ℕ, 0 ∉ A → 1 ∉ A →
    ∑ n ∈ A, (1 / n : ℚ) < 2 → ∃ (A₁ A₂ : Finset ℕ),
      Disjoint A₁ A₂ ∧ A = A₁ ∪ A₂ ∧
      ∑ n ∈ A₁, (1 / n : ℚ) < 1 ∧ ∑ n ∈ A₂, (1 / n : ℚ) <  1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/316.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/316.lean#L44).

## `Erdos316.erdos_316.variants.multiset`

Textbook result, proved here.

> This is not true if $A$ is a multiset, for example $2,3,3,5,5,5,5$.

```lean
lemma erdos_316.variants.multiset : ∃ A : Multiset ℕ, 0 ∉ A ∧ 1 ∉ A ∧
    (A.map ((1 : ℚ) / ·)).sum < 2 ∧ ∀ (A₁ A₂ : Multiset ℕ),
      A = A₁ + A₂ →
        1 ≤ (A₁.map ((1 : ℚ) / ·)).sum ∨ 1 ≤ (A₂.map ((1 : ℚ) / ·)).sum
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/316.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/316.lean#L59).

## `Erdos316.erdos_316.variants.generalized`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos316_erdos_316_variants_generalized.lean#L252](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos316_erdos_316_variants_generalized.lean#L252).

> This is not true in general, as shown by Sándor [Sa97], who observed that the proper divisors of
> $120$ form a counterexample. More generally, Sándor shows that for any $n\geq 2$ there exists a
> finite set $A\subseteq \mathbb{N}\backslash\{1\}$ with $\sum_{k\in A}\frac{1}{k} < n$ and no
> partition into $n$ parts each of which has $\sum_{k\in A_i}\frac{1}{k}<1$.
>
> A `Finpartition` has no empty parts, so partitions into at most $n$ parts are tested. Testing
> exactly $n$ parts would let the singleton $\{2\}$ satisfy the statement vacuously.

```lean
theorem erdos_316.variants.generalized (n : ℕ) (hn : 2 ≤ n) : ∃ A : Finset ℕ,
    A.Nonempty ∧ 0 ∉ A ∧ 1 ∉ A ∧ ∑ k ∈ A, (1 / k : ℚ) < n ∧ ∀ P : Finpartition A,
    P.parts.card ≤ n → ∃ p ∈ P.parts, 1 ≤ ∑ n ∈ p, (1 / n : ℚ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/316.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/316.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/316.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/316.lean)
- [erdosproblems.com/316](https://www.erdosproblems.com/316)
