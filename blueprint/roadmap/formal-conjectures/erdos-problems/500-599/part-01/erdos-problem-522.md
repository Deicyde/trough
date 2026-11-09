---
declaration: theorem
origin: cited
lean: Erdos522.erdos_522, Erdos522.erdos_522.variants.zero_one, Erdos522.erdos_522.variants.number_real_roots, Erdos522.erdos_522.variants.yakir_solution
statement: formalized
---

# Erdős Problem 522

> *References:*
> - [erdosproblems.com/522](https://www.erdosproblems.com/522)
> - [Ch26] Chojecki, P., *A strong law for the roots of random Littlewood polynomials* (2026),
>   [ulam.ai/research/erdos522-final.pdf](https://www.ulam.ai/research/erdos522-final.pdf).
> - [Ka26] Kawada, S., *Almost-Sure Radial Laws for Nested Random Polynomials and Erdős
>   Problem #522*, [doi:10.5281/zenodo.22970145](https://zenodo.org/records/22970145) (2026).
>   Lean 4 formalization: [chreia/erdos-522](https://github.com/chreia/erdos-522).
> - [Ki26] Kitamura, K., *A Lean proof of Erdős Problem 522*,
>   [KitaKen1/erdos-522-strong-law](https://github.com/KitaKen1/erdos-522-strong-law) (2026).
> - [KZ26] Kwon, Y. and Zou, J., *A fourth moment estimate for logarithmic integrals of random
>   Littlewood polynomials and Erdős's root-count problem* (2026),
>   [ykwon0407/erdos-521-522](https://github.com/ykwon0407/erdos-521-522).

*Quoted from [FormalConjectures/ErdosProblems/522.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/522](https://www.erdosproblems.com/522).

The file states 4 research or textbook statements: 4 solved.

## `Erdos522.erdos_522`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-522-strong-law/blob/9374493206d192708ef50f90f2752aa0dc690e16/lean/Erdos522StrongLawFC.lean#L9086-L9089](https://github.com/KitaKen1/erdos-522-strong-law/blob/9374493206d192708ef50f90f2752aa0dc690e16/lean/Erdos522StrongLawFC.lean#L9086-L9089); a Lean proof is at [https://github.com/chreia/erdos-522/blob/b3c1d7c089fcada59cc48cf664cd3d02157407ca/lean/Erdos522/Probability/IndependentCoefficientRadialLaws.lean#L39-L47](https://github.com/chreia/erdos-522/blob/b3c1d7c089fcada59cc48cf664cd3d02157407ca/lean/Erdos522/Probability/IndependentCoefficientRadialLaws.lean#L39-L47); a Lean proof is at [https://github.com/chreia/erdos-522/blob/57af1556d1b40f37d09d1270495acc0f282ff0fc/lean/Erdos522/Bridge/FormalConjectures.lean#L238-L253](https://github.com/chreia/erdos-522/blob/57af1556d1b40f37d09d1270495acc0f282ff0fc/lean/Erdos522/Bridge/FormalConjectures.lean#L238-L253).

> Let $f(z)=\sum_{0\leq k\leq n} \epsilon_k z^k$ be a random polynomial, where
> $\epsilon_k\in \{-1,1\}$ independently uniformly at random for $0\leq k\leq n$.
>
> Is it true that, if $R_n$ is the number of roots of $f(z)$ in
> $\{ z\in \mathbb{C} : \lvert z\rvert \leq 1\}$, then
> $$
>   \frac{R_n}{n/2}\to 1
> $$
> almost surely?
>
> There is some ambiguity as to whether the intended coefficient set is $\{-1, 1\}$ or $\{0, 1\}$,
> see `erdos_522.variants.zero_one` for the alternate version.
>
> This is true. Proofs were posted on the erdosproblems.com forum in April 2026 [Ch26], [KZ26],
> and Lean proofs were given independently in September 2026 [Ka26], [Ki26].
>
> More generally, [Ka26] proves an almost-sure radial law: the number of roots in
> $\{\lvert z\rvert \le 1 + x/n\}$ is $\Phi(x)\,n + o(n)$ for every $x$, where
> $\Phi(x) = \tfrac12\left(1 + \coth x - \tfrac1x\right)$. This problem is the case $x = 0$.

```lean
theorem erdos_522 :
    ∀ {Ω : Type*} [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
      (c : KacCoefficients ({-1, 1} : Set ℂ) Ω),
      ℙ {ω | atTop.Tendsto (fun n : ℕ ↦ (2 * c.numRootsInUnitDisk n ω : ℝ) / n) (𝓝 1)} = 1
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/522.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean#L127).

## `Erdos522.erdos_522.variants.zero_one`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-522-strong-law/blob/9374493206d192708ef50f90f2752aa0dc690e16/lean/Erdos522StrongLawFC.lean#L9101-L9104](https://github.com/KitaKen1/erdos-522-strong-law/blob/9374493206d192708ef50f90f2752aa0dc690e16/lean/Erdos522StrongLawFC.lean#L9101-L9104).

> Let $f(z)=\sum_{0\leq k\leq n} \epsilon_k z^k$ be a random polynomial, where
> $\epsilon_k\in \{0,1\}$ independently uniformly at random for $0\leq k\leq n$.
>
> Is it true that, if $R_n$ is the number of roots of $f(z)$ in
> $\{ z\in \mathbb{C} : \lvert z\rvert \leq 1\}$, then
> $$
>   \frac{R_n}{n/2}\to 1
> $$
> almost surely?
>
> This is true; a Lean proof is given in [Ki26].

```lean
theorem erdos_522.variants.zero_one :
    ∀ {Ω : Type*} [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
      {n : ℕ} (hn : 1 ≤ n) (f : KacCoefficients ({0, 1} : Set ℂ) Ω),
      ℙ {ω | atTop.Tendsto (fun n : ℕ ↦ (2 * f.numRootsInUnitDisk n ω : ℝ) / n) (𝓝 1)} = 1
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/522.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean#L150).

## `Erdos522.erdos_522.variants.number_real_roots`

Solved: stated here without proof.

> Erdős and Offord showed that the number of real roots of a random degree `n` polynomial with `±1`
> coefficients is `(2/π+o(1))log n`.

```lean
theorem erdos_522.variants.number_real_roots : ∃ p o : ℕ → ℝ,
    atTop.Tendsto o (𝓝 0) ∧ atTop.Tendsto p (𝓝 0) ∧
    ∀ (Ω : Type*) [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
      (n : ℕ) (hn : 2 ≤ n) (f : KacCoefficients ({-1, 1} : Set ℝ) Ω),
      (ℙ {ω | |(f.roots n ω).card / (n : ℝ).log - 2 / π| ≥ o n}).toReal ≤ p n
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/522.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean#L161).

## `Erdos522.erdos_522.variants.yakir_solution`

Solved: stated here without proof.

> Yakir proved that almost all Kac polynomials have `n/2+O(n^(9/10))` many roots in `{z∈C:|z|≤1}`.

```lean
theorem erdos_522.variants.yakir_solution :
    ∃ p : ℕ → ℝ, atTop.Tendsto p (𝓝 0) ∧
    ∀ (Ω : Type*) [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
      (n : ℕ) (hn : 2 ≤ n) (f : KacCoefficients ({-1, 1} : Set ℂ) Ω),
       (ℙ {ω | |(f.roots n ω).countP
         (· ∈ Metric.closedBall 0 1) - (n / 2 : ℝ)| ≥ n^(9/10 : ℝ) }).toReal ≤ p n
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/522.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean#L173).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/522.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/522.lean)
- [erdosproblems.com/522](https://www.erdosproblems.com/522)
