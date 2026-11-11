---
declaration: theorem
origin: cited
lean: TauCeti.ae_tsum_rootCount_eq
statement: formalized
proof: formalized
---

# TauCeti.ae_tsum_rootCount_eq

Almost everywhere on the Eisenstein region, the root counts over all totally ramified
degree-`n` subextensions sum to `n`. This also holds in equal characteristic, because the
inseparable Eisenstein polynomials have measure zero.

```lean
TauCeti.ae_tsum_rootCount_eq.{u_1} {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] {n : ℕ} [MeasurableSpace (Fin n → K)] [BorelSpace (Fin n → K)]
  (μ : MeasureTheory.Measure (Fin n → K)) [μ.IsAddHaarMeasure] :
  ∀ᵐ (a : Fin n → K) ∂μ.restrict (TauCeti.eisensteinSet K n),
    ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)), ↑((↑L).rootCount a) = ↑n
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_tsum_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.html#TauCeti.ae_tsum_rootCount_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.ae_tsum_rootCount_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.html#TauCeti.ae_tsum_rootCount_eq)
- [Source of `TauCeti.ae_tsum_rootCount_eq` in TauCeti/NumberTheory/LocalField/MassFormula/RootCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.lean#L133)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
