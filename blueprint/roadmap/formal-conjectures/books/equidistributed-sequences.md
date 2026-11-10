---
declaration: theorem
origin: cited
lean: Equidistribution.isAccumulationPoint_exists_subsequence_tendsto, Equidistribution.isEquidistributedModuloOne_three_halves_pow, Equidistribution.isEquidistributedModuloOne_transcendental_three_halves_pow, Equidistribution.isAccumulationPoint_three_halves_pow_infinite, Equidistribution.isAccumulationPoint_three_halves_pow
statement: formalized
---

# Equidistributed Sequences

> Corollary 4.2 of Chapter 1 states that the sequence $(x^n), n = 1, 2, ... ,$ is equidistributed modulo 1 for
> almost all x > 1. And a little bit further down:
> "one does not know whether sequences such as $(e^n)$, $(π^n)$, or even $((\frac 3 2)^n)$"
> are equidistributed modulo 1 or not.
>
> *References:*
>   - [Uniform Distribution of Sequences](https://store.doverpublications.com/products/9780486149998)
> by *L. Kuipers* and *H. Niederreiter*, 1974
>   - [Wikipedia](https://en.wikipedia.org/wiki/Equidistributed_sequence)
>   - [Mat80] de Mathan, Bernard. "Numbers contravening a condition in density modulo 1."
>     Acta Mathematica Hungarica 36.3-4 (1980): 237-241.
>   - [Pol79] Pollington, Andrew Douglas. "On the density of sequence $\{n_ {k}\xi\} $."
>     Illinois Journal of Mathematics 23.4 (1979): 511-515.

*Quoted from [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Equidistribution.isAccumulationPoint_exists_subsequence_tendsto`

Textbook result, proved here.

> If a point `x` is an accumulation point of a sequence `s_0, s_1, ...` then
> there is a subsequence of `s` that tends to `x`

```lean
theorem isAccumulationPoint_exists_subsequence_tendsto
    (x : ℝ) (s : ℕ → ℝ) (hx : IsAccumulationPoint x s) :
    ∃ (u : ℕ → ℕ), StrictMono u ∧ Filter.atTop.Tendsto (s ∘ u) (𝓝 x)
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [54 General topology](../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean#L56).

## `Equidistribution.isEquidistributedModuloOne_three_halves_pow`

Open: stated without proof.

> The sequence `(3/2)^n` is equidistributed modulo `1`.

```lean
theorem isEquidistributedModuloOne_three_halves_pow :
    IsEquidistributedModuloOne (fun n => (3 / 2 : ℝ)^n)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean#L81).

## `Equidistribution.isEquidistributedModuloOne_transcendental_three_halves_pow`

Solved: stated here without proof.

> It is not true that for every transcendental number `x` the sequence `x * (3 / 2) ^ n` is
> equidistributed modulo `1`. The sequence `(3 / 2) ^ n` is lacunary, so by the theorem of
> Pollington [Pol79] and de Mathan [Mat80] the set of real numbers `x` for which `x * (3 / 2) ^ n`
> is not even dense modulo `1` has Hausdorff dimension `1`. This set is uncountable, so it contains
> transcendental numbers. Alternatively, an elementary nested-interval construction (see issue
> #5003) gives a Cantor set of `x` with `Int.fract (x * (3 / 2) ^ (8 * j)) ∈ [0, 1 / 10]` for all
> `j`, which already rules out equidistribution for uncountably many, hence some transcendental,
> `x`. By Koksma's metric theorem (Kuipers–Niederreiter, Chapter 1, Section 4), the sequence
> `x * (3 / 2) ^ n` is equidistributed modulo `1` for almost all `x`.

```lean
theorem isEquidistributedModuloOne_transcendental_three_halves_pow :
    ¬ ∀ x : ℝ, Transcendental ℚ x →
      IsEquidistributedModuloOne (fun n ↦ x * (3 / 2 : ℝ) ^ n)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean#L95).

## `Equidistribution.isAccumulationPoint_three_halves_pow_infinite`

Solved: stated here without proof.

> The sequence `(3/2)^n` has infinitely many accumulation points modulo `1`.

```lean
theorem isAccumulationPoint_three_halves_pow_infinite :
    {x | IsAccumulationPoint x (fun n => Int.fract <| (3 / 2 : ℝ)^n)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean#L104).

## `Equidistribution.isAccumulationPoint_three_halves_pow`

Open: stated without proof.

> Find an accumulation point of the sequence `(3/2)^n` modulo `1`.

```lean
theorem isAccumulationPoint_three_halves_pow :
    IsAccumulationPoint isAccumulationPoint_three_halves_pow.answer
      (fun n => Int.fract <| (3 / 2 : ℝ)^n)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/UniformDistributionOfSequences/Equidistribution.lean)
- [Uniform Distribution of Sequences](https://store.doverpublications.com/products/9780486149998)
