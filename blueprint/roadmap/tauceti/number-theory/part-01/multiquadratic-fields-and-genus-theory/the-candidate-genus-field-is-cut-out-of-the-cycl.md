---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup
statement: formalized
proof: formalized
---

# The candidate genus field is cut out of the cyclotomic field by the genus characters

For
squarefree `d` with fundamental discriminant `D` and a cyclotomic subfield `K ⊆ ℂ` of level `|D|`,
the candidate genus field of `ℚ(√d)` is the image in `ℂ` of the intermediate field of `K` that the
character correspondence attaches to the genus character group of `D`. The correspondence is
taken for the abelian Galois structure of the cyclotomic extension.

```lean
TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup.{u_1} {d : ℤ}
  (hd : Squarefree d) (K : IntermediateField ℚ ℂ) [NumberField ↥K]
  [IsCyclotomicExtension {(∏ P ∈ TauCeti.Multiquadratic.genusPrimeDiscriminants hd, P).natAbs} ℚ ↥K]
  (R : Type u_1) [CommRing R] [CharZero R]
  [HasEnoughRootsOfUnity R
      (Monoid.exponent
        (ZMod (∏ P ∈ TauCeti.Multiquadratic.genusPrimeDiscriminants hd, P).natAbs)ˣ)] :
  TauCeti.Multiquadratic.candidateGenusField hd =
    IntermediateField.map K.val
      ((IsCyclotomicExtension.Rat.intermediateFieldEquivSubgroupChar
            (∏ P ∈ TauCeti.Multiquadratic.genusPrimeDiscriminants hd, P).natAbs (↥K) R).symm
        (Subgroup.map (MulChar.ringHomCompHom (Int.castRingHom R))
          (TauCeti.Multiquadratic.genusCharGroup (TauCeti.Multiquadratic.genusPrimeDiscriminants hd)
            ⋯)))
```

## Depends on

- [TauCeti.Multiquadratic.genusCharGroup](tauceti-multiquadratic-genuschargroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Cyclotomic/CandidateGenusField.html#TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Cyclotomic/CandidateGenusField.html#TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup)
- [Source of `TauCeti.Multiquadratic.candidateGenusField_eq_map_characterSubfield_genusCharGroup` in TauCeti/NumberTheory/Multiquadratic/Cyclotomic/CandidateGenusField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Cyclotomic/CandidateGenusField.lean#L55)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)
