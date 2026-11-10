---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.extensionByZeroSets, Stacks.EtaleCohomology.extensionByZeroSetsAdj, Stacks.EtaleCohomology.extensionByZero, Stacks.EtaleCohomology.extensionByZeroAdj, AlgebraicGeometry.abelianExtensionByZero, AlgebraicGeometry.abelianExtensionByZeroAdjunction, AlgebraicGeometry.moduleExtensionByZeroAdjunction, AlgebraicGeometry.moduleOpenExtensionByZeroAdjunction
statement: formalized
proof: formalized
---

# 59.70 Extension by zero

Section 59.70 of the Stacks Project, [Tag 03S2](https://stacks.math.columbia.edu/tag/03S2). 10 tags here are carried by 51 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03S3, a definition

[Tag 03S3](https://stacks.math.columbia.edu/tag/03S3) in the Stacks Project.

**`Stacks.EtaleCohomology.extensionByZeroSets`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean#L308). The attribute's comment: “sets: the left adjoint of restriction”.

> **Stacks Project, Tag 03S3 (1).** Extension by zero `j_!^{Sh}` on sheaves of sets of the
> small étale sites of an étale morphism `j : U ⟶ X`: the left adjoint of restriction, realised as
> the sheafification of the left Kan extension along composition with `j`.

```lean
abbrev extensionByZeroSets :
    Sheaf U.smallEtaleTopology (Type (max (u + 1) v)) ⥤
      Sheaf X.smallEtaleTopology (Type (max (u + 1) v))
```

**`Stacks.EtaleCohomology.extensionByZeroSetsAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean#L317). The attribute's comment: “sets: the left adjoint of restriction”.

> **Stacks Project, Tag 03S3 (1).** Extension by zero is left adjoint to restriction, on
> sheaves of sets.

```lean
def extensionByZeroSetsAdj :
    extensionByZeroSets.{u, v} j ⊣ etaleRestrictionSets.{u, v} j
```

**`Stacks.EtaleCohomology.extensionByZero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean#L351). The attribute's comment: “abelian: the left adjoint of restriction”.

> **Stacks Project, Tag 03S3 (2).** Extension by zero `j_!` on abelian sheaves of the small
> étale sites of an étale morphism `j : U ⟶ X`: the left adjoint of restriction, realised as the
> sheafification of the left Kan extension along composition with `j`.

```lean
abbrev extensionByZero [HasSheafify X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}] :
    Sheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} ⥤
      Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}
```

**`Stacks.EtaleCohomology.extensionByZeroAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Basic.lean#L360). The attribute's comment: “abelian: the left adjoint of restriction”.

> **Stacks Project, Tag 03S3 (2).** Extension by zero is left adjoint to restriction, on
> abelian sheaves.

```lean
def extensionByZeroAdj [HasSheafify X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}] :
    extensionByZero.{u, v} j ⊣ etaleRestriction.{u, v} j
```

**`AlgebraicGeometry.abelianExtensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean#L91). The attribute's comment: “abelian\_extension\_by\_zero”.

> **Stacks 03S3, part (2).** Extension by zero of abelian étale sheaves along the étale
> morphism `U ⟶ X`: the sheafification of `V ↦ ⨁_{V → U} F(V → U)`, realised as the sheaf
> pullback of the continuous site functor `AlgebraicGeometry.smallEtalePostcompose`.

```lean
public def abelianExtensionByZero :
    Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
        AddCommGrpCat.{u + 1} ⥤
      Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.abelianExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean#L106). The attribute's comment: “abelian\_extension\_by\_zero”. References: SGA 4 XVII (6.2.11), “f\_! ⊣ f^* (abelian)”; SGA 4 IV (11.3.1), “étale site, Ab”.

> **Stacks 03S3, part (2).** Extension by zero is left adjoint to restriction, which is
> the property characterising it.

```lean
public def abelianExtensionByZeroAdjunction :
    abelianExtensionByZero B X hX U ⊣ abelianRestriction B X hX U
```

**`AlgebraicGeometry.moduleExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Adjunction.lean#L171). The attribute's comment: “module\_extension\_by\_zero”. References: SGA 4 XVII (6.2.11), “f\_! ⊣ f^* (Λ-modules)”; SGA 4 IV (11.3.1), “étale site, Λ-modules”.

> **Stacks 03S3, part (3).** Extension by zero of sheaves of modules is left adjoint to
> restriction.

```lean
public def moduleExtensionByZeroAdjunction :
    moduleExtensionByZero B X hX U Λ ⊣ moduleRestriction B X hX U Λ
```

**`AlgebraicGeometry.moduleOpenExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/OpenImmersion.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/OpenImmersion.lean#L147). The attribute's comment: “module\_extension\_by\_zero”.

> Extension by zero along an open immersion is left adjoint to restriction.

```lean
public def moduleOpenExtensionByZeroAdjunction
    [HasWeakSheafify (SmallEtale.topology B X hX) (ModuleCat.{w} Λ)] :
    moduleOpenExtensionByZero B X hX U Λ ⊣ moduleRestriction B X hX U Λ
```

**`AlgebraicGeometry.setExtensionByEmpty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Sets.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Sets.lean#L85). The attribute's comment: “sheaves\_of\_sets”.

> **Stacks 03S3, part (1).** Extension by the empty set of étale sheaves of sets along the
> étale morphism `U ⟶ X`: the sheafification of `V ↦ ⨿_{V → U} F(V → U)`, realised as the sheaf
> pullback of the continuous site functor `AlgebraicGeometry.smallEtalePostcompose`.

```lean
public def setExtensionByEmpty :
    Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
        (Type (max (u + 1) v)) ⥤
      Sheaf (SmallEtale.topology B X hX) (Type (max (u + 1) v))
```

**`AlgebraicGeometry.setExtensionByEmptyAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Sets.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Sets.lean#L99). The attribute's comment: “sheaves\_of\_sets”.

> **Stacks 03S3, part (1).** Restriction of étale sheaves of sets along `U ⟶ X` has a left
> adjoint, namely extension by the empty set. This adjunction is the property characterising
> it.

```lean
public def setExtensionByEmptyAdjunction :
    setExtensionByEmpty.{u, v} B X hX U ⊣ setRestriction.{u, v} B X hX U
```

**`AlgebraicGeometry.Space.abelianEtaleExtensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean#L71). The attribute's comment: “extension by zero of abelian sheaves”.

> **Extension by zero of abelian étale sheaves** along an étale morphism `f : X ⟶ Y` of
> algebraic spaces: the left adjoint of restriction, constructed as the sheafification of the
> left Kan extension along postcomposition.

```lean
def abelianEtaleExtensionByZero (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u} ⥤
      Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.Space.abelianEtaleExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean#L80). The attribute's comment: “the adjunction”.

> **Extension by zero is left adjoint to restriction** for abelian étale sheaves along an
> étale morphism of algebraic spaces.

```lean
def abelianEtaleExtensionByZeroAdjunction (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    abelianEtaleExtensionByZero B S hS f hf ⊣ abelianEtaleRestriction B S hS f hf
```

## Tag 0F4K, an equation

[Tag 0F4K](https://stacks.math.columbia.edu/tag/0F4K) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_sigmaDesc_extensionByZeroSummandInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean#L376). The attribute's comment: “the presheaf formula (j\_\{p!} F)(V) = ⨁\_\{φ : V → U} F(V →^φ U)”.

> **Stacks Project, Tag 0F4K.** The sections of the presheaf `j_{p!} F` over a scheme `V` étale
> over `X` are the direct sum, over the morphisms `φ : V ⟶ U` over `X`, of the sections of `F` over
> `V` regarded as étale over `U` through `φ`; the comparison map is the one induced on each summand
> by the Kan extension unit.

```lean
theorem isIso_sigmaDesc_extensionByZeroSummandInclusion (F : (U.Etale)ᵒᵖ ⥤ A) (V : X.Etale) :
    IsIso (Sigma.desc
      (f := fun φ : V ⟶ smallEtaleSource j => F.obj (op (sourceDescend j φ)))
      (P := (extensionByZeroPresheaf j F).obj (op V))
      (fun φ => extensionByZeroSummandInclusion j F φ))
```

**`Stacks.EtaleCohomology.extensionByZeroPresheafSectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean#L411). The attribute's comment: “the presheaf formula (j\_\{p!} F)(V) = ⨁\_\{φ : V → U} F(V →^φ U)”.

> **Stacks Project, Tag 0F4K.** The direct-sum formula for the sections of the presheaf
> `j_{p!} F` over a scheme `V` étale over `X`, as an isomorphism.

```lean
def extensionByZeroPresheafSectionIso (F : (U.Etale)ᵒᵖ ⥤ A) (V : X.Etale) :
    (∐ fun φ : V ⟶ smallEtaleSource j => F.obj (op (sourceDescend j φ))) ≅
      (extensionByZeroPresheaf j F).obj (op V)
```

**`Stacks.EtaleCohomology.extensionByZero_obj_eq_sheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Formula.lean#L458). The attribute's comment: “j\_! F is the sheafification of j\_\{p!} F”.

> **Stacks Project, Tag 0F4K.** Extension by zero of an abelian sheaf is the sheafification of
> the presheaf `j_{p!} F` whose sections are given by the direct-sum formula.

```lean
theorem extensionByZero_obj_eq_sheafify
    [HasSheafify X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}]
    (F : Sheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (extensionByZero.{u, v} j).obj F =
      (presheafToSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
        (extensionByZeroPresheaf j F.obj)
```

**`Stacks.Sites.ExtensionByZero.isIso_lanSigmaDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L110).

> **Stacks 0F4K.** The left Kan extension along `(Over.forget U).op` is, over `V`, the
> coproduct of the values of `F` at the objects `φ : V ⟶ U` of `C/U`, the comparison map being
> the one induced by the Kan extension unit on each summand. Applied to the small étale site of
> a scheme and an étale `U ⟶ X`, this is the presheaf extension by zero along `U ⟶ X`: its
> sections over `V` are the direct sum of the sections of `F` over the lifts `V ⟶ U`.

```lean
theorem isIso_lanSigmaDesc
    {C : Type u} [Category.{u} C] (U : C)
    [∀ F : (Over U)ᵒᵖ ⥤ AddCommGrpCat.{u}, (Over.forget U).op.HasLeftKanExtension F]
    (F : (Over U)ᵒᵖ ⥤ AddCommGrpCat.{u}) (V : C) :
    IsIso (Sigma.desc
      (f := fun φ : V ⟶ U => F.obj (op (Over.mk φ)))
      (P := (((Over.forget U).op.lan.obj F).obj (op V)))
      (fun φ => (((Over.forget U).op.lanUnit.app F).app (op (Over.mk φ)))))
```

## Tag 03S4, an exercise

[Tag 03S4](https://stacks.math.columbia.edu/tag/03S4) in the Stacks Project.

**`Stacks.EtaleCohomology.extensionByZeroDirectSumAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/FormulaAdjunction.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/FormulaAdjunction.lean#L202). The attribute's comment: “the sheafification of the direct-sum presheaf j\_\{p!} is a left adjoint of j^\{-1}”.

> **Stacks Project, Tag 03S4.** Extension by zero, defined as the sheafification of the
> presheaf `j_{p!}` whose sections over a scheme `V` étale over `X` are the direct sum
> `⨁_{φ : V → U} F(V →^φ U)` of Stacks Tag 0F4K, is a left adjoint of the restriction functor
> `j^{-1}` on abelian sheaves of the small étale sites of an étale morphism `j : U ⟶ X` of
> schemes.

```lean
def extensionByZeroDirectSumAdj :
    sheafToPresheaf U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} ⋙
        extensionByZeroDirectSum j (A := AddCommGrpCat.{max (u + 1) v}) ⋙
        presheafToSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} ⊣
      etaleRestriction.{u, v} j
```

## Tag 03S5, a proposition

[Tag 03S5](https://stacks.math.columbia.edu/tag/03S5) in the Stacks Project.

**`AlgebraicGeometry.abelianExtensionByZero_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L105). The attribute's comment: “left exactness of j\_! in a big étale site”.

