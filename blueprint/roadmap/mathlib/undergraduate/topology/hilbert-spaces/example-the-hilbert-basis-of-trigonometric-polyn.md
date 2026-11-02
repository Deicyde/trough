---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: fourierBasis
mathlib_file: Mathlib/Analysis/Fourier/AddCircle.lean
---

# Example, the Hilbert basis of trigonometric polynomials

We define `fourierBasis` to be a `ℤ`-indexed Hilbert basis for `Lp ℂ 2 haarAddCircle`,
which by definition is an isometric isomorphism from `Lp ℂ 2 haarAddCircle` to `ℓ²(ℤ, ℂ)`.

```lean
fourierBasis {T : ℝ} [hT : Fact (0 < T)] :
  HilbertBasis ℤ ℂ ↥(MeasureTheory.Lp ℂ 2 AddCircle.haarAddCircle)
```

## Depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Hilbert bases](hilbert-bases.md)
- [Homeomorphisms](../topology-and-metric-spaces/homeomorphisms.md)
- [Inner product space $L^2$](inner-product-space-l-2-2.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `fourierBasis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#fourierBasis)
- [Source of `fourierBasis` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/AddCircle.lean#L408)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L447)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L532)
