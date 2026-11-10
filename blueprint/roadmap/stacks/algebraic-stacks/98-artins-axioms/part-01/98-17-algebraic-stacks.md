---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_of_artinAxioms, AlgebraicGeometry.Stack.isAlgebraicStack_of_artinAxioms_of_secondDiagonal
statement: formalized
proof: formalized
---

# 98.17 Algebraic stacks

Section 98.17 of the Stacks Project, [Tag 07Y3](https://stacks.math.columbia.edu/tag/07Y3). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07Y4, a lemma

[Tag 07Y4](https://stacks.math.columbia.edu/tag/07Y4) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_artinAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ArtinCriterion/Algebraicity.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ArtinCriterion/Algebraicity.lean#L429).

> **Stacks 07Y4 (Artin's criterion).** Let `S` be a locally Noetherian scheme and let `𝒳` be a
> category fibred in groupoids over the big fppf site of `S`. Assume that
>
> 1. the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces,
> 2. `𝒳` satisfies axioms [-1], [0], [1], [2] and [3]: the set-theoretic bound of Stacks 07Y3
>    (`hsize`), the stack condition for the étale topology (`hstack`), limit preservation
>    (`hlimit`), the Rim–Schlessinger condition (`hRS`) and finite dimensionality of tangent spaces
>    (`htangent`),
> 3. every formal object of `𝒳` is effective,
> 4. `𝒳` satisfies openness of versality, and
> 5. `𝒪_{S, s}` is a G-ring for all finite type points `s` of `S`.
>
> Then `𝒳` is an algebraic stack.
>
> Axiom [0] is the source's: `𝒳` is a stack in groupoids for the étale topology. The proof is the
> source's: Stacks 07XY produces, through every finite type field-valued object, a smooth finite type
> neighbourhood; `AlgebraicGeometry.Stack.isAlgebraicStack_of_hasSmoothFiniteTypeNeighborhoods`
> assembles them into a surjective smooth atlas; and Stacks 076V
> (`AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale_of_smooth`), where the
> étale stack condition of axiom [0] is used, makes `𝒳` an fppf stack and hence an algebraic stack.
>
> Of axiom [3] only the tangent-space half is asked for, which is all Stacks 07XY uses; the index
> universe of the stack condition in the conclusion is free.

```lean
public theorem isAlgebraicStack_of_artinAxioms [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (AlgebraicGeometry.BigFppfOver B S hS))
    (hdiag : HasRepresentableDiagonal B S hS 𝒳)
    (hsize : IsSizeBounded B S hS 𝒳)
    (hstack : 𝒳.val.p.IsStackInGroupoids.{u + 1}
      ((AlgebraicGeometry.etaleTopology B).over (B.obj hS)))
    (hlimit : Deformation.Artin.IsLimitPreserving.{u, u, u, max (u + 1) v w, max u v} B S hS 𝒳)
    (hRS : Deformation.Artin.SatisfiesRS B S hS 𝒳.val.p 𝒳.property)
    (htangent : HasFiniteDimensionalTangentSpaces B S hS 𝒳)
    (heffective : ∀ ξ : Deformation.Artin.FormalObject B S hS 𝒳.val.p,
      Deformation.Artin.FormalObject.IsEffective B S hS 𝒳.val.p 𝒳.property ξ)
    (hopen : ∀ U : Over S, LocallyOfFiniteType U.hom →
      ∀ (y : 𝒳.val.obj) (hy : (𝒳.val.p ⋙ Over.post B.inclusion).obj y = U) (u : U.left),
        AlgebraicGeometry.IsFiniteTypePoint u →
        Deformation.Artin.IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u y hy →
        ∃ V : U.left.Opens, u ∈ V.1 ∧
          ∀ u' : U.left, u' ∈ V.1 →
            AlgebraicGeometry.IsFiniteTypePoint u' →
            Deformation.Artin.IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u' y hy)
    (hG : ∀ s : S, AlgebraicGeometry.IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s)) :
    IsAlgebraicStack.{u, z, max u v, max (u + 1) v w} B S hS 𝒳.val
```

## Tag 07Y5, a proposition

[Tag 07Y5](https://stacks.math.columbia.edu/tag/07Y5) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_artinAxioms_of_secondDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ArtinAxiomsSecondDiagonal.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ArtinAxiomsSecondDiagonal.lean#L396).

> **Stacks 07Y5 (Artin's axioms, second diagonal form).** Let `S` be a locally Noetherian
> scheme and `𝒳` a category fibred in groupoids over the big fppf site of `S`. Assume that
>
> 1. the second diagonal `Δ_Δ : 𝒳 ⟶ 𝒳 ×_{𝒳 × 𝒳} 𝒳` is representable by algebraic spaces,
> 2. `𝒳` satisfies Artin's axioms of Section 07XJ: [-1] the cardinalities of the sets of
>    isomorphism classes of objects and of the sets of arrows of the fibres of `𝒳` over the finite
>    type fields over `S` are bounded by the size of one object of the site; [0] `𝒳` is a stack
>    in groupoids for the étale topology; [1] `𝒳` is limit preserving; [2] `𝒳` satisfies the
>    Rim–Schlessinger condition; [3] the tangent spaces and the infinitesimal automorphism spaces
>    of `𝒳` at the finite type field-valued points are finite dimensional; [4] the functor of
>    Stacks 07X6 from objects over complete local bases to formal objects is an equivalence;
>    [5] `𝒳` and `Δ : 𝒳 ⟶ 𝒳 × 𝒳` satisfy openness of versality (Stacks 07XQ: for `Δ`, for every
>    scheme `V` locally of finite type over `S` and every point `y` of `𝒳 × 𝒳` over `V`, the
>    2-fibre product `(Sch/V)_{fppf} ×_{y, 𝒳 × 𝒳, Δ} 𝒳` has openness of versality), and
> 3. the local rings `𝒪_{S,s}` at the finite type points `s` of `S` are G-rings.
>
> Then `𝒳` is an algebraic stack.
>
> Openness of versality is written out (`Deformation.Artin.HasOpenVersality`) rather than through
> `Deformation.Artin.IsOpenVersality`, whose fibred-in-groupoids hypothesis over all schemes over
> `S` cannot hold for a category over the bounded big fppf site. A point `y` of `𝒳 × 𝒳` over `V` is
> given, by the 2-Yoneda lemma, as a 1-morphism `(Sch/V)_{fppf} ⟶ 𝒳 × 𝒳` over the site.
>
> The proof is the source's:
> `AlgebraicGeometry.Stack.hasRepresentableDiagonal_of_artinAxioms_of_secondDiagonal` makes the
> diagonal representable (Stacks 07WH, 07WG and Proposition 07Y1 for the functors `Y`), and
> Lemma 07Y4 concludes.

```lean
theorem isAlgebraicStack_of_artinAxioms_of_secondDiagonal [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (hΔΔ : IsRepresentableByAlgebraicSpaces B S hS
      (relativeDiagonalBasedFunctor B S hS 𝒳 (CatFiberedInGroupoids.product 𝒳 𝒳)
        (diagonalBasedFunctor B S hS 𝒳)))
    (hsize : ∃ T : BigFppfOver B S hS,
      ∀ (U : BigFppfOver B S hS) (k : Type u) [Field k],
        U.left.1 = Spec (.of k) → Deformation.Artin.IsFiniteTypeOver B S hS U →
        Cardinal.lift.{u, u + 1}
            (Cardinal.mk (Quotient (isIsomorphicSetoid (𝒳.val.p.Fiber U)))) ≤
          Cardinal.lift.{u + 1, u} T.left.1.size ∧
        Cardinal.lift.{u, u + 1} (Cardinal.mk (Σ a b : 𝒳.val.p.Fiber U, a ⟶ b)) ≤
          Cardinal.lift.{u + 1, u} T.left.1.size)
    (hstack : 𝒳.val.p.IsStackInGroupoids.{u + 1}
      ((AlgebraicGeometry.etaleTopology B).over (B.obj hS)))
    (hlimit : Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳)
    (hRS : Deformation.Artin.SatisfiesRS B S hS 𝒳.val.p 𝒳.property)
    (htangent : HasFiniteDimensionalTangentSpaces B S hS 𝒳)
    (hInf : Deformation.Artin.HasFiniteDimensionalInfinitesimalAutomorphismsOf B S hS 𝒳.val.p)
    (happrox : (Deformation.Artin.approximationFunctor B S hS 𝒳.val.p 𝒳.property).IsEquivalence)
    (hopen : Deformation.Artin.HasOpenVersality (𝒳.val.p ⋙ Over.post B.inclusion))
    (hopenΔ : ∀ V : BigFppfOver B S hS, LocallyOfFiniteType (B.inclusion.map V.hom) →
      ∀ (y : BigFppfOver B V.left.1 V.left.2 ⥤ (CatFiberedInGroupoids.product 𝒳 𝒳).val.obj),
        y ⋙ (CatFiberedInGroupoids.product 𝒳 𝒳).val.p = Over.map V.hom →
        Deformation.Artin.HasOpenVersality
          (TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p
            (CatFiberedInGroupoids.product 𝒳 𝒳).val.p y
            (diagonalBasedFunctor B S hS 𝒳).toFunctor ⋙ Over.post B.inclusion))
    (hG : ∀ s : S, AlgebraicGeometry.IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s)) :
    IsAlgebraicStack.{u, z, u, u + 1} B S hS 𝒳.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.17, Tag 07Y3](https://stacks.math.columbia.edu/tag/07Y3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
