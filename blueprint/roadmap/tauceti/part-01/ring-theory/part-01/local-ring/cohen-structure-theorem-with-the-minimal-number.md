---
declaration: theorem
origin: cited
lean: TauCeti.exists_surjective_mvPowerSeries_spanFinrank, TauCeti.exists_surjective_mvPowerSeries_of_span_eq_maximalIdeal
statement: formalized
proof: formalized
---

# Cohen structure theorem with the minimal number of variables

A complete local ring
containing a field whose maximal ideal `𝔪` is finitely generated has a coefficient field `s` and
is a quotient of the power series ring over its residue field in `spanFinrank 𝔪` variables, by a
surjection which is `s` on constants and sends the variables to generators of `𝔪`.

```lean
TauCeti.exists_surjective_mvPowerSeries_spanFinrank.{u_1, u_2} (k : Type u_1) (R : Type u_2)
  [Field k] [CommRing R] [IsLocalRing R] [Algebra k R]
  [IsAdicComplete (IsLocalRing.maximalIdeal R) R] (hfg : (IsLocalRing.maximalIdeal R).FG) :
  ∃ s,
    (∀ (a : IsLocalRing.ResidueField R), (IsLocalRing.residue R) (s a) = a) ∧
      ∃ φ,
        Function.Surjective ⇑φ ∧
          φ.comp MvPowerSeries.C = s ∧
            Ideal.span (Set.range fun i => φ (MvPowerSeries.X i)) = IsLocalRing.maximalIdeal R
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cohen's theorem: a complete local ring containing a field has a coefficient field](cohens-theorem-a-complete-local-ring-containing.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_surjective_mvPowerSeries_spanFinrank`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/CoefficientField.html#TauCeti.exists_surjective_mvPowerSeries_spanFinrank).

## Other forms

**Cohen structure theorem for complete local rings containing a field.** Formalized in Tau Ceti as [`TauCeti.exists_surjective_mvPowerSeries_of_span_eq_maximalIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/CoefficientField.html#TauCeti.exists_surjective_mvPowerSeries_of_span_eq_maximalIdeal).

```lean
TauCeti.exists_surjective_mvPowerSeries_of_span_eq_maximalIdeal.{u_1, u_2, u_3} (k : Type u_1)
  (R : Type u_2) [Field k] [CommRing R] [IsLocalRing R] [Algebra k R]
  [IsAdicComplete (IsLocalRing.maximalIdeal R) R] {σ : Type u_3} [Finite σ] (x : σ → R)
  (hx : Ideal.span (Set.range x) = IsLocalRing.maximalIdeal R) :
  ∃ s,
    (∀ (a : IsLocalRing.ResidueField R), (IsLocalRing.residue R) (s a) = a) ∧
      ∃ φ,
        Function.Surjective ⇑φ ∧ φ.comp MvPowerSeries.C = s ∧ ∀ (i : σ), φ (MvPowerSeries.X i) = x i
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_surjective_mvPowerSeries_spanFinrank`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/CoefficientField.html#TauCeti.exists_surjective_mvPowerSeries_spanFinrank)
- [Source of `TauCeti.exists_surjective_mvPowerSeries_spanFinrank` in TauCeti/RingTheory/LocalRing/CoefficientField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LocalRing/CoefficientField.lean#L160)
