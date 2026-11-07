---
declaration: theorem
origin: cited
lean: HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det
statement: formalized
proof: formalized
---

# HomologicalComplex.reidemeisterTorsion\_eq\_mul\_finprod\_det

The basis-change formula for the torsion: replacing the bases `c i` of `C` by `c' i`
multiplies the torsion by `∏ᵢ [c'ᵢ / cᵢ] ^ ((-1) ^ i)`, where `[c'ᵢ / cᵢ]` is the determinant of
`c' i` with respect to `c i`. This holds for every complex, both sides being `0` when `C` is
not acyclic or is unbounded.

```lean
HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det.{u_1, u_2} {F : Type u_1} [Field F]
  (C : ChainComplex (ModuleCat F) ℤ) {n : ℤ → ℕ}
  (c c' : (i : ℤ) → Module.Basis (Fin (n i)) F ↑(C.X i)) :
  HomologicalComplex.reidemeisterTorsion C c' =
    HomologicalComplex.reidemeisterTorsion C c * ∏ᶠ (i : ℤ), (c i).det ⇑(c' i) ^ ↑i.negOnePow
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det).

## Sources

- [Tau Ceti documentation: `HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det)
- [Source of `HomologicalComplex.reidemeisterTorsion_eq_mul_finprod_det` in TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean#L399)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
