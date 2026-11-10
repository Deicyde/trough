---
declaration: section
origin: cited
lean: Stacks.Topos.Skyscraper.skyscraperAb_exact, Stacks.Topos.Skyscraper.abelianEta, Stacks.Topos.Skyscraper.abelianEta_hom, Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod, Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod_fst, Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod_inl, Stacks.Topos.Skyscraper.auxKernelComplementAbFunctorObjIso, Stacks.Topos.Skyscraper.kernelComplementAbFunctorNatIso
statement: formalized
proof: formalized
---

# 18.37 Skyscraper sheaves

Section 18.37 of the Stacks Project, [Tag 05V6](https://stacks.math.columbia.edu/tag/05V6). 3 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05V7, a lemma

[Tag 05V7](https://stacks.math.columbia.edu/tag/05V7) in the Stacks Project.

**`Stacks.Topos.Skyscraper.skyscraperAb_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperExact.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperExact.lean#L157). The attribute's comment: “(1) p\_* is exact”.

> The direct image `p_* : Ab ⥤ Ab(C)` of a point of a topos is exact.

```lean
theorem skyscraperAb_exact [HasSheafify J AddCommGrpCat.{w}] :
    exactFunctor AddCommGrpCat.{w} (Sheaf J AddCommGrpCat.{w}) (skyscraperAb p)
```

**`Stacks.Topos.Skyscraper.abelianEta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L94). The attribute's comment: “skyscraper\_splitting”.

> The canonical map from an abelian group into the stalk of its skyscraper,
> natural in the abelian group. Its underlying map is the elementwise map of
> Stacks Project, Tag 05UX.

```lean
noncomputable def abelianEta (p : PointOfTopos.{w, v, u} J) :
    NatTrans (Functor.id (CommGrp (Type w))) (stalkSkyscraperAbFunctor p)
```

**`Stacks.Topos.Skyscraper.abelianEta_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L106). The attribute's comment: “skyscraper\_splitting”.

> The natural section on abelian group objects has the canonical underlying
> map of Stacks Project, Tag 05UX.

```lean
theorem abelianEta_hom (p : PointOfTopos.{w, v, u} J)
    (A : CommGrp (Type w)) :
    ((abelianEta p).app A).hom.hom.hom = (p.counitSection.app A.X)
```

**`Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L203). The attribute's comment: “skyscraper\_splitting”.

> **Stacks Project, Tag 05V7.** The decomposition
> `p⁻¹p_*A = A ⊕ Iₚ(A)` is functorial in the abelian group `A`.

```lean
noncomputable def stalkSkyscraperAbFunctorIsoBiprod
    (p : PointOfTopos.{w, v, u} J) :
    Iso (stalkSkyscraperAbFunctor p ⋙ commGrpAddEquivalence.functor)
      (commGrpAddEquivalence.functor ⊞ kernelComplementAbFunctor p)
```

**`Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L211). The attribute's comment: “skyscraper\_splitting”.

> The first projection of the splitting is the canonical counit.

```lean
theorem stalkSkyscraperAbFunctorIsoBiprod_fst
    (p : PointOfTopos.{w, v, u} J) :
    (stalkSkyscraperAbFunctorIsoBiprod p).hom ≫ biprod.fst =
      Functor.whiskerRight (abelianCounit p) commGrpAddEquivalence.functor
```

**`Stacks.Topos.Skyscraper.stalkSkyscraperAbFunctorIsoBiprod_inl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L226). The attribute's comment: “skyscraper\_splitting”.

> The first inclusion of the splitting is the canonical map from an
> abelian group into the stalk of its skyscraper.

```lean
theorem stalkSkyscraperAbFunctorIsoBiprod_inl
    (p : PointOfTopos.{w, v, u} J) :
    Functor.whiskerRight (abelianEta p) commGrpAddEquivalence.functor ≫
      (stalkSkyscraperAbFunctorIsoBiprod p).hom = biprod.inl
```

**`Stacks.Topos.Skyscraper.auxKernelComplementAbFunctorObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L243). The attribute's comment: “skyscraper\_splitting”.

> Objectwise, the auxiliary kernel functor is canonically isomorphic to the
> prescribed `Iₚ`.

```lean
noncomputable def auxKernelComplementAbFunctorObjIso
    (p : PointOfTopos.{w, v, u} J)
    (A : CommGrp (Type w)) :
    (auxKernelComplementAbFunctor p).obj A ≅ PointOfTopos.kernelComplementOfCounit p A
```

**`Stacks.Topos.Skyscraper.kernelComplementAbFunctorNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperStalkSplitting.lean#L266). The attribute's comment: “skyscraper\_splitting”.

> The identification of the kernel summand with `Iₚ` is natural, not merely
> an objectwise identification.

```lean
noncomputable def kernelComplementAbFunctorNatIso
    (p : PointOfTopos.{w, v, u} J) :
    Iso (kernelComplementAbFunctor p ⋙ commGrpAddEquivalence.inverse)
      (auxKernelComplementAbFunctor p)
```

## Tag 05V8, a lemma

