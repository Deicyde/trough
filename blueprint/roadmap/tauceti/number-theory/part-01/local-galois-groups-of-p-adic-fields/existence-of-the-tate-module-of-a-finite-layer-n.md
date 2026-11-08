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

- [The Artin map is transported by a layer isomorphism matching the invariant maps](../../part-02/class-field-theory/the-artin-map-is-transported-by-a-layer-isomorph.md)
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Dimension shifting in every positive degree, `Hⁱ⁺¹(G, M) ≅ Hⁱ(G, Coind_1^G M ⧸ M)` for `i ≥ 1` and a compact group `G`, as an isomorphism of Mathlib's canonical continuous cohomology](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree-hi-1.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The inverse of Shapiro's isomorphism is natural in the coefficients](../../../representation-theory/homological/the-inverse-of-shapiros-isomorphism-is-natural-i.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local class formation](../class-field-theory/the-local-class-formation.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Local reciprocity for `A(L)`](local-reciprocity-for-a-l.md)
- [Local Tate duality in degree one](../../part-02/class-field-theory/local-tate-duality-in-degree-one.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Schanuel's lemma in automorphism form](../../../algebra/module/schanuels-lemma-in-automorphism-form.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
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
- [Source of `TauCeti.nonempty_layerTateModule` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean#L90)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
