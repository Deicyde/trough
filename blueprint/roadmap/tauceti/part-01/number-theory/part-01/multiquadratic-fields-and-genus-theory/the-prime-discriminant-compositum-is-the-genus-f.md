---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.isGenusField_candidateGenusField
statement: formalized
proof: formalized
---

# The prime-discriminant compositum is the genus field in the imaginary quadratic case

For a squarefree negative integer `d`, `candidateGenusField hd` is abelian over `ℚ`, is unramified
at every place over its embedded copy of `ℚ(√d)`, and admits a root-preserving embedding from
every other abelian extension with those properties.

```lean
TauCeti.Multiquadratic.isGenusField_candidateGenusField.{v} {d : ℤ} (hd : Squarefree d)
  (hneg : d < 0) :
  TauCeti.Multiquadratic.IsGenusField d (↥(TauCeti.Multiquadratic.candidateGenusField hd))
    (TauCeti.Multiquadratic.candidateGenusFieldBaseRoot hd)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The converse of the multiquadratic degree theorem](../../part-02/multiquadratic/the-converse-of-the-multiquadratic-degree-theore.md)
- [Degree of a multiquadratic field over a finite index](degree-of-a-multiquadratic-field-over-a-finite-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.isGenusField_candidateGenusField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/GenusField.html#TauCeti.Multiquadratic.isGenusField_candidateGenusField).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.isGenusField_candidateGenusField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/GenusField.html#TauCeti.Multiquadratic.isGenusField_candidateGenusField)
- [Source of `TauCeti.Multiquadratic.isGenusField_candidateGenusField` in TauCeti/NumberTheory/Multiquadratic/GenusField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/GenusField.lean#L111)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Multiquadratic/STATUS.md)
