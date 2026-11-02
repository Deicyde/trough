---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_hasDerivWithinAt_eq_of_gt_of_lt, exists_hasDerivWithinAt_eq_of_lt_of_gt, Set.OrdConnected.image_hasDerivWithinAt, Set.OrdConnected.image_derivWithin, Set.OrdConnected.image_deriv, Convex.image_hasDerivWithinAt, Convex.image_derivWithin, Convex.image_deriv, exists_hasDerivWithinAt_eq_of_ge_of_le, exists_hasDerivWithinAt_eq_of_le_of_ge
mathlib_file: Mathlib/Analysis/Calculus/Darboux.lean
---

# Darboux's theorem (analysis)

Mathlib records this with 10 declarations.

`exists_hasDerivWithinAt_eq_of_gt_of_lt`: **Darboux's theorem**: if `a ≤ b` and `f' a < m < f' b`, then `f' c = m` for some
`c ∈ (a, b)`.

```lean
exists_hasDerivWithinAt_eq_of_gt_of_lt {a b : ℝ} {f f' : ℝ → ℝ} (hab : a ≤ b)
  (hf : ∀ x ∈ Set.Icc a b, HasDerivWithinAt f (f' x) (Set.Icc a b) x) {m : ℝ} (hma : f' a < m)
  (hmb : m < f' b) : m ∈ f' '' Set.Ioo a b
```

`exists_hasDerivWithinAt_eq_of_lt_of_gt`: **Darboux's theorem**: if `a ≤ b` and `f' b < m < f' a`, then `f' c = m` for some `c ∈ (a, b)`.

```lean
exists_hasDerivWithinAt_eq_of_lt_of_gt {a b : ℝ} {f f' : ℝ → ℝ} (hab : a ≤ b)
  (hf : ∀ x ∈ Set.Icc a b, HasDerivWithinAt f (f' x) (Set.Icc a b) x) {m : ℝ} (hma : m < f' a)
  (hmb : f' b < m) : m ∈ f' '' Set.Ioo a b
```

`Set.OrdConnected.image_hasDerivWithinAt`: **Darboux's theorem**: the image of a `Set.OrdConnected` set under `f'` is a `Set.OrdConnected`
set, `HasDerivWithinAt` version.

```lean
Set.OrdConnected.image_hasDerivWithinAt {f f' : ℝ → ℝ} {s : Set ℝ} (hs : s.OrdConnected)
  (hf : ∀ x ∈ s, HasDerivWithinAt f (f' x) s x) : (f' '' s).OrdConnected
```

`Set.OrdConnected.image_derivWithin`: **Darboux's theorem**: the image of a `Set.OrdConnected` set under `f'` is a `Set.OrdConnected`
set, `derivWithin` version.

```lean
Set.OrdConnected.image_derivWithin {f : ℝ → ℝ} {s : Set ℝ} (hs : s.OrdConnected)
  (hf : DifferentiableOn ℝ f s) : (derivWithin f s '' s).OrdConnected
```

`Set.OrdConnected.image_deriv`: **Darboux's theorem**: the image of a `Set.OrdConnected` set under `f'` is a `Set.OrdConnected`
set, `deriv` version.

```lean
Set.OrdConnected.image_deriv {f : ℝ → ℝ} {s : Set ℝ} (hs : s.OrdConnected)
  (hf : ∀ x ∈ s, DifferentiableAt ℝ f x) : (deriv f '' s).OrdConnected
```

`Convex.image_hasDerivWithinAt`: **Darboux's theorem**: the image of a convex set under `f'` is a convex set,
`HasDerivWithinAt` version.

```lean
Convex.image_hasDerivWithinAt {f f' : ℝ → ℝ} {s : Set ℝ} (hs : Convex ℝ s)
  (hf : ∀ x ∈ s, HasDerivWithinAt f (f' x) s x) : Convex ℝ (f' '' s)
```

`Convex.image_derivWithin`: **Darboux's theorem**: the image of a convex set under `f'` is a convex set,
`derivWithin` version.

```lean
Convex.image_derivWithin {f : ℝ → ℝ} {s : Set ℝ} (hs : Convex ℝ s) (hf : DifferentiableOn ℝ f s) :
  Convex ℝ (derivWithin f s '' s)
```

`Convex.image_deriv`: **Darboux's theorem**: the image of a convex set under `f'` is a convex set,
`deriv` version.

```lean
Convex.image_deriv {f : ℝ → ℝ} {s : Set ℝ} (hs : Convex ℝ s)
  (hf : ∀ x ∈ s, DifferentiableAt ℝ f x) : Convex ℝ (deriv f '' s)
```

`exists_hasDerivWithinAt_eq_of_ge_of_le`: **Darboux's theorem**: if `a ≤ b` and `f' a ≤ m ≤ f' b`, then `f' c = m` for some
`c ∈ [a, b]`.

```lean
exists_hasDerivWithinAt_eq_of_ge_of_le {a b : ℝ} {f f' : ℝ → ℝ} (hab : a ≤ b)
  (hf : ∀ x ∈ Set.Icc a b, HasDerivWithinAt f (f' x) (Set.Icc a b) x) {m : ℝ} (hma : f' a ≤ m)
  (hmb : m ≤ f' b) : m ∈ f' '' Set.Icc a b
```

`exists_hasDerivWithinAt_eq_of_le_of_ge`: **Darboux's theorem**: if `a ≤ b` and `f' b ≤ m ≤ f' a`, then `f' c = m` for some
`c ∈ [a, b]`.

```lean
exists_hasDerivWithinAt_eq_of_le_of_ge {a b : ℝ} {f f' : ℝ → ℝ} (hab : a ≤ b)
  (hf : ∀ x ∈ Set.Icc a b, HasDerivWithinAt f (f' x) (Set.Icc a b) x) {m : ℝ} (hma : m ≤ f' a)
  (hmb : f' b ≤ m) : m ∈ f' '' Set.Icc a b
```

## Depends on

- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Differentiable function between normed vector spaces](../../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Finite set](../../../../overview/data-structures/sets/finite-set.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Dual of a normed space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extreme value theorem](../../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `exists_hasDerivWithinAt_eq_of_gt_of_lt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#exists_hasDerivWithinAt_eq_of_gt_of_lt)
- [Source of `exists_hasDerivWithinAt_eq_of_gt_of_lt` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L28)
- [Mathlib documentation: `exists_hasDerivWithinAt_eq_of_lt_of_gt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#exists_hasDerivWithinAt_eq_of_lt_of_gt)
- [Source of `exists_hasDerivWithinAt_eq_of_lt_of_gt` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L64)
- [Mathlib documentation: `Set.OrdConnected.image_hasDerivWithinAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Set.OrdConnected.image_hasDerivWithinAt)
- [Source of `Set.OrdConnected.image_hasDerivWithinAt` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L74)
- [Mathlib documentation: `Set.OrdConnected.image_derivWithin`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Set.OrdConnected.image_derivWithin)
- [Source of `Set.OrdConnected.image_derivWithin` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L92)
- [Mathlib documentation: `Set.OrdConnected.image_deriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Set.OrdConnected.image_deriv)
- [Source of `Set.OrdConnected.image_deriv` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L98)
- [Mathlib documentation: `Convex.image_hasDerivWithinAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Convex.image_hasDerivWithinAt)
- [Source of `Convex.image_hasDerivWithinAt` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L104)
- [Mathlib documentation: `Convex.image_derivWithin`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Convex.image_derivWithin)
- [Source of `Convex.image_derivWithin` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L110)
- [Mathlib documentation: `Convex.image_deriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#Convex.image_deriv)
- [Source of `Convex.image_deriv` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L116)
- [Mathlib documentation: `exists_hasDerivWithinAt_eq_of_ge_of_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#exists_hasDerivWithinAt_eq_of_ge_of_le)
- [Source of `exists_hasDerivWithinAt_eq_of_ge_of_le` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L122)
- [Mathlib documentation: `exists_hasDerivWithinAt_eq_of_le_of_ge`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Darboux.html#exists_hasDerivWithinAt_eq_of_le_of_ge)
- [Source of `exists_hasDerivWithinAt_eq_of_le_of_ge` in Mathlib/Analysis/Calculus/Darboux.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Darboux.lean#L130)
- [1000+ theorems list: Q660799](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L720)
- [1000+ theorems project: Q660799](https://1000-plus.github.io/?length=-1#Q660799)
- [Wikipedia: Darboux's theorem (analysis)](https://en.wikipedia.org/wiki/Darboux's_theorem_%28analysis%29)
- [Wikidata: Q660799](https://www.wikidata.org/wiki/Q660799)
