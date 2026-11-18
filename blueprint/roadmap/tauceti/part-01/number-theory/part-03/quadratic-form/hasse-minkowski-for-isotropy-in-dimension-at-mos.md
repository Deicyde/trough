---
declaration: theorem
origin: cited
lean: QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two, QuadraticForm.not_anisotropic_iff_isLocallyIsotropic_of_finrank_le_two
statement: formalized
proof: formalized
---

# Hasse–Minkowski for isotropy in dimension at most two, away from a finite set of finite places

A quadratic form of dimension `≤ 2` over a number field that is isotropic at all but
finitely many finite places is isotropic over `K`. Neither nondegeneracy nor an archimedean
hypothesis is needed.

```lean
QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two.{u, v}
  {K : Type u} [Field K] [NumberField K] {V : Type v} [AddCommGroup V] [_root_.Module K V]
  [FiniteDimensional K V] (Q : QuadraticForm K V) (hV : Module.finrank K V ≤ 2)
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)))
  (h : ∀ v ∉ S, ¬QuadraticMap.Anisotropic (Q.atFinitePlace v)) : ¬QuadraticMap.Anisotropic Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global square theorem (O'Meara 65:15)](the-global-square-theorem-omeara-65-15.md)
- [Witt decomposition](../../../linear-algebra/part-01/quadratic-form/witt-decomposition.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/LowRank.html#QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two).

## Other forms

**Hasse–Minkowski for isotropy in dimension at most two (O'Meara 66:1; Milne, VIII, Theorem 3.5(b) for `n = 2`).** Formalized in Tau Ceti as [`QuadraticForm.not_anisotropic_iff_isLocallyIsotropic_of_finrank_le_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/LowRank.html#QuadraticForm.not_anisotropic_iff_isLocallyIsotropic_of_finrank_le_two).

```lean
QuadraticForm.not_anisotropic_iff_isLocallyIsotropic_of_finrank_le_two.{u, v} {K : Type u} [Field K]
  [NumberField K] {V : Type v} [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V]
  (Q : QuadraticForm K V) (hV : Module.finrank K V ≤ 2) :
  ¬QuadraticMap.Anisotropic Q ↔ Q.IsLocallyIsotropic
```

## Sources

- [Tau Ceti documentation: `QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/LowRank.html#QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two)
- [Source of `QuadraticForm.not_anisotropic_of_not_anisotropic_atFinitePlace_of_notMem_of_finrank_le_two` in TauCeti/NumberTheory/QuadraticForm/Global/LowRank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/LowRank.lean#L63)