[Tag 05V8](https://stacks.math.columbia.edu/tag/05V8) in the Stacks Project.

**`Stacks.Sheaves.RingedPoint.RingedPointSituation.pushforwardModules_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean#L265). The attribute's comment: “exactness of the direct image”.

> **Stacks 05V8.** The direct image of modules from a ringed point is exact.

```lean
theorem pushforwardModules_exact
    [HasWeakSheafify s.point.J AddCommGrpCat.{w}]
    [s.point.J.WEqualsLocallyBijective AddCommGrpCat.{w}] :
    exactFunctor
      (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf s.point.O))
      (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (pushforwardModules s.toRingedToposHom)
```

**`Stacks.Sheaves.RingedPoint.RingedPointSituation.pullbackPushforwardModules_counit_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean#L333). The attribute's comment: “surjectivity of the counit”.

> **Stacks 05V8.** The canonical map `p^*p_*M ⟶ M` is a surjection of `O_p`-modules: it is
> the counit of the pullback-pushforward adjunction of Stacks 03D7, hence a morphism of sheaves
> of modules, and it is an epimorphism because the direct image is faithful.

```lean
theorem pullbackPushforwardModules_counit_epi
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [HasWeakSheafify s.point.J AddCommGrpCat.{w}]
    [s.point.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (M : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf s.point.O)) :
    Epi ((pullbackAdjPushforwardModules s.toRingedToposHom).counit.app M)
```

**`Stacks.Sheaves.RingedPoint.RingedPointSituation.pullbackPushforwardModules_counit_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointPushforward.lean#L456). The attribute's comment: “(2) the canonical surjection p⁻¹p\_*M → M is O\_p-linear”.

> **Stacks 05V8.** The canonical surjection `p⁻¹p_*M ⟶ M` of Stacks 05V7 — the counit of the
> adjunction `p⁻¹ ⊣ p_*` of the point — is `O_p`-linear: under the canonical identification
> `p⁻¹p_*M = (p^*p_*M)^♭` it is the underlying map of the counit `p^*p_*M ⟶ M` of the adjunction
> of Stacks 03D7 for modules, which is a morphism of sheaves of `O_p`-modules by construction.
>
> This is the source's argument: `p⁻¹O = O_p`, hence `p^* = p⁻¹`, hence the map of Stacks 05V7 is
> the counit of the adjunction for modules, "whence linear".

```lean
theorem pullbackPushforwardModules_counit_stalk
    [HasWeakSheafify s.point.J AddCommGrpCat.{w}]
    [s.point.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (M : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf s.point.O)) :
    (Sheaf.moduleSheafFunctor (Stacks.SheafOfModules.Tensor.ringSheaf s.point.O) ⋙
      s.pointEquiv.functor).map
        ((pullbackAdjPushforwardModules s.toRingedToposHom).counit.app M) =
      (s.pullbackPushforwardStalkIso M).hom ≫
        p.adj.counit.app (s.pointEquiv.functor.obj
          ((Sheaf.moduleSheafFunctor
            (Stacks.SheafOfModules.Tensor.ringSheaf s.point.O)).obj M))
```

**`Stacks.Sheaves.RingedPoint.GSets.realSMul_eq_twistedSMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointSplittingNotLinear.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointSplittingNotLinear.lean#L261). The attribute's comment: “(3) the O\_p-module structure on p⁻¹p\_*M is (r f)(σ) = σ(r) f(σ)”.

> **Stacks Project, Tag 05V8, part (3).** The `𝒪_p`-module structure on `p⁻¹p_*M = Map(G, M)`
> is `(r f)(σ) = σ(r) f(σ)`.
>
> This is the source's own justification, and it is applied to the actual structure rather than
> assumed of it: `realSMul` is `G`-equivariant (`translate_realSMul`) and evaluation at `1_G` is
> `R`-linear for it (`realSMul_one`), and by `twistedSMul_eq_of_equivariant_of_evalOne` there is
> exactly one such scalar action, namely `twistedSMul`.

```lean
theorem realSMul_eq_twistedSMul (r : R) (f : G → M) :
    realSMul G R M r f = twistedSMul G R M r f
```

**`Stacks.Sheaves.RingedPoint.GSets.not_isRealLinear_skyscraperSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointSplittingNotLinear.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointSplittingNotLinear.lean#L339). The attribute's comment: “(3) the splitting is not O\_p-linear in general”.

> **Stacks Project, Tag 05V8, part (3).** The functorial direct sum decomposition
> `p⁻¹p_*M = M ⊕ I(M)` of Stacks 05V7 is **not** `𝒪_p`-linear in general.
>
> Take for `p` the point of the topos of `G`-sets whose inverse image forgets the action, and for
> `𝒪` the sheaf of rings attached to a commutative ring `R` with an action of `G`, so that
> `𝒪_p = R`. Then `p⁻¹p_*R = Map(G, R)`, the counit is evaluation at `1_G` and the canonical
> section of the splitting sends `r` to the constant function with value `r`. That section is not
> linear for the actual `𝒪_p`-module structure on `p⁻¹p_*R` — the pointwise action of the sections
> of `𝒪` over `{}_G G`, read through `𝒪_p = R`, which is `realSMul` — as soon as some `σ` moves
> some `r`: by `realSMul_eq_twistedSMul` that action carries the constant function `1` to
> `σ ↦ σ(r₀)`, which is not constant.

```lean
theorem not_isRealLinear_skyscraperSection
    (e : Action (Type w) G ≌ Sheaf J (Type w)) {σ₀ : G} {r₀ : R} (h : σ₀ • r₀ ≠ r₀) :
    ¬ IsRealLinear G R R (fun r =>
      skyscraperStalkEquiv G e R ((forgetfulPoint G e).counitSection.app R r))
```

## Tag 05V9, an example

[Tag 05V9](https://stacks.math.columbia.edu/tag/05V9) in the Stacks Project.

**`Stacks.Sites.GSets.skyscraperStalkEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L196). The attribute's comment: “p⁻¹p\_*M = Map(G, M)”.

