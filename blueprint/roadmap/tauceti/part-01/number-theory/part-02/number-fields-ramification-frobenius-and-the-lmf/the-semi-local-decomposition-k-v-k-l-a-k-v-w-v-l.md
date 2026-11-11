---
declaration: def
origin: cited
lean: TauCeti.semilocalEquiv
statement: formalized
---

# The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`

completing `L` at the
finitely many places above a finite place `v` of `K` decomposes the scalar extension of `L` to
`K_v` into the product of those completions.

```lean
TauCeti.semilocalEquiv.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K] (L : Type u_2) [Field L]
  [NumberField L] [Algebra K L]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) :
  TensorProduct K (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
      L ≃ₐ[IsDedekindDomain.HeightOneSpectrum.adicCompletion K v]
    (w : { w // w.asIdeal.LiesOver v.asIdeal }) →
      IsDedekindDomain.HeightOneSpectrum.adicCompletion L ↑w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.semilocalEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/Basic.html#TauCeti.semilocalEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.semilocalEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/Basic.html#TauCeti.semilocalEquiv)
- [Source of `TauCeti.semilocalEquiv` in TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/Basic.lean#L195)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
