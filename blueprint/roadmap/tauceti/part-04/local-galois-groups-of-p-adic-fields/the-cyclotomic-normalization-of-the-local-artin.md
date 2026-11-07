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

- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](../../part-01/class-field-theory/tauceti-classfieldtheory-classformation-tateiso.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.invMap](../../part-01/class-field-theory/tauceti-classfieldtheory-invmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.html#TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.html#TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit)
- [Source of `TauCeti.ClassFieldTheory.localCyclotomicCharacter_artinMap_unit` in TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/ExplicitCyclotomicSymbol/ArtinMap.lean#L302)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
