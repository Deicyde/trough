---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE, TauCeti.IsRegularLocalRing.of_globalDimension_lt_top
statement: formalized
proof: formalized
---

# Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)

A Noetherian local ring whose residue field has finite projective
dimension is a regular local ring. Its dimension is then that projective dimension, by
`TauCeti.IsRegularLocalRing.projectiveDimension_quotient_maximalIdeal_eq_ringKrullDim`.

```lean
TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE.{v, u} {R : Type u} [CommRing R]
  [IsLocalRing R] [IsNoetherianRing R] [Small.{v, u} R] (n : ℕ)
  [CategoryTheory.HasProjectiveDimensionLE (↧(Shrink.{v, u} (R ⧸ IsLocalRing.maximalIdeal R))) n] :
  IsRegularLocalRing R
```

## Depends on

- [TauCeti.globalDimension](tauceti-globaldimension.md)

## Proof depends on

- [Regularity lifts along a nonzerodivisor](../abhyankars-lemma-for-a-regular-divisor/regularity-lifts-along-a-nonzerodivisor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE).

## Other forms

**Serre's theorem, global dimension form.** Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.of_globalDimension_lt_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.IsRegularLocalRing.of_globalDimension_lt_top).

```lean
TauCeti.IsRegularLocalRing.of_globalDimension_lt_top.{v, u} {R : Type u} [CommRing R]
  [IsLocalRing R] [IsNoetherianRing R] [Small.{v, u} R] (h : TauCeti.globalDimension R < ⊤) :
  IsRegularLocalRing R
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE)
- [Source of `TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE` in TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean#L332)
