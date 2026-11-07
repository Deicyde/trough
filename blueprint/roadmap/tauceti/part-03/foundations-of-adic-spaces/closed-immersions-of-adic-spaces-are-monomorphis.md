---
declaration: theorem
origin: cited
lean: TauCeti.AdicSpace.mono_of_isClosedImmersion
statement: formalized
proof: formalized
---

# Closed immersions of adic spaces are monomorphisms

a morphism into an adic space factors
through a closed immersion in at most one way.

```lean
TauCeti.AdicSpace.mono_of_isClosedImmersion.{u} {X Y : TauCeti.AdicSpace} (f : X ⟶ Y)
  (hf : TauCeti.PreAdicSpace.IsClosedImmersion f.hom) : CategoryTheory.Mono f
```

## Depends on

- [Adic spaces](adic-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.mono_of_isClosedImmersion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/ClosedImmersion/Mono.html#TauCeti.AdicSpace.mono_of_isClosedImmersion).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.mono_of_isClosedImmersion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/ClosedImmersion/Mono.html#TauCeti.AdicSpace.mono_of_isClosedImmersion)
- [Source of `TauCeti.AdicSpace.mono_of_isClosedImmersion` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/ClosedImmersion/Mono.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/ClosedImmersion/Mono.lean#L183)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
