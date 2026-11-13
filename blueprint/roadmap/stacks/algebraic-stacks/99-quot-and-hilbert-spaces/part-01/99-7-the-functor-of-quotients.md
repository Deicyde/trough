---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuotientSituation, AlgebraicGeometry.Space.QuotientSituation.mk_kernel_quotientProjection, AlgebraicGeometry.Space.QuotientSituation.quotients, AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotients, AlgebraicGeometry.Space.QuotientSituation.quotientPullback, AlgebraicGeometry.Space.QuotientSituation.quotientPullback_mem_quotients', AlgebraicGeometry.Space.QuotientSituation.quotientPullback_mem_finitePresentationQuotients, AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor_obj
statement: formalized
proof: formalized
---

# 99.7 The functor of quotients

Section 99.7 of the Stacks Project, [Tag 082L](https://stacks.math.columbia.edu/tag/082L). 12 tags here are carried by 44 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 082M, a situation

[Tag 082M](https://stacks.math.columbia.edu/tag/082M) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean#L96). The attribute's comment: “the standing data”.

> **Stacks 082M, the standing data.**  A morphism `f : X ⟶ Y` of algebraic spaces over `S`
> together with a quasi-coherent `𝒪_X`-module `F`: the data whose quotients, flat over the test
> scheme, the functor of quotients of `F/X/Y` classifies.

```lean
structure QuotientSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.QuotientSituation.mk_kernel_quotientProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean#L158). The attribute's comment: “the identification of two quotients of F\_T that have the same kernel: the submodules of F\_T list the quotients of F\_T once each”.

> The kernel of the projection `F_T ⟶ F_T / K` is `K` again.  Together with surjectivity of
> the projection this says that the submodules of `F_T` list the quotients of `F_T` once each,
> which is the source's identification of two quotients with the same kernel.

```lean
theorem mk_kernel_quotientProjection (T : SchemesOver D.Y)
    (K : Subobject (D.baseChangeModule T)) :
    Subobject.mk (kernel.ι (D.quotientProjection T K)) = K
```

**`AlgebraicGeometry.Space.QuotientSituation.quotients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean#L178). The attribute's comment: “the set of quotients”.

> **Stacks 082M.**  The set `Q_{F/X/Y}(T)` of quotients of `F_T` which are quasi-coherent and
> flat over the test scheme `T`, the two conditions of the source.
>
> A quotient of `F_T` is recorded by its kernel, a submodule `K` of `F_T`, the quotient itself
> being `F_T / K`; this is exactly the source's identification of two quotients of `F_T` that
> have the same kernel.

```lean
def quotients (T : SchemesOver D.Y) : Set (Subobject (D.baseChangeModule T))
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctor.lean#L185). The attribute's comment: “the finite-presentation subfunctor”.

> **Stacks 082M.**  The subset `Q^{fp}_{F/X/Y}(T)` of `Q_{F/X/Y}(T)` consisting of those
> quotients `F_T ⟶ Q` for which `Q` is of finite presentation as an `𝒪_{X_T}`-module.

```lean
def finitePresentationQuotients (T : SchemesOver D.Y) :
    Set (Subobject (D.baseChangeModule T))
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L171). The attribute's comment: “the pullback Q' = (X\_\{T'} ⟶ X\_T)^*Q of a quotient of F\_T along a morphism T' ⟶ T of test schemes over Y”.

> The pullback of a quotient of `F_T` along a morphism `h : T' ⟶ T` of test schemes,
> `Q ↦ (X_{T'} ⟶ X_T)^*Q`, recorded by its kernel.

```lean
def quotientPullback {T' T : SchemesOver D.Y} (h : T' ⟶ T)
    (K : Subobject (D.baseChangeModule T)) : Subobject (D.baseChangeModule T')
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientPullback_mem_quotients'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L247). The attribute's comment: “the pullback clause: if F\_T ⟶ Q is an element of Q\_\{F/X/Y}(T) and T' ⟶ T is a morphism of schemes over Y, then Q' = (X\_\{T'} ⟶ X\_T)^*Q is a quasi-coherent 𝒪\_\{X\_\{T'}}-module flat over T', so it is an element of Q\_\{F/X/Y}(T')”.

> The pullback of a quotient of `F_T` which is quasi-coherent and flat over `T` is
> quasi-coherent and flat over `T'`.

```lean
theorem quotientPullback_mem_quotients' {T' T : SchemesOver D.Y} (h : T' ⟶ T)
    (K : Subobject (D.baseChangeModule T)) (hK : K ∈ D.quotients T) :
    D.quotientPullback h K ∈ D.quotients T'
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientPullback_mem_finitePresentationQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L259). The attribute's comment: “Q^\{fp}\_\{F/X/Y} is a subfunctor of Q\_\{F/X/Y}: finite presentation of a quotient is preserved by the pullback along a morphism of test schemes, so the finitely presented quotients are stable under the transition maps”.

> The pullback of a finitely presented quotient is a finitely presented quotient.

```lean
theorem quotientPullback_mem_finitePresentationQuotients {T' T : SchemesOver D.Y} (h : T' ⟶ T)
    (K : Subobject (D.baseChangeModule T)) (hK : K ∈ D.finitePresentationQuotients T) :
    D.quotientPullback h K ∈ D.finitePresentationQuotients T'
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L319). The attribute's comment: “the functor Q\_\{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets obtained from the pullback clause, through its value at a test scheme T over Y, which is the set Q\_\{F/X/Y}(T)”.

> The value of the functor of quotients at a test scheme `T` over `Y` is the set
> `Q_{F/X/Y}(T)`.

```lean
theorem quotientsFunctor_obj (T : SchemesOver D.Y) :
    D.quotientsFunctor.obj (Opposite.op T) = D.quotients T
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L327). The attribute's comment: “the functor Q\_\{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets obtained from the pullback clause, through its transition maps, which are the pullback Q ↦ (X\_\{T'} ⟶ X\_T)^*Q of quotients”.

> The action of the functor of quotients on a morphism of test schemes is
> pullback of quotients.

```lean
theorem quotientsFunctor_map {T' T : SchemesOver D.Y} (h : T' ⟶ T)
    (K : Subobject (D.baseChangeModule T)) (hK : K ∈ D.quotients T) :
    (D.quotientsFunctor.map (Opposite.op h)
      ⟨K, hK⟩ : D.quotients T').1 = D.quotientPullback h K
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsFunctorToQuotientsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L356). The attribute's comment: “Q^\{fp}\_\{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets is a subfunctor of Q\_\{F/X/Y}: the inclusion of the finitely presented quotients into all of them is a morphism of functors”.

> The finite-presentation subfunctor is a subfunctor of the functor of
> quotients: at every test scheme its value is a subset of the value of
> `AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor`, and the two actions agree.

```lean
def finitePresentationQuotientsFunctorToQuotientsFunctor :
    D.finitePresentationQuotientsFunctor ⟶ D.quotientsFunctor
```

**`AlgebraicGeometry.Space.QuotientSituation.sourceRestricted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean#L210). The attribute's comment: “the standing data on a member of a covering of the source”.

> **Situation 082M on a member of a covering of the source.**  For a morphism
> `a : W ⟶ X` of algebraic spaces, the standing data consisting of `W`, the composite
> `a ≫ f : W ⟶ Y` and the pullback `a^*F` of the module.
>
> Its functor of quotients is the source's `Q_{F i/X i/Y}` when `a` is a member of a covering of
> `X`, and the source's `Q_{F ijk/X ijk/Y}` when `a` is the composite `X ijk ⟶ X i ×_X X j ⟶ X`:
> in both cases the module is *the* pullback of `F` to the member, which is what the source
> writes.
>
> Quasi-coherence of `a^*F` is Stacks 03GA, which holds along an arbitrary morphism of algebraic
> spaces by
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite` of
> `StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean`, so no
> local-presentation hypothesis on `a` is asked for.
>
> It is made reducible below so that the identifications `(D.sourceRestricted a).Y = D.Y` and
> `(D.sourceRestricted a).f = a ≫ D.f`, on which the types of the restriction maps below depend,
> are available to the unifier.

```lean
def sourceRestricted {W : AlgebraicSpaces B S hS} (a : W ⟶ D.X) :
    QuotientSituation B S hS
```

## Tag 082N, an equation

[Tag 082N](https://stacks.math.columbia.edu/tag/082N) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L305). The attribute's comment: “the functor of quotients Q\_\{F/X/Y} of F/X/Y, with its two functor laws and the stability of the quotients of the source under pullback along a morphism of test schemes”. References: SGA 3 XV (3.8), “more general”.

> The functor of quotients of `F/X/Y`,
> `Q_{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets`: its value at a test scheme `T` over `Y` is the set
> `Q_{F/X/Y}(T)` of quotients of `F_T` that are quasi-coherent and flat over `T`, and its action
> on a morphism of test schemes is pullback of quotients.

```lean
def quotientsFunctor : (SchemesOver D.Y)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 0CZL, an equation

[Tag 0CZL](https://stacks.math.columbia.edu/tag/0CZL) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPullback.lean#L338). The attribute's comment: “the finite-presentation subfunctor Q^\{fp}\_\{F/X/Y} of the functor of quotients”.

> The finite-presentation subfunctor `Q^{fp}_{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets` of the functor of
> quotients: its value at a test scheme `T` is the subset of `Q_{F/X/Y}(T)` of those quotients that
> are of finite presentation as `𝒪_{X_T}`-modules, and its action on a morphism of test schemes is
> pullback of quotients.

```lean
def finitePresentationQuotientsFunctor : (SchemesOver D.Y)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 08IT, a remark

[Tag 08IT](https://stacks.math.columbia.edu/tag/08IT) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.canonicalBaseChangedSituation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L498). The attribute's comment: “the base-changed situation F'/X'/B'”.

> The standing data of Stacks 082M obtained by changing the base algebraic space along
> `p : B' ⟶ B`: source `X' = X ×_B B'`, morphism the second projection, module the pullback `F'` of
> `F`, quasi-coherent by Stacks 03GA.

```lean
abbrev canonicalBaseChangedSituation : QuotientSituation B S hS
```

**`AlgebraicGeometry.Space.QuotientSituation.canonicalBaseChangeQuotientModuleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L506). The attribute's comment: “the identification of the quotients themselves, F'\_T/K' = F\_T/K under X'\_T ≅ X\_T”.

> **The quotients themselves correspond**, at the canonical pseudofunctoriality datum: the
> quotient `F'_T/K'` named by the subobject corresponding to `K` is the inverse image along
> `X'_T ≅ X_T` of the quotient `F_T/K`.

```lean
def canonicalBaseChangeQuotientModuleIso (T : SchemesOver Y')
    (K : Subobject (D.baseChangeModule ((CostructuredArrow.map p).obj T))) :
    (D.canonicalBaseChangedSituation p).quotientModule T
        (D.baseChangeSubobjectEquiv p (D.isQuasicoherentOnSite_baseChangedSourceModule p)
          (modulePushforwardCoherence B S hS) T K) ≅
      (modulePullback B S hS
          (D.baseChangeFiberIso p (D.isQuasicoherentOnSite_baseChangedSourceModule p) T).hom).obj
        (D.quotientModule ((CostructuredArrow.map p).obj T) K)
```

**`AlgebraicGeometry.Space.QuotientSituation.mem_quotients_canonicalBaseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L543). The attribute's comment: “the identification Q(F'/X'/B')(T) = Q(F/X/B)(T), in membership form”.

> For a test scheme `T` over `B'` a subobject of `F'_T` is an element of `Q_{F'/X'/B'}(T)`
> exactly when the corresponding subobject of `F_T` is an element of `Q_{F/X/B}(T)`, where on the
> right `T` is read as a scheme over `B` through `T ⟶ B' ⟶ B`.

```lean
theorem mem_quotients_canonicalBaseChange_iff (T : SchemesOver Y')
    (K : Subobject (D.baseChangeModule ((CostructuredArrow.map p).obj T))) :
    D.baseChangeSubobjectEquiv p (D.isQuasicoherentOnSite_baseChangedSourceModule p)
        (modulePushforwardCoherence B S hS) T K ∈
        (D.canonicalBaseChangedSituation p).quotients T ↔
      K ∈ D.quotients ((CostructuredArrow.map p).obj T)
```

**`AlgebraicGeometry.Space.QuotientSituation.quotients_canonicalBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L559). The attribute's comment: “the identification Q(F'/X'/B')(T) = Q(F/X/B)(T)”.

> `Q_{F'/X'/B'}(T) = Q_{F/X/B}(T)`: the canonical bijection of the two lattices of subobjects
> carries the set of quotients of Stacks 082M for `F/X/B` at `T`, read as a scheme over `B`, onto the
> one for `F'/X'/B'` at `T`, read as a scheme over `B'`.

```lean
theorem quotients_canonicalBaseChange (T : SchemesOver Y') :
    (D.canonicalBaseChangedSituation p).quotients T =
      D.baseChangeSubobjectEquiv p (D.isQuasicoherentOnSite_baseChangedSourceModule p)
          (modulePushforwardCoherence B S hS) T ''
        D.quotients ((CostructuredArrow.map p).obj T)
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientsCanonicalBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L568). The attribute's comment: “the bijection Q(F'/X'/B')(T) ≃ Q(F/X/B)(T)”.

> The equality `Q_{F'/X'/B'}(T) = Q_{F/X/B}(T)` read as a bijection of the two sets.

```lean
def quotientsCanonicalBaseChangeEquiv (T : SchemesOver Y') :
    D.quotients ((CostructuredArrow.map p).obj T) ≃
      (D.canonicalBaseChangedSituation p).quotients T
```

**`AlgebraicGeometry.Space.QuotientSituation.mem_finitePresentationQuotients_canonicalBaseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L580). The attribute's comment: “the same identification for the finite-presentation subfunctor, in membership form”.

> The same identification for `Q^{fp}`, in membership form: a subobject of `F'_T` is an element
> of `Q^{fp}_{F'/X'/B'}(T)` exactly when the corresponding subobject of `F_T` is an element of
> `Q^{fp}_{F/X/B}(T)`.

```lean
theorem mem_finitePresentationQuotients_canonicalBaseChange_iff (T : SchemesOver Y')
    (K : Subobject (D.baseChangeModule ((CostructuredArrow.map p).obj T))) :
    D.baseChangeSubobjectEquiv p (D.isQuasicoherentOnSite_baseChangedSourceModule p)
        (modulePushforwardCoherence B S hS) T K ∈
        (D.canonicalBaseChangedSituation p).finitePresentationQuotients T ↔
      K ∈ D.finitePresentationQuotients ((CostructuredArrow.map p).obj T)
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotients_canonicalBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L601). The attribute's comment: “the same identification for the finite-presentation subfunctor”.

> The same identification for `Q^{fp}`: `Q^{fp}_{F'/X'/B'}(T) = Q^{fp}_{F/X/B}(T)` under the
> canonical bijection of the two lattices of subobjects.

```lean
theorem finitePresentationQuotients_canonicalBaseChange (T : SchemesOver Y') :
    (D.canonicalBaseChangedSituation p).finitePresentationQuotients T =
      D.baseChangeSubobjectEquiv p (D.isQuasicoherentOnSite_baseChangedSourceModule p)
          (modulePushforwardCoherence B S hS) T ''
        D.finitePresentationQuotients ((CostructuredArrow.map p).obj T)
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsCanonicalBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorBaseChange.lean#L611). The attribute's comment: “the bijection for the finite-presentation subfunctor”.

> The equality `Q^{fp}_{F'/X'/B'}(T) = Q^{fp}_{F/X/B}(T)` read as a bijection of the two sets.

```lean
def finitePresentationQuotientsCanonicalBaseChangeEquiv (T : SchemesOver Y') :
    D.finitePresentationQuotients ((CostructuredArrow.map p).obj T) ≃
      (D.canonicalBaseChangedSituation p).finitePresentationQuotients T
```

## Tag 08IU, a remark

[Tag 08IU](https://stacks.math.columbia.edu/tag/08IU) in the Stacks Project.

**`AlgebraicGeometry.Space.bijOn_quotientRestrict_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientDescentClauses.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientDescentClauses.lean#L492). References: SGA 1 VIII (1.8), “more general”.

> **Stacks 08IU.**  Let `X` be an algebraic space over a scheme `S` of a big fppf site, let
> `F` be a quasi-coherent `𝒪_X`-module, let `{f i : X i ⟶ X}` be an fpqc covering and for each
> `i, j` let `{g i j k : X ijk ⟶ X i ×_X X j}` be an fpqc covering.  Then restriction along the
> members of the covering is a bijection from the quotients `F ⟶ Q` with `Q` quasi-coherent onto
> the families of quotients `f i ^* F ⟶ Q i` with `Q i` quasi-coherent such that `Q i` and `Q j`
> restrict to the same quotient on every `X ijk`.
>
> A quotient is recorded by its kernel, a subobject of the module, as in Situation 082M; the
> restriction of a quotient of `F` along `f i` is `AlgebraicGeometry.Space.quotientRestrict`, and
> the restrictions of `Q i` and `Q j` to `X ijk` are compared as quotients of the single inverse
> image of `F` along `X ijk ⟶ X`, through `AlgebraicGeometry.Space.quotientRestrictOver`.
>
> Injectivity is the faithfulness clause of Stacks 04W8 applied to the kernels, which are
> quasi-coherent.  For surjectivity, agreement on the `X ijk` gives agreement on `X i ×_X X j`
> (`AlgebraicGeometry.Space.quotientRestrict_pairFst_eq_of_refinement`), and the family descends
> by `AlgebraicGeometry.Space.exists_quotientRestrict_eq_of_isFpqcCovering`.

```lean
theorem bijOn_quotientRestrict_of_isFpqcCovering {I : Type v} {X : AlgebraicSpaces B S hS}
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    {Xi : I → AlgebraicSpaces B S hS} (f : ∀ i, Xi i ⟶ X)
    (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    {J : I → I → Type w} {Xijk : ∀ i j, J i j → AlgebraicSpaces B S hS}
    (g : ∀ i j k, Xijk i j k ⟶ QuasiCoherentDescent.pair B S hS Xi f i j)
    (hg : ∀ i j, IsFpqcCovering B S hS fun k ↦ (g i j k).hom) :
    Set.BijOn (fun (K : Subobject F) i ↦ quotientRestrict (f i) K)
      {K | (cokernel K.arrow).IsQuasicoherentOnSite}
      {Q | (∀ i, (cokernel (Q i).arrow).IsQuasicoherentOnSite) ∧
        ∀ i j k, quotientRestrictOver (g i j k ≫ QuasiCoherentDescent.pairFst B S hS Xi f i j)
            rfl F (Q i) =
          quotientRestrictOver (g i j k ≫ QuasiCoherentDescent.pairSnd B S hS Xi f i j)
            (pair_comp_condition f i j (g i j k)) F (Q j)}
```

## Tag 082P, a lemma

[Tag 082P](https://stacks.math.columbia.edu/tag/082P) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.quotientsFunctor_isSheaf_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean#L174). The attribute's comment: “the functor of quotients Q\_\{F/X/Y}”.

> **Stacks 082P for `Q_{F/X/Y}`.**  The functor of quotients `Q_{F/X/Y} : (Sch/Y)ᵒᵖ ⥤ Sets`
> of Stacks 082N satisfies the sheaf property for the fpqc topology.

```lean
theorem quotientsFunctor_isSheaf_fpqcTopology :
    Presheaf.IsSheaf (fpqcTopology D.Y) D.quotientsFunctor
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsFunctor_isSheaf_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean#L183). The attribute's comment: “the finite-presentation subfunctor Q^\{fp}\_\{F/X/Y}”.

> **Stacks 082P for `Q^{fp}_{F/X/Y}`.**  The finite-presentation subfunctor of the functor of
> quotients satisfies the sheaf property for the fpqc topology.

```lean
theorem finitePresentationQuotientsFunctor_isSheaf_fpqcTopology :
    Presheaf.IsSheaf (fpqcTopology D.Y) D.finitePresentationQuotientsFunctor
```

**`AlgebraicGeometry.Space.QuotientSituation.isSheafFor_quotientsFunctor_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorFpqcSheaf.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorFpqcSheaf.lean#L175).

> In Situation 082M the functor of quotients satisfies the
> sheaf property for the fpqc topology: for every fpqc covering `{U i ⟶ T}` of schemes over `Y`,
> every compatible family of quotients of the `F_{U i}`, quasi-coherent and flat over `U i`, has a
> unique amalgamation, a quotient of `F_T` quasi-coherent and flat over `T`.

```lean
theorem isSheafFor_quotientsFunctor_of_isFpqcCovering
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom) :
    Presieve.IsSheafFor D.quotientsFunctor (Presieve.ofArrows U g)
```

**`AlgebraicGeometry.Space.QuotientSituation.isSheafFor_finitePresentationQuotientsFunctor_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorFpqcSheaf.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorFpqcSheaf.lean#L198).

> In Situation 082M the finite-presentation subfunctor of the functor of quotients satisfies
> the sheaf property for the fpqc topology: for every fpqc covering `{U i ⟶ T}` of schemes over `Y`,
> every compatible family of finitely presented quotients of the `F_{U i}`, flat over `U i`, has a
> unique amalgamation, a finitely presented quotient of `F_T` flat over `T`.

```lean
theorem isSheafFor_finitePresentationQuotientsFunctor_of_isFpqcCovering
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom) :
    Presieve.IsSheafFor D.finitePresentationQuotientsFunctor (Presieve.ofArrows U g)
```

## Tag 0D3U, a lemma

[Tag 0D3U](https://stacks.math.columbia.edu/tag/0D3U) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.morEquivSpaceQuotientOfAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSpaceDescent.lean, line 690](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSpaceDescent.lean#L690). The attribute's comment: “the first displayed identification, for Q\_\{F/X/Y} and an arbitrary algebraic space T”.

> For an algebraic space `T` over `S`, the morphisms of sheaves on the big fppf site of `S`
> from `T` into the functor of quotients `Q_{F/X/Y}` of Stacks 082P are in bijection with the pairs
> `(h, F_T ⟶ Q)` consisting of a morphism `h : T ⟶ Y` of algebraic spaces and a quotient of the
> pullback `F_T` of `F` to `X ×_{Y, h} T` which is quasi-coherent and flat over `T`.
>
> The sheaf of `T` is lifted to the universe of the functor of quotients. The inverse sends a pair
> to the transformation restricting it along the chart `t : V ⟶ T` of each section `t` of `T` over
> a scheme `V` of the site (`AlgebraicGeometry.Space.QuotientSituation.SpaceQuotient.toMor`).
>
> The inverse images are composed with `AlgebraicGeometry.Space.modulePushforwardCoherence`, so
> nothing is assumed.  The untagged
> `AlgebraicGeometry.Space.QuotientSituation.morEquivSpaceQuotient` is the special case of a
> scheme `T` of the site, for any proof of that coherence.

```lean
def morEquivSpaceQuotientOfAlgebraicSpace (T : AlgebraicSpaces B S hS) :
    (T.obj ⋙ uliftFunctor.{u + 1, u} ⟶
        D.totalQuotientsFunctor (modulePushforwardCoherence B S hS)) ≃
      D.SpaceQuotients T
```

**`AlgebraicGeometry.Space.QuotientSituation.morEquivSpaceFinitePresentationQuotientOfAlgebraicSpaceUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSpaceDescent.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSpaceDescent.lean#L766). The attribute's comment: “the second displayed identification, for Q^\{fp}\_\{F/X/Y} and an arbitrary algebraic space T”.

> For an algebraic space `T` over `S`, the morphisms of sheaves on the big fppf site of `S`
> from `T` into the finite-presentation subfunctor `Q^{fp}_{F/X/Y}` of Stacks 0CZL are in bijection
> with the pairs `(h, F_T ⟶ Q)` consisting of a morphism `h : T ⟶ Y` and a quotient of `F_T` which
> is of finite presentation and flat over `T`.
>
> The subfunctor is formed with the pseudofunctoriality of inverse images
> `AlgebraicGeometry.Space.modulePushforwardCoherence` and the preservation of finite presentation
> by the base-change pullbacks
> `AlgebraicGeometry.Space.QuotientSituation.pullbackPreservesFinitePresentation`.

```lean
def morEquivSpaceFinitePresentationQuotientOfAlgebraicSpaceUnconditional
    (T : AlgebraicSpaces B S hS) :
    (T.obj ⋙ uliftFunctor.{u + 1, u} ⟶
        D.totalFinitePresentationQuotientsFunctor (modulePushforwardCoherence B S hS)
          D.pullbackPreservesFinitePresentation) ≃
      D.SpaceFinitePresentationQuotients T
```

## Tag 08IV, a lemma

[Tag 08IV](https://stacks.math.columbia.edu/tag/08IV) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.bijOn_restrictQuotientToMember`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean#L611). The attribute's comment: “the full bijection onto the matching families, every T, with nothing assumed beyond Situation 082M and the two coverings: 03LU for commutativity, 04W8 faithfulness and 03DO kernels for injectivity, 03GA and 05VW along the flat members of the covering for the restrictions, Remark 08IT (04W8 fullness and effectivity, at the quasi-coherent module of the situation) and 05VY for surjectivity”.

> **Stacks 08IV.**  In Situation 082M, let `{a i : W i ⟶ X}` be an fpqc covering of the source,
> let `P i j` be the fibre product `W i ×_X W j` and let `{Z i j k ⟶ P i j}` be fpqc coverings.
> For every scheme `T` over `Y` the diagram
>
> `Q_{F/X/Y}(T) ⟶ ∏_i Q_{F i/W i/Y}(T) ⇉ ∏_{ijk} Q_{F ijk/Z i j k/Y}(T)`
>
> presents the first arrow as the equalizer of the other two: restriction is a bijection from
> `Q_{F/X/Y}(T)` onto the set of families `(Q i)` whose two restrictions to each `Z i j k` agree.
>
> The three halves of this are
> `AlgebraicGeometry.Space.QuotientSituation.restrictQuotientToMember_mem_quotients` together with
> `AlgebraicGeometry.Space.QuotientSituation.restrictQuotientBetweenMembers_toMember`,
> `AlgebraicGeometry.Space.QuotientSituation.eq_of_restrictQuotientToMember_eq` and
> `AlgebraicGeometry.Space.QuotientSituation.exists_mem_quotients_restrictQuotientToMember_eq`.
>
> Nothing beyond Situation 082M and the two coverings is assumed.

```lean
theorem bijOn_restrictQuotientToMember
    {I : Type v} {κ : I → I → Type v} {W : I → AlgebraicSpaces B S hS}
    {P : I → I → AlgebraicSpaces B S hS} {Z : ∀ i j, κ i j → AlgebraicSpaces B S hS}
    (a : ∀ i, W i ⟶ D.X) {c₀ : ∀ i j, P i j ⟶ W i} {c₁ : ∀ i j, P i j ⟶ W j}
    {d : ∀ i j, P i j ⟶ D.X} (q : ∀ i j k, Z i j k ⟶ P i j) {e : ∀ i j k, Z i j k ⟶ D.X}
    (hcov : IsFpqcCovering B S hS fun i ↦ (a i).hom)
    (hP : ∀ i j, IsPullback (c₀ i j) (c₁ i j) (a i) (a j))
    (hd₀ : ∀ i j, c₀ i j ≫ a i = d i j) (hd₁ : ∀ i j, c₁ i j ≫ a j = d i j)
    (hqcov : ∀ i j, IsFpqcCovering B S hS fun k ↦ (q i j k).hom)
    (he₀ : ∀ i j k, (q i j k ≫ c₀ i j) ≫ a i = e i j k)
    (he₁ : ∀ i j k, (q i j k ≫ c₁ i j) ≫ a j = e i j k) (T : SchemesOver D.Y) :
    Set.BijOn (fun K i ↦
        D.restrictQuotientToMember (a i) T K)
      (D.quotients T)
      {Q | (∀ i, Q i ∈ (D.sourceRestricted (a i)).quotients T) ∧
        ∀ i j k, D.restrictQuotientBetweenMembers (q i j k ≫ c₀ i j) (he₀ i j k) T (Q i) =
          D.restrictQuotientBetweenMembers (q i j k ≫ c₁ i j) (he₁ i j k) T (Q j)}
```

**`AlgebraicGeometry.Space.QuotientSituation.bijOn_restrictQuotientToMember_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheaf.lean#L659). The attribute's comment: “the same equalizer property for the finite-presentation subfunctor Q^\{fp}, again with nothing assumed and no weakening: the inputs of bijOn\_restrictQuotientToMember together with Section 05VR for the restriction maps and 060V on the site for surjectivity”.

> **Stacks 08IV for the finite-presentation subfunctor.**  The diagram of Stacks 08IV presents
> the first arrow as the equalizer of the other two for `Q^{fp}_{F/X/Y}` as well: restriction is a
> bijection from `Q^{fp}_{F/X/Y}(T)` onto the set of families of elements of
> `Q^{fp}_{F i/W i/Y}(T)` whose two restrictions to each `Z i j k` agree.
>
> Only the two outer halves change: the restriction maps preserve finite presentation, which is
> `restrictQuotientToMember_mem_finitePresentationQuotients` of this namespace, and the quotient
> descended by
> `AlgebraicGeometry.Space.QuotientSituation.exists_mem_quotients_restrictQuotientToMember_eq` is
> of finite presentation by
> `AlgebraicGeometry.Space.finitePresentationOnSiteDescendsAlongFpqcCovering`, Stacks 060V on the
> site.
>
> Nothing beyond Situation 082M and the two coverings is assumed.

```lean
theorem bijOn_restrictQuotientToMember_finitePresentation
    {I : Type v} {κ : I → I → Type v} {W : I → AlgebraicSpaces B S hS}
    {P : I → I → AlgebraicSpaces B S hS} {Z : ∀ i j, κ i j → AlgebraicSpaces B S hS}
    (a : ∀ i, W i ⟶ D.X) {c₀ : ∀ i j, P i j ⟶ W i} {c₁ : ∀ i j, P i j ⟶ W j}
    {d : ∀ i j, P i j ⟶ D.X} (q : ∀ i j k, Z i j k ⟶ P i j) {e : ∀ i j k, Z i j k ⟶ D.X}
    (hcov : IsFpqcCovering B S hS fun i ↦ (a i).hom)
    (hP : ∀ i j, IsPullback (c₀ i j) (c₁ i j) (a i) (a j))
    (hd₀ : ∀ i j, c₀ i j ≫ a i = d i j) (hd₁ : ∀ i j, c₁ i j ≫ a j = d i j)
    (hqcov : ∀ i j, IsFpqcCovering B S hS fun k ↦ (q i j k).hom)
    (he₀ : ∀ i j k, (q i j k ≫ c₀ i j) ≫ a i = e i j k)
    (he₁ : ∀ i j k, (q i j k ≫ c₁ i j) ≫ a j = e i j k) (T : SchemesOver D.Y) :
    Set.BijOn (fun K i ↦
        D.restrictQuotientToMember (a i) T K)
      (D.finitePresentationQuotients T)
      {Q | (∀ i, Q i ∈ (D.sourceRestricted (a i)).finitePresentationQuotients T) ∧
        ∀ i j k, D.restrictQuotientBetweenMembers (q i j k ≫ c₀ i j) (he₀ i j k) T (Q i) =
          D.restrictQuotientBetweenMembers (q i j k ≫ c₁ i j) (he₁ i j k) T (Q j)}
```

**`AlgebraicGeometry.Space.QuotientSituation.bijOn_restrictQuotientToMember_of_isFpqcCovering`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheafUnconditional.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheafUnconditional.lean#L81).

> In Situation 082M, let `{a i : W i ⟶ X}` be an fpqc covering of the source, let `P i j` be the
> fibre product `W i ×_X W j` and let `{Z i j k ⟶ P i j}` be fpqc coverings. For every scheme `T`
> over `Y` the diagram
>
> `Q_{F/X/Y}(T) ⟶ ∏_i Q_{F i/W i/Y}(T) ⇉ ∏_{ijk} Q_{F ijk/Z i j k/Y}(T)`
>
> presents the first arrow as the equalizer of the other two: restriction is a bijection from
> `Q_{F/X/Y}(T)` onto the set of families `(Q i)` of elements of the `Q_{F i/W i/Y}(T)` whose two
> restrictions `pr₀^*`, `pr₁^*` to each `Z i j k` agree.  Being a bijection onto that set is the
> commutativity `pr₀^* ∘ res = pr₁^* ∘ res`, the injectivity of `res`, and the surjectivity of
> `res` onto the equalizer.
>
> Here `F i` is the inverse image of `F` along `a i` and `F ijk` the inverse image of `F` along the
> single morphism `e i j k : Z i j k ⟶ X`.

```lean
alias bijOn_restrictQuotientToMember_of_isFpqcCovering
```

**`AlgebraicGeometry.Space.QuotientSituation.bijOn_restrictQuotientToMember_finitePresentation_of_isFpqcCovering`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheafUnconditional.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorSourceSheafUnconditional.lean#L89).

> The diagram of Stacks 08IV presents the first arrow as the equalizer of the other two for
> `Q^{fp}_{F/X/Y}` as well: restriction is a bijection from `Q^{fp}_{F/X/Y}(T)` onto the set of
> families of elements of the `Q^{fp}_{F i/W i/Y}(T)` whose two restrictions to each `Z i j k`
> agree.

```lean
alias bijOn_restrictQuotientToMember_finitePresentation_of_isFpqcCovering
```

## Tag 082Q, a lemma

[Tag 082Q](https://stacks.math.columbia.edu/tag/082Q) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsFunctor_limitPreserving_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorLimitPreservingUnconditional.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorLimitPreservingUnconditional.lean#L85). The attribute's comment: “corrected per the 082Q erratum: f also locally of finite presentation; as written the statement is false, see not\_forall\_finitePresentationQuotientsFunctor\_limitPreserving”.

> **Stacks 082Q, corrected.**  In Situation 082M assume that (a) `f : X ⟶ Y` is quasi-compact
> and quasi-separated, and also locally of finite presentation, and (b) `F` is of finite
> presentation.  Then `Q^{fp}_{F/X/Y}` is limit preserving: for a directed limit `T = lim T_i` of
> affine schemes over `Y`, `Q^{fp}_{F/X/Y}(T) = colim Q^{fp}_{F/X/Y}(T_i)`.
>
> The tag as written, without local finite presentation of `f`, is false:
> `not_forall_finitePresentationQuotientsFunctor_limitPreserving`
> (in `StacksFrontier.AlgebraicGeometry.Quot.QuotientFunctorLimitPreservingSpaceCounterexample`)
> proves the negation, with `X = Spec ℚ[t][y_a]/((t - a) y_a)` over `Spec ℚ[t]` and
> `T = Spec ℚ(t)`.

```lean
theorem finitePresentationQuotientsFunctor_limitPreserving_of_isLocallyOfFinitePresentation
    (D : QuotientSituation B S hS) (hqc : IsQuasiCompact B S hS D.f.hom)
    (hqs : IsQuasiSeparated B S hS D.f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS D.f.hom)
    (hF : D.F.IsFinitePresentationOnSite) :
    LimitPreserving.{u, u + 1, u, u} D.testScheme D.finitePresentationQuotientsFunctor
```

## Tag 08IW, a lemma

[Tag 08IW](https://stacks.math.columbia.edu/tag/08IW) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.quotientsPushoutMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPushoutBijective.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPushoutBijective.lean#L70).

> **Stacks 08IW**, for `Q_{F/X/B}`: for a pushout `Y' = Y ⊔_Z Z'` of schemes over `B` along a
> thickening `Z ⟶ Z'` and an affine morphism `Z ⟶ Y`, the natural map
> `Q_{F/X/B}(Y') ⟶ Q_{F/X/B}(Y) ×_{Q_{F/X/B}(Z)} Q_{F/X/B}(Z')` is bijective.

```lean
theorem quotientsPushoutMap_bijective :
    Function.Bijective (D.quotientsPushoutMap i f g h hpo)
```

**`AlgebraicGeometry.Space.QuotientSituation.finitePresentationQuotientsPushoutMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPushoutBijective.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorPushoutBijective.lean#L80).

> **Stacks 08IW**, for `Q^{fp}_{F/X/B}`: if moreover `X ⟶ B` is locally of finite
> presentation, the natural map `Q^{fp}(Y') ⟶ Q^{fp}(Y) ×_{Q^{fp}(Z)} Q^{fp}(Z')` is
> bijective.

```lean
theorem finitePresentationQuotientsPushoutMap_bijective
    (hlfp : IsLocallyOfFinitePresentation B S hS D.f.hom) :
    Function.Bijective (D.finitePresentationQuotientsPushoutMap i f g h hpo)
```

## Tag 0CZU, a remark

[Tag 0CZU](https://stacks.math.columbia.edu/tag/0CZU) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.quotientObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L253).

> **Remark 0CZU: the obstruction vanishes exactly when the quotient lifts.** For `x ∈ Q(T)`
> given by `K ⊂ F_T`, `o_x(T') = 0` if and only if there is `x' ∈ Q(T')` restricting to `x`.

```lean
theorem quotientObstruction_eq_zero_iff {K : Subobject (D.baseChangeModule T)}
    (hK : K ∈ D.quotients T) :
    D.quotientObstruction hF h hh K = 0 ↔ ∃ K' ∈ D.quotients T', D.quotientPullback h K' = K
```

**`AlgebraicGeometry.Space.QuotientSituation.mem_finitePresentationQuotients_of_quotientPullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L272).

> **Remark 0CZU, finite presentation (Stacks 08VU).** If `x ∈ Q^{fp}(T)`, every lift
> `x' ∈ Q(T')` of `x` lies in `Q^{fp}(T')`.

```lean
theorem mem_finitePresentationQuotients_of_quotientPullback_eq
    {K : Subobject (D.baseChangeModule T)} (hK : K ∈ D.finitePresentationQuotients T)
    {K' : Subobject (D.baseChangeModule T')} (hK' : K' ∈ D.quotients T')
    (hpb : D.quotientPullback h K' = K) :
    K' ∈ D.finitePresentationQuotients T'
```

**`AlgebraicGeometry.Space.QuotientSituation.reductionShortComplex_relativeSquare_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L319).

> **Remark 0CZU: `0 ⟶ f_T^*𝒥 ⊗ F_T ⟶ F_{T'} ⟶ F_T ⟶ 0` is exact.** Since `F_{T'}` is flat
> over `T'`, the reduction `π : F_{T'} ⟶ F_T` (read on `X_{T'}`) has kernel `f_T^*𝒥 ⊗ F_T`, embedded
> by `i`.

```lean
theorem reductionShortComplex_relativeSquare_shortExact :
    (reductionShortComplex (smallEtaleRingedToposHom B S hS (D.relativeMap h))
      (D.relativeSquareThickening h) (D.relativeSquareLeft h)
      (relBaseRight (smallEtaleRingedToposHom B S hS (D.projection T')))
      (D.relativeMapFirstOrderThickening h hh) (D.relativeSquareThickeningFirstOrderThickening h hh)
      (D.relativeSquare_comm h) (D.baseChangeModule T') (D.isStrict_relativeSquare h hh)
      (D.isFlat_baseChangeModule_relBaseRight hF T')).ShortExact
```

**`AlgebraicGeometry.Space.QuotientSituation.isIso_baseIdealTensorToIdealTensor_relativeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L339).

> **Remark 0CZU: `f_T^*𝒥 ⊗ F_T = I ⊗ F_T` (Stacks 08MQ).** The canonical comparison of
> `f_T^*𝒥 ⊗ F_T` with `I ⊗ F_T`, for `F_T = F_{T'}|_{X_T}`, is an isomorphism.

```lean
theorem isIso_baseIdealTensorToIdealTensor_relativeSquare :
    IsIso (baseIdealTensorToIdealTensor (smallEtaleRingedToposHom B S hS (D.relativeMap h))
      (D.relativeSquareThickening h) (D.relativeSquareLeft h)
      (relBaseRight (smallEtaleRingedToposHom B S hS (D.projection T')))
      (D.relativeMapFirstOrderThickening h hh) (D.relativeSquareThickeningFirstOrderThickening h hh)
      (D.relativeSquare_comm h)
      ((modulePullback B S hS (D.relativeMap h)).obj (D.baseChangeModule T')))
```

**`AlgebraicGeometry.Space.QuotientSituation.obstructionKernel_baseIdealTensor_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L358).

> **Remark 0CZU: `0 ⟶ K ⊗_{𝒪_T} 𝒥 ⟶ F_T ⊗_{𝒪_T} 𝒥 ⟶ Q ⊗_{𝒪_T} 𝒥 ⟶ 0` is exact**, `Q` being
> flat over `T`. Here `G ⊗_{𝒪_T} 𝒥 = f_T^*𝒥 ⊗ G`.

```lean
theorem obstructionKernel_baseIdealTensor_shortExact {K : Subobject (D.baseChangeModule T)}
    (hK : K ∈ D.quotients T) :
    ((ShortComplex.mk (C := SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedTopos B S hS (D.space T)).O)) (D.obstructionKernel h K).arrow
        (cokernel.π (D.obstructionKernel h K).arrow)
      (cokernel.condition _)).map (baseIdealTensor.{u, u + 1, u, u, u + 1, u, u, u + 1, u}
        (D.relativeSquareThickening h) (D.relativeSquareLeft h)
        (D.relativeSquareThickeningFirstOrderThickening h hh))).ShortExact
```

**`AlgebraicGeometry.Space.QuotientSituation.quotientObstructionExtension_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorObstruction.lean#L376).

> **Remark 0CZU: the canonical extension
> `0 ⟶ Q ⊗_{𝒪_T} 𝒥 ⟶ π⁻¹(K)/i(K ⊗_{𝒪_T} 𝒥) ⟶ K ⟶ 0` of `𝒪_{X_T}`-modules is short exact.** Its
> class is `AlgebraicGeometry.Space.QuotientSituation.quotientObstruction`.

```lean
theorem quotientObstructionExtension_shortExact (K : Subobject (D.baseChangeModule T)) :
    (quotientLiftExtension (smallEtaleRingedToposHom B S hS (D.relativeMap h))
      (D.relativeSquareThickening h) (D.relativeSquareLeft h)
      (relBaseRight (smallEtaleRingedToposHom B S hS (D.projection T')))
      (D.relativeMapFirstOrderThickening h hh) (D.relativeSquareThickeningFirstOrderThickening h hh)
      (D.relativeSquare_comm h) (D.baseChangeModule T') (D.isStrict_relativeSquare h hh)
      (D.isFlat_baseChangeModule_relBaseRight hF T') (D.obstructionKernel h K)).ShortExact
```

**`AlgebraicGeometry.Space.QuotientSituation.isStrict_relativeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorRelativeSquareStrict.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorRelativeSquareStrict.lean#L551).

> **Remark 0CZU: the ideal `I` of `X_T ⊂ X_{T'}` is a quotient of `f_T^*𝒥`.** The relative
> square is strict (Stacks 08M9): the map of ideals `f̃'^*(f'⁻¹𝒥) ⟶ I` of the morphism of
> thickenings of Stacks 08M7, built from the first order thickenings `X_T ⊂ X_{T'}` and
> `t̃ = (id, f'⁻¹t^♯)` and the commutative square `f̃' ∘ i = t̃ ∘ f̃`, is an epimorphism.

```lean
theorem isStrict_relativeSquare :
    MorphismOfThickenings.IsStrict.{u, u + 1, u, u, u + 1, u, u, u + 1, u, u, u + 1, u}
      (MorphismOfThickenings.ofFirstOrderThickenings.{u, u + 1, u, u, u + 1, u, u + 1, u, u,
          u + 1, u}
        (smallEtaleRingedToposHom B S hS (D.relativeMap h)) (D.relativeSquareThickening h)
        (D.relativeSquareLeft h) (relBaseRight (smallEtaleRingedToposHom B S hS (D.projection T')))
        (D.relativeMapFirstOrderThickening h hh)
        (D.relativeSquareThickeningFirstOrderThickening h hh) (D.relativeSquare_comm h))
```

**`AlgebraicGeometry.Space.QuotientSituation.isFirstOrderThickening_range_relativeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorThickening.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorThickening.lean#L89).

> **Remark 0CZU, `X_T ⊂ X_{T'}` is a first order thickening**: the image of `X_T` in `X_{T'}`,
> which is the inverse image of the first order thickening `T ⊂ T'`, is a first order thickening of
> `X_{T'}` (Stacks 09ZX).

```lean
theorem isFirstOrderThickening_range_relativeMap :
    IsFirstOrderThickening B S hS (D.space T') (Subfunctor.range (D.relativeMap h).hom)
```

## Tag 0CZV, a remark

[Tag 0CZV](https://stacks.math.columbia.edu/tag/0CZV) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotientSituation.exists_addTorsor_quotientLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorDeformationTorsor.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotientFunctorDeformationTorsor.lean#L168).

> In Situation 082M with `F` flat over `B`, let
> `T ⊂ T'` be a first order thickening of schemes over `B` with ideal sheaf `𝒥`, and let
> `x ∈ Q_{F/X/B}(T)` be given by `0 ⟶ 𝒦 ⟶ F_T ⟶ 𝒬 ⟶ 0` (`K ∈ D.quotients T`). If the obstruction
> `o_x(T')` of Remark 0CZU vanishes (`D.quotientObstruction hF h hh K = 0`), the set of lifts
> `x' ∈ Q_{F/X/B}(T')` of `x` (`D.quotientLifts h K`: the `K' ∈ D.quotients T'` with
> `D.quotientPullback h K' = K`) is a principal homogeneous space under
> `Hom_{𝒪_{X_T}}(𝒦, 𝒬 ⊗_{𝒪_T} 𝒥)` (`D.deformationGroup h hh K`), with the action of the remark:
> `φ` sends `𝒦'` to `𝒦'_φ` (`D.quotientLiftAction hF h hh hK φ K'`).

```lean
theorem exists_addTorsor_quotientLifts {K : Subobject (D.baseChangeModule T)}
    (hK : K ∈ D.quotients T) (ho : D.quotientObstruction.{e} hF h hh K = 0) :
    ∃ Tor : AddTorsor (D.deformationGroup h hh K) (D.quotientLifts h K),
      ∀ (φ : D.deformationGroup h hh K) (K' : D.quotientLifts h K),
        (Tor.vadd φ K').val = D.quotientLiftAction hF h hh hK φ K'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.7, Tag 082L](https://stacks.math.columbia.edu/tag/082L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