> Extension by zero of abelian étale sheaves preserves finite limits.

```lean
public instance abelianExtensionByZero_preservesFiniteLimits :
    PreservesFiniteLimits (abelianExtensionByZero B X hX U)
```

**`AlgebraicGeometry.abelianExtensionByZero_preservesFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L111). The attribute's comment: “right exactness of j\_! in a big étale site”.

> Extension by zero of abelian étale sheaves preserves finite colimits.

```lean
public instance abelianExtensionByZero_preservesFiniteColimits :
    PreservesFiniteColimits (abelianExtensionByZero B X hX U)
```

**`Stacks.EtaleCohomology.etaleModuleExtensionByZero_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZero.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZero.lean#L224). The attribute's comment: “left exactness of j\_! for module coefficients”.

> **Stacks Project, Tag 03S5** for module coefficients: extension by zero of sheaves of
> `Λ`-modules on small étale sites preserves finite limits.  It is additive, preserves
> monomorphisms and preserves all colimits, hence preserves homology, hence finite limits.

```lean
instance etaleModuleExtensionByZero_preservesFiniteLimits :
    PreservesFiniteLimits (etaleModuleExtensionByZero.{u, r} Λ j)
```

**`Stacks.EtaleCohomology.extensionByZero_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean#L212). The attribute's comment: “left exactness of j\_!”.

> Extension by zero preserves finite limits.

```lean
instance extensionByZero_preservesFiniteLimits
    [HasSheafify U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}] :
    PreservesFiniteLimits (extensionByZero.{u, v} j)
