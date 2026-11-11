---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top
statement: formalized
proof: formalized
---

# Minkowski's class-group generation bound

The classes of nonzero prime ideals of norm
at most `B` generate the class group whenever `B` is at least the Minkowski bound.

In particular, the exact Minkowski bound can be used by taking `hB := le_rfl`.

```lean
TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top.{u_1} (K : Type u_1) [Field K]
  [NumberField K] {B : ℝ}
  (hB :
    (4 / Real.pi) ^ NumberField.InfinitePlace.nrComplexPlaces K *
        (↑(Module.finrank ℚ K).factorial / ↑(Module.finrank ℚ K) ^ Module.finrank ℚ K *
          √|↑(NumberField.discr K)|) ≤
      B) :
  Subgroup.closure
      (IsDedekindDomain.HeightOneSpectrum.classGroupMk '' {v | ↑(Ideal.absNorm v.asIdeal) ≤ B}) =
    ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ClassNumber/Minkowski.html#TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ClassNumber/Minkowski.html#TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top)
- [Source of `TauCeti.NumberField.closure_classGroupMk_image_absNorm_le_eq_top` in TauCeti/NumberTheory/NumberField/ClassNumber/Minkowski.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/ClassNumber/Minkowski.lean#L37)
