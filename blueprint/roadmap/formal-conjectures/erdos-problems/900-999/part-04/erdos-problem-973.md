---
declaration: theorem
origin: cited
lean: Erdos973.erdos_973, Erdos973.erdos_973.variants.luo_yang_zhu, Erdos973.erdos_973.variants.le_one, Erdos973.erdos_973.variants.m2_bounds, Erdos973.erdos_973.variants.tang
statement: formalized
---

# Erdős Problem 973

> *References:*
> - [erdosproblems.com/973](https://www.erdosproblems.com/973)
> - [Er92f] Erdős, L., On some problems of {P}. Turán concerning power sums of
>   complex numbers. Acta Math. Hungar. (1992), 11--24.
> - [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
> - [LYZ26] Luo, Yanping and Yang, Ruiyi and Zhu, Keheng, Exterior power sums.
>   [arxiv/2607.22017](https://arxiv.org/abs/2607.22017)
> - [TWHC26] Tan, Xiaojun and Wang, Qihang and Huang, Wei and Chen, Kun, Residual bounds for
>   Schur-stable polynomials. [arxiv/2608.02043](https://arxiv.org/abs/2608.02043)
> - [Tu84b] Turán, Paul, On a new method of analysis and its applications. (1984), xvi+584.
> - [PALOMAR-2026-09-20-000008](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-20-000008&version=1)

*Quoted from [FormalConjectures/ErdosProblems/973.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/973](https://www.erdosproblems.com/973).

The file states 5 research or textbook statements: 5 solved.

## `Erdos973.erdos_973`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/1571a487465fb6a87f92dcc46f1bd71b0846c413/erdos-973/Solution.lean#L47](https://github.com/linrock/math-proofs/blob/1571a487465fb6a87f92dcc46f1bd71b0846c413/erdos-973/Solution.lean#L47).

> Does there exist a constant $C>1$ such that, for every $n\geq 2$, there exists a sequence
> $z_i\in \mathbb{C}$ with $z_1=1$ and $\lvert z_i\rvert \geq 1$ for all $1\leq i\leq n$ with
> $\max_{2\leq k\leq n+1}\left\lvert \sum_{1\leq i\leq n}z_i^k\right\rvert < C^{-n}$?
>
> This is Problem 7.3 in [Ha74], where it is attributed to Erdős.
>
> The answer is no, by Luo, Yang and Zhu [LYZ26] (and via the residual-polynomial method of Tan,
> Wang, Huang and Chen [TWHC26]): the maximum exceeds $e^{-\lambda n}$ for every fixed $\lambda>0$
> once $n$ is large, so it decays subexponentially and no such $C$ exists. See
> `erdos_973.variants.luo_yang_zhu` below.

```lean
theorem erdos_973 :
    ¬ ∃ C : ℝ, C > 1 ∧
      ∀ n : ℕ, n ≥ 2 → ∃ z : ℕ → ℂ,
        z 1 = 1 ∧
        (∀ i ∈ Icc 1 n, 1 ≤ ‖z i‖) ∧
        (∀ k ∈ Icc 2 (n + 1), ‖∑ i ∈ Icc 1 n, z i ^ k‖ < C ^ (-(n : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/973.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean#L56).

## `Erdos973.erdos_973.variants.luo_yang_zhu`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/1571a487465fb6a87f92dcc46f1bd71b0846c413/erdos-973/Solution.lean#L53](https://github.com/linrock/math-proofs/blob/1571a487465fb6a87f92dcc46f1bd71b0846c413/erdos-973/Solution.lean#L53).

> The result of [LYZ26] that settles the problem: for every fixed $\lambda>0$ and all large enough
> $n$, any $z_1,\dots,z_n$ with $\lvert z_j\rvert\geq 1$ satisfy
> $\max_{2\leq k\leq n+1}\left\lvert\sum_j z_j^k\right\rvert > e^{-\lambda n}$.
>
> This is sharper than `erdos_973.variants.tang`, whose bound $(2e)^{-(1+o(1))n}$ pins the rate at
> $\log(2e) = 1 + \log 2$, still exponential decay.

```lean
theorem erdos_973.variants.luo_yang_zhu (lam : ℝ) (hlam : 0 < lam) :
    ∀ᶠ n in atTop, ∀ z : ℕ → ℂ,
      (∀ i ∈ Icc 1 n, 1 ≤ ‖z i‖) →
      ∃ k ∈ Icc 2 (n + 1),
        Real.exp (-lam * n) < ‖∑ i ∈ Icc 1 n, z i ^ k‖
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/973.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean#L74).

## `Erdos973.erdos_973.variants.le_one`

Solved: stated here without proof.

> Erdős proved (as described on p.35 of [Tu84b]) that such a sequence does exist with
> $\lvert z_i\rvert\leq 1$. Indeed, Erdős' construction gives a value of $C\approx 1.32$.

```lean
theorem erdos_973.variants.le_one :
    ∃ C : ℝ, C > 1 ∧
      ∀ n : ℕ, n ≥ 2 → ∃ z : ℕ → ℂ,
        z 1 = 1 ∧
        (∀ i ∈ Icc 1 n, ‖z i‖ ≤ 1) ∧
        (∀ k ∈ Icc 2 (n + 1), ‖∑ i ∈ Icc 1 n, z i ^ k‖ < C ^ (-(n : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/973.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean#L86).

## `Erdos973.erdos_973.variants.m2_bounds`

Solved: stated here without proof.

> In [Er92f] (a different) Erdős refines this analysis, proving that if
> $M_2=\min_{z_j} \max_{2\leq k\leq n+1} \left\lvert \sum_{1\leq j\leq n}z_j^k\right\rvert$
> where the minimum is taken over all $z_j\in \mathbb{C}$ with $\max \lvert z_j\rvert=1$, then
> $(1.746)^{-n} < M_2 < (1.745)^{-n}$ for all sufficiently large $n$.

```lean
theorem erdos_973.variants.m2_bounds :
    ∀ᶠ n : ℕ in atTop, ∀ M_2 : ℝ,
      IsGLB { M | ∃ z : ℕ → ℂ,
        (∀ j ∈ Icc 1 n, ‖z j‖ ≤ 1) ∧
        (∃ j ∈ Icc 1 n, ‖z j‖ = 1) ∧
        (∃ k ∈ Icc 2 (n + 1), M = ‖∑ j ∈ Icc 1 n, z j ^ k‖ ∧
          ∀ m ∈ Icc 2 (n + 1), ‖∑ j ∈ Icc 1 n, z j ^ m‖ ≤ M) } M_2 →
      (1.746 : ℝ) ^ (-(n : ℝ)) < M_2 ∧ M_2 < (1.745 : ℝ) ^ (-(n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/973.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean#L101).

## `Erdos973.erdos_973.variants.tang`

Solved: stated here without proof.

> Tang notes in the comments that Theorem 6.1 of [Tu84b] implies that, if $\lvert z_i\rvert \geq 1$
> for all $i$, then
> $\max_{2\leq k\leq n+1}\left\lvert \sum_{1\leq i\leq n}z_i^k\right\rvert \geq (2e)^{-(1+o(1))n}$.

```lean
theorem erdos_973.variants.tang :
    ∃ f : ℕ → ℝ, f =o[atTop] (fun _ ↦ (1 : ℝ)) ∧
    ∀ᶠ n in atTop, ∀ z : ℕ → ℂ,
      (∀ i ∈ Icc 1 n, 1 ≤ ‖z i‖) →
      ∃ k ∈ Icc 2 (n + 1),
        ‖∑ i ∈ Icc 1 n, z i ^ k‖ ≥
        (2 * Real.exp 1) ^ (-(1 + f n) * (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/973.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/973.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/973.lean)
- [erdosproblems.com/973](https://www.erdosproblems.com/973)
