---
declaration: theorem
origin: cited
lean: Erdos44.maxSidonSubsetCard_icc_bound, Erdos44.erdos_44, Erdos44.erdos_44.variants.empty_start, Erdos44.example_sidon_set, Erdos44.sidon_set_lower_bound, Erdos44.greedy_sidon_construction
statement: formalized
---

# Erdős Problem 44: Extending Sidon Sets

> *References:*
> - [erdosproblems.com/44](https://www.erdosproblems.com/44)
> - [Si38] Singer, James, A theorem in finite projective geometry and some applications to number
>   theory. Trans. Amer. Math. Soc. (1938), 377--385.

*Quoted from [FormalConjectures/ErdosProblems/44.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/44](https://www.erdosproblems.com/44).

The file states 6 research or textbook statements: 1 open, 1 solved and 4 textbook results.

## `Erdos44.maxSidonSubsetCard_icc_bound`

Textbook result, proved here.

> The maximum size of a Sidon set in `{1, ..., N}` is less than or equal to `2 * √N`.

```lean
theorem maxSidonSubsetCard_icc_bound (N : ℕ) (hN : 1 ≤ N) :
    maxSidonSubsetCard (Icc 1 N) ≤ 2 * Real.sqrt N
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L38).

## `Erdos44.erdos_44`

Open: stated without proof.

> **Erdős Problem 44:** Let N ≥ 1 and `A ⊆ {1,…,N}` be a Sidon set. Is it true that, for any ε > 0,
> there exist M = M(ε) and `B ⊆ {N+1,…,M}` such that `A ∪ B ⊆ {1,…,M}` is a Sidon set
> of size at least `(1−ε)M^{1/2}`?
>
> This problem asks whether any Sidon set can be extended to achieve a density
> arbitrarily close to the optimal density for Sidon sets.

```lean
theorem erdos_44 : ∀ᵉ (N ≥ (1 : ℕ)) (A ⊆ Finset.Icc 1 N), IsSidon (A : Set ℕ) →
    ∀ᵉ (ε > (0 : ℝ)), ∃ᵉ (M > N) (B ⊆ Finset.Icc (N + 1) M),
      IsSidon (A ∪ B : Set ℕ) ∧ (1 - ε) * Real.sqrt M ≤ (A ∪ B).card
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L92).

## `Erdos44.erdos_44.variants.empty_start`

Solved: stated here without proof.

> The case where we start with an empty set (constructing large Sidon sets).
>
> The answer is yes. Singer [Si38] constructed Sidon sets of size $q + 1$ in
> $\{1, \ldots, q^2 + q + 1\}$ for every prime $q$. Since $p_{n+1}/p_n \to 1$ for consecutive primes,
> this gives Sidon sets of size $(1 - o(1))M^{1/2}$ in $\{1, \ldots, M\}$ for every $M$; see
> [erdosproblems.com/30](https://www.erdosproblems.com/30).

```lean
theorem erdos_44.variants.empty_start : ∀ᵉ (ε > (0 : ℝ)), ∀ᶠ (M : ℕ) in Filter.atTop,
    ∃ᵉ (A ⊆ Finset.Icc 1 M), IsSidon (A : Set ℕ) ∧ (1 - ε) * Real.sqrt M ≤ A.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L106).

## `Erdos44.example_sidon_set`

Textbook result, proved here.

> The set `{1, 2, 4, 8, 13}` is a Sidon set in `{1, ..., 13}`.

```lean
theorem example_sidon_set : IsSidon ({1, 2, 4, 8, 13} : Set ℕ)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L116).

## `Erdos44.sidon_set_lower_bound`

Textbook result, stated without proof.

> For any `N`, there exists a Sidon set of size at least `√N/2`.

```lean
theorem sidon_set_lower_bound (N : ℕ) (hN : 1 ≤ N) :
    ∃ᵉ (A ⊆ Finset.Icc 1 N), IsSidon (A : Set ℕ) ∧ Real.sqrt N / 2 ≤ A.card
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L129).

## `Erdos44.greedy_sidon_construction`

Textbook result, stated without proof.

> The greedy construction gives a Sidon set `A ⊆ {1, ..., N}` of size at least $N^{1/3}$,
> stated here as $N \le |A|^3$. See Section 1 of [arXiv:2103.15850](https://arxiv.org/abs/2103.15850).

```lean
theorem greedy_sidon_construction (N : ℕ) (hN : 1 ≤ N) :
    ∃ᵉ (A ⊆ Finset.Icc 1 N), IsSidon (A : Set ℕ) ∧ N ≤ A.card ^ 3
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/44.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/44.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/44.lean)
- [erdosproblems.com/44](https://www.erdosproblems.com/44)
