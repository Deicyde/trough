---
declaration: theorem
origin: cited
lean: Erdos690.erdos_690, Erdos690.erdos_690.variants.hasDensity, Erdos690.erdos_690.variants.cambie_unimodal, Erdos690.erdos_690.variants.cambie_not_unimodal, Erdos690.erdos_690.variants.large_k
statement: formalized
---

# Erdős Problem 690

> *References:*
> - [erdosproblems.com/690](https://www.erdosproblems.com/690)
> - [Er79e] Erdős, Paul, _Some unconventional problems in number theory_. Astérisque (1979), 73-82.
> - [Ca25] S. Cambie, _Resolution of Erdős' problems about unimodularity_. arXiv:2501.10333 (2025).
> - [WC26] S. Wang and D. Crapis, _A Complete Answer to Erdős Problem 690_. arXiv:2605.08542 (2026).

*Quoted from [FormalConjectures/ErdosProblems/690.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/690](https://www.erdosproblems.com/690).

The file states 5 research or textbook statements: 5 solved.

## `Erdos690.erdos_690`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162).

> Let $d_k(p)$ be the density of those integers whose $k$th smallest prime factor is $p$ (i.e. if
> $p_1\lt p_2\lt \cdots$ are the primes dividing $n$ then $p_k=p$).
>
> For fixed $k\geq 1$ is $d_k(p)$ unimodular in $p$? That is, it first increases in $p$ until its
> maximum then decreases.
>
> The answer is no in general: Cambie [Ca25] has shown that $d_k(p)$ is unimodular for
> $1\leq k\leq 3$ and is not unimodular for $4\leq k\leq 20$.
>
> The densities $d_k(p)$ exist (see `erdos_690.variants.hasDensity`), so the statement quantifies
> over any function `d` recording them.

```lean
theorem erdos_690 :
    ¬ ∀ k ≥ 1, ∀ d : ℕ → ℝ,
      (∀ p, p.Prime → (kthPrimeFactorSet k p).HasDensity (d p)) → IsUnimodalOnPrimes d
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/690.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean#L63).

## `Erdos690.erdos_690.variants.hasDensity`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162).

> For every $k\geq 1$ and prime $p$, the set of integers whose $k$th smallest prime factor is
> $p$ has a natural density.

```lean
theorem erdos_690.variants.hasDensity (k p : ℕ) (hk : 1 ≤ k) (hp : p.Prime) :
    ∃ δ : ℝ, (kthPrimeFactorSet k p).HasDensity δ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/690.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean#L73).

## `Erdos690.erdos_690.variants.cambie_unimodal`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162).

> Cambie [Ca25] has shown that $d_k(p)$ is unimodular for $1\leq k\leq 3$.

```lean
theorem erdos_690.variants.cambie_unimodal (k : ℕ) (hk : 1 ≤ k) (hk' : k ≤ 3)
    (d : ℕ → ℝ) (hd : ∀ p, p.Prime → (kthPrimeFactorSet k p).HasDensity (d p)) :
    IsUnimodalOnPrimes d
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/690.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean#L81).

## `Erdos690.erdos_690.variants.cambie_not_unimodal`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos690.lean#L2162).

> Cambie [Ca25] has shown that $d_k(p)$ is not unimodular for $4\leq k\leq 20$.

```lean
theorem erdos_690.variants.cambie_not_unimodal (k : ℕ) (hk : 4 ≤ k) (hk' : k ≤ 20)
    (d : ℕ → ℝ) (hd : ∀ p, p.Prime → (kthPrimeFactorSet k p).HasDensity (d p)) :
    ¬ IsUnimodalOnPrimes d
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/690.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean#L90).

## `Erdos690.erdos_690.variants.large_k`

Solved: stated here without proof.

> Is $d_k(p)$ unimodular for any $k\geq 21$?
>
> The answer is no: $d_k(p)$ is not unimodal for any $k \geq 4$ [WC26] (arXiv preprint).

```lean
theorem erdos_690.variants.large_k :
    ¬ ∃ k ≥ 21, ∀ d : ℕ → ℝ,
      (∀ p, p.Prime → (kthPrimeFactorSet k p).HasDensity (d p)) → IsUnimodalOnPrimes d
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/690.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/690.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/690.lean)
- [erdosproblems.com/690](https://www.erdosproblems.com/690)
