---
declaration: def
origin: cited
lean: TauCeti.profiniteCyclotomicCharacter
statement: formalized
---

# TauCeti.profiniteCyclotomicCharacter

The continuous cyclotomic character of the absolute Galois group of a characteristic-zero
field `K`, recording its action on all roots of unity in `AlgebraicClosure K` with normalization
`σ ζ = ζ ^ χ_n(σ)` at each finite level `n`.

```lean
TauCeti.profiniteCyclotomicCharacter.{u_1, u_2} (K : Type u_1) [Field K] [CharZero K] :
  Field.absoluteGaloisGroup K →ₜ* (Additive ↑TauCeti.zHat.toProfinite.toTop)ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The product decomposition of the profinite integers](../../topology/profinite-integers-profinite-powers-and-continuo/the-product-decomposition-of-the-profinite-integ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.profiniteCyclotomicCharacter`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Cyclotomic/Profinite.html#TauCeti.profiniteCyclotomicCharacter).

## Sources

- [Tau Ceti documentation: `TauCeti.profiniteCyclotomicCharacter`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Cyclotomic/Profinite.html#TauCeti.profiniteCyclotomicCharacter)
- [Source of `TauCeti.profiniteCyclotomicCharacter` in TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Cyclotomic/Profinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Cyclotomic/Profinite.lean#L36)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
