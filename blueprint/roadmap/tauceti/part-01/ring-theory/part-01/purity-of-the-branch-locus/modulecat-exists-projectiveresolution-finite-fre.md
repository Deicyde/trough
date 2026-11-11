---
declaration: theorem
origin: cited
lean: ModuleCat.exists_projectiveResolution_finite_free_minimal
statement: formalized
proof: formalized
---

# ModuleCat.exists_projectiveResolution_finite_free_minimal

A finite module over a Noetherian local ring with projective dimension at most `n` has a
minimal finite free projective resolution of length at most `n`: all terms are finite free,
all terms above degree `n` vanish, and every differential lands in the maximal ideal times
its target.

```lean
ModuleCat.exists_projectiveResolution_finite_free_minimal.{u} {R : Type u} [CommRing R]
  [IsLocalRing R] [IsNoetherianRing R] (M : ModuleCat R) [Module.Finite R ↑M] {n : ℕ}
  (hM : CategoryTheory.HasProjectiveDimensionLE M n) :
  ∃ F,
    (∀ (i : ℕ), Module.Finite R ↑(F.complex.X i) ∧ Module.Free R ↑(F.complex.X i)) ∧
      (∀ (i : ℕ), n < i → CategoryTheory.Limits.IsZero (F.complex.X i)) ∧
        HomologicalComplex.IsMinimal F.complex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ModuleCat.exists_projectiveResolution_finite_free_minimal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Projective/MinimalResolution/ChainComplex.html#ModuleCat.exists_projectiveResolution_finite_free_minimal).

## Sources

- [Tau Ceti documentation: `ModuleCat.exists_projectiveResolution_finite_free_minimal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Projective/MinimalResolution/ChainComplex.html#ModuleCat.exists_projectiveResolution_finite_free_minimal)
- [Source of `ModuleCat.exists_projectiveResolution_finite_free_minimal` in TauCeti/Algebra/Category/ModuleCat/Projective/MinimalResolution/ChainComplex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/Projective/MinimalResolution/ChainComplex.lean#L93)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
