---
declaration: abbrev
origin: cited
lean: AddEquiv.cyclicRep
statement: formalized
---

# AddEquiv.cyclicRep

The cyclic representation of `A` as an object of `Rep ℤ C_m`.

```lean
AddEquiv.cyclicRep.{u_1} {T : Type u_1} [AddCommGroup T] {m : ℕ} [NeZero m] (A : T ≃+ T)
  (hA : (⇑A)^[m] = id) : Rep.{u_1, 0, 0} ℤ (Multiplicative (ZMod m))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddEquiv.cyclicRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Automorphism.html#AddEquiv.cyclicRep).

## Sources

- [Tau Ceti documentation: `AddEquiv.cyclicRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Automorphism.html#AddEquiv.cyclicRep)
- [Source of `AddEquiv.cyclicRep` in TauCeti/RepresentationTheory/Cyclic/Automorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Cyclic/Automorphism.lean#L107)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
