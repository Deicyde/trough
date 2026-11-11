---
declaration: theorem
origin: cited
lean: TauCeti.vectorsOfNorm_two_leechLattice
statement: formalized
proof: formalized
---

# The Leech lattice has no roots

it has no vector of norm `2`.

```lean
TauCeti.vectorsOfNorm_two_leechLattice : TauCeti.leechLattice.vectorsOfNorm 2 = ∅
```

## Depends on

- [TauCeti.ConstructionA.lattice](../algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [The minimum of the Leech lattice is four](the-minimum-of-the-leech-lattice-is-four.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vectorsOfNorm_two_leechLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.vectorsOfNorm_two_leechLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.vectorsOfNorm_two_leechLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.vectorsOfNorm_two_leechLattice)
- [Source of `TauCeti.vectorsOfNorm_two_leechLattice` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean#L187)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
