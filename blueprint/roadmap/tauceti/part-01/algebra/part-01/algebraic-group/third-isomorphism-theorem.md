---
declaration: def
origin: cited
lean: CommHopfAlgCat.Hom.quotientIsoQuotientQuotient
statement: formalized
---

# Third isomorphism theorem

For Hopf ideals `I ≤ J` of `H`, the quotient of `H` by `J` is
the quotient of `H ⧸ I` by the image of `J`: it is the inverse of the identification of that
quotient with `H ⧸ J` along `quotientMapOfLe`. The quotient morphism `q : H ⟶ H ⧸ I` is taken
together with `hq : q = mkQuotient H I`, so that this applies verbatim to a coordinate map that
is only propositionally the quotient morphism.

```lean
CommHopfAlgCat.Hom.quotientIsoQuotientQuotient.{u, v} {R : Type u} [CommRing R]
  {H : CommHopfAlgCat R} {I J : TauCeti.HopfIdeal R ↑H} (q : H ⟶ H.quotient I)
  (hq : q = H.mkQuotient I) (hIJ : I ≤ J) :
  H.quotient J ≅ (H.quotient I).quotient (J.map (CommHopfAlgCat.Hom.hom q))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CommHopfAlgCat.Hom.quotientIsoQuotientQuotient`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Basic.html#CommHopfAlgCat.Hom.quotientIsoQuotientQuotient).

## Sources

- [Tau Ceti documentation: `CommHopfAlgCat.Hom.quotientIsoQuotientQuotient`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Basic.html#CommHopfAlgCat.Hom.quotientIsoQuotientQuotient)
- [Source of `CommHopfAlgCat.Hom.quotientIsoQuotientQuotient` in TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Basic.lean#L605)
