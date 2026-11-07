---
declaration: theorem
origin: cited
lean: HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact
statement: formalized
proof: formalized
---

# Multiplicativity of the torsion

Let `0 → C₁ → C₂ → C₃ → 0` be a short exact sequence of
chain complexes of vector spaces, with `C₁` and `C₃` acyclic, and with compatible bases: the basis
`c₂ i` of `C₂ᵢ` is the image of the basis `c₁ i` of `C₁ᵢ` followed by lifts of the basis `c₃ i` of
`C₃ᵢ`. Then `τ(C₂) = ε · τ(C₁) · τ(C₃)`, with the sign `ε = ∏ⱼ (-1) ^ (dim B₃,ⱼ₊₁ · dim B₁,ⱼ)`
given by the dimensions of the boundaries `Bₖ,ⱼ ⊆ Cₖ,ⱼ`. This also holds when the complexes are
unbounded, both sides being `0`.

```lean
HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact.{u_1, u_2} {F : Type u_1} [Field F]
  {S : CategoryTheory.ShortComplex (ChainComplex (ModuleCat F) ℤ)} (hS : S.ShortExact)
  (h₁ : HomologicalComplex.Acyclic S.X₁) (h₃ : HomologicalComplex.Acyclic S.X₃) {n₁ n₃ : ℤ → ℕ}
  (c₁ : (i : ℤ) → Module.Basis (Fin (n₁ i)) F ↑(S.X₁.X i))
  (c₃ : (i : ℤ) → Module.Basis (Fin (n₃ i)) F ↑(S.X₃.X i))
  (c₂ : (i : ℤ) → Module.Basis (Fin (n₁ i + n₃ i)) F ↑(S.X₂.X i))
  (hc₁ :
    ∀ (i : ℤ) (k : Fin (n₁ i)),
      (c₂ i) (Fin.castAdd (n₃ i) k) = (ModuleCat.Hom.hom (S.f.f i)) ((c₁ i) k))
  (hc₃ :
    ∀ (i : ℤ) (k : Fin (n₃ i)),
      (ModuleCat.Hom.hom (S.g.f i)) ((c₂ i) (Fin.natAdd (n₁ i) k)) = (c₃ i) k) :
  HomologicalComplex.reidemeisterTorsion S.X₂ c₂ =
    (∏ᶠ (j : ℤ),
        (-1) ^
          (Module.finrank F ↥(ModuleCat.Hom.hom (S.X₃.d (j + 1 + 1) (j + 1))).range *
            Module.finrank F ↥(ModuleCat.Hom.hom (S.X₁.d (j + 1) j)).range)) *
      (HomologicalComplex.reidemeisterTorsion S.X₁ c₁ *
        HomologicalComplex.reidemeisterTorsion S.X₃ c₃)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact).

## Sources

- [Tau Ceti documentation: `HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.html#HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact)
- [Source of `HomologicalComplex.reidemeisterTorsion_eq_mul_of_shortExact` in TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/ReidemeisterTorsion/Basic.lean#L662)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
