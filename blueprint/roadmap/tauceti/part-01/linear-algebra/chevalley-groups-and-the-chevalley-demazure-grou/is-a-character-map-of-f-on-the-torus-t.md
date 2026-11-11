---
declaration: def
origin: cited
lean: TauCeti.IsCharacterMap
statement: formalized
---

# `φ` is a character map of `F` on the torus `T`

the endomorphism `F` of `G` preserves the
image of the torus parametrization `T` and acts on its points through the endomorphism `φ` of the
character lattice, `F (T s) = T (torusPointMap φ s)`. By
`TauCeti.torusCharacter_torusPointMap`, a character `χ` evaluated at the parameter of `F (T s)` is
`φ χ` evaluated at `s`, so `φ` is the pullback of characters along `F`.

The character map is data supplied together with `F`: over a finite field it is not determined
by `F`, and an endomorphism preserving the torus need not have one.

```lean
TauCeti.IsCharacterMap.{u_2, u_4, u_5} {κ : Type u_2} {R : Type u_4} [CommRing R] [Fintype κ]
  [DecidableEq κ] {G : Type u_5} [Monoid G] (T : (κ → Rˣ) →* G) (F : G →* G)
  (φ : Module.End ℤ (κ → ℤ)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCharacterMap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/DiagonalTorus/CharacterMap.html#TauCeti.IsCharacterMap).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCharacterMap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/DiagonalTorus/CharacterMap.html#TauCeti.IsCharacterMap)
- [Source of `TauCeti.IsCharacterMap` in TauCeti/LinearAlgebra/Basis/DiagonalTorus/CharacterMap.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Basis/DiagonalTorus/CharacterMap.lean#L244)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
