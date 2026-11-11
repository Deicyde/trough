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

- [The lattice `N_r` of a row of the rootful rank-24 table](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-lattice-n-r-of-a-row-of-the-rootful-rank-24.md)
- [TauCeti.ConstructionA.lattice](../../../linear-algebra/algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)
- [TauCeti.RootfulNiemeierType](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/tauceti-rootfulniemeiertype.md)

## Proof depends on

- [The `A₂¹²` table glue is the extended ternary Golay code](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-a212-table-glue-is-the-extended-ternary-gola.md)
- [The glue subgroup of `D₄⁶` is the hexacode](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-glue-subgroup-of-d46-is-the-hexacode.md)
- [The Leech lattice has no roots](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-leech-lattice-has-no-roots.md)
- [The root sublattice of `N_r` is `R_r`](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-root-sublattice-of-n-r-is-r-r.md)
- [The shortest norm of a glue word is the sum of the shortest norms of its labels](../../../linear-algebra/niemeier-glue-data-and-explicit-leech-constructi/the-shortest-norm-of-a-glue-word-is-the-sum-of-t.md)
- [The standard model is isometric to the discriminant quadratic module of an even-rank checkerboard lattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/the-standard-model-is-isometric-to-the-discrimin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NiemeierType.nonempty_isometry_lattice_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.nonempty_isometry_lattice_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NiemeierType.nonempty_isometry_lattice_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.html#TauCeti.NiemeierType.nonempty_isometry_lattice_iff)
- [Source of `TauCeti.NiemeierType.nonempty_isometry_lattice_iff` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/ReferenceLattices.lean#L172)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
