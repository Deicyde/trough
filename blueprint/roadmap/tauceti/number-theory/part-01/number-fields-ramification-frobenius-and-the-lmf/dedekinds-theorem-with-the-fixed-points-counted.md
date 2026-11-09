---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt, TauCeti.NumberField.fullCycleType_galActionHom_restrict_eq_factorDegrees, TauCeti.NumberField.fullCycleType_galActionHom_restrict_minpoly_eq_map_natDegree_monicFactorsMod
statement: formalized
proof: formalized
---

# Dedekind's theorem, with the fixed points counted separately

The multiset of degrees of
the monic irreducible factors of `minpoly ℤ θ` modulo `p` is the cycle type of a Frobenius at a
prime above `p` acting on the roots of `minpoly ℚ θ`, together with one part `1` for each fixed
root. This is the form with the cycle type and the fixed points separated; the full cycle type of
`fullCycleType_galActionHom_restrict_minpoly_eq_map_natDegree_monicFactorsMod` packages the two
summands.

```lean
TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt.{u_1, u_2} {M : Type u_1} [Field M]
  [NumberField M] {p : ℕ} [Fact (Nat.Prime p)] {K : Type u_2} [Field K] [NumberField K]
  {θ : NumberField.RingOfIntegers K}
  (hsq : Squarefree (Polynomial.map (Int.castRingHom (ZMod p)) (minpoly ℤ θ)))
  [Fact (Polynomial.map (algebraMap ℚ M) (minpoly ℚ ↑θ)).Splits]
  (Q : Ideal (NumberField.RingOfIntegers M)) [Q.IsPrime] [Q.LiesOver (Ideal.span {↑p})]
  {σ : Gal(M/ℚ)} (hσ : IsArithFrobAt ℤ σ Q) :
  Multiset.map Polynomial.natDegree (RingOfIntegers.monicFactorsMod θ p).val =
    ((Polynomial.Gal.galActionHom (minpoly ℚ ↑θ) M)
          ((Polynomial.Gal.restrict (minpoly ℚ ↑θ) M) σ)).cycleType +
      Multiset.replicate
        (Nat.card
          ↑(Function.fixedPoints
              ⇑((Polynomial.Gal.galActionHom (minpoly ℚ ↑θ) M)
                  ((Polynomial.Gal.restrict (minpoly ℚ ↑θ) M) σ))))
        1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt).

## Other forms

**Dedekind's theorem.** Formalized in Tau Ceti as [`TauCeti.NumberField.fullCycleType_galActionHom_restrict_eq_factorDegrees`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.fullCycleType_galActionHom_restrict_eq_factorDegrees).

```lean
TauCeti.NumberField.fullCycleType_galActionHom_restrict_eq_factorDegrees.{u_1} {M : Type u_1}
  [Field M] [NumberField M] {f : Polynomial ℤ} {p : ℕ} [Fact (Nat.Prime p)] (hf : f.Monic)
  (hsq : Squarefree (Polynomial.map (Int.castRingHom (ZMod p)) f))
  [Fact (Polynomial.map (algebraMap ℚ M) (Polynomial.map (Int.castRingHom ℚ) f)).Splits]
  (Q : Ideal (NumberField.RingOfIntegers M)) [Q.IsPrime] [Q.LiesOver (Ideal.span {↑p})]
  {σ : Gal(M/ℚ)} (hσ : IsArithFrobAt ℤ σ Q) :
  ((Polynomial.Gal.galActionHom (Polynomial.map (Int.castRingHom ℚ) f) M)
        ((Polynomial.Gal.restrict (Polynomial.map (Int.castRingHom ℚ) f) M) σ)).fullCycleType =
    f.factorDegrees p
```

**Dedekind's theorem for a generator.** Formalized in Tau Ceti as [`TauCeti.NumberField.fullCycleType_galActionHom_restrict_minpoly_eq_map_natDegree_monicFactorsMod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.fullCycleType_galActionHom_restrict_minpoly_eq_map_natDegree_monicFactorsMod).

```lean
TauCeti.NumberField.fullCycleType_galActionHom_restrict_minpoly_eq_map_natDegree_monicFactorsMod.{u_1,
    u_2}
  {M : Type u_1} [Field M] [NumberField M] {p : ℕ} [Fact (Nat.Prime p)] {K : Type u_2} [Field K]
  [NumberField K] {θ : NumberField.RingOfIntegers K}
  (hsq : Squarefree (Polynomial.map (Int.castRingHom (ZMod p)) (minpoly ℤ θ)))
  [Fact (Polynomial.map (algebraMap ℚ M) (minpoly ℚ ↑θ)).Splits]
  (Q : Ideal (NumberField.RingOfIntegers M)) [Q.IsPrime] [Q.LiesOver (Ideal.span {↑p})]
  {σ : Gal(M/ℚ)} (hσ : IsArithFrobAt ℤ σ Q) :
  ((Polynomial.Gal.galActionHom (minpoly ℚ ↑θ) M)
        ((Polynomial.Gal.restrict (minpoly ℚ ↑θ) M) σ)).fullCycleType =
    Multiset.map Polynomial.natDegree (RingOfIntegers.monicFactorsMod θ p).val
```

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt)
- [Source of `TauCeti.NumberField.factorizationType_eq_cycleType_isArithFrobAt` in TauCeti/NumberTheory/NumberField/Frobenius/CycleType.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.lean#L186)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/NumberFieldArithmetic/STATUS.md)
