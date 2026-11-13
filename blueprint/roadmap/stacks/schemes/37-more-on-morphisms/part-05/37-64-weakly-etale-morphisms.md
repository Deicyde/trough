---
declaration: section
origin: cited
lean: AlgebraicGeometry.weaklyEtale_iff_stalkMap_weaklyEtale, AlgebraicGeometry.isFlatOver_self_of_flat_diagonal, AlgebraicGeometry.weaklyEtale_tfae, AlgebraicGeometry.WeaklyEtale.instResLE, CategoryTheory.MorphismProperty.diagonal_isStableUnderComposition, AlgebraicGeometry.WeaklyEtale.instCompScheme, CategoryTheory.MorphismProperty.IsStableUnderBaseChange.diagonal, AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme
statement: formalized
proof: formalized
---

# 37.64 Weakly étale morphisms

Section 37.64 of the Stacks Project, [Tag 094N](https://stacks.math.columbia.edu/tag/094N). 13 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 094Q, a lemma

[Tag 094Q](https://stacks.math.columbia.edu/tag/094Q) in the Stacks Project.

**`AlgebraicGeometry.weaklyEtale_iff_stalkMap_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Stalks.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Stalks.lean#L170).

> A morphism of schemes is weakly étale if and only if all of its maps on local rings
> are weakly étale.

```lean
theorem weaklyEtale_iff_stalkMap_weaklyEtale
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y) :
    AlgebraicGeometry.WeaklyEtale f ↔
      ∀ x : X,
        letI := (f.stalkMap x).hom.toAlgebra
        Algebra.WeaklyEtale (Y.presheaf.stalk (f x)) (X.presheaf.stalk x)
```

## Tag 094R, a lemma

[Tag 094R](https://stacks.math.columbia.edu/tag/094R) in the Stacks Project.

**`AlgebraicGeometry.isFlatOver_self_of_flat_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Flat.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Flat.lean#L84).

> If the diagonal of a scheme morphism is flat, every module flat over the
> target is flat over the source.

```lean
theorem isFlatOver_self_of_flat_diagonal
    {X Y : Scheme.{u}} (f : X ⟶ Y) (F : X.Modules)
    [Flat (pullback.diagonal f)]
    (hF : IsFlatOver f.toLRSHom.toShHom F) :
    IsFlatOver ((𝟙 X : X ⟶ X).toLRSHom.toShHom) F
```

## Tag 094S, a lemma

[Tag 094S](https://stacks.math.columbia.edu/tag/094S) in the Stacks Project.

**`AlgebraicGeometry.weaklyEtale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean#L110). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 094S.** For a morphism of schemes, weak étaleness is equivalent to
> weak étaleness of every induced map on affine-open sections, to admitting compatible open
> coverings on which the restricted morphisms are weakly étale, and to the analogous condition for
> affine-open coverings and their induced maps on sections.

```lean
theorem weaklyEtale_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    let weaklyEtaleOn := fun (V : S.Opens) (U : X.Opens) (e : U ≤ f ⁻¹ᵁ V) ↦
      @Algebra.WeaklyEtale Γ(S, V) Γ(X, U) _ _ (f.appLE V U e).hom.toAlgebra
    List.TFAE [
      WeaklyEtale f,
      ∀ (U : X.Opens), IsAffineOpen U →
        ∀ (V : S.Opens), IsAffineOpen V →
          ∀ (e : U ≤ f ⁻¹ᵁ V), weaklyEtaleOn V U e,
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ (V j)),
            ∀ i, WeaklyEtale
              (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ (V j)),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i, weaklyEtaleOn (V j) (U i) ((le_iSup U i).trans hU.le)]
```

Declarations registered for the tag:

- [`AlgebraicGeometry.WeaklyEtale.instResLE`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.WeaklyEtale.instResLE#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean#L173) (StacksFrontier): “restriction to open subschemes”.

## Tag 094T, a lemma

[Tag 094T](https://stacks.math.columbia.edu/tag/094T) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.diagonal_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.diagonal_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L43) (StacksFrontier): “(1), for `P = @AlgebraicGeometry.Flat` on schemes: flat diagonals compose”.
- [`AlgebraicGeometry.WeaklyEtale.instCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.WeaklyEtale.instCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L46) (StacksFrontier): “(2)”.

