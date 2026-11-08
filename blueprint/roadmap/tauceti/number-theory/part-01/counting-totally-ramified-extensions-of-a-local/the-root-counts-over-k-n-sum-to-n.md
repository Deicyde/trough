---
declaration: theorem
origin: cited
lean: TauCeti.tsum_rootCount_eq_of_separable
statement: formalized
proof: formalized
---

# The root counts over `σ_K(n)` sum to `n`

Let `f` be an Eisenstein polynomial over `𝒪[K]`
with image `monicOfCoeff a` over `K`, for `a : Fin n → K`, and assume that `monicOfCoeff a` is
separable. Then `∑_{L ∈ σ_K(n)} L.rootCount a = n`: each of the `n` roots of `monicOfCoeff a` in
the separable closure lies in exactly one member of `σ_K(n)`, the one it generates.

```lean
TauCeti.tsum_rootCount_eq_of_separable.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} {a : Fin n → K}
  {f : Polynomial ↥(ValuativeRel.valuation K).integer}
  (he : f.IsEisensteinAt (IsLocalRing.maximalIdeal ↥(ValuativeRel.valuation K).integer))
  (hf :
    Polynomial.map (algebraMap (↥(ValuativeRel.valuation K).integer) K) f =
      TauCeti.Polynomial.monicOfCoeff a)
  (hsep : (TauCeti.Polynomial.monicOfCoeff a).Separable) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)), ↑((↑L).rootCount a) = ↑n
```

## Depends on

- [IntermediateField.rootCount](intermediatefield-rootcount.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_rootCount_eq_of_separable`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.html#TauCeti.tsum_rootCount_eq_of_separable).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_rootCount_eq_of_separable`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.html#TauCeti.tsum_rootCount_eq_of_separable)
- [Source of `TauCeti.tsum_rootCount_eq_of_separable` in TauCeti/NumberTheory/LocalField/MassFormula/RootCount.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/RootCount.lean#L97)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
