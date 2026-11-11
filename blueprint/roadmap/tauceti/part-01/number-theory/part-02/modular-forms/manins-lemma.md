---
declaration: theorem
origin: cited
lean: TauCeti.ModularSymbols.degreeZero_eq_span_unimodular, TauCeti.ModularSymbols.span_degreeZeroRep_eq_top
statement: formalized
proof: formalized
---

# Manin's lemma

The degree-zero divisors on the cusps are spanned by the unimodular
symbols `[g∞] - [g0]`, `g ∈ SL(2, ℤ)`, that is, by the `SL(2, ℤ)`-translates of `[∞] - [0]`.

```lean
TauCeti.ModularSymbols.degreeZero_eq_span_unimodular.{u_1} {R : Type u_1} [Ring R] :
  TauCeti.ModularSymbols.degreeZero R =
    Submodule.span R
      (Set.range fun g =>
        MonoidAlgebra.single ((Matrix.SpecialLinearGroup.mapGL ℚ) g • OnePoint.infty) 1 -
          MonoidAlgebra.single ((Matrix.SpecialLinearGroup.mapGL ℚ) g • ↑0) 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularSymbols.degreeZero_eq_span_unimodular`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.html#TauCeti.ModularSymbols.degreeZero_eq_span_unimodular).

## Other forms

**Manin's lemma, inside `Div⁰(ℙ¹(ℚ))`.** Formalized in Tau Ceti as [`TauCeti.ModularSymbols.span_degreeZeroRep_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.html#TauCeti.ModularSymbols.span_degreeZeroRep_eq_top).

```lean
TauCeti.ModularSymbols.span_degreeZeroRep_eq_top.{u_1} {R : Type u_1} [Ring R] :
  Submodule.span R
      (Set.range fun g =>
        ((TauCeti.ModularSymbols.degreeZeroRep R) g)
          ⟨MonoidAlgebra.single OnePoint.infty 1 - MonoidAlgebra.single (↑0) 1, ⋯⟩) =
    ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.ModularSymbols.degreeZero_eq_span_unimodular`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.html#TauCeti.ModularSymbols.degreeZero_eq_span_unimodular)
- [Source of `TauCeti.ModularSymbols.degreeZero_eq_span_unimodular` in TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.lean#L185)
