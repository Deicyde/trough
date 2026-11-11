---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain
statement: formalized
proof: formalized
---

# The volume of a unit fundamental domain (Neukirch VII (5.6))

every fundamental domain `D`
for the action of the units on the norm-one hypersurface has `d*x`-mass `2^(r - 1) R / 2^r₂`,
where `r = r₁ + r₂` is the number of infinite places and `R` the regulator. Neukirch's value
`2^(r - 1) R` is for his canonical measure, which is `2^r₂` times `surfaceHaar K`.

```lean
TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {D : Set (NumberField.mixedEmbedding.realSpace K)}
  (hD : TauCeti.LFunctions.IsUnitFundamentalDomain K D) :
  (TauCeti.LFunctions.surfaceHaar K) (Subtype.val ⁻¹' D) =
    ENNReal.ofReal
      (2 ^
            (NumberField.InfinitePlace.nrRealPlaces K +
                NumberField.InfinitePlace.nrComplexPlaces K -
              1) *
          NumberField.Units.regulator K /
        2 ^ NumberField.InfinitePlace.nrComplexPlaces K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Surface/Volume.html#TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Surface/Volume.html#TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain)
- [Source of `TauCeti.LFunctions.surfaceHaar_of_isUnitFundamentalDomain` in TauCeti/NumberTheory/LFunctions/Theta/Surface/Volume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Theta/Surface/Volume.lean#L294)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
