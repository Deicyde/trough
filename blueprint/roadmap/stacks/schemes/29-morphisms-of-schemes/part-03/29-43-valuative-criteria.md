---
declaration: section
origin: cited
lean: AlgebraicGeometry.universallyClosed_of_unique_lift_of_denseRange, AlgebraicGeometry.isSeparated_of_unique_lift_of_denseRange, AlgebraicGeometry.refinedValuative_unique_iff_hasLift_of_isSeparated, AlgebraicGeometry.exists_hasLift_of_denseRange_not_universallyClosed_not_isSeparated, AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isReduced, AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isIntegral, AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isLocallyNoetherian, AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_locallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 29.43 Valuative criteria

Section 29.43 of the Stacks Project, [Tag 0BX4](https://stacks.math.columbia.edu/tag/0BX4). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0894, a lemma

[Tag 0894](https://stacks.math.columbia.edu/tag/0894) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_of_unique_lift_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefined.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefined.lean#L542). The attribute's comment: “universally closed conclusion”.

> **Stacks 0894, universally closed part.**
> Let `f : X ⟶ S` and `h : U ⟶ X` be quasi-compact morphisms of schemes and suppose that
> `h(U)` is dense in `X`. If every valuative square for `f` whose generic-point map factors through
> `h` has a unique lift, then `f` is universally closed.

```lean
public lemma universallyClosed_of_unique_lift_of_denseRange
    {U X S : AlgebraicGeometry.Scheme.{u}}
    (h : U ⟶ X) (f : X ⟶ S) [AlgebraicGeometry.QuasiCompact f]
    [AlgebraicGeometry.QuasiCompact h] (hdense : DenseRange h)
    (hvaluative : ∀ (D : AlgebraicGeometry.ValuativeCommSq f)
      (g : AlgebraicGeometry.Spec (.of D.K) ⟶ U),
      g ≫ h = D.i₁ → Nonempty (Unique D.commSq.LiftStruct)) :
    AlgebraicGeometry.UniversallyClosed f
```

**`AlgebraicGeometry.isSeparated_of_unique_lift_of_denseRange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefined.lean, line 606](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefined.lean#L606). The attribute's comment: “separated conclusion”.

> **Stacks 0894, separated part.**
> Under the hypotheses of the refined valuative criterion, a quasi-separated morphism `f` is
> separated.

```lean
public lemma isSeparated_of_unique_lift_of_denseRange
    {U X S : AlgebraicGeometry.Scheme.{u}}
    (h : U ⟶ X) (f : X ⟶ S) [AlgebraicGeometry.QuasiCompact f]
    [AlgebraicGeometry.QuasiCompact h] [AlgebraicGeometry.QuasiSeparated f]
    (hdense : DenseRange h)
    (hvaluative : ∀ (D : AlgebraicGeometry.ValuativeCommSq f)
      (g : AlgebraicGeometry.Spec (.of D.K) ⟶ U),
      g ≫ h = D.i₁ → Nonempty (Unique D.commSq.LiftStruct)) :
    AlgebraicGeometry.IsSeparated f
```

## Tag 0895, a remark

[Tag 0895](https://stacks.math.columbia.edu/tag/0895) in the Stacks Project.

**`AlgebraicGeometry.refinedValuative_unique_iff_hasLift_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefinedNecessity.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefinedNecessity.lean#L55). The attribute's comment: “uniqueness of the dotted arrows is guaranteed when f is separated”.

> If `f` is separated, the dotted arrows in the refined valuative criterion are automatically
> unique: every valuative square for `f` whose generic-point map factors through `h` has a unique
> lift as soon as it has one.

```lean
public theorem refinedValuative_unique_iff_hasLift_of_isSeparated
    {U X S : Scheme.{u}} (h : U ⟶ X) (f : X ⟶ S) [IsSeparated f] :
    (∀ (D : ValuativeCommSq f) (g : Spec (.of D.K) ⟶ U),
      g ≫ h = D.i₁ → Nonempty (Unique D.commSq.LiftStruct)) ↔
    (∀ (D : ValuativeCommSq f) (g : Spec (.of D.K) ⟶ U),
      g ≫ h = D.i₁ → D.commSq.HasLift)
```

**`AlgebraicGeometry.exists_hasLift_of_denseRange_not_universallyClosed_not_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefinedNecessity.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ValuativeCriterionRefinedNecessity.lean#L355). The attribute's comment: “the uniqueness assumption of Lemma 0894 is necessary”.

> The uniqueness of the dotted arrows in the refined valuative criterion
> `universallyClosed_of_unique_lift_of_denseRange` cannot be dropped. There are quasi-compact
> morphisms `f : X ⟶ S` and `h : U ⟶ X`, with `f` quasi-separated and `h(U)` dense in `X`, such
> that every commutative square from `Spec K ⟶ Spec A` (with `A` a valuation ring with fraction
> field `K`) whose top map factors through `h` admits a dotted arrow, while `f` is neither
> universally closed nor separated.

```lean
public theorem exists_hasLift_of_denseRange_not_universallyClosed_not_isSeparated :
    ∃ (U X S : Scheme.{u}) (h : U ⟶ X) (f : X ⟶ S),
      QuasiCompact f ∧ QuasiCompact h ∧ QuasiSeparated f ∧ DenseRange h ∧
      (∀ (D : ValuativeCommSq f) (g : Spec (.of D.K) ⟶ U),
        g ≫ h = D.i₁ → D.commSq.HasLift) ∧
      ¬ UniversallyClosed f ∧ ¬ IsSeparated f
```

## Tag 0BX6, a lemma

[Tag 0BX6](https://stacks.math.columbia.edu/tag/0BX6) in the Stacks Project.

**`AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isReduced`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean#L257). The attribute's comment: “local\_extension”. References: EGA I (6.5.1), “(ii), X reduced case”.

> A compatible local homomorphism is induced by a morphism on an open neighbourhood when the
> target is locally of finite type and the source is reduced with finitely many irreducible
> components.

```lean
lemma exists_open_morphism_inducing_localHom_of_isReduced
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (s : S) (x : X) (y : Y) (hx : pX x = s) (hy : pY y = s)
    (phi : Y.presheaf.stalk y →+* X.presheaf.stalk x)
    (hphi : IsLocalHom phi)
    (hphiS : phi.comp
        ((pY.stalkMap y).hom.comp
          (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hy).symm).hom) =
      (pX.stalkMap x).hom.comp
        (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hx).symm).hom)
    (hft : LocallyOfFiniteType pY) (hred : IsReduced X)
    (hcomp : (irreducibleComponents X).Finite) :
    ∃ (U : X.Opens) (hxU : x ∈ U) (f : (U : Scheme.{u}) ⟶ Y)
      (_hf : f ≫ pY = U.ι ≫ pX)
      (hfy : f ⟨x, hxU⟩ = y),
      ((U.stalkIso ⟨x, hxU⟩).hom.hom.comp
          ((f.stalkMap ⟨x, hxU⟩).hom.comp
            (eqToHom (congrArg (fun z ↦ Y.presheaf.stalk z) hfy).symm).hom)) = phi
