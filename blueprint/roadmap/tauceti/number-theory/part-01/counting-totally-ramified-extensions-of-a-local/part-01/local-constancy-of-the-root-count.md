---
declaration: theorem
origin: cited
lean: TauCeti.exists_card_aroots_eq
statement: formalized
proof: formalized
---

# Local constancy of the root count

For a monic `f` over `𝒪[K]` that is separable over
`K`, there is a threshold `T > 0` such that every monic `g` over `𝒪[K]` with
`g.coeff i - f.coeff i ∈ 𝓂[K] ^ T` for all `i` has as many roots as `f`, counted with
multiplicity, in every finite intermediate field of `Ω / K`. The threshold depends only on `f`.

```lean
TauCeti.exists_card_aroots_eq.{u_1, u_2} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (Ω : Type u_2) [Field Ω] [Algebra K Ω]
  {f : Polynomial ↥(ValuativeRel.valuation K).integer} (hf : f.Monic)
  (hfsep : (Polynomial.map (algebraMap (↥(ValuativeRel.valuation K).integer) K) f).Separable) :
  ∃ T,
    0 < T ∧
      ∀ (M : IntermediateField K Ω) [Module.Finite K ↥M]
        (g : Polynomial ↥(ValuativeRel.valuation K).integer),
        g.Monic →
          (∀ (i : ℕ),
              g.coeff i - f.coeff i ∈
                IsLocalRing.maximalIdeal ↥(ValuativeRel.valuation K).integer ^ T) →
            ((Polynomial.map (algebraMap (↥(ValuativeRel.valuation K).integer) K) g).aroots
                  ↥M).card =
              ((Polynomial.map (algebraMap (↥(ValuativeRel.valuation K).integer) K) f).aroots
                  ↥M).card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](hensels-lemma-with-an-estimate-over-a-henselian.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_card_aroots_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/RootCount/Basic.html#TauCeti.exists_card_aroots_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_card_aroots_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/RootCount/Basic.html#TauCeti.exists_card_aroots_eq)
- [Source of `TauCeti.exists_card_aroots_eq` in TauCeti/NumberTheory/LocalField/RootCount/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/RootCount/Basic.lean#L113)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
