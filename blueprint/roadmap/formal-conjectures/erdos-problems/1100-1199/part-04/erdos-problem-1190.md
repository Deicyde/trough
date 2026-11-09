---
declaration: theorem
origin: cited
lean: Erdos1190.erdos_1190, Erdos1190.erdos_1190.variants.lt_one, Erdos1190.erdos_1190.variants.tendsto_zero, Erdos1190.erdos_1190.variants.lower_bound, Erdos1190.erdos_1190.variants.upper_bound
statement: formalized
---

# Erdős Problem 1190

> *References:*
> - [erdosproblems.com/1190](https://www.erdosproblems.com/1190)
> - [BFV13] de la Bretèche, Régis and Ford, Kevin and Vandehey, Joseph, *On non-intersecting
>   arithmetic progressions*. Acta Arith. (2013), 381-392.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.

*Quoted from [FormalConjectures/ErdosProblems/1190.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1190](https://www.erdosproblems.com/1190).

The file states 5 research or textbook statements: 5 solved.

## `Erdos1190.erdos_1190`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1190.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1190.lean).

> Let
> $$\epsilon_m=\max \sum \frac{1}{n_i}$$
> where the maximum is taken over all finite sequences $m\lt n_1\lt \cdots\lt n_k$ for which there exist
> congruences $a_i\pmod{n_i}$ such that no integer satisfies two such congruences.
>
> Estimate $\epsilon_m$.
>
> The resolution of [202] by GPT-5.4 Pro implies via the same reduction that
> $$\epsilon_m=L(m)^{-1+o(1)},$$
> where $L(m)=\exp(\sqrt{\log m\log\log m})$.

```lean
theorem erdos_1190 : ∀ ε : ℝ, 0 < ε → ∀ᶠ m : ℕ in atTop,
    scaleL m ^ (-1 - ε : ℝ) < eps m ∧ eps m < scaleL m ^ (-1 + ε : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1190.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean#L63).

## `Erdos1190.erdos_1190.variants.lt_one`

Solved: stated here without proof.

> Erdős [Er80] seems to credit Mirsky and Newman with the result that $\epsilon_m<1$, but gives no
> reference.

```lean
theorem erdos_1190.variants.lt_one (m : ℕ) (hm : 1 ≤ m) (S : Finset ℕ) (a : ℕ → ℤ)
    (hS : ∀ n ∈ S, m < n)
    (hdisj : ∀ n ∈ S, ∀ n' ∈ S, n ≠ n' → ¬ ∃ x : ℤ, x ≡ a n [ZMOD n] ∧ x ≡ a n' [ZMOD n']) :
    (∑ n ∈ S, (n : ℝ)⁻¹) < 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1190.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean#L72).

## `Erdos1190.erdos_1190.variants.tendsto_zero`

Solved: stated here without proof.

> He could not even decide whether $\epsilon_m\to 0$ as $m\to \infty$.

```lean
theorem erdos_1190.variants.tendsto_zero : Tendsto eps atTop (𝓝 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1190.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean#L82).

## `Erdos1190.erdos_1190.variants.lower_bound`

Solved: stated here without proof.

> The work of de la Bretèche, Ford, and Vandehey [BFV13] implies
> $$L(m)^{-1+o(1)}< \epsilon_m < L(m)^{-\sqrt{3}/2+o(1)},$$
> where $L(m)=\exp(\sqrt{\log m\log\log m})$. The lower bound is implicit in their construction.

```lean
theorem erdos_1190.variants.lower_bound : ∀ ε : ℝ, 0 < ε → ∀ᶠ m : ℕ in atTop,
    scaleL m ^ (-1 - ε : ℝ) < eps m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1190.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean#L91).

## `Erdos1190.erdos_1190.variants.upper_bound`

Solved: stated here without proof.

> The work of de la Bretèche, Ford, and Vandehey [BFV13] implies
> $$L(m)^{-1+o(1)}< \epsilon_m < L(m)^{-\sqrt{3}/2+o(1)},$$
> where $L(m)=\exp(\sqrt{\log m\log\log m})$. The upper bound follows immediately from their upper
> bound as reported in [202] and partial summation.

```lean
theorem erdos_1190.variants.upper_bound : ∀ ε : ℝ, 0 < ε → ∀ᶠ m : ℕ in atTop,
    eps m < scaleL m ^ (-(sqrt 3 / 2) + ε : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1190.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1190.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1190.lean)
- [erdosproblems.com/1190](https://www.erdosproblems.com/1190)
