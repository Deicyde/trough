---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.localWeilArtinEquiv
statement: formalized
---

# Local reciprocity for the Weil group

For a nonarchimedean local field `K` of
characteristic zero, the local Artin map is an isomorphism of topological groups from `Kˣ` onto
the topological abelianization of the local Weil group (`localWeilArtinEquiv_apply`).

```lean
TauCeti.ClassFieldTheory.localWeilArtinEquiv (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [CharZero K] :
  Kˣ ≃ₜ* TopologicalAbelianization (TauCeti.ClassFieldTheory.WeilGroup K)
```

## Depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localWeilArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.html#TauCeti.ClassFieldTheory.localWeilArtinEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localWeilArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.html#TauCeti.ClassFieldTheory.localWeilArtinEquiv)
- [Source of `TauCeti.ClassFieldTheory.localWeilArtinEquiv` in TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.lean#L67)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
