---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: riesz_extension
mathlib_file: Mathlib/Analysis/Convex/Cone/Extension.lean
---

# M. Riesz extension theorem

M. **Riesz extension theorem**: given a convex cone `s` in a vector space `E`, a submodule `p`,
and a linear `f : p → ℝ`, assume that `f` is nonnegative on `p ∩ s` and `p + s = E`. Then
there exists a globally defined linear function `g : E → ℝ` that agrees with `f` on `p`,
and is nonnegative on `s`.

```lean
riesz_extension.{u_1} {E : Type u_1} [AddCommGroup E] [_root_.Module ℝ E] (s : PointedCone ℝ E)
  (f : E →ₗ.[ℝ] ℝ) (nonneg : ∀ (x : ↥f.domain), ↑x ∈ s → 0 ≤ ↑f x)
  (dense : ∀ (y : E), ∃ x, ↑x + y ∈ s) : ∃ g, (∀ (x : ↥f.domain), g ↑x = ↑f x) ∧ ∀ x ∈ s, 0 ≤ g x
```

## Depends on

- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Pointed cone](../../../../overview/geometry/convex-geometry/pointed-cone.md)
- [Real number](../../../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Generating sets](../../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Order (Real numbers)](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `riesz_extension`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Cone/Extension.html#riesz_extension)
- [Source of `riesz_extension` in Mathlib/Analysis/Convex/Cone/Extension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Cone/Extension.lean#L141)
- [1000+ theorems list: Q3527217](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2549)
- [1000+ theorems project: Q3527217](https://1000-plus.github.io/?length=-1#Q3527217)
- [Wikipedia: M. Riesz extension theorem](https://en.wikipedia.org/wiki/M._Riesz_extension_theorem)
- [Wikidata: Q3527217](https://www.wikidata.org/wiki/Q3527217)