```

**`Stacks.EtaleCohomology.extensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean#L222). The attribute's comment: “j\_! is an exact functor”.

> Extension by zero along an étale morphism of schemes is an exact functor on
> abelian sheaves of the small étale sites.

```lean
theorem extensionByZero_exact
    [HasSheafify U.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}] :
    exactFunctor _ _ (extensionByZero.{u, v} j)
```

**`AlgebraicGeometry.moduleExtensionByZero_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleExactness.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleExactness.lean#L106). The attribute's comment: “left exactness of j\_! for sheaves of modules on the small etale sites of Tag 021B”.

> **Stacks 03S5 for sheaves of modules, on the sites of Tag 021B.** Extension by zero of
> sheaves of `Λ`-modules along an object `U` of the small étale site of `X` preserves finite
> limits. Together with the finite colimits it preserves as a left adjoint, extension by zero is
> exact.
>
> The small étale site of `U` has fibre products and equalizers, and composition with `U ⟶ X`
> preserves both, so Tag 04BH for module coefficients applies.

```lean
public instance moduleExtensionByZero_preservesFiniteLimits :
    PreservesFiniteLimits (moduleExtensionByZero B X hX U Λ)
```

**`AlgebraicGeometry.stalkExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L535). The attribute's comment: “stalk formula”.

> **Stacks 03S5.** The stalk at a geometric point `x` of `X` of the extension by zero of an
> abelian étale sheaf on `U` is the direct sum of its stalks at the lifts of `x` to `U`.

```lean
public def stalkExtensionByZeroIso
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1}) :
    etaleStalk B X hX x ((abelianExtensionByZero B X hX U).obj F).obj ≅
      (∐ fun p : geometricPointLifts B X hX U x => liftedStalk B X hX U x F p)
```

