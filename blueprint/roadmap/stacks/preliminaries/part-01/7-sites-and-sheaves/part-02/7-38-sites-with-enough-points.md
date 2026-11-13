---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.IsConservativeFamily, CategoryTheory.GrothendieckTopology.HasConservativeFamily, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isLimit_iff, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.injective_app_of_forall_injective_sheafFiber_map, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.isLocallySurjective_of_forall_surjective_sheafFiber_map, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.eq_of_forall_sheafFiber_map_eq, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isColimit_iff, CategoryTheory.GrothendieckTopology.isConservativeFamily_iff_exists_toPresheafFiber_ne
statement: formalized
proof: formalized
---

# 7.38 Sites with enough points

Section 7.38 of the Stacks Project, [Tag 00YJ](https://stacks.math.columbia.edu/tag/00YJ). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00YK, a definition

[Tag 00YK](https://stacks.math.columbia.edu/tag/00YK) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsConservativeFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean#L97). The attribute's comment: “(1)”. References: SGA 4 IV (6.4.1), “conservative family”.

> **Stacks 00YK (1).** A family of points `{p_i}_{i ∈ I}` of a site `(C, J)` is *conservative* if
> every map of sheaves of sets `φ : F ⟶ G` which is an isomorphism on all the fibres
> `F_{p_i} ⟶ G_{p_i}` is an isomorphism.

```lean
def IsConservativeFamily {ι : Type t} (p : ι → Point.{w} J) : Prop
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean#L105). The attribute's comment: “(2)”. References: SGA 4 IV (6.4.1), “enough points”.

> **Stacks 00YK (2).** A site `(C, J)` *has enough points* if there exists a conservative family
> of points. No smallness is required of the family; contrast
> `CategoryTheory.GrothendieckTopology.HasEnoughPoints`, which asks for a `w`-small one.

```lean
def HasConservativeFamily (J : GrothendieckTopology C) : Prop
```

## Tag 00YL, a lemma

[Tag 00YL](https://stacks.math.columbia.edu/tag/00YL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isLimit_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L157). The attribute's comment: “(4): a cone over a finite diagram of sheaves is a limit if and only if it is one in every stalk at a conservative family of points.”.

> **Stacks 00YL (4).** Let `(C, J)` be a site and let `P` be a conservative family of points of
> it. Let `G : K ⥤ Sh(C)` be a finite diagram of sheaves with values in `A`. Then a cone over `G` is
> a limit if and only if its image under every stalk functor `F ↦ F_{p_i}`, `p_i ∈ P`, is a limit.

```lean
public theorem nonempty_isLimit_iff {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {P : ObjectProperty (GrothendieckTopology.Point.{w} J)}
    (hP : P.IsConservativeFamilyOfPoints) {A : Type u'} [Category.{v'} A] [LocallySmall.{w} C]
    [HasColimitsOfSize.{w, w} A] [HasFiniteLimits A] [AB5OfSize.{w, w} A]
    {FC : A → A → Type*} {CC : A → Type w}
    [∀ X Y : A, FunLike (FC X Y) (CC X) (CC Y)] [ConcreteCategory.{w} A FC]
    [(forget A).ReflectsIsomorphisms] [PreservesFilteredColimitsOfSize.{w, w} (forget A)]
    [J.HasSheafCompose (forget A)]
    {K : Type u''} [SmallCategory K] [FinCategory K] {G : K ⥤ Sheaf J A} (c : Cone G) :
    Nonempty (IsLimit c) ↔
      ∀ Φ : P.FullSubcategory, Nonempty (IsLimit ((Φ.obj.sheafFiber (A := A)).mapCone c))
```

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.injective_app_of_forall_injective_sheafFiber_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L176). The attribute's comment: “(1): a map of sheaves of sets which is injective on the stalks at a conservative family of points is injective.”.

> **Stacks 00YL (1).** Let `(C, J)` be a site and let `P` be a conservative family of points of
> it. Let `φ : F ⟶ G` be a map of sheaves of sets. If every stalk map `φ_{p_i}`, `p_i ∈ P`, is
> injective, then `φ` is injective, that is, injective on the sections over every object `U`
> (Stacks 00WM (1)).

```lean
public theorem injective_app_of_forall_injective_sheafFiber_map {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {P : ObjectProperty (GrothendieckTopology.Point.{w} J)}
    (hP : P.IsConservativeFamilyOfPoints) [LocallySmall.{w} C] {F G : Sheaf J (Type w)}
    (φ : F ⟶ G)
    (h : ∀ Φ : P.FullSubcategory, Function.Injective (Φ.obj.sheafFiber.map φ)) (U : Cᵒᵖ) :
    Function.Injective (φ.hom.app U)
```

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.isLocallySurjective_of_forall_surjective_sheafFiber_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L194). The attribute's comment: “(2): a map of sheaves of sets which is surjective on the stalks at a conservative family of points is surjective.”.

> **Stacks 00YL (2).** Let `(C, J)` be a site and let `P` be a conservative family of points of
> it. Let `φ : F ⟶ G` be a map of sheaves of sets. If every stalk map `φ_{p_i}`, `p_i ∈ P`, is
> surjective, then `φ` is surjective, that is, every section of `G` is locally in the image of `φ`
> (Stacks 00WM (2); `CategoryTheory.Sheaf.IsLocallySurjective`).

```lean
public theorem isLocallySurjective_of_forall_surjective_sheafFiber_map {C : Type u}
    [Category.{v} C] {J : GrothendieckTopology C}
    {P : ObjectProperty (GrothendieckTopology.Point.{w} J)}
    (hP : P.IsConservativeFamilyOfPoints) [LocallySmall.{w} C] [HasSheafify J (Type w)]
    {F G : Sheaf J (Type w)} (φ : F ⟶ G)
    (h : ∀ Φ : P.FullSubcategory, Function.Surjective (Φ.obj.sheafFiber.map φ)) :
    Sheaf.IsLocallySurjective φ
```

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.eq_of_forall_sheafFiber_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L211). The attribute's comment: “(3): two maps of sheaves which agree on the stalks at a conservative family of points are equal.”.

> **Stacks 00YL (3).** Let `(C, J)` be a site and let `P` be a conservative family of points of
> it. Two maps of sheaves `φ₁ φ₂ : F ⟶ G` which agree on the stalks at every `p_i ∈ P` are
> equal.

```lean
public theorem eq_of_forall_sheafFiber_map_eq {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {P : ObjectProperty (GrothendieckTopology.Point.{w} J)}
    (hP : P.IsConservativeFamilyOfPoints) {A : Type u'} [Category.{v'} A] [LocallySmall.{w} C]
    [HasColimitsOfSize.{w, w} A] [HasFiniteLimits A] [AB5OfSize.{w, w} A]
    {FC : A → A → Type*} {CC : A → Type w}
    [∀ X Y : A, FunLike (FC X Y) (CC X) (CC Y)] [ConcreteCategory.{w} A FC]
    [(forget A).ReflectsIsomorphisms] [PreservesFilteredColimitsOfSize.{w, w} (forget A)]
    [J.HasSheafCompose (forget A)] {F G : Sheaf J A} {φ₁ φ₂ : F ⟶ G}
    (h : ∀ Φ : P.FullSubcategory, Φ.obj.sheafFiber.map φ₁ = Φ.obj.sheafFiber.map φ₂) :
    φ₁ = φ₂
```

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isColimit_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L229). The attribute's comment: “(5): a cocone under a finite diagram of sheaves is a colimit if and only if it is one in every stalk at a conservative family of points.”.

> **Stacks 00YL (5).** Let `(C, J)` be a site and let `P` be a conservative family of points of
> it. Let `G : K ⥤ Sh(C)` be a finite diagram of sheaves with values in `A`. Then a cocone under `G`
> is a colimit if and only if its image under every stalk functor `F ↦ F_{p_i}`, `p_i ∈ P`, is a
> colimit.

```lean
public theorem nonempty_isColimit_iff {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {P : ObjectProperty (GrothendieckTopology.Point.{w} J)}
    (hP : P.IsConservativeFamilyOfPoints) {A : Type u'} [Category.{v'} A] [LocallySmall.{w} C]
    [HasColimitsOfSize.{w, w} A] [HasWeakSheafify J A] [HasProducts.{w} A]
    {FC : A → A → Type*} {CC : A → Type w}
    [∀ X Y : A, FunLike (FC X Y) (CC X) (CC Y)] [ConcreteCategory.{w} A FC]
    [(forget A).ReflectsIsomorphisms] [PreservesFilteredColimitsOfSize.{w, w} (forget A)]
    [J.HasSheafCompose (forget A)]
    {K : Type u''} [SmallCategory K] [FinCategory K] {G : K ⥤ Sheaf J A} (c : Cocone G) :
    Nonempty (IsColimit c) ↔
      ∀ Φ : P.FullSubcategory, Nonempty (IsColimit ((Φ.obj.sheafFiber (A := A)).mapCocone c))
```

## Tag 00YM, a lemma

[Tag 00YM](https://stacks.math.columbia.edu/tag/00YM) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.isConservativeFamily_iff_exists_toPresheafFiber_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SeparatingGerms.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SeparatingGerms.lean#L158).

> **Stacks 00YM.** Let `(C, J)` be a site and `{p_i}_{i ∈ I}` a family of points. The family is
> conservative if and only if for every sheaf of sets `F`, every object `U` of `C` and every pair of
> distinct sections `s ≠ s'` of `F` over `U`, there are an index `i` and `x ∈ u_i(U)` such that the
> triples `(U, x, s)` and `(U, x, s')` define distinct elements of the stalk `F_{p_i}`; that element
> is the germ `(p i).toPresheafFiber U x F.obj s`.

```lean
theorem isConservativeFamily_iff_exists_toPresheafFiber_ne {ι : Type t}
    (p : ι → Point.{w} J) :
    IsConservativeFamily p ↔
      ∀ (F : Sheaf J (Type w)) (U : C) (s s' : F.obj.obj (op U)), s ≠ s' →
        ∃ (i : ι) (x : (p i).fiber.obj U),
          (p i).toPresheafFiber U x F.obj s ≠ (p i).toPresheafFiber U x F.obj s'
```

## Tag 04H6, a lemma

[Tag 04H6](https://stacks.math.columbia.edu/tag/04H6) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsConservativeFamily.over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean#L97).

> **Stacks 04H6.** Let `{p_i}_{i ∈ I}` be a conservative family of points of a site `(C, J)`,
> with fibre functors `u_i`, and let `X` be an object of `C`. Then the points
> `q_{i,x} = (p i).over x` of the localized site `C/X` of Stacks 04H2, for `i ∈ I` and
> `x ∈ u_i(X)`, form a conservative family of points of `C/X`.

```lean
theorem IsConservativeFamily.over {ι : Type t} {p : ι → Point.{w} J}
    (hp : IsConservativeFamily p) (X : C) [HasSheafify (J.over X) (Type w)] :
    IsConservativeFamily (fun ix : Σ i, (p i).fiber.obj X ↦ (p ix.1).over ix.2)
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily.over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean#L114). The attribute's comment: “in particular”.

> **Stacks 04H6**, the "in particular": if a site `(C, J)` has enough points, i.e. a
> conservative family of points (Stacks 00YK (2)), then so does every localization `C/X`.

```lean
theorem HasConservativeFamily.over (h : HasConservativeFamily.{w} J) (X : C)
    [HasSheafify (J.over X) (Type w)] : HasConservativeFamily.{w} (J.over X)
```

## Tag 06UL, a lemma

[Tag 06UL](https://stacks.math.columbia.edu/tag/06UL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean#L95). References: SGA 4 IV (6.7.4), “second assertion”; SGA 4 IV (6.7.3), “converse direction”.

> **Stacks 06UL**, the conservativity step. If the `U_i` cover the final object and each
> `P i` is a conservative family of points of `C/U_i`, then the pushed-forward family
> `pointsOfLocalizations` is a conservative family of points of `C`.

```lean
theorem ObjectProperty.IsConservativeFamilyOfPoints.of_coversTop
    (hU : J.CoversTop Ui) (hP : ∀ i, (P i).IsConservativeFamilyOfPoints) :
    (GrothendieckTopology.pointsOfLocalizations Ui P).IsConservativeFamilyOfPoints
```

**`CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean#L113). References: SGA 4 IV (6.7.3), “converse”; SGA 4 IV (6.7.4), “second assertion”.

> **Stacks 06UL.** Let `C` be a site and `{U_i}_{i ∈ I}` a family of objects such that
> the `U_i` cover the final object (hypothesis (1), see the module docstring) and each
> localization `C/U_i` has enough points (hypothesis (2)). Then `C` has enough points.

```lean
theorem GrothendieckTopology.hasEnoughPoints_of_coversTop [Small.{w} I]
    (hU : J.CoversTop Ui) [∀ i, HasEnoughPoints.{w} (J.over (Ui i))] :
    HasEnoughPoints.{w} J
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily.of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyLocality.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyLocality.lean#L51).

> **Stacks 06UL** for `CategoryTheory.GrothendieckTopology.HasConservativeFamily`. If a family
> of objects covers the final object and each localization at a member of the family has a
> conservative family of points, then so does the site itself.

```lean
theorem HasConservativeFamily.of_coversTop (hU : J.CoversTop Ui)
    (hP : ∀ i, (J.over (Ui i)).HasConservativeFamily.{w}) :
    J.HasConservativeFamily.{w}
```

## Tag 0F4G, a lemma

[Tag 0F4G](https://stacks.math.columbia.edu/tag/0F4G) in the Stacks Project.

**`CategoryTheory.Functor.isMorphismOfSites_of_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Exactness.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Exactness.lean#L135).

> **Stacks 0F4G.** Let `u : C ⥤ D` be a continuous functor of sites. Let `{(q_i, v_i)}`
> be a conservative family of points of `D`. If each functor `u_i = v_i ∘ u` defines a point
> of `C`, then `u` defines a morphism of sites `f : D → C`.

```lean
theorem isMorphismOfSites_of_points
    (hP : P.IsConservativeFamilyOfPoints)
    (Ψ : P.FullSubcategory → Point.{u} J)
    (hΨ : ∀ Φ : P.FullSubcategory, (Ψ Φ).fiber = u ⋙ Φ.obj.fiber) :
    u.IsMorphismOfSites J K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.38, Tag 00YJ](https://stacks.math.columbia.edu/tag/00YJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
