---
declaration: def
origin: cited
lean: HomologicalComplex.componentwiseReidemeisterTorsion
statement: formalized
---

# HomologicalComplex.componentwiseReidemeisterTorsion

The componentwise torsion of a based complex `C` over `A` along a ring homomorphism
`f : A →+* Q` into a reduced Artinian ring, which is the finite product of its residue fields
`Q ⧸ m`: the element of `Q` whose component in `Q ⧸ m` is the torsion of the coordinate base change
of `C` along `A → Q → Q ⧸ m`. A component is `0` exactly when that base change is not acyclic, or
when `C` is unbounded.

```lean
HomologicalComplex.componentwiseReidemeisterTorsion.{u_1, u_2, u_3} {A : Type u_1} [CommRing A]
  {Q : Type u_2} [CommRing Q] [IsArtinianRing Q] [IsReduced Q] (C : ChainComplex (ModuleCat A) ℤ)
  {n : ℤ → ℕ} (c : (i : ℤ) → Module.Basis (Fin (n i)) A ↑(C.X i)) (f : A →+* Q) : Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.componentwiseReidemeisterTorsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Componentwise.html#HomologicalComplex.componentwiseReidemeisterTorsion).

## Sources

- [Tau Ceti documentation: `HomologicalComplex.componentwiseReidemeisterTorsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Componentwise.html#HomologicalComplex.componentwiseReidemeisterTorsion)
- [Source of `HomologicalComplex.componentwiseReidemeisterTorsion` in TauCeti/Algebra/Homology/ReidemeisterTorsion/Componentwise.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/ReidemeisterTorsion/Componentwise.lean#L121)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
