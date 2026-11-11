---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.IsConservativeFamily, CategoryTheory.GrothendieckTopology.HasConservativeFamily, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isLimit_iff, stalkSet_map_germ, CategoryTheory.GrothendieckTopology.IsConservativeFamily.over, CategoryTheory.GrothendieckTopology.HasConservativeFamily.over, CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.of_coversTop, CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_coversTop
statement: formalized
proof: formalized
---

# 7.38 Sites with enough points

Section 7.38 of the Stacks Project, [Tag 00YJ](https://stacks.math.columbia.edu/tag/00YJ). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00YK, a definition

[Tag 00YK](https://stacks.math.columbia.edu/tag/00YK) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsConservativeFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean#L97). The attribute's comment: “(1)”. References: SGA 4 IV (6.4.1), “conservative family”.

> **Stacks 00YK (1).** A family of points `{p_i}_{i ∈ I}` of a site `(C, J)` is *conservative* if
> every map of sheaves of sets `φ : F ⟶ G` which is an isomorphism on all the fibres
> `F_{p_i} ⟶ G_{p_i}` is an isomorphism.

```lean
def IsConservativeFamily {ι : Type t} (p : ι → Point.{w} J) : Prop
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamily.lean#L105). The attribute's comment: “(2)”. References: SGA 4 IV (6.4.1), “enough points”.

> **Stacks 00YK (2).** A site `(C, J)` *has enough points* if there exists a conservative family
> of points. No smallness is required of the family; contrast
> `CategoryTheory.GrothendieckTopology.HasEnoughPoints`, which asks for a `w`-small one.

```lean
def HasConservativeFamily (J : GrothendieckTopology C) : Prop
```

## Tag 00YL, a lemma

[Tag 00YL](https://stacks.math.columbia.edu/tag/00YL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.nonempty_isLimit_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SitesWithEnoughPoints.lean#L141). The attribute's comment: “(4): a cone over a finite diagram of sheaves is a limit if and only if it is one in every stalk at a conservative family of points.”.

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

## Tag 00YM, a lemma

[Tag 00YM](https://stacks.math.columbia.edu/tag/00YM) in the Stacks Project.

**`stalkSet_map_germ`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/GermNaturality.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/GermNaturality.lean#L169).

> **Germ naturality (narrowed substantiation).**
>
> For distinct sections `s ≠ s' ∈ F(U)`, the Stacks argument identifies
> an index `i` and a point `x ∈ u_i(U)` separating their germs in the
> stalk at `p_i`. The "Unwinding the definitions" step rests on the
> identity below: pushing a germ00YM along a sheaf morphism agrees with the
> germ00YM of the pushed section. The remaining categorical packaging
> (equalizer of representable maps, etc.) is deferred.

```lean
lemma stalkSet_map_germ {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (P : C ⥤ Type u)
    [P.IsContinuous J (GrothendieckTopology.trivial (Type u))]
    [(P.sheafPushforwardContinuous (Type u) J
        (GrothendieckTopology.trivial (Type u))).IsRightAdjoint]
    {F G : Sheaf J (Type u)} (φ : F ⟶ G) (U : C)
    (s : F.obj.obj (Opposite.op U)) (x : P.obj U) :
    (stalkSet J P).map φ (germ00YM J P F U s x)
      = germ00YM J P G U (φ.hom.app (Opposite.op U) s) x
```

## Tag 04H6, a lemma

[Tag 04H6](https://stacks.math.columbia.edu/tag/04H6) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsConservativeFamily.over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean#L97).

> **Stacks 04H6.** Let `{p_i}_{i ∈ I}` be a conservative family of points of a site `(C, J)`,
> with fibre functors `u_i`, and let `X` be an object of `C`. Then the points
> `q_{i,x} = (p i).over x` of the localized site `C/X` of Stacks 04H2, for `i ∈ I` and
> `x ∈ u_i(X)`, form a conservative family of points of `C/X`.

```lean
theorem IsConservativeFamily.over {ι : Type t} {p : ι → Point.{w} J}
    (hp : IsConservativeFamily p) (X : C) [HasSheafify (J.over X) (Type w)] :
    IsConservativeFamily (fun ix : Σ i, (p i).fiber.obj X ↦ (p ix.1).over ix.2)
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily.over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyOver.lean#L114). The attribute's comment: “in particular”.

> **Stacks 04H6**, the "in particular": if a site `(C, J)` has enough points, i.e. a
> conservative family of points (Stacks 00YK (2)), then so does every localization `C/X`.

```lean
theorem HasConservativeFamily.over (h : HasConservativeFamily.{w} J) (X : C)
    [HasSheafify (J.over X) (Type w)] : HasConservativeFamily.{w} (J.over X)
```

## Tag 06UL, a lemma

[Tag 06UL](https://stacks.math.columbia.edu/tag/06UL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean#L95). References: SGA 4 IV (6.7.4), “second assertion”; SGA 4 IV (6.7.3), “converse direction”.

> **Stacks 06UL**, the conservativity step. If the `U_i` cover the final object and each
> `P i` is a conservative family of points of `C/U_i`, then the pushed-forward family
> `pointsOfLocalizations` is a conservative family of points of `C`.

```lean
theorem ObjectProperty.IsConservativeFamilyOfPoints.of_coversTop
    (hU : J.CoversTop Ui) (hP : ∀ i, (P i).IsConservativeFamilyOfPoints) :
    (GrothendieckTopology.pointsOfLocalizations Ui P).IsConservativeFamilyOfPoints
```

**`CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Conservative.lean#L113). References: SGA 4 IV (6.7.3), “converse”; SGA 4 IV (6.7.4), “second assertion”.

> **Stacks 06UL.** Let `C` be a site and `{U_i}_{i ∈ I}` a family of objects such that
> the `U_i` cover the final object (hypothesis (1), see the module docstring) and each
> localization `C/U_i` has enough points (hypothesis (2)). Then `C` has enough points.

```lean
theorem GrothendieckTopology.hasEnoughPoints_of_coversTop [Small.{w} I]
    (hU : J.CoversTop Ui) [∀ i, HasEnoughPoints.{w} (J.over (Ui i))] :
    HasEnoughPoints.{w} J
```

**`CategoryTheory.GrothendieckTopology.HasConservativeFamily.of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyLocality.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ConservativeFamilyLocality.lean#L51).

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

**`CategoryTheory.Functor.isMorphismOfSites_of_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Exactness.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/Exactness.lean#L135).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
