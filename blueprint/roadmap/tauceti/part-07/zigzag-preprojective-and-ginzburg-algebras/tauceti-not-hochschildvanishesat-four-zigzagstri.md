---
declaration: theorem
origin: cited
lean: TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra
statement: formalized
proof: formalized
---

# TauCeti.not\_hochschildVanishesAt\_four\_zigzagStrictAInfinityAlgebra

**The quartic Hochschild cohomology `HH^{4, -2}` of a zigzag algebra is nonzero** when four
distinct darts of `G` have a common head, that is when some vertex has four distinct neighbours,
over every nontrivial commutative ring: some Hochschild cocycle of the strict zigzag algebra of
suspended degree one, concentrated on words of length four, is not the Hochschild differential of
a cochain of degree zero.

```lean
TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra.{u, w} {k : Type w} [CommRing k]
  {V : Type u} {G : SimpleGraph V} [Finite V] {hns : ∀ (i : V), ∃ j, G.Adj i j} [Nontrivial k]
  {δ : Fin 4 → G.Dart} (hδ : Function.Injective δ) {v : V}
  (hv : ∀ (i : Fin 4), (δ i).toProd.2 = v) :
  ¬(TauCeti.zigzagStrictAInfinityAlgebra k hns).HochschildVanishesAt
      ⟨4, TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra._proof_1⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/HochschildClass.html#TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/HochschildClass.html#TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra)
- [Source of `TauCeti.not_hochschildVanishesAt_four_zigzagStrictAInfinityAlgebra` in TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/HochschildClass.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/HochschildClass.lean#L924)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
