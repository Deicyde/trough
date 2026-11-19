---
declaration: theorem
origin: cited
lean: TauCeti.NiemeierType.nonempty_isometry_lattice_iff
statement: formalized
proof: formalized
---

# The 24 Niemeier lattices are pairwise non-isometric

An isometry preserves the number of
roots, which separates the Leech row from the rootful rows, and two rootful rows are separated by
`TauCeti.RootfulNiemeierType.nonempty_isometry_lattice_iff`.

```lean
TauCeti.NiemeierType.nonempty_isometry_lattice_iff {m n : TauCeti.NiemeierType} :
  Nonempty (m.lattice.Isometry n.lattice) ↔ m = n
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
- [The root sublattice of `N_r` is `R_r`](../niemeier-glue-data-and-explicit-leech-constructi/the-root-sublattice-of-n-r-is-r-r.md)
- [The shortest norm of a glue word is the sum of the shortest norms of its labels](../niemeier-glue-data-and-explicit-leech-constructi/the-shortest-norm-of-a-glue-word-is-the-sum-of-t.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NiemeierType.nonempty_isometry_lattice_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.nonempty_isometry_lattice_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NiemeierType.nonempty_isometry_lattice_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.nonempty_isometry_lattice_iff)
- [Source of `TauCeti.NiemeierType.nonempty_isometry_lattice_iff` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean#L172)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
