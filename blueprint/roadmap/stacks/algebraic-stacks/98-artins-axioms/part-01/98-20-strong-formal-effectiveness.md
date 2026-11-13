---
declaration: section
origin: cited
lean: Deformation.Artin.exists_sequence_firstOrderThickenings_without_localRetraction, Deformation.Artin.IsEffectiveSystem, Deformation.Artin.IsStronglyFormallyEffective, Deformation.Artin.isOpenVersality_of_isSquareZeroEffective, Deformation.Artin.isOpenVersality_diagonal_of_isFullyFaithfulOnSquareZeroTowers
statement: formalized
proof: formalized
---

# 98.20 Strong formal effectiveness

Section 98.20 of the Stacks Project, [Tag 0CXR](https://stacks.math.columbia.edu/tag/0CXR). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G2S, a lemma

[Tag 0G2S](https://stacks.math.columbia.edu/tag/0G2S) in the Stacks Project.

**`Deformation.Artin.exists_sequence_firstOrderThickenings_without_localRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/NonversalThickeningSequence.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/NonversalThickeningSequence.lean#L1354).

> **Stacks Project, Tag 0G2S.** Let `𝒳` be a category fibred in groupoids over the big
> fppf site of a locally Noetherian scheme `S`, satisfying (RS*), and let `x` be an object of
> `𝒳` over an affine scheme `U` of finite type over `S`. Let `u 0, u 1, …` be finite type
> points of `U` with no specializations between distinct ones, at none of which `x` is versal.
> Then there are morphisms `x ⟶ x₁ ⟶ x₂ ⟶ …` of `𝒳` over `U ⟶ U₁ ⟶ U₂ ⟶ …` over `S` such
> that each `U ⟶ Uₙ₊₁` is a first order thickening, the ideal of `Uₙ ⟶ Uₙ₊₁` is the residue
> field `κ(u n)`, and `x ⟶ xₙ₊₁` admits no retraction over any open neighbourhood of `u n`.

```lean
public theorem exists_sequence_firstOrderThickenings_without_localRetraction
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : Type v} [Category.{w} F]
    (p : F ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRSStar B S hS p hp)
    (U : Over S) [IsAffine U.left] [IsLocallyNoetherian S]
    [LocallyOfFiniteType U.hom] [QuasiCompact U.hom]
    (x : F) (hx : (p ⋙ Over.post B.inclusion).obj x = U)
    (u : ℕ → U.left)
    (hfinite : ∀ n, AlgebraicGeometry.IsFiniteTypePoint (u n))
    (hincomparable : ∀ n m, n ≠ m → ¬ (u n ⤳ u m))
    (hnonversal : ∀ n,
      ¬ Deformation.Artin.IsVersalAt U (p ⋙ Over.post B.inclusion) (u n) x hx) :
    let q : F ⥤ Over S := p ⋙ Over.post B.inclusion
    ∃ (xs : ℕ → F)
      (step : ∀ n, xs n ⟶ xs (n + 1))
      (fromX : ∀ n, x ⟶ xs n),
      ∃ hzero : xs 0 = x,
        fromX 0 = eqToHom hzero.symm ∧
        (∀ n, fromX (n + 1) = fromX n ≫ step n) ∧
        (let j : ∀ n, U.left ⟶ (q.obj (xs n)).left :=
          fun n ↦ eqToHom (congrArg Over.left hx).symm ≫ (q.map (fromX n)).left
        ∀ n,
          Stacks.Thickenings.IsFirstOrderThickening (j (n + 1)) ∧
          (let i : (q.obj (xs n)).left ⟶ (q.obj (xs (n + 1))).left :=
              (q.map (step n)).left
           Epi (SheafOfModules.unitToPushforwardObjUnit i.toRingCatSheafHom) ∧
           Nonempty (kernel (SheafOfModules.unitToPushforwardObjUnit
               i.toRingCatSheafHom) ≅
             (Scheme.Modules.pushforward
                 ((q.obj (xs (n + 1))).left.fromSpecResidueField (j (n + 1) (u n)))).obj
               (SheafOfModules.unit (Spec ((q.obj (xs (n + 1))).left.residueField
                 (j (n + 1) (u n)))).ringCatSheaf))) ∧
          (∀ (y : F) (r : y ⟶ xs (n + 1)),
            IsOpenImmersion (q.map r).left →
            (∃ z : (q.obj y).left,
              (q.map r).left z = j (n + 1) (u n)) →
            ∀ (z : F) (t : z ⟶ x) (s : z ⟶ y),
              IsPullback (q.map t).left (q.map s).left
                (q.map (fromX (n + 1))).left (q.map r).left →
              ¬ ∃ β : y ⟶ x,
                s ≫ β = t ∧ t ≫ fromX (n + 1) = s ≫ r))
```

## Tag 0CXT, a remark

[Tag 0CXT](https://stacks.math.columbia.edu/tag/0CXT) in the Stacks Project.

**`Deformation.Artin.IsEffectiveSystem`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/Effectiveness.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/FormalObject/Effectiveness.lean#L63). The attribute's comment: “effectivity\_of\_a\_system\_of\_objects”.

> A diagram in a category over a base is effective over a specified base cocone when
> that cocone comes from a cocone of the objects. In a category fibred in groupoids, the
> lifted maps exhibit the diagram objects as the restrictions of the vertex object.

```lean
public abbrev IsEffectiveSystem {J : Type u₁} [Category.{v₁} J] {X : Type u₂}
    [Category.{v₂} X] {C : Type u₃} [Category.{v₃} C] (p : X ⥤ C) (ξ : J ⥤ X)
    (c : Cocone (ξ ⋙ p)) : Prop
```

**`Deformation.Artin.IsStronglyFormallyEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/Effectiveness.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/FormalObject/Effectiveness.lean#L81). The attribute's comment: “strong\_formal\_effectiveness”.

> Strong formal effectiveness for a category fibred in groupoids over the big
> fppf site of a locally Noetherian scheme.

```lean
public abbrev IsStronglyFormallyEffective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S] {X : Type v} [Category.{w} X]
    (p : X ⥤ BigFppfOver B S hS)
    (_hp : p.IsFiberedInGroupoids) : Prop
```

## Tag 0CXU, a lemma

[Tag 0CXU](https://stacks.math.columbia.edu/tag/0CXU) in the Stacks Project.

**`Deformation.Artin.isOpenVersality_of_isSquareZeroEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessOfVersality.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/OpennessOfVersality.lean#L443).

> **Stacks 0CXU.** Let `S` be a locally Noetherian scheme and `𝒳` a category fibred in
> groupoids over the big fppf site of `S` such that
>
> 1. the diagonal of `𝒳` is representable by algebraic spaces,
> 2. `𝒳` has (RS*),
> 3. `𝒳` is limit preserving,
> 4. systems of objects as in Stacks 0CXT, over inverse systems of algebras whose transition maps
>    are surjective with square-zero kernels, are effective.
>
> Then `𝒳` satisfies openness of versality: if `x` is an object of `𝒳` over a scheme `U` locally of
> finite type over `S`, versal at a finite type point `u₀` of `U`, then `x` is versal at every finite
> type point of an open neighbourhood of `u₀`.
>
> The conclusion is the body of `Deformation.Artin.IsOpenVersality` (Stacks 07XQ), written out; see
> the implementation notes of this file.

```lean
public theorem isOpenVersality_of_isSquareZeroEffective [IsLocallyNoetherian S]
    (hΔ : AlgebraicGeometry.Stack.HasRepresentableDiagonal B S hS 𝒳)
    (hRS : SatisfiesRSStar B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (hlim : IsLimitPreserving.{u, u, u, w, v} B S hS 𝒳)
    (heff : IsSquareZeroEffective B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (U : Over S) (hUft : LocallyOfFiniteType U.hom) (x : 𝒳.val.obj)
    (hx : (𝒳.val.p ⋙ Over.post B.inclusion).obj x = U) (u₀ : U.left)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀)
    (hversal : IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u₀ x hx) :
    ∃ V : U.left.Opens, u₀ ∈ V.1 ∧
      ∀ u ∈ V.1, AlgebraicGeometry.IsFiniteTypePoint u →
        IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u x hx
```

## Tag 0CXV, a remark

[Tag 0CXV](https://stacks.math.columbia.edu/tag/0CXV) in the Stacks Project.

**`Deformation.Artin.isOpenVersality_diagonal_of_isFullyFaithfulOnSquareZeroTowers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/DiagonalOpenness.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/DiagonalOpenness.lean#L81).

> Let `S` be a locally Noetherian scheme and `𝒳` a category fibred in groupoids over the big fppf
> site of `S` whose second diagonal is representable by algebraic spaces, which satisfies (RS*),
> which is limit preserving, and for which the restriction functors
> `𝒳_{Spec lim Rₙ} ⟶ lim 𝒳_{Spec Rₙ}` of square-zero towers are fully faithful. Then the diagonal
> `Δ : 𝒳 ⟶ 𝒳 × 𝒳` satisfies openness of versality: for every scheme `V` locally of finite type over
> `S` and every object `y` of `𝒳 × 𝒳` over `V`, the 2-fibre product
> `(Sch/V)_{fppf} ×_{y, 𝒳 × 𝒳, Δ} 𝒳` satisfies openness of versality — an object over a scheme `U`
> locally of finite type over `V` which is versal at a finite type point `u₀` is versal at every
> finite type point of an open neighbourhood of `u₀`.

```lean
theorem isOpenVersality_diagonal_of_isFullyFaithfulOnSquareZeroTowers
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (AlgebraicGeometry.BigFppfOver B S hS))
    (h1 : AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS
      (AlgebraicGeometry.Stack.relativeDiagonalBasedFunctor B S hS 𝒳
        (CatFiberedInGroupoids.product 𝒳 𝒳)
        (AlgebraicGeometry.Stack.diagonalBasedFunctor B S hS 𝒳)))
    (h2 : SatisfiesRSStar B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (h3 : IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳)
    (h4 : IsFullyFaithfulOnSquareZeroTowers B S hS 𝒳.val.p) :
    ∀ (V : AlgebraicGeometry.BigFppfOver B S hS), LocallyOfFiniteType (B.inclusion.map V.hom) →
      ∀ (y : AlgebraicGeometry.BigFppfOver B V.left.1 V.left.2 ⥤
          (CatFiberedInGroupoids.product 𝒳 𝒳).val.obj),
        y ⋙ (CatFiberedInGroupoids.product 𝒳 𝒳).val.p = Over.map V.hom →
        let q := TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p
          (CatFiberedInGroupoids.product 𝒳 𝒳).val.p y
          (AlgebraicGeometry.Stack.diagonalBasedFunctor B S hS 𝒳).toFunctor ⋙
            Over.post B.inclusion
        ∀ (U : Over V.left.1), LocallyOfFiniteType U.hom →
          ∀ (x : TwoFibreProductOver (Over.map V.hom) 𝒳.val.p
              (CatFiberedInGroupoids.product 𝒳 𝒳).val.p y
              (AlgebraicGeometry.Stack.diagonalBasedFunctor B S hS 𝒳).toFunctor)
            (hx : q.obj x = U) (u₀ : U.left),
            IsFiniteTypePoint u₀ →
            IsVersalAt U q u₀ x hx →
            ∃ W : U.left.Opens, u₀ ∈ W.1 ∧
              ∀ u ∈ W.1, IsFiniteTypePoint u → IsVersalAt U q u x hx
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.20, Tag 0CXR](https://stacks.math.columbia.edu/tag/0CXR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
