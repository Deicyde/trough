---
declaration: theorem
origin: cited
lean: TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq
statement: formalized
proof: formalized
---

# Jointly exchangeable arrays are exactly the Aldous--Hoover codings in law

An array process
with a.e.-measurable entries in a standard Borel space, on a probability space, is jointly
exchangeable if and only if its law is the law of a measurable joint Aldous--Hoover coding
`X i j = F(U, U_i, U_j, U_{i,j})` under independent uniform noise.

```lean
TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] [StandardBorelSpace α] {Ω : Type u_2} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ × ℕ → Ω → α}
  (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) :
  TauCeti.Probability.JointlyExchangeable μ X ↔
    ∃ F,
      Measurable F ∧
        MeasureTheory.Measure.map (fun u p => TauCeti.Probability.AldousHoover.jointArray F p u)
            (TauCeti.Probability.AldousHoover.noiseMeasure Unit (Sym2 ℕ)) =
          MeasureTheory.Measure.map (fun ω p => X p ω) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Joint/Representation.html#TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Joint/Representation.html#TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq)
- [Source of `TauCeti.Probability.jointlyExchangeable_iff_exists_map_jointArray_eq` in TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Joint/Representation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Joint/Representation.lean#L712)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Exchangeability/STATUS.md)
