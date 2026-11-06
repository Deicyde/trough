# Radon's theorem

**Radon's theorem on convex sets**.

Any family `f` of affine dependent vectors contains a set `I` with the property that convex hulls of
`I` and `Iᶜ` intersect nontrivially.
In particular, any `d + 2` points in a `d`-dimensional space can be partitioned this way, since they
are affinely dependent \(see `finrank_vectorSpan_le_iff_not_affineIndependent`\).

```lean
Convex.radon_partition.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E] {f : ι → E}
  (h : ¬AffineIndependent 𝕜 f) : ∃ I, ((convexHull 𝕜) (f '' I) ∩ (convexHull 𝕜) (f '' Iᶜ)).Nonempty
```

## Depends on

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Convex hull of a subset of an affine real space](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Convex.radon_partition`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Radon.html#Convex.radon_partition)
- [Source of `Convex.radon_partition` in Mathlib/Analysis/Convex/Radon.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Radon.lean#L42)
- [1000+ theorems list: Q1471282](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1710)
- [1000+ theorems project: Q1471282](https://1000-plus.github.io/all.html?length=-1#Q1471282)
- [Wikipedia: Radon's theorem](https://en.wikipedia.org/wiki/Radon's_theorem)
- [Wikidata: Q1471282](https://www.wikidata.org/wiki/Q1471282)
