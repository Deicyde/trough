---
declaration: theorem
origin: cited
lean: Polynomial.exists_isRoot_addVal_eval_eq, PowerSeries.henselianLocalRing, TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem, TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow, Polynomial.existsUnique_isRoot_addVal_lt, Polynomial.exists_isRoot_sub_mem
statement: formalized
proof: formalized
---

# Hensel's lemma with an estimate over a Henselian discrete valuation ring

If the order of
`F` at `y₀` exceeds twice the order of its derivative there, then `F` has a root `z` whose
distance to `y₀` has order exactly `addVal (F(y₀)) - addVal (F'(y₀))`. This is the existence
part of Mathlib's `hensels_lemma` in `addVal` spelling; the uniqueness of `z` in that ball is
`Polynomial.existsUnique_isRoot_addVal_lt`.

```lean
Polynomial.exists_isRoot_addVal_eval_eq.{u_1} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsDiscreteValuationRing A] [HenselianLocalRing A] (F : Polynomial A) (y₀ : A)
  (hlt :
    (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) +
        (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) <
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ F)) :
  ∃ z,
    F.IsRoot z ∧
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ F) =
        (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) +
          (IsDiscreteValuationRing.addVal A) (z - y₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's estimate](../../../../algebraic-topology/belyi-maps-dessins-denfants-and-three-point-cove/taylors-estimate.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.exists_isRoot_addVal_eval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Hensel.html#Polynomial.exists_isRoot_addVal_eval_eq).

## Other forms

**Hensel's lemma for `K⟦t⟧`.** Formalized in Tau Ceti as [`PowerSeries.henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Hensel.html#PowerSeries.henselianLocalRing).

```lean
PowerSeries.henselianLocalRing.{u_1} {K : Type u_1} [Field K] : HenselianLocalRing (PowerSeries K)
```

**Hensel's lemma for the norm.** Formalized in Tau Ceti as [`TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Norm/Henselian.html#TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem).

```lean
TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem.{u_1, u_2} {R : Type u_1} {S : Type u_2} [CommRing R]
  [CommRing S] [Algebra R S] [Module.Free R S] [Module.Finite R S] {I : Ideal R} [HenselianRing R I]
  {w : S} (hw : IsUnit w) (htr : IsUnit ((Algebra.trace R S) w)) {a : S} {v : R} (hv : IsUnit v)
  (hav : (Algebra.norm R) a - v ∈ I) :
  ∃ y, (Algebra.norm R) y = v ∧ y - a ∈ Ideal.map (algebraMap R S) I
```

**Hensel's lemma with a derivative dividing `π ^ k`.** Formalized in Tau Ceti as [`TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Newton.html#TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow).

```lean
TauCeti.IsAdicComplete.existsUnique_eval_eq_zero_of_dvd_pow.{u_1} {R : Type u_1} [CommRing R]
  {π : R} {f : Polynomial R} {k : ℕ} {t : R} [IsAdicComplete (Ideal.span {π}) R]
  (hπ : IsLeftRegular π) (hd : Polynomial.eval t (Polynomial.derivative f) ∣ π ^ k)
  (ht : π ^ (2 * k + 1) ∣ Polynomial.eval t f) : ∃! u, π ^ (k + 1) ∣ u - t ∧ Polynomial.eval u f = 0
```

**Hensel's lemma with uniqueness over a Henselian discrete valuation ring.** Formalized in Tau Ceti as [`Polynomial.existsUnique_isRoot_addVal_lt`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Hensel.html#Polynomial.existsUnique_isRoot_addVal_lt).

```lean
Polynomial.existsUnique_isRoot_addVal_lt.{u_1} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsDiscreteValuationRing A] [HenselianLocalRing A] (F : Polynomial A) (y₀ : A)
  (hlt :
    (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) +
        (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) <
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ F)) :
  ∃! z,
    F.IsRoot z ∧
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) <
        (IsDiscreteValuationRing.addVal A) (z - y₀)
```

**Hensel's lemma without monicity.** Formalized in Tau Ceti as [`Polynomial.exists_isRoot_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Basic.html#Polynomial.exists_isRoot_sub_mem).

```lean
Polynomial.exists_isRoot_sub_mem.{u_1} {R : Type u_1} [CommRing R] {J : Ideal R} [HenselianRing R J]
  (f : Polynomial R) {a₀ : R} (h₁ : Polynomial.eval a₀ f ∈ J)
  (h₂ : IsUnit ((Ideal.Quotient.mk J) (Polynomial.eval a₀ (Polynomial.derivative f)))) :
  ∃ a, f.IsRoot a ∧ a - a₀ ∈ J
```

## Sources

- [Tau Ceti documentation: `Polynomial.exists_isRoot_addVal_eval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Hensel.html#Polynomial.exists_isRoot_addVal_eval_eq)
- [Source of `Polynomial.exists_isRoot_addVal_eval_eq` in TauCeti/RingTheory/DiscreteValuationRing/Hensel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DiscreteValuationRing/Hensel.lean#L126)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
