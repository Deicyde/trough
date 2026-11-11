---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq
statement: formalized
proof: formalized
---

# The Euler quotient is invariant under pseudo-isomorphism

Over a noetherian local ring of
dimension two with finite residue field, such as `O⟦T⟧`, a pseudo-isomorphism `M → N` satisfies
`#(M ⧸ rM) / #M[r] = #(N ⧸ rN) / #N[r]` for every scalar `r`. Both sides are `0` when the torsion
groups are infinite. For `r = ω_n` this lets the Euler quotient `#(M ⧸ ω_n M) / #M[ω_n]` of a
finitely generated module be computed on an elementary module, while the finiteness of the
coinvariants `M ⧸ ω_n M` and of the invariants `M[ω_n]` transfers by
`IsPseudoIsomorphism.finite_quotSMulTop_iff` and `IsPseudoIsomorphism.finite_torsionBy_iff`;
the individual orders need not agree.

```lean
TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq.{u_1, u_2, u_3}
  {A : Type u_1} [CommRing A] {M : Type u_2} {N : Type u_3} [AddCommGroup M] [_root_.Module A M]
  [AddCommGroup N] [_root_.Module A N] [IsLocalRing A] [IsNoetherianRing A]
  [Finite (IsLocalRing.ResidueField A)] (hdim : ringKrullDim A = 2) {f : M →ₗ[A] N} (r : A)
  (hf : TauCeti.Iwasawa.IsPseudoIsomorphism f) :
  ↑(Nat.card (QuotSMulTop r M)) / ↑(Nat.card ↥(Submodule.torsionBy A M r)) =
    ↑(Nat.card (QuotSMulTop r N)) / ↑(Nat.card ↥(Submodule.torsionBy A N r))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/PseudoIsomorphism.html#TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/PseudoIsomorphism.html#TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq)
- [Source of `TauCeti.Iwasawa.IsPseudoIsomorphism.natCard_quotSMulTop_div_natCard_torsionBy_eq` in TauCeti/RingTheory/Iwasawa/PseudoIsomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/PseudoIsomorphism.lean#L377)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
