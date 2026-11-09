---
declaration: theorem
origin: cited
lean: Erdos42.erdos_42, Erdos42.erdos_42.variants.constructive, Erdos42.example_maximal_sidon, Erdos42.example_difference_set, Erdos42.maximal_sidon_contains_zero
statement: formalized
---

# Erdős Problem 42: Maximal Sidon Sets and Disjoint Difference Sets

> *Reference:* [erdosproblems.com/42](https://www.erdosproblems.com/42)
>
> This problem asks whether maximal Sidon sets can coexist with other Sidon sets that have
> disjoint difference sets (apart from 0).

*Quoted from [FormalConjectures/ErdosProblems/42.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/42](https://www.erdosproblems.com/42).

The file states 5 research or textbook statements: 2 solved and 3 textbook results.

## `Erdos42.erdos_42`

Solved: stated here; a Lean proof is at [https://github.com/Shashi456/erdos-formalizations/blob/main/Erdos/P42/CompactCayley/Proof.lean](https://github.com/Shashi456/erdos-formalizations/blob/main/Erdos/P42/CompactCayley/Proof.lean).

> **Erdős Problem 42**: Let M ≥ 1 and N be sufficiently large in terms of M. Is it true that for every
> maximal Sidon set `A ⊆ {1,…,N}` there is another Sidon set `B ⊆ {1,…,N}` of size M such that
> `(A - A) ∩ (B - B) = {0}`?
>
> This was proved for all $M$ by GPT 5.5 Pro (prompted by Sandhu), see discussion thread for more details.

```lean
theorem erdos_42 :
    ∀ M ≥ 1, ∀ᶠ N in atTop, ∀ (A : Set ℕ) (_ : IsMaximalSidonSetIn A N),
    ∃ᵉ (B : Set ℕ), B ⊆ Set.Icc 1 N ∧ IsSidon B ∧ B.ncard = M ∧
    ((A - A) ∩ (B - B)) = {0}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/42.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean#L45).

## `Erdos42.erdos_42.variants.constructive`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-42-constructive-variant/blob/1f82c76be43cb56f22e2f7f792e392d5fb3ff78c/lean/Erdos42Constructive.lean](https://github.com/KitaKen1/erdos-42-constructive-variant/blob/1f82c76be43cb56f22e2f7f792e392d5fb3ff78c/lean/Erdos42Constructive.lean).

> A variant asking for explicit bounds on how large N needs to be in terms of M.
>
> This version provides a constructive function f such that for all M ≥ 1 and N ≥ f(M),
> every maximal Sidon set A ⊆ {1,…,N} has another Sidon set B ⊆ {1,…,N} of size M with
> disjoint difference sets (apart from 0).

```lean
theorem erdos_42.variants.constructive :
    ∃ (f : ℕ → ℕ), ∀ (M N : ℕ) (_ : 1 ≤ M) (_ : f M ≤ N),
    ∀ (A : Set ℕ) (_ : IsMaximalSidonSetIn A N), ∃ᵉ (B : Set ℕ),
      B ⊆ Set.Icc 1 N ∧ IsSidon B ∧ B.ncard = M ∧
      ((A - A) ∩ (B - B)) = {0}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/42.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean#L61).

## `Erdos42.example_maximal_sidon`

Textbook result, proved here.

> The set `{1, 2, 4}` is a maximal Sidon set in `{1, ..., 4}`.

```lean
theorem example_maximal_sidon : IsMaximalSidonSetIn {1, 2, 4} 4
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/42.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean#L75).

## `Erdos42.example_difference_set`

Textbook result, proved here.

> The difference set of `{1, 2, 4}` is `{0, 1, 2, 3}`.

```lean
theorem example_difference_set : ({1, 2, 4} : Set ℕ) - {1, 2, 4} = {0, 1, 2, 3}
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/42.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean#L100).

## `Erdos42.maximal_sidon_contains_zero`

Textbook result, proved here.

> For any maximal Sidon set, the difference set contains 0.

```lean
theorem maximal_sidon_contains_zero (A : Set ℕ) (N : ℕ) (hN : 1 ≤ N)
    (hA : IsMaximalSidonSetIn A N) : 0 ∈ A - A
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/42.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/42.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/42.lean)
- [erdosproblems.com/42](https://www.erdosproblems.com/42)
