---
declaration: section
origin: cited
lean: Stacks.Intersection.Diagonal.derivedDiagonalIsos, Stacks.Intersection.Diagonal.torDiagonalIso, Stacks.Intersection.ReductionToDiagonal.intersectProperly_exteriorProduct_diagonalCycle, Stacks.Intersection.ReductionToDiagonal.reductionToDiagonal, Stacks.Intersection.Diagonal.intersectionMultiplicity_pos_of_isRegular, Stacks.Intersection.ReductionToDiagonal.intersectProperly_coherentSheafCycle, Stacks.Intersection.ReductionToDiagonal.torFormula_integerDimension, Stacks.Intersection.ReductionToDiagonal.torFormula
statement: formalized
proof: formalized
---

# 43.19 Reduction to the diagonal

Section 43.19 of the Stacks Project, [Tag 0B0A](https://stacks.math.columbia.edu/tag/0B0A). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B0T, a lemma

[Tag 0B0T](https://stacks.math.columbia.edu/tag/0B0T) in the Stacks Project.

**`Stacks.Intersection.Diagonal.derivedDiagonalIsos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/DerivedDiagonal.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/DerivedDiagonal.lean#L259). The attribute's comment: “(2)”.

> **[Stacks, Tag 0B0T], part (2).** Let `f : X ⟶ S` be a separated morphism of schemes (for
> instance a variety over a field) with projections `pr₁, pr₂ : X ×_S X ⟶ X` and diagonal `Δ`.
> For `K, M ∈ D(𝒪_X)` there are canonical isomorphisms, natural in `(K, M)`,
>
> * `LΔ^*(Lpr₁^*K ⊗^L Lpr₂^*M) ≅ K ⊗^L M` (the first component, `diagonalRestrictionIso`), and
> * `𝒪_Δ ⊗^L (Lpr₁^*K ⊗^L Lpr₂^*M) ≅ Δ_*(K ⊗^L M)` (the second, `diagonalTensorIso`),
>
> where `𝒪_Δ = Δ_*𝒪_X` is placed in degree zero. They are the composites of canonical maps recorded
> by `derivedRestrictionIso_hom` and `diagonalTensorIso_hom`: the comparison of [Stacks, Tag 079U]
> with the composition isomorphisms of [Stacks, Tag 0D5S], and the projection formula of
> [Stacks, Tag 0B55]. The source's hypotheses (`X` a nonsingular variety, `K, M ∈ D_QCoh(𝒪_X)`)
> are not needed beyond separatedness; `D_QCoh(𝒪_X)` being a full subcategory, these are in
> particular isomorphisms in `D_QCoh`.

```lean
def derivedDiagonalIsos :
    (exteriorDerivedTensor (pullback.fst f f).toLRSHom.toShHom (pullback.snd f f).toLRSHom.toShHom ⋙
        derivedPullback (pullback.diagonal f).toLRSHom.toShHom ≅
      Functor.uncurry.obj (derivedTensorProductFunctor X.toRingedSpace.sheaf)) ×
    (exteriorDerivedTensor (pullback.fst f f).toLRSHom.toShHom (pullback.snd f f).toLRSHom.toShHom ⋙
        (derivedTensorProductFunctor (pullback f f).toRingedSpace.sheaf).obj
          ((DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing (pullback f f).toRingedSpace)) 0).obj
          (diagonalStructureModule f)) ≅
      Functor.uncurry.obj (derivedTensorProductFunctor X.toRingedSpace.sheaf) ⋙
        diagonalPushforward f)
```

**`Stacks.Intersection.Diagonal.torDiagonalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/TorDiagonal.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/TorDiagonal.lean#L341). The attribute's comment: “(1)”.

> **[Stacks, Tag 0B0T], part (1).** Let `k` be a field and `f : X ⟶ Spec k` separated (for
> instance a nonsingular variety), with projections `pr₁, pr₂` and diagonal `Δ`. For
> `𝒪_X`-modules `F` and `G` with `G` quasi-coherent (for instance coherent) there are canonical
> isomorphisms
>
> `Tor_p^{𝒪_{X ×_k X}}(𝒪_Δ, pr₁^*F ⊗ pr₂^*G) ≅ Δ_* Tor_p^{𝒪_X}(F, G)`.
>
> The isomorphism is `H^{-p}` of the composite of the Tor-independence isomorphism
> `exteriorDerivedTensorSingleIso` (inverted, in the second factor) and the second isomorphism of
> part (2), `diagonalTensorIso`, followed by the commutation of the exact functor `Δ_*` with
> cohomology.

