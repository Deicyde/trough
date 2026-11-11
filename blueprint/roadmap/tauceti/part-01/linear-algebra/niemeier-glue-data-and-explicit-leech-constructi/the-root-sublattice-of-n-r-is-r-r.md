---
declaration: theorem
origin: cited
lean: TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice
statement: formalized
proof: formalized
---

# The root sublattice of `N_r` is `R_r`

for every row, the norm-`2` vectors of `N_r` span
exactly the carrier of the orthogonal sum of the component root lattices.

```lean
TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice (r : TauCeti.RootfulNiemeierType) :
  Submodule.span ℤ ((fun x => ↑x) '' r.lattice.vectorsOfNorm 2) = r.rootLattice.carrier
```

## Depends on

- [The lattice `N_r` of a row of the rootful rank-24 table](the-lattice-n-r-of-a-row-of-the-rootful-rank-24.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.RootfulNiemeierType](tauceti-rootfulniemeiertype.md)

## Proof depends on

- [The `A₂¹²` table glue is the extended ternary Golay code](the-a212-table-glue-is-the-extended-ternary-gola.md)
- [The glue subgroup of `D₄⁶` is the hexacode](the-glue-subgroup-of-d46-is-the-hexacode.md)
- [The shortest norm of a glue word is the sum of the shortest norms of its labels](the-shortest-norm-of-a-glue-word-is-the-sum-of-t.md)
- [The standard model is isometric to the discriminant quadratic module of an even-rank checkerboard lattice](../integral-lattices-discriminant-forms-and-overlat/the-standard-model-is-isometric-to-the-discrimin.md)
- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.html#TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice).

## Sources

- [Tau Ceti documentation: `TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.html#TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice)
- [Source of `TauCeti.RootfulNiemeierType.span_vectorsOfNorm_two_lattice` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.lean#L264)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
