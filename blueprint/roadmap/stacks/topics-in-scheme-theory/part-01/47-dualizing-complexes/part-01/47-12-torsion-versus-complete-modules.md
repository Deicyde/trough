---
declaration: section
origin: cited
lean: Dualizing.isIso_derivedCompletion_map_localCohomologyCounit, Dualizing.isIso_localCohomology_map_derivedCompletionUnit, Dualizing.torsionCompleteEquivalence, Dualizing.derivedHomCompletionTorsionIso, Dualizing.derivedCompletionDerivedHomTorsionNatIso, Stacks.Algebraization.isDerivedLimitWithProjections_completedLocalCohomologyNormalizedProjection_of_finite, Dualizing.exists_isDerivedLimit_adicQuotientLocalCohomologySystem, Dualizing.exists_milnor_shortExact_of_isDerivedLimit
statement: formalized
proof: formalized
---

# 47.12 Torsion versus complete modules

Section 47.12 of the Stacks Project, [Tag 0A6V](https://stacks.math.columbia.edu/tag/0A6V). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A6W, a lemma

[Tag 0A6W](https://stacks.math.columbia.edu/tag/0A6W) in the Stacks Project.

**`Dualizing.isIso_derivedCompletion_map_localCohomologyCounit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletionAfterLocalCohomology.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletionAfterLocalCohomology.lean#L184). The attribute's comment: “completion\_after\_local”.

> **Stacks 0A6W, completion after local cohomology.** For a finitely generated ideal `I` of a
> commutative ring `A` and `Z = V(I)`, the counit `RΓ_Z(K) ⟶ K` of the adjunction defining local
> cohomology becomes an isomorphism after derived `I`-completion; equivalently
> `RΓ_Z(K)^∧ = K^∧` in `D(A)`, naturally in `K`.
>
> The statement holds for every reflection `C` of `D(A)` onto the derived `I`-complete objects, so
> it is independent of the chosen model of derived completion.

```lean
theorem isIso_derivedCompletion_map_localCohomologyCounit
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (C : DerivedCategory (ModuleCat.{v} A) ⥤ DerivedCompleteDerivedCategory A I)
    (hC : C ⊣ (derivedCompleteProperty A I).ι) (K : DerivedCategory (ModuleCat.{v} A)) :
    IsIso ((C ⋙ (derivedCompleteProperty A I).ι).map
      ((localCohomologyAdjunction A I hI).counit.app K))
```

**`Dualizing.isIso_localCohomology_map_derivedCompletionUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/LocalCohomologyAfterCompletion.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/LocalCohomologyAfterCompletion.lean#L330). The attribute's comment: “local\_after\_completion”.

> **Stacks 0A6W, local cohomology after completion.** For a finitely generated ideal
> `I = (f₁, …, f_r)` of a commutative ring `A` and `Z = V(I)`, the derived-completion unit
> `K ⟶ K^∧` induces an isomorphism `RΓ_Z(K) ⟶ RΓ_Z(K^∧)` in `D(A)`, naturally in `K`.

```lean
theorem isIso_localCohomology_map_derivedCompletionUnit (I : Ideal A) (hI : I.FG)
    (f : Fin r → A) (hf : Ideal.span (Set.range f) = I)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    IsIso (((localCohomologyRightAdjoint A I hI).1 ⋙
      (derivedPowerTorsionProperty A I hI).ι).map
        ((DerivedCompletion.derivedCompletionUnit A f).app K))
```

## Tag 0A6X, a proposition

[Tag 0A6X](https://stacks.math.columbia.edu/tag/0A6X) in the Stacks Project.

**`Dualizing.torsionCompleteEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/Equivalence.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/Equivalence.lean#L291).

> **Stacks 0A6X.** For a finitely generated ideal `I` of a commutative ring `A` and `Z = V(I)`,
> derived `I`-completion and local cohomology with support in `Z` are quasi-inverse equivalences
> between the full subcategory of `D(A)` of complexes with `I`-power-torsion cohomology and the
> full subcategory of derived `I`-complete complexes. The two functors of the equivalence are
> identified with derived completion and local cohomology by natural isomorphisms, not merely
> objectwise.

```lean
def torsionCompleteEquivalence (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    Σ E : PowerTorsionDerivedCategory.{u, v} A I hI ≌ DerivedCompleteDerivedCategory A I,
      (E.functor ≅ ((derivedPowerTorsionProperty A I hI).ι ⋙ derivedCompletion A I hI)) ×
      (E.inverse ≅ ((derivedCompleteProperty A I).ι ⋙ localCohomologyFunctor A I hI))
```

## Tag 0A6Y, a lemma

[Tag 0A6Y](https://stacks.math.columbia.edu/tag/0A6Y) in the Stacks Project.

**`Dualizing.derivedHomCompletionTorsionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/DerivedHomCompletionTorsion.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/DerivedHomCompletionTorsion.lean#L435).

> For `A` a commutative ring, `I` a finitely generated ideal, `Z = V(I)`, `(-)^∧` derived
> `I`-adic completion and `RΓ_Z` local cohomology, the canonical isomorphism
> `RHom_A(K^∧, L^∧) ≅ RHom_A(RΓ_Z(K), RΓ_Z(L))` in `D(A)`.

```lean
def derivedHomCompletionTorsionIso (I : Ideal A) (hI : I.FG) (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = I) (K L : DerivedCategory (ModuleCat.{u} A)) :
    (StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
        (Opposite.op ((DerivedCompletion.derivedCompletionFunctor A f).obj K),
          (DerivedCompletion.derivedCompletionFunctor A f).obj L) ≅
      (StacksDraft.DerivedHom.derivedHomAdjunction (R := A)).hom.obj
        (Opposite.op ((localCohomologyEndofunctor A I hI).obj K),
          (localCohomologyEndofunctor A I hI).obj L)
```

**`Dualizing.derivedCompletionDerivedHomTorsionNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/DerivedHomCompletionTorsion.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/DerivedHomCompletionTorsion.lean#L592). The attribute's comment: “natural in the source object”.

> For a finite family `f` generating an ideal `I` of a commutative ring `A`, with `Z = V(I)`,
> there is an isomorphism `RHom_A(-, L)^∧ ≅ RHom_A(RΓ_Z(-), RΓ_Z(L))` of contravariant functors
> on `D(A)`.

```lean
def derivedCompletionDerivedHomTorsionNatIso (I : Ideal A) (hI : I.FG) (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = I) (L : DerivedCategory (ModuleCat.{u} A)) :
    derivedHomInto A L ⋙ DerivedCompletion.derivedCompletionFunctor A f ≅
      (localCohomologyEndofunctor A I hI).op ⋙
        derivedHomInto A ((localCohomologyEndofunctor A I hI).obj L)
```

## Tag 0EEW, a lemma

[Tag 0EEW](https://stacks.math.columbia.edu/tag/0EEW) in the Stacks Project.

**`Stacks.Algebraization.isDerivedLimitWithProjections_completedLocalCohomologyNormalizedProjection_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionUnitLocalCohomology/NormalizedProjections.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionUnitLocalCohomology/NormalizedProjections.lean#L241). The attribute's comment: “part (1) for the projections normalized against the completion unit”.

> **Stacks 0EEW, part (1), for the projections normalized against the completion unit.** For a
> finite module over a Noetherian ring, `RΓ_{V(J)}(M)^∧` is a derived limit of the tower
> `n ↦ RΓ_{V(J)}(M/IⁿM)` *with the normalized projections* — the cone whose composites with the
> completion unit are the maps induced by `M ↠ M/IⁿM`.
>
> `Stacks.Algebraization.isDerivedLimitWithProjections_completedLocalCohomologyNormalizedProjection`
> reduces this to exhibiting *one* unit-normalized derived-limit cone, and
> `Dualizing.exists_isDerivedLimitWithProjections_of_uliftAdicQuotientIso` is one: Stacks 0922
> supplies a reflection onto the derived `I`-complete objects whose unit induces the reduction maps
> of the tower `n ↦ K ⊗ᴸ A/Iⁿ`, the comparison with the tower of ordinary quotients is normalized,
> and two reflections onto the same subcategory agree compatibly with their units, so the cone
> transports to the reflection `adicCompletionFunctor`.

```lean
theorem isDerivedLimitWithProjections_completedLocalCohomologyNormalizedProjection_of_finite
    [IsNoetherianRing A] (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (M : ModuleCat.{u} A)
    [Module.Finite A M] :
    NoetherianAdicCompletion.IsDerivedLimitWithProjections
      (Dualizing.adicQuotientLocalCohomologySystem A I J hJ M)
      ((adicCompletionFunctor A I hI).obj
        ((Dualizing.localCohomologyFunctor A J hJ).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M)).obj)
      (completedLocalCohomologyNormalizedProjection I J hI hJ M)
```

**`Dualizing.exists_isDerivedLimit_adicQuotientLocalCohomologySystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean#L131). The attribute's comment: “the tower of local cohomologies has a derived limit”.

> The tower `n ↦ RΓ_Z(M/IⁿM)` has a derived limit: countable products exist in `D(A)`, so the
> difference map `1 - shift` on the product of the terms sits in a distinguished triangle.

```lean
theorem exists_isDerivedLimit_adicQuotientLocalCohomologySystem (I J : Ideal A) (hJ : J.FG)
    (M : ModuleCat.{u} A) :
    ∃ K : DerivedCategory (ModuleCat.{u} A),
      IsDerivedLimit (adicQuotientLocalCohomologySystem A I J hJ M) K
```

**`Dualizing.exists_milnor_shortExact_of_isDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean#L174). The attribute's comment: “the Milnor short exact sequence for the tower”.

> **Stacks 0EEW, part (2), for an arbitrary derived limit of the tower.** The cohomology of a
> derived limit of `n ↦ RΓ_Z(M/IⁿM)` sits in a short exact sequence between the first derived
> limit `R¹lim H^{r-1}_Z(M/IⁿM)`, presented as the cokernel of one minus shift, and the inverse
> limit `lim Hʳ_Z(M/IⁿM)`. The inclusion is the connecting morphism of the presenting triangle and
> the projection is characterized by its composites with the limit projections.

```lean
theorem exists_milnor_shortExact_of_isDerivedLimit (I J : Ideal A) (hJ : J.FG)
    (M : ModuleCat.{u} A) (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsDerivedLimit (adicQuotientLocalCohomologySystem A I J hJ M) K) :
    let F := adicQuotientLocalCohomologySystem A I J hJ M
    let X : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (Opposite.op n)
    let d : (∏ᶜ X) ⟶ ∏ᶜ X := Pi.lift fun n : ℕ ↦
      Pi.π X n - Pi.π X (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    ∃ (a : K ⟶ ∏ᶜ X) (b : (∏ᶜ X) ⟶ K⟦(1 : ℤ)⟧),
      let T := Pretriangulated.Triangle.mk a d b
      T ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
        ∀ r : ℤ,
          let H := DerivedCategory.homologyFunctor (ModuleCat.{u} A) r
          let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{u} A) (r - 1)
          let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H
          let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H₁
          let P : ModuleCat.{u} A :=
            ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)
          let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) n -
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) (n + 1) ≫
                shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
          ∃ (e : H₁.obj (∏ᶜ X) ≅ P)
            (i : cokernel δ ⟶ H.obj K) (q : H.obj K ⟶ limit homologySystem)
            (w : i ≫ q = 0),
            e.hom = piComparison H₁ X ∧
              cokernel.π δ ≫ i = e.inv ≫
                DerivedCategory.HomologySequence.δ T (r - 1) r ∧
              (∀ n : ℕ, q ≫ limit.π homologySystem (Opposite.op n) =
                H.map a ≫ H.map (Pi.π X n)) ∧
              (ShortComplex.mk i q w).ShortExact
```

**`Dualizing.isZero_homology_of_isDerivedLimit_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean#L381). The attribute's comment: “vanishing in negative degrees”.

> **Stacks 0EEW, the negative-degree vanishing, for an arbitrary derived limit of the tower.**
> A derived limit of `n ↦ RΓ_Z(M/IⁿM)` has no cohomology in negative degrees.

```lean
theorem isZero_homology_of_isDerivedLimit_of_neg (I J : Ideal A) (hJ : J.FG)
    (M : ModuleCat.{u} A) (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsDerivedLimit (adicQuotientLocalCohomologySystem A I J hJ M) K) (i : ℤ) (hi : i < 0) :
    IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K)
```

**`Dualizing.isDerivedLimit_completedLocalCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyLimit.lean#L421). The attribute's comment: “part (1): the derived I-adic completion of RΓ\_J(M) is R lim RΓ\_J(M/IⁿM)”.

> **Stacks 0EEW, part (1).** The derived `I`-adic completion of `RΓ_Z(M)` is a derived limit
> of the tower `n ↦ RΓ_Z(M/IⁿM)`.
>
> The Čech formula for local cohomology replaces `RΓ_Z` by `C(g) ⊗ᴸ -`, where `C(g)` is the
> extended alternating Čech complex of a finite generating family of `J`. Derived `I`-adic
> completion of `C(g) ⊗ᴸ M` is the derived limit of the tower `n ↦ (C(g) ⊗ᴸ M) ⊗ᴸ A/Iⁿ`
> (Tag 0EET), and associativity of the derived tensor product rewrites that tower as
> `n ↦ C(g) ⊗ᴸ (M ⊗ᴸ A/Iⁿ)`. The comparison with the tower of ordinary quotients
> `n ↦ C(g) ⊗ᴸ (M/IⁿM)` is a pro-isomorphism, because the fibres only carry the Tor modules
> `Torᵢ(M, A/Iⁿ)` and those are pro-zero over a Noetherian ring for a finite module
> (Tag 0911).

```lean
theorem isDerivedLimit_completedLocalCohomology [IsNoetherianRing A]
    (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (M : ModuleCat.{u} A) [Module.Finite A M] :
    IsDerivedLimit (adicQuotientLocalCohomologySystem A I J hJ M)
      (completedLocalCohomology A I J hI hJ M)
```

## Tag 0EEX, a lemma

[Tag 0EEX](https://stacks.math.columbia.edu/tag/0EEX) in the Stacks Project.

**`Dualizing.exists_iso_homology_zero_completedLocalCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyDegreeZero.lean, line 643](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TorsionComplete/CompletedLocalCohomologyDegreeZero.lean#L643).

> **Stacks 0EEX.** Let `I` and `J` be ideals of a Noetherian ring `A` which is `I`-adically
> complete, let `M` be a finite `A`-module and `Z = V(J)`. The degree-zero cohomology of the
> derived `I`-adic completion `RΓ_Z(M)^∧` of local cohomology is the filtered colimit of
> `H⁰_{V(J')}(M)` over the ideals `J' ⊆ J` with `V(J') ∩ V(I) = V(J) ∩ V(I)`.
>
> The colimit is realized as the supremum `P` of the `J'`-power-torsion submodules `Γ_{J'}(M)`
> of `M` (each `H⁰_{V(J')}(M)` is `Γ_{J'}(M)` by
> `Stacks.Duality.supportLocalCohomology_zero_iso_torsion`; the index set is directed and the
> supremum is the union of its terms by `Dualizing.iSup_primaryComponent_eq_supportTraceSubmodule`).
> The isomorphism is the one induced by the comparison of Tag 0EEW with `lim H⁰_Z(M/IⁿM)`:
> composing it with the inclusion into `M` and the projection to `M/IⁿM` gives the `n`-th limit
> projection followed by the canonical map `H⁰_Z(M/IⁿM) ⟶ M/IⁿM`. Tag 0EEW part (1),
> `Dualizing.isDerivedLimit_completedLocalCohomology`, identifies `RΓ_Z(M)^∧` with the derived
> limit of the tower `n ↦ RΓ_Z(M/IⁿM)`.

```lean
theorem exists_iso_homology_zero_completedLocalCohomology [IsNoetherianRing A]
    (I J : Ideal A) [IsAdicComplete I A] (M : ModuleCat.{u} A) [Module.Finite A M]
    (P : Submodule A M)
    (hP : P = ⨆ (J' : Ideal A) (_ : J' ≤ J)
      (_ : PrimeSpectrum.zeroLocus (J' : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
        PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A)),
      Ideal.primaryComponent M J') :
    ∃ e : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
        (completedLocalCohomology A I J I.fg_of_isNoetherianRing J.fg_of_isNoetherianRing M) ≅
          ModuleCat.of A P,
      ∀ n : ℕ, e.hom ≫ ModuleCat.ofHom P.subtype ≫
          ModuleCat.ofHom (I ^ n • (⊤ : Submodule A M)).mkQ =
        completedLocalCohomologyToLimit A I J J.fg_of_isNoetherianRing M _
            (isDerivedLimit_completedLocalCohomology A I J I.fg_of_isNoetherianRing
              J.fg_of_isNoetherianRing M) 0 ≫
          limit.π (adicQuotientLocalCohomologySystem A I J J.fg_of_isNoetherianRing M ⋙
            DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0) (Opposite.op n) ≫
          Stacks.Duality.supportLocalCohomologyToModule.{u, u} A J J.fg_of_isNoetherianRing
            ((adicQuotientModuleSystem A I M).obj
              (Opposite.op n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.12, Tag 0A6V](https://stacks.math.columbia.edu/tag/0A6V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
