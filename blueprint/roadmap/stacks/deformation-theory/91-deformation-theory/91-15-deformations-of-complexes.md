---
declaration: section
origin: cited
lean: Deformation.Obstruction.canonicalObstructionMap_baseChange, Deformation.Obstruction.existsUnique_isCanonicalObstructionMap, Deformation.Obstruction.canonicalObstructionMap_natural, Deformation.Obstruction.canonicalObstructionMap_eq_zero_iff_exists_lift
statement: formalized
proof: formalized
---

# 91.15 Deformations of complexes

Section 91.15 of the Stacks Project, [Tag 0DYQ](https://stacks.math.columbia.edu/tag/0DYQ). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DYR, a lemma

[Tag 0DYR](https://stacks.math.columbia.edu/tag/0DYR) in the Stacks Project.

**`Deformation.Obstruction.canonicalObstructionMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CanonicalObstructionBaseChange.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CanonicalObstructionBaseChange.lean#L345). The attribute's comment: “part (3)”.

> **The canonical obstruction morphism is compatible with base change.** Derived base change
> along `b` carries the canonical obstruction morphism of a bounded-above `K` for the square-zero
> surjection `fR` to the canonical obstruction morphism of its base change for `fS`, read through
> the comparison of the two targets attached to a bounded-above free K-flat representative `P` of
> `K` and a K-flat resolution `q` of `I/I²`.

```lean
theorem canonicalObstructionMap_baseChange
    (hI : RingHom.ker fR ^ 2 = ⊥)
    (hJ : RingHom.ker fS = Ideal.map a (RingHom.ker fR))
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).minus K)
    (P : CochainComplex (ModuleCat.{u} R) ℤ) (m : ℤ) (hPLE : P.IsStrictlyLE m)
    (hfree : ∀ n, Module.Free R (P.X n)) (hP : P.KFlat)
    (e : DerivedCategory.Q.obj P ≅ K)
    (T : CochainComplex (ModuleCat.{u} R) ℤ) (k : ℤ) (hTLE : T.IsStrictlyLE k)
    (hTproj : ∀ i, Projective (T.X i)) (hT : T.KFlat)
    (q : T ⟶ kernelComplex fR hfR) (hq : QuasiIso q)
    (hQq : IsIso (DerivedCategory.Q.map q)) :
    (derivedExtensionScalarsGeneral.{u, u, u} b).functor.map
        (canonicalObstructionMap fR hfR hI K hK).1 ≫
      ((derivedExtensionScalarsGeneral.{u, u, u} b).functor.commShiftIso (2 : ℤ)).hom.app
          (((canonicalDerivedTensorProductFunctor R).obj K).obj
            (squareZeroKernelObject fR hfR)) ≫
        (shiftFunctor (DerivedCategory (ModuleCat.{u} S)) (2 : ℤ)).map
          (obstructionTargetBaseChangeMap fR hfR fS hfS a b hcomm P hP e T hT q hQq) =
      (canonicalObstructionMap fS hfS (ker_sq_eq_bot_baseChange fR fS a hJ hI)
        ((derivedExtensionScalarsGeneral.{u, u, u} b).functor.obj K)
        ((derivedExtensionScalarsGeneral.{u, u, u} b).maps_boundedAbove ⟨K, hK⟩)).1
```

**`Deformation.Obstruction.existsUnique_isCanonicalObstructionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CanonicalObstructionMap/DerivedMorphism.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CanonicalObstructionMap/DerivedMorphism.lean#L296). The attribute's comment: “canonical_obstruction_map”.

> There is a unique morphism represented by the squares of lifted differentials on every
> bounded-above free representative, independently of the lifts and all comparison data.

```lean
theorem existsUnique_isCanonicalObstructionMap
    (f : R' →+* R) (hf : Function.Surjective f) (hzero : (RingHom.ker f) ^ 2 = ⊥)
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).minus K) :
    ∃! ω : K ⟶ (((canonicalDerivedTensorProductFunctor R).obj K).obj
      (squareZeroKernelObject f hf))⟦(2 : ℤ)⟧, IsCanonicalObstructionMap f hf K ω
```

**`Deformation.Obstruction.canonicalObstructionMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CanonicalObstructionNaturality.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CanonicalObstructionNaturality.lean#L337). The attribute's comment: “naturality”.

> The canonical obstruction morphism commutes with every morphism of bounded-above
> derived complexes.

```lean
theorem canonicalObstructionMap_natural
    {R' R : Type u} [CommRing R'] [CommRing R]
    (f : R' →+* R) (hf : Function.Surjective f)
    (hzero : (RingHom.ker f) ^ 2 = ⊥)
    {K L : DerivedCategory (ModuleCat.{u} R)}
    (hK : (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).minus K)
    (hL : (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).minus L)
    (g : K ⟶ L) :
    g ≫ (Deformation.Obstruction.canonicalObstructionMap
      f hf hzero L hL).val =
      (Deformation.Obstruction.canonicalObstructionMap
        f hf hzero K hK).val ≫
        (shiftFunctor (DerivedCategory (ModuleCat.{u} R)) (2 : ℤ)).map
          (((canonicalDerivedTensorProductFunctor R).map g).app
            (Deformation.Obstruction.squareZeroKernelObject f hf))
```

**`Deformation.Obstruction.canonicalObstructionMap_eq_zero_iff_exists_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CanonicalObstructionVanishing.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CanonicalObstructionVanishing.lean#L714). The attribute's comment: “vanishing_criterion”.

> A bounded-above derived complex over `R` lifts across a square-zero surjection
> `R' → R` exactly when its canonical obstruction morphism is zero.

```lean
theorem canonicalObstructionMap_eq_zero_iff_exists_lift
    {R' R : Type u} [CommRing R'] [CommRing R]
    (f : R' →+* R) (hf : Function.Surjective f)
    (hzero : (RingHom.ker f) ^ 2 = ⊥)
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : (DerivedCategory.TStructure.t (C := ModuleCat.{u} R)).minus K) :
      (Deformation.Obstruction.canonicalObstructionMap f hf hzero K hK).val = 0 ↔
      ∃ K' : DerivedCategory (ModuleCat.{u} R'),
        Nonempty ((derivedExtensionScalarsGeneral.{u, u, u} f).functor.obj K' ≅ K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.15, Tag 0DYQ](https://stacks.math.columbia.edu/tag/0DYQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