**`AlgebraicGeometry.stalkExtensionByZeroIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L546). The attribute's comment: “germ computation”.

> **Stacks 03S5.** The stalk isomorphism sends the germ of a section over an étale
> neighbourhood `W ⟶ U`, viewed in the extension by zero through the adjunction unit, to its
> germ at the induced lift, in the corresponding summand of the direct sum. This formula
> characterises the isomorphism.

```lean
public theorem stalkExtensionByZeroIso_germ
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1})
    (W : SmallEtale B U.obj.left.1 U.obj.left.property)
    (p : geometricPointLifts B X hX U x)
    (w : (geometricPointFiber B U.obj.left.1 U.obj.left.property
      (geometricPointOfLift B X hX U x p)).obj W)
    (q : (geometricPointFiber B X hX x).obj ((smallEtalePostcompose B X hX U).obj W))
    (hq : q.1 = w.1) (s : F.obj.obj (op W)) :
    (stalkExtensionByZeroIso B X hX U x F).hom
      ((colimit.ι ((CategoryOfElements.π (geometricPointFiber B X hX x)).op ⋙
          ((abelianExtensionByZero B X hX U).obj F).obj)
          (op (Functor.elementsMk _ ((smallEtalePostcompose B X hX U).obj W) q)))
        (((abelianExtensionByZeroAdjunction B X hX U).unit.app F).hom.app (op W) s)) =
      (Sigma.ι (fun p : geometricPointLifts B X hX U x => liftedStalk B X hX U x F p) p)
        ((colimit.ι ((CategoryOfElements.π (geometricPointFiber B U.obj.left.1
            U.obj.left.property (geometricPointOfLift B X hX U x p))).op ⋙ F.obj)
          (op (Functor.elementsMk _ W w))) s)
```

**`AlgebraicGeometry.stalkExtensionByZeroIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L577). The attribute's comment: “naturality”.

> **Stacks 03S5.** The stalk decomposition of extension by zero is natural in the abelian
> sheaf.

```lean
public theorem stalkExtensionByZeroIso_naturality
    {F G : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1}}
    (f : F ⟶ G) :
    colimMap (Functor.whiskerLeft (CategoryOfElements.π (geometricPointFiber B X hX x)).op
        ((abelianExtensionByZero B X hX U).map f).hom) ≫
        (stalkExtensionByZeroIso B X hX U x G).hom =
      (stalkExtensionByZeroIso B X hX U x F).hom ≫
        Limits.Sigma.map (fun p : geometricPointLifts B X hX U x =>
          colimMap (Functor.whiskerLeft (CategoryOfElements.π (geometricPointFiber
            B U.obj.left.1 U.obj.left.property (geometricPointOfLift B X hX U x p))).op f.hom))
```

**`AlgebraicGeometry.abelianExtensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L594). The attribute's comment: “exactness”.

> **Stacks 03S5.** Extension by zero of abelian sheaves along an étale morphism is exact.
> Under the equivalence of the small étale site of `U` with the localization of the small étale
> site of `X` at `U`, extension by zero becomes lower shriek along `Over.forget U`, which is
> exact.

```lean
public theorem abelianExtensionByZero_exact :
    exactFunctor _ _ (abelianExtensionByZero B X hX U)
```

## Tag 0F70, a lemma

[Tag 0F70](https://stacks.math.columbia.edu/tag/0F70) in the Stacks Project.

**`Stacks.EtaleCohomology.directImageRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/Exactness.lean#L263). The attribute's comment: “the isomorphism j^\{-1} j\_* F → F”.

> For an étale monomorphism `j : U ⟶ X`, the natural isomorphism `j^{-1} j_* F ≅ F` for
> abelian sheaves `F` on the small étale site of `U`, given by the counit of `j^{-1} ⊣ j_*`.

```lean
def directImageRestrictionIso :
    etaleDirectImage.{u, v} j ⋙ etaleRestriction.{u, v} j ≅ 𝟭 _
```

**`AlgebraicGeometry.abelianDirectImageAdjunction_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/DirectImage.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/DirectImage.lean#L90). The attribute's comment: “direct\_image\_counit”.

> **Stacks 0F70.** Along an open immersion `U ⟶ X` the counit of the adjunction between
> restriction and direct image is an isomorphism: an abelian étale sheaf on `U` is recovered from
> its direct image by restricting back to `U`. Composition with `U ⟶ X` is continuous,
> cocontinuous, and — because the structure morphism of `U` is a monomorphism — fully faithful,
> which is exactly the situation of Stacks 00XT.

```lean
public theorem abelianDirectImageAdjunction_counit_isIso :
    IsIso (abelianDirectImageAdjunction B X hX U).counit
```

**`AlgebraicGeometry.abelianExtensionByZeroAdjunction_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/OpenImmersion.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/OpenImmersion.lean#L63). The attribute's comment: “extension\_by\_zero\_unit”.

> Along an open immersion `U ⟶ X` the unit of the extension-by-zero adjunction is an
> isomorphism: an abelian étale sheaf on `U` is recovered from its extension by zero by
> restricting back to `U`.

