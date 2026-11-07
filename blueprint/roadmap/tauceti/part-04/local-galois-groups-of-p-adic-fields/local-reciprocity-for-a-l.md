---
declaration: def
origin: cited
lean: TauCeti.padicCompletionUnitsEquivAbelianizationProP
statement: formalized
---

# Local reciprocity for `A(L)`

If `V ≤ G_K` is the subgroup fixing the image of a finite
extension `L/K` under `ι : L →ₐ[K] Kˢ`, then the multiplicative `p`-adic completion `A(L)` of
`Lˣ` is canonically isomorphic to `V^ab(p)`, the maximal pro-`p` quotient of the topological
abelianization of `V`.

```lean
TauCeti.padicCompletionUnitsEquivAbelianizationProP (p : ℕ) [Fact (Nat.Prime p)] (K L : Type)
  [Field K] [Field L] [Algebra K L] [FiniteDimensional K L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [CharZero L] (ι : L →ₐ[K] SeparableClosure K) :
  ↥(TauCeti.padicCompletionUnits p L) ≃ₜ*
    TauCeti.abelianizationProP p (TauCeti.AbsoluteGaloisGroup K) ↑(TauCeti.galoisSubgroup K L ι)
```

## Depends on

- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](../../part-01/class-field-theory/tauceti-classfieldtheory-classformation-tateiso.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.invMap](../../part-01/class-field-theory/tauceti-classfieldtheory-invmap.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP).

## Sources

- [Tau Ceti documentation: `TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP)
- [Source of `TauCeti.padicCompletionUnitsEquivAbelianizationProP` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean#L156)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
