---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.globalInv_injective
statement: formalized
proof: formalized
---

# The global invariant is injective, because the idele-class `H¹` vanishes and the sum of the local invariants vanishes only on the classes that die in the idele classes

```lean
TauCeti.ClassFieldTheory.globalInv_injective {K : Type} [Field K] [NumberField K]
  (L : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K)) :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.globalInv K L)
```

## Depends on

- [The global invariant `H²(Gal(L/F), C_L) → ℚ/ℤ` of a finite normal layer `L/F` inside `Kˢ`](the-global-invariant-h2-gal-l-f-c-l-q-z-of-a-fin.md)

## Proof depends on

- [A prime-degree Galois extension has a prime with full decomposition group](a-prime-degree-galois-extension-has-a-prime-with.md)
- [The Artin map is transported by a layer isomorphism matching the invariant maps](../../part-02/class-field-theory/the-artin-map-is-transported-by-a-layer-isomorph.md)
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois action on the semi-local decomposition](../number-fields-ramification-frobenius-and-the-lmf/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The inverse of Shapiro's isomorphism is natural in the coefficients](../../../representation-theory/homological/the-inverse-of-shapiros-isomorphism-is-natural-i.md)
- [The Kummer case of the second fundamental inequality](../../part-02/class-field-theory/the-kummer-case-of-the-second-fundamental-inequa.md)
- [The local class formation](the-local-class-formation.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [The Mackey formula for the degree-one corestriction cochain](../../../representation-theory/homological/the-mackey-formula-for-the-degree-one-corestrict.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective)
- [Source of `TauCeti.ClassFieldTheory.globalInv_injective` in TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean#L245)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
