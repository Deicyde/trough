---
declaration: theorem
origin: cited
lean: Erdos931.erdos_931, Erdos931.erdos_931.variants.additional_condition, Erdos931.erdos_931.variants.additional_condition_nonempty, Erdos931.erdos_931.variants.exists_prime
statement: formalized
---

# Erdős Problem 931

> *Reference:* [erdosproblems.com/931](https://www.erdosproblems.com/931)

*Quoted from [FormalConjectures/ErdosProblems/931.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/931](https://www.erdosproblems.com/931).

The file states 4 research or textbook statements: 3 open and 1 solved.

## `Erdos931.erdos_931`

Open: stated without proof.

> Let $k_1 \geq k_2 \geq 3$. Are there only finitely many $n_2\geq n_1 + k_1$
> such that
>
> $$
>   \prod_{1\leq i\leq k_1}(n_1 + i)\ \text{and}\ \prod_{1\leq j\leq k_2} (n_2 + j)
> $$
>
> have the same prime factors?

```lean
theorem erdos_931 : ∀ᵉ (k₁ : ℕ) (k₂ ≥ 3), k₂ ≤ k₁ →
    { (n₁, n₂) | n₁ + k₁ ≤ n₂ ∧
      (∏ i ∈ Finset.Icc 1 k₁, (n₁ + i)).primeFactors =
      (∏ j ∈ Finset.Icc 1 k₂, (n₂ + j)).primeFactors }.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/931.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean#L39).

## `Erdos931.erdos_931.variants.additional_condition`

Open: stated without proof.

> Erdős thought perhaps if the two products have the same factors then
> $n_2 > 2(n_1 + k_1)$.
> It is an open question whether this is true when allowing a finite number of counterexamples.

```lean
theorem erdos_931.variants.additional_condition : ∀ᵉ (k₁ : ℕ) (k₂ ≥ 3), k₂ ≤ k₁ →
    {(n₁, n₂) | n₁ + k₁ ≤ n₂ ∧ n₂ ≤ 2 * (n₁ + k₁) ∧
      (∏ i ∈ Finset.Icc 1 k₁, (n₁ + i)).primeFactors =
      (∏ j ∈ Finset.Icc 1 k₂, (n₂ + j)).primeFactors}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/931.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean#L51).

## `Erdos931.erdos_931.variants.additional_condition_nonempty`

Proved here.

> In fact there exist counterexamples, like this one found by AlphaProof.

```lean
theorem erdos_931.variants.additional_condition_nonempty : ∃ (k₁ k₂ : ℕ), ∃ (_h₁ : k₂ ≤ k₁), ∃ (_h₂ : 3 ≤ k₂),
  {(n₁, n₂) | n₁ + k₁ ≤ n₂ ∧ n₂ ≤ 2 * (n₁ + k₁) ∧
      (∏ i ∈ Finset.Icc 1 k₁, (n₁ + i)).primeFactors =
      (∏ j ∈ Finset.Icc 1 k₂, (n₂ + j)).primeFactors}.Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/931.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean#L61).

## `Erdos931.erdos_931.variants.exists_prime`

Open: stated without proof.

> Erdős was unable to prove that if the two products have the same factors
> then there must exist a prime between $n_1$ and $n_2$.

```lean
theorem erdos_931.variants.exists_prime (k₁ k₂ n₁ n₂ : ℕ) (h₁ : k₂ ≤ k₁) (h₂ : 3 ≤ k₂)
    (h₃ : n₁ + k₁ ≤ n₂) (h₄ : (∏ i ∈ Finset.Icc 1 k₁, (n₁ + i)).primeFactors =
      (∏ j ∈ Finset.Icc 1 k₂, (n₂ + j)).primeFactors) :
    ∃ (p : ℕ), p.Prime ∧ n₁ ≤ p ∧ p ≤ n₂
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/931.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/931.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/931.lean)
- [erdosproblems.com/931](https://www.erdosproblems.com/931)
