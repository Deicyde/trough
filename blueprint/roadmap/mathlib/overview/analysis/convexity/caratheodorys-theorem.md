# Carathéodory's theorem

**Carathéodory's convexity theorem**

```lean
convexHull_eq_union.{u, u_1} {𝕜 : Type u_1} {E : Type u} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E] {s : Set E} :
  (convexHull 𝕜) s = ⋃ t, ⋃ (_ : ↑t ⊆ s), ⋃ (_ : AffineIndependent 𝕜 Subtype.val), (convexHull 𝕜) ↑t
```

## Depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Convex hull of a subset of an affine real space](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Field](../../general-algebra/field-theory/field.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)

## Proof depends on

- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `convexHull_eq_union`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Caratheodory.html#convexHull_eq_union)
- [Source of `convexHull_eq_union` in Mathlib/Analysis/Convex/Caratheodory.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Caratheodory.lean#L105)
- [Mathlib overview: Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L326)
- [1000+ theorems list: Q2471737](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2220)
- [1000+ theorems project: Q2471737](https://1000-plus.github.io/all.html?length=-1#Q2471737)
- [Wikipedia: Carathéodory's theorem (convex hull)](https://en.wikipedia.org/wiki/Carath%C3%A9odory's_theorem_%28convex_hull%29)
- [Wikidata: Q2471737](https://www.wikidata.org/wiki/Q2471737)
