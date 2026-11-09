---
declaration: theorem
origin: cited
lean: Erdos46.erdos_46, Erdos46.erdos_46.variants.infinitely_many_disjoint, Erdos46.erdos_46.variants.positive_rat
statement: formalized
---

# Erdős Problem 46

> *References:*
> - [erdosproblems.com/46](https://www.erdosproblems.com/46)
> - [Cr03] Croot, III, Ernest S., *On a coloring conjecture about unit fractions*. Ann. of Math. (2)
>   (2003), 545-556.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).

*Quoted from [FormalConjectures/ErdosProblems/46.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/46.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/46](https://www.erdosproblems.com/46).

The file states 3 research or textbook statements: 3 solved.

## `Erdos46.erdos_46`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos46.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos46.lean).

> Does every finite colouring of the integers have a monochromatic solution to
> $1=\sum \frac{1}{n_i}$ with $2\leq n_1\lt \cdots \lt n_k$?
>
> The answer is yes, as proved by Croot [Cr03] - indeed, there are infinitely many disjoint such
> monochromatic solutions.

```lean
theorem erdos_46 :
    -- For any finite colouring of the integers
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite →
      -- there are integers `2 ≤ n₁ < ⋯ < n_k`
      ∃ S : Finset ℕ, (∀ n ∈ S, 2 ≤ n) ∧
        -- whose reciprocals sum to `1`
        ∑ n ∈ S, (1 / n : ℚ) = 1 ∧
        -- and which all have the same colour
        (𝓒 '' (S : Set ℕ)).Subsingleton
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/46.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/46.lean#L44).

## `Erdos46.erdos_46.variants.infinitely_many_disjoint`

Solved: stated here without proof.

> Croot [Cr03] proved more: there are infinitely many disjoint such monochromatic solutions.

```lean
theorem erdos_46.variants.infinitely_many_disjoint :
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite →
      ∃ S : ℕ → Finset ℕ, (∀ i j, i ≠ j → Disjoint (S i) (S j)) ∧
        ∀ i, (∀ n ∈ S i, 2 ≤ n) ∧ ∑ n ∈ S i, (1 / n : ℚ) = 1 ∧
          (𝓒 '' (S i : Set ℕ)).Subsingleton
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/46.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/46.lean#L59).

## `Erdos46.erdos_46.variants.positive_rat`

Solved: stated here without proof.

> In [ErGr80] they also ask for a monochromatic representation of any $\frac{a}{b}>0$.

```lean
theorem erdos_46.variants.positive_rat :
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite → ∀ q : ℚ, 0 < q →
      ∃ S : Finset ℕ, (∀ n ∈ S, 2 ≤ n) ∧ ∑ n ∈ S, (1 / n : ℚ) = q ∧
        (𝓒 '' (S : Set ℕ)).Subsingleton
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/46.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/46.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/46.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/46.lean)
- [erdosproblems.com/46](https://www.erdosproblems.com/46)