```lean
def torDiagonalIso (p : ℤ) :
    Stacks.Cohomology.tor (pullback f f).toRingedSpace p (diagonalStructureModule f)
        (exteriorTensor f F G) ≅
      (modulePushforward (pullback.diagonal f).toLRSHom.toShHom).obj
        (Stacks.Cohomology.tor X.toRingedSpace p F G)
```

## Tag 0B0U, a lemma

[Tag 0B0U](https://stacks.math.columbia.edu/tag/0B0U) in the Stacks Project.

**`Stacks.Intersection.ReductionToDiagonal.intersectProperly_exteriorProduct_diagonalCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/ProperIntersection.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/ProperIntersection.lean#L176). The attribute's comment: “part (1): `α × β` and `[Δ]` intersect properly, for any variety over a field: no nonsingularity is used. Parts (2) and (3), `Δ_*(α · β) = [Δ] · α × β` and `pr_{1,*}([Δ] · α × β) = α · β`, are not stated, because the intersection product of two cycles on a nonsingular variety is not defined in this library; their proof also needs the higher `Tor_i` of Stacks 0B0T, which is `Stacks.Intersection.Diagonal.torDiagonalIso`”.

> Let `X` be a variety, let `α` be an `r`-cycle and `β` an `s`-cycle on `X`, and assume `α` and
> `β` intersect properly. Then the exterior product `α × β` and the diagonal cycle `[Δ]` intersect
> properly on `X ×_k X`.

```lean
theorem intersectProperly_exteriorProduct_diagonalCycle (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] (r s : ℕ)
    (α : CycleGroup (fieldChowSituation k) f (r : ℤ))
    (β : CycleGroup (fieldChowSituation k) f (s : ℤ))
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1) :
    AlgebraicCycle.IntersectProperly
      (exteriorProduct (fieldChowSituation k) f f (r : ℤ) (s : ℤ) α β).1
      (diagonalCycle f)
```

**`Stacks.Intersection.ReductionToDiagonal.reductionToDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/Whole.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/Whole.lean#L424). The attribute's comment: “all three parts, for a nonsingular variety over an algebraically closed field — the chapter's convention, and what makes a product of two closed subvarieties a closed subvariety (Stacks 05P3), which part (2) needs. (1) `α × β` and `[Δ]` intersect properly; (2) `Δ_*(α · β) = [Δ] · α × β` on `X ×_k X`; (3) `pr_{1,*}([Δ] · α × β) = α · β` when `X` is proper over the field, the source's own hypothesis for that part. Both intersection products are the Section 43.17 product of Stacks 0B08 computed by the Tor formula of Section 43.14, `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct`, in the source's dimension `r + s - dim X`; proper pushforward is `Stacks.Chow.properPushforward` (Stacks 02R4). The hypotheses are exactly the source's: the natural number `dX` holding `dim X`, the regularity of `X ×_k X` and the delta-dimension of each of the two products are all asserted among the conclusions. The dimensions `r` and `s` are natural numbers, as the dimensions of the subvarieties the cycles are supported on.”.

> **Stacks Project, Tag 0B0U: reduction to the diagonal.** Let `X` be a nonsingular variety
> over an algebraically closed field `k`. Let `α` be an `r`-cycle and `β` an `s`-cycle on `X`, and
> assume `α` and `β` intersect properly. Then
>
> 1. the exterior product `α × β` and the cycle `[Δ]` of the diagonal intersect properly on
>    `X ×_k X`;
> 2. `Δ_*(α · β) = [Δ] · α × β` as cycles on `X ×_k X`;
> 3. if `X` is proper over `k` then `pr_{1,*}([Δ] · α × β) = α · β`, for `pr₁` the first
>    projection.
>
> The intersection products are the ones of Section 43.17 computed by the Tor formula of Section
> 43.14, `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct` (Tag 0B08), in the
> expected dimension `r + s - dim X`. Everything beyond the source's hypotheses is asserted among
> the conclusions rather than assumed: the natural number `dX` carrying the dimension of `X`, which
> exists by `AlgebraicGeometry.exists_topologicalKrullDim_eq_natCast_of_isVariety` and is unique,
> so that the index `r + s - dX` is the source's `r + s - dim X`; the regularity of `X ×_k X`; and
> the delta-dimension of each of the two intersection products, which the two pushforwards need of
> their argument.

