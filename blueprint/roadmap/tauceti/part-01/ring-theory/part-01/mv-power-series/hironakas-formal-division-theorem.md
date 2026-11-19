---
declaration: theorem
origin: cited
lean: TauCeti.formalDivision, MonomialOrder.existsUnique_formalDivision
statement: formalized
proof: formalized
---

# Hironaka's formal division theorem

**Hironaka's formal division theorem** in `MvPowerSeries (Fin n) K` with respect to graded
lexicographic initial exponents (Bierstone–Milman 1997, Theorem 3.17).

```lean
TauCeti.formalDivision.{u_1} {K : Type u_1} [Field K] (n m : ℕ)
  (F : Fin m → MvPowerSeries (Fin n) K) (α : Fin m → Fin n →₀ ℕ)
  (hα : ∀ (i : Fin m), IsLeast (⇑toDegLex '' Function.support (F i)) (toDegLex (α i)))
  (G : MvPowerSeries (Fin n) K) :
  ∃! qr,
    G = ∑ i, qr.1 i * F i + qr.2 ∧
      (∀ (i : Fin m), ∀ β ∈ Function.support (qr.1 i), ∀ j < i, ¬α j ≤ α i + β) ∧
        ∀ β ∈ Function.support qr.2, ∀ (i : Fin m), ¬α i ≤ β
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.formalDivision`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/FormalDivision.html#TauCeti.formalDivision).

## Other forms

**Hironaka's formal division theorem for an arbitrary monomial order `ord` over a ring `R`.** Formalized in Tau Ceti as [`MonomialOrder.existsUnique_formalDivision`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/FormalDivision.html#MonomialOrder.existsUnique_formalDivision).

```lean
MonomialOrder.existsUnique_formalDivision.{u_1, u_2, u_3, u_4} {σ : Type u_1} {R : Type u_2}
  [Ring R] (ord : MonomialOrder σ) {ι : Type u_3} [Fintype ι] [LinearOrder ι]
  (F : ι → MvPowerSeries σ R) (α : ι → σ →₀ ℕ)
  (hα : ∀ (i : ι), IsLeast (⇑ord.toSyn '' Function.support (F i)) (ord.toSyn (α i)))
  (hu : ∀ (i : ι), IsUnit ((MvPowerSeries.coeff (α i)) (F i))) (G : MvPowerSeries σ R) :
  ∃! qr,
    G = ∑ i, qr.1 i * F i + qr.2 ∧
      (∀ (i : ι), ∀ β ∈ Function.support (qr.1 i), ∀ j < i, ¬α j ≤ α i + β) ∧
        ∀ β ∈ Function.support qr.2, ∀ (i : ι), ¬α i ≤ β
```

## Sources

- [Tau Ceti documentation: `TauCeti.formalDivision`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/FormalDivision.html#TauCeti.formalDivision)
- [Source of `TauCeti.formalDivision` in TauCeti/RingTheory/MvPowerSeries/FormalDivision.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPowerSeries/FormalDivision.lean#L965)
