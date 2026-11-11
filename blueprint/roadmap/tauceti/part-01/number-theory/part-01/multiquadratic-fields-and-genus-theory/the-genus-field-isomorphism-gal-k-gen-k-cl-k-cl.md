---
declaration: def
origin: cited
lean: TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient
statement: formalized
---

# The genus-field isomorphism `Gal(K_gen/K) ≅ Cl⁺(K)/Cl⁺(K)²`

For a squarefree integer `d`
that is not a rational square, the Galois group of the candidate genus field over its embedded
quadratic base `K = ℚ(√d)` is isomorphic to the maximal elementary-`2` quotient of the narrow class
group of `K`. Both are the space of even-parity sign patterns on the prime discriminants dividing
`disc K`: the Galois group by its sign patterns, the class group by its genus characters.

The map is pinned down coordinate for coordinate on those prime discriminants: it sends an
automorphism `σ` to the unique narrow class modulo squares whose genus characters are the signs
that `σ` puts on the chosen square roots
(`autCandidateGenusFieldEquivNarrowElementaryTwoQuotient_apply` together with
`narrowElementaryTwoQuotientEquivRelativeSign_apply_coe`). Its identification with the inverse
Artin map of `K_gen / K` is not proved here; see the module docstring.

```lean
TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient {d : ℤ}
  (hd : Squarefree d) (hnsq : ¬IsSquare ↑d) :
  Gal(↥(TauCeti.Multiquadratic.candidateGenusField
          hd)/↥(TauCeti.Multiquadratic.candidateGenusFieldBase hd)) ≃*
    Multiplicative
      (NumberField.NarrowClassGroup.ElementaryTwoQuotient
        ↥(TauCeti.Multiquadratic.candidateGenusFieldBase hd))
```

## Depends on

- [The genus character on the narrow class group](the-genus-character-on-the-narrow-class-group.md)
- [NumberField.NarrowClassGroup](numberfield-narrowclassgroup.md)

## Proof depends on

- [The `2`-rank formula for the narrow class group of a quadratic field](the-2-rank-formula-for-the-narrow-class-group-of.md)
- [Degree of a multiquadratic field over a finite index](degree-of-a-multiquadratic-field-over-a-finite-i.md)
- [Dirichlet's theorem for prime-discriminant characters](../../part-02/multiquadratic/dirichlets-theorem-for-prime-discriminant-charac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/CandidateGenusField/Relative/GenusCharacter.html#TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/CandidateGenusField/Relative/GenusCharacter.html#TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient)
- [Source of `TauCeti.Multiquadratic.autCandidateGenusFieldEquivNarrowElementaryTwoQuotient` in TauCeti/NumberTheory/Multiquadratic/CandidateGenusField/Relative/GenusCharacter.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/CandidateGenusField/Relative/GenusCharacter.lean#L155)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Multiquadratic/STATUS.md)
