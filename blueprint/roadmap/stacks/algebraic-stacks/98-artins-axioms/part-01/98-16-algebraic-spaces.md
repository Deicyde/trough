---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_of_artinAxioms, Deformation.Artin.isAlgebraicSpace_of_injective_of_artinAxioms
statement: formalized
proof: formalized
---

# 98.16 Algebraic spaces

Section 98.16 of the Stacks Project, [Tag 07Y0](https://stacks.math.columbia.edu/tag/07Y0). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07Y1, a proposition

[Tag 07Y1](https://stacks.math.columbia.edu/tag/07Y1) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_artinAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ArtinAxiomsAlgebraicSpace.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ArtinAxiomsAlgebraicSpace.lean#L442).

> **Stacks 07Y1 (Artin's axioms for algebraic spaces).** Let `S` be a locally Noetherian scheme
> and `F` a set-valued functor on the big fppf site of `S`. Assume that
>
> 1. the diagonal `Δ : F ⟶ F × F` is representable by algebraic spaces,
> 2. `F` satisfies Artin's axioms of Section 07XZ: [-1] the cardinalities `|F(Spec k)|`, for `k`
>    running over the finite type fields over `S`, are bounded by the size of one object of the
>    site; [0] `F` is a sheaf for the étale topology; [1] `F` is limit preserving (Stacks 049J);
>    [2] `F` satisfies the Rim–Schlessinger condition; [3] every tangent space of `F` at a finite
>    type field-valued point is finite dimensional; [4] every formal object of `F` is effective;
>    [5] `F` satisfies openness of versality — axioms [2]–[5] read, as in Section 07XZ, on the
>    category fibred in sets `𝒮_F`, and
> 3. the local rings `𝒪_{S,s}` at the finite type points `s` of `S` are G-rings.
>
> Then `F` is an algebraic space.
>
> Axiom [5] is written out rather than through `AlgebraicGeometry.IsOpenVersality`, which asks its
> fibred category to be fibred in groupoids over all schemes over `S` and so cannot hold for a
> category over the bounded big fppf site; the written-out form is the source's definition.
>
> The proof is `AlgebraicGeometry.Space.isAlgebraicSpace_isoClassPresheafModel_of_artinAxioms` for
> `𝒮_F`, whose presheaf of isomorphism classes is `F`, after the translations of Section 07XZ.

```lean
theorem isAlgebraicSpace_of_artinAxioms [IsLocallyNoetherian S]
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (diag F))
    (hsize : ∃ T : BigFppfOver B S hS,
      ∀ (U : BigFppfOver B S hS) (k : Type u) [Field k],
        U.left.1 = Spec (.of k) → Deformation.Artin.IsFiniteTypeOver B S hS U →
          Cardinal.mk (F.obj (op U)) ≤ T.left.1.size)
    (hF : Presheaf.IsSheaf ((AlgebraicGeometry.etaleTopology B).over (B.obj hS)) F)
    (hlimit : AlgebraicGeometry.LimitPreserving.{u, u, u, u} (BigFppfOver.toScheme B S hS) F)
    (hRS : Deformation.Artin.SatisfiesRS B S hS (fibredCategory B S hS F).val.p
      (fibredCategory B S hS F).property)
    (htangent : HasFiniteDimensionalTangentSpaces B S hS (fibredCategory B S hS F))
    (heffective : ∀ ξ : Deformation.Artin.FormalObject B S hS (fibredCategory B S hS F).val.p,
      Deformation.Artin.FormalObject.IsEffective B S hS (fibredCategory B S hS F).val.p
        (fibredCategory B S hS F).property ξ)
    (hopen : ∀ U : Over S, LocallyOfFiniteType U.hom →
      ∀ (y : (fibredCategory B S hS F).val.obj)
        (hy : ((fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion).obj y = U)
        (u : U.left),
        AlgebraicGeometry.IsFiniteTypePoint u →
        Deformation.Artin.IsVersalAt U ((fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion)
          u y hy →
        ∃ V : U.left.Opens, u ∈ V.1 ∧
          ∀ u' : U.left, u' ∈ V.1 →
            AlgebraicGeometry.IsFiniteTypePoint u' →
            Deformation.Artin.IsVersalAt U
              ((fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion) u' y hy)
    (hG : ∀ s : S, AlgebraicGeometry.IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s)) :
    IsAlgebraicSpace B S hS F
```

## Tag 07Y2, a lemma

[Tag 07Y2](https://stacks.math.columbia.edu/tag/07Y2) in the Stacks Project.

**`Deformation.Artin.isAlgebraicSpace_of_injective_of_artinAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/AlgebraicSpaceCriterionInjective.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/AlgebraicSpaceCriterionInjective.lean#L358).

> **Stacks 07Y2.** Let `S` be a locally Noetherian scheme and `a : F ⟶ G` a transformation of
> functors `(Sch/S)_{fppf}^{opp} ⟶ Sets`. Assume that
>
> 1. `a` is injective;
> 2. `F` satisfies axioms [0] (`F` is an étale sheaf), [1] (`F` is limit preserving), [2]
>    (condition (RS) for `F`), [4] (every formal object of `𝒮_F` is effective) and [5]
>    (openness of versality for `𝒮_F`);
> 3. `𝒪_{S,s}` is a G-ring for every finite type point `s` of `S`;
> 4. `G` is an algebraic space locally of finite type over `S`.
>
> Then `F` is an algebraic space.
>
> As in the source, the proof applies Stacks 07Y1 to `F`: the diagonal of `F` is the base change of
> the diagonal of `G` along `a × a`, hence representable; axiom [3] holds for `F` because
> `a` induces fully faithful maps of predeformation categories into those of `𝒮_G`, whose tangent
> spaces are finite-dimensional by Stacks 07X1; and the set-theoretic condition [-1] holds for `F`
> because it holds for the algebraic space `G` and `F(U) ⟶ G(U)` is injective.

```lean
theorem isAlgebraicSpace_of_injective_of_artinAxioms [IsLocallyNoetherian S]
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G)
    (ha : ∀ U, Function.Injective (a.app U))
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    (hlim : LimitPreserving.{u, u, u, u, u + 1} (BigFppfOver.toScheme B S hS) F)
    (hRS : SatisfiesRSFunctor B S hS F)
    (heff : ∀ ξ : FormalObject B S hS (Stack.fibredCategory B S hS F).val.p,
      FormalObject.IsEffective B S hS (Stack.fibredCategory B S hS F).val.p
        (Stack.fibredCategory B S hS F).property ξ)
    (hopen : ∀ (U : Over S), LocallyOfFiniteType U.hom →
      ∀ (x : (Stack.fibredCategory B S hS F).val.obj)
        (hx : ((Stack.fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion).obj x = U)
        (u₀ : U.left), IsFiniteTypePoint u₀ →
        IsVersalAt U ((Stack.fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion) u₀ x hx →
        ∃ W : U.left.Opens, u₀ ∈ W.1 ∧ ∀ u : U.left, u ∈ W.1 → IsFiniteTypePoint u →
          IsVersalAt U ((Stack.fibredCategory B S hS F).val.p ⋙ Over.post B.inclusion) u x hx)
    (hGring : ∀ s : S, IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s))
    (hG : IsAlgebraicSpace B S hS G)
    (hGft : Space.IsLocallyOfFiniteType B S hS (terminal.from G)) :
    IsAlgebraicSpace B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.16, Tag 07Y0](https://stacks.math.columbia.edu/tag/07Y0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
