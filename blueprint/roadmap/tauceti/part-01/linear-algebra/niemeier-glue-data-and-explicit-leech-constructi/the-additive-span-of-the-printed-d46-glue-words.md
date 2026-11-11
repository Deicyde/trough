---
declaration: theorem
origin: cited
lean: TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup
statement: formalized
proof: formalized
---

# The additive span of the printed `D₄⁶` glue words is a proper subgroup of the glue subgroup

```lean
TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup :
  AddSubgroup.closure
      ((fun d j => ((TauCeti.DynkinType.D 4).glueLabelEquiv ⋯) (d j)) ''
        TauCeti.d4SixPrintedDigits) <
    TauCeti.d4SixGlueSubgroup
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)

## Proof depends on

- [The glue subgroup of `D₄⁶` is the hexacode](the-glue-subgroup-of-d46-is-the-hexacode.md)
- [The standard model is isometric to the discriminant quadratic module of an even-rank checkerboard lattice](../integral-lattices-discriminant-forms-and-overlat/the-standard-model-is-isometric-to-the-discrimin.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/AdditiveSpan.html#TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/AdditiveSpan.html#TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup)
- [Source of `TauCeti.closure_d4SixPrintedDigits_lt_d4SixGlueSubgroup` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/AdditiveSpan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/D4Six/AdditiveSpan.lean#L159)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
