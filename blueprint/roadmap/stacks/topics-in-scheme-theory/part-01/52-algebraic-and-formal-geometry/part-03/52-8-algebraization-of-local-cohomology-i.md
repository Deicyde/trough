---
declaration: section
origin: cited
lean: Stacks.Algebraization.associatedSubset, Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology, Stacks.Algebraization.prod_smul_id_derivedHom_homology_eq_zero, Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedHom, Stacks.LocalCohomology.isLE_localCohomologyDerived_single_of_cohomologicalDimension_le, Stacks.LocalCohomology.isGE_localCohomologyDerived_single, Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyWithSupportIn_sup, Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyModule_sup
statement: formalized
proof: formalized
---

# 52.8 Algebraization of local cohomology, I

Section 52.8 of the Stacks Project, [Tag 0EFF](https://stacks.math.columbia.edu/tag/0EFF). 7 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EFG, an equation

[Tag 0EFG](https://stacks.math.columbia.edu/tag/0EFG) in the Stacks Project.

**`Stacks.Algebraization.associatedSubset`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AssociatedSubset.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AssociatedSubset.lean#L42).

> The primes whose specializations in `V(I)` all belong to `V(J) ∩ V(I)`.
>
> This is the subset denoted by `T` in Stacks Project, Tag 0EFG.

```lean
def associatedSubset (I J : Ideal A) : Set (PrimeSpectrum A)
```

## Tag 0EFH, a lemma

[Tag 0EFH](https://stacks.math.columbia.edu/tag/0EFH) in the Stacks Project.

**`Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorCompletedLocalCohomology.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorCompletedLocalCohomology.lean#L143). The attribute's comment: “the full statement: an element outside `p` annihilating the cohomology of the derived `I`-adic completion of `RΓ_{V(J)}(M)` in every degree `≤ s`”.

> Let `I` and `J` be ideals of a Noetherian ring `A` with a dualizing complex, let `M` be a
> finite `A`-module, and let `p` be a prime outside `V(J) ∩ V(I)` with `cd(A, I) ≤ d`. If
> `depth_{A_{p'}}(M_{p'}) + dim((A/p')_q) > s + d` for all primes `p' ⊆ p` and all
> `q ∈ V(p') ∩ V(J) ∩ V(I)`, then some `f ∈ A` outside `p` annihilates the degree-`i` cohomology of
> the derived `I`-adic completion of `RΓ_{V(J)}(M)` for every `i ≤ s`.

```lean
theorem exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (p : PrimeSpectrum A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hp : p ∉ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I I.fg_of_isNoetherianRing ≤ d)
    (hdepth : ∀ x y : PrimeSpectrum A, x.asIdeal ≤ p.asIdeal →
      y ∈ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) →
      x.asIdeal ≤ y.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime x.asIdeal)
            (maximalIdeal (Localization.AtPrime x.asIdeal))
            (LocalizedModule x.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
            x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) >
        ((s + d : ℤ) : EInt))
    {r : ℕ} (gen : Fin r → A) (hgen : Ideal.span (Set.range gen) = I) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ i : ℤ, i ≤ s →
      f ∈ Module.annihilator A
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
          ((DerivedCompletion.derivedCompletionFunctor A gen).obj
            ((Dualizing.derivedPowerTorsionProperty A J J.fg_of_isNoetherianRing).ι.obj
              ((Dualizing.localCohomologyFunctor.{u, u} A J J.fg_of_isNoetherianRing).obj
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A M))))))
```

**`Stacks.Algebraization.prod_smul_id_derivedHom_homology_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorTruncationReduction.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorTruncationReduction.lean#L325). The attribute's comment: “the quantitative form of the truncation reduction, with the explicit product of per-degree annihilators”.

> **The engine.** For `P` concentrated in degrees `≤ d` and `Q` in degrees `≥ a`, the product
> of scalars annihilating `H^j(Q)` for `a ≤ j ≤ s + d` annihilates `H^i(RHom_A(P, Q))` for every
> `i ≤ s`.

```lean
public theorem prod_smul_id_derivedHom_homology_eq_zero {A : Type u} [CommRing A] (f : ℤ → A)
    (a d s : ℤ) (P Q : DerivedCategory (ModuleCat.{u} A)) [P.IsLE d] [Q.IsGE a]
    (hQ : ∀ j : ℤ, j ≤ s + d →
      f j • 𝟙 ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) j).obj Q) = 0)
    (i : ℤ) (hi : i ≤ s) :
    (∏ j ∈ Finset.range ((s + d - a).toNat + 1), f (a + j)) • 𝟙
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
        ((StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
          (Opposite.op P, Q))) = 0
```

**`Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorTruncationReduction.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorTruncationReduction.lean#L364). The attribute's comment: “the homological-algebra reduction: after the two identifications of the first paragraph, the canonical-truncation argument producing an element outside `p` annihilating `H^i(RHom(P, Q))` for `i ≤ s`”.

> **Stacks 0EFH, the homological reduction.** Let `P` have cohomology concentrated in degrees
> `≤ d` and `Q` in degrees `≥ a`. If for each `j ≤ s + d` some element outside a prime `p`
> annihilates `H^j(Q)`, then one element outside `p` annihilates `H^i(RHom_A(P, Q))` for all
> `i ≤ s`.

```lean
public theorem exists_notMem_mem_annihilator_homology_derivedHom {A : Type u} [CommRing A]
    (p : PrimeSpectrum A) (a d s : ℤ) (P Q : DerivedCategory (ModuleCat.{u} A)) [Q.IsGE a]
    (hP : ∀ i : ℤ, d < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj P))
    (hQ : ∀ j : ℤ, j ≤ s + d → ∃ f : A, f ∉ p.asIdeal ∧
      f ∈ Module.annihilator A
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) j).obj Q)) :
    ∃ g : A, g ∉ p.asIdeal ∧ ∀ i : ℤ, i ≤ s →
      g ∈ Module.annihilator A
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
          ((StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
            (Opposite.op P, Q)))
```

**`Stacks.LocalCohomology.isLE_localCohomologyDerived_single_of_cohomologicalDimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean#L108). The attribute's comment: “the use of hypothesis (3): `H^i(RΓ_I(A)) = 0` for `i > d` when `cd(A, I) ≤ d`”.

> A bound `d` on the cohomological dimension of `I` places the local cohomology
> `RΓ_{V(I)}(M[0])` of Stacks 0A6Q in degrees `≤ d`.

```lean
theorem isLE_localCohomologyDerived_single_of_cohomologicalDimension_le
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) (d : ℤ)
    (hcd : cohomologicalDimension A I hI ≤ d) (M : ModuleCat.{u} A) :
    ((Dualizing.derivedPowerTorsionProperty A I hI).ι.obj
      ((Dualizing.localCohomologyFunctor A I hI).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M))).IsLE d
```

**`Stacks.LocalCohomology.isGE_localCohomologyDerived_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean#L152). The attribute's comment: “the boundedness the truncation reduction needs: `RΓ_{V(I)}(M[0])` lies in degrees `≥ 0`”.

> The local cohomology `RΓ_{V(I)}(M[0])` of Stacks 0A6Q of a module placed in degree zero lies
> in degrees `≥ 0`.

```lean
theorem isGE_localCohomologyDerived_single
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{u} A) :
    ((Dualizing.derivedPowerTorsionProperty A I hI).ι.obj
      ((Dualizing.localCohomologyFunctor A I hI).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M))).IsGE 0
```

**`Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyWithSupportIn_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean#L202). The attribute's comment: “the per-degree annihilator input: a single element outside `p` annihilating `H^j_{V(I+J)}(M)` for every `j ≤ s + d`”.

> **The per-degree annihilator input of Stacks 0EFH, in the support-indexed model.** For `M`
> finite over a Noetherian ring `A` with a dualizing complex and `p` a prime outside
> `V(J) ∩ V(I)`, the depth-plus-dimension inequality in the range `s + d` gives one element of `A`
> outside `p` annihilating `H^j_{V(I+J)}(M)` for every `j ≤ s + d`.

```lean
theorem exists_notMem_mem_annihilator_localCohomologyWithSupportIn_sup
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (p : PrimeSpectrum A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hp : p ∉ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A))
    (hdepth : ∀ x y : PrimeSpectrum A, x.asIdeal ≤ p.asIdeal →
      y ∈ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) →
      x.asIdeal ≤ y.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime x.asIdeal)
            (maximalIdeal (Localization.AtPrime x.asIdeal))
            (LocalizedModule x.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
            x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) >
        ((s + d : ℤ) : EInt)) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ j : ℤ, j ≤ s + d →
      f ∈ Module.annihilator A
        (localCohomologyWithSupportIn.{u, u} A
          (PrimeSpectrum.zeroLocus ((I ⊔ J : Ideal A) : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) j)
```

**`Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyModule_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean#L246). The attribute's comment: “the per-degree annihilator input, in the `RΓ_{V(I+J)}` coreflection model”.

> **The per-degree annihilator input of Stacks 0EFH, in the coreflection model.** The
> annihilator of the previous statement, transported to the local cohomology `RΓ_{V(I+J)}` of
> Stacks 0A6Q along the comparison of Stacks 0955.

```lean
theorem exists_notMem_mem_annihilator_localCohomologyModule_sup
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (p : PrimeSpectrum A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hp : p ∉ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A))
    (hdepth : ∀ x y : PrimeSpectrum A, x.asIdeal ≤ p.asIdeal →
      y ∈ PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) →
      x.asIdeal ≤ y.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime x.asIdeal)
            (maximalIdeal (Localization.AtPrime x.asIdeal))
            (LocalizedModule x.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
            x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) >
        ((s + d : ℤ) : EInt)) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ j : ℤ, j ≤ s + d →
      f ∈ Module.annihilator A
        (localCohomologyModule A (I ⊔ J) (I ⊔ J).fg_of_isNoetherianRing
          (ModuleCat.of A M) j)
```

**`Stacks.Algebraization.derivedCompletionLocalCohomologySupIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean#L114). The attribute's comment: “the first identification of the proof: `RΓ_J(-)^∧ = RΓ_{I+J}(-)^∧`, which is what lets `J` be replaced by `I + J`”.

> For ideals `I` and `J` of `A` with `I` generated by the finite family `f`, derived `I`-adic
> completion does not distinguish `RΓ_{V(J)}` from `RΓ_{V(J + I)}`: there is a natural isomorphism
> `RΓ_{V(J)}(-)^∧ ≅ RΓ_{V(J + I)}(-)^∧`.

```lean
def derivedCompletionLocalCohomologySupIso (A : Type u) [CommRing A] (I J : Ideal A)
    (hI : I.FG) (hJ : J.FG) {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = I) :
    Dualizing.localCohomologyFunctor.{u, u} A J hJ ⋙
        (Dualizing.derivedPowerTorsionProperty A J hJ).ι ⋙
          DerivedCompletion.derivedCompletionFunctor A f ≅
      Dualizing.localCohomologyFunctor.{u, u} A (J + I) (Submodule.FG.sup hJ hI) ⋙
        (Dualizing.derivedPowerTorsionProperty A (J + I) (Submodule.FG.sup hJ hI)).ι ⋙
          DerivedCompletion.derivedCompletionFunctor A f
```

**`Stacks.Algebraization.derivedCompletionIsoDerivedHomLocalCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean#L150). The attribute's comment: “the second identification of the proof: derived `I`-adic completion is `RHom` out of `RΓ_{V(I)}(A)`”.

> For a finite family `f` generating `I`, derived `I`-adic completion is derived Hom out of the
> local cohomology `RΓ_{V(I)}(A)` of the ring: `K^∧ ≅ RHom_A(RΓ_{V(I)}(A), K)`.

```lean
def derivedCompletionIsoDerivedHomLocalCohomology (A : Type u) [CommRing A] (I : Ideal A)
    (hI : I.FG) {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = I)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    (DerivedCompletion.derivedCompletionFunctor A f).obj K ≅
      (StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
        (Opposite.op ((Stacks.LocalCohomology.localCohomologyOnModules.{u, u} A I hI).obj
          (ModuleCat.of A A)), K)
```

**`Stacks.Algebraization.derivedCompletionIsoDerivedHomDerivedPowerTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean#L165). The attribute's comment: “the second identification of the proof, written with `RΓ_I(A)` over a Noetherian ring”.

> Over a Noetherian ring derived `I`-adic completion is derived Hom out of derived `I`-power
> torsion of the ring: `K^∧ ≅ RHom_A(RΓ_I(A), K)`.

```lean
def derivedCompletionIsoDerivedHomDerivedPowerTorsion (A : Type u) [CommRing A]
    [IsNoetherianRing A] (I : Ideal A) {r : ℕ} (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = I) (K : DerivedCategory (ModuleCat.{u} A)) :
    (DerivedCompletion.derivedCompletionFunctor A f).obj K ≅
      (StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
        (Opposite.op (Stacks.LocalCohomology.derivedPowerTorsionObj.{u, u} A I
          (Ideal.fg_of_isNoetherianRing I) (ModuleCat.of A A)), K)
```

**`Stacks.Algebraization.derivedCompletionLocalCohomologyIsoDerivedHomSup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyCompletionComparison.lean#L180). The attribute's comment: “the two identifications of the first paragraph of the proof, composed into the form the truncation reduction consumes”.

> For ideals `I` and `J` of `A` with `I` generated by the finite family `f`, the derived
> `I`-adic completion of `RΓ_{V(J)}(K)` is `RHom_A(RΓ_{V(I)}(A), RΓ_{V(J + I)}(K))`.

```lean
def derivedCompletionLocalCohomologyIsoDerivedHomSup (A : Type u) [CommRing A] (I J : Ideal A)
    (hI : I.FG) (hJ : J.FG) {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = I)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    (DerivedCompletion.derivedCompletionFunctor A f).obj
        ((Dualizing.derivedPowerTorsionProperty A J hJ).ι.obj
          ((Dualizing.localCohomologyFunctor.{u, u} A J hJ).obj K)) ≅
      (StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
        (Opposite.op ((Stacks.LocalCohomology.localCohomologyOnModules.{u, u} A I hI).obj
            (ModuleCat.of A A)),
          (Dualizing.derivedPowerTorsionProperty A (J + I) (Submodule.FG.sup hJ hI)).ι.obj
            ((Dualizing.localCohomologyFunctor.{u, u} A (J + I)
              (Submodule.FG.sup hJ hI)).obj K))
```

## Tag 0EFI, a lemma

[Tag 0EFI](https://stacks.math.columbia.edu/tag/0EFI) in the Stacks Project.

**`Stacks.Algebraization.stabilizingIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Stabilization.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Stabilization.lean#L318). The attribute's comment: “the stabilizing ideal is contained in J”.

> **Stacks 0EFI.** The stabilizing ideal is contained in the ideal it shrinks.

```lean
public theorem stabilizingIdeal_le :
    stabilizingIdeal I J s d omega H ≤ J
```

**`Stacks.Algebraization.zeroLocus_stabilizingIdeal_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Stabilization.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Stabilization.lean#L328). The attribute's comment: “V(J₀) ∩ V(I) = V(J) ∩ V(I) for the stabilizing ideal”.

> **Stacks 0EFI.** Shrinking `J` to the stabilizing ideal does not change the intersection of
> the zero locus with `V(I)`.

```lean
public theorem zeroLocus_stabilizingIdeal_inter :
    PrimeSpectrum.zeroLocus (stabilizingIdeal I J s d omega H : Set A) ∩
        PrimeSpectrum.zeroLocus (I : Set A) =
      PrimeSpectrum.zeroLocus (J : Set A) ∩
        PrimeSpectrum.zeroLocus (I : Set A)
```

**`Stacks.Algebraization.exists_isStabilizingData_of_nonpos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationExistence/CandidateIdeal.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationExistence/CandidateIdeal.lean#L499). The attribute's comment: “the existence of the stabilizing data, for s ≤ 0”.

> **Stacks 0EFI for `s ≤ 0`.** Let `I` and `J` be ideals of a Noetherian ring `A` and let `M` be
> a finite `A`-module. For every integer `s ≤ 0` there is a pair `(J₀, n)` with the stabilization
> property of Stacks 0EFI: `J₀ ≤ J` and `V(J₀) ∩ V(I) = V(J) ∩ V(I)`, every further ideal `J' ≤ J₀`
> with `V(J') ∩ V(I) = V(J) ∩ V(I)` has `RΓ_{J₀}(M) → RΓ_{J'}(M)` an isomorphism on cohomology in
> degrees `≤ s`, and `(J₀ I) ^ n` annihilates all of those cohomology modules.
>
> The ideal is the one the source constructs, `J₀ = J ⊓ I(B)` for `B` the set of primes outside
> `V(I)` lying in `T` at which the depth of `M` is at most `s`. In this range the hypotheses
> (1)–(4) of the source — a dualizing complex and bounds on depth and relative dimension — are not
> needed: the semicontinuity argument of Claim I is replaced by the nonnegativity of depth, and the
> annihilator criterion Stacks 0EFC of Claim III by the finiteness of `H⁰_{J₀}(M)`.
>
> For `s ≥ 1` the hypotheses are needed; see
> `Stacks.Algebraization.exists_isStabilizingData`.

```lean
public theorem exists_isStabilizingData_of_nonpos
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (s : ℤ) (hs : s ≤ 0) :
    ∃ p : Ideal A × ℕ, IsStabilizingData (M := M) I J s p
```

**`Stacks.Algebraization.exists_isStabilizingData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationExistence/UniformAnnihilation.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationExistence/UniformAnnihilation.lean#L354). The attribute's comment: “the existence of the stabilizing data, given hypotheses (1)-(4) and 0 ≤ d”.

> **Stacks 0EFI.** Let `I` and `J` be ideals of a Noetherian ring `A`, let `M` be a finite
> `A`-module, and let `s` and `d` be integers with `0 ≤ d`. Under hypotheses (1)–(4) of the source
> there is a pair `(J₀, n)` with the stabilization property: `J₀ ≤ J` and
> `V(J₀) ∩ V(I) = V(J) ∩ V(I)`, every further ideal `J' ≤ J₀` with `V(J') ∩ V(I) = V(J) ∩ V(I)` has
> `RΓ_{J₀}(M) → RΓ_{J'}(M)` an isomorphism on cohomology in degrees `≤ s`, and `(J₀ I) ^ n`
> annihilates all of those cohomology modules.
>
> The proof is the source's. The ideal is `J ⊓ I(B)` for `B` the set of primes outside `V(I)` lying
> in `T` at which the depth of `M` is at most `s`, shrunk once more at the end to absorb the
> annihilator ideal; Claim I is the semicontinuity of `depth + δ`, Claim II the comparison criterion
> Stacks 0DWV, and Claim III Faltings' annihilator theorem Stacks 0EFC.
>
> `0 ≤ d` belongs to the statement of 0EFI: the source's wording omits it, uses it silently in
> Claim III, and is false without it, by the counterexample
> `Stacks.Algebraization.not_forall_exists_isStabilizingData_of_neg`
> (`StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationCounterexample.lean:451`). It is not
> recorded by `Stacks.Algebraization.StabilizationHypotheses` and does not follow from it. See
> `Stacks.Algebraization.exists_isStabilizingData_iff_of_neg` for what the conclusion amounts to
> when `d < 0`, and the module docstring for the erratum.

```lean
public theorem exists_isStabilizingData
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (s d : ℤ) (hd : 0 ≤ d)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (H : StabilizationHypotheses (M := M) I J s d omega) :
    ∃ p : Ideal A × ℕ, IsStabilizingData (M := M) I J s p
```

## Tag 0EFJ, a lemma

[Tag 0EFJ](https://stacks.math.columbia.edu/tag/0EFJ) in the Stacks Project.

**`Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFiniteness.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFiniteness.lean#L183). The attribute's comment: “H^i\_\{J₀}(M) is a finite A-module for i ≤ s, given the annihilation clause of 0EFI”.

> **Stacks 0EFJ.** Under hypothesis (2') the local cohomology of `M` supported in the
> stabilizing ideal `J₀` of Stacks 0EFI is a finite `A`-module in every degree `i ≤ s`.
>
> The annihilation of `H^i_{J₀}(M)` by a power of `J₀ I` for `i ≤ s` is carried as a hypothesis
> here; it is the clause `Stacks.Algebraization.IsStabilizingData.pow_mul_le_annihilator` of the
> conclusion of Stacks 0EFI. For the form of Stacks 0EFJ in which it is proved rather than
> assumed, see
> `Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_of_nonneg`.

```lean
public theorem finite_localCohomologyModule_stabilizingIdeal
    (h2 : DepthAddDimGtOnZeroLocus (M := M) I J s) (hs : 0 ≤ s)
    (hann : ∃ n : ℕ, ∀ i : ℤ, i ≤ s →
      ((stabilizingIdeal I J s d omega H * I) ^ n : Ideal A) ≤ Module.annihilator A
        (localCohomologyModule A (stabilizingIdeal I J s d omega H)
          (Ideal.fg_of_isNoetherianRing (stabilizingIdeal I J s d omega H))
          (ModuleCat.of A M) i))
    (i : ℤ) (hi : i ≤ s) :
    Module.Finite A
      (localCohomologyModule A (stabilizingIdeal I J s d omega H)
        (Ideal.fg_of_isNoetherianRing (stabilizingIdeal I J s d omega H))
        (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_of_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFiniteness.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFiniteness.lean#L227). The attribute's comment: “H^i\_\{J₀}(M) is a finite A-module for i ≤ s, for 0 ≤ d”.

> **Stacks 0EFJ.** Under hypotheses (1), (3), (4) of Stacks 0EFI together with hypothesis (2')
> in place of its empty hypothesis (2), the local cohomology of `M` supported in the stabilizing
> ideal `J₀` of Stacks 0EFI is a finite `A`-module in every degree `i ≤ s`.
>
> Nothing is assumed about `H^i_{J₀}(M)`: the annihilation of those modules by a power of `J₀ I`
> for `i ≤ s`, which the source takes from Stacks 0EFI, is proved here from
> `Stacks.Algebraization.exists_isStabilizingData`, the existence statement of that lemma. The
> only hypothesis beyond those of the source is `0 ≤ d`, which Stacks 0EFI needs and which the
> source uses silently when it reads `depth + dim > d + s` as `depth + dim > s`; see the module
> documentation. In particular `0 ≤ s` is not assumed: in degrees `i ≤ s < 0` local cohomology
> vanishes, so the statement is free there.

```lean
public theorem finite_localCohomologyModule_stabilizingIdeal_of_nonneg
    (h2 : DepthAddDimGtOnZeroLocus (M := M) I J s) (hd : 0 ≤ d)
    (i : ℤ) (hi : i ≤ s) :
    Module.Finite A
      (localCohomologyModule A (stabilizingIdeal I J s d omega H)
        (Ideal.fg_of_isNoetherianRing (stabilizingIdeal I J s d omega H))
        (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.IsStabilizingData.finite_localCohomologyModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFinitenessGeneral.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationFinitenessGeneral.lean#L82). The attribute's comment: “H^i\_\{J₀}(M) is a finite A-module for i ≤ s, for every ideal J₀ with the conclusions of 0EFI”.

> **Stacks 0EFJ.** Let `A` be a Noetherian ring with a dualizing complex `omega`, let `I`, `J`
> be ideals, `M` a finite `A`-module and `s` an integer, and assume hypothesis (2'): for
> `𝔭 ∈ V(I)` outside `V(J) ∩ V(I)`, `depth(M_𝔭) + dim((A/𝔭)_𝔮) > s` for every
> `𝔮 ∈ V(𝔭) ∩ V(J) ∩ V(I)`. Then for every ideal `J₀` with the conclusion of Stacks 0EFI —
> `J₀ ⊆ J`, `V(J₀) ∩ V(I) = V(J) ∩ V(I)`, stability of `H^i_{J'}(M)` for `i ≤ s` under further
> shrinking `J' ⊆ J₀` with the same trace on `V(I)`, and annihilation of these modules by
> `(J₀ I) ^ n` — the module `H^i_{J₀}(M)` is finite for every `i ≤ s`.
>
> Hypotheses (3) and (4) of Stacks 0EFI are not needed here: they enter only in producing `J₀`.
> No pair `(J₀, n)` need exist when `d < 0`, where Stacks 0EFI fails; there the statement is
> vacuous.

```lean
public theorem IsStabilizingData.finite_localCohomologyModule {I J J₀ : Ideal A} {s : ℤ}
    {n : ℕ} (hJ₀ : IsStabilizingData (M := M) I J s (J₀, n))
    (omega : letI := HasDerivedCategory.standard (ModuleCat.{u} A)
      DerivedCategory (ModuleCat.{u} A))
    (homega : letI := HasDerivedCategory.standard (ModuleCat.{u} A)
      Dualizing.IsDualizingComplex (A := A) (K := omega))
    (h2 : DepthAddDimGtOnZeroLocus (M := M) I J s) (i : ℤ) (hi : i ≤ s) :
    Module.Finite A
      (localCohomologyModule A J₀ J₀.fg_of_isNoetherianRing (ModuleCat.of A M) i)
```

## Tag 0EFK, a lemma

[Tag 0EFK](https://stacks.math.columbia.edu/tag/0EFK) in the Stacks Project.

**`Stacks.Algebraization.isIso_homologyMap_localCohomologyComparison_stabilizingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean#L290). The attribute's comment: “H^i\_\{J₀}(M) = H^i\_J(M) for i ≤ s”.

> Under hypothesis (6) of Stacks 0EFK the local cohomology of `M` supported in the stabilizing
> ideal `J₀` of Stacks 0EFI agrees with the local cohomology supported in `J` in all degrees
> `i ≤ s`.

```lean
public theorem isIso_homologyMap_localCohomologyComparison_stabilizingIdeal
    (h6 : DepthGtOnAssociatedSubset (M := M) I J s) (i : ℤ) (hi : i ≤ s) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
      (localCohomologyComparison A J (stabilizingIdeal I J s d omega H)
        (Ideal.fg_of_isNoetherianRing J)
        (Ideal.fg_of_isNoetherianRing (stabilizingIdeal I J s d omega H))
        (stabilizingIdeal_le I J s d omega H)
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M))))
```

**`Stacks.Algebraization.isIso_homologyMap_localCohomologyComparison_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean#L315). The attribute's comment: “H^i\_J(M) = H^i\_\{J + I}(M) for i ≤ s”.

> Under hypothesis (6) of Stacks 0EFK the local cohomology of `M` supported in `J` agrees
> with the local cohomology supported in `J + I` in all degrees `i ≤ s`.

```lean
public theorem isIso_homologyMap_localCohomologyComparison_sup
    (h6 : DepthGtOnAssociatedSubset (M := M) I J s) (i : ℤ) (hi : i ≤ s) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
      (localCohomologyComparison A (J ⊔ I) J
        (Ideal.fg_of_isNoetherianRing (J ⊔ I)) (Ideal.fg_of_isNoetherianRing J) le_sup_left
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M))))
```

**`Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean#L330). The attribute's comment: “H^i\_\{J + I}(M) is annihilated by a power of I for i ≤ s”.

> Under hypothesis (6) of Stacks 0EFK a single power of `I` annihilates `H^i_{J + I}(M)` in
> every degree `i ≤ s`.

```lean
public theorem exists_pow_le_annihilator_localCohomologyModule_sup
    (h6 : DepthGtOnAssociatedSubset (M := M) I J s) (hs : 0 ≤ s) (hd : 0 ≤ d) :
    ∃ n : ℕ, ∀ i : ℤ, i ≤ s →
      I ^ n ≤ Module.annihilator A
        (localCohomologyModule A (J ⊔ I) (Ideal.fg_of_isNoetherianRing (J ⊔ I))
          (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_stabilizingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationDepthCollapse.lean#L384). The attribute's comment: “H^i\_\{J₀}(M) is annihilated by a power of I for i ≤ s”.

> Under hypothesis (6) of Stacks 0EFK a single power of `I` annihilates the local cohomology
> of `M` supported in the stabilizing ideal `J₀` of Stacks 0EFI, in every degree `i ≤ s`.

```lean
public theorem exists_pow_le_annihilator_localCohomologyModule_stabilizingIdeal
    (h6 : DepthGtOnAssociatedSubset (M := M) I J s) (hs : 0 ≤ s) (hd : 0 ≤ d) :
    ∃ n : ℕ, ∀ i : ℤ, i ≤ s →
      I ^ n ≤ Module.annihilator A
        (localCohomologyModule A (stabilizingIdeal I J s d omega H)
          (Ideal.fg_of_isNoetherianRing (stabilizingIdeal I J s d omega H))
          (ModuleCat.of A M) i)
```

## Tag 0EFL, a lemma

[Tag 0EFL](https://stacks.math.columbia.edu/tag/0EFL) in the Stacks Project.

**`Stacks.Algebraization.isAlgebraizationIdeal_of_zeroLocus_inter_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparison.lean, line 936](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparison.lean#L936). The attribute's comment: “existence of J₀ in the case V(J) ∩ V(I) = ∅, which the δmax and δmin fields of AlgebraizationHypotheses exclude and the source does not: the source's condition (5), the only one naming δ, is guarded by V(𝔭) ∩ V(J) ∩ V(I) ≠ ∅ and so is vacuous here. J₀ = J serves, for every s and on I-adic completeness alone. With exists\_isAlgebraizationIdeal, which is the nonempty case, this covers the tag”.

> **Stacks 0EFL when `V(J) ∩ V(I)` is empty.** For an `I`-adically complete Noetherian ring and
> ideals with `V(J) ∩ V(I) = ∅`, the ideal `J` itself has the property asserted of `J₀`, in every
> degree and for every finite module.
>
> This is the case of the source that the extreme values `δmax` and `δmin` of
> `Stacks.Algebraization.AlgebraizationHypotheses` exclude, and it is not vacuous: `J = A` is an
> instance. The source's conditions hold in it with no constraint beyond (1), because its condition
> (5), the only one mentioning `δ`, is guarded by `V(𝔭) ∩ V(J) ∩ V(I) ≠ ∅`.
>
> Completeness is what makes the case true. Since `I` lies in the Jacobson radical of an
> `I`-adically complete ring, every prime has a specialization in `V(I)`, so an admissible
> shrinking `J'` has `V(J') ∩ V(I) = ∅` only if `V(J')` is empty — that is, only for `J' = A`.
> Then `RΓ_{J'}(M)` is supported on the empty set, hence already derived `I`-complete, so the unit
> of derived completion is invertible at it; both sides are in fact zero.

```lean
public theorem isAlgebraizationIdeal_of_zeroLocus_inter_eq_empty
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (s : ℤ) (hcomplete : IsAdicComplete I A)
    (hJI : PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) = ∅) :
    IsAlgebraizationIdeal (M := M) I J s J
```

**`Stacks.Algebraization.exists_isAlgebraizationIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparison.lean, line 979](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparison.lean#L979). The attribute's comment: “existence of J₀ in the case V(J) ∩ V(I) ≠ ∅, which is what the δmax and δmin fields of AlgebraizationHypotheses presuppose; the empty case, where the source's condition (5) is vacuous, is isAlgebraizationIdeal\_of\_zeroLocus\_inter\_eq\_empty, and the two together are the tag. The dualizing complex is taken in the ring's own module universe”.

> **Stacks 0EFL.** Let `I` and `J` be ideals of a Noetherian ring `A`, let `M` be a finite
> `A`-module and let `s` and `d` be integers. Under conditions (1), (3), (4) and (5)
> of the source there is an ideal `J₀ ⊆ J` with `V(J₀) ∩ V(I) = V(J) ∩ V(I)` such that for every
> further ideal `J' ⊆ J₀` with the same intersection with `V(I)` the canonical map
>
> `RΓ_{J'}(M) ⟶ RΓ_J(M)^∧`
>
> is an isomorphism on cohomology in all degrees `≤ s`.
>
> The proof is the source's induction on `s`; the arrow is
> `Stacks.Algebraization.localCohomologyToCompletedLocalCohomology`, the composite of the unit of
> derived `I`-adic completion with the identification `RΓ_{J'}(M)^∧ ≅ RΓ_J(M)^∧` of the opening
> paragraph of the source, and the latter is invertible, so the assertion is exactly that the unit
> is invertible on cohomology in degrees `≤ s`. The case `s < 0`, where both sides vanish in the
> relevant degrees and `J₀ = J` serves, is
> `Stacks.Algebraization.isAlgebraizationIdeal_of_lt_zero`.

```lean
public theorem exists_isAlgebraizationIdeal
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I J : Ideal A) (s d : ℤ) (omega : DerivedCategory (ModuleCat.{u} A))
    (δ : PrimeSpectrum A → ℤ) (δmax δmin : ℤ)
    (H : AlgebraizationHypotheses (M := M) I J s d omega δ δmax δmin) :
    ∃ J₀ : Ideal A, IsAlgebraizationIdeal (M := M) I J s J₀
```

**`Stacks.Algebraization.exists_isAlgebraizationIdeal_of_sourceHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparisonSource.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparisonSource.lean#L73).

> **Stacks 0EFL.** Let `I, J` be ideals of a Noetherian ring `A`, let `M` be a finite
> `A`-module, let `s, d` be integers, and let `T = {𝔭 : V(𝔭) ∩ V(I) ⊆ V(J) ∩ V(I)}`. Assume
> 1. `A` is `I`-adically complete and has a dualizing complex;
> 2. (no condition at primes of `V(I)`);
> 3. `cd(A, I) ≤ d`;
> 4. if `𝔭 ∉ V(I)`, `𝔭 ∉ T`, then `depth(M_𝔭) ≥ s` or `depth(M_𝔭) + dim((A/𝔭)_𝔮) > d + s` for
>    all `𝔮 ∈ V(𝔭) ∩ V(J) ∩ V(I)`;
> 5. for a dimension function `δ`, with `δmax` and `δmin` the maximum and the minimum of `δ` on
>    `V(J) ∩ V(I)`: if `𝔭 ∉ V(I)`, `𝔭 ∉ T`, `V(𝔭) ∩ V(J) ∩ V(I) ≠ ∅` and `depth(M_𝔭) < s`, then
>    (a) `dim(Supp(M_𝔭)) < s + 2`, or (b) `δ(𝔭) > d + δmax - 1`, or
>    (c) `depth(M_𝔭) + dim((A/𝔭)_𝔮) > d + s + δmax - δmin - 2` for all
>    `𝔮 ∈ V(𝔭) ∩ V(J) ∩ V(I)`.
>
> Then there is an ideal `J₀ ⊆ J` with `V(J₀) ∩ V(I) = V(J) ∩ V(I)` such that for every
> `J' ⊆ J₀` with `V(J') ∩ V(I) = V(J) ∩ V(I)` the map `RΓ_{J'}(M) → RΓ_J(M)^∧` is an isomorphism
> on cohomology in degrees `≤ s` (`Stacks.Algebraization.IsAlgebraizationIdeal`).
>
> The proof is by cases. If `V(J) ∩ V(I)` is empty, `J₀ = J` serves
> (`isAlgebraizationIdeal_of_zeroLocus_inter_eq_empty`). Otherwise the extreme values of `δ` on
> `V(J) ∩ V(I)` exist (`exists_isGreatest_isLeast_image_dimensionFunction`, using that `A` has
> finite Krull dimension by Stacks 0A80), and `exists_isAlgebraizationIdeal` applies.

```lean
public theorem exists_isAlgebraizationIdeal_of_sourceHypotheses (I J : Ideal A) (s d : ℤ)
    (hcomplete : IsAdicComplete I A)
    (hdual : ∃ ω : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex ω)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I I.fg_of_isNoetherianRing ≤ d)
    (h4 : ∀ p : PrimeSpectrum A,
      p ∉ PrimeSpectrum.zeroLocus (I : Set A) →
      p ∉ associatedSubset I J →
      ((enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) ≥ (s : EInt)) ∨
        (∀ q : PrimeSpectrum A,
          q ∈ (PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩
            PrimeSpectrum.zeroLocus (J : Set A)) ∩
            PrimeSpectrum.zeroLocus (I : Set A) →
          enatToEInt
              (Module.depth (Localization.AtPrime p.asIdeal)
                (maximalIdeal (Localization.AtPrime p.asIdeal))
                (LocalizedModule p.asIdeal.primeCompl M)) +
              krullDimToEInt
                (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
                  p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) >
            ((d + s : ℤ) : EInt))))
    (h5 : ∃ δ : TopologicalSpace.DimensionFunction (PrimeSpectrum A),
      ∀ δmax δmin : ℤ,
      IsGreatest (δ.toFun '' (PrimeSpectrum.zeroLocus (J : Set A) ∩
        PrimeSpectrum.zeroLocus (I : Set A))) δmax →
      IsLeast (δ.toFun '' (PrimeSpectrum.zeroLocus (J : Set A) ∩
        PrimeSpectrum.zeroLocus (I : Set A))) δmin →
      ∀ p : PrimeSpectrum A,
      p ∉ PrimeSpectrum.zeroLocus (I : Set A) →
      p ∉ associatedSubset I J →
      ((PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩
        PrimeSpectrum.zeroLocus (J : Set A)) ∩
        PrimeSpectrum.zeroLocus (I : Set A)).Nonempty →
      enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) < (s : EInt) →
      (krullDimToEInt (Module.supportDim (Localization.AtPrime p.asIdeal)
            (LocalizedModule p.asIdeal.primeCompl M)) < ((s + 2 : ℤ) : EInt) ∨
        (d + δmax - 1 < δ.toFun p) ∨
        (∀ q : PrimeSpectrum A,
          q ∈ (PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩
            PrimeSpectrum.zeroLocus (J : Set A)) ∩
            PrimeSpectrum.zeroLocus (I : Set A) →
          enatToEInt
              (Module.depth (Localization.AtPrime p.asIdeal)
                (maximalIdeal (Localization.AtPrime p.asIdeal))
                (LocalizedModule p.asIdeal.primeCompl M)) +
              krullDimToEInt
                (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
                  p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) >
            ((d + s + δmax - δmin - 2 : ℤ) : EInt)))) :
    ∃ J₀ : Ideal A, IsAlgebraizationIdeal (M := M) I J s J₀
```

## Tag 0EFM, an example

[Tag 0EFM](https://stacks.math.columbia.edu/tag/0EFM) in the Stacks Project.

**`Stacks.Algebraization.MittagLefflerFailure.pow_mul_pow_mem_modIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean#L314). The attribute's comment: “the containment `(yⁿ) ⊆` the image: `xⁿyⁿ = pⁿ` in `M`”.

> `xⁿyⁿ = pⁿ` in `M`, so `xⁿyⁿ` lies in `(xy - p, pⁿ)`.

```lean
theorem pow_mul_pow_mem_modIdeal (n : ℕ) : varX p ^ n * varY p ^ n ∈ modIdeal p n
```

**`Stacks.Algebraization.MittagLefflerFailure.mem_span_of_pow_mul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean#L401). The attribute's comment: “the containment image `⊆ (yⁿ)`: an `x`-power-torsion element mod `(xy - p, pⁿ)` lies in `(p, xy, yⁿ)`”.

> **The `x`-power-torsion of `A/(xy - p, pⁿ⁺¹)` is carried by `(xy - p, yⁿ⁺¹)`.** If
> `x^k f ∈ (xy - p, pⁿ⁺¹)` then `f ∈ (p, xy, yⁿ⁺¹)`.

```lean
theorem mem_span_of_pow_mul_mem (n k : ℕ) (f : MvPowerSeries (Fin 2) ℤ_[p])
    (hf : varX p ^ k * f ∈ modIdeal p (n + 1)) :
    f ∈ Ideal.span {((p : ℕ) : MvPowerSeries (Fin 2) ℤ_[p]), varX p * varY p,
      varY p ^ (n + 1)}
```

**`Stacks.Algebraization.MittagLefflerFailure.imageSections_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean#L458). The attribute's comment: “the example: the image of `H⁰_J(M/pⁿM) ⟶ H⁰_J(M/pM)` is the ideal generated by `yⁿ` in `M/pM = A/(p, xy)`, for `A = ℤ_p[[x,y]]`, `I = (p)`, `J = (p, x)` and `M = A/(xy - p)`”.

> **Stacks 0EFM.** The image of `H⁰_J(M/pⁿM) → H⁰_J(M/pM)` is the ideal generated by `yⁿ` in
> `M/pM = A/(p, xy)`, for `A = ℤ_p[[x, y]]`, `I = (p)`, `J = (p, x)` and `M = A/(xy - p)`.

```lean
theorem imageSections_eq (n : ℕ) :
    imageSections p n = Submodule.restrictScalars (MvPowerSeries (Fin 2) ℤ_[p])
      (Ideal.span {Ideal.Quotient.mk (modIdeal p 1) (varY p ^ (n + 1))})
```

**`Stacks.Algebraization.MittagLefflerFailure.not_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationMittagLefflerFailure.lean#L514). The attribute's comment: “the point of the example: the inverse system `H⁰_J(M/pⁿM)` does NOT satisfy the Mittag-Leffler condition, so the hypothesis of Lemma 0EFL cannot be dropped”.

> **The inverse system `n ↦ H⁰_J(M/pⁿM)` is not Mittag-Leffler.** The images of its transition
> maps into `H⁰_J(M/pM)` never stabilise.

```lean
theorem not_mittagLeffler :
    ¬ ∃ m : ℕ, ∀ k, m ≤ k → imageSections p k = imageSections p m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.8, Tag 0EFF](https://stacks.math.columbia.edu/tag/0EFF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
