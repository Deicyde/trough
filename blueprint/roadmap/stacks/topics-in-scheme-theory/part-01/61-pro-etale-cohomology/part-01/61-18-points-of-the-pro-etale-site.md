---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.proetale_hasEnoughPoints, AlgebraicGeometry.ProEtale.exists_geometricPoint_lift_of_proetaleCover, AlgebraicGeometry.geometricPointToStrictHenselization_comp, AlgebraicGeometry.weaklyEtale_strictHenselizationToBase, AlgebraicGeometry.strictHenselizationSectionsEquivStalk, AlgebraicGeometry.strictHenselizationSectionsEquivStalk_apply, AlgebraicGeometry.strictHenselizationSectionsEquivStalk_natural
statement: formalized
proof: formalized
---

# 61.18 Points of the pro-étale site

Section 61.18 of the Stacks Project, [Tag 0991](https://stacks.math.columbia.edu/tag/0991). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0992, a lemma

[Tag 0992](https://stacks.math.columbia.edu/tag/0992) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.proetale_hasEnoughPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughPoints.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughPoints.lean#L530).

> **Stacks 0992.** The pro-étale sites of schemes, the small pro-étale site of a scheme, the
> big pro-étale site over it, the affine objects of the small site and the affine objects of the
> big site all have enough points.

```lean
public theorem proetale_hasEnoughPoints
    (B : BigProetaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    GrothendieckTopology.HasConservativeFamily.{u + 1} B.topology ∧
      GrothendieckTopology.HasConservativeFamily.{u} (Scheme.ProEt.topology S) ∧
      GrothendieckTopology.HasConservativeFamily.{u + 1} (BigProetaleOver.topology B S hS) ∧
      GrothendieckTopology.HasConservativeFamily.{u} (AffineProetale.topology S) ∧
      GrothendieckTopology.HasConservativeFamily.{u + 1}
        (BigAffineProetale.topology B S hS)
```

## Tag 0F6C, a lemma

[Tag 0F6C](https://stacks.math.columbia.edu/tag/0F6C) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_geometricPoint_lift_of_proetaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/GeometricPoints.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/GeometricPoints.lean#L115).

> A geometric point of a scheme lifts to a member of any pro-étale covering family.

```lean
theorem exists_geometricPoint_lift_of_proetaleCover
    {S : Scheme.{u}} (s : AlgebraicGeometry.GeometricPoint S)
    {I : Type v} {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (h : Presieve.ofArrows X f ∈ Scheme.proetalePrecoverage S) :
    ∃ i, ∃ t : AlgebraicGeometry.GeometricPoint (X i),
      t.map (f i) = s
```

## Tag 0993, a lemma

[Tag 0993](https://stacks.math.columbia.edu/tag/0993) in the Stacks Project.

**`AlgebraicGeometry.geometricPointToStrictHenselization_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/StrictHenselization.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/StrictHenselization.lean#L222). The attribute's comment: “the canonical geometric point”.

> **Stacks Project, Tag 0993.** The canonical lift of a geometric point to its strict
> henselization lies over that geometric point, so the strict henselization is a pro-étale
> neighbourhood of the point.

```lean
public theorem geometricPointToStrictHenselization_comp :
    geometricPointToStrictHenselization B S hS s ≫ strictHenselizationToBase B S hS s =
      s.hom
```

**`AlgebraicGeometry.weaklyEtale_strictHenselizationToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean#L262). The attribute's comment: “the pro-étale object”.

> **Stacks Project, Tag 0993.** The canonical morphism from the strict henselization of `S` at
> a geometric point `s` is weakly étale, so the strict henselization is an object of the small
> pro-étale site of `S`. It is the spectrum of an ind-étale ring map followed by the canonical
> morphism from the local ring at the image of `s`.

```lean
theorem weaklyEtale_strictHenselizationToBase :
    WeaklyEtale (strictHenselizationToBase B S hS s)
```

**`AlgebraicGeometry.strictHenselizationSectionsEquivStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean#L336). The attribute's comment: “the stalk comparison”.

> **Stacks Project, Tag 0993.** Sections of a presheaf on the small pro-étale site over the
> strict henselization at a geometric point are canonically the stalk of the presheaf at that
> geometric point.

```lean
def strictHenselizationSectionsEquivStalk (F : (S.ProEt)ᵒᵖ ⥤ Type (max (u + 1) v)) :
    F.obj (op (strictHenselizationProEt B S hS s)) ≃ proetaleStalk S s F
```

**`AlgebraicGeometry.strictHenselizationSectionsEquivStalk_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean#L350). The attribute's comment: “the canonical stalk comparison”.

> **Stacks Project, Tag 0993.** The comparison of sections over the strict henselization with
> the stalk is the colimit insertion at the canonical pro-étale neighbourhood; this is what makes
> it canonical.

```lean
theorem strictHenselizationSectionsEquivStalk_apply
    (F : (S.ProEt)ᵒᵖ ⥤ Type (max (u + 1) v))
    (x : F.obj (op (strictHenselizationProEt B S hS s))) :
    strictHenselizationSectionsEquivStalk B S hS s F x =
      colimit.ι ((Functor.Elements.π (proetalePointFiber S s)).op ⋙ F)
        (op ((proetalePointFiber S s).elementsMk (strictHenselizationProEt B S hS s)
        (strictHenselizationPoint B S hS s))) x
```

**`AlgebraicGeometry.strictHenselizationSectionsEquivStalk_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/GeometricPointStalk.lean#L362). The attribute's comment: “functoriality of the stalk comparison”.

> **Stacks Project, Tag 0993.** The comparison of sections over the strict henselization with
> the stalk is functorial in the presheaf.

```lean
theorem strictHenselizationSectionsEquivStalk_natural
    {F G : (S.ProEt)ᵒᵖ ⥤ Type (max (u + 1) v)} (α : F ⟶ G)
    (x : F.obj (op (strictHenselizationProEt B S hS s))) :
    strictHenselizationSectionsEquivStalk B S hS s G
        (α.app (op (strictHenselizationProEt B S hS s)) x) =
      colim.map (Functor.whiskerLeft (Functor.Elements.π (proetalePointFiber S s)).op α)
        (strictHenselizationSectionsEquivStalk B S hS s F x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.18, Tag 0991](https://stacks.math.columbia.edu/tag/0991)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
