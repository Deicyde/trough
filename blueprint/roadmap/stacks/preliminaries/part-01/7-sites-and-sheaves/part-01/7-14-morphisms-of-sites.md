---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsMorphismOfSites, StacksZariskiSite.topPushforward_eq_sheafPushforwardContinuous, StacksZariskiSite.topPullback_eq_sheafPullback, StacksZariskiSite.topAdjunction_eq_sheafAdjunctionContinuous, StacksZariskiSite.isMorphismOfSites_opensMap, isMorphismOfSites_comp, CategoryTheory.Functor.IsMorphismOfSites.comp, isMorphismOfSites_of_essentiallySmall
statement: formalized
proof: formalized
---

# 7.14 Morphisms of sites

Section 7.14 of the Stacks Project, [Tag 00X0](https://stacks.math.columbia.edu/tag/00X0). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00X1, a definition

[Tag 00X1](https://stacks.math.columbia.edu/tag/00X1) in the Stacks Project.

**`CategoryTheory.Functor.IsMorphismOfSites`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean#L78). The tag is given by the `attribute` command at [StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean#L91). The attribute's comment: “A morphism of sites is a continuous functor in the opposite direction whose induced functor `u_s` on sheaves of sets is exact.”. References: SGA 4 IV (4.9.1); SGA 4 IV (4.9), “morphism of sites def”.

> A *morphism of sites* `f : D → C` between the sites `(C, J)` and `(D, K)` is given by a
> functor `u : C ⥤ D` in the opposite direction which is continuous and whose induced functor on
> sheaves of sets `u_s = f⁻¹ : Sh(C) ⥤ Sh(D)` is exact, i.e. preserves both finite limits and
> finite colimits. Here `u_s` is `Functor.sheafPullback`, the left adjoint of the pushforward
> `u^s = f_* = Functor.sheafPushforwardContinuous`.

```lean
structure IsMorphismOfSites (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) : Prop
```

## Tag 00X2, an example

[Tag 00X2](https://stacks.math.columbia.edu/tag/00X2) in the Stacks Project.

**`StacksZariskiSite.topPushforward_eq_sheafPushforwardContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean#L45).

> **Stacks 00X2.** The site-theoretic pushforward `u^s` along `u = Opens.map f` is the usual
> topological pushforward `f_*` on sheaves of sets: Mathlib's `TopCat.Sheaf.pushforward` is defined
> to be precisely `(Opens.map f).sheafPushforwardContinuous`, so the identification asserted by the
> example holds on the nose.

```lean
theorem topPushforward_eq_sheafPushforwardContinuous :
    TopCat.Sheaf.pushforward (Type u) f =
      (Opens.map f).sheafPushforwardContinuous (Type u) (Opens.grothendieckTopology Y)
        (Opens.grothendieckTopology X)
```

**`StacksZariskiSite.topPullback_eq_sheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean#L54).

> **Stacks 00X2.** The site-theoretic pullback `u_s` along `u = Opens.map f` is the usual
> topological pullback `f⁻¹` on sheaves of sets.

```lean
theorem topPullback_eq_sheafPullback :
    TopCat.Sheaf.pullback (Type u) f =
      (Opens.map f).sheafPullback (Type u) (Opens.grothendieckTopology Y)
        (Opens.grothendieckTopology X)
```

**`StacksZariskiSite.topAdjunction_eq_sheafAdjunctionContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean#L64).

> **Stacks 00X2.** Consequently the topological adjunction `f⁻¹ ⊣ f_*` is the site-theoretic
> adjunction `u_s ⊣ u^s`; this is the step by which the example concludes `f⁻¹ ≅ u_s` from
> uniqueness of adjoints.

```lean
theorem topAdjunction_eq_sheafAdjunctionContinuous :
    TopCat.Sheaf.pullbackPushforwardAdjunction (Type u) f =
      (Opens.map f).sheafAdjunctionContinuous (Type u) (Opens.grothendieckTopology Y)
        (Opens.grothendieckTopology X)
```

**`StacksZariskiSite.isMorphismOfSites_opensMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/TopologicalComparison.lean#L83). References: SGA 4 IV (4.1.1), “morphism of topoi Top(f)”; SGA 4 III (1.9.1), “continuity of f^{-1}”.

> **Stacks 00X2.** The functor `u = Opens.map f : Y_Zar ⥤ X_Zar`, `V ↦ f⁻¹(V)`, defines a
> morphism of sites `X_Zar → Y_Zar`: it is continuous, and the induced pullback `u_s = f⁻¹` on
> sheaves of sets is exact.
>
> Continuity is Mathlib's instance for `Opens.map f` and the Zariski topologies.  For exactness the
> example argues that `u_s ≅ f⁻¹` is exact because `f⁻¹` is; here it is obtained from the criterion
> of Stacks 00X5 (`CategoryTheory.Functor.isMorphismOfSites_of_representablyFlat`), whose hypothesis
> `RepresentablyFlat (Opens.map f)` holds because the categories `I_V^u` of Stacks 00VC are the
> lattices of open `W ⊆ Y` with `V ⊆ f⁻¹(W)`, which are closed under intersection and contain
> `W = Y`.

```lean
theorem isMorphismOfSites_opensMap :
    (Opens.map f).IsMorphismOfSites (Opens.grothendieckTopology Y)
      (Opens.grothendieckTopology X)
```

## Tag 03CB, a lemma

[Tag 03CB](https://stacks.math.columbia.edu/tag/03CB) in the Stacks Project.

**`isMorphismOfSites_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/MorphismDefs.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/MorphismDefs.lean#L42).

> **Stacks 03CB.** If `v : C₃ ⥤ C₂` and `u : C₂ ⥤ C₁` are continuous functors defining
> morphisms of sites, then so is `v ⋙ u`: the left adjoints compose, and a composition of left
> exact functors is left exact.

```lean
theorem isMorphismOfSites_comp
    {C₁ C₂ C₃ : Type*} [Category C₁] [Category C₂] [Category C₃]
    (J₁ : GrothendieckTopology C₁) (J₂ : GrothendieckTopology C₂)
    (J₃ : GrothendieckTopology C₃)
    (v : C₃ ⥤ C₂) (u : C₂ ⥤ C₁)
    [IsMorphismOfSites.{w} v J₃ J₂] [IsMorphismOfSites.{w} u J₂ J₁] :
    IsMorphismOfSites.{w} (v ⋙ u) J₃ J₁
```

## Tag 03CC, a definition

[Tag 03CC](https://stacks.math.columbia.edu/tag/03CC) in the Stacks Project.

**`CategoryTheory.Functor.IsMorphismOfSites.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites.lean#L133). The attribute's comment: “The composition of two morphisms of sites is a morphism of sites, given by the composite of the two underlying continuous functors; this is what makes the composition of Stacks 03CC well defined.”.

> The *composition* of morphisms of sites. If `f : D → C` is a morphism of sites given by
> `u : C ⥤ D` and `g : E → D` is one given by `u' : D ⥤ E`, then the composite functor
> `u ⋙ u' : C ⥤ E` is again continuous with exact induced functor on sheaves of sets, so it defines
> a morphism of sites `E → C`, the composition `f ∘ g`.

```lean
theorem IsMorphismOfSites.comp {u : C ⥤ D} {u' : D ⥤ E} {J : GrothendieckTopology C}
    {K : GrothendieckTopology D} {L : GrothendieckTopology E}
    (h : u.IsMorphismOfSites J K) (h' : u'.IsMorphismOfSites K L) :
    (u ⋙ u').IsMorphismOfSites J L
```

## Tag 00X5, a lemma

[Tag 00X5](https://stacks.math.columbia.edu/tag/00X5) in the Stacks Project.

**`isMorphismOfSites_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/SmallModel.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/SmallModel.lean#L173). The attribute's comment: “the site condition at the universe of a small model”.

> **Stacks 00X5 at the universe of a small model.**  A continuous representably flat functor
> between two sites that are essentially small at `u` defines a morphism of sites for sheaves of
> sets valued in `Type u`, one universe below the objects of the sites.
>
> The left exact left adjoint of the direct image is the pullback along the transported functor on
> the small models, which is left exact by Stacks 00X5 at the universe of a genuinely small site,
> conjugated by the two restriction equivalences along the comparisons with the small models.

```lean
public theorem isMorphismOfSites_of_essentiallySmall (F : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) [F.IsContinuous J K] [RepresentablyFlat F] :
    IsMorphismOfSites.{u} F J K
```

**`CategoryTheory.Functor.isMorphismOfSites_of_isFiltered_op`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSitesLimits.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSitesLimits.lean#L82). The attribute's comment: “A continuous functor all of whose index categories `(I_V^u)ᵒᵖ` are filtered defines a morphism of sites; equivalently a continuous representably flat functor does.”.

> Let `u : C ⥤ D` be a continuous functor between sites and assume that all the
> categories `(I_V^u)ᵒᵖ` of Stacks 00VC are filtered. Then `u` defines a morphism of sites `D → C`,
> in other words `u_s` is exact.

```lean
theorem isMorphismOfSites_of_isFiltered_op (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) [u.IsContinuous J K]
    (h : ∀ V : D, IsFiltered (StructuredArrow V u)ᵒᵖ) : u.IsMorphismOfSites J K
```

## Tag 00X6, a proposition

[Tag 00X6](https://stacks.math.columbia.edu/tag/00X6) in the Stacks Project.

**`CategoryTheory.Functor.isMorphismOfSites_of_isTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSitesLimits.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSitesLimits.lean#L107). The attribute's comment: “A continuous functor `u` such that `C` has a final object sent by `u` to a final object and has fibre products preserved by `u` defines a morphism of sites; this is the criterion under which `u` induces a morphism of topoi with exact pullback.”. References: SGA 4 IV (4.9.2), “sufficient condition”; SGA 4 III (1.3), “5)”.

> Let `u : C ⥤ D` be a continuous functor between sites. Assume furthermore that
>
> 1. the category `C` has a final object `X` and `u(X)` is a final object of `D`, and
> 2. the category `C` has fibre products and `u` commutes with them.
>
> Then `u` defines a morphism of sites `D → C`, in other words `u_s` is exact.

```lean
theorem isMorphismOfSites_of_isTerminal (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) [u.IsContinuous J K] [HasPullbacks C]
    [PreservesLimitsOfShape WalkingCospan u] {X : C} (hX : IsTerminal X)
    (huX : IsTerminal (u.obj X)) : u.IsMorphismOfSites J K
```

## Tag 00X7, a remark

[Tag 00X7](https://stacks.math.columbia.edu/tag/00X7) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.preservesFiniteLimits_of_preservesTerminal_and_pullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.preservesFiniteLimits_of_preservesTerminal_and_pullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L36) (StacksFrontier): “If the category has a final object and fibre products, a functor preserving the final object and fibre products is left exact (preserves finite limits).”. References: SGA 4 I (2.4.2), “sufficiency”.
- [`CategoryTheory.Limits.PreservesFiniteLimits.preservesFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.PreservesFiniteLimits.preservesFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L39) (StacksFrontier): “Conversely, a left exact functor preserves limits of every finite shape, in particular final objects and fibre products.”.

## Tag 00X8, a remark

[Tag 00X8](https://stacks.math.columbia.edu/tag/00X8) in the Stacks Project.

**`QuasiMorphismOfSites.IsQuasiMorphismOfSites`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/QuasiMorphism.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/QuasiMorphism.lean#L360). The attribute's comment: “the definition of quasi-morphism of sites”.

> **Definition 5 (Quasi-morphism of sites).** Given a quasi-continuous functor
> `u : C → D` (witnessed by `hqc`), `u` defines a quasi-morphism of sites
> `f : D → C` if the induced left adjoint `u_s : Sh(C) → Sh(D)` on set-valued
> sheaves is exact. The continuity instance needed to form
> `u_s = u.sheafPullback` is derived from `hqc` via Background Lemma A, not
> assumed.

```lean
def IsQuasiMorphismOfSites
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D]
    [HasPullbacks C] [HasPullbacks D] (u : C ⥤ D)
    (PC : Pretopology C) (PD : Pretopology D)
    (hqc : IsQuasiContinuous u PC PD) : Prop
```

**`QuasiMorphismOfSites.isQuasiMorphismOfSites_of_isQuasiContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/QuasiMorphism.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/QuasiMorphism.lean#L394).

> **Statement 1.** A quasi-continuous functor `u : C → D` between sites that
> preserves the terminal object and preserves fibre products (pullbacks) defines a
> quasi-morphism of sites: the induced functor `u_s : Sh(C) → Sh(D)` on set-valued
> sheaves is exact. Continuity is derived internally from quasi-continuity via
> Background Lemma A and is not assumed.

```lean
theorem isQuasiMorphismOfSites_of_isQuasiContinuous
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D]
    [HasPullbacks C] [HasPullbacks D] [HasTerminal C]
    (u : C ⥤ D) (PC : Pretopology C) (PD : Pretopology D)
    (hqc : IsQuasiContinuous u PC PD)
    -- Hypothesis (1): `u` sends the final object of `C` to a final object of `D`.
    (hterminal : PreservesLimitsOfShape (Discrete PEmpty.{1}) u)
    -- Hypothesis (2): `u` commutes with fibre products.
    (hpullbacks : PreservesLimitsOfShape WalkingCospan u) :
    IsQuasiMorphismOfSites u PC PD hqc
```

## Tag 08H2, a lemma

[Tag 08H2](https://stacks.math.columbia.edu/tag/08H2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.coversTop_obj_of_preservesTerminal_sheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/MorphismsOfSites.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/MorphismsOfSites.lean#L222). The attribute's comment: “For a morphism of sites f : D → C given by u : C ⥤ D, every object V of D has a covering {V_j → V} such that each V_j admits a morphism V_j ⟶ u(U_j) for some object U_j of C.”.

> **Stacks 08H2.** Let `u : C ⥤ D` be a continuous functor of sites, giving a morphism of sites
> `f : D → C`, and assume that `f⁻¹ = u_s : Sh(C) ⥤ Sh(D)` preserves the final object (as it does
> when `u_s` is exact, i.e. when `u` defines a morphism of sites, Stacks 00X1). Then the objects
> `u U`, for `U` an object of `C`, cover the final object of `Sh(D)`: for every object `V` of `D`
> there is a covering `{V_j → V}` such that every `V_j` admits a morphism `V_j ⟶ u U_j` to the
> image of some object `U_j` of `C`.

```lean
public theorem coversTop_obj_of_preservesTerminal_sheafPullback {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) [u.IsContinuous J K]
    [PreservesLimit (Functor.empty.{0} (Sheaf J (Type u))) (u.sheafPullback (Type u) J K)] :
    K.CoversTop u.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.14, Tag 00X0](https://stacks.math.columbia.edu/tag/00X0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
