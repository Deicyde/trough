---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PhragmenLindelof.horizontal_strip
mathlib_file: Mathlib/Analysis/Complex/PhragmenLindelof.lean
---

# Phragmen-Lindelöf principle

**Phragmen-Lindelöf principle** in a strip `U = {z : ℂ | a < im z < b}`.
Let `f : ℂ → E` be a function such that

* `f` is differentiable on `U` and is continuous on its closure;
* `‖f z‖` is bounded from above by `A * exp(B * exp(c * |re z|))` on `U` for some `c < π / (b - a)`;
* `‖f z‖` is bounded from above by a constant `C` on the boundary of `U`.

Then `‖f z‖` is bounded by the same constant on the closed strip
`{z : ℂ | a ≤ im z ≤ b}`. Moreover, it suffices to verify the second assumption
only for sufficiently large values of `|re z|`.

```lean
PhragmenLindelof.horizontal_strip.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  {a b C : ℝ} {f : ℂ → E} {z : ℂ} (hfd : DiffContOnCl ℂ f (Complex.im ⁻¹' Set.Ioo a b))
  (hB :
    ∃ c < Real.pi / (b - a),
      ∃ B,
        f =O[Filter.comap (abs ∘ Complex.re) Filter.atTop ⊓
            Filter.principal (Complex.im ⁻¹' Set.Ioo a b)]
          fun z => Real.exp (B * Real.exp (c * |z.re|)))
  (hle_a : ∀ (z : ℂ), z.im = a → ‖f z‖ ≤ C) (hle_b : ∀ (z : ℂ), z.im = b → ‖f z‖ ≤ C)
  (hza : a ≤ z.im) (hzb : z.im ≤ b) : ‖f z‖ ≤ C
```

## Depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Exponential](../special-functions/exponential.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Cauchy integral formula](cauchy-integral-formula.md)

## Sources

- [Mathlib documentation: `PhragmenLindelof.horizontal_strip`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/PhragmenLindelof.html#PhragmenLindelof.horizontal_strip)
- [Source of `PhragmenLindelof.horizontal_strip` in Mathlib/Analysis/Complex/PhragmenLindelof.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/PhragmenLindelof.lean#L102)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L374)
- [1000+ theorems list: Q4378868](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2686)
- [1000+ theorems project: Q4378868](https://1000-plus.github.io/all.html?length=-1#Q4378868)
- [Wikipedia: Phragmén–Lindelöf theorem](https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_theorem)
- [Wikidata: Q4378868](https://www.wikidata.org/wiki/Q4378868)
