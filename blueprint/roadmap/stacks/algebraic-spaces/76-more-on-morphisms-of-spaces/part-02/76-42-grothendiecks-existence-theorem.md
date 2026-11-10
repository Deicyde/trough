---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.abelian_coherentAdicSystems, AlgebraicGeometry.Space.coherentAdicInverseImage_exact, AlgebraicGeometry.Space.exact_iff_forall_exact_coherentAdicChartRestriction, AlgebraicGeometry.Space.coherentAdicSystems_abelian_and_exact, AlgebraicGeometry.Space.epi_iff_epi_app_zero, AlgebraicGeometry.Space.completionFunctor, AlgebraicGeometry.Space.preservesFiniteColimits_completionFunctor, AlgebraicGeometry.Space.preservesMonomorphisms_completionFunctor
statement: formalized
proof: formalized
---

# 76.42 Grothendieck's existence theorem

Section 76.42 of the Stacks Project, [Tag 089N](https://stacks.math.columbia.edu/tag/089N). 14 tags here are carried by 36 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 089P, a lemma

[Tag 089P](https://stacks.math.columbia.edu/tag/089P) in the Stacks Project.

**`AlgebraicGeometry.Space.abelian_coherentAdicSystems`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicAbelian.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicAbelian.lean#L424). The attribute's comment: “the category is abelian”.

> **The category `Coh(F, 𝓘)` of coherent adic systems on a Noetherian algebraic space is
> abelian.**
>
> It is preadditive, has finite products, kernels and cokernels, and every monomorphism is a kernel
> and every epimorphism a cokernel.

```lean
def abelian_coherentAdicSystems : Abelian (CoherentAdicSystems B S hS F hF 𝓘)
```

**`AlgebraicGeometry.Space.coherentAdicInverseImage_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean#L110). The attribute's comment: “part (3): the inverse image along a flat morphism of Noetherian algebraic spaces is exact”.

> **Part (3) of Stacks 089P: the inverse image along a flat morphism of Noetherian algebraic
> spaces is exact.**  For a flat morphism `f : X' ⟶ X` of Noetherian algebraic spaces and a
> quasi-coherent sheaf of ideals `𝓘 ⊆ 𝒪_X`, the functor
> `f^* : Coh(X, 𝓘) ⥤ Coh(X', f⁻¹𝓘 · 𝒪_{X'})` preserves finite limits and finite colimits.

```lean
theorem coherentAdicInverseImage_exact (hf : IsFlat B S hS f.hom) :
    exactFunctor (CoherentAdicSystems B S hS X.1 X.2 𝓘)
      (CoherentAdicSystems B S hS X'.1 X'.2 (pullbackIdealImage B S hS f 𝓘))
      (coherentAdicInverseImage B S hS f 𝓘 hN'.2.2)
```

**`AlgebraicGeometry.Space.exact_iff_forall_exact_coherentAdicChartRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean#L149). The attribute's comment: “part (2): exactness can be checked on an étale covering by affine charts”.

> **Part (2) of Stacks 089P: exactness in `Coh(X, 𝓘)` can be checked étale locally.**  For a
> Noetherian algebraic space `X`, a quasi-coherent sheaf of ideals `𝓘 ⊆ 𝒪_X` and an étale covering
> of `X` by affine charts `U i`, a short complex `E ⟶ G ⟶ H` of `Coh(X, 𝓘)` is exact exactly when
> its restriction `E|_{U i} ⟶ G|_{U i} ⟶ H|_{U i}` to `Coh(U i, 𝓘 · 𝒪_{U i})` is exact for every
> `i`.

```lean
theorem exact_iff_forall_exact_coherentAdicChartRestriction {I : Type v}
    (U : I → SmallEtale B S hS X.1) (hU : ∀ i, IsAffine (chartScheme (U i)))
    (hcov : IsEtaleCovering B S hS (fun i => (chartSpace B S hS X (U i)).1)
      (fun i => (chartToSpace B S hS X (U i)).hom))
    (T : ShortComplex (CoherentAdicSystems B S hS X.1 X.2 𝓘)) :
    T.Exact ↔ ∀ i, (coherentAdicRestrictToChartShortComplex B S hS X 𝓘 hZ hN (U i)
      (pullbackIdealImage B S hS (chartToSpace B S hS X (U i)) 𝓘) (hU i)
      (idealPowerMultipleCompatible_pullbackIdealImage B S hS (chartToSpace B S hS X (U i)) 𝓘)
      T).Exact
```

**`AlgebraicGeometry.Space.coherentAdicSystems_abelian_and_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInverseImageIdeal.lean#L178).

> **Stacks 089P.**  Let `X` be a Noetherian algebraic space over a scheme `S` and `𝓘 ⊆ 𝒪_X` a
> quasi-coherent sheaf of ideals.
>
> 1. `Coh(X, 𝓘)` is abelian.
> 2. Exactness in `Coh(X, 𝓘)` can be checked étale locally: on every étale covering of `X` by
>    affine charts `U i`, a short complex is exact exactly when its restrictions to the categories
>    `Coh(U i, 𝓘 · 𝒪_{U i})` are.
> 3. For every flat morphism `f : X' ⟶ X` of Noetherian algebraic spaces the inverse image
>    `f^* : Coh(X, 𝓘) ⥤ Coh(X', f⁻¹𝓘 · 𝒪_{X'})` is exact.

```lean
theorem coherentAdicSystems_abelian_and_exact :
    Nonempty (Abelian (CoherentAdicSystems B S hS X.1 X.2 𝓘)) ∧
    (∀ {I : Type v} (U : I → SmallEtale B S hS X.1) (hU : ∀ i, IsAffine (chartScheme (U i))),
      IsEtaleCovering B S hS (fun i => (chartSpace B S hS X (U i)).1)
          (fun i => (chartToSpace B S hS X (U i)).hom) →
        ∀ T : ShortComplex (CoherentAdicSystems B S hS X.1 X.2 𝓘),
          T.Exact ↔ ∀ i, (coherentAdicRestrictToChartShortComplex B S hS X 𝓘 hZ hN (U i)
            (pullbackIdealImage B S hS (chartToSpace B S hS X (U i)) 𝓘) (hU i)
            (idealPowerMultipleCompatible_pullbackIdealImage B S hS
              (chartToSpace B S hS X (U i)) 𝓘) T).Exact) ∧
    (∀ {X' : AlgebraicSpaces B S hS} (f : X' ⟶ X) (hN' : IsNoetherian B S hS hZ X'.1),
      IsFlat B S hS f.hom →
        exactFunctor (CoherentAdicSystems B S hS X.1 X.2 𝓘)
          (CoherentAdicSystems B S hS X'.1 X'.2 (pullbackIdealImage B S hS f 𝓘))
          (coherentAdicInverseImage B S hS f 𝓘 hN'.2.2))
```

## Tag 08B3, a lemma

[Tag 08B3](https://stacks.math.columbia.edu/tag/08B3) in the Stacks Project.

**`AlgebraicGeometry.Space.epi_iff_epi_app_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystem.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystem.lean#L486).

> A map of coherent adic systems on an algebraic space is surjective in `Coh(F, 𝓘)` exactly when
> its component at the lowest level is surjective.

```lean
theorem epi_iff_epi_app_zero {E E' : CoherentAdicSystems B S hS F hF 𝓘} (f : E ⟶ E') :
    Epi f ↔ Epi (f.hom.app (op 0))
```

## Tag 08B4, an equation

[Tag 08B4](https://stacks.math.columbia.edu/tag/08B4) in the Stacks Project.

**`AlgebraicGeometry.Space.completionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionFunctor.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionFunctor.lean#L326).

> The completion functor `Coh(𝒪_F) ⟶ Coh(F, 𝓘)` on a locally Noetherian algebraic space, for a
> quasi-coherent sheaf of ideals `𝓘`, sending a coherent `𝒪_F`-module `𝓖` to the coherent `𝓘`-adic
> system `𝓖^∧ = (𝓖 / 𝓘 ^ (n + 1) 𝓖)_n`.

```lean
def completionFunctor
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (hI : 𝓘.toSheafOfModules.IsQuasicoherentOnSite) :
    CoherentModules.{u, u} B S hS F hF ⥤ CoherentAdicSystems B S hS F hF 𝓘
```

## Tag 08B5, a lemma

[Tag 08B5](https://stacks.math.columbia.edu/tag/08B5) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesFiniteColimits_completionFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean#L340). The attribute's comment: “right exactness: preservation of finite colimits”.

> **Stacks 08B5, right exactness.**  The completion functor `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` preserves
> finite colimits.
>
> No Noetherian hypothesis is needed: the term at `n` of a completion is the reflection of a
> coherent module onto the modules annihilated by `𝓘 ^ (n + 1)`, and every term of a coherent
> `𝓘`-adic system is so annihilated.

```lean
instance preservesFiniteColimits_completionFunctor :
    PreservesFiniteColimits (completionFunctor B S hS F hF 𝓘 hI)
```

**`AlgebraicGeometry.Space.preservesMonomorphisms_completionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean#L432). The attribute's comment: “preservation of monomorphisms”.

> **Stacks 08B5, preservation of monomorphisms.**  On a Noetherian algebraic space the
> completion functor `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` carries a monomorphism to a monomorphism.
>
> Let `f : M ⟶ N` be a monomorphism and let `c` be the Artin-Rees constant of
> `AlgebraicGeometry.Space.exists_comp_completionTermProjection_eq_zero_of_mono`.  A morphism into
> `M ^ ∧` killed by `f ^ ∧` is tested level by level; at level `n` the transition map down from
> level `n + c` is an epimorphism, so it suffices to kill the morphism at level `n + c` after that
> transition, and the quotient projection out of `M` is an epimorphism, so that in turn is the
> Artin-Rees step.

```lean
theorem preservesMonomorphisms_completionFunctor (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ F) :
    (completionFunctor B S hS F hF 𝓘 hI).PreservesMonomorphisms
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_completionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean#L531). The attribute's comment: “left exactness: the completion functor preserves finite limits”.

> **Stacks 08B5, left exactness.**  On a Noetherian algebraic space the completion functor
> `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` of Stacks 08B4 preserves finite limits.
>
> It preserves homology by `AlgebraicGeometry.Space.preservesHomology_completionFunctor`, given
> that every monomorphism of `Coh(F, 𝓘)` is a kernel; and that holds by
> `AlgebraicGeometry.Space.isNormalMonoCategory_coherentAdicSystems`, from part (1) of Stacks 089P,
> since `𝓘` is cartesian on the affine charts by
> `AlgebraicGeometry.Space.isCartesianOnAffineCharts_of_isQuasicoherentOnSite`. The hypotheses are
> the source's own: `F` is Noetherian — which is where Artin–Rees, Stacks 07UL, enters through
> `AlgebraicGeometry.Space.preservesMonomorphisms_completionFunctor` — and `𝓘` is
> quasi-coherent.

```lean
theorem preservesFiniteLimits_completionFunctor (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ F) :
    PreservesFiniteLimits (completionFunctor B S hS F hF 𝓘 hI)
```

**`AlgebraicGeometry.Space.exactFunctor_completionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExact.lean#L547). The attribute's comment: “exactness: the completion functor is exact”.

> **Stacks 08B5.**  On a Noetherian algebraic space the completion functor
> `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` of Stacks 08B4 is exact.
>
> Right exactness is `AlgebraicGeometry.Space.preservesFiniteColimits_completionFunctor` and needs
> no Noetherian hypothesis; left exactness is
> `AlgebraicGeometry.Space.preservesFiniteLimits_completionFunctor`.

```lean
theorem exactFunctor_completionFunctor (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ F) :
    exactFunctor (CoherentModules.{u, u} B S hS F hF) (CoherentAdicSystems B S hS F hF 𝓘)
      (completionFunctor B S hS F hF 𝓘 hI)
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_completionFunctor_of_isNoetherian`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean#L103). The attribute's comment: “left exactness: the completion functor preserves finite limits, over the source's own hypotheses that the algebraic space is Noetherian and the sheaf of ideals quasi-coherent”.

> **Stacks 08B5, left exactness.**  On a Noetherian algebraic space the completion functor
> `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` of Stacks 08B4 preserves finite limits.
>
> This is `AlgebraicGeometry.Space.preservesFiniteLimits_completionFunctor`.

```lean
alias preservesFiniteLimits_completionFunctor_of_isNoetherian
```

**`AlgebraicGeometry.Space.exactFunctor_completionFunctor_of_isNoetherian`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean#L112). The attribute's comment: “exactness of the completion functor over the source's own hypotheses that the algebraic space is Noetherian and the sheaf of ideals quasi-coherent”.

> **Stacks 08B5.**  On a Noetherian algebraic space the completion functor
> `Coh(𝒪_F) ⥤ Coh(F, 𝓘)` of Stacks 08B4 is exact.
>
> This is `AlgebraicGeometry.Space.exactFunctor_completionFunctor`.

```lean
alias exactFunctor_completionFunctor_of_isNoetherian
```

## Tag 08B6, a lemma

[Tag 08B6](https://stacks.math.columbia.edu/tag/08B6) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleInternalHomAdicEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHom.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHom.lean#L607). The attribute's comment: “granted Stacks 0882, the case of schemes, on each étale chart as the hypothesis h0882; the étale-descent globalisation is proved”.

> **Stacks 08B6.**  Let `F` be an algebraic space over a scheme `S`, let `𝓘 ⊆ 𝒪_F` be a sheaf
> of ideals and let `M`, `N` be `𝒪_F`-modules.  Put `𝓗 = 𝓗om_{𝒪_F}(M, N)`.  Then
>
> `lim_n H⁰(F, 𝓗 / 𝓘 ^ n 𝓗) = Mor((M / 𝓘 ^ n M), (N / 𝓘 ^ n N))`,
>
> the inverse limit of the global sections of the ideal-power quotients of `𝓗` being the
> morphisms of inverse systems of `𝒪_F`-modules from the completion of `M` to the completion of
> `N`.  Since `Coh(F, 𝓘)` is a full subcategory of the inverse systems of `𝒪_F`-modules, the
> right-hand side is `Mor_{Coh(F, 𝓘)}(M^∧, N^∧)` whenever the two completions are objects of
> it.
>
> The source argues that both sides are sheaves on `F_étale` and so the identity may be checked
> étale locally, where it is the case of schemes.  That reduction is the hypothesis `h0882`: it
> asks, for every étale chart `U`, that the comparison be bijective on the inverse limits of the
> sections over `U`, which on a chart is Stacks 0882 for the scheme `U`.  What is proved here is
> the globalisation, in three steps: the comparison is a morphism of inverse systems of sheaves
> (`smallEtaleInternalHomAdicComparison_compat`), so a chartwise bijection is a bijection on
> global sections (`bijective_adicSectionsMap_of_bijective_adicSectionsMapAt`); the global
> sections of `𝓗om(M, N / 𝓘 ^ n N)` are the morphisms `M ⟶ N / 𝓘 ^ n N`
> (`smallEtaleInternalHomSectionsEquiv`); and such a morphism is the same as a morphism
> `M / 𝓘 ^ n M ⟶ N / 𝓘 ^ n N`, compatibly in `n`
> (`bijective_smallEtaleInternalHomAdicSection`).
>
> The Noetherian hypothesis on `F` and the coherence of `M` and `N` are not used: they enter only
> through `h0882`, whose chartwise content is the Noetherian scheme case.

```lean
def smallEtaleInternalHomAdicEquiv
    (h0882 : ∀ U, Function.Bijective (adicSectionsMapAt B S hS F hF
      (fun n => smallEtaleAdicQuotient B S hS F hF 𝓘 (n + 1)
        (smallEtaleInternalHom B S hS F hF M N))
      (fun n => smallEtaleInternalHom B S hS F hF M
        (smallEtaleAdicQuotient B S hS F hF 𝓘 (n + 1) N))
      (fun n => smallEtaleAdicQuotientTransition B S hS F hF 𝓘 (n + 1)
        (smallEtaleInternalHom B S hS F hF M N))
      (fun n => smallEtaleInternalHomMapRight B S hS F hF M
        (smallEtaleAdicQuotientTransition B S hS F hF 𝓘 (n + 1) N))
      (smallEtaleInternalHomAdicComparisonApp B S hS F hF 𝓘 M N)
      (smallEtaleInternalHomAdicComparison_compat B S hS F hF 𝓘 M N) U)) :
    adicSections B S hS F hF
        (fun n => smallEtaleAdicQuotient B S hS F hF 𝓘 (n + 1)
          (smallEtaleInternalHom B S hS F hF M N))
        (fun n => smallEtaleAdicQuotientTransition B S hS F hF 𝓘 (n + 1)
          (smallEtaleInternalHom B S hS F hF M N)) ≃
      (smallEtaleAdicQuotientSystem B S hS F hF 𝓘 M ⟶
        smallEtaleAdicQuotientSystem B S hS F hF 𝓘 N)
```

**`AlgebraicGeometry.Space.smallEtaleInternalHomSmallAdicEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomAffine.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomAffine.lean#L80).

> **Stacks 08B6.**  Let `F` be a locally Noetherian algebraic space over a scheme `S`, let
> `𝓘 ⊆ 𝒪_F` be a quasi-coherent sheaf of ideals and let `M`, `N` be coherent `𝒪_F`-modules.  Put
> `𝓗 = 𝓗om_{𝒪_F}(M, N)`.  Then
>
> `lim_n H⁰(F, 𝓗 / 𝓘 ^ n 𝓗) = Mor((M / 𝓘 ^ n M), (N / 𝓘 ^ n N))`,
>
> the inverse limit of the global sections of the ideal-power quotients of `𝓗` being the
> morphisms of inverse systems of `𝒪_F`-modules from the completion of `M` to the completion of
> `N`; since `Coh(F, 𝓘)` is a full subcategory of the inverse systems of `𝒪_F`-modules, this is
> `Mor_{Coh(F, 𝓘)}(M^∧, N^∧)`.  Here `𝓗` is the internal hom at the module universe of the
> schemes, `AlgebraicGeometry.Space.smallEtaleInternalHomSmall`, whose universe lift is
> `AlgebraicGeometry.Space.smallEtaleInternalHom`.  The source asks for `F` Noetherian; local
> Noetherianity is all that is used.

```lean
def smallEtaleInternalHomSmallAdicEquiv :
    adicSections B S hS F hF
        (fun n => smallEtaleAdicQuotient B S hS F hF 𝓘 (n + 1)
          (smallEtaleInternalHomSmall B S hS F hF M N))
        (fun n => smallEtaleAdicQuotientTransition B S hS F hF 𝓘 (n + 1)
          (smallEtaleInternalHomSmall B S hS F hF M N)) ≃
      (smallEtaleAdicQuotientSystem B S hS F hF 𝓘 M ⟶
        smallEtaleAdicQuotientSystem B S hS F hF 𝓘 N)
```

**`AlgebraicGeometry.Space.bijective_adicSectionsMap_of_isSeqProIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomProIso.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomProIso.lean#L391). The attribute's comment: “the pro-isomorphism step: pro-isomorphic inverse systems of `𝒪_F`-modules have the same inverse limit of global sections, which is what identifies the tag's two limits `lim H⁰(𝓗 / 𝓘 ^ n 𝓗)` and `lim H⁰(𝓗om(M, N / 𝓘 ^ n N))` from a pro-isomorphism of the comparison”.

> **A pro-isomorphism of inverse systems of `𝒪_F`-modules induces a bijection on the inverse
> limits of their global sections.**  Pro-isomorphic systems therefore have the same
> `lim_n H⁰(F, -)`, although they are nowhere isomorphic level by level.  The chartwise statement
> is `bijective_adicSectionsMapAt_of_isSeqProIso` and the passage to global sections is the étale
> descent of `bijective_adicSectionsMap_of_bijective_adicSectionsMapAt`.
>
> This is the step by which Stacks 08B6 identifies its left-hand side
> `lim_n H⁰(F, 𝓗 / 𝓘 ^ n 𝓗)` with `lim_n H⁰(F, 𝓗om(M, N / 𝓘 ^ n N))`: the comparison
> `AlgebraicGeometry.Space.smallEtaleInternalHomAdicComparisonApp` between those two systems is
> not an isomorphism at any single level, and the source's Noetherian and coherence hypotheses
> enter only to make it a pro-isomorphism.  Once that is known, this theorem turns it into the
> identity of inverse limits, with no hypothesis on the systems at all.

```lean
theorem bijective_adicSectionsMap_of_isSeqProIso
    (hβ : ∀ n : ℕ, trX n ≫ β n = β (n + 1) ≫ trY n)
    (hpro : IsSeqProIso B S hS F hF X Y trX trY β) :
    Function.Bijective (adicSectionsMap B S hS F hF X Y trX trY β hβ)
```

**`AlgebraicGeometry.Space.smallEtaleInternalHomAdicEquivOfNoetherian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInternalHomAdicNoetherian.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInternalHomAdicNoetherian.lean#L141).

> **Stacks 08B6.**  Let `X` be a Noetherian algebraic space over a scheme `S`, let `𝓘 ⊆ 𝒪_X` be
> a quasi-coherent sheaf of ideals and let `M`, `N` be coherent `𝒪_X`-modules.  Put
> `𝓗 = 𝓗om_{𝒪_X}(M, N)`.  Then
>
> `lim_n H⁰(X, 𝓗 / 𝓘 ^ n 𝓗) = Mor((M / 𝓘 ^ n M), (N / 𝓘 ^ n N))`,
>
> the inverse limit of the global sections of the ideal-power quotients of `𝓗` being the morphisms
> of inverse systems of `𝒪_X`-modules from the completion of `M` to the completion of `N`.
>
> This is `AlgebraicGeometry.Space.smallEtaleInternalHomAdicEquiv` with its assumed chartwise input
> `h0882` discharged, so the hypotheses are exactly the source's: Noetherianness of `X`,
> quasi-coherence of `𝓘`, coherence of `M` and of `N`.
>
> The tag is registered here, bare, because this is where the source's identity is proved outright
> under the source's own hypotheses and nothing else.  The two registrations on
> `StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHom.lean` carry clause strings naming
> the two steps proved there — the pro-isomorphism step and the morphism step — and stay as they
> are; by the covering-set rule they and this one together carry the tag.  No registration is
> placed on `AlgebraicGeometry.Space.smallEtaleInternalHomAdicEquiv` itself, which still takes
> `h0882` as an assumed input: a tag may not sit on a declaration that assumes the thing it
> asserts.

```lean
def smallEtaleInternalHomAdicEquivOfNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ X.1)
    (hI : 𝓘.toSheafOfModules.IsQuasicoherentOnSite)
    (hM : IsCoherent B S hS X.1 X.2 M) (hN : IsCoherent B S hS X.1 X.2 N) :
    adicSections B S hS X.1 X.2
        (fun n => smallEtaleAdicQuotient B S hS X.1 X.2 𝓘 (n + 1)
          (smallEtaleInternalHom B S hS X.1 X.2 M N))
        (fun n => smallEtaleAdicQuotientTransition B S hS X.1 X.2 𝓘 (n + 1)
          (smallEtaleInternalHom B S hS X.1 X.2 M N)) ≃
      (smallEtaleAdicQuotientSystem B S hS X.1 X.2 𝓘 M ⟶
        smallEtaleAdicQuotientSystem B S hS X.1 X.2 𝓘 N)
```

Declarations registered for the tag:

- [`bijective_smallEtaleInternalHomAdicSection`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=bijective_smallEtaleInternalHomAdicSection#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomProIso.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicInternalHomProIso.lean#L442) (StacksFrontier): “the morphism step of the identity: morphisms of the inverse systems of ideal-power quotients are exactly the compatible families of global sections of the internal homs into those quotients, so that `Mor((M / 𝓘 ^ n M), (N / 𝓘 ^ n N))` is `lim_n H⁰(F, 𝓗om(M, N / 𝓘 ^ n N))`”.

## Tag 08B7, a situation

[Tag 08B7](https://stacks.math.columbia.edu/tag/08B7) in the Stacks Project.

**`AlgebraicGeometry.Space.ExistenceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/GrothendieckExistence.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/GrothendieckExistence.lean#L63).

> **Stacks 08B7.** The standing data of Grothendieck's existence theorem: a Noetherian
> ring `A` complete with respect to an ideal `I`, together with a separated algebraic space
> `X` of finite type over `Spec A`.

```lean
structure ExistenceSituation
```

## Tag 08B8, an equation

[Tag 08B8](https://stacks.math.columbia.edu/tag/08B8) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperSupport_idealPowerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystemProperSupport.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystemProperSupport.lean#L132). The attribute's comment: “the support condition, by which equation 76.42.2.1 restricts to the two full subcategories constructed below: the completion M / 𝓘 ^ n M of a coherent module with support proper over the base again has support proper over the base. The arrow itself is the completion functor of Stacks 08B4, which is `AlgebraicGeometry.Space.completionFunctor`”.

> **Stacks 08B8, the support condition.** The terms `M / 𝓘 ^ n M` of the completion of a
> coherent `𝒪_X`-module `M` whose support is proper over `Y` again have support proper over `Y`.
>
> A coherent module is of finite type, and `M / 𝓘 ^ n M` is a quotient of `M`, so this is the
> quotient clause of Stacks 0CZK part (1).

```lean
theorem hasProperSupport_idealPowerQuotient (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (𝓘 : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X hX).O))).Submodule)
    (n : ℕ) (M : Modules.{u, u} B S hS X hX) (hMcoh : IsCoherent B S hS X hX M)
    (hM : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj M)) :
    HasProperSupport B S hS hX hY f hf
      ((SheafOfModules.toSheaf _).obj (idealPowerQuotient B S hS X hX 𝓘 n M))
```

**`AlgebraicGeometry.Space.completionFunctorProperOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionProperSupport.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionProperSupport.lean#L84). The attribute's comment: “the arrow, restricting the completion functor of Stacks 08B4 to the two full subcategories of objects with support proper over the base”.

> **Stacks 08B8, the arrow.**  The completion functor
> `Coh_{support proper over Y}(𝒪_X) ⟶ Coh_{support proper over Y}(X, 𝓘)` of
> equation 76.42.5.1, the restriction of the completion functor of Stacks 08B4 to the full
> subcategories of objects whose support is proper over `Y`.
>
> It is well defined because the completion of a coherent module with support proper over `Y`
> has all of its terms supported inside the support of the module, which is
> `AlgebraicGeometry.Space.hasProperSupport_idealPowerQuotient`.

```lean
def completionFunctorProperOver
    [Fact (HasEtaleLocalProperty B S hS X (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (hI : 𝓘.toSheafOfModules.IsQuasicoherentOnSite) :
    CoherentModulesProperOver B S hS hX hY g hg ⥤
      CoherentAdicSystemsProperOver B S hS hX hY g hg 𝓘
```

## Tag 08B9, a lemma

[Tag 08B9](https://stacks.math.columbia.edu/tag/08B9) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_completionFunctor_map_of_isProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupport.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupport.lean#L82). The attribute's comment: “the bijection on morphisms; the source's Situation 08B7 asks X separated of finite type over Spec A, of which only local finite type is used”.

> **Stacks 08B9, the bijection on morphisms.**  Let `A` be a Noetherian ring complete with
> respect to an ideal `I`, let `X` be an algebraic space with a morphism
> `f : X ⟶ Spec A` locally of finite type, and let `F`, `G` be coherent `𝒪_X`-modules such that the
> intersection of their supports is proper over `Spec A`.  Then completion along `I 𝒪_X`
> (Stacks 08B4) is a bijection
> `Mor_{Coh(𝒪_X)}(F, G) ⟶ Mor_{Coh(X, I 𝒪_X)}(F^∧, G^∧)`.
>
> The source's Situation 08B7 has `X` separated and of finite type over `Spec A`, so locally
> Noetherian (`AlgebraicGeometry.Space.isLocallyNoetherian_of_isLocallyOfFiniteType` with
> `AlgebraicGeometry.Space.hasEtaleLocalProperty_isLocallyNoetherian_baseObject` supply the `Fact`
> instance the completion functor of Stacks 08B4 is stated with); neither separatedness nor
> quasi-compactness is used.

```lean
theorem bijective_completionFunctor_map_of_isProperOver [IsNoetherianRing A] [IsAdicComplete I A]
    (f : X ⟶ schemeSpace (baseObject A B hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f.hom)
    (F G : CoherentModules.{u, u} B (Spec (.of A)) hA X.1 X.2)
    (hcl : IsClosed (supportOfSheaf B (Spec (.of A)) hA X.1 ((SheafOfModules.toSheaf _).obj F.obj) ∩
      supportOfSheaf B (Spec (.of A)) hA X.1 ((SheafOfModules.toSheaf _).obj G.obj)))
    (hp : IsProperOver B (Spec (.of A)) hA X.2 (schemeSpace (baseObject A B hA)).2 f.hom hf _ hcl) :
    letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf
    Function.Bijective ((completionFunctor B (Spec (.of A)) hA X.1 X.2
      (C1573.baseIdealSubmodule X.1 X.2 I)
      (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).map
        (X := F) (Y := G))
```

**`AlgebraicGeometry.Space.completionFunctorProperOverFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupport.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupport.lean#L101). The attribute's comment: “in particular, the completion functor of 08B8 is fully faithful”.

> **Stacks 08B9, full faithfulness.**  In the situation of
> `AlgebraicGeometry.Space.bijective_completionFunctor_map_of_isProperOver`, the completion functor
> `Coh_{support proper over A}(𝒪_X) ⟶ Coh_{support proper over A}(X, I 𝒪_X)` of Stacks 08B8 is
> fully faithful.

```lean
def completionFunctorProperOverFullyFaithful [IsNoetherianRing A] [IsAdicComplete I A]
    (f : X ⟶ schemeSpace (baseObject A B hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f.hom) :
    letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf
    (completionFunctorProperOver B (Spec (.of A)) hA X.1
      (schemeSpace (baseObject A B hA)).1 X.2 (schemeSpace (baseObject A B hA)).2 f.hom hf
      (C1573.baseIdealSubmodule X.1 X.2 I)
      (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).FullyFaithful
```

**`AlgebraicGeometry.Space.bijective_completionFunctor_map_and_fullyFaithful_of_isProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean#L72).

> **Stacks 08B9.**  Let `A` be a Noetherian ring complete with respect to an ideal `I` and let
> `X` be an algebraic space with a morphism `f : X ⟶ Spec A` locally of finite type.
>
> 1. For coherent `𝒪_X`-modules `F`, `G` such that the intersection of their supports is proper
>    over `Spec A`, completion along `I 𝒪_X` (Stacks 08B4) is a bijection
>    `Mor_{Coh(𝒪_X)}(F, G) ⟶ Mor_{Coh(X, I 𝒪_X)}(F^∧, G^∧)`.
> 2. In particular, the completion functor
>    `Coh_{support proper over A}(𝒪_X) ⟶ Coh_{support proper over A}(X, I 𝒪_X)` of Stacks 08B8 is
>    fully faithful.
>
> The source's Situation 08B7 has `X` separated and of finite type over `Spec A`, so locally
> Noetherian (`AlgebraicGeometry.Space.C1573.fact_isLocallyNoetherian_of_baseObject` supplies the
> `Fact` instance the completion functor of Stacks 08B4 is stated with); neither separatedness nor
> quasi-compactness is used.  The properness of `Supp F ∩ Supp G` is stated in the curried form
> `IsProperOver … hcl` of `AlgebraicGeometry.Space.IsProperOver`, which takes the closedness `hcl`
> of the subset as an argument.

```lean
theorem bijective_completionFunctor_map_and_fullyFaithful_of_isProperOver
    [IsNoetherianRing A] [IsAdicComplete I A]
    (f : X ⟶ schemeSpace (baseObject A B hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f.hom) :
    letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf
    (∀ (F G : CoherentModules.{u, u} B (Spec (.of A)) hA X.1 X.2)
      (hcl : IsClosed
        (supportOfSheaf B (Spec (.of A)) hA X.1 ((SheafOfModules.toSheaf _).obj F.obj) ∩
          supportOfSheaf B (Spec (.of A)) hA X.1 ((SheafOfModules.toSheaf _).obj G.obj))),
      IsProperOver B (Spec (.of A)) hA X.2 (schemeSpace (baseObject A B hA)).2 f.hom hf _ hcl →
      Function.Bijective ((completionFunctor B (Spec (.of A)) hA X.1 X.2
        (C1573.baseIdealSubmodule X.1 X.2 I)
        (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).map
          (X := F) (Y := G))) ∧
    Nonempty (completionFunctorProperOver B (Spec (.of A)) hA X.1
      (schemeSpace (baseObject A B hA)).1 X.2 (schemeSpace (baseObject A B hA)).2 f.hom hf
      (C1573.baseIdealSubmodule X.1 X.2 I)
      (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).FullyFaithful
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.bijective_completionFunctor_map_of_isProperOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/HomBijection/CompletionFullyFaithfulProperSupport.lean#L262), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean#L93) (StacksFrontier): “the bijection on morphisms; the source's Situation 08B7 asks X separated of finite type over Spec A, of which only local finite type is used”.
- [`AlgebraicGeometry.Space.C1573.completionFunctorProperOverFullyFaithful`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/HomBijection/CompletionFullyFaithfulProperSupport.lean#L338), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CompletionFullyFaithfulProperSupportTag.lean#L97) (StacksFrontier): “in particular, the completion functor of 08B8 is fully faithful”.

## Tag 08BA, a remark

[Tag 08BA](https://stacks.math.columbia.edu/tag/08BA) in the Stacks Project.

**`Ideal.exists_pow_le_annihilator_ker_and_coker_mapQ_pow_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean#L341). The attribute's comment: “equivalence of the annihilation conditions”.

> **Stacks Project, Tag 08BA.** For a linear map `φ : M → N` of `I`-adically complete
> modules, one positive power of `K` annihilates the kernels and the cokernels of all the
> reductions `M / Iⁿ⁺¹ M → N / Iⁿ⁺¹ N` if and only if one positive power of `K` annihilates
> `Ker(φ)` and `Coker(φ)`.

```lean
theorem exists_pow_le_annihilator_ker_and_coker_mapQ_pow_iff (I K : Ideal A)
    [IsAdicComplete I M] [IsHausdorff I N] (φ : M →ₗ[A] N) :
    (∃ t : ℕ, 0 < t ∧ ∀ n : ℕ,
        K ^ t ≤ Module.annihilator A
          ↑(LinearMap.ker (Submodule.mapQ (I ^ (n + 1) • (⊤ : Submodule A M))
            (I ^ (n + 1) • (⊤ : Submodule A N)) φ
            (Submodule.smul_top_le_comap_smul_top _ φ))) ∧
        K ^ t ≤ Module.annihilator A
          (_ ⧸ LinearMap.range (Submodule.mapQ (I ^ (n + 1) • (⊤ : Submodule A M))
            (I ^ (n + 1) • (⊤ : Submodule A N)) φ
            (Submodule.smul_top_le_comap_smul_top _ φ)))) ↔
      ∃ t : ℕ, 0 < t ∧ K ^ t ≤ Module.annihilator A ↑(LinearMap.ker φ) ∧
        K ^ t ≤ Module.annihilator A (N ⧸ LinearMap.range φ)
```

**`AlgebraicGeometry.Space.IsKernelCokernelAnnihilatedByPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicKernelCokernelAnnihilated.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicKernelCokernelAnnihilated.lean#L195). The attribute's comment: “the notion named by the remark: condition (1), one power of K annihilating every levelwise kernel and cokernel”.

> **Stacks 08BA, the notion.** A map `α : (F_n) ⟶ (G_n)` of inverse systems of `𝒪_X`-modules
> on an algebraic space is a *map whose kernel and cokernel are annihilated by a power of `𝓚`* if
> one integer `t ≥ 1` works for every level: `𝓚 ^ t` annihilates `Ker(α_n)` and `Coker(α_n)` for
> all `n`. This is condition (1) of the remark; its equivalence with condition (2), which is what
> makes the notion the one the remark names, is
> `AlgebraicGeometry.Space.isKernelCokernelAnnihilatedByPower_tfae`.
>
> The systems are indexed from `0`, the term at `n` being the source's term at `n + 1`; the
> condition quantifies over every level, so this is the source's condition for all `n ≥ 1`.

```lean
def IsKernelCokernelAnnihilatedByPower
    (𝓚 : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).Submodule)
    {E E' : ℕᵒᵖ ⥤ Modules.{u, u} B S hS F hF} (α : E ⟶ E') : Prop
```

**`AlgebraicGeometry.Space.isKernelCokernelAnnihilatedByPower_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicKernelCokernelAnnihilated.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicKernelCokernelAnnihilated.lean#L371). The attribute's comment: “the equivalence of (1) with (2) for any, and for some, surjective etale affine chart U = Spec(A), with alpha_U the map of 087W”.

> **Stacks Project, Tag 08BA.** Let `X` be a Noetherian algebraic space over a scheme `S`, let
> `𝓘, 𝓚 ⊆ 𝒪_X` be quasi-coherent sheaves of ideals and let `α : (F_n) ⟶ (G_n)` be a morphism of
> `Coh(X, 𝓘)`. For a surjective étale morphism `U = Spec(A) ⟶ X` write `I, K ⊆ A` for the ideals of
> `𝓘|_U, 𝓚|_U` and `α_U : M ⟶ N` for the map of finite `A^∧`-modules attached to `α|_U` by Stacks
> 087W. The following are equivalent:
>
> 1. there is an integer `t ≥ 1` such that `Ker(α_n)` and `Coker(α_n)` are annihilated by `𝓚 ^ t`
>    for all `n`;
> 2. for any such `U`, the modules `Ker(α_U)` and `Coker(α_U)` are annihilated by `K ^ t` for some
>    integer `t ≥ 1`;
> 3. for some such `U`, the modules `Ker(α_U)` and `Coker(α_U)` are annihilated by `K ^ t` for some
>    integer `t ≥ 1`.
>
> A chart `U ⟶ X` is an object of the small étale site of `X`, so étale; "`U = Spec(A)`" is
> affineness of its underlying scheme; surjectivity is surjectivity after every representable base
> change. Such a chart exists, by
> `AlgebraicGeometry.Space.exists_surjective_isNoetherianAffineChart`, which is what makes (3) follow
> from (2).

```lean
theorem isKernelCokernelAnnihilatedByPower_tfae
    (hZ : B.Contains (⊤_ Scheme.{u})) (hN : IsNoetherian B S hS hZ F)
    (h𝓘 : 𝓘.toSheafOfModules.IsQuasicoherentOnSite)
    (h𝓚 : 𝓚.toSheafOfModules.IsQuasicoherentOnSite)
    {E E' : CoherentAdicSystems B S hS F hF 𝓘} (α : E ⟶ E') :
    List.TFAE
      [IsKernelCokernelAnnihilatedByPower B S hS F hF 𝓚 α.hom,
        ∀ U : SmallEtale B S hS F, IsAffine (chartScheme U) →
          (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf U.1.hom →
          IsChartKernelCokernelAnnihilated B S hS F hF 𝓘 𝓚 α.hom U,
        ∃ U : SmallEtale B S hS F, IsAffine (chartScheme U) ∧
          (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf U.1.hom ∧
          IsChartKernelCokernelAnnihilated B S hS F hF 𝓘 𝓚 α.hom U]
```

## Tag 08BB, a lemma

[Tag 08BB](https://stacks.math.columbia.edu/tag/08BB) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_iso_of_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraization.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraization.lean#L482). The attribute's comment: “uniqueness, carrying left exactness of completion (08B5) as a hypothesis”.

> **Stacks 08BB, uniqueness of the algebraization.**
>
> Let `𝓘 ⊆ 𝒪_F` be a quasi-coherent sheaf of ideals on an algebraic space `F` with locally
> Noetherian étale charts, let `G` be a coherent `𝒪_F`-module and let `E` be a coherent `𝓘`-adic
> system with a map `α : E ⟶ G^∧`.  Given two algebraizations of `α` — coherent modules `M`, `N`
> with maps `a : M ⟶ G`, `a' : N ⟶ G` whose kernels and cokernels are annihilated by a power of
> `𝓘`, and isomorphisms `β : E ≅ M^∧`, `β' : E ≅ N^∧` with `α = β ≫ a^∧ = β' ≫ a'^∧` — there is a
> *unique* isomorphism `e : M ≅ N` compatible with the maps to `G` and with the comparison
> isomorphisms.
>
> **Left exactness of the completion functor is carried as a hypothesis**, in the form of
> the instance argument `PreservesFiniteLimits (completionFunctor B S hS F hF 𝓘 hI)`.  It is
> not a hypothesis of the source, which proves it beforehand as Stacks 08B5; it enters this proof
> only
> through the step that recognizes the completion of the pullback `M ×_G N` as the pullback of the
> completions.  Local Noetherianity replaces the source's Noetherian hypothesis, exactly as for
> the completion functor itself.
>
> The existence of an algebraization is *not* proved here: the source obtains it by étale descent
> from the case of a Noetherian scheme, and the restriction of coherent adic systems to an étale
> chart is not available in this tree.

```lean
theorem existsUnique_iso_of_algebraization {G M N : CoherentModules.{u, u} B S hS F hF}
    {E : CoherentAdicSystems B S hS F hF 𝓘}
    (α : E ⟶ (completionFunctor B S hS F hF 𝓘 hI).obj G) (a : M ⟶ G) (a' : N ⟶ G)
    (β : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj M)
    (β' : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj N)
    (ha : IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a)
    (ha' : IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a')
    (hα : α = β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a)
    (hα' : α = β'.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a') :
    ∃! e : M ≅ N, e.hom ≫ a' = a ∧
      β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map e.hom = β'.hom
```

**`AlgebraicGeometry.Space.exists_algebraization_and_existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraizationTag.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraizationTag.lean#L70).

> **Stacks 08BB.**  Let `F` be a Noetherian algebraic space over `S` and `𝓘 ⊆ 𝒪_F` a
> quasi-coherent sheaf of ideals.  Let `G` be a coherent `𝒪_F`-module, `E` an object of
> `Coh(F, 𝓘)` and `α : E ⟶ G^∧` a map whose kernel and cokernel are annihilated by a power of `𝓘`.
> Then there exists a triple `(M, a, β)` where
>
> 1. `M` is a coherent `𝒪_F`-module,
> 2. `a : M ⟶ G` is an `𝒪_F`-module map whose kernel and cokernel are annihilated by a power of
>    `𝓘`,
> 3. `β : E ≅ M^∧` is an isomorphism, and
> 4. `α = a^∧ ∘ β`,
>
> and it is unique up to unique isomorphism: for any two such triples `(M, a, β)` and
> `(N, a', β')` there is exactly one isomorphism `e : M ≅ N` with `a' ∘ e = a` and
> `e^∧ ∘ β = β'`.

```lean
theorem exists_algebraization_and_existsUnique_iso
    (hZ : B.Contains (⊤_ Scheme.{u})) (hN : IsNoetherian B S hS hZ F)
    {G : CoherentModules.{u, u} B S hS F hF} {E : CoherentAdicSystems B S hS F hF 𝓘}
    (α : E ⟶ (completionFunctor B S hS F hF 𝓘 hI).obj G)
    (hα : IsSystemKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 α.hom) :
    (∃ (M : CoherentModules.{u, u} B S hS F hF) (a : M ⟶ G)
      (β : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj M),
      IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a ∧
        α = β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a) ∧
    ∀ {M N : CoherentModules.{u, u} B S hS F hF} (a : M ⟶ G) (a' : N ⟶ G)
      (β : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj M)
      (β' : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj N),
      IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a →
      IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a' →
      α = β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a →
      α = β'.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a' →
      ∃! e : M ≅ N, e.hom ≫ a' = a ∧
        β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map e.hom = β'.hom
```

**`AlgebraicGeometry.Space.existsUnique_iso_of_algebraization_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionLeftExact.lean#L133). The attribute's comment: “uniqueness of the algebraization over the source's own hypotheses, with left exactness of completion (Stacks 08B5) supplied”.

> **Stacks 08BB, uniqueness of the algebraization**, over the source's own hypotheses.
>
> Let `𝓘 ⊆ 𝒪_F` be a quasi-coherent sheaf of ideals on a Noetherian algebraic space `F`, let `G`
> be a coherent `𝒪_F`-module and let `E` be a coherent `𝓘`-adic system with a map
> `α : E ⟶ G^∧`.  Two algebraizations of `α` — coherent modules `M`, `N` with maps `a : M ⟶ G`,
> `a' : N ⟶ G` whose kernels and cokernels are annihilated by a power of `𝓘`, and isomorphisms
> `β : E ≅ M^∧`, `β' : E ≅ N^∧` factoring `α` — differ by a unique isomorphism `M ≅ N` compatible
> with the maps to `G` and with the comparison isomorphisms.
>
> `AlgebraicGeometry.Space.existsUnique_iso_of_algebraization` states this with left exactness of
> the completion functor as an instance argument, because Stacks 08B5 was not available where it
> was proved; here that argument is supplied by
> `AlgebraicGeometry.Space.preservesFiniteLimits_completionFunctor_of_isNoetherian`, so the only
> hypotheses left are the source's.

```lean
theorem existsUnique_iso_of_algebraization_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hN : IsNoetherian B S hS hZ F)
    {G M N : CoherentModules.{u, u} B S hS F hF} {E : CoherentAdicSystems B S hS F hF 𝓘}
    (α : E ⟶ (completionFunctor B S hS F hF 𝓘 hI).obj G) (a : M ⟶ G) (a' : N ⟶ G)
    (β : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj M)
    (β' : E ≅ (completionFunctor B S hS F hF 𝓘 hI).obj N)
    (ha : IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a)
    (ha' : IsMapKernelCokernelAnnihilatedByPower B S hS F hF 𝓘 a')
    (hα : α = β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a)
    (hα' : α = β'.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map a') :
    ∃! e : M ≅ N, e.hom ≫ a' = a ∧
      β.hom ≫ (completionFunctor B S hS F hF 𝓘 hI).map e.hom = β'.hom
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.exists_algebraization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/CoherentCompletionExistence.lean#L319), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraizationTag.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionAlgebraizationTag.lean#L93) (StacksFrontier): “existence of the algebraization (F, a, β), over the source's hypotheses with Noetherianity of the algebraic space weakened to local Noetherianity of its étale charts”.
- [`AlgebraicGeometry.Space.C1573.exists_algebraization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/CoherentCompletionExistence.lean#L319), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExistence.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentCompletionExistence.lean#L76) (StacksFrontier): “existence of the algebraization (F, a, β), over the source's hypotheses with Noetherianity of the algebraic space weakened to local Noetherianity of its étale charts”.

## Tag 08BC, a lemma

[Tag 08BC](https://stacks.math.columbia.edu/tag/08BC) in the Stacks Project.

**`AlgebraicGeometry.Space.essImage_completionFunctorProperOver_of_auxiliaryIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AuxiliaryIdealClosedSubspace.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AuxiliaryIdealClosedSubspace.lean#L138).

> **Stacks 08BC.**  In Situation 08B7 — `A` Noetherian and `I`-adically complete,
> `f : X ⟶ Spec A` of finite type and separated, `𝓘 = I 𝒪_X` — let `𝓚 ⊆ 𝒪_X` be a
> quasi-coherent sheaf of ideals and `(F_n)` an object of
> `Coh_{support proper over A}(X, 𝓘)`.  Assume
>
> 1. for every `e ≥ 1`, the closed subspace `X_e` cut out by `𝓚^e` is such that completion along
>    `𝓘_e = I 𝒪_{X_e}` is an equivalence
>    `Coh_{support proper over A}(𝒪_{X_e}) ≌ Coh_{support proper over A}(X_e, 𝓘_e)`, and
> 2. there are an object `𝓗` of `Coh_{support proper over A}(𝒪_X)` and a map
>    `α : (F_n) ⟶ 𝓗^∧` whose kernel and cokernel are annihilated by a power of `𝓚`.
>
> Then `(F_n)` is in the essential image of the completion functor of Stacks 08B8.
>
> The closed subspace `X_e` of (1) is given as a closed immersion `i : Z ⟶ X` whose ideal sheaf
> `ker(𝒪_X ⟶ i_* 𝒪_Z)` is `𝓚^e`. The proof follows the source: the systems `(F_n / 𝓚^(e+1) F_n)_n`
> are algebraized on `X_(e+1)` and pushed to `X`
> (`AlgebraicGeometry.Space.C1573.kTorsionEssSurj_of_essSurj`); the algebraizations `G_e` form a
> coherent `𝓚`-adic system mapping to `𝓗^∧` with kernels and cokernels killed by `𝓚^(2t)` — the bound
> the source leaves as "details omitted"
> (`C1573.TorsionAlgebraization.isSystemKernelCokernelAnnihilatedByPower_γSystem`, a sharper exponent
> than the source's `𝓚^(4t)`); Stacks 08BB along `𝓚` algebraizes this map to `a : 𝓕 ⟶ 𝓗`; reducing
> modulo `𝓘^(n+1)` identifies `𝓕 / 𝓘^(n+1) 𝓕` with `F_n`; and the kernel of `a` embeds into some
> `G_e` by Artin–Rees, so `𝓕` has proper support by Stacks 0CZH
> (`AlgebraicGeometry.Space.C1573.essImage_completionFunctorProperOver_of_kTorsionEssSurj`).

```lean
theorem essImage_completionFunctorProperOver_of_auxiliaryIdeal [IsNoetherianRing A] (I : Ideal A)
    [IsAdicComplete I A] (X : AlgebraicSpaces B (Spec (.of A)) hA)
    (f : X ⟶ schemeSpace (baseObject A B hA)) (hf : IsFiniteType B (Spec (.of A)) hA f.hom)
    (hsep : IsSeparated B (Spec (.of A)) hA f.hom)
    (K : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of A)) hA X.1
        X.2).O))).Submodule) (hK : K.toSheafOfModules.IsQuasicoherentOnSite)
    (h1 : ∀ e : ℕ, 0 < e → ∃ (Z : AlgebraicSpaces B (Spec (.of A)) hA) (i : Z ⟶ X)
      (hi : IsClosedImmersion B (Spec (.of A)) hA i.hom),
      SheafOfModules.kerIdeal (structureSharp B (Spec (.of A)) hA i) =
        idealPowerMultiple B (Spec (.of A)) hA X.1 X.2 K e (SheafOfModules.unit _) ∧
      letI := C1573.fact_isLocallyNoetherian_of_baseObject Z (i ≫ f)
        (C1573.isLocallyOfFiniteType_closedImmersion_comp i hi f hf.1)
      (completionFunctorProperOver B (Spec (.of A)) hA Z.1 (schemeSpace (baseObject A B hA)).1
        Z.2 (schemeSpace (baseObject A B hA)).2 (i ≫ f).hom
        (C1573.isLocallyOfFiniteType_closedImmersion_comp i hi f hf.1)
        (C1573.baseIdealSubmodule Z.1 Z.2 I)
        (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := Z.1) (hX := Z.2) I)).IsEquivalence)
    (E : CoherentAdicSystemsProperOver B (Spec (.of A)) hA X.2 (schemeSpace (baseObject A B hA)).2
      f.hom hf.1 (C1573.baseIdealSubmodule X.1 X.2 I))
    (H : CoherentModulesProperOver B (Spec (.of A)) hA X.2 (schemeSpace (baseObject A B hA)).2
      f.hom hf.1)
    (α : E ⟶ letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf.1
      (completionFunctorProperOver B (Spec (.of A)) hA X.1 (schemeSpace (baseObject A B hA)).1 X.2
        (schemeSpace (baseObject A B hA)).2 f.hom hf.1 (C1573.baseIdealSubmodule X.1 X.2 I)
        (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).obj H)
    (hα : IsSystemKernelCokernelAnnihilatedByPower B (Spec (.of A)) hA X.1 X.2 K α.hom.hom) :
    letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf.1
    (completionFunctorProperOver B (Spec (.of A)) hA X.1 (schemeSpace (baseObject A B hA)).1 X.2
      (schemeSpace (baseObject A B hA)).2 f.hom hf.1 (C1573.baseIdealSubmodule X.1 X.2 I)
      (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).essImage E
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.essImage_completionFunctorProperOver_of_auxiliaryIdeal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/AuxiliaryIdealClosedSubspace.lean#L533), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceTags.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceTags.lean#L33) (StacksFrontier).

## Tag 08BD, a lemma

[Tag 08BD](https://stacks.math.columbia.edu/tag/08BD) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_completionMap_kernel_cokernel_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicCompletionMap.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicCompletionMap.lean#L221). The attribute's comment: “the full statement: for a representable proper morphism of Noetherian algebraic spaces which is an isomorphism over Y minus V(K), a map alpha from (G_n) to the completion of f_*F in Coh(Y, J) whose levelwise kernels and cokernels are all annihilated by one positive power of K”.

> **Stacks 08BD.** Let `f : X ⟶ Y` be a representable proper morphism of Noetherian algebraic
> spaces over `S`, let `𝓙, 𝓚 ⊆ 𝒪_Y` be quasi-coherent sheaves of ideals, and assume `f` is an
> isomorphism over `Y ∖ V(𝓚)`.  Set `𝓘 = f⁻¹𝓙 𝒪_X`.  Let `(𝓖_n)` be an object of `Coh(Y, 𝓙)`,
> `𝓕` a coherent `𝒪_X`-module and `β : (f^*𝓖_n) ≅ 𝓕^∧` an isomorphism in `Coh(X, 𝓘)`.  Then there
> is a map `α : (𝓖_n) ⟶ (f_*𝓕)^∧` in `Coh(Y, 𝓙)` whose kernel and cokernel are annihilated by a
> power of `𝓚` (`AlgebraicGeometry.Space.IsKernelCokernelAnnihilatedByPower`, the notion of
> Stacks 08BA: one exponent `t > 0` with `𝓚 ^ t` killing every levelwise kernel and cokernel).
>
> `α` is the map whose composite with the comparison `(f_*𝓕)^∧ ⟶ f_*(𝓕^∧)` is the system of
> adjunction maps followed by `f_*β`; it exists because that comparison is an isomorphism on limits
> (the theorem on formal functions, checked on affine charts), and the annihilation is the scheme
> case Stacks 088B on one surjective affine chart of `Y`, spread over `Y` by quasi-coherence.

```lean
theorem exists_completionMap_kernel_cokernel_annihilated (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f.hom)
    (hfp : IsProper B S hS f.hom) (hX : IsNoetherian B S hS hZ X.1)
    (hY : IsNoetherian B S hS hZ Y.1)
    (J K : (SheafOfModules.unit.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).Submodule)
    (hJ : J.toSheafOfModules.IsQuasicoherentOnSite) (hK : K.toSheafOfModules.IsQuasicoherentOnSite)
    (hiso : IsIso ((idealComplementSubfunctor B S hS Y K).fromPreimage f.hom))
    (G : CoherentAdicSystems B S hS Y.1 Y.2 J) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : IsCoherent B S hS X.1 X.2 F) :
    letI : Fact (HasEtaleLocalProperty B S hS X.1 (fun V : Scheme.{u} => IsLocallyNoetherian V)) :=
      ⟨hX.2.2⟩
    letI : Fact (HasEtaleLocalProperty B S hS Y.1 (fun V : Scheme.{u} => IsLocallyNoetherian V)) :=
      ⟨hY.2.2⟩
    ∀ _β : G.obj ⋙ modulePullback B S hS f ≅
        ((completionFunctor B S hS X.1 X.2 (pullbackIdealSubsheaf B S hS f hf J)
          (isQuasicoherentOnSite_pullbackIdealSubsheaf B S hS f hf J hJ)).obj ⟨F, hF⟩).obj,
      ∃ α : G ⟶ (completionFunctor B S hS Y.1 Y.2 J hJ).obj
          ⟨(modulePushforward B S hS f).obj F,
            isCoherent_modulePushforward_of_isProper B S hS f hf hfp hY.2.2 F hF⟩,
        IsKernelCokernelAnnihilatedByPower B S hS Y.1 Y.2 K α.hom
```

**`AlgebraicGeometry.Space.directImageComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicDirectImageComparison.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicDirectImageComparison.lean#L163). The attribute's comment: “the maps gamma_n of the proof: the adjunction map followed by f_*beta_n. The map alpha into (f_*F)^ is a different declaration and is not constructed in this library”.

> **The maps `γ_n : 𝓖_n ⟶ f_*f^*𝓖_n ⟶ f_*(𝓕/𝓘 ⁿ⁺¹𝓕)` of the proof of Stacks 08BD**, as a
> morphism of inverse systems of `𝒪_Y`-modules on an algebraic space: the adjunction map followed
> by `f_*β_n`.

```lean
def directImageComparison :
    G.obj ⟶ ((completionFunctor B S hS X.1 X.2 𝓘 hI).obj F).obj ⋙ modulePushforward B S hS f
```

**`AlgebraicGeometry.Space.exists_pos_idealPowerMultiple_kernel_cokernel_directImageComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicDirectImageComparison.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicDirectImageComparison.lean#L210). The attribute's comment: “the reduction of the lemma's kernel-cokernel condition from gamma to the adjunction maps. The map alpha into (f_*F)^ is not constructed in this library, which proves neither 08AR for a representable proper morphism nor the uniform Artin-Rees bounds 02OB behind the scheme case 088B”.

> **The reduction of the kernel–cokernel condition of Stacks 08BD to the adjunction maps.**
> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, let `𝓙, 𝓚 ⊆ 𝒪_Y` and
> `𝓘 ⊆ 𝒪_X` be sheaves of ideals, let `(𝓖_n)` be an object of `Coh(Y, 𝓙)`, let `𝓕` be a coherent
> `𝒪_X`-module and let `β : (f^*𝓖_n) ⟶ 𝓕^∧` be an isomorphism in `Coh(X, 𝓘)`.  The maps
>
> `γ_n : 𝓖_n ⟶ f_*f^*𝓖_n ⟶ f_*(𝓕/𝓘 ⁿ⁺¹𝓕)`
>
> have their levelwise kernels and cokernels annihilated by one positive power of `𝓚` exactly when
> the adjunction maps `𝓖_n ⟶ f_*f^*𝓖_n` do, because `γ_n` differs from the adjunction map by the
> isomorphism `f_*β_n`.  This is the step of the source's proof which makes the isomorphism `β`
> disappear from the annihilation statement, leaving the adjunction map that the closing paragraph
> of the scheme case is about.
>
> The map `α : (𝓖_n) ⟶ (f_*𝓕)^∧` which the source produces out of `γ` is not constructed; see the
> implementation notes of this file.

```lean
theorem exists_pos_idealPowerMultiple_kernel_cokernel_directImageComparison_iff
    (𝓚 : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).Submodule) :
    (∃ t : ℕ, 0 < t ∧ ∀ k : ℕ,
        idealPowerMultiple B S hS Y.1 Y.2 𝓚 t
            (kernel ((directImageComparison B S hS f 𝓙 𝓘 hI G F β).app (op k))) = ⊥ ∧
          idealPowerMultiple B S hS Y.1 Y.2 𝓚 t
            (cokernel ((directImageComparison B S hS f 𝓙 𝓘 hI G F β).app (op k))) = ⊥) ↔
      ∃ t : ℕ, 0 < t ∧ ∀ k : ℕ,
        idealPowerMultiple B S hS Y.1 Y.2 𝓚 t
            (kernel ((pullbackPushforwardUnitSystem B S hS f G.obj).app (op k))) = ⊥ ∧
          idealPowerMultiple B S hS Y.1 Y.2 𝓚 t
            (cokernel ((pullbackPushforwardUnitSystem B S hS f G.obj).app (op k))) = ⊥
```

**`AlgebraicGeometry.Space.exists_hom_completion_modulePushforward_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperDirectImageCompletionMap.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperDirectImageCompletionMap.lean#L71).

> **Stacks 08BD.**  For a representable proper morphism `f : X ⟶ Y` of Noetherian algebraic
> spaces which is an isomorphism over the complement of the closed subspace `Z = V(𝒦)`, a coherent
> `𝒥`-adic system `(𝒢_n)` on `Y`, a coherent `𝒪_X`-module `𝓕` and an isomorphism
> `β : (f^*𝒢_n) ≅ 𝓕^∧` of inverse systems on `X` (for the ideal `𝓘 = f⁻¹𝒥 𝒪_X`), the direct image
> `f_*𝓕` is coherent and there is a map `α : (𝒢_n) ⟶ (f_*𝓕)^∧` of coherent `𝒥`-adic systems whose
> kernel and cokernel are annihilated by a power of `𝒦`.

```lean
theorem exists_hom_completion_modulePushforward_annihilated
    (hZ0 : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS}
    (hX : IsNoetherian B S hS hZ0 X.1) (hY : IsNoetherian B S hS hZ0 Y.1)
    (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f.hom) (hfp : IsProper B S hS f.hom)
    (J K : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).Submodule)
    (hJ : J.toSheafOfModules.IsQuasicoherentOnSite)
    (Z : ClosedSubspaces B S hS Y.1) (hZ : definingIdealSheaf B S hS Y Z = K)
    (hiso : IsIso ((openComplement B S hS Z.1).fromPreimage f.hom))
    (G : CoherentAdicSystems B S hS Y.1 Y.2 J)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (β : G.obj ⋙ modulePullback B S hS f ≅
      adicQuotientSystem B S hS X.1 X.2 (C1573.inverseImageIdeal B S hS f hf J) F) :
    haveI : Fact (HasEtaleLocalProperty B S hS Y.1
        (fun T : Scheme.{u} => IsLocallyNoetherian T)) := ⟨hY.2.2⟩
    ∃ hP : IsCoherent B S hS Y.1 Y.2 ((modulePushforward B S hS f).obj F),
      ∃ α : G ⟶ (completionFunctor B S hS Y.1 Y.2 J hJ).obj
          ⟨(modulePushforward B S hS f).obj F, hP⟩,
        IsSystemKernelCokernelAnnihilatedByPower B S hS Y.1 Y.2 K α.hom
```

## Tag 08BE, a theorem

[Tag 08BE](https://stacks.math.columbia.edu/tag/08BE) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_completionFunctorProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceSpaces.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceSpaces.lean#L53).

> **Stacks 08BE, Grothendieck's existence theorem for algebraic spaces.**  Let `A` be a
> Noetherian ring complete with respect to an ideal `I`, and let `f : X ⟶ Spec A` be a separated
> morphism of finite type of algebraic spaces (Situation 08B7, with `𝓘 = I 𝒪_X`).  Then the
> completion functor
>
> `Coh_{support proper over A}(𝒪_X) ⟶ Coh_{support proper over A}(X, 𝓘)`
>
> of Stacks 08B8 is an equivalence of categories.

```lean
theorem isEquivalence_completionFunctorProperOver [IsNoetherianRing A] (I : Ideal A)
    [IsAdicComplete I A] (X : AlgebraicSpaces B (Spec (.of A)) hA)
    (f : X ⟶ schemeSpace (baseObject A B hA)) (hf : IsFiniteType B (Spec (.of A)) hA f.hom)
    (hsep : IsSeparated B (Spec (.of A)) hA f.hom) :
    letI := C1573.fact_isLocallyNoetherian_of_baseObject X f hf.1
    (completionFunctorProperOver B (Spec (.of A)) hA X.1 (schemeSpace (baseObject A B hA)).1 X.2
      (schemeSpace (baseObject A B hA)).2 f.hom hf.1 (C1573.baseIdealSubmodule X.1 X.2 I)
      (C1573.isQuasicoherentOnSite_baseIdealSubmodule (X := X.1) (hX := X.2) I)).IsEquivalence
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.isEquivalence_completionFunctorProperOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/GrothendieckExistenceSpaces.lean#L153), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceTags.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistenceTags.lean#L36) (StacksFrontier).

## Tag 08BF, a remark

[Tag 08BF](https://stacks.math.columbia.edu/tag/08BF) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_adicFibreRestrictionProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdicFibreSystem.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdicFibreSystem.lean#L410).

> **Stacks 08BF.**  Let `A` be a Noetherian ring complete with respect to an ideal `I`, write
> `S = Spec A` and `Sₙ = Spec(A/Iⁿ)`, and let `X ⟶ S` be a separated morphism of algebraic spaces of
> finite type, with `Xₙ = X ×_S Sₙ`.  Then the completion functor `𝓕 ↦ (𝓕|_{Xₙ})ₙ`, from coherent
> `𝒪_X`-modules with support proper over `A` to systems `(𝓕ₙ, φₙ)` of coherent
> `𝒪_{Xₙ}`-modules `𝓕ₙ` with isomorphisms `φₙ : iₙ^* 𝓕ₙ₊₁ ≅ 𝓕ₙ` such that `Supp(𝓕₁)` is proper
> over `S₁`, is an equivalence of categories.
>
> The adic fibres are indexed from `0`: `adicFibreSpaceOf A I B hA X f n` is the source's `Xₙ₊₁`.

```lean
theorem isEquivalence_adicFibreRestrictionProperOver [IsNoetherianRing A] [IsAdicComplete I A]
    (hf : IsFiniteType B (Spec (.of A)) hA f.hom) (hsep : IsSeparated B (Spec (.of A)) hA f.hom) :
    (adicFibreRestrictionProperOver I X f hf.1).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_adicFibreRestriction_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdicFibreSystem.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdicFibreSystem.lean#L434). The attribute's comment: “the special case of X proper over A, where the conditions on the supports are omitted”.

> **Stacks 08BF, the case of `X` proper over `A`.**  If `X ⟶ S = Spec A` is proper, the
> completion functor `𝓕 ↦ (𝓕|_{Xₙ})ₙ` from all coherent `𝒪_X`-modules to all systems `(𝓕ₙ, φₙ)` of
> coherent `𝒪_{Xₙ}`-modules with isomorphisms `φₙ : iₙ^* 𝓕ₙ₊₁ ≅ 𝓕ₙ` is an equivalence of
> categories: the conditions on the supports can be omitted.

```lean
theorem isEquivalence_adicFibreRestriction_of_isProper [IsNoetherianRing A] [IsAdicComplete I A]
    (hf : IsProper B (Spec (.of A)) hA f.hom) :
    (adicFibreRestrictionOf I X f hf.2.1.1).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.42, Tag 089N](https://stacks.math.columbia.edu/tag/089N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
