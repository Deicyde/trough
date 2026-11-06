# Jensen's inequality (finite sum version)

Convex **Jensen's inequality**, `Finset.sum` version.

```lean
ConvexOn.map_sum_le.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2} {β : Type u_3} {ι : Type u_4}
  [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup E] [AddCommGroup β]
  [PartialOrder β] [IsOrderedAddMonoid β] [_root_.Module 𝕜 E] [_root_.Module 𝕜 β]
  [IsStrictOrderedModule 𝕜 β] {s : Set E} {f : E → β} {t : Finset ι} {w : ι → 𝕜} {p : ι → E}
  (hf : ConvexOn 𝕜 s f) (h₀ : ∀ i ∈ t, 0 ≤ w i) (h₁ : ∑ i ∈ t, w i = 1) (hmem : ∀ i ∈ t, p i ∈ s) :
  f (∑ i ∈ t, w i • p i) ≤ ∑ i ∈ t, w i • f (p i)
```

## Depends on

- [Convex function](convex-function.md)
- [Field](../../general-algebra/field-theory/field.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)

## Sources

- [Mathlib documentation: `ConvexOn.map_sum_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Jensen.html#ConvexOn.map_sum_le)
- [Source of `ConvexOn.map_sum_le` in Mathlib/Analysis/Convex/Jensen.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Jensen.lean#L65)
- [Mathlib overview: Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L323)
