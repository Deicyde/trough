---
declaration: section
origin: cited
lean: StacksDraft.Smooth.exists_smooth_isLocalization_of_hasProjectiveDimensionLT_diagonal, StacksDraft.Smooth.smooth_of_flat_of_hasProjectiveDimensionLT_diagonal
statement: formalized
proof: formalized
---

# 23.10 Smooth ring maps and diagonals

Section 23.10 of the Stacks Project, [Tag 0FCV](https://stacks.math.columbia.edu/tag/0FCV). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FCW, a lemma

[Tag 0FCW](https://stacks.math.columbia.edu/tag/0FCW) in the Stacks Project.

**`StacksDraft.Smooth.exists_smooth_isLocalization_of_hasProjectiveDimensionLT_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/PerfectDiagonal.lean, line 1187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/PerfectDiagonal.lean#L1187).

> **Stacks 0FCW.** Let `A → B` be a flat ring map, essentially of finite type, from a Noetherian
> ring to a local ring. If `B` has finite projective dimension over `B ⊗[A] B`, then `B` is the
> localization of a smooth `A`-algebra.
>
> The source states this for a local homomorphism of Noetherian local rings whose diagonal is
> perfect; that form is `StacksDraft.Smooth.exists_smooth_isLocalization_of_isPerfect_diagonal`.
> Finite projective dimension of the diagonal gives formal smoothness by
> `StacksDraft.Smooth.formallySmooth_of_hasProjectiveDimensionLT_diagonal`, and a formally smooth
> local algebra essentially of finite type is a localization of a smooth algebra by
> `StacksDraft.Smooth.exists_smooth_isLocalization_of_formallySmooth`.

```lean
public theorem exists_smooth_isLocalization_of_hasProjectiveDimensionLT_diagonal
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [IsLocalRing B] [IsNoetherianRing A]
    [Algebra A B] [Module.Flat A B] [Algebra.EssFiniteType A B]
    (hpd : letI := (Algebra.TensorProduct.lmul' (R := A) (S := B)).toRingHom.toAlgebra
      ∃ n : ℕ, HasProjectiveDimensionLT (ModuleCat.of (TensorProduct A B B) B) n) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C) (_ : Algebra.Smooth A C)
      (M : Submonoid C) (_ : Algebra C B), IsScalarTower A C B ∧ IsLocalization M B
```

## Tag 0FCX, a lemma

[Tag 0FCX](https://stacks.math.columbia.edu/tag/0FCX) in the Stacks Project.

**`StacksDraft.Smooth.smooth_of_flat_of_hasProjectiveDimensionLT_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/PerfectDiagonal.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/PerfectDiagonal.lean#L1354).

> **Stacks 0FCX.** Let `A → B` be a flat finite type ring map from a Noetherian ring. If `B` has
> finite projective dimension over `B ⊗[A] B`, then `B` is a smooth `A`-algebra.
>
> The source assumes that `B` is Noetherian and that the diagonal is perfect; that form is
> `StacksDraft.Smooth.smooth_of_flat_of_isPerfect_diagonal`. Smoothness is local on `B`, and at a
> prime `𝔮` of `B` over `𝔭` of `A` finite projective dimension of the diagonal passes to the
> localized map `A_𝔭 → B_𝔮`, which is then formally smooth by
> `StacksDraft.Smooth.formallySmooth_of_hasProjectiveDimensionLT_diagonal`.

```lean
public theorem smooth_of_flat_of_hasProjectiveDimensionLT_diagonal
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [Module.Flat A B] [Algebra.FiniteType A B]
    (hpd : letI := (Algebra.TensorProduct.lmul' (R := A) (S := B)).toRingHom.toAlgebra
      ∃ n : ℕ, HasProjectiveDimensionLT (ModuleCat.of (TensorProduct A B B) B) n) :
    Algebra.Smooth A B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.10, Tag 0FCV](https://stacks.math.columbia.edu/tag/0FCV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
