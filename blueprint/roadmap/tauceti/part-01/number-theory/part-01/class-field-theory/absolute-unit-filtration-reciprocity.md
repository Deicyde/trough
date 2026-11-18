---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper
statement: formalized
proof: formalized
---

# Absolute unit-filtration reciprocity

For a nonarchimedean local field `K` in either
characteristic and every `n : ℕ`, the image of `U(K, n)` under `artinMap K` equals the image of
`localAbsoluteUpperRamificationGroup K n` in `G_K^ab` modulo the closed commutator subgroup of
`G_K` (Serre, *Local Fields*, XV §2, Theorem 2 and Corollary 3 to Theorem 1).

```lean
TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (n : ℕ) :
  Subgroup.map (TauCeti.ClassFieldTheory.artinMap K) (TauCeti.unitFiltration K n) =
    Subgroup.map (QuotientGroup.mk' (commutator (Field.absoluteGaloisGroup K)).topologicalClosure)
      (TauCeti.localAbsoluteUpperRamificationGroup K ⟨↑n, ⋯⟩)
```

## Depends on

- [The absolute upper ramification group of a local field](the-absolute-upper-ramification-group-of-a-local.md)
- [The local invariant](the-local-invariant.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Herbrand's theorem in the upper numbering](../local-fields-and-ramification/herbrands-theorem-in-the-upper-numbering.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [The upper-numbering theorem for finite local reciprocity](the-upper-numbering-theorem-for-finite-local-rec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.html#TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.html#TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper)
- [Source of `TauCeti.ClassFieldTheory.map_artinMap_unitFiltration_eq_upper` in TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.lean#L286)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