## Tag 094U, a lemma

[Tag 094U](https://stacks.math.columbia.edu/tag/094U) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsStableUnderBaseChange.diagonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsStableUnderBaseChange.diagonal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L49) (StacksFrontier): “(1), for `P = @AlgebraicGeometry.Flat` on schemes: flat diagonals base change”.
- [`AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L52) (StacksFrontier): “(2)”.

## Tag 094V, a lemma

[Tag 094V](https://stacks.math.columbia.edu/tag/094V) in the Stacks Project.

**`AlgebraicGeometry.flat_diagonal_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/WeaklyEtale/DiagonalDescent.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/WeaklyEtale/DiagonalDescent.lean#L37).

> Flatness of the relative diagonal descends along a surjective flat morphism.

```lean
theorem flat_diagonal_of_surjective_flat {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z) [Flat f] [Surjective f]
    [Flat (pullback.diagonal (f ≫ g))] :
    Flat (pullback.diagonal g)
```

## Tag 094W, a lemma

[Tag 094W](https://stacks.math.columbia.edu/tag/094W) in the Stacks Project.

**`AlgebraicGeometry.instFormallyUnramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean#L179).

> **Stacks Project, Tag 094W.** A weakly étale morphism of schemes is formally
> unramified.

```lean
instance instFormallyUnramified
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y)
    [AlgebraicGeometry.WeaklyEtale f] :
    AlgebraicGeometry.FormallyUnramified f
```

## Tag 094X, a lemma

[Tag 094X](https://stacks.math.columbia.edu/tag/094X) in the Stacks Project.

**`AlgebraicGeometry.WeaklyEtale.of_flat_of_mono`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean#L50). The attribute's comment: “(1) flat monomorphism”.

> A flat monomorphism of schemes is weakly étale: its diagonal is an isomorphism.

```lean
instance (priority := 900) of_flat_of_mono [Flat f] [Mono f] : WeaklyEtale f
```

**`AlgebraicGeometry.WeaklyEtale.of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean#L54). The attribute's comment: “(2) open immersion”.

> An open immersion of schemes is weakly étale.

```lean
theorem of_isOpenImmersion [IsOpenImmersion f] : WeaklyEtale f
```

**`AlgebraicGeometry.WeaklyEtale.of_flat_of_formallyUnramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean#L59). The attribute's comment: “(3) flat and unramified”.

> A flat unramified morphism of schemes is weakly étale: its diagonal is an open immersion.

```lean
instance (priority := 900) of_flat_of_formallyUnramified [Flat f] [FormallyUnramified f]
    [LocallyOfFiniteType f] : WeaklyEtale f
```

**`AlgebraicGeometry.WeaklyEtale.of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Examples.lean#L64). The attribute's comment: “(4) étale”.

> An étale morphism of schemes is weakly étale.

```lean
theorem of_etale [Etale f] : WeaklyEtale f
```

## Tag 094Y, a lemma

[Tag 094Y](https://stacks.math.columbia.edu/tag/094Y) in the Stacks Project.

**`AlgebraicGeometry.isReduced_of_weaklyEtale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Characterization.lean#L190).

> The source of a weakly étale morphism with reduced target is reduced.

```lean
lemma isReduced_of_weaklyEtale
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y)
    [AlgebraicGeometry.IsReduced Y] [AlgebraicGeometry.WeaklyEtale f] :
    AlgebraicGeometry.IsReduced X
```

## Tag 094Z, a lemma

[Tag 094Z](https://stacks.math.columbia.edu/tag/094Z) in the Stacks Project.

**`AlgebraicGeometry.weaklyEtale_iff_strictHenselizationMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Stalks.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Stalks.lean#L351).

> A morphism of schemes is weakly étale if and only if every map that it induces between
> compatible strict henselizations of its local rings is an isomorphism.

```lean
theorem weaklyEtale_iff_strictHenselizationMap_bijective
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y) :
    AlgebraicGeometry.WeaklyEtale f ↔
      ∀ (x : X) (Ysh Xsh : Type u)
        [CommRing Ysh] [IsLocalRing Ysh]
        [CommRing Xsh] [IsLocalRing Xsh]
        [Algebra (Y.presheaf.stalk (f x)) Ysh]
        [Algebra (IsLocalRing.ResidueField (Y.presheaf.stalk (f x)))
          (IsLocalRing.ResidueField Ysh)]
        [IsSepClosure (IsLocalRing.ResidueField (Y.presheaf.stalk (f x)))
          (IsLocalRing.ResidueField Ysh)]
        [IsLocalRing.IsHenselization (Y.presheaf.stalk (f x))
          (IsLocalRing.ResidueField Ysh) Ysh]
        [Algebra (X.presheaf.stalk x) Xsh]
        [Algebra (IsLocalRing.ResidueField (X.presheaf.stalk x))
          (IsLocalRing.ResidueField Xsh)]
        [IsSepClosure (IsLocalRing.ResidueField (X.presheaf.stalk x))
          (IsLocalRing.ResidueField Xsh)]
        [IsLocalRing.IsHenselization (X.presheaf.stalk x)
          (IsLocalRing.ResidueField Xsh) Xsh]
        (φ : IsLocalRing.ResidueField Ysh →+* IsLocalRing.ResidueField Xsh)
        (g : Ysh →+* Xsh),
        IsLocalHom g →
          g.comp (algebraMap (Y.presheaf.stalk (f x)) Ysh) =
            (algebraMap (X.presheaf.stalk x) Xsh).comp (f.stalkMap x).hom →
          (IsLocalRing.residue Xsh).comp g =
              φ.comp (IsLocalRing.residue Ysh) →
            Function.Bijective g
```

## Tag 0950, a lemma

[Tag 0950](https://stacks.math.columbia.edu/tag/0950) in the Stacks Project.

**`AlgebraicGeometry.isNormal_of_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Normal.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Normal.lean#L63).

> **Stacks Project, Tag 0950.** A weakly étale morphism with normal target has normal
> source.

```lean
theorem isNormal_of_weaklyEtale {X Y : Scheme.{u}} (f : X ⟶ Y) [IsNormal Y] [WeaklyEtale f] :
    IsNormal X
```

## Tag 0F6V, a lemma

[Tag 0F6V](https://stacks.math.columbia.edu/tag/0F6V) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_weaklyEtale_of_universalHomeomorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Isomorphism.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Isomorphism.lean#L40).

> A weakly étale universal homeomorphism of schemes is an isomorphism.

```lean
instance isIso_of_weaklyEtale_of_universalHomeomorphism
    {X Y : Scheme.{u}} (f : X ⟶ Y) [WeaklyEtale f]
    [UniversalHomeomorphism f] : IsIso f
```

## Tag 0F6W, a lemma

[Tag 0F6W](https://stacks.math.columbia.edu/tag/0F6W) in the Stacks Project.

**`AlgebraicGeometry.isIso_relativeFrobenius_of_weaklyEtale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Isomorphism.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Isomorphism.lean#L67). References: SGA 4½ Fonctions L (3.4), “more general”; SGA 4½ Rapport (1.2), “special case”; SGA 5 XV (1.Proposition2), “more general”.

> The relative Frobenius of a weakly étale scheme is an isomorphism.

```lean
instance isIso_relativeFrobenius_of_weaklyEtale (X : Scheme.{u}) (p : ℕ)
    [Fact p.Prime] (hX : IsInCharacteristic X p) (U : Over X) [WeaklyEtale U.hom] :
    IsIso (relativeFrobenius X p hX U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.64, Tag 094N](https://stacks.math.columbia.edu/tag/094N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
