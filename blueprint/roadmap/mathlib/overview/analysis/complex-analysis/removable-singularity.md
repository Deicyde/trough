---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.differentiableOn_update_limUnder_insert_of_isLittleO
mathlib_file: Mathlib/Analysis/Complex/RemovableSingularity.lean
---

# Removable singularity

**Removable singularity** theorem: if `s` is a punctured neighborhood of `c : ℂ`, a function
`f : ℂ → E` is complex differentiable on `s`, and $f(z) - f(c)=o((z-c)^{-1})$, then `f` redefined to
be equal to `limUnder (𝓝[≠] c) f` at `c` is complex differentiable on `{c} ∪ s`.

```lean
Complex.differentiableOn_update_limUnder_insert_of_isLittleO.{u} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {s : Set ℂ} {c : ℂ} (hc : s ∈ nhdsWithin c {c}ᶜ)
  (hd : DifferentiableOn ℂ f s)
  (ho : (fun z => f z - f c) =o[nhdsWithin c {c}ᶜ] fun z => (z - c)⁻¹) :
  DifferentiableOn ℂ (Function.update f c ((nhdsWithin c {c}ᶜ).limUnder f)) (insert c s)
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Euclidean affine space](../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Cauchy formulas](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/cauchy-formulas.md)

## Sources

- [Mathlib documentation: `Complex.differentiableOn_update_limUnder_insert_of_isLittleO`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/RemovableSingularity.html#Complex.differentiableOn_update_limUnder_insert_of_isLittleO)
- [Source of `Complex.differentiableOn_update_limUnder_insert_of_isLittleO` in Mathlib/Analysis/Complex/RemovableSingularity.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/RemovableSingularity.lean#L88)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L373)
