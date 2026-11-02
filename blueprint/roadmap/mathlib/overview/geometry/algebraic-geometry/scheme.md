---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgebraicGeometry.Scheme
mathlib_file: Mathlib/AlgebraicGeometry/Scheme.lean
---

# Scheme

We define `Scheme` as an `X : LocallyRingedSpace`,
along with a proof that every point has an open neighbourhood `U`
so that the restriction of `X` to `U` is isomorphic,
as a locally ringed space, to `Spec.toLocallyRingedSpace.obj (op R)`
for some `R : CommRingCat`.

```lean
AlgebraicGeometry.Scheme.{u_1} : Type (u_1 + 1)
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [Locally ringed space](locally-ringed-space.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Zariski topology](zariski-topology.md)

## Sources

- [Mathlib documentation: `AlgebraicGeometry.Scheme`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Scheme.html#AlgebraicGeometry.Scheme)
- [Source of `AlgebraicGeometry.Scheme` in Mathlib/AlgebraicGeometry/Scheme.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/AlgebraicGeometry/Scheme.lean#L34)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L484)
