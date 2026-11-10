---
declaration: section
origin: cited
lean: AlgebraicGeometry.isGorenstein_Spec_iff, AlgebraicGeometry.IsGorenstein, AlgebraicGeometry.isCohenMacaulay_of_isGorenstein, AlgebraicGeometry.isGorenstein_of_isRegular, Stacks.Duality.isGorenstein_iff_isInvertible_dualizingComplex, Stacks.Duality.isGorenstein_iff_hasInvertibleDualizingModelOn, Stacks.Duality.isGorenstein_iff_isInvertible_dualizingModel, Stacks.Duality.exists_isOpen_isGorenstein
statement: formalized
proof: formalized
---

# 48.24 Gorenstein schemes

Section 48.24 of the Stacks Project, [Tag 0AWV](https://stacks.math.columbia.edu/tag/0AWV). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AWV, the section

[Tag 0AWV](https://stacks.math.columbia.edu/tag/0AWV) in the Stacks Project.

**`AlgebraicGeometry.isGorenstein_Spec_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/AffineCharacterization.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/AffineCharacterization.lean#L60). The attribute's comment: “the definition makes sense: for a Noetherian ring R, Spec R is a Gorenstein scheme if and only if R is a Gorenstein ring”.

> **The definition of a Gorenstein scheme agrees with that of a Gorenstein ring** (Section
> 0AWV). For a Noetherian ring `R`, the scheme `Spec R` is Gorenstein if and only if `R` is a
> Gorenstein ring, i.e. all of its local rings are Gorenstein.

```lean
theorem isGorenstein_Spec_iff (R : CommRingCat.{u}) [IsNoetherianRing R] :
    IsGorenstein (Spec R) ↔ Dualizing.IsGorensteinRing R
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsGorenstein`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Basic.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/AffineCharacterization.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/AffineCharacterization.lean#L43) (StacksFrontier): “the definition of the section: a scheme is Gorenstein if it is locally Noetherian and all of its local rings are Gorenstein”.

## Tag 0AWW, a definition

[Tag 0AWW](https://stacks.math.columbia.edu/tag/0AWW) in the Stacks Project.

**`AlgebraicGeometry.IsGorenstein`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Basic.lean#L43).

> A scheme is Gorenstein if it is locally Noetherian and all of its local rings are
> Gorenstein.

```lean
public class IsGorenstein (X : Scheme.{u}) : Prop extends IsLocallyNoetherian X
```

## Tag 0C00, a lemma

[Tag 0C00](https://stacks.math.columbia.edu/tag/0C00) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/CohenMacaulay.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/CohenMacaulay.lean#L37).

> **Stacks Project, Tag 0C00.** Every Gorenstein scheme is Cohen–Macaulay.

```lean
public theorem isCohenMacaulay_of_isGorenstein (X : Scheme.{u}) [IsGorenstein X] :
    IsCohenMacaulay X
```

## Tag 0DWG, a lemma

[Tag 0DWG](https://stacks.math.columbia.edu/tag/0DWG) in the Stacks Project.

**`AlgebraicGeometry.isGorenstein_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Regular.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Regular.lean#L36).

> **Stacks Project, Tag 0DWG.** Every regular scheme is Gorenstein.

```lean
public theorem isGorenstein_of_isRegular (X : Scheme.{u}) (hX : IsRegular X) :
    IsGorenstein X
```

## Tag 0BFQ, a lemma

[Tag 0BFQ](https://stacks.math.columbia.edu/tag/0BFQ) in the Stacks Project.

**`Stacks.Duality.isGorenstein_iff_isInvertible_dualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/DualizingInvertible.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/DualizingInvertible.lean#L214). The attribute's comment: “(1)(a): X is Gorenstein iff its dualizing complex is invertible in D(O_X)”.

> **Stacks Project, Tag 0BFQ, clause (1)(a).** A locally Noetherian scheme `X` carrying a
> dualizing complex `ω_X^•` is Gorenstein if and only if `ω_X^•` is an invertible object of
> `D(𝒪_X)`.

```lean
public theorem isGorenstein_iff_isInvertible_dualizingComplex [IsLocallyNoetherian X]
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K) :
    AlgebraicGeometry.IsGorenstein X ↔
      letI := Scheme.Modules.derivedMonoidal X
      MonoidalCategory.IsInvertible K
```

**`Stacks.Duality.isGorenstein_iff_hasInvertibleDualizingModelOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/InvertibleDualizing.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/InvertibleDualizing.lean#L140). The attribute's comment: “(1)(a): Gorenstein iff the dualizing complex is locally a shift of the structure ring, read at the affine-local models”.

> A locally Noetherian scheme carrying a dualizing complex is Gorenstein exactly when, at every
> affine open, that complex is the associated sheaf of a dualizing complex over the ring of sections
> which is locally a shifted unit — an invertible module in a single degree, locally on the affine
> open.
>
> By [Stacks, Tag 0FNT] the condition on the model says that it is an invertible object of
> `D(Γ(X, U))`; see `Stacks.Duality.isGorenstein_iff_isInvertible_dualizingModel`.

```lean
public theorem isGorenstein_iff_hasInvertibleDualizingModelOn (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) :
    AlgebraicGeometry.IsGorenstein X ↔
      ∀ (U : X.Opens) (hU : IsAffineOpen U), HasInvertibleDualizingModelOn K U hU
```

**`Stacks.Duality.isGorenstein_iff_isInvertible_dualizingModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/InvertibleDualizing.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/InvertibleDualizing.lean#L175). The attribute's comment: “(1)(a): Gorenstein iff the dualizing complex is an invertible object, read at the affine-local models”.

> A locally Noetherian scheme carrying a dualizing complex is Gorenstein exactly when, at every
> affine open, that complex is the associated sheaf of a dualizing complex over the ring of sections
> which is an invertible object of its derived category, for the canonical derived tensor product of
> [Stacks, Tag 0FNQ].
>
> This is `Stacks.Duality.isGorenstein_iff_hasInvertibleDualizingModelOn` rewritten through
> [Stacks, Tag 0FNT].

```lean
public theorem isGorenstein_iff_isInvertible_dualizingModel (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) :
    AlgebraicGeometry.IsGorenstein X ↔
      ∀ (U : X.Opens) (hU : IsAffineOpen U),
        letI : IsNoetherianRing Γ(X, U) := IsLocallyNoetherian.component_noetherian ⟨U, hU⟩
        letI := HasDerivedCategory.standard U.toScheme.Modules
        letI := HasDerivedCategory.standard (ModuleCat.{u} Γ(X, U))
        letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
          Γ(X, U)).choose
        ∃ ω : DerivedCategory (ModuleCat.{u} Γ(X, U)),
          Dualizing.IsDualizingComplex ω ∧
            MonoidalCategory.IsInvertible ω ∧
              Nonempty ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj K ≅
                (tilde.functor Γ(X, U) ⋙
                  Scheme.Modules.restrictFunctor hU.isoSpec.hom).mapDerivedCategory.obj ω)
