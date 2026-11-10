---
declaration: section
origin: cited
lean: Dualizing.LocalDuality.exists_isInjectiveHull_homology_zero_localCohomology, Dualizing.LocalDuality.nonempty_localCohomology_iso_single_homology_zero, Dualizing.LocalDuality.nonempty_localCohomology_iso_localCohomology, Dualizing.LocalDuality.injectiveHullUnitsMulEquivUnitsAdicCompletion, Dualizing.IsNormalizedDualizingComplex.nonempty_iso, Dualizing.IsDualizingComplex.autMulEquivUnits, exists_isInjectiveHull_homology_zero_localCohomology, nonempty_localCohomology_iso_single_homology_zero
statement: formalized
proof: formalized
---

# 47.18 The local duality theorem

Section 47.18 of the Stacks Project, [Tag 0A81](https://stacks.math.columbia.edu/tag/0A81). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A82, a lemma

[Tag 0A82](https://stacks.math.columbia.edu/tag/0A82) in the Stacks Project.

**`Dualizing.LocalDuality.exists_isInjectiveHull_homology_zero_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/NormalizedDualizingComplex/InjectiveHull.lean, line 663](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/NormalizedDualizingComplex/InjectiveHull.lean#L663). The attribute's comment: “injective hull”.

> The degree-zero local cohomology of a normalized dualizing complex at the closed point is an
> injective hull of the residue field.

```lean
public theorem exists_isInjectiveHull_homology_zero_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K) :
    let m := IsLocalRing.maximalIdeal A
    let hm : m.FG := IsNoetherian.noetherian m
    let L := (derivedPowerTorsionProperty A m hm).ι.obj
      ((localCohomologyFunctor A m hm).obj K)
    let E := (DerivedCategory.homologyFunctor (ModuleCat.{max v u} A) 0).obj L
    ∃ (i : (ModuleCat.uliftFunctor.{v} A).obj
          (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
        (hi : Mono i),
      @Module.IsInjectiveHull (ModuleCat.{max v u} A) _ _ _ _ _ i hi
```

**`Dualizing.LocalDuality.nonempty_localCohomology_iso_single_homology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/NormalizedDualizingComplex/InjectiveHull.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/NormalizedDualizingComplex/InjectiveHull.lean#L687). The attribute's comment: “concentration in degree zero”.

> Local cohomology of a normalized dualizing complex at the closed point is its degree-zero
> cohomology module placed in degree zero.

```lean
public theorem nonempty_localCohomology_iso_single_homology_zero
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex K) :
    let m := IsLocalRing.maximalIdeal A
    let hm : m.FG := IsNoetherian.noetherian m
    let L := (derivedPowerTorsionProperty A m hm).ι.obj
      ((localCohomologyFunctor A m hm).obj K)
    let E := (DerivedCategory.homologyFunctor (ModuleCat.{max v u} A) 0).obj L
    Nonempty (L ≅ (DerivedCategory.singleFunctor (ModuleCat.{max v u} A) 0).obj E)
```

## Tag 0A83, a remark

[Tag 0A83](https://stacks.math.columbia.edu/tag/0A83) in the Stacks Project.

**`Dualizing.LocalDuality.nonempty_localCohomology_iso_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L71). The attribute's comment: “the realization is independent of the normalized dualizing complex”.

> Let `(A, 𝔪, κ)` be a Noetherian local ring and let `Z = V(𝔪)`. If `ω` and `ω'` are normalized
> dualizing complexes for `A`, then `RΓ_Z(ω) ≅ RΓ_Z(ω')` in `D(A)`.

```lean
public theorem nonempty_localCohomology_iso_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (ω ω' : DerivedCategory (ModuleCat.{max v u} A))
    (hω : IsNormalizedDualizingComplex.{u, v} ω)
    (hω' : IsNormalizedDualizingComplex.{u, v} ω') :
    Nonempty
      ((derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).ι.obj
            ((localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).obj ω) ≅
          (derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).ι.obj
            ((localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).obj ω'))
```

**`Dualizing.LocalDuality.injectiveHullUnitsMulEquivUnitsAdicCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L101). The attribute's comment: “the automorphism group of an injective hull of the residue field is the units of the completion”.

> Let `(A, 𝔪, κ)` be a Noetherian local ring and let `i : κ ⟶ E` present `E` as an injective
> hull of the residue field. The units of `End_A(E)` are the units of the `𝔪`-adic completion
> `A^∧` of `A`.

```lean
public def injectiveHullUnitsMulEquivUnitsAdicCompletion
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (E : Type u) [AddCommGroup E] [Module A E]
    (i : ModuleCat.of A (A ⧸ IsLocalRing.maximalIdeal A) ⟶ ModuleCat.of A E)
    [Mono i] (hi : Module.IsInjectiveHull i) :
    (Module.End A E)ˣ ≃* (AdicCompletion (IsLocalRing.maximalIdeal A) A)ˣ
```

**`Dualizing.IsNormalizedDualizingComplex.nonempty_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedUniqueness.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedUniqueness.lean#L108). The attribute's comment: “a normalized dualizing complex is unique up to isomorphism; stated at the ring's own module universe”.

> **A normalized dualizing complex over a Noetherian local ring is unique up to isomorphism.**
> Two dualizing complexes differ by derived tensor product with an invertible object
> ([Stacks, Tag 0A7F]); over a local ring such an object is the ring placed in a single degree
> ([Stacks, Tag 0FNT]), so the two complexes differ by a shift; and the normalization convention of
> [Stacks, Tag 0A7M] admits exactly one normalizing shift, so that shift is zero.
>
> This is the uniqueness half of the comparison made in [Stacks, Tag 0A83], whose other side —
> uniqueness of an injective hull of the residue field — is [Stacks, Tag 08Y4].

```lean
public theorem IsNormalizedDualizingComplex.nonempty_iso
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {ω ω' : DerivedCategory (ModuleCat.{u} A)}
    (hω : IsNormalizedDualizingComplex.{u, u} ω)
    (hω' : IsNormalizedDualizingComplex.{u, u} ω') :
    Nonempty (ω ≅ ω')
```

**`Dualizing.IsDualizingComplex.autMulEquivUnits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/NormalizedUniqueness.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/NormalizedUniqueness.lean#L173). The attribute's comment: “the automorphism group of a dualizing complex is the group of units of the base ring; proved for every dualizing complex, not only a normalized one, and stated at the ring's own module universe”.

> **The automorphism group of a dualizing complex is the unit group of the base ring.** Reading
> off the units of `Dualizing.IsDualizingComplex.endAlgEquiv`: an automorphism of `ω` in `D(A)` is
> multiplication by a unique unit of `A`.
>
> This is the automorphism-group half of the comparison made in [Stacks, Tag 0A83]. The source
> states it for a normalized dualizing complex over a Noetherian local ring; no normalization and
> no local hypothesis are needed, so the statement here is more general. The other side of the
> comparison is `Dualizing.LocalDuality.injectiveHullUnitsMulEquivUnitsAdicCompletion`, where the
> automorphism group is instead the units of the `𝔪`-adic completion.

```lean
public def IsDualizingComplex.autMulEquivUnits
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {ω : DerivedCategory (ModuleCat.{u} A)} (hω : IsDualizingComplex ω) :
    Aut ω ≃* Aˣ
```

Declarations registered for the tag:

- [`exists_isInjectiveHull_homology_zero_localCohomology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_isInjectiveHull_homology_zero_localCohomology#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L109) (StacksFrontier): “the opening sentence, that `RΓ_Z(ω)` is an injective hull of the residue field: the hull half, read from Stacks 0A82”.
- [`nonempty_localCohomology_iso_single_homology_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=nonempty_localCohomology_iso_single_homology_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L113) (StacksFrontier): “the opening sentence, that `RΓ_Z(ω)` is an injective hull of the residue field placed in degree zero: the concentration half, read from Stacks 0A82”.
- [`Module.exists_iso_of_isInjectiveHull`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L210), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L117) (StacksFrontier): “an injective hull of the residue field is unique up to isomorphism; proved for an arbitrary object of an arbitrary abelian category, which is Stacks 08Y4”.

## Tag 0A84, a theorem

[Tag 0A84](https://stacks.math.columbia.edu/tag/0A84) in the Stacks Project.

**`Dualizing.LocalDuality.nonempty_derivedCompletion_derivedHom_iso_derivedHom_injectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L145).

> The local duality theorem. Let `(A, 𝔪, κ)` be a Noetherian local ring, let `ω` be a
> normalized dualizing complex, let `i : κ ⟶ E` be an injective hull of the residue field, and let
> `Z = V(𝔪)`. Then derived `𝔪`-adic completion of `RHom_A(K, ω)` is `RHom_A(RΓ_Z(K), E[0])`, for
> every `K` in `D(A)`.

```lean
public theorem nonempty_derivedCompletion_derivedHom_iso_derivedHom_injectiveHull
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = IsLocalRing.maximalIdeal A)
    (ω : DerivedCategory (ModuleCat.{u} A))
    (hω : IsNormalizedDualizingComplex.{u, u} ω)
    {E : ModuleCat.{u} A}
    (i : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono i] (hi : Module.IsInjectiveHull i)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    Nonempty
      ((DerivedCompletion.derivedCompletionFunctor A f).obj
          ((derivedHomAdjunction (R := A)).hom.obj (Opposite.op K, ω)) ≅
        (derivedHomAdjunction (R := A)).hom.obj
          (Opposite.op ((derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).ι.obj
            ((localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
              (IsNoetherian.noetherian _)).obj K)),
            (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj E))
```

**`Dualizing.LocalDuality.nonempty_localDualityNatIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDuality.lean#L180). The attribute's comment: “natural in K”.

> The local duality theorem, natural in `K`. Let `(A, 𝔪, κ)` be a Noetherian local ring, let
> `ω` be a normalized dualizing complex, let `i : κ ⟶ E` be an injective hull of the residue
> field, and let `Z = V(𝔪)`. Then derived `𝔪`-adic completion of `RHom_A(-, ω)` is
> `RHom_A(RΓ_Z(-), E[0])`, as an isomorphism of contravariant functors on `D(A)`.

```lean
public theorem nonempty_localDualityNatIso
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = IsLocalRing.maximalIdeal A)
    (ω : DerivedCategory (ModuleCat.{u} A))
    (hω : IsNormalizedDualizingComplex.{u, u} ω)
    {E : ModuleCat.{u} A}
    (i : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono i] (hi : Module.IsInjectiveHull i) :
    Nonempty (Dualizing.derivedHomInto A ω ⋙ DerivedCompletion.derivedCompletionFunctor A f ≅
      (Stacks.LocalCohomology.CechFormula.localCohomologyEndofunctor A
          (IsLocalRing.maximalIdeal A) (IsNoetherian.noetherian _)).op ⋙
        Dualizing.derivedHomInto A
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj E))
```

## Tag 0AAK, a lemma

[Tag 0AAK](https://stacks.math.columbia.edu/tag/0AAK) in the Stacks Project.

**`Dualizing.LocalDuality.nonempty_adicCompletion_ext_linearEquiv_linearMap_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDualityExt.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDualityExt.lean#L771). References: SGA 2 V (2.1), “Ext^{-i}≅Hom(H^i,E)”.

> Let `(A, 𝔪, κ)` be a Noetherian local ring, let `ω` be a normalized dualizing complex, let
> `ι : κ ⟶ E` be an injective hull of the residue field, and let `K` be an object of `D_Coh(A)`,
> that is, a complex all of whose cohomology modules are finite. Then the `𝔪`-adic completion of
> `Ext^{-i}_A(K, ω)` is isomorphic to the module of `A`-linear maps from `H^i_𝔪(K)` to `E`.
> Local cohomology is `RΓ_Z` for `Z = V(𝔪)`, and `Ext^{-i}_A(K, ω)` is `Hom_{D(A)}(K, ω⟦-i⟧)`.

```lean
public theorem nonempty_adicCompletion_ext_linearEquiv_linearMap_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {r : ℕ} (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = IsLocalRing.maximalIdeal A)
    (ω : DerivedCategory (ModuleCat.{u} A))
    (hω : IsNormalizedDualizingComplex.{u, u} ω)
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : ∀ j : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) j).obj K))
    {E : ModuleCat.{u} A}
    (ι : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono ι] (hι : Module.IsInjectiveHull ι) (i : ℤ) :
    Nonempty
      (AdicCompletion (IsLocalRing.maximalIdeal A)
          (DerivedCategory.Ext K ω (-i)) ≃ₗ[A]
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
            ((derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
                (IsNoetherian.noetherian _)).ι.obj
              ((localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
                (IsNoetherian.noetherian _)).obj K)) →ₗ[A] E))
```

**`Dualizing.LocalDuality.exists_localDualityExtNatEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDualityExt.lean, line 878](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/LocalDualityExt.lean#L878). The attribute's comment: “natural in K”.

> Let `(A, 𝔪, κ)` be a Noetherian local ring, let `ω` be a normalized dualizing complex, let
> `ι : κ ⟶ E` be an injective hull of the residue field, and let `Z = V(𝔪)`. For every integer
> `i` there is a family of `A`-linear isomorphisms
>
> `H^0(RHom_A(K, ω⟦-i⟧)^∧) ≅ Hom_A(H^i_Z(K), E)`
>
> indexed by the objects `K` of `D(A)`, compatible with the maps induced by every morphism of
> `D(A)`: local duality in its module form, natural in `K`.
>
> The left-hand side is the degree-zero cohomology of the derived `𝔪`-adic completion of
> `RHom_A(K, ω⟦-i⟧)`, whose degree-zero cohomology is `Ext^{-i}_A(K, ω)`; the right-hand side is
> the Matlis dual of the degree-`i` local cohomology module.

```lean
public theorem exists_localDualityExtNatEquiv
    [IsNoetherianRing A] [IsLocalRing A]
    {r : ℕ} (f : Fin r → A) (hf : Ideal.span (Set.range f) = IsLocalRing.maximalIdeal A)
    (ω : DerivedCategory (ModuleCat.{u} A))
    (hω : IsNormalizedDualizingComplex.{u, u} ω)
    {E : ModuleCat.{u} A}
    (ι : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono ι] (hι : Module.IsInjectiveHull ι) (i : ℤ) :
    ∃ θ : ∀ K : DerivedCategory (ModuleCat.{u} A),
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((DerivedCompletion.derivedCompletionFunctor A f).obj
              ((StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
                (Opposite.op K,
                  (CategoryTheory.shiftFunctor
                    (DerivedCategory (ModuleCat.{u} A)) (-i)).obj ω))) : Type u) ≃ₗ[A]
          (((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
              ((localCohomologyEndofunctor A (IsLocalRing.maximalIdeal A)
                (IsNoetherian.noetherian _)).obj K) : Type u) →ₗ[A] (E : Type u)),
      ∀ (K K' : DerivedCategory (ModuleCat.{u} A)) (g : K' ⟶ K)
        (x : ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
          ((DerivedCompletion.derivedCompletionFunctor A f).obj
            ((StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
              (Opposite.op K,
                (CategoryTheory.shiftFunctor
                  (DerivedCategory (ModuleCat.{u} A)) (-i)).obj ω))) : Type u)),
        θ K' (((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
              ((DerivedCompletion.derivedCompletionFunctor A f).map
                ((StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.map
                  (show (Opposite.op K, (CategoryTheory.shiftFunctor
                        (DerivedCategory (ModuleCat.{u} A)) (-i)).obj ω) ⟶
                      (Opposite.op K', (CategoryTheory.shiftFunctor
                        (DerivedCategory (ModuleCat.{u} A)) (-i)).obj ω) from
                    (g.op, 𝟙 _))))).hom x) =
          (θ K x).comp
            ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
              ((localCohomologyEndofunctor A (IsLocalRing.maximalIdeal A)
                (IsNoetherian.noetherian _)).map g)).hom