```lean
theorem reductionToDiagonal (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [IsVariety k f] (hX : IsRegular X) (r s : ℕ)
    (α : CycleGroup (fieldChowSituation k) f (r : ℤ))
    (β : CycleGroup (fieldChowSituation k) f (s : ℤ))
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    haveI : IsLocallyNoetherian (pullback f f : Scheme.{u}) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst f f ≫ f)
    letI : IsClosedImmersion (pullback.diagonal f) := IsSeparated.isClosedImmersion_diagonal
    AlgebraicCycle.IntersectProperly
        (exteriorProduct (fieldChowSituation k) f f (r : ℤ) (s : ℤ) α β).1 (diagonalCycle f) ∧
      ∃ dX : ℕ, topologicalKrullDim X = (dX : WithBot ℕ∞) ∧
        ∃ hP : IsRegular (pullback f f : Scheme.{u}),
          ∃ hprod : torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX
              ((r : ℤ) + (s : ℤ) - (dX : ℤ)) α.1 β.1 ∈
              cyclesOfDimension (fieldChowSituation k) f ((r : ℤ) + (s : ℤ) - (dX : ℤ)),
            (properPushforward (fieldChowSituation k) f (pullback.fst f f ≫ f)
                  (pullback.diagonal f) (diagonal_comp_fst_comp f)
                  ((r : ℤ) + (s : ℤ) - (dX : ℤ)) ⟨_, hprod⟩).1 =
                torFormulaCycleIntersectionProduct (fieldChowSituation k) (pullback.fst f f ≫ f)
                  hP ((r : ℤ) + (s : ℤ) - (dX : ℤ)) (diagonalCycle f)
                  (exteriorProduct (fieldChowSituation k) f f (r : ℤ) (s : ℤ) α β).1 ∧
              ∀ [IsProper f],
                ∃ hdiag : torFormulaCycleIntersectionProduct (fieldChowSituation k)
                    (pullback.fst f f ≫ f) hP ((r : ℤ) + (s : ℤ) - (dX : ℤ)) (diagonalCycle f)
                    (exteriorProduct (fieldChowSituation k) f f (r : ℤ) (s : ℤ) α β).1 ∈
                    cyclesOfDimension (fieldChowSituation k) (pullback.fst f f ≫ f)
                      ((r : ℤ) + (s : ℤ) - (dX : ℤ)),
                  (properPushforward (fieldChowSituation k) (pullback.fst f f ≫ f) f
                      (pullback.fst f f) rfl ((r : ℤ) + (s : ℤ) - (dX : ℤ)) ⟨_, hdiag⟩).1 =
                    torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX
                      ((r : ℤ) + (s : ℤ) - (dX : ℤ)) α.1 β.1
```

## Tag 0B0V, a proposition

