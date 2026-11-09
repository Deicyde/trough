---
declaration: theorem
origin: cited
lean: QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank
statement: formalized
proof: formalized
---

# The Hasse–Minkowski induction step in rank at least five

Let `Q` be a regular quadratic
form of rank `n ≥ 5` over a number field that is isotropic at every finite and real place. If every
diagonal regular form of rank `n - 1` that is isotropic at every finite and real place is isotropic
over `K`, then `Q` is isotropic over `K`.

```lean
QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank.{u_1, u_2} {K : Type u_1}
  [Field K] [NumberField K] {X : Type u_2} [AddCommGroup X] [_root_.Module K X]
  [FiniteDimensional K X] {Q : QuadraticForm K X} (hQ : QuadraticMap.Nondegenerate)
  (hX : 5 ≤ Module.finrank K X) (hloc : Q.IsLocallyIsotropic)
  (ih :
    ∀ (p : TauCeti.RegularFormPresentation K),
      p.fst + 1 = Module.finrank K X →
        (TauCeti.presentedForm p).IsLocallyIsotropic →
          ¬QuadraticMap.Anisotropic (TauCeti.presentedForm p)) :
  ¬QuadraticMap.Anisotropic Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/HigherRank.html#QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank).

## Sources

- [Tau Ceti documentation: `QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/HigherRank.html#QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank)
- [Source of `QuadraticForm.not_anisotropic_of_isLocallyIsotropic_of_five_le_finrank` in TauCeti/NumberTheory/QuadraticForm/Global/HigherRank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/HigherRank.lean#L83)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
