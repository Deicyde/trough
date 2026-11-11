---
declaration: def
origin: cited
lean: PowerSeries.multiplicativeSequence
statement: formalized
---

# PowerSeries.multiplicativeSequence

The **multiplicative sequence** belonging to the power series `Q`, in `n` variables:
`Q.multiplicativeSequence n k` is the unique polynomial `Kₖ` such that substituting the
elementary symmetric polynomials `e₁, …, eₙ` of `x₁, …, xₙ` gives the coefficient of `tᵏ` in
`∏ᵢ Q(xᵢ t)`. The variable `j : Fin n` stands for `e_{j+1}`, following
`MvPolynomial.esymmAlgHom`.

```lean
PowerSeries.multiplicativeSequence.{u_1} {R : Type u_1} [CommRing R] (Q : PowerSeries R) (n k : ℕ) :
  MvPolynomial (Fin n) R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.multiplicativeSequence).

## Sources

- [Tau Ceti documentation: `PowerSeries.multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.multiplicativeSequence)
- [Source of `PowerSeries.multiplicativeSequence` in TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean#L105)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