```

**`AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isIntegral`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean#L282). The attribute's comment: “local\_extension, Y locally of finite type and X integral”.

> A compatible local homomorphism is induced by a morphism on an open neighbourhood when the
> target is locally of finite type over the base and the source is integral.

```lean
lemma exists_open_morphism_inducing_localHom_of_isIntegral
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (s : S) (x : X) (y : Y) (hx : pX x = s) (hy : pY y = s)
    (phi : Y.presheaf.stalk y →+* X.presheaf.stalk x)
    (hphi : IsLocalHom phi)
    (hphiS : phi.comp
        ((pY.stalkMap y).hom.comp
          (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hy).symm).hom) =
      (pX.stalkMap x).hom.comp
        (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hx).symm).hom)
    (hft : LocallyOfFiniteType pY) (hint : IsIntegral X) :
    ∃ (U : X.Opens) (hxU : x ∈ U) (f : (U : Scheme.{u}) ⟶ Y)
      (_hf : f ≫ pY = U.ι ≫ pX)
      (hfy : f ⟨x, hxU⟩ = y),
      ((U.stalkIso ⟨x, hxU⟩).hom.hom.comp
          ((f.stalkMap ⟨x, hxU⟩).hom.comp
            (eqToHom (congrArg (fun z ↦ Y.presheaf.stalk z) hfy).symm).hom)) = phi
```

**`AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_isLocallyNoetherian`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtension.lean#L305). The attribute's comment: “local\_extension, Y locally of finite type and X locally Noetherian”.

> A compatible local homomorphism is induced by a morphism on an open neighbourhood when the
> target is locally of finite type over the base and the source is locally Noetherian.

```lean
lemma exists_open_morphism_inducing_localHom_of_isLocallyNoetherian
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (s : S) (x : X) (y : Y) (hx : pX x = s) (hy : pY y = s)
    (phi : Y.presheaf.stalk y →+* X.presheaf.stalk x)
    (hphi : IsLocalHom phi)
    (hphiS : phi.comp
        ((pY.stalkMap y).hom.comp
          (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hy).symm).hom) =
      (pX.stalkMap x).hom.comp
        (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hx).symm).hom)
    (hft : LocallyOfFiniteType pY) (hnoeth : IsLocallyNoetherian X) :
    ∃ (U : X.Opens) (hxU : x ∈ U) (f : (U : Scheme.{u}) ⟶ Y)
      (_hf : f ≫ pY = U.ι ≫ pX)
      (hfy : f ⟨x, hxU⟩ = y),
      ((U.stalkIso ⟨x, hxU⟩).hom.hom.comp
          ((f.stalkMap ⟨x, hxU⟩).hom.comp
            (eqToHom (congrArg (fun z ↦ Y.presheaf.stalk z) hfy).symm).hom)) = phi
