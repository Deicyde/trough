---
declaration: theorem
origin: cited
lean: HomologicalComplex.reidemeisterTorsion_eq_zero_iff
statement: formalized
proof: formalized
---

# HomologicalComplex.reidemeisterTorsion\_eq\_zero\_iff

The torsion of a bounded based complex vanishes if and only if the complex is not acyclic.

```lean
HomologicalComplex.reidemeisterTorsion_eq_zero_iff.{u_1, u_2} {F : Type u_1} [Field F]
  (C : ChainComplex (ModuleCat F) ℤ) {n : ℤ → ℕ} (c : (i : ℤ) → Module.Basis (Fin (n i)) F ↑(C.X i))
  (hn : {i | n i ≠ 0}.Finite) :
  HomologicalComplex.reidemeisterTorsion C c = 0 ↔ ¬HomologicalComplex.Acyclic C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.reidemeisterTorsion_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `HomologicalComplex.reidemeisterTorsion_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_zero_iff)
- [Source of `HomologicalComplex.reidemeisterTorsion_eq_zero_iff` in TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean#L312)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
