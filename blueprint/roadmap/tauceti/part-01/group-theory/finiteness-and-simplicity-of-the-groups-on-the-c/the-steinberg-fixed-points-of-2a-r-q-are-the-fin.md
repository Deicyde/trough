---
declaration: def
origin: cited
lean: TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints
statement: formalized
---

# The Steinberg fixed points of `²A_r(q)` are the finite special unitary group

They are
isomorphic to the points of `SL_{r+1}(𝔽_{q²})` fixed by the graph-twisted `q`-power Frobenius,
which are the determinant-one isometries of the sesquilinear form with the signed reversal Gram
matrix. The isomorphism is the coefficient extension to the closure followed by the inverse of
the carrier equivalence.

```lean
TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints (r : ℕ) (q : TauCeti.PrimePower)
  (hv : (TauCeti.LieTypeIndex.twistedA r q).Valid) :
  ↥(TauCeti.fixedSubgroup
        ((↑(TauCeti.TypeALieIndex.ofTwistedA r q hv)).galoisFieldTwistedFrobenius
          (↑(TauCeti.TypeALieIndex.ofTwistedA r q hv)).rank)) ≃*
    (TauCeti.TypeALieIndex.ofTwistedA r q hv).FixedPoints
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TwistedA.html#TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TwistedA.html#TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints)
- [Source of `TauCeti.TypeALieIndex.specialUnitaryEquivFixedPoints` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TwistedA.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TwistedA.lean#L69)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