```lean
public theorem abelianExtensionByZeroAdjunction_unit_isIso
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1}) :
    IsIso ((abelianExtensionByZeroAdjunction B X hX U).unit.app F)
```

**`AlgebraicGeometry.abelianExtensionByZeroAdjunction_hom_isIso_of_stalk_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroCharacterization.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroCharacterization.lean#L226). The attribute's comment: “extension\_by\_zero\_characterization: uniqueness”.

> **Stacks 0F70.** An abelian étale sheaf on `X` whose restriction to the open subscheme `U`
> is identified with `F` and whose stalks at the geometric points of `X` outside `U` vanish is
> canonically the extension by zero of `F`: the map from `j_!F` adjoint to the given
> identification is an isomorphism. Together with the vanishing of the stalks of `j_!F` outside
> `U` this is the uniqueness assertion of the source.

```lean
public theorem abelianExtensionByZeroAdjunction_hom_isIso_of_stalk_isZero
    [IsOpenImmersion (B.inclusion.map U.obj.hom)]
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1})
    (G : Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1})
    (e : F ≅ (abelianRestriction B X hX U).obj G)
    (hG : ∀ x : GeometricPoint X,
      x.hom default ∉ Set.range (B.inclusion.map U.obj.hom).base →
        IsZero (etaleStalk B X hX x G.obj)) :
    IsIso (((abelianExtensionByZeroAdjunction B X hX U).homEquiv F G).symm e.hom)
```

**`AlgebraicGeometry.abelianExtensionByZero_stalk_isZero_of_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L677). The attribute's comment: “extension\_by\_zero\_characterization: zero stalks”.

> **Stacks 0F70.** The extension by zero of an abelian étale sheaf on `U` has zero stalk at
> every geometric point of `X` outside the image of `U`: by the stalk formula the stalk is the
> direct sum over the lifts of that point, and there are none.

```lean
public theorem abelianExtensionByZero_stalk_isZero_of_not_mem_range
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1})
    (hx : x.hom default ∉ Set.range (B.inclusion.map U.obj.hom).base) :
    IsZero (etaleStalk B X hX x ((abelianExtensionByZero B X hX U).obj F).obj)
```

**`AlgebraicGeometry.abelianExtensionByZero_stalk_isZero_of_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroStalk.lean#L677). The attribute's comment: “extension\_by\_zero\_characterization”.

> **Stacks 0F70.** The extension by zero of an abelian étale sheaf on `U` has zero stalk at
> every geometric point of `X` outside the image of `U`: by the stalk formula the stalk is the
> direct sum over the lifts of that point, and there are none.

```lean
public theorem abelianExtensionByZero_stalk_isZero_of_not_mem_range
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1})
    (hx : x.hom default ∉ Set.range (B.inclusion.map U.obj.hom).base) :
    IsZero (etaleStalk B X hX x ((abelianExtensionByZero B X hX U).obj F).obj)
```

## Tag 03S6, a lemma

[Tag 03S6](https://stacks.math.columbia.edu/tag/03S6) in the Stacks Project.

**`AlgebraicGeometry.abelianExtensionByZeroBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange.lean#L182). The attribute's comment: “abelian sheaves”.

> **Stacks 03S6, abelian sheaves.** Extension by zero of abelian étale sheaves commutes
> with base change: for `f : Y ⟶ X` and `j : V ⟶ X` étale with base change `j' : V' ⟶ Y` and
> `f' : V' ⟶ V`, one has `j'_! ∘ f'^{-1} ≅ f^{-1} ∘ j_!`, naturally in the sheaf.

```lean
public noncomputable def abelianExtensionByZeroBaseChangeIso
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : Y ⟶ X)
    (U : SmallEtale B X.1 X.property) :
    (smallEtaleBaseChange B (baseChangedEtaleProjection B f U)).sheafPullback
        AddCommGrpCat.{u + 1}
        (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
        (SmallEtale.topology B
          ((smallEtaleBaseChange B f).obj U).obj.left.1
          ((smallEtaleBaseChange B f).obj U).obj.left.property) ⋙
      abelianExtensionByZero B Y.1 Y.property
        ((smallEtaleBaseChange B f).obj U) ≅
    abelianExtensionByZero B X.1 X.property U ⋙
      (smallEtaleBaseChange B f).sheafPullback AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Y.1 Y.property)
```

**`AlgebraicGeometry.moduleExtensionByZeroBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange.lean#L214). The attribute's comment: “sheaves of modules”.

> **Stacks 03S6, sheaves of modules.** Extension by zero of étale sheaves of `Λ`-modules
> commutes with base change, by the same adjunction argument as for abelian sheaves.

```lean
public noncomputable def moduleExtensionByZeroBaseChangeIso
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : Y ⟶ X)
    (U : SmallEtale B X.1 X.property) (Λ : Type v) [Ring Λ] :
    (smallEtaleBaseChange B (baseChangedEtaleProjection B f U)).sheafPullback
        (ModuleCat.{max (u + 1) v} Λ)
        (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
        (SmallEtale.topology B
          ((smallEtaleBaseChange B f).obj U).obj.left.1
          ((smallEtaleBaseChange B f).obj U).obj.left.property) ⋙
      moduleExtensionByZero B Y.1 Y.property
        ((smallEtaleBaseChange B f).obj U) Λ ≅
    moduleExtensionByZero B X.1 X.property U Λ ⋙
      (smallEtaleBaseChange B f).sheafPullback (ModuleCat.{max (u + 1) v} Λ)
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Y.1 Y.property)
```

## Tag 0F4L, a lemma

[Tag 0F4L](https://stacks.math.columbia.edu/tag/0F4L) in the Stacks Project.

**`AlgebraicGeometry.abelianExtensionByZeroToPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 887](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L887). The attribute's comment: “abelian natural map”.

