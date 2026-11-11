---
declaration: theorem
origin: cited
lean: NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver
statement: formalized
proof: formalized
---

# Absolute values over a finite place

Let `F / K` be a finite extension of number fields.
An absolute value `w` of `F` lying over the finite place `FinitePlace.mk 𝔭` of `K` is
`y ↦ FinitePlace.mk 𝔓 y ^ (e * f)⁻¹` for a unique prime `𝔓` of `𝓞 F` over `𝔭`, where `e` and `f`
are the ramification index and the inertia degree of `𝔓` over `𝔭`.

```lean
NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver.{u_1, u_2} {K : Type u_1}
  {F : Type u_2} [Field K] [Field F] [NumberField K] [NumberField F] [Algebra K F]
  {𝔭 : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)} {w : AbsoluteValue F ℝ}
  [w.LiesOver ↑(NumberField.FinitePlace.mk 𝔭)] :
  ∃! 𝔓,
    𝔓.asIdeal.LiesOver 𝔭.asIdeal ∧
      ∀ (y : F),
        w y =
          (NumberField.FinitePlace.mk 𝔓) y ^
            (↑(𝔓.asIdeal.ramificationIdx (NumberField.RingOfIntegers K)) *
                ↑(𝔓.asIdeal.inertiaDeg (NumberField.RingOfIntegers K)))⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PlacesOver/FinitePlace.html#NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver).

## Sources

- [Tau Ceti documentation: `NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PlacesOver/FinitePlace.html#NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver)
- [Source of `NumberField.existsUnique_finitePlace_rpow_inv_eq_of_liesOver` in TauCeti/NumberTheory/NumberField/PlacesOver/FinitePlace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/PlacesOver/FinitePlace.lean#L193)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
