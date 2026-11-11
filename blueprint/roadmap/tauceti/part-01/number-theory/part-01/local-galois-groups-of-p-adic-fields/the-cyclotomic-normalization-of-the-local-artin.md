---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit
statement: formalized
proof: formalized
---

# The cyclotomic normalization of the local Artin map of a finite extension of `ℚ_p`

Let
`F/ℚ_p` be finite. If `σ ∈ G_F` represents the absolute Artin symbol of a unit `u` of the valuation
ring of `F` (`v(u) = 1`), then the `p`-adic cyclotomic character of `σ` is the inverse of the norm
of `u`:

```text
χ_cyc (Art_F u) = N_{F/ℚ_p}(u)⁻¹.
```

```lean
TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit (p : ℕ) [Fact (Nat.Prime p)]
  (F : Type) [Field F] [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F]
  [Algebra ℚ_[p] F] [FiniteDimensional ℚ_[p] F] [ValuativeExtension ℚ_[p] F] (u : Fˣ)
  (hu : (ValuativeRel.valuation F) ↑u = 1) (σ : Field.absoluteGaloisGroup F)
  (hσ : ↑σ = (TauCeti.ClassFieldTheory.artinMap F) u) :
  (Units.map ↑(algebraMap ℤ_[p] ℚ_[p])) ((TauCeti.localCyclotomicCharacter p F) σ) =
    ((Units.map (Algebra.norm ℚ_[p])) u)⁻¹
```

## Depends on

- [The local class formation](../class-field-theory/the-local-class-formation.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.html#TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.html#TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit)
- [Source of `TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit` in TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.lean#L298)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
