---
declaration: theorem
origin: cited
lean: Erdos3.erdos_3, Erdos3.erdos_3.variants.kelley_meka, Erdos3.erdos_3.variants.three, Erdos3.erdos_3.variants.green_tao, Erdos3.erdos_3.variants.gowers, Erdos3.erdos_3.variants.leng_sah_sawhney
statement: formalized
---

# Erdős Problem 3

> *References:*
> - [erdosproblems.com/3](https://www.erdosproblems.com/3)
> - [BlSi20] Bloom, Thomas F. and Sisask, Olof, *Breaking the logarithmic barrier in Roth's theorem
>   on arithmetic progressions*. arXiv:2007.03528 (2020).
> - [Go01] Gowers, W. T., *A new proof of Szemerédi's theorem*. Geom. Funct. Anal. (2001), 465-588.
> - [GrTa17] Green, Ben and Tao, Terence, *New bounds for Szemerédi's theorem, III: a
>   polylogarithmic bound for $r_4(N)$*. Mathematika (2017).
> - [KeMe23] Kelley, Zander and Meka, Raghu, *Strong bounds for 3-progressions*. 2023 IEEE 64th
>   Annual Symposium on Foundations of Computer Science (FOCS) (2023).
> - [LSS24] Leng, James, Sah, Ashwin and Sawhney, Mehtaab, *Improved bounds for Szemerédi's
>   theorem*. arXiv:2402.17995 (2024).
> - [OAI26] OpenAI, *Quasipolynomial Bounds for Arithmetic Progressions*. OpenAI Math Release
>   preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/3.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/3](https://www.erdosproblems.com/3).

The file states 6 research or textbook statements: 6 solved.

## `Erdos3.erdos_3`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Progressions/Results/Conclusions.lean#L38](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Progressions/Results/Conclusions.lean#L38).

> If $A \subset \mathbb{N}$ has $\sum_{n \in A}\frac 1 n = \infty$, then must $A$ contain arbitrarily
> long arithmetic progressions?
>
> Yes. This was proved by an internal OpenAI model in September 2026 [OAI26]; see the linked Lean
> proof.

```lean
theorem erdos_3 : ∀ A : Set ℕ,
    (¬ Summable fun a : A ↦ 1 / (a : ℝ)) →
    ∃ᶠ (k : ℕ) in Filter.atTop, ∃ S ⊆ A, S.IsAPOfLength k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L55).

## `Erdos3.erdos_3.variants.kelley_meka`

Solved: stated here without proof.

> There are $\beta > 0$ and $c > 0$ such that $r_3(N) \ll N \exp(-c (\log N)^{\beta})$.
>
> Proved by Kelley and Meka [KeMe23].

```lean
theorem erdos_3.variants.kelley_meka : ∃ β > (0 : ℝ), ∃ c > (0 : ℝ),
    (fun N ↦ (r 3 N : ℝ)) ≪ fun N : ℕ ↦ (N : ℝ) * Real.exp (-c * Real.log N ^ β)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L72).

## `Erdos3.erdos_3.variants.three`

Solved: stated here; a Lean proof assuming `erdos_3.variants.kelley_meka` is at [https://github.com/wilsonwu-ai/sundai-erdos-3/blob/8a58287a16558bf1e708eaa2d0f7cba4c86566a3/lean/Erdos3ThreeCase.lean#L96-L97](https://github.com/wilsonwu-ai/sundai-erdos-3/blob/8a58287a16558bf1e708eaa2d0f7cba4c86566a3/lean/Erdos3ThreeCase.lean#L96-L97).

> The case of $3$-term progressions: if $A \subset \mathbb{N}$ has $\sum_{n \in A}\frac 1 n = \infty$,
> then $A$ contains a non-trivial $3$-term arithmetic progression.
>
> Proved by Bloom and Sisask [BlSi20].

```lean
theorem erdos_3.variants.three : ∀ A : Set ℕ,
    (¬ Summable fun a : A ↦ 1 / (a : ℝ)) → ∃ S ⊆ A, S.IsAPOfLength 3
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L87).

## `Erdos3.erdos_3.variants.green_tao`

Solved: stated here without proof.

> There is $c > 0$ such that $r_4(N) \ll N (\log N)^{-c}$.
>
> Proved by Green and Tao [GrTa17].

```lean
theorem erdos_3.variants.green_tao : ∃ c > (0 : ℝ),
    (fun N ↦ (r 4 N : ℝ)) ≪ fun N : ℕ ↦ (N : ℝ) * Real.log N ^ (-c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L97).

## `Erdos3.erdos_3.variants.gowers`

Solved: stated here without proof.

> For every $k \geq 3$ there is $c_k > 0$ such that $r_k(N) \ll_k N (\log \log N)^{-c_k}$.
>
> Proved by Gowers [Go01].

```lean
theorem erdos_3.variants.gowers (k : ℕ) (hk : 3 ≤ k) : ∃ c > (0 : ℝ),
    (fun N ↦ (r k N : ℝ)) ≪ fun N : ℕ ↦ (N : ℝ) * Real.log (Real.log N) ^ (-c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L107).

## `Erdos3.erdos_3.variants.leng_sah_sawhney`

Solved: stated here without proof.

> For every $k \geq 5$ there is $c_k > 0$ such that $r_k(N) \ll_k N \exp(-(\log \log N)^{c_k})$.
>
> Proved by Leng, Sah and Sawhney [LSS24].

```lean
theorem erdos_3.variants.leng_sah_sawhney (k : ℕ) (hk : 5 ≤ k) : ∃ c > (0 : ℝ),
    (fun N ↦ (r k N : ℝ)) ≪
      fun N : ℕ ↦ (N : ℝ) * Real.exp (-Real.log (Real.log N) ^ c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/3.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/3.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/3.lean)
- [erdosproblems.com/3](https://www.erdosproblems.com/3)
