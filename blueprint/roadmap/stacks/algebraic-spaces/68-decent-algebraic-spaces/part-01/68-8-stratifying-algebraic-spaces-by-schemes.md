---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_closedChain_isFiniteLocallyFreeOfRank, AlgebraicGeometry.Space.exists_antitone_isOpenSubspace_iff_fibre_degree_ge, AlgebraicGeometry.Space.exists_schemeStratification_quasiCompactPoint_mem_stratum, AlgebraicGeometry.Space.exists_finiteFiltration_of_isReasonableSpace, AlgebraicGeometry.Space.exists_finiteFiltration_isRepresentable_strata, AlgebraicGeometry.Space.exists_finiteFiltration_of_isQuasiCompactSpace, AlgebraicGeometry.Space.isEtaleLocallyConstructible_iff_isLocallyConstructible
statement: formalized
proof: formalized
---

# 68.8 Stratifying algebraic spaces by schemes

Section 68.8 of the Stacks Project, [Tag 0A4I](https://stacks.math.columbia.edu/tag/0A4I). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07S8, a lemma

[Tag 07S8](https://stacks.math.columbia.edu/tag/07S8) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_closedChain_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreDegreeClosedStratification.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreDegreeClosedStratification.lean#L138).

> **Stacks Project, Tag 07S8.** A flat, locally finitely presented, separated, locally
> quasi-finite morphism from a scheme to an algebraic space with universally bounded fibres induces
> a finite increasing chain of closed subsets of the point set, from `∅` to the whole point set,
> whose strata are the loci over which the base change of the morphism is finite locally free of a
> fixed degree.

```lean
theorem exists_closedChain_isFiniteLocallyFreeOfRank
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (W : BigFppfOver B S hS)
    (g : yoneda.obj W ⟶ X) (hX : IsAlgebraicSpace B S hS X)
    (hflat : IsFlat B S hS g) (hlfp : IsLocallyOfFinitePresentation B S hS g)
    (hsep : IsSeparated B S hS g) (hlqf : IsLocallyQuasiFinite B S hS g)
    (hbound : HasUniversallyBoundedFibers B S hS W g) :
    ∃ (n : ℕ) (Z : ℕ → Set (points B S hS X)), Z 0 = ∅ ∧ (∀ r, IsClosed (Z r)) ∧ Monotone Z ∧
      Z (n + 1) = Set.univ ∧
      ∀ r : ℕ, r ≤ n → ∀ (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hm : T ⟶ X),
        IsAlgebraicSpace B S hS T →
        ∀ (Pp : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (pr₁ : Pp ⟶ yoneda.obj W) (pr₂ : Pp ⟶ T),
          IsPullback pr₁ pr₂ g hm →
          ((MorphismProperty.inverseImage (IsFiniteLocallyFreeOfRank.property.{u} r)
              (BigFppfOver.toScheme B S hS)).presheaf pr₂ ↔
            Set.range (pointsMap B S hS T hm) ⊆ Z (r + 1) \ Z r)
```

## Tag 086T, a lemma

[Tag 086T](https://stacks.math.columbia.edu/tag/086T) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_antitone_isOpenSubspace_iff_fibre_degree_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreDegreeStratification.lean, line 982](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreDegreeStratification.lean#L982).

> Let `X` be an algebraic space over a scheme `S` and let `f : yoneda.obj W ⟶ X` be a morphism
> from a scheme which is flat, locally of finite presentation, separated and locally quasi-finite.
> Then there is a descending chain of open subspaces
> `X = X₀ ⊇ X₁ ⊇ X₂ ⊇ …`
> such that a field-valued point of `X` factors through `Xᵈ` exactly when the fibre of `f`
> above it has degree at least `d`; a fibre which is not finite counts as having infinite
> degree.

```lean
theorem exists_antitone_isOpenSubspace_iff_fibre_degree_ge
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    {W : BigFppfOver B S hS} (f : yoneda.obj W ⟶ X)
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hsep : IsSeparated B S hS f) (hlqf : IsLocallyQuasiFinite B S hS f) :
    ∃ Y : ℕ → Subfunctor X,
      Y 0 = ⊤ ∧ Antitone Y ∧ (∀ d, IsOpenSubspace B S hS (Y d)) ∧
      ∀ (d : ℕ) (p : FieldValuedPoint B S hS X),
        (∃ g : yoneda.obj p.siteObject ⟶ (Y d).toFunctor,
            g ≫ (Y d).ι = yonedaEquiv.symm p.value) ↔
          (¬ (MorphismProperty.inverseImage (@_root_.AlgebraicGeometry.IsFinite.{u})
                (BigFppfOver.toScheme B S hS)).presheaf
                (pullback.fst (yonedaEquiv.symm p.value) f) ∨
            ∃ r : ℕ, d ≤ r ∧
              (MorphismProperty.inverseImage (IsFiniteLocallyFreeOfRank.property.{u} r)
                (BigFppfOver.toScheme B S hS)).presheaf
                (pullback.fst (yonedaEquiv.symm p.value) f))
```

## Tag 0BBN, a lemma

[Tag 0BBN](https://stacks.math.columbia.edu/tag/0BBN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_schemeStratification_quasiCompactPoint_mem_stratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean#L298).

> A quasi-compact algebraic space `X` over `S` carries a descending
> chain of open subspaces starting at `X` whose reduced strata, the differences of
> consecutive members, each receive an isomorphism from the part lying over them of a
> separated scheme surjective and étale over the corresponding member; and every point of
> `|X|` represented by a quasi-compact morphism from the spectrum of a field lies in one of
> those strata.

```lean
public theorem exists_schemeStratification_quasiCompactPoint_mem_stratum
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hqc : AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS X) :
    ∃ strat : AlgebraicGeometry.Space.SchemeStratification B S hS X,
      ∀ (x : AlgebraicGeometry.Space.points B S hS X)
        (z : AlgebraicGeometry.Space.FieldValuedPoint B S hS X),
        z.class B S hS X = x →
        AlgebraicGeometry.Space.IsQuasiCompact B S hS
          (AlgebraicGeometry.Space.fieldMorphism B S hS X z) →
        ∃ p : ℕ, x ∈ Set.range (AlgebraicGeometry.Space.pointsMap B S hS
          (strat.stratum p).toFunctor ((strat.stratum p).ι ≫ (strat.openPart p).ι))
```

## Tag 07S9, a lemma

[Tag 07S9](https://stacks.math.columbia.edu/tag/07S9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteFiltration_of_isReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean#L474).

> A quasi-compact reasonable algebraic space has a finite filtration by open
> subspaces such that every reduced stratum has a separated scheme as an étale
> neighborhood, isomorphic above the stratum.

```lean
public theorem exists_finiteFiltration_of_isReasonableSpace
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hqc : AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS X)
    (hr : AlgebraicGeometry.Space.IsReasonableSpace B S hS X) :
    ∃ (n : ℕ) (U : ℕ → Subfunctor X),
      0 < n ∧
      U 0 = ⊤ ∧
      U n = (⊥ : Subfunctor X).sheafify
        (AlgebraicGeometry.BigFppfOver.topology B S hS) ∧
      (∀ p ≤ n, AlgebraicGeometry.Space.IsOpenSubspace B S hS (U p)) ∧
      (∀ p < n, U (p + 1) ≤ U p) ∧
      ∃ (T : (p : Fin n) → Subfunctor (U p.val).toFunctor)
        (V : Fin n → AlgebraicGeometry.BigFppfOver B S hS)
        (f : ∀ p : Fin n, yoneda.obj (V p) ⟶ (U p.val).toFunctor),
        ∀ p : Fin n,
          (AlgebraicGeometry.Space.IsClosedSubspace B S hS (T p)) ∧
          (Set.range (AlgebraicGeometry.Space.pointsMap B S hS (T p).toFunctor
            ((T p).ι ≫ (U p.val).ι)) =
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U p.val).toFunctor
                (U p.val).ι) \
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U (p.val + 1)).toFunctor
                (U (p.val + 1)).ι)) ∧
          (AlgebraicGeometry.Space.HasEtaleLocalProperty B S hS (T p).toFunctor
            (fun Y : Scheme.{u} => IsReduced Y)) ∧
          Scheme.IsSeparated ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).obj (V p)) ∧
          (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf (f p) ∧
          AlgebraicGeometry.Space.IsEtale B S hS (f p) ∧
          IsIso (pullback.fst (T p).ι (f p))
```

## Tag 07SA, a lemma

[Tag 07SA](https://stacks.math.columbia.edu/tag/07SA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteFiltration_isRepresentable_strata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean#L519).

> A quasi-compact reasonable algebraic space has a finite filtration by open
> subspaces whose reduced strata are schemes.

```lean
public theorem exists_finiteFiltration_isRepresentable_strata
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hqc : AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS X)
    (hr : AlgebraicGeometry.Space.IsReasonableSpace B S hS X) :
    ∃ (n : ℕ) (U : ℕ → Subfunctor X),
      0 < n ∧
      U 0 = ⊤ ∧
      U n = (⊥ : Subfunctor X).sheafify
        (AlgebraicGeometry.BigFppfOver.topology B S hS) ∧
      (∀ p ≤ n, AlgebraicGeometry.Space.IsOpenSubspace B S hS (U p)) ∧
      (∀ p < n, U (p + 1) ≤ U p) ∧
      ∃ T : (p : Fin n) → Subfunctor (U p.val).toFunctor,
        ∀ p : Fin n,
          (AlgebraicGeometry.Space.IsClosedSubspace B S hS (T p)) ∧
          (Set.range (AlgebraicGeometry.Space.pointsMap B S hS (T p).toFunctor
            ((T p).ι ≫ (U p.val).ι)) =
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U p.val).toFunctor
                (U p.val).ι) \
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U (p.val + 1)).toFunctor
                (U (p.val + 1)).ι)) ∧
          (AlgebraicGeometry.Space.HasEtaleLocalProperty B S hS (T p).toFunctor
            (fun Y : Scheme.{u} => IsReduced Y)) ∧
          (T p).toFunctor.IsRepresentable
```

## Tag 07ST, a lemma

[Tag 07ST](https://stacks.math.columbia.edu/tag/07ST) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteFiltration_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteSchemeFiltration/Strata.lean#L420).

> A quasi-compact quasi-separated algebraic space has a finite filtration
> by open subspaces such that every reduced stratum has a quasi-compact
> separated scheme as an étale neighborhood, isomorphic above the stratum.

```lean
public theorem exists_finiteFiltration_of_isQuasiCompactSpace
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hqc : AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS X)
    (hqs : AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated B S hS hZ X) :
    ∃ (n : ℕ) (U : ℕ → Subfunctor X),
      0 < n ∧
      U 0 = ⊤ ∧
      U n = (⊥ : Subfunctor X).sheafify
        (AlgebraicGeometry.BigFppfOver.topology B S hS) ∧
      (∀ p ≤ n, AlgebraicGeometry.Space.IsOpenSubspace B S hS (U p)) ∧
      (∀ p < n, U (p + 1) ≤ U p) ∧
      ∃ (T : (p : Fin n) → Subfunctor (U p.val).toFunctor)
        (V : Fin n → AlgebraicGeometry.BigFppfOver B S hS)
        (f : ∀ p : Fin n, yoneda.obj (V p) ⟶ (U p.val).toFunctor),
        ∀ p : Fin n,
          (AlgebraicGeometry.Space.IsClosedSubspace B S hS (T p)) ∧
          (Set.range (AlgebraicGeometry.Space.pointsMap B S hS (T p).toFunctor
            ((T p).ι ≫ (U p.val).ι)) =
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U p.val).toFunctor
                (U p.val).ι) \
              Set.range (AlgebraicGeometry.Space.pointsMap B S hS (U (p.val + 1)).toFunctor
                (U (p.val + 1)).ι)) ∧
          (AlgebraicGeometry.Space.HasEtaleLocalProperty B S hS (T p).toFunctor
            (fun Y : Scheme.{u} => IsReduced Y)) ∧
          CompactSpace ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).obj (V p)) ∧
          Scheme.IsSeparated ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).obj (V p)) ∧
          (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf (f p) ∧
          AlgebraicGeometry.Space.IsEtale B S hS (f p) ∧
          IsIso (pullback.fst (T p).ι (f p))
```

## Tag 0ECZ, a lemma

[Tag 0ECZ](https://stacks.math.columbia.edu/tag/0ECZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_iff_isLocallyConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePointsQuasiSeparated.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePointsQuasiSeparated.lean#L290).

> **Stacks 0ECZ.** A subset of the point space of a quasi-separated algebraic space over `S`
> is étale locally constructible exactly when it is locally constructible.

```lean
theorem isEtaleLocallyConstructible_iff_isLocallyConstructible
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X)
    (E : Set (points B S hS X)) :
    IsEtaleLocallyConstructible B S hS X E ↔ IsLocallyConstructible E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.8, Tag 0A4I](https://stacks.math.columbia.edu/tag/0A4I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