```

**`Stacks.Duality.exists_isOpen_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Locus.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/Locus.lean#L140). The attribute's comment: “(1)(c): the Gorenstein locus is an open Gorenstein subscheme”.

> **Stacks Project, Tag 0BFQ, clause (1)(c).** On a locally Noetherian scheme carrying a
> dualizing complex, `U = {x ∈ X | 𝒪_{X,x} is Gorenstein}` is open and, as an open subscheme, is a
> Gorenstein scheme.

```lean
public theorem exists_isOpen_isGorenstein (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) :
    ∃ hU : IsOpen {x : X | Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x)},
      AlgebraicGeometry.IsGorenstein (Scheme.Opens.toScheme (X := X) ⟨_, hU⟩)
```

**`Stacks.Duality.isGorensteinLocalRing_stalk_iff_isInvertible_localizedDualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkInvertibleDualizing.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkInvertibleDualizing.lean#L88). The attribute's comment: “(1)(b): the local ring at a point is Gorenstein iff the dualizing complex localized at that point is invertible, read at the affine-local models”.

> Let `X` be a locally Noetherian scheme, `U` an affine open and `x` a point of `U`. For every
> dualizing complex `ω` over `Γ(X, U)`, the local ring of `X` at `x` is Gorenstein exactly when the
> derived localization of `ω` at the prime `x` defines is an invertible object of the derived
> category of that localization.

```lean
public theorem isGorensteinLocalRing_stalk_iff_isInvertible_localizedDualizing
    {U : X.Opens} (hU : IsAffineOpen U) (x : U) :
    letI : IsNoetherianRing Γ(X, U) := IsLocallyNoetherian.component_noetherian ⟨U, hU⟩
    letI := HasDerivedCategory.standard (ModuleCat.{u} Γ(X, U))
    letI : (hU.primeIdealOf x).asIdeal.IsPrime := (hU.primeIdealOf x).isPrime
    letI := HasDerivedCategory.standard
      (ModuleCat.{u} (Localization.AtPrime (hU.primeIdealOf x).asIdeal))
    letI := Dualizing.derivedCategoryMonoidal.{u, u}
      (Localization.AtPrime (hU.primeIdealOf x).asIdeal)
    ∀ ω : DerivedCategory (ModuleCat.{u} Γ(X, U)), Dualizing.IsDualizingComplex ω →
      (Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x.1) ↔
        MonoidalCategory.IsInvertible
          ((StacksDraft.PseudoCoherence.derivedExtensionScalars
              (algebraMap Γ(X, U)
                (Localization.AtPrime (hU.primeIdealOf x).asIdeal))).obj ω))
```

**`Stacks.Duality.isGorensteinLocalRing_stalk_iff_isInvertible_localizedDualizingModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkInvertibleDualizing.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkInvertibleDualizing.lean#L130). The attribute's comment: “(1)(b): the local ring at a point is Gorenstein iff the dualizing complex of the scheme, localized at that point, is invertible, read at the affine-local models”.

