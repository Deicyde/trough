---
declaration: def
origin: cited
lean: TauCeti.galEquivOfInjective
statement: formalized
---

# Artin's theorem for a finite group of automorphisms

An injective homomorphism
`f : H →* Gal(L/K)` from a finite group identifies `H` with the Galois group of `L` over the fixed
field of the image of `f` (`FixedPoints.toAlgAutMulEquiv`). No finiteness of `L/K` is needed.

```lean
TauCeti.galEquivOfInjective {K L : Type} [Field K] [Field L] [Algebra K L] {H : Type} [Group H]
  [Finite H] {f : H →* Gal(L/K)} (hf : Function.Injective ⇑f) :
  H ≃* Gal(L/↥(IntermediateField.fixedField f.range))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.galEquivOfInjective`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.html#TauCeti.galEquivOfInjective).

## Sources

- [Tau Ceti documentation: `TauCeti.galEquivOfInjective`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.html#TauCeti.galEquivOfInjective)
- [Source of `TauCeti.galEquivOfInjective` in TauCeti/FieldTheory/GaloisCohomology/Hilbert90.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.lean#L138)
