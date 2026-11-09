---
declaration: theorem
origin: cited
lean: Erdos283.erdos_283, Erdos283.erdos_283.variants.graham, Erdos283.erdos_283.variants.graham_alpha, Erdos283.erdos_283.variants.cassels, Erdos283.erdos_283.variants.burr, Erdos283.erdos_283.variants.alekseyev, Erdos283.erdos_283.variants.van_doorn_linear, Erdos283.erdos_283.variants.van_doorn_quadratic
statement: formalized
---

# Erdős Problem 283

> *References:*
> - [erdosproblems.com/283](https://www.erdosproblems.com/283)
> - [Al19] Alekseyev, Max A., On partitions into squares of distinct integers whose
> reciprocals sum to 1. (2019), 213--221.
> - [Ca60] Cassels, J. W. S., On the representation of integers as the sums of distinct summands taken from a fixed set. Acta Sci. Math. (Szeged) (1960), 111-124.
> - [Gr63] Graham, R. L., A theorem on partitions. J. Austral. Math. Soc. (1963), 435-441.
> - [vD25] W. van Doorn, Partitions with prescribed sum of rationals: asymptotic bounds. arXiv:2502.02200 (2025).

*Quoted from [FormalConjectures/ErdosProblems/283.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/283](https://www.erdosproblems.com/283).

The file states 8 research or textbook statements: 8 solved.

## `Erdos283.erdos_283`

Solved: stated here; a Lean proof is at [https://github.com/Shashi456/erdos-formalizations/blob/286f856aa3fc08957b80950fd18a45aab8d045ea/Erdos/P283/Proof_flat.lean#L9738-L9746](https://github.com/Shashi456/erdos-formalizations/blob/286f856aa3fc08957b80950fd18a45aab8d045ea/Erdos/P283/Proof_flat.lean#L9738-L9746).

> Let $p\colon \mathbb{Z} \rightarrow \mathbb{Z}$ be a polynomial (with rational coefficients,
> taking integer values at all integers) whose leading coefficient is positive and such that there
> exists no $d≥2$ with $d ∣ p(n)$ for all $n≥1$. Is it true that,
> for all sufficiently large $m$, there exist integers $1≤n_1\lt \dots < n_k$ such that
> $$1=\frac{1}{n_1}+\cdots+\frac{1}{n_k}$$
> and
> $$m=p(n_1)+\cdots+p(n_k)$$?
>
> GPT 5.5 Pro (prompted by Price) has given a proof that the answer is yes, for the stronger version
> with $1$ replaced by any rational $\alpha>0$.
>
> This was formalized in Lean by Ammanamanchi using Opus 4.6 and GPT 5.5 Pro.

```lean
theorem erdos_283 : ∀ p : ℚ[X], Condition p
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L67).

## `Erdos283.erdos_283.variants.graham`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos283_erdos_283_variants_graham.lean#L383](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos283_erdos_283_variants_graham.lean#L383).

> Graham [Gr63] has proved this when $p(x)=x$.

```lean
theorem erdos_283.variants.graham : Condition X
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L75).

## `Erdos283.erdos_283.variants.graham_alpha`

Solved: stated here without proof.

> Graham also conjectures that this remains true with $1$ replaced by an arbitrary rational $\alpha>0$
> (provided $m$ is taken sufficiently large depending on $\alpha$).

```lean
theorem erdos_283.variants.graham_alpha :
  ∀ (p : ℚ[X]) (α : ℚ),
    (∀ n : ℤ, ∃ z : ℤ, p.eval (n : ℚ) = z) →
    0 < p.leadingCoeff →
    (¬ ∃ (d : ℤ), d ≥ 2 ∧ ∀ (n : ℤ), n ≥ 1 → ∃ z : ℤ, p.eval (n : ℚ) = d * z) →
    α > 0 →
    ∀ᶠ (m : ℕ) in atTop,
      ∃ S : Finset ℕ, (∀ n ∈ S, 1 ≤ n) ∧
        (∑ n ∈ S, (1 / (n : ℚ))) = α ∧
        (∑ n ∈ S, p.eval (n : ℚ)) = (m : ℚ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L83).

## `Erdos283.erdos_283.variants.cassels`

Solved: stated here without proof.

> Cassels [Ca60] has proved that these conditions on the polynomial imply every sufficiently large
> integer is the sum of $p(n_i)$ with distinct $n_i$.

```lean
theorem erdos_283.variants.cassels :
  ∀ (p : ℚ[X]),
    (∀ n : ℤ, ∃ z : ℤ, p.eval (n : ℚ) = z) →
    0 < p.leadingCoeff →
    (¬ ∃ (d : ℤ), d ≥ 2 ∧ ∀ (n : ℤ), n ≥ 1 → ∃ z : ℤ, p.eval (n : ℚ) = d * z) →
    ∀ᶠ (m : ℕ) in atTop,
      ∃ S : Finset ℕ, (∀ n ∈ S, 1 ≤ n) ∧
        (∑ n ∈ S, p.eval (n : ℚ)) = (m : ℚ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L100).

## `Erdos283.erdos_283.variants.burr`

Solved: stated here without proof.

> Burr has proved this if $p(x)=x^k$ with $k\geq 1$ and if we allow $n_i=n_j$.

```lean
theorem erdos_283.variants.burr :
  ∀ (k : ℕ), k ≥ 1 →
    ∀ᶠ (m : ℕ) in atTop,
      ∃ M : Multiset ℕ, (∀ n ∈ M, 1 ≤ n) ∧
        (M.map (fun n ↦ 1 / (n : ℚ))).sum = 1 ∧
        (M.map (fun n ↦ (n : ℤ)^k)).sum = (m : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L114).

## `Erdos283.erdos_283.variants.alekseyev`

Solved: stated here without proof.

> Alekseyev [Al19] has proved this when $p(x)=x^2$, for all $m>8542$.

```lean
theorem erdos_283.variants.alekseyev :
  ∀ (m : ℕ), m > 8542 →
    ∃ S : Finset ℕ, (∀ n ∈ S, 1 ≤ n) ∧
      (∑ n ∈ S, (1 / (n : ℚ))) = 1 ∧
      (∑ n ∈ S, (n : ℤ)^2) = (m : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L126).

## `Erdos283.erdos_283.variants.van_doorn_linear`

Solved: stated here without proof.

> van Doorn [vD25] has investigated the question of what 'sufficiently large' means for $p(x)=x$.
> van Doorn has also proved the original conjecture for many linear and quadratic polynomials.
> For example, if $p(x) = x + b$ with $1 \leq b \leq 5000$, then the conjecture is true.

```lean
theorem erdos_283.variants.van_doorn_linear :
  ∀ b : ℤ, 1 ≤ b → b ≤ 5000 → Condition (X + C (b : ℚ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L139).

## `Erdos283.erdos_283.variants.van_doorn_quadratic`

Solved: stated here without proof.

> van Doorn [vD25] has proved the original conjecture for many linear and quadratic polynomials.
> For example, if $p(x) = x^2 + b$ with $1 \leq b \leq 800$, then the conjecture is true.

```lean
theorem erdos_283.variants.van_doorn_quadratic :
  ∀ b : ℤ, 1 ≤ b → b ≤ 800 → Condition (X^2 + C (b : ℚ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/283.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean#L148).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/283.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/283.lean)
- [erdosproblems.com/283](https://www.erdosproblems.com/283)
