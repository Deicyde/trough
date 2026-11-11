---
declaration: theorem
origin: cited
lean: Submodule.covolume_mixedImage
statement: formalized
proof: formalized
---

# The covolume of an `𝓞 K`-module, read at the finite places

Let `Λ` be a finitely
generated `𝓞 K`-module spanning `ι → K`, and let `B v` be the largest value of the finite place `v`
on the determinants of `card ι` vectors of `Λ` (it exists by
`Submodule.exists_isGreatest_apply_det`). Then the covolume of the mixed image of `Λ` is
`(∏ᶠ v, B v)⁻¹` times the covolume of `(𝓞 K) ^ ι`.

```lean
Submodule.covolume_mixedImage.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K] {ι : Type u_2}
  [Fintype ι] [DecidableEq ι] {Λ : Submodule (NumberField.RingOfIntegers K) (ι → K)} (hΛ : Λ.FG)
  (hspan : Submodule.span K ↑Λ = ⊤) {B : NumberField.FinitePlace K → ℝ}
  (hB :
    ∀ (v : NumberField.FinitePlace K),
      IsGreatest ((fun x => v (Matrix.of x).det) '' Set.univ.pi fun x => ↑Λ) (B v)) :
  ZLattice.covolume Λ.mixedImage MeasureTheory.volume =
    (∏ᶠ (v : NumberField.FinitePlace K), B v)⁻¹ *
      ZLattice.covolume (NumberField.mixedEmbedding.integerLattice K) MeasureTheory.volume ^
        Fintype.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Pseudo-bases over a Dedekind domain](pseudo-bases-over-a-dedekind-domain.md)
- [Ultrametric Hadamard bound, row form](../../../linear-algebra/matrix/ultrametric-hadamard-bound-row-form.md)

## Lean

Formalized in Tau Ceti as [`Submodule.covolume_mixedImage`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/ModuleCovolume.html#Submodule.covolume_mixedImage).

## Sources

- [Tau Ceti documentation: `Submodule.covolume_mixedImage`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/ModuleCovolume.html#Submodule.covolume_mixedImage)
- [Source of `Submodule.covolume_mixedImage` in TauCeti/NumberTheory/NumberField/CanonicalEmbedding/ModuleCovolume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/ModuleCovolume.lean#L253)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
