---
declaration: theorem
origin: cited
lean: TauCeti.etale_aeval_of_basis, Ideal.isRegularLocalRing_localization_of_derivation_notMem, TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero, TauCeti.rank_jacobiMatrixAt_dehomogenize_div
statement: formalized
proof: formalized
---

# The Jacobian criterion for étaleness

If `T` is smooth over `R` and the differentials
`d aᵢ` of finitely many elements `aᵢ` of `T` form a basis of `Ω[T⁄R]`, then `T` is étale over the
polynomial ring `R[Xᵢ]` via `Xᵢ ↦ aᵢ`.

```lean
TauCeti.etale_aeval_of_basis.{u_1, u_3, u_4} {R : Type u_1} {T : Type u_3} [CommRing R] [CommRing T]
  [Algebra R T] [Algebra.Smooth R T] {ι : Type u_4} [Finite ι] (a : ι → T)
  (b : Module.Basis ι T Ω[T⁄R]) (hb : ∀ (i : ι), b i = (KaehlerDifferential.D R T) (a i)) :
  (MvPolynomial.aeval a).Etale
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.etale_aeval_of_basis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Kaehler/FormallyEtale.html#TauCeti.etale_aeval_of_basis).

## Other forms

**The Jacobian criterion for a hypersurface.** Formalized in Tau Ceti as [`Ideal.isRegularLocalRing_localization_of_derivation_notMem`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Hypersurface.html#Ideal.isRegularLocalRing_localization_of_derivation_notMem).

```lean
Ideal.isRegularLocalRing_localization_of_derivation_notMem.{u_1, u_2} {R : Type u_1} {A : Type u_2}
  [CommRing R] [CommRing A] [Algebra R A] {f : A} (P : Ideal (A ⧸ Ideal.span {f})) [P.IsPrime]
  [IsRegularLocalRing (Localization.AtPrime (Ideal.comap (Ideal.Quotient.mk (Ideal.span {f})) P))]
  {D : Derivation R A A} (hD : D f ∉ Ideal.comap (Ideal.Quotient.mk (Ideal.span {f})) P) :
  IsRegularLocalRing (Localization.AtPrime P)
```

**The Jacobian criterion for a single equation.** Formalized in Tau Ceti as [`TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero).

```lean
TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero.{u_2, u_3, u_4}
  {σ : Type u_2} {ι : Type u_3} {K : Type u_4} [Field K] [Unique ι] [Fintype σ]
  {p : ι → MvPolynomial σ K} {v : σ → K} :
  Function.Surjective (TauCeti.jacobiMatrixAt p v).mulVec ↔
    ∃ j, (MvPolynomial.eval v) ((MvPolynomial.pderiv j) (p default)) ≠ 0
```

**The Jacobian criterion in a ratio chart.** Formalized in Tau Ceti as [`TauCeti.rank_jacobiMatrixAt_dehomogenize_div`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.rank_jacobiMatrixAt_dehomogenize_div).

```lean
TauCeti.rank_jacobiMatrixAt_dehomogenize_div.{u_3, u_4} {ι : Type u_3} {K : Type u_4} [Field K]
  [Finite ι] {n : ℕ} (i : Fin (n + 1)) {p : ι → MvPolynomial (Fin (n + 1)) K} {d : ι → ℕ}
  (hp : ∀ (k : ι), (p k).IsHomogeneous (d k)) {b : Fin (n + 1) → K} (hi : b i ≠ 0)
  (hb : ∀ (k : ι), (MvPolynomial.eval b) (p k) = 0) :
  (TauCeti.jacobiMatrixAt (fun k => (TauCeti.dehomogenize i) (p k)) fun j =>
        b (i.succAbove j) / b i).rank =
    (TauCeti.jacobiMatrixAt p b).rank
```

## Sources

- [Tau Ceti documentation: `TauCeti.etale_aeval_of_basis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Kaehler/FormallyEtale.html#TauCeti.etale_aeval_of_basis)
- [Source of `TauCeti.etale_aeval_of_basis` in TauCeti/RingTheory/Kaehler/FormallyEtale.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Kaehler/FormallyEtale.lean#L147)
