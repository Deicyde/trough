---
declaration: theorem
origin: cited
lean: TauCeti.RegularFormClass.wittDecomposition, QuadraticForm.exists_equivalent_hyperbolicPresentation_prod, TauCeti.eq_of_nsmul_hyperbolicClass_add_eq, TauCeti.exists_nsmul_hyperbolicClass_add
statement: formalized
proof: formalized
---

# Witt decomposition

a class is its Witt index worth of hyperbolic planes plus its
anisotropic part.

```lean
TauCeti.RegularFormClass.wittDecomposition.{u} {K : Type u} [Field K] [Invertible 2]
  (c : TauCeti.RegularFormClass K) : c = c.wittIndex • TauCeti.hyperbolicClass K + c.anisotropicPart
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.wittDecomposition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.html#TauCeti.RegularFormClass.wittDecomposition).

## Other forms

**Witt decomposition for a regular form.** Formalized in Tau Ceti as [`QuadraticForm.exists_equivalent_hyperbolicPresentation_prod`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.html#QuadraticForm.exists_equivalent_hyperbolicPresentation_prod).

```lean
QuadraticForm.exists_equivalent_hyperbolicPresentation_prod.{u, v} {K : Type u} [Field K]
  [Invertible 2] {V : Type v} [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V]
  (Q : QuadraticForm K V) (hQ : QuadraticMap.Nondegenerate) :
  ∃ p,
    QuadraticMap.Anisotropic (TauCeti.presentedForm p) ∧
      Module.finrank K V = 2 * (TauCeti.formClass Q hQ).wittIndex + p.fst ∧
        QuadraticMap.Equivalent Q
          (QuadraticMap.prod
            (TauCeti.presentedForm
              (TauCeti.hyperbolicPresentation K (TauCeti.formClass Q hQ).wittIndex))
            (TauCeti.presentedForm p))
```

**Witt decomposition (Lam I.4.1), uniqueness.** Formalized in Tau Ceti as [`TauCeti.eq_of_nsmul_hyperbolicClass_add_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.html#TauCeti.eq_of_nsmul_hyperbolicClass_add_eq).

```lean
TauCeti.eq_of_nsmul_hyperbolicClass_add_eq.{u} {K : Type u} [Field K] [Invertible 2] {m m' : ℕ}
  {a a' : TauCeti.RegularFormClass K} (ha : a.Anisotropic) (ha' : a'.Anisotropic)
  (h : m • TauCeti.hyperbolicClass K + a = m' • TauCeti.hyperbolicClass K + a') : m = m' ∧ a = a'
```

**Witt decomposition (Lam I.4.1), existence.** Formalized in Tau Ceti as [`TauCeti.exists_nsmul_hyperbolicClass_add`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.html#TauCeti.exists_nsmul_hyperbolicClass_add).

```lean
TauCeti.exists_nsmul_hyperbolicClass_add.{u} {K : Type u} [Field K] [Invertible 2]
  (c : TauCeti.RegularFormClass K) : ∃ m a, a.Anisotropic ∧ c = m • TauCeti.hyperbolicClass K + a
```

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.wittDecomposition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.html#TauCeti.RegularFormClass.wittDecomposition)
- [Source of `TauCeti.RegularFormClass.wittDecomposition` in TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/QuadraticForm/Witt/Decomposition.lean#L260)
