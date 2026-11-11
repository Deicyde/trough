---
declaration: theorem
origin: cited
lean: TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry
statement: formalized
proof: formalized
---

# The glue subgroup of `D₄⁶` is the hexacode

in the coordinates of
`d4SixHexacodeIsometry` it is exactly `Hexacode.code ω`.

```lean
TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry.{u_1} {F : Type u_1} [Field F] [Finite F]
  (hF : Nat.card F = 4) {ω : F} (hω : ω ^ 2 + ω + 1 = 0) :
  AddSubgroup.map (↑(TauCeti.d4SixHexacodeIsometry hF hω).toAddEquiv) TauCeti.d4SixGlueSubgroup =
    (TauCeti.Hexacode.code ω).toAddSubgroup
```

## Depends on

- [The standard model is isometric to the discriminant quadratic module of an even-rank checkerboard lattice](../integral-lattices-discriminant-forms-and-overlat/the-standard-model-is-isometric-to-the-discrimin.md)
- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/Glue.html#TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry).

## Sources

- [Tau Ceti documentation: `TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/Glue.html#TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry)
- [Source of `TauCeti.map_d4SixGlueSubgroup_d4SixHexacodeIsometry` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/Glue.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/Glue.lean#L210)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
