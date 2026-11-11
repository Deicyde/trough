---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary
statement: formalized
proof: formalized
---

# The structure theorem for Iwasawa modules

Let `O` be a discrete valuation ring with
uniformiser `ϖ`, complete for its maximal ideal. Every finitely generated `O⟦X⟧`-module admits a
pseudo-isomorphism onto an elementary module `O⟦X⟧ʳ × ∏ᵢ O⟦X⟧ ⧸ (ϖ ^ mᵢ) × ∏ⱼ O⟦X⟧ ⧸ (Fⱼ ^ nⱼ)`
with every `mᵢ` and `nⱼ` positive and every `Fⱼ` irreducible and distinguished.
Neukirch–Schmidt–Wingberg, Theorem (5.3.8).

```lean
TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary.{u_1, u_2} {O : Type u_1} [CommRing O]
  [IsDomain O] [IsDiscreteValuationRing O] [IsAdicComplete (IsLocalRing.maximalIdeal O) O] {ϖ : O}
  {M : Type u_2} [AddCommGroup M] [_root_.Module (PowerSeries O) M] (hϖ : Irreducible ϖ)
  [Module.Finite (PowerSeries O) M] :
  ∃ r a b m F n,
    (∀ (i : Fin a), m i ≠ 0) ∧
      (∀ (j : Fin b),
          (F j).IsDistinguishedAt (IsLocalRing.maximalIdeal O) ∧ Irreducible (F j) ∧ n j ≠ 0) ∧
        ∃ f, TauCeti.Iwasawa.IsPseudoIsomorphism f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The structure theorem over a regular local ring of dimension at most two](../../../ring-theory/part-02/other-results/part-02/the-structure-theorem-over-a-regular-local-ring.md)
- [Weierstrass preparation with a uniformiser power](../../part-01/newton-polygons-of-polynomials-and-power-series/weierstrass-preparation-with-a-uniformiser-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Elementary.html#TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/Elementary.html#TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary)
- [Source of `TauCeti.Iwasawa.exists_isPseudoIsomorphism_elementary` in TauCeti/RingTheory/Iwasawa/Elementary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/Elementary.lean#L67)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
