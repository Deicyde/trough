---
declaration: section
origin: cited
lean: Stacks.SteinFactorization.etale_fromNormalization_of_properFlat, Stacks.SteinFactorization.isFinite_fromNormalization_of_properFlat, AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_of_properFlat, AlgebraicGeometry.surjective_etaleFundamentalGroupMap_of_properFlat, AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_of_properFlat
statement: formalized
proof: formalized
---

# 58.15 Homotopy exact sequence

Section 58.15 of the Stacks Project, [Tag 0BUM](https://stacks.math.columbia.edu/tag/0BUM). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BUN, a lemma

[Tag 0BUN](https://stacks.math.columbia.edu/tag/0BUN) in the Stacks Project.

**`Stacks.SteinFactorization.etale_fromNormalization_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ProperFlatGeomReduced.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ProperFlatGeomReduced.lean#L134). The attribute's comment: “étaleness of the second factor”. References: SGA 1 X (1.2), “Y′ → Y is étale”.

> **Stacks Project, Tag 0BUN.** Let `f : X ⟶ S` be a proper morphism of schemes which is flat,
> of finite presentation and has geometrically reduced fibres, and let `X ⟶ S' ⟶ S` be its Stein
> factorization. Then the second factor `S' ⟶ S` is étale.

```lean
public theorem etale_fromNormalization_of_properFlat (hfp : FinitePresentation f) :
    Etale f.fromNormalization
```

**`Stacks.SteinFactorization.isFinite_fromNormalization_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ProperFlatGeomReduced.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ProperFlatGeomReduced.lean#L143). The attribute's comment: “finiteness of the second factor”. References: EGA III (7.8.10), “partial”.

> **Stacks Project, Tag 0BUN.** Let `f : X ⟶ S` be a proper morphism of schemes which is flat,
> of finite presentation and has geometrically reduced fibres, and let `X ⟶ S' ⟶ S` be its Stein
> factorization. Then the second factor `S' ⟶ S` is finite.

```lean
public theorem isFinite_fromNormalization_of_properFlat (hfp : FinitePresentation f) :
    IsFinite f.fromNormalization
```

## Tag 0C0J, a proposition

[Tag 0C0J](https://stacks.math.columbia.edu/tag/0C0J) in the Stacks Project.

**`AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/HomotopySequenceExactness.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/HomotopySequenceExactness.lean#L287). References: SGA 1 X (1.4), “Surjectivity of π₁(X”; SGA 1 XIII (4.1), “Surjectivity of v”; SGA 1 XIII (4.4), “partial”.

> **The homotopy sequence of a proper flat family is exact.** Let `f : X ⟶ S` be a flat proper
> morphism of finite presentation whose geometric fibres are connected and reduced, let `S` be
> connected, let `s` be a geometric point of `S` and let `z` be a geometric point of the geometric
> fibre `X_s`. Then
>
> ```
> π₁(X_s, z) ⟶ π₁(X, z ∘ p) ⟶ π₁(S, z ∘ p ∘ f) ⟶ 1
> ```
>
> is exact: the second map is surjective, the composite of the two is trivial, and the kernel of
> the second map is the smallest closed normal subgroup containing the image of the first.

```lean
theorem isExactSequence_etaleFundamentalGroupMap_of_properFlat {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [IsProper f] (hfp : FinitePresentation f) [GeometricallyConnected f]
    [GeometricallyReduced f] [ConnectedSpace ↥S] (s : GeometricPoint S)
    (z : GeometricPoint (pullback f s.hom)) :
    letI : LocallyOfFinitePresentation f := hfp.1
    letI : ConnectedSpace ↥X := GeometricallyConnected.connectedSpace f f.isOpenMap
    letI : ConnectedSpace ↥(pullback f s.hom) :=
      connectedSpace_pullback_geometricPoint_of_geometricallyConnected f s
    IsExactSequence (etaleFundamentalGroupMap (pullback.fst f s.hom) z)
      (etaleFundamentalGroupMap f (z.map (pullback.fst f s.hom)))
```

**`AlgebraicGeometry.surjective_etaleFundamentalGroupMap_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProperFlatHomotopySequence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProperFlatHomotopySequence.lean#L123). The attribute's comment: “surjectivity of `π₁(X) → π₁(S)`, the assertion `→ 1` of the homotopy sequence; triviality of the composite and exactness at `π₁(X)` are separate”. References: SGA 1 XIII (4.4), “(X)”.

> For a flat proper morphism of finite presentation with geometrically connected and
> geometrically reduced fibres over a connected base, the fundamental group of the total space maps
> onto the fundamental group of the base, at the base points coming from a geometric point of a
> geometric fibre.

```lean
theorem surjective_etaleFundamentalGroupMap_of_properFlat {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [IsProper f] (hfp : FinitePresentation f) [GeometricallyConnected f]
    [GeometricallyReduced f] [ConnectedSpace ↥S] (s : GeometricPoint S)
    (z : GeometricPoint (pullback f s.hom)) :
    letI : LocallyOfFinitePresentation f := hfp.1
    letI : ConnectedSpace ↥X := GeometricallyConnected.connectedSpace f f.isOpenMap
    Function.Surjective (etaleFundamentalGroupMap f (z.map (pullback.fst f s.hom)))
```

**`AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProperFlatHomotopySequence.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProperFlatHomotopySequence.lean#L192). The attribute's comment: “triviality of the composite `π₁(X_s) → π₁(X) → π₁(S)`, the complex condition of the homotopy sequence; surjectivity and exactness at `π₁(X)` are separate”.

> For a flat proper morphism of finite presentation with geometrically connected and
> geometrically reduced fibres over a connected base, the composite of the maps on fundamental
> groups from a geometric fibre to the total space and from there to the base is trivial.

```lean
theorem etaleFundamentalGroupMap_comp_eq_one_of_properFlat {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [IsProper f] (hfp : FinitePresentation f) [GeometricallyConnected f]
    [GeometricallyReduced f] [ConnectedSpace ↥S] (s : GeometricPoint S)
    (z : GeometricPoint (pullback f s.hom)) :
    letI : LocallyOfFinitePresentation f := hfp.1
    letI : ConnectedSpace ↥X := GeometricallyConnected.connectedSpace f f.isOpenMap
    letI : ConnectedSpace ↥(pullback f s.hom) :=
      connectedSpace_pullback_geometricPoint_of_geometricallyConnected f s
    (etaleFundamentalGroupMap f (z.map (pullback.fst f s.hom))).toMonoidHom.comp
        (etaleFundamentalGroupMap (pullback.fst f s.hom) z).toMonoidHom = 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.15, Tag 0BUM](https://stacks.math.columbia.edu/tag/0BUM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
