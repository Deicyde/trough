---
declaration: section
origin: cited
lean: StacksDraft.PseudoCoherence.exists_boundedAboveFiniteFree_of_isPseudoCoherent_restrictScalars, AlgebraicGeometry.ProjectiveSpacePseudoCoherent.isPseudoCoherent_tfae, AlgebraicGeometry.isPseudoCoherent_derivedGlobalSectionsOver_tensor_of_isPseudoCoherent
statement: formalized
proof: formalized
---

# 36.34 Characterizing pseudo-coherent complexes, II

Section 36.34 of the Stacks Project, [Tag 0CSE](https://stacks.math.columbia.edu/tag/0CSE). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CSF, a lemma

[Tag 0CSF](https://stacks.math.columbia.edu/tag/0CSF) in the Stacks Project.

**`StacksDraft.PseudoCoherence.exists_boundedAboveFiniteFree_of_isPseudoCoherent_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RestrictScalars/FiniteFreeAlgebra.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RestrictScalars/FiniteFreeAlgebra.lean#L104).

> **Stacks 0CSF.** If a derived right `R`-module is pseudo-coherent over `A`, where `R` is a
> possibly noncommutative `A`-algebra which is finite free over `A`, then it is represented by a
> bounded-above complex of finite free right `R`-modules.

```lean
theorem exists_boundedAboveFiniteFree_of_isPseudoCoherent_restrictScalars
    (A : Type uA) (R : Type uR) [CommRing A] [Ring R] [Algebra A R]
    (M : DerivedCategory (ModuleCat.{max uA uR v} Rᵐᵒᵖ))
    (hR : Module.Finite A R ∧ Module.Free A R)
    (hM : ∀ m : ℤ, IsPseudoCoherentFrom
      ((ModuleCat.restrictScalars.{max uA uR v} (algebraMap A Rᵐᵒᵖ)).mapDerivedCategory.obj M)
      m) :
    ∃ E : CochainComplex (ModuleCat.{max uA uR v} Rᵐᵒᵖ) ℤ,
      IsBoundedAboveFiniteFree E ∧ Nonempty (DerivedCategory.Q.obj E ≅ M)
```

## Tag 0CSG, a lemma

[Tag 0CSG](https://stacks.math.columbia.edu/tag/0CSG) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpacePseudoCoherent.isPseudoCoherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpacePseudoCoherent/Equivalences.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpacePseudoCoherent/Equivalences.lean#L61).

> **[Stacks, Tag 0CSG].** Let `A` be a ring, `n ≥ 0` and `K ∈ D_QCoh(𝒪_{ℙⁿ_A})`. The following
> are equivalent:
> 1. `K` is pseudo-coherent;
> 2. `RΓ(ℙⁿ_A, E ⊗^𝐋 K)` is a pseudo-coherent object of `D(A)` for each pseudo-coherent `E` of
>    `D(𝒪_{ℙⁿ_A})`;
> 3. `RΓ(ℙⁿ_A, E ⊗^𝐋 K)` is a pseudo-coherent object of `D(A)` for each perfect `E`;
> 4. `RHom_{ℙⁿ_A}(E, K) = RΓ(ℙⁿ_A, R𝓗om(E, K))` is a pseudo-coherent object of `D(A)` for each
>    perfect `E`;
> 5. `RΓ(ℙⁿ_A, K ⊗^𝐋 𝒪(d))` is a pseudo-coherent object of `D(A)` for `d = 0, 1, …, n`.

```lean
theorem isPseudoCoherent_tfae :
    letI : HasDerivedCategory (Proj (polyGrading A n)).Modules := HasDerivedCategory.standard _
    letI : HasDerivedCategory (StrictlyPerfect.OXMod (Proj (polyGrading A n)).toRingedSpace) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory
        (Stacks.DerivedTensor.RingedSite.Modules (Proj (polyGrading A n)).sheaf) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory (ModuleCat.{u} A) := HasDerivedCategory.standard _
    ∀ K : DerivedCategory (Proj (polyGrading A n)).Modules, quasicoherentObject A n K →
      List.TFAE
        [RingedSpace.IsPseudoCoherent (X := (Proj (polyGrading A n)).toRingedSpace) K,
          ∀ E : DerivedCategory (Proj (polyGrading A n)).Modules,
            RingedSpace.IsPseudoCoherent (X := (Proj (polyGrading A n)).toRingedSpace) E →
              StacksDraft.PseudoCoherence.IsPseudoCoherent
                ((derivedGlobalSectionsOver (projToSpecCoeff A n)).obj
                  (((derivedTensorProductFunctor (Proj (polyGrading A n)).sheaf).obj E).obj K)),
          ∀ E : DerivedCategory (Proj (polyGrading A n)).Modules,
            Stacks.Cohomology.PerfectComplexes.IsPerfect
                (X := (Proj (polyGrading A n)).toRingedSpace) E →
              StacksDraft.PseudoCoherence.IsPseudoCoherent
                ((derivedGlobalSectionsOver (projToSpecCoeff A n)).obj
                  (((derivedTensorProductFunctor (Proj (polyGrading A n)).sheaf).obj E).obj K)),
          ∀ E : DerivedCategory (Proj (polyGrading A n)).Modules,
            Stacks.Cohomology.PerfectComplexes.IsPerfect
                (X := (Proj (polyGrading A n)).toRingedSpace) E →
              StacksDraft.PseudoCoherence.IsPseudoCoherent
                ((derivedGlobalSectionsOver (projToSpecCoeff A n)).obj
                  (((Stacks.SheafOfModules.derivedSheafHom (Proj (polyGrading A n)).sheaf).obj
                    (Opposite.op E)).obj K)),
          ∀ d : Fin (n + 1), StacksDraft.PseudoCoherence.IsPseudoCoherent
            ((derivedGlobalSectionsOver (projToSpecCoeff A n)).obj
              (((derivedTensorProductFunctor (Proj (polyGrading A n)).sheaf).obj K).obj
                ((DerivedCategory.singleFunctor (Proj (polyGrading A n)).Modules 0).obj
                  (ProjectiveSpectrum.Proj.twistingSheaf (polyGrading A n) d))))]
```

## Tag 0CSH, a lemma

[Tag 0CSH](https://stacks.math.columbia.edu/tag/0CSH) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherent_derivedGlobalSectionsOver_tensor_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/DerivedSectionsTensorPseudoCoherence.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/DerivedSectionsTensorPseudoCoherence.lean#L370).

> **[Stacks, Tag 0CSH].** Let `A` be a ring, let `X` be a quasi-compact and quasi-separated
> scheme over `A` (the structure morphism being `f : X ⟶ Spec A`), and let `K ∈ D^-_QCoh(𝒪_X)`,
> i.e. `K` has quasi-coherent cohomology sheaves vanishing in all sufficiently large degrees. If
> `RΓ(X, E ⊗^𝐋 K)` is pseudo-coherent in `D(A)` for every perfect `E` in `D(𝒪_X)`, then
> `RΓ(X, E ⊗^𝐋 K)` is pseudo-coherent in `D(A)` for every pseudo-coherent `E` in `D(𝒪_X)`.
>
> The proof is the source's: by [Stacks, Tag 08ES] a pseudo-coherent `E` is approximated, in any
> given degree, by a perfect `P ⟶ E` whose cone `C` has no cohomology from that degree on; tensoring
> with `K` raises the vanishing bound by an upper bound `b` of the cohomology of `K` and keeps it in
> `D_QCoh` ([Stacks, Tag 08DX]); `RΓ(X, -)` raises it by its cohomological dimension `N`
> ([Stacks, Tag 08D5]); so `RΓ(X, P ⊗^𝐋 K) ⟶ RΓ(X, E ⊗^𝐋 K)` is an isomorphism in high degrees and
> the pseudo-coherence of its source passes to its target degree by degree.

```lean
theorem isPseudoCoherent_derivedGlobalSectionsOver_tensor_of_isPseudoCoherent
    [CompactSpace X] [QuasiSeparatedSpace X]
    (K : DerivedCategory (StructureSheafModules X.sheaf))
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor (StructureSheafModules X.sheaf) i).obj
      K).IsQuasicoherent)
    (hKb : ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((DerivedCategory.homologyFunctor (StructureSheafModules X.sheaf) i).obj K))
    (hpc : ∀ E : DerivedCategory (StructureSheafModules X.sheaf),
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E →
        StacksDraft.PseudoCoherence.IsPseudoCoherent
          ((derivedGlobalSectionsOver f).obj (((derivedTensor X.sheaf).obj E).obj K)))
    (E : DerivedCategory (StructureSheafModules X.sheaf))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) :
    StacksDraft.PseudoCoherence.IsPseudoCoherent
      ((derivedGlobalSectionsOver f).obj (((derivedTensor X.sheaf).obj E).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.34, Tag 0CSE](https://stacks.math.columbia.edu/tag/0CSE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