> The canonical map from extension by zero to the direct image of abelian sheaves along the étale
> morphism `U ⟶ X`. On the summand of the presheaf extension indexed by `φ : V ⟶ U` it extends a
> section by zero along the open and closed graph of `φ`; that requires `U ⟶ X` to be separated, and
> off the separated locus the map is zero.

```lean
public noncomputable def abelianExtensionByZeroToPushforward :
    let := smallEtaleBaseChange_isContinuous B U.obj.hom
    abelianExtensionByZero B X hX U ⟶
      (smallEtaleBaseChange B U.obj.hom).sheafPushforwardContinuous
        AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X hX)
        (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
```

**`AlgebraicGeometry.abelianExtensionByZeroToPushforward_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 924](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L924). The attribute's comment: “abelian injectivity”.

> For a separated étale morphism, every component of the canonical map from extension by zero to
> the direct image of abelian sheaves is a monomorphism.

```lean
public theorem abelianExtensionByZeroToPushforward_mono
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      AddCommGrpCat.{u + 1}) :
    Mono ((abelianExtensionByZeroToPushforward B X hX U).app F)
```

**`AlgebraicGeometry.abelianExtensionByZeroToPushforward_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 946](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L946). The attribute's comment: “abelian graph restriction”.

> On the summand indexed by `W ⟶ U`, the canonical map restricts along the graph `W ⟶ W ×_X U` to
> the original section.

```lean
public theorem abelianExtensionByZeroToPushforward_graph
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      AddCommGrpCat.{u + 1})
    (W : SmallEtale B U.obj.left.1 U.obj.left.property)
    (s : F.obj.obj (Opposite.op W)) :
    let V := (smallEtalePostcompose B X hX U).obj W
    (F.obj.map (smallEtaleGraph B X hX U W).op)
      (((abelianExtensionByZeroToPushforward B X hX U).app F).hom.app
        (Opposite.op V)
        (((abelianExtensionByZeroAdjunction
          B X hX U).unit.app F).hom.app (Opposite.op W) s)) = s
```

**`AlgebraicGeometry.abelianExtensionByZeroToPushforward_graph_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 967](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L967). The attribute's comment: “abelian complementary vanishing”.

> The image of the summand indexed by `W ⟶ U` restricts to zero along every morphism into
> `W ×_X U` whose image avoids the graph of `W`.

```lean
public theorem abelianExtensionByZeroToPushforward_graph_compl
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      AddCommGrpCat.{u + 1})
    (W T : SmallEtale B U.obj.left.1 U.obj.left.property)
    (g : T ⟶ (smallEtaleBaseChange B U.obj.hom).obj
      ((smallEtalePostcompose B X hX U).obj W))
    (hg : disjointFromSmallEtaleGraph B X hX U W T g)
    (s : F.obj.obj (Opposite.op W)) :
    let V := (smallEtalePostcompose B X hX U).obj W
    (F.obj.map g.op)
      (((abelianExtensionByZeroToPushforward B X hX U).app F).hom.app
        (Opposite.op V)
        (((abelianExtensionByZeroAdjunction
          B X hX U).unit.app F).hom.app (Opposite.op W) s)) = 0
```

**`AlgebraicGeometry.moduleExtensionByZeroToPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 993](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L993). The attribute's comment: “module natural map”.

> The canonical map from extension by zero to the direct image of sheaves of `Λ`-modules along
> the étale morphism `U ⟶ X`, constructed exactly as in the abelian case.

```lean
public noncomputable def moduleExtensionByZeroToPushforward
    (Λ : Type v) [Ring Λ] :
    let := smallEtaleBaseChange_isContinuous B U.obj.hom
    moduleExtensionByZero B X hX U Λ ⟶
      (smallEtaleBaseChange B U.obj.hom).sheafPushforwardContinuous
        (ModuleCat.{max (u + 1) v} Λ)
        (SmallEtale.topology B X hX)
        (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
```

**`AlgebraicGeometry.moduleExtensionByZeroToPushforward_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 1032](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L1032). The attribute's comment: “module injectivity”.

> For a separated étale morphism, every component of the canonical map from extension by zero to
> the direct image of sheaves of `Λ`-modules is a monomorphism.

```lean
public theorem moduleExtensionByZeroToPushforward_mono
    (Λ : Type v) [Ring Λ]
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      (ModuleCat.{max (u + 1) v} Λ)) :
    Mono ((moduleExtensionByZeroToPushforward B X hX U Λ).app F)
```

**`AlgebraicGeometry.moduleExtensionByZeroToPushforward_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 1064](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L1064). The attribute's comment: “module graph restriction”.

