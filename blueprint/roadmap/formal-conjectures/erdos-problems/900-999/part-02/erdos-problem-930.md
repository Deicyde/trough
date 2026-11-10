---
declaration: theorem
origin: cited
lean: Erdos930.erdos_930, Erdos930.erdos_930.variants.consecutive_strong, Erdos930.erdos_930.variants.consecutive_integers
statement: formalized
---

# Erdős Problem 930

> *Reference:* [erdosproblems.com/930](https://www.erdosproblems.com/930)

*Quoted from [FormalConjectures/ErdosProblems/930.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/930.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/930](https://www.erdosproblems.com/930).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos930.erdos_930`

Open: stated without proof.

> Is it true that, for every $r$, there is a $k$ such that
> if $I_1,\ldots,I_r$ are disjoint intervals of consecutive integers,
> all of length at least $k$, then
>
> $$
>   \prod_{1\leq i\leq r}\prod_{m\in I_i}m
> $$
>
> is not a perfect power?

```lean
theorem erdos_930 :
    ∀ r > 0, ∃ k, ∀ I₁ I₂ : Fin r → ℕ,
      (∀ i : Fin r, 0 < I₁ i ∧ I₁ i + k ≤ I₂ i + 1) →
        (∀ i j : Fin r, i < j → I₂ i < I₁ j) →
          ¬ IsPower (∏ i : Fin r, ∏ m ∈ Icc (I₁ i) (I₂ i), m)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/930.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/930.lean#L49).

## `Erdos930.erdos_930.variants.consecutive_strong`

Solved: stated here without proof.

> Let $k$, $l$, $n$ be integers such that $k \ge 3$, $l \ge 2$ and $n + k \ge p^{(k)}$,
> where $p^{(k)}$ is the least prime satisfying $p^{(k)} \ge k$.
> Then there is a prime $p \ge k$ for which $l$ does not divide
> the multiplicity of the prime factor $p$ in $(n + 1) \ldots (n + k)$.
>
> Theorem 2 from [ErSe75].
>
> [ErSe75] Erdős, P. and Selfridge, J. L., The product of consecutive integers is never a power. Illinois J. Math. (1975), 292-301.

```lean
theorem erdos_930.variants.consecutive_strong :
    ∀ k l n, 3 ≤ k → 2 ≤ l → nextPrime k ≤ n + k →
      ∃ p, k ≤ p ∧ p.Prime ∧
        ¬ (l ∣ Nat.factorization (∏ m ∈ Icc (n + 1) (n + k), m) p)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/930.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/930.lean#L73).

## `Erdos930.erdos_930.variants.consecutive_integers`

Solved: stated here without proof.

> Erdos and Selfridge [ErSe75] proved that the product of
> consecutive integers is never a power (establishing the case $r=1$).
>
> Theorem 1 from [ErSe75].
>
> It is implied from `erdos_930.variants.consecutive_strong`.
>
> [ErSe75] Erdős, P. and Selfridge, J. L., The product of consecutive integers is never a power. Illinois J. Math. (1975), 292-301.

```lean
theorem erdos_930.variants.consecutive_integers :
    ∀ n k, 0 ≤ n → 2 ≤ k →
      ¬ IsPower (∏ m ∈ Icc (n + 1) (n + k), m)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/930.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/930.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/930.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/930.lean)
- [erdosproblems.com/930](https://www.erdosproblems.com/930)
