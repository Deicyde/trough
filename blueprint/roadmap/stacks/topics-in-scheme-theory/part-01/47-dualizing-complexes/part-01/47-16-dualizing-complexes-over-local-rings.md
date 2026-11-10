---
declaration: section
origin: cited
lean: Dualizing.IsNormalizedDualizingComplex, Dualizing.exists_isNormalizedDualizingComplex_shift, Dualizing.isNormalizedDualizingComplex_shift_iff_eq, Dualizing.isNormalizedDualizingComplex_derivedHom, Dualizing.linearEquivalenceFiniteLengthIsoIdentity, Dualizing.derivedHomFiniteLengthIsoMatlisDual, Dualizing.depth_eq_least_nonzero_negative_ext, Dualizing.ext_degree_mem_Icc_of_nontrivial
statement: formalized
proof: formalized
---

# 47.16 Dualizing complexes over local rings

Section 47.16 of the Stacks Project, [Tag 0A7M](https://stacks.math.columbia.edu/tag/0A7M). 11 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A7M, the section

[Tag 0A7M](https://stacks.math.columbia.edu/tag/0A7M) in the Stacks Project.

Declarations registered for the tag:

- [`Dualizing.IsNormalizedDualizingComplex`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Normalized.lean#L59), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean#L46) (StacksFrontier): “the normalization convention `RHom_A(κ, ω_A^•) = κ` in degree zero”.
- [`Dualizing.exists_isNormalizedDualizingComplex_shift`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedShift.lean#L324), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean#L48) (StacksFrontier): “every dualizing complex over a Noetherian local ring is a shift of a normalized one”.
- [`Dualizing.isNormalizedDualizingComplex_shift_iff_eq`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedShift.lean#L349), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedDualizingConvention.lean#L50) (StacksFrontier): “the normalizing shift is unique”.

## Tag 0AX1, a lemma

[Tag 0AX1](https://stacks.math.columbia.edu/tag/0AX1) in the Stacks Project.

**`Dualizing.isNormalizedDualizingComplex_derivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedFiniteMap.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedFiniteMap.lean#L162).

> **Stacks Project, Tag 0AX1.** If `A → B` is a finite local homomorphism of Noetherian local
> rings and `K` is a normalized dualizing complex over `A`, then `RHom_A(B, K)` is a normalized
> dualizing complex over `B`.

```lean
theorem isNormalizedDualizingComplex_derivedHom
    {A B : Type u} [CommRing A] [CommRing B]
    [IsLocalRing A] [IsLocalRing B] [IsNoetherianRing A] [IsNoetherianRing B]
    (f : A →+* B) [IsLocalHom f] (hf : f.Finite)
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) :
    IsNormalizedDualizingComplex.{u, v}
      ((derivedHom.{u, v} f).obj K)
```

## Tag 0A7N, a lemma

[Tag 0A7N](https://stacks.math.columbia.edu/tag/0A7N) in the Stacks Project.

**`Dualizing.isNormalizedDualizingComplex_derivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedFiniteMap.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedFiniteMap.lean#L162). The attribute's comment: “the surjective case, a surjection of local rings being a finite local homomorphism”.

> **Stacks Project, Tag 0AX1.** If `A → B` is a finite local homomorphism of Noetherian local
> rings and `K` is a normalized dualizing complex over `A`, then `RHom_A(B, K)` is a normalized
> dualizing complex over `B`.

```lean
theorem isNormalizedDualizingComplex_derivedHom
    {A B : Type u} [CommRing A] [CommRing B]
    [IsLocalRing A] [IsLocalRing B] [IsNoetherianRing A] [IsNoetherianRing B]
    (f : A →+* B) [IsLocalHom f] (hf : f.Finite)
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) :
    IsNormalizedDualizingComplex.{u, v}
      ((derivedHom.{u, v} f).obj K)
```

## Tag 0A7P, a lemma

[Tag 0A7P](https://stacks.math.columbia.edu/tag/0A7P) in the Stacks Project.

**`Dualizing.linearEquivalenceFiniteLengthIsoIdentity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complex/Local.lean, line 888](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complex/Local.lean#L888).

> Every linear self-equivalence of finite-length modules over a Noetherian local ring is
> naturally isomorphic to the identity functor.

```lean
theorem linearEquivalenceFiniteLengthIsoIdentity
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (F : ObjectProperty.FullSubcategory (fun M : ModuleCat.{u} A => IsFiniteLength A M) ≌
      ObjectProperty.FullSubcategory (fun M : ModuleCat.{u} A => IsFiniteLength A M))
    [F.functor.Linear A] :
    Nonempty (F.functor ≅ 𝟭 (ObjectProperty.FullSubcategory
      (fun M : ModuleCat.{u} A => IsFiniteLength A M)))
```

## Tag 0A7Q, a lemma

[Tag 0A7Q](https://stacks.math.columbia.edu/tag/0A7Q) in the Stacks Project.

**`Dualizing.derivedHomFiniteLengthIsoMatlisDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/FiniteLengthMatlisDuality/MatlisComparison.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FiniteLengthMatlisDuality/MatlisComparison.lean#L764).

> **Stacks Project, Tag 0A7Q.** Derived Hom into a normalized dualizing complex agrees
> naturally, on finite-length modules, with Matlis duality into an injective hull of the residue
> field.

```lean
public theorem derivedHomFiniteLengthIsoMatlisDual
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K)
    (E : ModuleCat.{max v u} A)
    (i : (ModuleCat.uliftFunctor.{v} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    Nonempty
      (derivedHomFiniteLengthFunctor A K ≅ matlisDualFiniteLengthFunctor A E)
```

## Tag 0A7U, a lemma

[Tag 0A7U](https://stacks.math.columbia.edu/tag/0A7U) in the Stacks Project.

**`Dualizing.depth_eq_least_nonzero_negative_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DepthFromExt.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DepthFromExt.lean#L287). The attribute's comment: “depth_from_ext”.

> **Stacks Project, Tag 0A7U, part (3).** For a nonzero finite module over a
> Noetherian local ring, depth is the least nonnegative integer `δ` for which
> `Ext^(-δ)(M, ω_A^•)` is nonzero.

```lean
public theorem depth_eq_least_nonzero_negative_ext
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {M : Type (max v u)}
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (omega : DerivedCategory (ModuleCat.{max v u} A))
    (homega : IsNormalizedDualizingComplex omega)
    (hM : Nontrivial M) :
    ∃ delta : ℕ,
      IsLeast
          {i : ℕ |
            Nontrivial
              (DerivedCategory.Ext
                ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
                  (ModuleCat.of A M))
                omega (-(i : ℤ)))}
          delta ∧
        Module.depth A (IsLocalRing.maximalIdeal A) M = (delta : ℕ∞)
```

**`Dualizing.ext_degree_mem_Icc_of_nontrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ExtDegreeBounds.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/ExtDegreeBounds.lean#L430). The attribute's comment: “ext_degree_bounds”. References: SGA 2 V (3.1), “(i)”.

> **Stacks Project, Tag 0A7U.** For a nonzero finite module `M` of support dimension `d`,
> Ext from `M` into a normalized dualizing complex can be nonzero only in the integer degrees
> from `-d` through `0`.

```lean
theorem ext_degree_mem_Icc_of_nontrivial
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {M : Type (max v u)} [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K)
    (d : ℕ) (hd : Module.supportDim A M = (d : WithBot ℕ∞))
    (i : ℤ)
    (hi : Nontrivial
      (DerivedCategory.Ext
        ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
          (ModuleCat.of A M)) K i)) :
    i ∈ Set.Icc (-(d : ℤ)) 0
```

**`Dualizing.supportDim_ext_le_neg_degree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ExtSupportBound.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/ExtSupportBound.lean#L357). The attribute's comment: “ext_support_bound”. References: SGA 2 V (3.1), “(ii)”.

> **Stacks Project, Tag 0A7U, support bound.** If `K` is a normalized dualizing
> complex over a Noetherian local ring `A` and `M` is a nonzero finite `A`-module, then
> the support of `Ext^i_A(M, K)` has dimension at most `-i` for every integer `i`.

```lean
public theorem supportDim_ext_le_neg_degree
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (M : Type (max v u))
    [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    (hK : IsNormalizedDualizingComplex K) (i : ℤ) :
    Module.supportDim A
        (DerivedCategory.Ext
          ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
            (ModuleCat.of A M)) K i) ≤
      if i ≤ 0 then (((Int.toNat (-i) : ℕ) : ℕ∞) : WithBot ℕ∞) else ⊥
```

## Tag 0B5A, a lemma

[Tag 0B5A](https://stacks.math.columbia.edu/tag/0B5A) in the Stacks Project.

**`Dualizing.isCohenMacaulay_iff_ext_concentrated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayCriterion.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/CohenMacaulayCriterion.lean#L287). The attribute's comment: “cm_criterion”.

> **Stacks Project, Tag 0B5A.** For a nonzero finite module over a Noetherian local ring with
> normalized dualizing complex, Cohen--Macaulayness is equivalent to `Ext` into the dualizing
> complex being nonzero in at most one degree, and also to its being concentrated in degree minus
> the dimension of the support.

```lean
public theorem isCohenMacaulay_iff_ext_concentrated
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {M : Type (max v u)} [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K) :
    List.TFAE [
      Module.IsCohenMacaulayAtMaximalIdeal A M,
      ∀ i j : ℤ,
        Nontrivial (DerivedCategory.Ext
          ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
            (ModuleCat.of A M)) K i) →
        Nontrivial (DerivedCategory.Ext
          ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
            (ModuleCat.of A M)) K j) → i = j,
      ∀ i : ℤ,
        ¬ (0 ≤ i ∧ Module.supportDim A M = ((i.toNat : ℕ∞) : WithBot ℕ∞)) →
          Subsingleton (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
              (ModuleCat.of A M)) K (-i))]
```

**`Dualizing.cohenMacaulayExtDuality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayDuality.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/CohenMacaulayDuality.lean#L1041). The attribute's comment: “cm_duality, that CM_d is anti-autoequivalent to itself”.

> **Cohen--Macaulay duality (Stacks Project, Tag 0B5A).** For a normalized dualizing complex,
> `Ext` in degree minus the depth induces an anti-autoequivalence of the category of finite
> Cohen--Macaulay modules of that depth.

```lean
public noncomputable def cohenMacaulayExtDuality
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (omega : DerivedCategory (ModuleCat.{max u v} A))
    (homega : IsNormalizedDualizingComplex omega) (d : ℕ) :
    (CohenMacaulayModulesOfDepth.{u, max u v} A d)ᵒᵖ ≌
      CohenMacaulayModulesOfDepth.{u, max (u + 1) (v + 1)} A d
```

**`Dualizing.cohenMacaulayExtDuality_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayDuality.lean, line 1052](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/CohenMacaulayDuality.lean#L1052). The attribute's comment: “cm_duality, that the anti-autoequivalence is M ↦ Ext^{-d}(M, ω)”.

> The duality functor, after forgetting the Cohen--Macaulay condition, is naturally the
> canonical contravariant `Ext^{-d}` functor.

```lean
public theorem cohenMacaulayExtDuality_forget
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (omega : DerivedCategory (ModuleCat.{max u v} A))
    (homega : IsNormalizedDualizingComplex omega) (d : ℕ) :
    Nonempty
      ((cohenMacaulayExtDuality omega homega d).functor ⋙
          (IsCohenMacaulayModuleOfDepth.{u, max (u + 1) (v + 1)} A d).ι ≅
        (IsCohenMacaulayModuleOfDepth.{u, max u v} A d).ι.op ⋙
          extIntoDualizingComplex omega d)
```

## Tag 0A7R, a lemma

[Tag 0A7R](https://stacks.math.columbia.edu/tag/0A7R) in the Stacks Project.

**`Dualizing.nonempty_iso_single_injectiveHull_of_ringKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedZeroDimensional.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedZeroDimensional.lean#L75).

> **Stacks Project, Tag 0A7R.** A normalized dualizing complex over a zero-dimensional
> Noetherian local ring is an injective hull of the residue field placed in degree zero.

```lean
theorem nonempty_iso_single_injectiveHull_of_ringKrullDim_eq_zero
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) (hdim : ringKrullDim A = 0)
    (E : ModuleCat.{max v u} A)
    (i : (ModuleCat.uliftFunctor.{v} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    Nonempty (K ≅ (DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj E)
```

## Tag 0A7S, a lemma

[Tag 0A7S](https://stacks.math.columbia.edu/tag/0A7S) in the Stacks Project.

**`Dualizing.exists_distTriang_normalizedDualizing_quotient_finiteLengthIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedFiniteLengthQuotient.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedFiniteLengthQuotient.lean#L317).

> **Stacks Project, Tag 0A7S.** If `I` is a finite-length ideal contained in the
> maximal ideal of a Noetherian local ring `A`, a normalized dualizing complex of `A / I`,
> restricted to `A`, fits into a distinguished triangle with the normalized dualizing complex
> of `A` and the degree-zero complex on `Hom_A(I, E)`, for any injective hull `E` of the
> residue field.

```lean
theorem exists_distTriang_normalizedDualizing_quotient_finiteLengthIdeal
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K)
    (I : Ideal A) (hI : I ≤ IsLocalRing.maximalIdeal A) (hIfl : IsFiniteLength A I)
    (E : ModuleCat.{max v u} A)
    (i : (ModuleCat.uliftFunctor.{v} A).obj
      (ModuleCat.of A (A ⧸ IsLocalRing.maximalIdeal A)) ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    letI : Nontrivial (A ⧸ I) := Ideal.Quotient.nontrivial_iff.mpr
      (lt_of_le_of_lt hI
        (inferInstance : (IsLocalRing.maximalIdeal A).IsMaximal).lt_top).ne
    letI : IsLocalRing (A ⧸ I) :=
      IsLocalRing.of_surjective' (Ideal.Quotient.mk I) Ideal.Quotient.mk_surjective
    ∃ (KB : DerivedCategory (ModuleCat.{max v u} (A ⧸ I))),
      IsNormalizedDualizingComplex KB ∧
        ∃ (f : ((ModuleCat.restrictScalars (Ideal.Quotient.mk I)).mapDerivedCategory).obj KB ⟶ K)
          (g : K ⟶ (DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
            (ModuleCat.of A (I →ₗ[A] E)))
          (δ : (DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj
              (ModuleCat.of A (I →ₗ[A] E)) ⟶
            (shiftFunctor (DerivedCategory (ModuleCat.{max v u} A)) (1 : ℤ)).obj
              (((ModuleCat.restrictScalars
                (Ideal.Quotient.mk I)).mapDerivedCategory).obj KB)),
          Triangle.mk f g δ ∈ distTriang (DerivedCategory (ModuleCat.{max v u} A))
```

## Tag 0A7T, a lemma

[Tag 0A7T](https://stacks.math.columbia.edu/tag/0A7T) in the Stacks Project.

**`Dualizing.exists_distinguishedTriangle_quotient_nonZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedRegularQuotient.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedRegularQuotient.lean#L330).

> **Stacks Project, Tag 0A7T.** Dividing a Noetherian local ring by a nonzerodivisor in
> its maximal ideal produces a normalized dualizing complex fitting into the distinguished
> triangle induced by multiplication by that element.

```lean
theorem exists_distinguishedTriangle_quotient_nonZeroDivisor
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K)
    (f : A) (hf : f ∈ IsLocalRing.maximalIdeal A)
    (hfreg : f ∈ nonZeroDivisors A) :
    letI : Nontrivial (A ⧸ Ideal.span {f}) := Ideal.Quotient.nontrivial_iff.mpr
      (lt_of_le_of_lt (Ideal.span_le.2 (Set.singleton_subset_iff.mpr hf))
        (inferInstance : (IsLocalRing.maximalIdeal A).IsMaximal).lt_top).ne
    letI : IsLocalRing (A ⧸ Ideal.span {f}) :=
      IsLocalRing.of_surjective' (Ideal.Quotient.mk (Ideal.span {f}))
        Ideal.Quotient.mk_surjective
    ∃ (KB : DerivedCategory (ModuleCat.{max v u} (A ⧸ Ideal.span {f}))),
      IsNormalizedDualizingComplex.{u, v} KB ∧
        ∃ (i : ((ModuleCat.restrictScalars
              (Ideal.Quotient.mk (Ideal.span {f}))).mapDerivedCategory).obj KB ⟶ K)
          (δ : K ⟶ (shiftFunctor (DerivedCategory (ModuleCat.{max v u} A)) (1 : ℤ)).obj
            (((ModuleCat.restrictScalars
              (Ideal.Quotient.mk (Ideal.span {f}))).mapDerivedCategory).obj KB)),
          Triangle.mk i (f • 𝟙 K) δ ∈ distTriang (DerivedCategory (ModuleCat.{max v u} A))
```

## Tag 0A7V, a lemma

[Tag 0A7V](https://stacks.math.columbia.edu/tag/0A7V) in the Stacks Project.

**`Dualizing.nontrivial_localized_homology_iff_eq_neg_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/MinimalPrimeNonvanishing.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/MinimalPrimeNonvanishing.lean#L506).

> **Stacks Project, Tag 0A7V.** Let `A` be a Noetherian local ring with a normalized dualizing
> complex `K`, and let `p` be a minimal prime of `A` with `dim(A/p) = e`. Then the localization at
> `p` of the cohomology module `H^i(K)` is nonzero if and only if `i = -e`.

```lean
theorem nontrivial_localized_homology_iff_eq_neg_dimension
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K)
    (p : PrimeSpectrum A) (hp : IsMinimalPrime p.asIdeal) (e : ℕ)
    (hdim : ringKrullDim (A ⧸ p.asIdeal) = (e : WithBot ℕ∞)) (i : ℤ) :
    Nontrivial (LocalizedModule p.asIdeal.primeCompl
        ((DerivedCategory.homologyFunctor (ModuleCat.{max v u} A) i).obj K)) ↔
      i = -(e : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.16, Tag 0A7M](https://stacks.math.columbia.edu/tag/0A7M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