[Tag 0B0V](https://stacks.math.columbia.edu/tag/0B0V) in the Stacks Project.

**`Stacks.Intersection.Diagonal.intersectionMultiplicity_pos_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/DiagonalPositivity.lean, line 631](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/DiagonalPositivity.lean#L631). The attribute's comment: “the whole proposition, for a nonsingular variety over an algebraically closed field — the chapter's own convention, Tag 0AZ8. `V` and `W` are closed subschemes of `X`, presented by closed immersions, so the statement proved is more general than the source's, which takes them integral; `V ∩ W` is the fibre product `V ×_X W` and `ξ` is the image in `X` of a point `ζ` of it. That the closure `Z` of `ξ` is an irreducible component of `V ∩ W` is `dim 𝒪_{V ∩ W, ξ} = 0`, and that `V` and `W` intersect properly along `Z` is `dim 𝒪_{X, ξ} ≤ dim 𝒪_{V, v} + dim 𝒪_{W, w}`, the criterion of Tag 0B1I — by Tag 0A21 it is `dim Z ≤ dim V + dim W - dim X`, so it is implied by, and weaker than, the source's global proper intersection. `e(X, V · W, Z)` is `Stacks.Intersection.intersectionMultiplicity` (Tag 0AZR). Everything the proof uses is proved in this development: the reduction to the diagonal of Tag 0B0U, the regular sequence cutting out the diagonal of Tag 0B0Q, and the Hilbert-polynomial formula of Tag 0B04.”.

> **Stacks Project, Tag 0B0V.** One of the main results of Serre's *Algèbre locale*. Let `X`
> be a nonsingular variety over an algebraically closed field `k` — the chapter's convention — let
> `V`, `W ⊆ X` be closed subvarieties which intersect properly and let `Z` be an irreducible
> component of `V ∩ W`, with generic point `ξ`. Then `e(X, V · W, Z) > 0`.
>
> Here `V` and `W` are presented by closed immersions `ι_V : V ⟶ X`, `ι_W : W ⟶ X`, the
> scheme-theoretic intersection `V ∩ W` is the fibre product `V ×_X W`, and `ξ` is the image in
> `X` of a point `ζ` of it. The two numerical hypotheses are the source's own, read at `ξ`:
> `dim 𝒪_{V ∩ W, ξ} = 0` says that the closure of `ξ` is an irreducible component `Z` of `V ∩ W`,
> and `dim 𝒪_{X, ξ} ≤ dim 𝒪_{V, v} + dim 𝒪_{W, w}` says that `V` and `W` intersect properly along
> `Z`, which is Tag 0B1I's criterion: by Tag 0A21 the three local dimensions are
> `dim X - dim Z`, `dim V - dim Z` and `dim W - dim Z`, so the inequality is exactly
> `dim Z ≤ dim V + dim W - dim X`. The multiplicity `e(X, V · W, Z)` is
> `Stacks.Intersection.intersectionMultiplicity` (Tag 0AZR), the alternating sum
> `∑ᵢ (-1)ⁱ length 𝒪_{X,ξ} Torᵢ^{𝒪_{X,ξ}}(𝒪_{V,ξ}, 𝒪_{W,ξ})`.
>
> The proof is the source's. The reduction to the diagonal (Tag 0B0U) identifies `e(X, V · W, Z)`
> with `e(X ×ₖ X, Δ · V ×ₖ W, Δ(Z))`, by
> `Stacks.Intersection.Diagonal.localIntersectionMultiplicity_stalk_comap_diagonal_eq`; the
> diagonal of a nonsingular variety is a regular immersion (Tag 0B0Q), so the local ideal of `Δ`
> at `Δ(ξ)` is generated by a regular sequence of `dim X` elements
> (`Stacks.Intersection.Diagonal.exists_isRegular_fin_generating_ker_stalkMap_diagonal`); and for
> such a pair the multiplicity is `dim X !` times the positive leading coefficient of a Hilbert
> polynomial (Tag 0B04,
> `Stacks.Intersection.localIntersectionMultiplicity_pos_of_isRegularSequence`). The two
> numerical hypotheses of that last step are supplied for the diagonal pair by clauses 3 and 4
> above, and `X ×ₖ X` is regular because `X` is and `k` is perfect.

```lean
theorem intersectionMultiplicity_pos_of_isRegular {k : Type u} [Field k] [IsAlgClosed k]
    {X V W : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsVariety k f] (hX : IsRegular X)
    (iV : V ⟶ X) (iW : W ⟶ X) [IsClosedImmersion iV] [IsClosedImmersion iW]
    (ζ : ↑(pullback iV iW))
    (hcomponent : ringKrullDim (X.presheaf.stalk (iV (pullback.fst iV iW ζ)) ⧸
      AlgebraicGeometry.IdealSheafData.stalk (iV.ker ⊔ iW.ker)
        (iV (pullback.fst iV iW ζ))) = 0)
    (hproper : ringKrullDim (X.presheaf.stalk (iV (pullback.fst iV iW ζ))) ≤
      ringKrullDim (V.presheaf.stalk (pullback.fst iV iW ζ)) +
        ringKrullDim (W.presheaf.stalk (pullback.snd iV iW ζ))) :
    0 < Stacks.Intersection.intersectionMultiplicity iV.ker iW.ker
      (iV (pullback.fst iV iW ζ))
```

## Tag 0B0W, a lemma

[Tag 0B0W](https://stacks.math.columbia.edu/tag/0B0W) in the Stacks Project.

**`Stacks.Intersection.ReductionToDiagonal.intersectProperly_coherentSheafCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/ProperIntersection.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/ProperIntersection.lean#L91). The attribute's comment: “the clause that `[ℱ]_r` and `[𝒢]_s` intersect properly, for any scheme locally of finite type over a field: no nonsingularity and no variety hypothesis is used. The Tor formula `[ℱ]_r · [𝒢]_s = ∑ (-1)^p [Tor_p(ℱ, 𝒢)]_{r+s-dim X}` is not stated, because the intersection product of two cycles on a nonsingular variety is not defined in this library; its proof also needs the higher `Tor_i` of Stacks 0B0T, which is `Stacks.Intersection.Diagonal.torDiagonalIso`”.

> Let `ℱ` and `𝒢` be coherent `𝒪_X`-modules whose supports have dimension at most `r` and `s`
> and meet in dimension at most `r + s - dim X`. Then the cycles `[ℱ]_r` and `[𝒢]_s` intersect
> properly.

```lean
theorem intersectProperly_coherentSheafCycle (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (F G : X.Modules)
    [F.IsCoherent] [G.IsCoherent] (r s : ℕ)
    (hF : schemeDeltaDimension (fieldChowSituation k)
      ((reducedSupport F).subschemeι ≫ f) ≤ ((r : ℤ) : EInt))
    (hG : schemeDeltaDimension (fieldChowSituation k)
      ((reducedSupport G).subschemeι ≫ f) ≤ ((s : ℤ) : EInt))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set X) +
      topologicalKrullDim X ≤ (r : WithBot ℕ∞) + (s : WithBot ℕ∞)) :
    AlgebraicCycle.IntersectProperly
      (coherentSheafCycle (fieldChowSituation k) f F (r : ℤ) hF)
      (coherentSheafCycle (fieldChowSituation k) f G (s : ℤ) hG)
```

**`Stacks.Intersection.ReductionToDiagonal.torFormula_integerDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/TorFormulaIntegerDimension.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/TorFormulaIntegerDimension.lean#L180). The attribute's comment: “the whole lemma, in every case of the integer expected dimension `r + s - dim X`, the case `r + s < dim X` included: the properness of `[ℱ]_r` and `[𝒢]_s` and the Tor formula `[ℱ]_r · [𝒢]_s = ∑ₚ (-1)ᵖ [Torₚ^{𝒪_X}(ℱ, 𝒢)]_{r + s - dim X}`, for a nonsingular variety over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — under the source's own three dimension bounds, read as bounds on the topological dimension of the two supports and of their intersection. `WithBot ℕ∞` has no subtraction, so `dim (Supp ℱ ∩ Supp 𝒢) ≤ r + s - dim X` is spelled `dim (Supp ℱ ∩ Supp 𝒢) + dim X ≤ r + s`, as proper intersection is in Tag 0AZQ; both products are taken in the integer dimension `(r : ℤ) + s - dim X`. The left-hand side is the intersection product of Tag 0B08 and the right-hand side the alternating sum of Tag 0AZR.”.

> **Stacks Project, Tag 0B0W**, with the expected dimension an integer. Let `X` be a
> nonsingular variety over an algebraically closed field — the chapter's convention, Tag 0AZ8 —
> of dimension `dX`, and let `ℱ`, `𝒢` be coherent `𝒪_X`-modules with `dim (Supp ℱ) ≤ r`,
> `dim (Supp 𝒢) ≤ s` and `dim (Supp ℱ ∩ Supp 𝒢) ≤ r + s - dX`. Then the cycles `[ℱ]_r` and
> `[𝒢]_s` intersect properly and
>
> `[ℱ]_r · [𝒢]_s = ∑ₚ (-1)ᵖ [Torₚ^{𝒪_X}(ℱ, 𝒢)]_{r + s - dX}`.
>
> Here `r + s - dX` is the integer `(r : ℤ) + s - dX`, and all of its values are covered, the
> negative ones included. `WithBot ℕ∞` has no subtraction, so the third bound is written
> `dim (Supp ℱ ∩ Supp 𝒢) + dX ≤ r + s`; when `r + s < dX` it says that the supports are
> disjoint, and then both sides are `0` (`torFormula_eq_zero_of_add_lt`). The intersection
> product of cycles is the one of Tag 0B08 and the right-hand side is the alternating sum of
> Tag 0AZR.

```lean
theorem torFormula_integerDimension (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] (hX : IsRegular X)
    (F G : X.Modules) (hFc : _root_.SheafOfModules.IsCoherent F)
    (hGc : _root_.SheafOfModules.IsCoherent G) (r s dX : ℕ)
    (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hFr : topologicalKrullDim (SheafOfModules.supp F : Set X) ≤ (r : WithBot ℕ∞))
    (hGs : topologicalKrullDim (SheafOfModules.supp G : Set X) ≤ (s : WithBot ℕ∞))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set X) +
      (dX : WithBot ℕ∞) ≤ (r : WithBot ℕ∞) + (s : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    letI := hFc
    letI := hGc
    letI := isFiniteType_of_isCoherent F
    letI := isFiniteType_of_isCoherent G
    have hFr' := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le k f F r hFr
    have hGs' := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le k f G s hGs
    have hn : ∀ w ∈ SheafOfModules.supp F ∩ SheafOfModules.supp G,
        relativeDimension (fieldChowSituation k).dimensionFunction f w ≤ (r : ℤ) + s - dX :=
      fun _ hw => relativeDimension_le_of_topologicalKrullDim_add_le k f
        ((SheafOfModules.isClosed_supp F).inter (SheafOfModules.isClosed_supp G)) hFG hw
    AlgebraicCycle.IntersectProperly
        (coherentSheafCycle (fieldChowSituation k) f F (r : ℤ) hFr')
        (coherentSheafCycle (fieldChowSituation k) f G (s : ℤ) hGs') ∧
      torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + s - dX)
          (coherentSheafCycle (fieldChowSituation k) f F (r : ℤ) hFr')
          (coherentSheafCycle (fieldChowSituation k) f G (s : ℤ) hGs')
        = intersectionProductCycle (fieldChowSituation k) f hX F G hFc hGc ((r : ℤ) + s - dX)
            (torSheafDeltaDimension_le_of_forall_mem_inter (fieldChowSituation k) f hX F G hFc
              hGc ((r : ℤ) + s - dX) hn)
```

**`Stacks.Intersection.ReductionToDiagonal.torFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/TorFormulaWhole.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/TorFormulaWhole.lean#L415). The attribute's comment: “the whole lemma in the case `r + s ≥ dim X`, the expected dimension being a natural number `n`; every case, `r + s < dim X` included, is `Stacks.Intersection.ReductionToDiagonal.torFormula_integerDimension`. Here: the properness of `[ℱ]_r` and `[𝒢]_s` and the Tor formula `[ℱ]_r · [𝒢]_s = ∑ₚ (-1)ᵖ [Torₚ^{𝒪_X}(ℱ, 𝒢)]_{r + s - dim X}`, for a nonsingular variety over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — under the source's own three dimension bounds, read as bounds on the topological dimension of the two supports and of their intersection. `WithBot ℕ∞` has no subtraction, so `n = r + s - dim X` is the relation `r + s = dim X + n`. The left-hand side is the intersection product of Tag 0B08 for the Section 43.14 product of two closed subvarieties, and the right-hand side the alternating sum of Tag 0AZR.”.

> **Stacks Project, Tag 0B0W.** Let `X` be a nonsingular variety over an algebraically closed
> field — the chapter's convention, Tag 0AZ8 — of dimension `dX`, and let `ℱ`, `𝒢` be coherent
> `𝒪_X`-modules with `dim (Supp ℱ) ≤ r`, `dim (Supp 𝒢) ≤ s` and
> `dim (Supp ℱ ∩ Supp 𝒢) ≤ r + s - dX`. Then the cycles `[ℱ]_r` and `[𝒢]_s` intersect properly and
>
> `[ℱ]_r · [𝒢]_s = ∑ₚ (-1)ᵖ [Torₚ^{𝒪_X}(ℱ, 𝒢)]_{r + s - dX}`.
>
> The intersection product of cycles is the one of Tag 0B08, the bilinear extension of the
> Section 43.14 product of two closed subvarieties, and the right-hand side is the alternating sum
> of Tag 0AZR.

```lean
theorem torFormula (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] (hX : IsRegular X)
    (F G : X.Modules) (hFc : _root_.SheafOfModules.IsCoherent F)
    (hGc : _root_.SheafOfModules.IsCoherent G) (r s n dX : ℕ)
    (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞)) (hrs : r + s = dX + n)
    (hFr : topologicalKrullDim (SheafOfModules.supp F : Set X) ≤ (r : WithBot ℕ∞))
    (hGs : topologicalKrullDim (SheafOfModules.supp G : Set X) ≤ (s : WithBot ℕ∞))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set X) ≤
      (n : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    letI := hFc
    letI := hGc
    letI := isFiniteType_of_isCoherent F
    letI := isFiniteType_of_isCoherent G
    have hFr' := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le k f F r hFr
    have hGs' := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le k f G s hGs
    have hn : ∀ w ∈ SheafOfModules.supp F ∩ SheafOfModules.supp G,
        relativeDimension (fieldChowSituation k).dimensionFunction f w ≤ (n : ℤ) := fun _w hw =>
      relativeDimension_le_of_topologicalKrullDim_le (fieldChowSituation k) (fun _ _ => rfl) f
        ((SheafOfModules.isClosed_supp F).inter (SheafOfModules.isClosed_supp G)) hFG hw
    AlgebraicCycle.IntersectProperly
        (coherentSheafCycle (fieldChowSituation k) f F (r : ℤ) hFr')
        (coherentSheafCycle (fieldChowSituation k) f G (s : ℤ) hGs') ∧
      torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX (n : ℤ)
          (coherentSheafCycle (fieldChowSituation k) f F (r : ℤ) hFr')
          (coherentSheafCycle (fieldChowSituation k) f G (s : ℤ) hGs')
        = intersectionProductCycle (fieldChowSituation k) f hX F G hFc hGc (n : ℤ)
            (torSheafDeltaDimension_le_of_forall_mem_inter (fieldChowSituation k) f hX F G hFc
              hGc (n : ℤ) hn)
```

## Tag 0B0X, a remark

[Tag 0B0X](https://stacks.math.columbia.edu/tag/0B0X) in the Stacks Project.

**`Stacks.Intersection.length_tor_ne_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/SerreMultiplicity.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/SerreMultiplicity.lean#L275). The attribute's comment: “finiteness of each term `length_A Tor_i^A(M, N)` of the sum `χ(M, N)`”.

> **Finiteness of the individual terms of `χ(M, N)`.** Let `A` be a regular local ring and let
> `M`, `N` be nonzero finite `A`-modules with `M ⊗_A N` supported in the maximal ideal. Then
> `length_A Torᵢ^A(M, N)` is finite for every `i`.

```lean
theorem length_tor_ne_top {A : Type u} [CommRing A] [IsRegularLocalRing A] (M N : Type u)
    [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] [Nontrivial N]
    (hMN : Module.support A (M ⊗[A] N) ⊆ {IsLocalRing.closedPoint A}) (i : ℕ) :
    Module.length A (((Tor (ModuleCat.{u} A) i).obj (ModuleCat.of A M)).obj
      (ModuleCat.of A N)) ≠ ⊤
```

**`Stacks.Intersection.torEulerCharacteristic_eq_sum_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/SerreMultiplicity.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToTheDiagonal/SerreMultiplicity.lean#L287). The attribute's comment: “the sum `χ(M, N)` has finitely many nonzero terms: `Tor_i = 0` for `i > dim A`”.

> **Finiteness of the number of nonzero terms of `χ(M, N)`.** Over a regular local ring of
> dimension at most `d`, the alternating sum defining `χ(M, N)` is the finite sum over `i = 0, …, d`.

```lean
theorem torEulerCharacteristic_eq_sum_range {A : Type u} [CommRing A] [IsRegularLocalRing A]
    (M N : Type u) [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N] (d : ℕ)
    (hd : ringKrullDim A ≤ (d : WithBot ℕ∞)) :
    torEulerCharacteristic A M N =
      ∑ i ∈ Finset.range (d + 1), (-1 : ℚ) ^ i *
        ((Module.length A (((Tor (ModuleCat.{u} A) i).obj (ModuleCat.of A M)).obj
          (ModuleCat.of A N))).toNat : ℚ)
```

**`Stacks.SerreIntersection.torEulerCharacteristic_eq_zero_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SerreIntersection/EqualCharacteristicTor.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SerreIntersection/EqualCharacteristicTor.lean#L116). The attribute's comment: “(1) when A contains a field: r + s < dim A gives χ(M, N) = 0”.

> **Serre's vanishing for a regular local ring containing a field.** Let `A` be a regular local
> ring containing a field and let `M`, `N` be nonzero finite `A`-modules with `M ⊗_A N` supported in
> the closed point. If `dim Supp M + dim Supp N < dim A`, then `χ(M, N) = 0`.

```lean
theorem torEulerCharacteristic_eq_zero_of_field (F : Type v) [Field F] [Algebra F A]
    (M N : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] [Nontrivial N]
    (hMN : Module.support A (M ⊗[A] N) ⊆ {closedPoint A})
    (hlt : Module.supportDim A M + Module.supportDim A N < ringKrullDim A) :
    Stacks.Intersection.torEulerCharacteristic A M N = 0
```

**`Stacks.SerreIntersection.torEulerCharacteristic_pos_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SerreIntersection/EqualCharacteristicTor.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SerreIntersection/EqualCharacteristicTor.lean#L128). The attribute's comment: “(2) when A contains a field: r + s = dim A gives χ(M, N) > 0”.

> **Serre's positivity for a regular local ring containing a field.** Let `A` be a regular
> local ring containing a field and let `M`, `N` be nonzero finite `A`-modules with `M ⊗_A N`
> supported in the closed point. If `dim Supp M + dim Supp N = dim A`, then `χ(M, N) > 0`.

```lean
theorem torEulerCharacteristic_pos_of_field (F : Type v) [Field F] [Algebra F A]
    (M N : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] [Nontrivial N]
    (hMN : Module.support A (M ⊗[A] N) ⊆ {closedPoint A})
    (heq : Module.supportDim A M + Module.supportDim A N = ringKrullDim A) :
    0 < Stacks.Intersection.torEulerCharacteristic A M N
```

**`Stacks.SerreIntersection.supportDim_add_supportDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SerreIntersection/MixedCharacteristic.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SerreIntersection/MixedCharacteristic.lean#L320). The attribute's comment: “Serre's inequality r + s ≤ dim A”.

> **Serre's dimension inequality** [Serre, *Algèbre locale*, V.B.6]. Let `A` be a regular local
> ring and let `M`, `N` be nonzero finite `A`-modules with `M ⊗_A N` supported in the closed point.
> Then `dim Supp M + dim Supp N ≤ dim A`.
>
> The statement passes to the completion; a complete regular local ring either contains a field
> (`supportDim_add_supportDim_le_of_field`) or has a Cohen coefficient ring
> (`supportDim_add_supportDim_le_of_isCohenRing`), by the Cohen structure theorem (Stacks 032A).

```lean
theorem supportDim_add_supportDim_le {A : Type u} [CommRing A] [IsRegularLocalRing A]
    (M N : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M] [Nontrivial M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] [Nontrivial N]
    (hMN : Module.support A (M ⊗[A] N) ⊆ {closedPoint A}) :
    Module.supportDim A M + Module.supportDim A N ≤ ringKrullDim A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.19, Tag 0B0A](https://stacks.math.columbia.edu/tag/0B0A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
