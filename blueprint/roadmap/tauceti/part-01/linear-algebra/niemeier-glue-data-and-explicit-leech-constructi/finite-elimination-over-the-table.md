---
declaration: theorem
origin: cited
lean: TauCeti.RootfulNiemeierType.forall
statement: formalized
proof: formalized
---

# Finite elimination over the table

a statement holds for every row exactly when it holds
for each of the 23 rows, in source order.  This specializes a theorem stated uniformly over the
table to all rows at once, and conversely assembles a uniform theorem from row-by-row proofs.

```lean
TauCeti.RootfulNiemeierType.forall {P : TauCeti.RootfulNiemeierType → Prop} :
  (∀ (r : TauCeti.RootfulNiemeierType), P r) ↔
    P TauCeti.RootfulNiemeierType.d24 ∧
      P TauCeti.RootfulNiemeierType.d16e8 ∧
        P TauCeti.RootfulNiemeierType.e8Cubed ∧
          P TauCeti.RootfulNiemeierType.a24 ∧
            P TauCeti.RootfulNiemeierType.d12Squared ∧
              P TauCeti.RootfulNiemeierType.a17e7 ∧
                P TauCeti.RootfulNiemeierType.d10e7Squared ∧
                  P TauCeti.RootfulNiemeierType.a15d9 ∧
                    P TauCeti.RootfulNiemeierType.d8Cubed ∧
                      P TauCeti.RootfulNiemeierType.a12Squared ∧
                        P TauCeti.RootfulNiemeierType.a11d7e6 ∧
                          P TauCeti.RootfulNiemeierType.e6Fourth ∧
                            P TauCeti.RootfulNiemeierType.a9SquaredD6 ∧
                              P TauCeti.RootfulNiemeierType.d6Fourth ∧
                                P TauCeti.RootfulNiemeierType.a8Cubed ∧
                                  P TauCeti.RootfulNiemeierType.a7SquaredD5Squared ∧
                                    P TauCeti.RootfulNiemeierType.a6Fourth ∧
                                      P TauCeti.RootfulNiemeierType.a5FourthD4 ∧
                                        P TauCeti.RootfulNiemeierType.d4Sixth ∧
                                          P TauCeti.RootfulNiemeierType.a4Sixth ∧
                                            P TauCeti.RootfulNiemeierType.a3Eighth ∧
                                              P TauCeti.RootfulNiemeierType.a2Twelfth ∧
                                                P TauCeti.RootfulNiemeierType.a1TwentyFourth
```

## Depends on

- [TauCeti.RootfulNiemeierType](tauceti-rootfulniemeiertype.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RootfulNiemeierType.forall`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/RootSystems.html#TauCeti.RootfulNiemeierType.forall).

## Sources

- [Tau Ceti documentation: `TauCeti.RootfulNiemeierType.forall`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/RootSystems.html#TauCeti.RootfulNiemeierType.forall)
- [Source of `TauCeti.RootfulNiemeierType.forall` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/RootSystems.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/RootSystems.lean#L99)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
