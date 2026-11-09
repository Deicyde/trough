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

- [The local class formation](../class-field-theory/the-local-class-formation.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP).

## Sources

- [Tau Ceti documentation: `TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP)
- [Source of `TauCeti.padicCompletionUnitsEquivAbelianizationProP` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean#L156)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
