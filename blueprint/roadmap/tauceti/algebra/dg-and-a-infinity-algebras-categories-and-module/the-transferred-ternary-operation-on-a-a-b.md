---
declaration: theorem
origin: cited
lean: TauCeti.HeisenbergDGA.minimalModel_m_three
statement: formalized
proof: formalized
---

# The transferred ternary operation on `([a], [a], [b])`

`m₃^H ([a], [a], [b]) = [a c]`.
Of the Kontsevich--Soibelman/Merkulov tree sum only the term
`-p m₂ (i (τ [a]), h m₂ (i [a], i [b]))` survives, with `h (a b) = c` and the Koszul twist
`τ [a] = -[a]`.

```lean
TauCeti.HeisenbergDGA.minimalModel_m_three.{u_1} (R : Type u_1) [CommRing R] :
  ((TauCeti.HeisenbergDGA.minimalModel R).m 3)
      ![(TauCeti.HeisenbergDGA.aInfinityAlgebra R).cohomologyClass ⋯,
        (TauCeti.HeisenbergDGA.aInfinityAlgebra R).cohomologyClass ⋯,
        (TauCeti.HeisenbergDGA.aInfinityAlgebra R).cohomologyClass ⋯] =
    (TauCeti.HeisenbergDGA.aInfinityAlgebra R).cohomologyClass ⋯
```

## Depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Proof depends on

- [The suspended Stasheff identity free of the structural coefficient holds exactly when the unsuspended one does](../homology/the-suspended-stasheff-identity-free-of-the-stru.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HeisenbergDGA.minimalModel_m_three`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.html#TauCeti.HeisenbergDGA.minimalModel_m_three).

## Sources

- [Tau Ceti documentation: `TauCeti.HeisenbergDGA.minimalModel_m_three`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.html#TauCeti.HeisenbergDGA.minimalModel_m_three)
- [Source of `TauCeti.HeisenbergDGA.minimalModel_m_three` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.lean#L623)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
