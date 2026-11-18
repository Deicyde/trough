---
declaration: theorem
origin: cited
lean: TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff
statement: formalized
proof: formalized
---

# The Leech row is the only row without roots

```lean
TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff {n : TauCeti.NiemeierType} :
  n.lattice.vectorsOfNorm 2 = ∅ ↔ n = TauCeti.NiemeierType.leech
```

## Depends on

- [The lattice `N_r` of a row of the rootful rank-24 table](../niemeier-glue-data-and-explicit-leech-constructi/the-lattice-n-r-of-a-row-of-the-rootful-rank-24.md)
- [TauCeti.ConstructionA.lattice](../algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)
- [TauCeti.RootfulNiemeierType](../niemeier-glue-data-and-explicit-leech-constructi/tauceti-rootfulniemeiertype.md)

## Proof depends on

- [The `A₂¹²` table glue is the extended ternary Golay code](../niemeier-glue-data-and-explicit-leech-constructi/the-a212-table-glue-is-the-extended-ternary-gola.md)
- [The glue subgroup of `D₄⁶` is the hexacode](../niemeier-glue-data-and-explicit-leech-constructi/the-glue-subgroup-of-d46-is-the-hexacode.md)
- [The Leech lattice has no roots](../niemeier-glue-data-and-explicit-leech-constructi/the-leech-lattice-has-no-roots.md)
- [The shortest norm of a glue word is the sum of the shortest norms of its labels](../niemeier-glue-data-and-explicit-leech-constructi/the-shortest-norm-of-a-glue-word-is-the-sum-of-t.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff)
- [Source of `TauCeti.NiemeierType.vectorsOfNorm_two_lattice_eq_empty_iff` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean#L165)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
