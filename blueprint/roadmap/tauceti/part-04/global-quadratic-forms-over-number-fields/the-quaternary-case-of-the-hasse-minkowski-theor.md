---
declaration: theorem
origin: cited
lean: QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary
statement: formalized
proof: formalized
---

# The quaternary case of the Hasse–Minkowski theorem

Let `Q` be a regular quaternary form
over a number field `K` which is isotropic at every finite and real place. If, over every number
field, every regular diagonal ternary form that is isotropic at every finite and real place is
isotropic, then `Q` is isotropic over `K`.

The ternary hypothesis is quantified over number fields because it is needed not only over `K` but
also over the quadratic field `K(√d)`, for `d` a nonsquare representative of the discriminant of
`Q`.

```lean
QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary.{u, v} {K : Type u} [Field K]
  [NumberField K] {V : Type v} [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V]
  {Q : QuadraticForm K V} (hQ : QuadraticMap.Nondegenerate) (hrank : Module.finrank K V = 4)
  (hloc : Q.IsLocallyIsotropic)
  (hternary :
    ∀ (L : Type u) [inst : Field L] [inst_1 : NumberField L]
      (p : TauCeti.RegularFormPresentation L),
      p.fst = 3 →
        (TauCeti.presentedForm p).IsLocallyIsotropic →
          ¬QuadraticMap.Anisotropic (TauCeti.presentedForm p)) :
  ¬QuadraticMap.Anisotropic Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Quaternary.html#QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary).

## Sources

- [Tau Ceti documentation: `QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Quaternary.html#QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary)
- [Source of `QuadraticForm.not_anisotropic_of_isLocallyIsotropic_quaternary` in TauCeti/NumberTheory/QuadraticForm/Global/Quaternary.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/Quaternary.lean#L129)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
