---
declaration: section
origin: cited
lean: AlgebraicGeometry.compactSupportDualityEquiv, AlgebraicGeometry.compactSupportDualityEquiv_naturality, AlgebraicGeometry.compactSupportDualityEquiv_restrict, AlgebraicGeometry.degreeZeroCompactSupportMap_injective_and_range
statement: formalized
proof: formalized
---

# 48.33 Duality for compactly supported cohomology

Section 48.33 of the Stacks Project, [Tag 0G59](https://stacks.math.columbia.edu/tag/0G59). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G5A, a lemma

[Tag 0G5A](https://stacks.math.columbia.edu/tag/0G5A) in the Stacks Project.

**`AlgebraicGeometry.compactSupportDualityEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/Basic.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/Basic.lean#L106). The attribute's comment: “the isomorphism of topological k-vector spaces”.

> **Stacks Project, Tag 0G5A.** Let `p : U ⟶ Spec k` be separated of finite type over a field
> `k` and `ω_{U/k}^• = p^!𝒪_{Spec k}`. For `K ∈ D^b_{Coh}(𝒪_U)` and `i ∈ ℤ` there is a canonical
> isomorphism of topological `k`-vector spaces
>
> `Hom_k(H^i(U, K), k) ≃ H^{-i}_c(U, R𝓗om(K, ω_{U/k}^•))`,
>
> for the topology of pointwise convergence on the dual (the limit topology over the finite
> dimensional subspaces, `Module.Dual.limitTopology_eq_iInf_finiteDimensional`) and the limit
> topology of [Stacks, Section 0G59] on compactly supported cohomology. It is functorial in `K`
> (`AlgebraicGeometry.compactSupportDualityEquiv_naturality`). Here `p^!` and `H^*_c` are computed
> at an arbitrary compactification `c` of `U` (one exists by [Stacks, Tag 0F41]).

```lean
def compactSupportDualityEquiv (K : BoundedCoherentDerived U) (i : ℤ) :
    letI := HasDerivedCategory.standard U.Modules
    letI := HasDerivedCategory.standard (ModuleCat.{u} k)
    haveI := isNoetherian_of_locallyOfFiniteType p
    letI := Module.Dual.limitTopology k ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) i).obj
        ((derivedGlobalSectionsOver p).obj K.obj))
    Module.Dual k ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) i).obj
        ((derivedGlobalSectionsOver p).obj K.obj)) ≃L[k]
      compactSupportCohomology c
        (openDualObj (standardUpperShriekDualizingComplex p c)
          (isDualizingComplex_standardUpperShriekDualizingComplex p c) K) (-i)
```

**`AlgebraicGeometry.compactSupportDualityEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/Basic.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/Basic.lean#L130). The attribute's comment: “functoriality in K”.

> **Stacks Project, Tag 0G5A, functoriality.** The isomorphisms of
> `AlgebraicGeometry.compactSupportDualityEquiv` are functorial in `K`: for `α : K ⟶ K'` and a
> linear form `l` on `H^i(U, K')`, the image of `l ∘ H^i(α)` is the image of `l` under the map
> `H^{-i}_c(U, D_U K') ⟶ H^{-i}_c(U, D_U K)` induced by `D_U α`.

```lean
theorem compactSupportDualityEquiv_naturality {K K' : BoundedCoherentDerived U} (α : K ⟶ K')
    (i : ℤ) (l :
      letI := HasDerivedCategory.standard U.Modules
      letI := HasDerivedCategory.standard (ModuleCat.{u} k)
      Module.Dual k ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) i).obj
        ((derivedGlobalSectionsOver p).obj K'.obj))) :
    letI := HasDerivedCategory.standard U.Modules
    letI := HasDerivedCategory.standard (ModuleCat.{u} k)
    haveI := isNoetherian_of_locallyOfFiniteType p
    compactSupportDualityEquiv p c K i
        (l ∘ₗ ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) i).map
          ((derivedGlobalSectionsOver p).map α.hom)).hom) =
      compactSupportCohomologyMap c
        (openDualMap (standardUpperShriekDualizingComplex p c)
          (isDualizingComplex_standardUpperShriekDualizingComplex p c) α) (-i)
        (compactSupportDualityEquiv p c K' i l)
```

## Tag 0G5B, a lemma

