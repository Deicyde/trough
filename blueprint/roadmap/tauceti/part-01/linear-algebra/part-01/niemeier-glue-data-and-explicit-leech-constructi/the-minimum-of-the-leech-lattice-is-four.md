---
declaration: theorem
origin: cited
lean: TauCeti.minimum_leechLattice
statement: formalized
proof: formalized
---

# The minimum of the Leech lattice is four

every nonzero vector has norm at least `4`, and
the odd shift has norm exactly `4`.

```lean
TauCeti.minimum_leechLattice : TauCeti.leechLattice.minimum = 4
```

## Depends on

- [TauCeti.ConstructionA.lattice](../algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [The congruence model of the Leech lattice](the-congruence-model-of-the-leech-lattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.minimum_leechLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.minimum_leechLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.minimum_leechLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.minimum_leechLattice)
- [Source of `TauCeti.minimum_leechLattice` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean#L170)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