> Let `K` be a dualizing complex on a locally Noetherian scheme `X`, and `x` a point of an
> affine open `U`. The local ring of `X` at `x` is Gorenstein exactly when `K` has a dualizing model
> on `U` whose derived localization at the prime of `x` is invertible.

```lean
public theorem isGorensteinLocalRing_stalk_iff_isInvertible_localizedDualizingModel
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K)
    {U : X.Opens} (hU : IsAffineOpen U) (x : U) :
    letI : IsNoetherianRing Γ(X, U) := IsLocallyNoetherian.component_noetherian ⟨U, hU⟩
    letI := HasDerivedCategory.standard U.toScheme.Modules
    letI := HasDerivedCategory.standard (ModuleCat.{u} Γ(X, U))
    letI : (hU.primeIdealOf x).asIdeal.IsPrime := (hU.primeIdealOf x).isPrime
    letI := HasDerivedCategory.standard
      (ModuleCat.{u} (Localization.AtPrime (hU.primeIdealOf x).asIdeal))
    letI := Dualizing.derivedCategoryMonoidal.{u, u}
      (Localization.AtPrime (hU.primeIdealOf x).asIdeal)
    Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x.1) ↔
      ∃ ω : DerivedCategory (ModuleCat.{u} Γ(X, U)),
        Dualizing.IsDualizingComplex ω ∧
          Nonempty ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj K ≅
            (tilde.functor Γ(X, U) ⋙
              Scheme.Modules.restrictFunctor hU.isoSpec.hom).mapDerivedCategory.obj ω) ∧
            MonoidalCategory.IsInvertible
              ((StacksDraft.PseudoCoherence.derivedExtensionScalars
                  (algebraMap Γ(X, U)
                    (Localization.AtPrime (hU.primeIdealOf x).asIdeal))).obj ω)
```

**`Stacks.Duality.isGorensteinLocalRing_stalk_iff_isInvertible_derivedStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkwiseInvertible.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StalkwiseInvertible.lean#L185). The attribute's comment: “(1)(b): the local ring at a point is Gorenstein iff the derived stalk of the dualizing complex is invertible”.

> On a locally Noetherian scheme carrying a dualizing complex `K`, the local ring at `x` is
> Gorenstein exactly when the derived stalk `K_x` is an invertible object of `D(𝒪_{X,x})`.

```lean
public theorem isGorensteinLocalRing_stalk_iff_isInvertible_derivedStalk
    [HasDerivedCategory.{u + 1} X.Modules] (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) (x : X) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} (X.presheaf.stalk x))
    letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
      (X.presheaf.stalk x)).choose
    Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x) ↔
      MonoidalCategory.IsInvertible ((AlgebraicGeometry.derivedStalkFunctor x).obj K)
```

**`Stacks.Duality.exists_isDualizingComplex_iff_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StructureSheafDualizing.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/StructureSheafDualizing.lean#L84). The attribute's comment: “(2): a Gorenstein scheme has a dualizing complex iff its structure sheaf is one”.

> A Gorenstein scheme has a dualizing complex if and only if its structure sheaf, placed in
> degree zero, is a dualizing complex.

```lean
public theorem exists_isDualizingComplex_iff_unit [AlgebraicGeometry.IsGorenstein X]
    [HasDerivedCategory.{w} X.Modules] :
    (∃ K : DerivedCategory X.Modules, IsDualizingComplex K) ↔
      IsDualizingComplex ((DerivedCategory.singleFunctor X.Modules 0).obj
        (SheafOfModules.unit X.ringCatSheaf))
```

## Tag 0BVA, a lemma

[Tag 0BVA](https://stacks.math.columbia.edu/tag/0BVA) in the Stacks Project.

**`AlgebraicGeometry.isGorenstein_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/LocalCompleteIntersection.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/LocalCompleteIntersection.lean#L118).

> A local complete intersection morphism whose target is a Gorenstein scheme has Gorenstein
> source.

```lean
public theorem isGorenstein_of_isLocalCompleteIntersectionMorphism {X Y : Scheme.{u}} (f : Y ⟶ X)
    (hf : IsLocalCompleteIntersectionMorphism f) (hX : IsGorenstein X) : IsGorenstein Y
```

## Tag 0C01, a lemma

[Tag 0C01](https://stacks.math.columbia.edu/tag/0C01) in the Stacks Project.

**`AlgebraicGeometry.isGorenstein_isLocal_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Gorenstein.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/Gorenstein.lean#L71).

> **Stacks Project, Tag 0C01.** Being Gorenstein is local for syntomic coverings.

```lean
instance isGorenstein_isLocal_syntomic :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsGorenstein X)
      (Scheme.precoverage @Syntomic)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.24, Tag 0AWV](https://stacks.math.columbia.edu/tag/0AWV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