```

**`AlgebraicGeometry.exists_open_morphism_inducing_localHom_of_locallyOfFinitePresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtensionFinitePresentation.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalExtensionFinitePresentation.lean#L270). The attribute's comment: “local\_extension”. References: EGA I (6.5.1), “(ii)”.

> **Stacks Project, Tag 0BX6 (local extension), finite-presentation case.** A compatible
> local homomorphism of local rings is induced by a morphism on an open neighbourhood.

```lean
public lemma exists_open_morphism_inducing_localHom_of_locallyOfFinitePresentation
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (s : S) (x : X) (y : Y) (hx : pX x = s) (hy : pY y = s)
    (phi : Y.presheaf.stalk y →+* X.presheaf.stalk x)
    (hphi : IsLocalHom phi)
    (hphiS : phi.comp
        ((pY.stalkMap y).hom.comp
          (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hy).symm).hom) =
      (pX.stalkMap x).hom.comp
        (eqToHom (congrArg (fun z ↦ S.presheaf.stalk z) hx).symm).hom)
    (hfin : LocallyOfFinitePresentation pY) :
    ∃ (U : X.Opens) (hxU : x ∈ U) (f : (U : Scheme.{u}) ⟶ Y)
      (_hf : f ≫ pY = U.ι ≫ pX)
      (hfy : f ⟨x, hxU⟩ = y),
      ((U.stalkIso ⟨x, hxU⟩).hom.hom.comp
          ((f.stalkMap ⟨x, hxU⟩).hom.comp
            (eqToHom (congrArg (fun z ↦ Y.presheaf.stalk z) hfy).symm).hom)) = phi
```

**`AlgebraicGeometry.exists_open_eq_of_stalkMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalUniqueness.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/LocalUniqueness.lean#L176). The attribute's comment: “local\_uniqueness”. References: EGA I (6.5.1), “(i)”.

> Two morphisms over a scheme which agree on the local ring at a point agree on some open
> neighbourhood of that point, provided the target is locally of finite type over the base, or
> the source is integral, locally Noetherian, or reduced with finitely many irreducible
> components.

```lean
theorem exists_open_eq_of_stalkMap_eq
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S) (f g : X ⟶ Y)
    (hf : f ≫ pY = pX) (hg : g ≫ pY = pX)
    (s : S) (x : X) (y : Y) (hxs : pX x = s) (hys : pY y = s)
    (hfx : f x = y) (hgx : g x = y)
    (hfg : f.stalkMap x =
      Y.presheaf.stalkSpecializes
        (Inseparable.of_eq (hfx.trans hgx.symm).symm).specializes ≫ g.stalkMap x)
    (h : LocallyOfFiniteType pY ∨ IsIntegral X ∨ IsLocallyNoetherian X ∨
      (IsReduced X ∧ (irreducibleComponents X).Finite)) :
    ∃ U : X.Opens, x ∈ U ∧ U.ι ≫ f = U.ι ≫ g
```

## Tag 0BX7, a lemma

[Tag 0BX7](https://stacks.math.columbia.edu/tag/0BX7) in the Stacks Project.

**`AlgebraicGeometry.exists_open_extension_of_valuationRing_stalk`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/Extension.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/Extension.lean#L209).

> **Stacks Project, Tag 0BX7.** A morphism from an open subscheme extends across a point
> whose local ring is a valuation ring, provided the target is proper over the base and the
> source is either reduced with finitely many irreducible components or Noetherian.

```lean
lemma exists_open_extension_of_valuationRing_stalk
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (x : X) (U : X.Opens) (f : (U : Scheme.{u}) ⟶ Y)
    (hf : f ≫ pY = U.ι ≫ pX)
    (hxU : x ∈ closure (U : Set X))
    (hX : (IsReduced X ∧ (irreducibleComponents X).Finite) ∨
      IsNoetherian X)
    [IsDomain (X.presheaf.stalk x)] [ValuationRing (X.presheaf.stalk x)]
    [IsProper pY] :
    ∃ (U' : X.Opens) (hUU' : U ≤ U') (_ : x ∈ U')
      (f' : (U' : Scheme.{u}) ⟶ Y),
      f' ≫ pY = U'.ι ≫ pX ∧ X.homOfLE hUU' ≫ f' = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.43, Tag 0BX4](https://stacks.math.columbia.edu/tag/0BX4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
