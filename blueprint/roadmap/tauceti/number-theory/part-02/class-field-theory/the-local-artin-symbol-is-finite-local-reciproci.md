---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue
statement: formalized
proof: formalized
---

# The local Artin symbol is finite local reciprocity at a place above `v`

For `L/K` Galois
and a finite place `w` of `L` above `v`, the local Artin symbol at `v` of `x ∈ K_vˣ` is the image
of its norm residue symbol in `Gal(L_w/K_v)^ab` under the identification of `Gal(L_w/K_v)` with
the decomposition group of `w` (`IsDedekindDomain.HeightOneSpectrum.decompositionEquiv`).

```lean
TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue {K : Type} [Field K] [NumberField K]
  {L : Type} [Field L] [Algebra K L] [NumberField L] [IsGalois K L]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L))
  [w.asIdeal.LiesOver v.asIdeal] (x : (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)ˣ) :
  (TauCeti.ClassFieldTheory.localArtinAt K L v) x =
    (Abelianization.map
        ((MulAction.stabilizer Gal(L/K) w.asIdeal).subtype.comp
          (v.decompositionEquiv w).symm.toMonoidHom))
      ((TauCeti.ClassFieldTheory.normResidue (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
          (IsDedekindDomain.HeightOneSpectrum.adicCompletion L w))
        ↑x)
```

## Depends on

- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/FinitePlace.html#TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/FinitePlace.html#TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue)
- [Source of `TauCeti.ClassFieldTheory.localArtinAt_eq_map_normResidue` in TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/FinitePlace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/LocalArtin/FinitePlace.lean#L147)
