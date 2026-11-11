---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_isThomClass_of_subsingleton_units
statement: formalized
proof: formalized
---

# Every real vector bundle has a unique Thom class

**Every real vector bundle has a unique Thom class** with coefficients in a commutative ring
`K` whose only unit is `1`, such as `ZMod 2`: there is exactly one class of `Hʳ(E, E₀; K, K)`,
`r = dim F`, restricting to a generator of `Hʳ(E_b, E_b ∖ {0}; K, K) ≅ K` on every fibre. No
orientation of the bundle is needed, and the base is arbitrary; for `K = ZMod 2` this is the
mod `2` Thom class.

```lean
TauCeti.existsUnique_isThomClass_of_subsingleton_units.{w} {B : Type w} [TopologicalSpace B]
  {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] (K : Type w) [CommRing K] [Subsingleton Kˣ] : ∃! u, TauCeti.IsThomClass F E u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Compatible local classes over a trivializing open cover glue uniquely to the Thom pair](compatible-local-classes-over-a-trivializing-ope.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`](../../../algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-below.md)
- [The relative universal coefficient theorem over a field](../../../algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_isThomClass_of_subsingleton_units`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.html#TauCeti.existsUnique_isThomClass_of_subsingleton_units).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_isThomClass_of_subsingleton_units`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.html#TauCeti.existsUnique_isThomClass_of_subsingleton_units)
- [Source of `TauCeti.existsUnique_isThomClass_of_subsingleton_units` in TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.lean#L468)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
