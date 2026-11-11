---
declaration: theorem
origin: cited
lean: TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff
statement: formalized
proof: formalized
---

# Popa–Zagier's criterion for `(1 - T)·ℛₙ`

An element of `k[ℳₙ]` lies in the range of left
multiplication by `1 - T` if and only if its coefficients sum to zero along every orbit of
`Γ_∞ = ⟨T⟩`.

```lean
TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff.{u_1} {k : Type u_1} [CommRing k] {n : ℤ}
  {ζ : MonoidAlgebra k (TauCeti.TraceFormulaMatrixModule n)} :
  ζ ∈
      (1 -
          (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
              (TauCeti.TraceFormulaMatrixModule n))
            ModularGroup.T).range ↔
    (MonoidAlgebra.mapDomainLinearMap k k
          (Quotient.mk
            (MulAction.orbitRel (↥(Subgroup.zpowers ModularGroup.T))
              (TauCeti.TraceFormulaMatrixModule n))))
        ζ =
      0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/PeriodRelation.html#TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/PeriodRelation.html#TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff)
- [Source of `TauCeti.TraceFormulaMatrixModule.mem_range_one_sub_T_iff` in TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/PeriodRelation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/PeriodRelation.lean#L98)