> On the summand indexed by `W ⟶ U`, the canonical map for sheaves of modules restricts along the
> graph `W ⟶ W ×_X U` to the original section.

```lean
public theorem moduleExtensionByZeroToPushforward_graph
    (Λ : Type v) [Ring Λ]
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      (ModuleCat.{max (u + 1) v} Λ))
    (W : SmallEtale B U.obj.left.1 U.obj.left.property)
    (s : F.obj.obj (Opposite.op W)) :
    let V := (smallEtalePostcompose B X hX U).obj W
    (F.obj.map (smallEtaleGraph B X hX U W).op)
      (((moduleExtensionByZeroToPushforward B X hX U Λ).app F).hom.app
        (Opposite.op V)
      (((moduleExtensionByZeroAdjunction
          B X hX U Λ).unit.app F).hom.app (Opposite.op W) s)) = s
```

**`AlgebraicGeometry.moduleExtensionByZeroToPushforward_graph_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean, line 1086](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Pushforward.lean#L1086). The attribute's comment: “module complementary vanishing”.

> The image of the summand indexed by `W ⟶ U` restricts to zero along every morphism into
> `W ×_X U` whose image avoids the graph of `W`, for sheaves of modules.

```lean
public theorem moduleExtensionByZeroToPushforward_graph_compl
    (Λ : Type v) [Ring Λ]
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property)
      (ModuleCat.{max (u + 1) v} Λ))
    (W T : SmallEtale B U.obj.left.1 U.obj.left.property)
    (g : T ⟶ (smallEtaleBaseChange B U.obj.hom).obj
      ((smallEtalePostcompose B X hX U).obj W))
    (hg : disjointFromSmallEtaleGraph B X hX U W T g)
    (s : F.obj.obj (Opposite.op W)) :
    let V := (smallEtalePostcompose B X hX U).obj W
    (F.obj.map g.op)
      (((moduleExtensionByZeroToPushforward B X hX U Λ).app F).hom.app
        (Opposite.op V)
      (((moduleExtensionByZeroAdjunction
          B X hX U Λ).unit.app F).hom.app (Opposite.op W) s)) = 0
```

## Tag 03S7, a lemma

[Tag 03S7](https://stacks.math.columbia.edu/tag/03S7) in the Stacks Project.

**`AlgebraicGeometry.abelianExtensionByZeroToPushforward_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/FinitePushforward.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/FinitePushforward.lean#L272). The attribute's comment: “abelian sheaves”.

> **Stacks 03S7.** For a finite étale morphism, the canonical map from extension by zero to
> the direct image is an isomorphism on abelian sheaves.

```lean
public theorem abelianExtensionByZeroToPushforward_isIso :
    IsIso (abelianExtensionByZeroToPushforward B X hX U)
```

**`AlgebraicGeometry.moduleExtensionByZeroToPushforward_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/FinitePushforward.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/FinitePushforward.lean#L322). The attribute's comment: “sheaves of modules”.

> **Stacks 03S7.** For a finite étale morphism, the canonical map from extension by zero to
> the direct image is an isomorphism on sheaves of `Λ`-modules.

```lean
public theorem moduleExtensionByZeroToPushforward_isIso (Λ : Type v) [Ring Λ] :
    IsIso (moduleExtensionByZeroToPushforward B X hX U Λ)
```

## Tag 095L, a lemma

[Tag 095L](https://stacks.math.columbia.edu/tag/095L) in the Stacks Project.

**`Stacks.EtaleCohomology.openClosedShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ClosedComplement.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ClosedComplement.lean#L46). The attribute's comment: “the canonical short complex”.

> The short complex `j_! j^{-1} F ⟶ F ⟶ i_* i^{-1} F` built from the counit of `j_! ⊣ j^{-1}` and
> the unit of `i^{-1} ⊣ i_*`, for a closed subscheme `i : Z ⟶ X` and the open immersion `j : U ⟶ X`
> of its complement.

```lean
def openClosedShortComplex :
    ShortComplex (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
```

**`Stacks.EtaleCohomology.openClosedShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ClosedComplement.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ClosedComplement.lean#L57). The attribute's comment: “short exactness”.

> For a closed immersion `i : Z ⟶ X` and the open immersion `j : U ⟶ X` of its complement, the
> short complex `0 ⟶ j_! j^{-1} F ⟶ F ⟶ i_* i^{-1} F ⟶ 0` is short exact.

```lean
theorem openClosedShortComplex_shortExact :
    (openClosedShortComplex.{u, v} i j hij F).ShortExact
```

**`Stacks.EtaleCohomology.shortExact_etaleModuleExtensionByZero_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ModuleOpenClosedTriangle.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ModuleOpenClosedTriangle.lean#L256). The attribute's comment: “module coefficients”. References: SGA 4 IV (14.6), “(14.6.1)”; SGA 4 VIII (6.5), “partial”.

