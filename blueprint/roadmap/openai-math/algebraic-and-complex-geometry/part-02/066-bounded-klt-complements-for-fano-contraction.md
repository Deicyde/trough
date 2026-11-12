---
declaration: section
origin: cited
lean: OAI.CartierSections.isCompact_closedChartFieldRetraction_cone
statement: formalized
proof: formalized
---

# 066. Bounded klt complements for Fano contractions

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the finite-rational-coefficient form of Shokurov’s bounded-klt-complement conjecture for *ϵ*-lc complex Fano-type pairs with nef anti-log-canonical divisor. For *ϵ*-lc Fano contractions over any algebraically closed characteristic-zero field, it gives klt complements near every base point, with index bounded only by dimension and positive rational *ϵ*.

## Bounded klt complements for Fano contractions

For fixed dimension *d* and positive rational *ϵ*, we prove that every *ϵ*-log-canonical Fano contraction over an algebraically closed field of characteristic zero admits, near each closed base point, a klt complement of index bounded only by *d* and *ϵ*. Over ℂ, we also obtain monotone klt complements for Fano type pairs with nef anti-log-canonical divisor and coefficients in a fixed finite rational set. This proves the finite-rational-coefficient form of Shokurov's bounded-klt-complement conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf).

## Uniform Cartier sections for Fano type contractions

We prove the Cartier-divisor conjecture of Birkar and Shokurov for rational boundaries in characteristic zero and for real boundaries over ℂ. For an *ϵ*-lc Fano type contraction with positive-dimensional base and nef negative log canonical class, a Cartier divisor through any prescribed base point can be chosen with pullback log canonical threshold bounded below in terms of the dimension and *ϵ* alone.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper develops uniform Cartier sections for Fano-type contractions as a step toward bounded klt complements. The linked formalization proves a local compactness result: for positive numbers $a_i$, the chart-field retractions indexed by nonnegative weights satisfying $\sum_i a_iw_i=1$ form a compact set in the pointwise topology on the fraction field.

The chart is built over an algebraically closed field from the localization of a polynomial ring at its origin. Its local domain is Noetherian, essentially of finite type and formally unramified over that localization, and formally étale over the polynomial ring.

This compactness result applies to one such chart. It does not construct a Cartier divisor through a prescribed base point whose pullback has a positive log-canonical-threshold bound along the whole fibre depending only on dimension and discrepancy, as required by the paper's uniform Cartier-section theorem. Bounded klt complements and the paper's real-boundary and companion conclusions are also outside this comparison.

## Lean: Compactness of normalized chart-field retractions

Stated in [CartierChartCompactnessSupport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CartierChartCompactnessSupport.lean); one of the main results in the repository's formalization.yaml.

```lean
lemma isCompact_closedChartFieldRetraction_cone
    (a : σ → NNReal) (ha : ∀ i, 0 < a i) :
    IsCompact ((fun w : σ → NNReal => fun x : K =>
      closedChartFieldRetraction (σ := σ) (k := k) (R := R) (A := A) w x) ''
      normalizedWeights a)
```

Proved in [lean/OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean, line 47](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean#L47).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/066.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/066.md)