```

**`Stacks.LocalCohomology.nonempty_adicCompletion_ext_linearEquiv_matlisDual_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean#L339). The attribute's comment: “the module form, with the support-closed-subset model of local cohomology in place of the torsion-complex model”.

> **Stacks Project, Tag 0AAK** in the spelling of local cohomology with support in `V(𝔪)`.
> Over a Noetherian local ring with a normalized dualizing complex, the `𝔪`-adic completion of
> `Ext^{-i}(K, ω)` is the Matlis dual of `H^i_{V(𝔪)}(K)`.

```lean
theorem nonempty_adicCompletion_ext_linearEquiv_matlisDual_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K ω : DerivedCategory (ModuleCat.{u} A))
    (hK : ∀ j : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) j).obj K))
    (hω : Dualizing.IsNormalizedDualizingComplex ω)
    (E : ModuleCat.{u} A)
    (e : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono e] (he : Module.IsInjectiveHull e) (i : ℤ) :
    Nonempty
      (AdicCompletion (maximalIdeal A) (DerivedCategory.Ext K ω (-i)) ≃ₗ[A]
        (localCohomologyWithSupportIn
          A (PrimeSpectrum.zeroLocus (maximalIdeal A : Set A)) K i →ₗ[A] E))
```

**`Stacks.LocalCohomology.nonempty_adicCompletion_ext_linearEquiv_matlisDual_localCohomologyPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean#L377). The attribute's comment: “the module form for a bounded-below complex, with the support-closed-subset model of local cohomology”.

> **Stacks Project, Tag 0AAK** for a bounded-below complex.

```lean
theorem nonempty_adicCompletion_ext_linearEquiv_matlisDual_localCohomologyPlus
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory.Plus (ModuleCat.{u} A))
    (ω : DerivedCategory (ModuleCat.{u} A))
    (hK : ∀ j : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{u} A) j).obj K))
    (hω : Dualizing.IsNormalizedDualizingComplex ω)
    (E : ModuleCat.{u} A)
    (e : (ModuleCat.uliftFunctor.{u} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono e] (he : Module.IsInjectiveHull e) (i : ℤ) :
    Nonempty
      (AdicCompletion (maximalIdeal A) (DerivedCategory.Ext K.obj ω (-i)) ≃ₗ[A]
        (localCohomologyWithSupportInPlus
          A (PrimeSpectrum.zeroLocus (maximalIdeal A : Set A)) K i →ₗ[A] E))
```

**`Stacks.LocalCohomology.nonempty_adicCompletion_localizedDualCohomology_linearEquiv_matlisDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/LocalDuality.lean#L726). The attribute's comment: “local duality at an arbitrary prime of a Noetherian ring with a dualizing complex, reached from the local case through the normalizing shift of 0A7Z and flat base change of Ext; objectwise, with no naturality in the complex”.

> **Local duality at an arbitrary prime.** Let `A` be Noetherian with dualizing complex `ω`
> and dimension function `δ`, let `q` be a prime, and let `E` be an injective hull of the residue
> field of `A_q`. For `K` in `D⁺_{Coh}(A)` and `n + i = -δ(q)`, the `qA_q`-adic completion of
> `H^n(RHom_A(K, ω))_q` is the Matlis dual of `H^i_{qA_q}(K_q)`.
>
> This is [Stacks, Tag 0AAK] at a general prime: the localization `ω_q⟦-δ(q)⟧` is a normalized
> dualizing complex over `A_q` by [Stacks, Tag 0A7Z], and flat base change identifies
> `H^n(RHom_A(K, ω))_q` with `Ext^n_{A_q}(K_q, ω_q)`. It is the local-duality input to the proof
> of [Stacks, Tag 0EFX]. The two sides are isomorphic as `A_q`-modules for each `K` separately;
> no naturality in `K` is claimed, and 0AAK provides none.

```lean
theorem nonempty_adicCompletion_localizedDualCohomology_linearEquiv_matlisDual
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (q : PrimeSpectrum A) (K : DerivedCategory.Plus (ModuleCat.{u} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{u} A) i).obj K))
    (ω : DerivedCategory (ModuleCat.{u} A)) (hω : Dualizing.IsDualizingComplex ω)
    (E : ModuleCat.{u} (Localization.AtPrime q.asIdeal))
    (e : (ModuleCat.uliftFunctor.{u} (Localization.AtPrime q.asIdeal)).obj
      (ModuleCat.of (Localization.AtPrime q.asIdeal)
        (ResidueField (Localization.AtPrime q.asIdeal))) ⟶ E)
    [Mono e] (he : Module.IsInjectiveHull e)
    (n i : ℤ) (hni : n + i = -Dualizing.dualizingDimension ω q) :
    Nonempty
      (AdicCompletion (maximalIdeal (Localization.AtPrime q.asIdeal))
          (LocalizedModule q.asIdeal.primeCompl
            ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj
              ((Dualizing.dualizingDerivedHomFunctor.{u, u} A ω).obj (.op K.obj))))
          ≃ₗ[Localization.AtPrime q.asIdeal]
        (localCohomologyWithSupportInPlus (Localization.AtPrime q.asIdeal)
          (PrimeSpectrum.zeroLocus (maximalIdeal (Localization.AtPrime q.asIdeal) : Set _))
          (localizedComplex.{u, u} q K) i →ₗ[Localization.AtPrime q.asIdeal] E))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.18, Tag 0A81](https://stacks.math.columbia.edu/tag/0A81)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
