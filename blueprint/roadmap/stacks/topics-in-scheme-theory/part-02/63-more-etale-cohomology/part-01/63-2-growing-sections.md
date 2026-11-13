---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.supportedSectionsEquiv, AlgebraicGeometry.SmallEtale.supportedSectionsEquiv_restrict, AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv, AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv_restrict
statement: formalized
proof: formalized
---

# 63.2 Growing sections

Section 63.2 of the Stacks Project, [Tag 0F71](https://stacks.math.columbia.edu/tag/0F71). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F6F, a lemma

[Tag 0F6F](https://stacks.math.columbia.edu/tag/0F6F) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.supportedSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/ClosedSupportEquiv.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/ClosedSupportEquiv.lean#L421). The attribute's comment: “canonical bijection”.

> The canonical bijection between sections supported on corresponding closed
> subschemes of two étale neighborhoods.

```lean
public noncomputable def supportedSectionsEquiv
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U U' : SmallEtale B S hS) (φ : U' ⟶ U)
    (Z' : Scheme.{u})
    (i : Z' ⟶ (SmallEtale.toScheme B S hS).obj U')
    [IsClosedImmersion i]
    [IsClosedImmersion (i ≫ (SmallEtale.toScheme B S hS).map φ)] :
    {s : F.obj.obj (op U) //
        supportSection B S hS F U s ⊆
          Set.range (i ≫ (SmallEtale.toScheme B S hS).map φ).base} ≃
      {s' : F.obj.obj (op U') //
        supportSection B S hS F U' s' ⊆
          Set.range i.base}
```

**`AlgebraicGeometry.SmallEtale.supportedSectionsEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean#L70). The attribute's comment: “restriction characterization”.

> The canonical bijection is restriction on any étale test object on which
> the inverse images of the two closed subsets coincide.

```lean
public theorem supportedSectionsEquiv_restrict
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U U' : SmallEtale B S hS) (φ : U' ⟶ U)
    (Z' : Scheme.{u})
    (i : Z' ⟶ (SmallEtale.toScheme B S hS).obj U')
    [IsClosedImmersion i]
    [IsClosedImmersion (i ≫ (SmallEtale.toScheme B S hS).map φ)]
    (V : SmallEtale B S hS) (f : V ⟶ U')
    (h : Set.preimage ((SmallEtale.toScheme B S hS).map (f ≫ φ)).base
        (Set.range (i ≫ (SmallEtale.toScheme B S hS).map φ).base) =
      Set.preimage ((SmallEtale.toScheme B S hS).map f).base
        (Set.range i.base))
    (s : {s : F.obj.obj (op U) //
      supportSection B S hS F U s ⊆
        Set.range (i ≫ (SmallEtale.toScheme B S hS).map φ).base}) :
    F.obj.map f.op (supportedSectionsEquiv B S hS F U U' φ Z' i s).val =
      F.obj.map (f ≫ φ).op s.val
```

**`AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean#L355). The attribute's comment: “locally closed support”.

> The canonical bijection of Tag 0F6G (merged into 0F6F), including its
> abelian-group structure. Both opens contain the given support as a closed subset.

```lean
public noncomputable def locallyClosedSupportEquiv
    (W : SmallEtale B S hS) (Z : Set ((SmallEtale.toScheme B S hS).obj W))
    (U V : ((SmallEtale.toScheme B S hS).obj W).Opens)
    (hZU : Z ⊆ U) (hZV : Z ⊆ V)
    (hUc : IsClosed (U.ι.base ⁻¹' Z)) (hVc : IsClosed (V.ι.base ⁻¹' Z)) :
    supportedSectionsOnOpen B S hS F W Z U ≃+
      supportedSectionsOnOpen B S hS F W Z V
```

**`AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean#L378). The attribute's comment: “locally closed support, restriction”.

> For nested opens the canonical identification is restriction.

```lean
public theorem locallyClosedSupportEquiv_restrict
    (W : SmallEtale B S hS) (Z : Set ((SmallEtale.toScheme B S hS).obj W))
    (U V : ((SmallEtale.toScheme B S hS).obj W).Opens)
    (hZU : Z ⊆ U) (hZV : Z ⊆ V)
    (hUc : IsClosed (U.ι.base ⁻¹' Z)) (hVc : IsClosed (V.ι.base ⁻¹' Z))
    (h : V ≤ U) (s : supportedSectionsOnOpen B S hS F W Z U) :
    (locallyClosedSupportEquiv B S hS F W Z U V hZU hZV hUc hVc s).val =
      F.obj.map (openObjectHomOfLE B S hS W h).op s.val
```

## Tag 0F6G, a lemma

[Tag 0F6G](https://stacks.math.columbia.edu/tag/0F6G) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean#L355). The attribute's comment: “the canonical bijection”.

> The canonical bijection of Tag 0F6G (merged into 0F6F), including its
> abelian-group structure. Both opens contain the given support as a closed subset.

```lean
public noncomputable def locallyClosedSupportEquiv
    (W : SmallEtale B S hS) (Z : Set ((SmallEtale.toScheme B S hS).obj W))
    (U V : ((SmallEtale.toScheme B S hS).obj W).Opens)
    (hZU : Z ⊆ U) (hZV : Z ⊆ V)
    (hUc : IsClosed (U.ι.base ⁻¹' Z)) (hVc : IsClosed (V.ι.base ⁻¹' Z)) :
    supportedSectionsOnOpen B S hS F W Z U ≃+
      supportedSectionsOnOpen B S hS F W Z V
```

**`AlgebraicGeometry.SmallEtale.locallyClosedSupportEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/SupportedSections/LocallyClosed.lean#L378). The attribute's comment: “the canonical bijection”.

> For nested opens the canonical identification is restriction.

```lean
public theorem locallyClosedSupportEquiv_restrict
    (W : SmallEtale B S hS) (Z : Set ((SmallEtale.toScheme B S hS).obj W))
    (U V : ((SmallEtale.toScheme B S hS).obj W).Opens)
    (hZU : Z ⊆ U) (hZV : Z ⊆ V)
    (hUc : IsClosed (U.ι.base ⁻¹' Z)) (hVc : IsClosed (V.ι.base ⁻¹' Z))
    (h : V ≤ U) (s : supportedSectionsOnOpen B S hS F W Z U) :
    (locallyClosedSupportEquiv B S hS F W Z U V hZU hZV hUc hVc s).val =
      F.obj.map (openObjectHomOfLE B S hS W h).op s.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.2, Tag 0F71](https://stacks.math.columbia.edu/tag/0F71)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