> **Stacks Project, Tag 05V9.** The identification `p⁻¹p_*E = Map(G, E)`: the direct image of
> `E` is the `G`-set `Map(G, E)` and the inverse image forgets the action.

```lean
def skyscraperStalkEquiv (E : Type w) :
    ((forgetfulPoint G e).pushforward ⋙ (forgetfulPoint G e).inverseImage).obj E ≃ (G → E)
```

**`Stacks.Sites.GSets.counit_app_eq_skyscraperStalkEquiv_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L213). The attribute's comment: “the counit p⁻¹p\_*M → M is evaluation at 1\_G”.

> **Stacks Project, Tag 05V9.** Under the identification of `p⁻¹p_*E` with `Map(G, E)` the
> counit `p⁻¹p_*E ⟶ E` is evaluation at `1_G`.

```lean
theorem counit_app_eq_skyscraperStalkEquiv_one (E : Type w)
    (x : ((forgetfulPoint G e).pushforward ⋙ (forgetfulPoint G e).inverseImage).obj E) :
    (forgetfulPoint G e).adj.counit.app E x = skyscraperStalkEquiv G e E x 1
```

**`Stacks.Sites.GSets.skyscraperStalkEquiv_counitSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L220). The attribute's comment: “M → Map(G, M) assigns to m the constant function with value m”.

> **Stacks Project, Tag 05V9.** Under the identification of `p⁻¹p_*E` with `Map(G, E)` the
> canonical section of the counit sends `m` to the constant function with value `m`.

```lean
theorem skyscraperStalkEquiv_counitSection (E : Type w) (m : E) :
    skyscraperStalkEquiv G e E ((forgetfulPoint G e).counitSection.app E m) =
      Function.const G m
```

**`Stacks.Sites.GSets.kernelCounitEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L234). The attribute's comment: “I(M) = \{f : G → M | f(1\_G) = 0}”.

> **Stacks Project, Tag 05V9.** `I(M) = {f : G → M | f(1_G) = 0}`: the kernel of the counit at
> an abelian group object `A` is the set of functions `G → A` vanishing at `1_G`. An abelian group
> object is written multiplicatively, so its zero is denoted `1`.

```lean
def kernelCounitEquiv (A : CommGrp (Type w)) :
    {x : ((forgetfulPoint G e).pushforward ⋙ (forgetfulPoint G e).inverseImage).obj A.X //
        (forgetfulPoint G e).adj.counit.app A.X x =
          (1 : commGrpTypeEquivalenceCommGrp.functor.obj A)} ≃
      {f : G → A.X // f 1 = (1 : commGrpTypeEquivalenceCommGrp.functor.obj A)}
```

**`Stacks.Sites.GSets.stalkEquivSectionsAtRegular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L344). The attribute's comment: “𝒪\_p = R forgetting the G-action: the stalk is the ring of sections over \{}\_G G”.

> **Stacks Project, Tag 05V9.** The stalk `𝒪_p` of the sheaf of rings attached to `R` is its
> ring of sections over an object presenting the regular `G`-set; with
> `sectionsAtRegularRingEquiv` this is `𝒪_p = R`.

```lean
def stalkEquivSectionsAtRegular :
    (forgetfulPoint G e).inverseImage.obj (e.functor.obj (Action.ofMulAction G R)) ≃
      (equivariantSubring G R (ι.obj u₀))
```

**`Stacks.Sites.GSets.sectionsAtRegularRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/SkyscraperOnGSets.lean#L355). The attribute's comment: “𝒪\_p = R forgetting the G-action: that ring is R”.

> **Stacks Project, Tag 05V9.** `𝒪_p = R` where we forget the `G`-action: evaluation at the
> base point is a ring isomorphism from the sections of the sheaf of rings attached to `R` over an
> object presenting the regular `G`-set onto `R`.

```lean
def sectionsAtRegularRingEquiv : (equivariantSubring G R (ι.obj u₀)) ≃+* R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.37, Tag 05V6](https://stacks.math.columbia.edu/tag/05V6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
