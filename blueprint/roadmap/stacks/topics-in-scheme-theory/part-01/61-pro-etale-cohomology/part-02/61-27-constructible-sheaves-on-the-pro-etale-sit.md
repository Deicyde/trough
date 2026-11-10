---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.IsConstructibleModuleSheaf, AlgebraicGeometry.ProEtale.IsConstructibleModuleSheaf', AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageConstructible, AlgebraicGeometry.ProEtale.isWeakSerreClass_isConstructibleModuleSheaf', AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageDerivedConstructible, AlgebraicGeometry.ProEtale.minus_tensor_and_isConstructibleModuleSheaf'_homology, AlgebraicGeometry.ProEtale.minus_and_isConstructibleModuleSheaf'_homology_derivedExtendScalars
statement: formalized
proof: formalized
---

# 61.27 Constructible sheaves on the pro-étale site

Section 61.27 of the Stacks Project, [Tag 09AI](https://stacks.math.columbia.edu/tag/09AI). 6 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09AJ, a definition

[Tag 09AJ](https://stacks.math.columbia.edu/tag/09AJ) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.IsConstructibleModuleSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/Defs.lean#L79).

> **Stacks 09AJ.** A sheaf of `Λ`-modules on the small pro-étale site of `X`, with `Λ`
> Noetherian, is *constructible* if every affine open of `X` has a finite partition into
> constructible locally closed subschemes on each of which the inverse image of the sheaf is
> locally constant of finite type.

```lean
abbrev IsConstructibleModuleSheaf (X : Scheme.{u}) (Λ : Type v) [CommRing Λ]
    [IsNoetherianRing Λ]
    [∀ Y : Scheme.{u}, HasWeakSheafify (Scheme.ProEt.topology Y) (ModuleCat.{w} Λ)]
    [∀ (Y : Scheme.{u}) (V : Y.ProEt),
      HasWeakSheafify ((Scheme.ProEt.topology Y).over V) (ModuleCat.{w} Λ)]
    [∀ {Z Y : Scheme.{u}} (f : Z ⟶ Y),
      ((Scheme.proetaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{w} Λ) (Scheme.ProEt.topology Y)
        (Scheme.ProEt.topology Z)).IsRightAdjoint]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{w} Λ)) : Prop
```

**`AlgebraicGeometry.ProEtale.IsConstructibleModuleSheaf'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleSheaves.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleSheaves.lean#L85).

> **Stacks 09AJ.** A sheaf of `Λ`-modules on the small pro-étale site of `X` is
> *constructible* when every affine open `U` of `X` admits a finite decomposition into
> constructible locally closed subschemes on each of which the inverse image of the sheaf is
> locally constant of finite type.
>
> This is reducible, so a client can use the witnesses of the stratification directly.
>
> The primed name records the weaker hypotheses: pinning the sections universe to
> `max (u + 1) v w` makes sheafification and the left Kan extensions exist unconditionally, so
> this form needs none of the `HasWeakSheafify` and `IsRightAdjoint` assumptions that
> `AlgebraicGeometry.ProEtale.IsConstructibleModuleSheaf` of
> `StacksFrontier.AlgebraicGeometry.ProEtale.Constructible.Defs` carries, at the cost of leaving
> that universe no longer free. The two are stated with different local-constancy predicates —
> `Stacks.ConstantSheaf.IsFiniteTypeLocallyConstantModuleSheaf` here against
> `Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant` there — and identifying them is not done.

```lean
public abbrev IsConstructibleModuleSheaf' (X : Scheme.{u}) (Λ : Type v) [CommRing Λ]
    [IsNoetherianRing Λ]
    (F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ)) : Prop
```

## Tag 09AK, a lemma

[Tag 09AK](https://stacks.math.columbia.edu/tag/09AK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageConstructible`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ConstructibleComparison.lean#L196), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L66) (StacksFrontier).

## Tag 09B5, a lemma

[Tag 09B5](https://stacks.math.columbia.edu/tag/09B5) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isWeakSerreClass_isConstructibleModuleSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/WeakSerre.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/WeakSerre.lean#L113).

> **Stacks 09B5.** For `Λ` a Noetherian ring, the constructible sheaves of `Λ`-modules on the
> small pro-étale site of a scheme `X` form a weak Serre subcategory of all sheaves of
> `Λ`-modules on that site. There is no hypothesis on `X`.

```lean
public theorem isWeakSerreClass_isConstructibleModuleSheaf' :
    ObjectProperty.IsWeakSerreClass
      (fun F : Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) v w} Λ) =>
        IsConstructibleModuleSheaf'.{u, v, w} X Λ F)
```

## Tag 09AL, a lemma

[Tag 09AL](https://stacks.math.columbia.edu/tag/09AL) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageDerivedConstructible`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ModuleComparisonWithEtale.lean#L346), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L68) (StacksFrontier).

## Tag 09BQ, a lemma

[Tag 09BQ](https://stacks.math.columbia.edu/tag/09BQ) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.minus_tensor_and_isConstructibleModuleSheaf'_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/DerivedTensor.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/DerivedTensor.lean#L158).

> **Stacks 09BQ.** Let `X` be a scheme and `Λ` a Noetherian ring. If `K` and `L` are bounded
> above objects of `D(X_proét, Λ)` whose cohomology sheaves are constructible, then their derived
> tensor product `K ⊗_Λ^L L` is bounded above and has constructible cohomology sheaves: it lies in
> `D_c^-(X_proét, Λ)`.

```lean
theorem minus_tensor_and_isConstructibleModuleSheaf'_homology
    (K L : DerivedCategory (Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ)))
    (hK : DerivedCategory.TStructure.t.minus K) (hL : DerivedCategory.TStructure.t.minus L)
    (hKc : ∀ i, IsConstructibleModuleSheaf'.{u, max (u + 1) w, w} X Λ
      ((DerivedCategory.homologyFunctor _ i).obj K))
    (hLc : ∀ i, IsConstructibleModuleSheaf'.{u, max (u + 1) w, w} X Λ
      ((DerivedCategory.homologyFunctor _ i).obj L)) :
    DerivedCategory.TStructure.t.minus (K ⊗ L) ∧
      ∀ i, IsConstructibleModuleSheaf'.{u, max (u + 1) w, w} X Λ
        ((DerivedCategory.homologyFunctor _ i).obj (K ⊗ L))
```

## Tag 09BR, a lemma

[Tag 09BR](https://stacks.math.columbia.edu/tag/09BR) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.minus_and_isConstructibleModuleSheaf'_homology_derivedExtendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/DerivedReduction.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Constructible/DerivedReduction.lean#L265).

> **Stacks 09BR.** Let `X` be a scheme, `Λ` a Noetherian ring, `I ⊆ Λ` an ideal and `K` an
> object of `D(X_proét, Λ)`. Set `Kₙ = K ⊗_Λ^L Λ/Iⁿ`, the derived extension of scalars of `K` along
> `Λ → Λ/Iⁿ`. If `K₁` lies in `D_c^-(X_proét, Λ/I)`, that is, it is bounded above and its
> cohomology sheaves are constructible, then `Kₙ` lies in `D_c^-(X_proét, Λ/Iⁿ)` for all `n`.

```lean
theorem minus_and_isConstructibleModuleSheaf'_homology_derivedExtendScalars
    (K : DerivedCategory (Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ)))
    (hK : DerivedCategory.TStructure.t.minus
        ((derivedExtendScalars _ (Ideal.Quotient.mk I)).obj K) ∧
      ∀ i, IsConstructibleModuleSheaf'.{u, max (u + 1) w, w} X (Λ ⧸ I)
        ((DerivedCategory.homologyFunctor _ i).obj
          ((derivedExtendScalars _ (Ideal.Quotient.mk I)).obj K)))
    (n : ℕ) :
    DerivedCategory.TStructure.t.minus
        ((derivedExtendScalars _ (Ideal.Quotient.mk (I ^ n))).obj K) ∧
      ∀ i, IsConstructibleModuleSheaf'.{u, max (u + 1) w, w} X (Λ ⧸ I ^ n)
        ((DerivedCategory.homologyFunctor _ i).obj
          ((derivedExtendScalars _ (Ideal.Quotient.mk (I ^ n))).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.27, Tag 09AI](https://stacks.math.columbia.edu/tag/09AI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
