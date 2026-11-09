---
declaration: theorem
origin: cited
lean: NowhereDenseSpectralSet.exists_nowhereDense_spectralSet, SpectralSetProduct.isSpectral_right_of_product_one_dimensional, SpectralSetProduct.isSpectral_right_of_product_two_dimensional, SpectralSetProduct.isSpectral_right_of_product_three_dimensional, SpectralSetProduct.isSpectral_right_of_product_of_convexBody
statement: formalized
---

# Spectral sets and weak tiling

> This file formalizes Problems 7.1 and 7.2 from Kolountzakis, Lev, and Matolcsi.
>
> *References:*
> - [KLM2023] Mihail N. Kolountzakis, Nir Lev, and Máté Matolcsi,
>   [Spectral sets and weak tiling](https://arxiv.org/abs/2209.04540).
> - [GL16] Rachel Greenfeld and Nir Lev, Spectrality and tiling by cylindric domains,
>   *Journal of Functional Analysis* 271 (2016), 2808–2821.
> - [GL20] Rachel Greenfeld and Nir Lev, Spectrality of product domains and Fuglede's conjecture
>   for convex polytopes, *Journal d'Analyse Mathématique* 140 (2020), 409–441.
> - [Ki26] Kenta Kitamura, A Lean proof of Problem 7.2 of Kolountzakis–Lev–Matolcsi in dimension
>   three, [GitHub repository](https://github.com/KitaKen1/klm-7-2-spectral-product-3d) (2026).

*Quoted from [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `NowhereDenseSpectralSet.exists_nowhereDense_spectralSet`

Open: stated without proof.

> [KLM2023, Problem 7.1] asks whether a bounded, measurable, nowhere dense subset
> $\Omega \subset \mathbb{R}^d$ of positive measure can be spectral. The answer is known to be
> negative for $d = 1$, so the dimension is restricted to $d \ge 2$, where the problem is open.

```lean
theorem exists_nowhereDense_spectralSet :
    ∃ d : ℕ, 2 ≤ d ∧
      ∃ Ω : Set (Fin d → ℝ), Bornology.IsBounded Ω ∧ MeasurableSet Ω ∧
        IsNowhereDense Ω ∧ 0 < volume Ω ∧ isSpectral Ω
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean#L48).

## `SpectralSetProduct.isSpectral_right_of_product_one_dimensional`

Solved: stated here without proof.

> [KLM2023, Problem 7.2; GL16] For a one-dimensional convex body $A$ and a bounded,
> measurable set $B$, if $A \times B$ is spectral, then $B$ is spectral.

```lean
theorem isSpectral_right_of_product_one_dimensional :
    ∀ (m : ℕ), 0 < m → spectralProductImpliesRightSpectral 1 m
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean#L79).

## `SpectralSetProduct.isSpectral_right_of_product_two_dimensional`

Solved: stated here without proof.

> [KLM2023, Problem 7.2; GL20] For a two-dimensional convex body $A$ and a bounded,
> measurable set $B$, if $A \times B$ is spectral, then $B$ is spectral.

```lean
theorem isSpectral_right_of_product_two_dimensional :
    ∀ (m : ℕ), 0 < m → spectralProductImpliesRightSpectral 2 m
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean#L88).

## `SpectralSetProduct.isSpectral_right_of_product_three_dimensional`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/klm-7-2-spectral-product-3d/blob/2874890904e117df17d8abf1dd27254eebfb2829/lean/SpectralProduct3DFC.lean#L20962-L20966](https://github.com/KitaKen1/klm-7-2-spectral-product-3d/blob/2874890904e117df17d8abf1dd27254eebfb2829/lean/SpectralProduct3DFC.lean#L20962-L20966).

> [KLM2023, Problem 7.2] For a three-dimensional convex body $A$ and a bounded,
> measurable set $B$, must spectrality of $A \times B$ imply spectrality of $B$?
>
> The answer is yes. For the Lean proof, see [Ki26].

```lean
theorem isSpectral_right_of_product_three_dimensional :
    ∀ (m : ℕ), 0 < m → spectralProductImpliesRightSpectral 3 m
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean#L102).

## `SpectralSetProduct.isSpectral_right_of_product_of_convexBody`

Open: stated without proof.

> [KLM2023, Problem 7.2] For every positive dimension $n$, a convex body $A$ and a bounded,
> measurable set $B$, must spectrality of $A \times B$ imply spectrality of $B$?

```lean
theorem isSpectral_right_of_product_of_convexBody :
    ∀ (n m : ℕ), 0 < n → 0 < m →
      spectralProductImpliesRightSpectral n m
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean)
- [Spectral sets and weak tiling](https://arxiv.org/abs/2209.04540)
