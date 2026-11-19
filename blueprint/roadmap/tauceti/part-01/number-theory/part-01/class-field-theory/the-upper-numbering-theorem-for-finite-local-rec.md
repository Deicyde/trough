---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.normResidue_map_unitFiltration
statement: formalized
proof: formalized
---

# The upper-numbering theorem for finite local reciprocity

For every finite Galois extension
`L/K` of nonarchimedean local fields and every `n : ℕ`, the reciprocity homomorphism
`Kˣ → Kˣ ⧸ N_{L/K}(Lˣ) ≃* Gal(L/K)^ab` maps the unit group `U(K, n)` onto the image of the upper
ramification group `Gal(L/K)^n` in `Gal(L/K)^ab` (Neukirch, *Algebraic Number Theory*, V Theorem
6.2; Serre, *Local Fields*, XV §2, Theorem 1 and Corollary 3).

```lean
TauCeti.ClassFieldTheory.normResidue_map_unitFiltration.{u_1} (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (L : Type u_1) [Field L] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L]
  [Module.Finite K L] [IsGalois K L] (n : ℕ) :
  Subgroup.map
      ((TauCeti.ClassFieldTheory.normResidue K L).toMonoidHom.comp
        (QuotientGroup.mk' (TauCeti.normGroup K L)))
      (TauCeti.unitFiltration K n) =
    Subgroup.map Group.Abelianization.of
      (TauCeti.LocalFieldsRamification.upperRamificationGroup K L ⟨↑n, ⋯⟩)
```

## Depends on

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
- [Hilbert's formula, truncated](../../part-02/local-field/hilberts-formula-truncated.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/part-02/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.normResidue_map_unitFiltration`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.html#TauCeti.ClassFieldTheory.normResidue_map_unitFiltration).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.normResidue_map_unitFiltration`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.html#TauCeti.ClassFieldTheory.normResidue_map_unitFiltration)
- [Source of `TauCeti.ClassFieldTheory.normResidue_map_unitFiltration` in TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ClassFieldTheory/Local/UnitFiltration.lean#L129)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
