---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.boundaryIntervalRepresentable, Stacks.CategoryTheory.Hypercovering.intervalEndpointMap, Stacks.CategoryTheory.Hypercovering.homotopyMatchingSquare, Stacks.CategoryTheory.Hypercovering.exists_homotopy_after_hypercovering_refinement
statement: formalized
proof: formalized
---

# 25.9 Homotopies

Section 25.9 of the Stacks Project, [Tag 01GO](https://stacks.math.columbia.edu/tag/01GO). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01GP, a lemma

[Tag 01GP](https://stacks.math.columbia.edu/tag/01GP) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.boundaryIntervalRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean#L82). The attribute's comment: “the two endpoint copies”.

> Restriction to the two vertices of the interval is represented by the product of two copies
> of a simplicial semi-representable object.

```lean
theorem boundaryIntervalRepresentable
    (L : SimplicialObject (FormalCoproduct.{w} (Over X))) :
    Nonempty (SimplicialObject.IsHomFromSSet (SSet.boundary.{max v w} 1) L (L ⨯ L))
```

**`Stacks.CategoryTheory.Hypercovering.intervalEndpointMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean#L90). The attribute's comment: “the ordered endpoint map”.

> The fixed endpoint-evaluation morphism `Hom(Δ[1], L) ⟶ L × L`. Its two components are, in
> order, the restrictions of the universal interval map to the vertices zero and one.

```lean
noncomputable def intervalEndpointMap
    (L H : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hH : SimplicialObject.IsHomFromSSet Δ[1] L H) :
    { e : H ⟶ L ⨯ L //
      (∀ m : SimplexCategoryᵒᵖ,
        (e ≫ prod.fst).app m =
          (Functor.functorHomEquiv H L Δ[1] (hH.homEquiv (𝟙 H))).app m
            (SSet.stdSimplex.const 1 0 m)) ∧
      (∀ m : SimplexCategoryᵒᵖ,
        (e ≫ prod.snd).app m =
          (Functor.functorHomEquiv H L Δ[1] (hH.homEquiv (𝟙 H))).app m
            (SSet.stdSimplex.const 1 1 m)) }
```

**`Stacks.CategoryTheory.Hypercovering.homotopyMatchingSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/MatchingSquare.lean#L116).

> **Stacks Project, Tag 01GP.** The four matching objects are represented by the corresponding
> simplicial sets, and the `Hom` object of the union is their fibre product. All arrows in the
> fibre product square are those induced by inclusions of simplicial sets.

```lean
theorem homotopyMatchingSquare
    (L : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (H : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hH : SimplicialObject.IsHomFromSSet Δ[1] L H) :
    ∀ n : ℕ, ∃ Q : FormalCoproduct.{w} (Over X),
      let e := (intervalEndpointMap X L H hH).1;
      let m := n + 1;
      let S := SSet.boundary.{max v w} 1;
      let T := SSet.boundary.{max v w} m;
      let U := S.unionProd T;
      let F := coyoneda ⋙
        (Functor.whiskeringLeft SimplexCategoryᵒᵖ
          (FormalCoproduct.{w} (Over X)) (Type (max v w))).obj L;
      ∃ (hFull : (F ⋙ coyoneda.obj (op (Δ[1] ⊗ Δ[m]))).RepresentableBy (H _⦋m⦌))
        (hTop : (F ⋙ coyoneda.obj (op (Δ[1] ⊗ (T : SSet)))).RepresentableBy
          (((SimplicialObject.cosk n).obj H) _⦋m⦌))
        (hBottom : (F ⋙ coyoneda.obj (op ((S : SSet) ⊗ Δ[m]))).RepresentableBy
          ((L ⨯ L) _⦋m⦌))
        (hRight : (F ⋙ coyoneda.obj (op ((S : SSet) ⊗ (T : SSet)))).RepresentableBy
          (((SimplicialObject.cosk n).obj (L ⨯ L)) _⦋m⦌))
        (hUnion : (F ⋙ coyoneda.obj (op (U : SSet))).RepresentableBy Q),
        let comparison := hUnion.homEquiv.symm (U.ι ≫ hFull.homEquiv (𝟙 _));
        (e.app (op ⦋m⦌) =
          hBottom.homEquiv.symm ((S.ι ▷ Δ[m]) ≫ hFull.homEquiv (𝟙 _))) ∧
        ((((SimplicialObject.coskAdj n).unit.app H).app (op ⦋m⦌)) =
          hTop.homEquiv.symm ((Δ[1] ◁ T.ι) ≫ hFull.homEquiv (𝟙 _))) ∧
        ((((SimplicialObject.coskAdj n).unit.app (L ⨯ L)).app (op ⦋m⦌)) =
          hRight.homEquiv.symm (((S : SSet) ◁ T.ι) ≫ hBottom.homEquiv (𝟙 _))) ∧
        ((((SimplicialObject.cosk n).map e).app (op ⦋m⦌)) =
          hRight.homEquiv.symm ((S.ι ▷ (T : SSet)) ≫ hTop.homEquiv (𝟙 _))) ∧
        (comparison ≫ hTop.homEquiv.symm
          (SSet.Subcomplex.unionProd.ι₁ S T ≫ hUnion.homEquiv (𝟙 Q)) =
          ((SimplicialObject.coskAdj n).unit.app H).app (op ⦋m⦌)) ∧
        (comparison ≫ hBottom.homEquiv.symm
          (SSet.Subcomplex.unionProd.ι₂ S T ≫ hUnion.homEquiv (𝟙 Q)) =
          e.app (op ⦋m⦌)) ∧
        IsPullback
          (hTop.homEquiv.symm (SSet.Subcomplex.unionProd.ι₁ S T ≫
            hUnion.homEquiv (𝟙 Q)))
          (hBottom.homEquiv.symm (SSet.Subcomplex.unionProd.ι₂ S T ≫
            hUnion.homEquiv (𝟙 Q)))
          (hRight.homEquiv.symm ((S.ι ▷ (T : SSet)) ≫ hTop.homEquiv (𝟙 _)))
          (hRight.homEquiv.symm (((S : SSet) ◁ T.ι) ≫ hBottom.homEquiv (𝟙 _)))
```

## Tag 01GS, a lemma

[Tag 01GS](https://stacks.math.columbia.edu/tag/01GS) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_homotopy_after_hypercovering_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/Homotopy.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringAndHomotopies/Homotopy.lean#L366).

> **Stacks Project, Tag 01GS.** Two morphisms between hypercoverings become simplicially
> homotopic after precomposition with a morphism from a further hypercovering.

```lean
theorem exists_homotopy_after_hypercovering_refinement (J : Pretopology C)
    [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    {K L : SimplicialObject (FormalCoproduct.{w} (Over X))}
    (hK : IsHypercovering J K) (hL : IsHypercovering J L) (a b : K ⟶ L) :
    ∃ (K' : SimplicialObject (FormalCoproduct.{w} (Over X))) (c : K' ⟶ K),
      IsHypercovering J K' ∧
        ∃ h : K'.copower Δ[1] ⟶ L, SimplicialObject.IsHomotopy h (c ≫ a) (c ≫ b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.9, Tag 01GO](https://stacks.math.columbia.edu/tag/01GO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
