---
declaration: theorem
origin: cited
lean: PadicInt.hasSum_vanDerPut, PadicInt.vanDerPutEquiv
statement: formalized
proof: formalized
---

# Van der Put's theorem

a continuous function on `ℤ_[p]` with values in an ultrametric
normed group is the uniformly convergent sum of its van der Put terms, without assuming
completeness.

```lean
PadicInt.hasSum_vanDerPut.{u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] {E : Type u_2}
  [NormedAddCommGroup E] [IsUltrametricDist E] (f : C(ℤ_[p], E)) :
  HasSum (fun n => PadicInt.vanDerPutTerm (PadicInt.vanDerPutCoeff (⇑f) n) n) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PadicInt.hasSum_vanDerPut`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/VanDerPut/Basic.html#PadicInt.hasSum_vanDerPut).

## Other forms

**PadicInt.vanDerPutEquiv.** Formalized in Tau Ceti as [`PadicInt.vanDerPutEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/VanDerPut/Basic.html#PadicInt.vanDerPutEquiv).

```lean
PadicInt.vanDerPutEquiv.{u_1, u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] (S : Type u_1) (E : Type u_2)
  [NormedAddCommGroup E] [IsUltrametricDist E] [CompleteSpace E] [Semiring S] [_root_.Module S E]
  [ContinuousConstSMul S E] : C(ℤ_[p], E) ≃ₗᵢ[S] ZeroAtInftyContinuousMap ℕ E
```

## Sources

- [Tau Ceti documentation: `PadicInt.hasSum_vanDerPut`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/VanDerPut/Basic.html#PadicInt.hasSum_vanDerPut)
- [Source of `PadicInt.hasSum_vanDerPut` in TauCeti/NumberTheory/Padics/VanDerPut/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/VanDerPut/Basic.lean#L331)
