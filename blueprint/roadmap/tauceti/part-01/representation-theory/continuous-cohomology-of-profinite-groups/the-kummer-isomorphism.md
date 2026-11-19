---
declaration: def
origin: cited
lean: TauCeti.kummerIso
statement: formalized
---

# The Kummer isomorphism

**The Kummer isomorphism** `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following
it), for `n` invertible in `K`. It is `TauCeti.kummerClassMap`, which is injective since the
kernel of the Kummer map is `(Kˣ)ⁿ` and surjective by Hilbert 90.

```lean
TauCeti.kummerIso.{u_1} (K : Type u_1) [Field K] (n : ℕ) (hn : IsUnit ↑n) :
  TauCeti.powerClassQuotient Kˣ n ≃*
    Multiplicative
      (TauCeti.ContCohomology.H1 (TauCeti.AbsoluteGaloisGroup K) (TauCeti.KummerCoeff K n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.kummerIso`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Kummer.html#TauCeti.kummerIso).

## Sources

- [Tau Ceti documentation: `TauCeti.kummerIso`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Kummer.html#TauCeti.kummerIso)
- [Source of `TauCeti.kummerIso` in TauCeti/FieldTheory/GaloisCohomology/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisCohomology/Kummer.lean#L383)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
