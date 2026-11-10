---
declaration: theorem
origin: cited
lean: Erdos287.erdos_287, Erdos287.erdos_287.variants.gap_at_least_two, Erdos287.erdos_287.variants.prime_conjecture, Erdos287.erdos_287.variants.prime_conjecture_implies
statement: formalized
---

# Erdős Problem 287

> *Reference:* [erdosproblems.com/287](https://www.erdosproblems.com/287)

*Quoted from [FormalConjectures/ErdosProblems/287.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/287](https://www.erdosproblems.com/287).

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `Erdos287.erdos_287`

Open: stated without proof.

> Let $k\geq2$. Is it true that, for any distinct integers
> $1 < n_1 < \cdots < n_k$ such that $\sum_{i=1}^k \frac{1}{n_i} = 1$,
> we must have $\max(n_{i+1} - n_i) \geq 3$?

```lean
theorem erdos_287 :
    ∀ (k : ℕ) (hk : 2 ≤ k) (s : Fin k → ℕ),
    StrictMono s → 1 < s ⟨0, by omega⟩ →
    ∑ i : Fin k, 1/ (s i : ℝ) = 1 →
    3 ≤ max_gap k s
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/287.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean#L43).

## `Erdos287.erdos_287.variants.gap_at_least_two`

Solved: stated here; a Lean proof is at [https://github.com/Zed-Rez/erdos-287-lean/blob/8bf27b1915ffbd155f071acbc57ba223451dc8ef/P287/gap_full.lean#L276-L281](https://github.com/Zed-Rez/erdos-287-lean/blob/8bf27b1915ffbd155f071acbc57ba223451dc8ef/P287/gap_full.lean#L276-L281).

> The lower bound of $\geq 2$ is equivalent to saying that $1$ is not the sum of reciprocals of
> consecutive integers, proved by Erdős [Er32].

```lean
theorem erdos_287.variants.gap_at_least_two :
    ∀ (k : ℕ) (_ : 2 ≤ k) (s : Fin k → ℕ),
    StrictMono s → 1 < s ⟨0, by omega⟩ →
    ∑ i : Fin k, 1 / (s i : ℝ) = 1 →
    2 ≤ max_gap k s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/287.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean#L58).

## `Erdos287.erdos_287.variants.prime_conjecture`

Open: stated without proof.

> For all large $N$, there exists a prime $p \in [N, 2N]$ such that $\frac{p+1}{2}$ is also prime.
>
> This is an open conjecture. If true, it would imply `erdos_287` for all but at most finitely
> many exceptions (see `erdos_287.variants.prime_conjecture_implies`).

```lean
theorem erdos_287.variants.prime_conjecture :
    ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N →
      ∃ p : ℕ, Nat.Prime p ∧ N ≤ p ∧ p ≤ 2 * N ∧ Nat.Prime ((p + 1) / 2)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/287.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean#L92).

## `Erdos287.erdos_287.variants.prime_conjecture_implies`

Textbook result, stated without proof. A Lean proof is at [https://github.com/Zed-Rez/erdos-287-lean/blob/43c2ef1c8f534d1c7547b1e18310daacba936083/P287/Part3.lean#L39-L47](https://github.com/Zed-Rez/erdos-287-lean/blob/43c2ef1c8f534d1c7547b1e18310daacba936083/P287/Part3.lean#L39-L47).

> The conjecture `erdos_287` would follow for all but at most finitely many exceptions if it were
> known that, for all large $N$, there exists a prime $p \in [N, 2N]$ such that $\frac{p+1}{2}$
> is also prime.
>
> More precisely: if the prime conjecture holds, then there exists $k_0$ such that for all
> $k \geq k_0$, any Egyptian fraction representation of $1$ with $k$ terms and all terms $> 1$
> must have $\max(n_{i+1} - n_i) \geq 3$.

```lean
theorem erdos_287.variants.prime_conjecture_implies : type_of% erdos_287.variants.prime_conjecture →
    ∃ (k₀ : ℕ), ∀ᵉ (k : ℕ) (hk₀ : k₀ ≤ k) (hk : 2 ≤ k) (s : Fin k → ℕ),
      StrictMono s → 1 < s ⟨0, by omega⟩ →
      ∑ i : Fin k, 1 / (s i : ℝ) = 1 →
      3 ≤ max_gap k s
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/287.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean#L109).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/287.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/287.lean)
- [erdosproblems.com/287](https://www.erdosproblems.com/287)
