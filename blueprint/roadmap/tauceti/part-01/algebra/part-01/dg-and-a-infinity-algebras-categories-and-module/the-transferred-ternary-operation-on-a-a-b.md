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

## Lean

Formalized in Tau Ceti as [`TauCeti.HeisenbergDGA.minimalModel_m_three`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.html#TauCeti.HeisenbergDGA.minimalModel_m_three).

## Sources

- [Tau Ceti documentation: `TauCeti.HeisenbergDGA.minimalModel_m_three`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.html#TauCeti.HeisenbergDGA.minimalModel_m_three)
- [Source of `TauCeti.HeisenbergDGA.minimalModel_m_three` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Heisenberg.lean#L623)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
