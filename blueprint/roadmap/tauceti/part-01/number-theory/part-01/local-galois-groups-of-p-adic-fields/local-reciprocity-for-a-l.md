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

- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/part-02/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP).

## Sources

- [Tau Ceti documentation: `TauCeti.padicCompletionUnitsEquivAbelianizationProP`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.html#TauCeti.padicCompletionUnitsEquivAbelianizationProP)
- [Source of `TauCeti.padicCompletionUnitsEquivAbelianizationProP` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Reciprocity.lean#L157)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalGaloisGroups/STATUS.md)
