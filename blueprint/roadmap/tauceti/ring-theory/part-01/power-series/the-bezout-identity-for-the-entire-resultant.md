---
declaration: theorem
origin: cited
lean: Polynomial.exists_C_entireResultant_eq
statement: formalized
proof: formalized
---

# The Bézout identity for the entire resultant

For monic `P` and entire `F` there are an
entire series `G` and a polynomial `H` of degree less than `deg P` with
`Res(P, F) = P * G + H * F`.

```lean
Polynomial.exists_C_entireResultant_eq.{u_1} {R : Type u_1} [NormedCommRing R] [CompleteSpace R]
  {P : Polynomial R} {F : PowerSeries R} (hP : P.Monic) (hF : F.IsEntire) :
  ∃ G,
    G.IsEntire ∧
      ∃ H, H.degree < ↑P.natDegree ∧ PowerSeries.C (P.entireResultant F) = ↑P * G + ↑H * F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.exists_C_entireResultant_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Resultant.html#Polynomial.exists_C_entireResultant_eq).

## Sources

- [Tau Ceti documentation: `Polynomial.exists_C_entireResultant_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Resultant.html#Polynomial.exists_C_entireResultant_eq)
- [Source of `Polynomial.exists_C_entireResultant_eq` in TauCeti/RingTheory/PowerSeries/Entire/Resultant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Entire/Resultant.lean#L163)