> **Stacks Project, Tag 095L** for module coefficients.  Let `X` be a scheme, let `i : Z ⟶ X`
> be a closed immersion and let `j : U ⟶ X` be an open immersion whose image is the complement of
> the image of `i`, and let `Λ` be a ring.  For every sheaf `ℱ` of `Λ`-modules on the small étale
> site of `X` the counit of `j_! ⊣ j^{-1}` and the unit of `i^{-1} ⊣ i_*` form a short exact
> sequence
> `0 → j_! j^{-1} ℱ → ℱ → i_* i^{-1} ℱ → 0`
> of sheaves of `Λ`-modules on `X_étale`.

```lean
theorem shortExact_etaleModuleExtensionByZero_directImage (Λ : Type r) [Ring Λ]
    {Z U X : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i] (j : U ⟶ X) [IsOpenImmersion j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ) (F : EtaleModules.{u, r} Λ X) :
    ∃ h : (etaleModuleExtensionByZeroAdj.{u, r} Λ j).counit.app F ≫
        (etaleModuleInverseImageAdj.{u, r} Λ i).unit.app F = 0,
      (ShortComplex.mk ((etaleModuleExtensionByZeroAdj.{u, r} Λ j).counit.app F)
        ((etaleModuleInverseImageAdj.{u, r} Λ i).unit.app F) h).ShortExact
```

**`Stacks.EtaleCohomology.shortExact_extensionByZero_etaleAbelianDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/OpenClosedSequence.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/OpenClosedSequence.lean#L400). References: SGA 4 VIII (6.5), “partial”.

> **Stacks Project, Tag 095L.** Let `X` be a scheme, let `i : Z ⟶ X` be a closed immersion and
> let `j : U ⟶ X` be an open immersion whose image is the complement of the image of `i`.  For
> every abelian sheaf `F` on the small étale site of `X` the counit of `j_! ⊣ j^{-1}` and the unit
> of `i^{-1} ⊣ i_*` form a short exact sequence
> `0 → j_! j^{-1} F → F → i_* i^{-1} F → 0`
> of abelian sheaves on `X_étale`.

```lean
theorem shortExact_extensionByZero_etaleAbelianDirectImage {Z U X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (j : U ⟶ X) [IsOpenImmersion j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    ∃ h : (extensionByZeroAdj.{u, v} j).counit.app F ≫
        (etaleAbelianInverseImageDirectImageAdj.{u, v} i).unit.app F = 0,
      (ShortComplex.mk ((extensionByZeroAdj.{u, v} j).counit.app F)
        ((etaleAbelianInverseImageDirectImageAdj.{u, v} i).unit.app F) h).ShortExact
```

## Tag 0GJ1, a lemma

[Tag 0GJ1](https://stacks.math.columbia.edu/tag/0GJ1) in the Stacks Project.

**`Stacks.EtaleCohomology.directImageExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/FiniteDirectImage.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/FiniteDirectImage.lean#L136). The attribute's comment: “at the coefficients AddCommGrpCat.\{u+1}, on Mathlib's small etale sites”.

> **Stacks Project, Tag 0GJ1.** For a cartesian square `j' ≫ f = g ≫ j` of schemes with `f`
> finite and `j` an open immersion, `f_* ∘ j'_! ≅ j_! ∘ g_*` as functors from abelian sheaves on
> `U_étale` to abelian sheaves on `Y_étale`.

```lean
def directImageExtensionByZeroIso :
    extensionByZero.{u, 0} j' ⋙ etaleAbelianDirectImage.{u, 0} f ≅
      etaleAbelianDirectImage.{u, 0} g ⋙ extensionByZero.{u, 0} j
```

**`AlgebraicGeometry.extensionByZeroFinitePushforwardCartesianIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroFinitePushforwardCartesian.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroFinitePushforwardCartesian.lean#L186).

> **Stacks 0GJ1.** For a cartesian square `g ≫ j = j' ≫ f` of schemes of a big étale site
> with `f` finite and `j : V ⟶ Y` an open immersion, the functors `j_! ∘ g_*` and `f_* ∘ j'_!`
> from abelian sheaves on the small étale site of `U` to abelian sheaves on the small étale site
> of `Y` are naturally isomorphic.
>
> The isomorphism is the mate, along the two extension-by-zero adjunctions, of the base change
> identification `AlgebraicGeometry.abelianRestrictionPushforwardCartesianIso` of the
> restriction functors; it is an isomorphism by the uniqueness characterisation of extension by
> zero, whose stalk hypothesis is
> `AlgebraicGeometry.etaleStalk_pushforward_extensionByZero_isZero`, where finiteness of `f` is
> used. The cartesian square is used twice: once for the base change identification, and once to
> see that `j'` is an open immersion.

```lean
public def extensionByZeroFinitePushforwardCartesianIso [IsFinite (B.inclusion.map f)]
    [IsOpenImmersion (B.inclusion.map V.obj.hom)]
    (sq : IsPullback (B.inclusion.map U.obj.hom) (B.inclusion.map g) (B.inclusion.map f)
      (B.inclusion.map V.obj.hom)) :
    B.smallPushforward g AddCommGrpCat.{u + 1} ⋙
        abelianExtensionByZero B Y.1 Y.property V ≅
      abelianExtensionByZero B X.1 X.property U ⋙
        B.smallPushforward f AddCommGrpCat.{u + 1}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.70, Tag 03S2](https://stacks.math.columbia.edu/tag/03S2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
