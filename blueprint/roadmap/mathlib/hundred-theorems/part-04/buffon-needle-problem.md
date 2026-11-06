# Buffon Needle Problem

Mathlib records this with 2 declarations.

`BuffonsNeedle.buffon_short`: Buffon's Needle, the short case (`l ≤ d`). The probability of the needle crossing a line
equals `(2 * l) / (d * π)`.

```lean
BuffonsNeedle.buffon_short.{u_1} {Ω : Type u_1} [MeasureTheory.MeasureSpace Ω] (d l : ℝ)
  (hd : 0 < d) (hl : 0 < l) (B : Ω → ℝ × ℝ) (hBₘ : Measurable B)
  (hB :
    MeasureTheory.pdf.IsUniform B (Set.Icc (-d / 2) (d / 2) ×ˢ Set.Icc 0 Real.pi)
      MeasureTheory.volume MeasureTheory.volume)
  (h : l ≤ d) : ∫ (x : Ω), BuffonsNeedle.N l B x = 2 * l * (d * Real.pi)⁻¹
```

`BuffonsNeedle.buffon_long`: Buffon's Needle, the long case (`d ≤ l`)

```lean
BuffonsNeedle.buffon_long.{u_1} {Ω : Type u_1} [MeasureTheory.MeasureSpace Ω] (d l : ℝ) (hd : 0 < d)
  (hl : 0 < l) (B : Ω → ℝ × ℝ) (hBₘ : Measurable B)
  (hB :
    MeasureTheory.pdf.IsUniform B (Set.Icc (-d / 2) (d / 2) ×ˢ Set.Icc 0 Real.pi)
      MeasureTheory.volume MeasureTheory.volume)
  (h : d ≤ l) :
  ∫ (x : Ω), BuffonsNeedle.N l B x =
    2 * l / (d * Real.pi) - 2 / (d * Real.pi) * (√(l ^ 2 - d ^ 2) + d * Real.arcsin (d / l)) + 1
```

## Depends on

- [Bochner integral](../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Conditional probability](../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Inverse trigonometric functions](../../overview/analysis/special-functions/inverse-trigonometric-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Compactness in terms of filters](../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Fubini's theorem](../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [The Triangle Inequality](the-triangle-inequality.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `BuffonsNeedle.buffon_short`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BuffonsNeedle.html#BuffonsNeedle.buffon_short)
- [Source of `BuffonsNeedle.buffon_short` in Archive/Wiedijk100Theorems/BuffonsNeedle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BuffonsNeedle.lean#L248)
- [Mathlib documentation: `BuffonsNeedle.buffon_long`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BuffonsNeedle.html#BuffonsNeedle.buffon_long)
- [Source of `BuffonsNeedle.buffon_long` in Archive/Wiedijk100Theorems/BuffonsNeedle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BuffonsNeedle.lean#L329)
- [Freek Wiedijk's 100 theorems, no. 99](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L510)
