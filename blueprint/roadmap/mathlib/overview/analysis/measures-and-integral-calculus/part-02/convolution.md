---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.convolution
mathlib_file: Mathlib/Analysis/Convolution.lean
---

# Convolution (Measures and integral calculus)

The convolution of two functions `f` and `g` with respect to a continuous bilinear map `L` and
measure `μ`. It is defined to be `(f ⋆[L, μ] g) x = ∫ t, L (f t) (g (x - t)) ∂μ`.

```lean
MeasureTheory.convolution.{u𝕜, uG, uE, uE', uF} {𝕜 : Type u𝕜} {G : Type uG} {E : Type uE}
  {E' : Type uE'} {F : Type uF} [NormedAddCommGroup E] [NormedAddCommGroup E']
  [NormedAddCommGroup F] [NontriviallyNormedField 𝕜] [NormedSpace 𝕜 E] [NormedSpace 𝕜 E']
  [NormedSpace 𝕜 F] [MeasurableSpace G] [NormedSpace ℝ F] [Sub G] (f : G → E) (g : G → E')
  (L : E →L[𝕜] E' →L[𝕜] F) (μ : MeasureTheory.Measure G := by volume_tac) : G → F
```

## Depends on

- [Bochner integral](../part-01/bochner-integral.md)

## Sources

- [Mathlib documentation: `MeasureTheory.convolution`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convolution.html#MeasureTheory.convolution)
- [Source of `MeasureTheory.convolution` in Mathlib/Analysis/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convolution.lean#L399)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L359)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L528)
