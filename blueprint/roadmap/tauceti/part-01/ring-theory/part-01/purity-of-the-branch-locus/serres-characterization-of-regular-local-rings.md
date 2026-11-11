---
declaration: theorem
origin: cited
lean: TauCeti.isRegularLocalRing_tfae
statement: formalized
proof: formalized
---

# Serre's characterization of regular local rings

For a Noetherian local ring `R` with
residue field `κ`, the following are equivalent:
1. `κ` has finite projective dimension;
2. `R` has finite global dimension;
3. `R` is a regular local ring;
4. the global dimension of `R` is its Krull dimension;
5. the projective dimension of `κ` is `dim_κ 𝔪 / 𝔪²`.

Conditions 4 and 5 are the equalities `gl dim R = dim R` and `pd κ = dim_κ 𝔪 / 𝔪²` of 00OC,
which hold for a regular local ring; they are equivalent to regularity because `R` has finite
Krull dimension.

```lean
TauCeti.isRegularLocalRing_tfae.{v, u} {R : Type u} [CommRing R] [IsLocalRing R]
  [IsNoetherianRing R] [Small.{v, u} R] :
  [CategoryTheory.projectiveDimension ↧(Shrink.{v, u} (R ⧸ IsLocalRing.maximalIdeal R)) ≠ ⊤,
      TauCeti.globalDimension R < ⊤, IsRegularLocalRing R,
      TauCeti.globalDimension R = ringKrullDim R,
      CategoryTheory.projectiveDimension ↧(Shrink.{v, u} (R ⧸ IsLocalRing.maximalIdeal R)) =
        ↑(Module.finrank (IsLocalRing.ResidueField R) (IsLocalRing.CotangentSpace R))].TFAE
```

## Depends on

- [TauCeti.globalDimension](tauceti-globaldimension.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](the-global-dimension-of-a-regular-local-ring-is.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](serres-theorem-tauceti-isregularlocalring-of-has.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRegularLocalRing_tfae`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.isRegularLocalRing_tfae).

## Sources

- [Tau Ceti documentation: `TauCeti.isRegularLocalRing_tfae`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.isRegularLocalRing_tfae)
- [Source of `TauCeti.isRegularLocalRing_tfae` in TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean#L380)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
