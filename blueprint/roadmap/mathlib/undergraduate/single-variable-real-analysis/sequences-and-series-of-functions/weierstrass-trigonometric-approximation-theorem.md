---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: span_fourier_closure_eq_top
mathlib_file: Mathlib/Analysis/Fourier/AddCircle.lean
---

# Weierstrass trigonometric approximation theorem

The linear span of the monomials `fourier n` is dense in `C(AddCircle T, ℂ)`.

```lean
span_fourier_closure_eq_top {T : ℝ} [hT : Fact (0 < T)] :
  (Submodule.span ℂ (Set.range fourier)).topologicalClosure = ⊤
```

## Depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Stone-Weierstrass theorem](../../../overview/topology/general-topology/part-02/stone-weierstrass-theorem.md)

## Sources

- [Mathlib documentation: `span_fourier_closure_eq_top`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#span_fourier_closure_eq_top)
- [Source of `span_fourier_closure_eq_top` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/AddCircle.lean#L243)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L357)