[Tag 0G5B](https://stacks.math.columbia.edu/tag/0G5B) in the Stacks Project.

**`AlgebraicGeometry.compactSupportDualityEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/OpenRestriction.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactSupportDuality/OpenRestriction.lean#L593).

> Let `p : U ⟶ Spec k` be separated of finite type over a field `k`, with a compactification
> `c : U ⊆ X` at which `p^!` and `H^*_c` are computed, as in [Stacks, Tag 0G5A]
> (`AlgebraicGeometry.compactSupportDualityEquiv`), and let `V ⊆ U` be an open, with the induced
> compactification `V ⊆ U ⊆ X` (`AlgebraicGeometry.compactificationOpen`). Then the square
>
> `Hom_k(H^i(U, K), k)       ⟶  H^{-i}_c(U, R𝓗om(K, ω_{U/k}^•))`
> `        ↑                                  ↑`
> `Hom_k(H^i(V, K|_V), k)    ⟶  H^{-i}_c(V, R𝓗om(K|_V, ω_{V/k}^•))`
>
> commutes, for every `K ∈ D^b_{Coh}(𝒪_U)` and `i ∈ ℤ`: for every linear form `l` on
> `H^i(V, K|_V)`, the image of `l ∘ res` under the duality isomorphism of `U` is the image under the
> right vertical arrow of the image of `l` under the duality isomorphism of `V`. Here the horizontal
> arrows are the isomorphisms of [Stacks, Tag 0G5A], the left vertical arrow is the contragredient
> of the restriction map `res : H^i(U, K) ⟶ H^i(V, K|_V)` (`AlgebraicGeometry.cohomologyRestrict`),
> and the right vertical arrow is the map of [Stacks, Remark 0G56]
> (`AlgebraicGeometry.compactSupportOpenDualMap`): `Rq_*` of the canonical map
> `Rj'_!(L|_V) ⟶ Rj_! L` of [Stacks, Tag 0G4Y], read through the canonical identification of
> `R𝓗om(K|_V, ω_{V/k}^•)` with `R𝓗om(K, ω_{U/k}^•)|_V`.

```lean
theorem compactSupportDualityEquiv_restrict (K : BoundedCoherentDerived U) (i : ℤ) :
    haveI := isNoetherian_of_locallyOfFiniteType p
    haveI := isNoetherian_of_locallyOfFiniteType (V.ι ≫ p)
    ∀ l : Module.Dual k ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) i).obj
      ((derivedGlobalSectionsOver (V.ι ≫ p)).obj ((restrictBoundedCoherentLift V.ι).obj K).obj)),
    compactSupportDualityEquiv p c K i (l ∘ₗ cohomologyRestrict p V K i) =
      compactSupportOpenDualMap p c V K i
        (compactSupportDualityEquiv (V.ι ≫ p) (compactificationOpen p c V)
          ((restrictBoundedCoherentLift V.ι).obj K) i l)
```

## Tag 0G5C, a lemma

[Tag 0G5C](https://stacks.math.columbia.edu/tag/0G5C) in the Stacks Project.

**`AlgebraicGeometry.degreeZeroCompactSupportMap_injective_and_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DegreeZeroCompactSupport.lean, line 604](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DegreeZeroCompactSupport.lean#L604).

> Let `X` be a proper scheme over a field `k`. Let
> `K ∈ D^b_{Coh}(𝒪_X)` with `H^i(K) = 0` for `i < 0`, and set `𝓕 = H^0(K)`. Let `Z ⊆ X` be closed
> with complement `U = X ∖ Z`. Then
>
> `H^0_c(U, K|_U) ⊂ H^0(X, 𝓕)`
>
> is given by those global sections of `𝓕` which vanish in an open neighbourhood of `Z`.
>
> Here `H^0_c(U, K|_U)` is `AlgebraicGeometry.degreeZeroCompactSupport`: the morphisms
> `𝒪_{Spec k} ⟶ Rg_!(K|_U)` in `Pro-D^b_{Coh}(𝒪_{Spec k})`, for `g : U ⟶ Spec k` and the functor
> `Rg_! = Rp_* ∘ Rj_!` of [Stacks, Section 0G4Z] attached to the compactification `j : U ⟶ X`
> (which is `lim_n H^0(X, K_n)` for a Deligne system `(K_n)` with value `K|_U`,
> [Stacks, Section 0G59]); the map `H^0_c(U, K|_U) ⟶ H^0(X, 𝓕)` is
> `AlgebraicGeometry.degreeZeroCompactSupportMap`, induced by the map `Rg_!(K|_U) ⟶ Rp_* K` of
> [Stacks, Tag 0G56] for `X` its own compactification and `H^0(X, K) = Γ(X, H^0(K))`. The statement
> is that this map is injective with exactly that image.

```lean
public theorem degreeZeroCompactSupportMap_injective_and_range {k : Type u} [Field k]
    {X : Scheme.{u}}
    (p : X ⟶ Spec (.of k)) [IsProper p] (K : BoundedCoherentDerived X)
    (hK : ∀ i < 0, IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K.obj))
    (Z : TopologicalSpace.Closeds X) :
    letI : IsNoetherian X := @IsNoetherian.mk X (LocallyOfFiniteType.isLocallyNoetherian p)
      (QuasiCompact.compactSpace_of_compactSpace p)
    Function.Injective (degreeZeroCompactSupportMap p Z.compl K
        ((DerivedCategory.isGE_iff K.obj 0).2 hK)) ∧
      Set.range (degreeZeroCompactSupportMap p Z.compl K
        ((DerivedCategory.isGE_iff K.obj 0).2 hK)) =
        {σ | ∃ V : X.Opens, (Z : Set X) ⊆ V ∧
          ((DerivedCategory.homologyFunctor X.Modules 0).obj K.obj).presheaf.map
            (homOfLE (le_top : V ≤ ⊤)).op σ = 0}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.33, Tag 0G59](https://stacks.math.columbia.edu/tag/0G59)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
