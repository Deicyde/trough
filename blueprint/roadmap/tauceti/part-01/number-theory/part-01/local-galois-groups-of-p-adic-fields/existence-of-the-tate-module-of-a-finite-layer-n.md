---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_layerTateModule
statement: formalized
proof: formalized
---

# Existence of the Tate module of a finite layer (NSW (5.6.5) and the proof of (7.4.1))

For
a finite Galois extension `L/K` of `p`-adic fields there is a finitely generated
`ℤ_p[Gal(L/K)]`-module of projective dimension at most one which is an extension of the
augmentation ideal by `A(L)`.

```lean
TauCeti.nonempty_layerTateModule.{u} (p : ℕ) [Fact (Nat.Prime p)] (K L : Type u) [Field L] [Field K]
  [Algebra K L] [Algebra ℚ_[p] L] [Module.Finite ℚ_[p] L] [Algebra ℚ_[p] K]
  [IsScalarTower ℚ_[p] K L] [IsGalois K L] : Nonempty (TauCeti.LayerTateModule p L K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Dimension shifting in every positive degree](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local class formation](../class-field-theory/the-local-class-formation.md)
- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Local reciprocity for `A(L)`](local-reciprocity-for-a-l.md)
- [Local Tate duality in degree one](../../part-02/class-field-theory/local-tate-duality-in-degree-one.md)
- [Nakayama–Rim, Sylow form](../../../representation-theory/homological/nakayama-rim-sylow-form.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The strict cohomological dimension through integral coefficients (NSW (3.3.4)), as vanishing predicates](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-strict-cohomological-dimension-through-integ.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_layerTateModule`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.html#TauCeti.nonempty_layerTateModule).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_layerTateModule`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.html#TauCeti.nonempty_layerTateModule)
- [Source of `TauCeti.nonempty_layerTateModule` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean#L90)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
