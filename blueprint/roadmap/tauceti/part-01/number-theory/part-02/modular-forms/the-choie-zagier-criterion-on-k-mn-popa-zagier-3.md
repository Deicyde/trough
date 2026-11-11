---
declaration: theorem
origin: cited
lean: TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff
statement: formalized
proof: formalized
---

# The Choie–Zagier criterion on `k[ℳₙ]` (Popa–Zagier, §3, Lemma 1)

for `n ≠ 0` and `2`, `3`
invertible in `k`, an element `x ∈ k[ℳₙ]` lies in `(1 + S) k[ℳₙ] + (1 + U + U²) k[ℳₙ]`, with
`U = T * S`, if and only if `(1 - S) x ∈ (1 - T) k[ℳₙ]`, all products being left
multiplications.

```lean
TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff.{u_1} {n : ℤ}
  {k : Type u_1} [Ring k] [Invertible 2] [Invertible 3] (hn : n ≠ 0)
  {x : MonoidAlgebra k (TauCeti.TraceFormulaMatrixModule n)} :
  (1 -
          (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
              (TauCeti.TraceFormulaMatrixModule n))
            ModularGroup.S)
        x ∈
      (1 -
          (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
              (TauCeti.TraceFormulaMatrixModule n))
            ModularGroup.T).range ↔
    x ∈
      (1 +
            (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
                (TauCeti.TraceFormulaMatrixModule n))
              ModularGroup.S).range ⊔
        (1 +
              (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
                  (TauCeti.TraceFormulaMatrixModule n))
                (ModularGroup.T * ModularGroup.S) +
            (Representation.ofMulAction k (Matrix.SpecialLinearGroup (Fin 2) ℤ)
                  (TauCeti.TraceFormulaMatrixModule n))
                (ModularGroup.T * ModularGroup.S) ^
              2).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Choie–Zagier criterion (Popa–Zagier, Lemma 1)](../../../linear-algebra/end/the-choie-zagier-criterion-popa-zagier-lemma-1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/Acyclicity.html#TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/Acyclicity.html#TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff)
- [Source of `TauCeti.TraceFormulaMatrixModule.one_sub_S_apply_mem_range_one_sub_T_iff` in TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/Acyclicity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/LevelOne/TraceFormula/Acyclicity.lean#L85)
