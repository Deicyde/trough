---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentPullbackDirectImageAdjunction, AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentDirectImageIsoComposite, AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImageIsoComposite, AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImageDeltaFunctor, AlgebraicGeometry.Stack.quasicoherentPushforward, AlgebraicGeometry.Stack.higherDirectImageQuasicoherent, AlgebraicGeometry.Stack.quasicoherentPullbackPushforwardAdjunction, AlgebraicGeometry.Stack.AlgebraicStacks.fppfQuasicoherentPushforward
statement: formalized
proof: formalized
---

# 103.11 Pushforward of quasi-coherent modules

Section 103.11 of the Stacks Project, [Tag 070A](https://stacks.math.columbia.edu/tag/070A). 7 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 077A, a proposition

[Tag 077A](https://stacks.math.columbia.edu/tag/077A) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentPullbackDirectImageAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImage.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImage.lean#L234). The attribute's comment: “first assertion: f^* on quasi-coherent modules has the right adjoint f\_\{QCoh,*} = Q ∘ f\_* ∘ i, for every 1-morphism of algebraic stacks”.

> **Stacks 077A, the first assertion: `f^* : QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)` has the right adjoint
> `f_{QCoh,*}`**, defined as the composite of the inclusion, the direct image of modules
> (**Stacks 06WE**) and the coherator (**Stacks 0778**, **Stacks 0781** part (2)).
>
> It holds for every 1-morphism; the source states it for quasi-compact and quasi-separated ones,
> for which the direct image of a quasi-coherent module lies in `LQCoh^fbc(𝒪_𝒴)`, where the
> coherator is the one of **Stacks 0778**.

```lean
def quasicoherentPullbackDirectImageAdjunction :
    quasicoherentPullback B S hS f ⊣ quasicoherentDirectImage B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentDirectImageIsoComposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean#L143). The attribute's comment: “f\_\{QCoh,*} is the composite QCoh(O\_X) → LQCoh^fbc(O\_X) → LQCoh^fbc(O\_Y) → QCoh(O\_Y) of the inclusion, f\_* of Stacks 0771 and Q of Stacks 0778”.

> **Stacks 077A**: `f_{QCoh,*}` is the composite
> `QCoh(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒴) → QCoh(𝒪_𝒴)` of the inclusion, the direct image
> of **Stacks 0771** and the coherator `Q` of **Stacks 0778**, the restriction of the coherator to
> `LQCoh^fbc(𝒪_𝒴)`.

```lean
def quasicoherentDirectImageIsoComposite :
    quasicoherentDirectImage B S hS f ≅
      (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).lift (quasicoherentInclusion B S hS 𝒳)
          (lqcohSheafFbcFppfModules_quasicoherentInclusion B E h S hS 𝒳) ⋙
        lqcohSheafFbcDirectImage B E h S hS f hqc hqs ⋙
          ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒴).ι ⋙ coherator B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImageIsoComposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean#L156). The attribute's comment: “R^i f\_\{QCoh,*} is the composite QCoh(O\_X) → LQCoh^fbc(O\_X) → LQCoh^fbc(O\_Y) → QCoh(O\_Y) of the inclusion, R^i f\_* of Stacks 0771 and Q of Stacks 0778”.

> **Stacks 077A**: `Rⁱf_{QCoh,*}` is the composite
> `QCoh(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒴) → QCoh(𝒪_𝒴)` of the inclusion, the higher direct
> image `Rⁱf_*` of **Stacks 0771** and the coherator `Q` of **Stacks 0778**.

```lean
def quasicoherentHigherDirectImageIsoComposite (i : ℕ) :
    quasicoherentHigherDirectImage B S hS f i ≅
      (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).lift (quasicoherentInclusion B S hS 𝒳)
          (lqcohSheafFbcFppfModules_quasicoherentInclusion B E h S hS 𝒳) ⋙
        lqcohSheafFbcHigherDirectImage B E h S hS f hqc hqs i ⋙
          ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒴).ι ⋙ coherator B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImageDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean#L172). The attribute's comment: “second assertion: \{R^i f\_\{QCoh,*}}\_\{i ≥ 0} forms a cohomological δ-functor QCoh(O\_X) ⥤ QCoh(O\_Y), for f quasi-compact and quasi-separated”.

> **Stacks 077A, the second assertion: `{Rⁱf_{QCoh,*}}_{i ≥ 0}` is a cohomological δ-functor**
> (**Stacks 010Q**) `QCoh(𝒪_𝒳) ⥤ QCoh(𝒪_𝒴)`, for a quasi-compact and quasi-separated 1-morphism
> `f` of algebraic stacks.  Its degree-`i` functor is
> `AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImage` (by `rfl`), the
> composite `Q ∘ Rⁱf_* ∘ i`.

```lean
def quasicoherentHigherDirectImageDeltaFunctor :
    DeltaFunctor (quasicoherentModules B S hS 𝒳) (quasicoherentModules B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.quasicoherentPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L349). The attribute's comment: “f\_\{QCoh,*} as the composite of the inclusion of Stacks 06WG, the direct image of Stacks 06WE on all modules, and the coherator of Stacks 0781 part (2); the coherator's three special-adjoint-functor-theorem inputs from Stacks 0781 part (1) are carried as the named hypotheses hclosed, hwp, hsep”.

> **Stacks 077A: the quasi-coherent direct image `f_{QCoh,*}`.**  Include the quasi-coherent
> modules of `𝒳` into all modules on its associated fppf site, take the direct image of
> **Stacks 06WE**, and come back with the coherator of **Stacks 0781** part (2).
>
> The source's middle slot is the direct image of **Stacks 0771** on `LQCoh^fbc(𝒪_𝒳)` and its
> coherator is the one of **Stacks 0778**; the two readings agree on the quasi-compact and
> quasi-separated 1-morphisms the source states 077A for, and this one needs neither hypothesis.
> See the implementation notes.

```lean
def quasicoherentPushforward :
    FibredSite.quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u, u + 1} B S hS q hq
```

**`AlgebraicGeometry.Stack.higherDirectImageQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L361). The attribute's comment: “R^i f\_\{QCoh,*} as the same composite with the i-th higher direct image of modules in the middle slot; the coherator's three inputs from Stacks 0781 part (1) are carried as the named hypotheses hclosed, hwp, hsep”.

> **Stacks 077A: the higher direct images `R^i f_{QCoh,*}`.**  The composite defining
> `f_{QCoh,*}` with the `i`-th higher direct image of modules in its middle slot.

```lean
def higherDirectImageQuasicoherent (i : ℕ) :
    FibredSite.quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u, u + 1} B S hS q hq
```

**`AlgebraicGeometry.Stack.quasicoherentPullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L378). The attribute's comment: “the assertion: the inverse image of quasi-coherent modules is left adjoint to f\_\{QCoh,*}; the coherator's three inputs from Stacks 0781 part (1) are carried as the named hypotheses hclosed, hwp, hsep”.

> **Stacks 077A, the assertion itself: `f^*` on quasi-coherent modules has the right adjoint
> `f_{QCoh,*}`.**
>
> The adjunction `f^* ⊣ f_*` of **Stacks 06WE** composed with the coherator adjunction of
> **Stacks 0781** part (2) is an adjunction between `QCoh(𝒪_𝒴)` and all of `Mod(𝒪_𝒳)`; restricting
> it along the fully faithful inclusion of `QCoh(𝒪_𝒳)`, which is possible because `f^*` preserves
> quasi-coherence by **Stacks 06WH**, is the asserted adjunction.

```lean
def quasicoherentPullbackPushforwardAdjunction :
    quasicoherentModulePullback B S hS p q hp hq f hf ⊣
      quasicoherentPushforward B S hS p q hp hq f hf hclosed hwp hsep
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.fppfQuasicoherentPushforward`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L440). The attribute's comment: “g\_\{QCoh,*} for a 1-morphism of algebraic stacks over S; the coherator's three inputs from Stacks 0781 part (1) are carried as the named hypotheses hclosed, hwp, hsep”.

> **Stacks 077A for a 1-morphism of algebraic stacks: the quasi-coherent direct image
> `g_{QCoh,*} : QCoh(𝒪_𝒳) ⥤ QCoh(𝒪_𝒴)`.**

```lean
abbrev fppfQuasicoherentPushforward :
    fppfQuasicoherentModules B S hS 𝒳 ⥤ fppfQuasicoherentModules B S hS 𝒴
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.fppfHigherDirectImageQuasicoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L452). The attribute's comment: “R^i g\_\{QCoh,*} for a 1-morphism of algebraic stacks over S; the coherator's three inputs from Stacks 0781 part (1) are carried as the named hypotheses hclosed, hwp, hsep”.

> **Stacks 077A for a 1-morphism of algebraic stacks: the higher direct images
> `R^i g_{QCoh,*} : QCoh(𝒪_𝒳) ⥤ QCoh(𝒪_𝒴)`.**  This is the higher direct image of modules on the
> fppf sites, the `Rⁱf_*` of **Stacks 0770**, read in `QCoh(𝒪_𝒴)` rather than in all of
> `Mod(𝒪_𝒴)`.

```lean
abbrev fppfHigherDirectImageQuasicoherent (i : ℕ) :
    fppfQuasicoherentModules B S hS 𝒳 ⥤ fppfQuasicoherentModules B S hS 𝒴
```

## Tag 0GQQ, a lemma

[Tag 0GQQ](https://stacks.math.columbia.edu/tag/0GQQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_app_quasicoherentDirectImageOfEtale_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageFlatObject.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageFlatObject.lean#L221). The attribute's comment: “the canonical comparison, namely the counit of Stacks 0778, is invertible on sections over a flat object: both (f\_*F)(y) = (f\_\{QCoh,*}F)(y) and (R^i f\_*F)(y) = (R^i f\_\{QCoh,*}F)(y), never an unspecified isomorphism. Carried: the middle étale direct image of Stacks 077A on LQCoh^fbc, as data D exactly as in 0GQX; and hker, hcoker, which are Stacks 0779 part (2), its library form needing Stacks 0771 part (2) to reach this reading”.

> **Stacks 0GQQ.**  Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks over `S`, let `y` be a flat object of `𝒴` and let `ℱ` be an object of
> `QCoh(𝒪_𝒳)`.  Then the canonical comparison from the sections at `y` of the quasi-coherent direct
> image of **Stacks 077A** to the sections at `y` of the étale direct image is invertible:
>
> `(f_*ℱ)(y) = (f_{QCoh,*}ℱ)(y)` and `(R^i f_*ℱ)(y) = (R^i f_{QCoh,*}ℱ)(y)`.
>
> The comparison is the component at `y` of the counit `ε : i Q(𝓖) ⟶ 𝓖` of the adjunction of
> **Stacks 0778** at `𝓖 = D(i ℱ)`, whose domain is `i` of the composite of **Stacks 077A** by
> `AlgebraicGeometry.Stack.quasicoherentToFlatBaseChange_quasicoherentDirectImageOfEtale_obj`.
> Both halves of the source are covered at once: `D` is the étale direct image for the first and
> its `i`-th right derived functor for the second.
>
> The hypotheses `hker` and `hcoker` are **Stacks 0779** part (2) read at the presheaf level; see
> "Carried versus proved" in the module documentation for why the library's part (2) does not
> discharge them.  Everything else is proved, by
> `AlgebraicGeometry.Stack.isIso_app_of_isParasitic`.  The two hypotheses on `f` are named `_hqc`
> and `_hqs` because the argument does not consume them: they are the source's, and they stand
> behind the carried data `D`.

```lean
theorem isIso_app_quasicoherentDirectImageOfEtale_counit
    (_hqc : IsQuasiCompactMorphism B S hS f)
    (_hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (D : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS
        (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
        (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) ⥤
      locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS 𝒴.val.val.p
        𝒴.val.isFiberedInGroupoids)
    (F : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom))
    (hker : IsParasitic B S hS 𝒴 .etale
      (kernel ((flatBaseChangeQuasicoheratorAdjunction B E h S hS 𝒴.val.val.p
        𝒴.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).counit.app
          (D.obj ((quasicoherentToFlatBaseChange B E h S hS
            (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
            (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) hincX).obj F))).hom.val))
    (hcoker : IsParasitic B S hS 𝒴 .etale
      (cokernel ((flatBaseChangeQuasicoheratorAdjunction B E h S hS 𝒴.val.val.p
        𝒴.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).counit.app
          (D.obj ((quasicoherentToFlatBaseChange B E h S hS
            (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
            (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) hincX).obj F))).hom.val))
    (y : 𝒴.val.val.obj) (hy : flatObject B S hS 𝒴.val y) :
    IsIso (((flatBaseChangeQuasicoheratorAdjunction B E h S hS 𝒴.val.val.p
      𝒴.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).counit.app
        (D.obj ((quasicoherentToFlatBaseChange B E h S hS
          (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
          (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) hincX).obj F))).hom.val.app
            (op y))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.bijective_coheratorAdjunction_counit_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHigherDirectImageDeltaFunctor.lean#L205). The attribute's comment: “(f\_*F)(y) = (f\_\{QCoh,*}F)(y) and (R^i f\_*F)(y) = (R^i f\_\{QCoh,*}F)(y) for f qcqs, y flat and F quasi-coherent: the adjunction maps of the coherator are bijective at y; i ≥ 0, both sides vanishing for i < 0”.

> **Stacks 0GQQ.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks, `y` an object of `𝒴` such that `y : V → 𝒴` is flat, and `𝓕` a quasi-coherent
> `𝒪_𝒳`-module.  Then `(f_*𝓕)(y) = (f_{QCoh,*}𝓕)(y)` and `(Rⁱf_*𝓕)(y) = (Rⁱf_{QCoh,*}𝓕)(y)` for
> all `i`: the adjunction maps `f_{QCoh,*}𝓕 = Q(f_*𝓕) ⟶ f_*𝓕` and
> `Rⁱf_{QCoh,*}𝓕 = Q(Rⁱf_*𝓕) ⟶ Rⁱf_*𝓕` of the coherator are bijective on sections at `y`.  Both
> `f_*𝓕` and `Rⁱf_*𝓕` lie in `LQCoh^fbc(𝒪_𝒴)`, so the kernels and cokernels of those maps are
> parasitic by **Stacks 0779** part (2), and vanish at `y`.  For `i < 0` both sides are zero.

```lean
theorem bijective_coheratorAdjunction_counit_directImage (F : quasicoherentModules B S hS 𝒳)
    (y : 𝒴.val.val.obj) (hy : flatObject B S hS 𝒴.val y) :
    Function.Bijective (((coheratorAdjunction B S hS 𝒴).counit.app
        ((fppfModulesPushforward B S hS f).obj ((quasicoherentInclusion B S hS 𝒳).obj F))).val.app
          (op y)) ∧
      ∀ i, Function.Bijective (((coheratorAdjunction B S hS 𝒴).counit.app
        ((fppfModulesHigherDirectImage B S hS f i).obj
          ((quasicoherentInclusion B S hS 𝒳).obj F))).val.app (op y))
```

## Tag 0GQR, a remark

[Tag 0GQR](https://stacks.math.columbia.edu/tag/0GQR) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.directImageNaiveCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean#L250). The attribute's comment: “the vertical arrow c on the right, the naive relative cup product in degree 0”.

> **The naive relative cup product in degree `0`** (Stacks 0FPJ), the right vertical arrow `c`
> of Stacks 0GQR: `f_*𝓕 ⊗ f_*𝓖 ⟶ f_*(𝓕 ⊗ 𝓖)`, adjoint to the comparison of Stacks 03EL
> followed by the counit of `f^* ⊣ f_*` in each factor. It is
> `Stacks.Cohomology.DegreeZeroCupProduct.naiveRelativeCupProduct` at this morphism of ringed
> topoi.

```lean
def directImageNaiveCupProduct (M N : quasicoherentModules.{u, u + 1, u, u} B S hS p hp) :
    (fppfSheafTensor B S hS q hq).obj
        ((fppfPushforwardModules B S hS p q hp hq F hF).obj
            ((quasicoherentModulesInclusion B S hS p hp).obj M),
          (fppfPushforwardModules B S hS p q hp hq F hF).obj
            ((quasicoherentModulesInclusion B S hS p hp).obj N)) ⟶
      (fppfPushforwardModules B S hS p q hp hq F hF).obj
        ((quasicoherentModulesInclusion B S hS p hp).obj
          ((quasicoherentSheafTensor B S hS p hp).obj (M, N)))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean#L336). The attribute's comment: “the left vertical arrow, Q applied to c through the comparison of Remark 0GQM”.

> **The left vertical arrow of Stacks 0GQR**,
> `f_{QCoh,*}𝓕 ⊗ f_{QCoh,*}𝓖 ⟶ f_{QCoh,*}(𝓕 ⊗ 𝓖)`, for a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks: `Q(c)` precomposed with the comparison `Q(A) ⊗ Q(B) ⟶ Q(A ⊗ B)` of Remark 0GQM
> (`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentCupProduct_eq`). Here
> `f_{QCoh,*} = Q ∘ f_* ∘ i`, with `f_*` the direct image of the morphism of ringed topoi `f`
> induces and `Q` the coherator `AlgebraicGeometry.Stack.AlgebraicStacks.coherator` of `𝒴`.

```lean
def quasicoherentCupProduct (𝓕 𝓖 : quasicoherentModules B S hS 𝒳) :
    (tensorQ𝒴).obj ((Q𝒴).obj ((fStar).obj ((i𝒳).obj 𝓕)), (Q𝒴).obj ((fStar).obj ((i𝒳).obj 𝓖))) ⟶
      (Q𝒴).obj ((fStar).obj ((i𝒳).obj ((tensorQ𝒳).obj (𝓕, 𝓖))))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.map_quasicoherentCupProduct_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean#L396). The attribute's comment: “commutativity of the diagram, for a quasi-compact quasi-separated 1-morphism of algebraic stacks”.

> **Stacks 0GQR.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks and let `𝓕`, `𝓖` be quasi-coherent `𝒪_𝒳`-modules. The square
>
> ```
> f_{QCoh,*}𝓕 ⊗ f_{QCoh,*}𝓖 ───→ f_*𝓕 ⊗ f_*𝓖
>         │                              │ c
>         ↓                              ↓
> f_{QCoh,*}(𝓕 ⊗ 𝓖) ─────────→ f_*(𝓕 ⊗ 𝓖)
> ```
>
> commutes: the left vertical arrow
> (`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentCupProduct`, the comparison of
> Remark 0GQM followed by `Q(c)`) followed by the counit `Q ⟶ id` at `f_*(𝓕 ⊗ 𝓖)` equals the top
> arrow (`i` commuting with `⊗`, then the counit at `f_*𝓕` and at `f_*𝓖`) followed by the naive
> relative cup product `c` (`AlgebraicGeometry.FibredSite.directImageNaiveCupProduct`). `f_*` is
> the direct image along the morphism of ringed topoi `f` induces, and `Q` is the coherator
> `AlgebraicGeometry.Stack.AlgebraicStacks.coherator` of `𝒴`, which takes no input.

```lean
theorem map_quasicoherentCupProduct_comp_counit
    (_hqc : IsQuasiCompactMorphism B S hS f) (_hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (𝓕 𝓖 : quasicoherentModules B S hS 𝒳) :
    (i𝒴).map (quasicoherentCupProduct B S hS f 𝓕 𝓖) ≫
        (adjQ).counit.app ((fStar).obj ((i𝒳).obj ((tensorQ𝒳).obj (𝓕, 𝓖)))) =
      (tensorIso𝒴).hom.app ((Q𝒴).obj ((fStar).obj ((i𝒳).obj 𝓕)),
          (Q𝒴).obj ((fStar).obj ((i𝒳).obj 𝓖))) ≫
        (tensor𝒴).map ((adjQ).counit.app ((fStar).obj ((i𝒳).obj 𝓕)) ×ₘ
          (adjQ).counit.app ((fStar).obj ((i𝒳).obj 𝓖))) ≫
        cupC 𝓕 𝓖
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentCupProduct_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean#L413). The attribute's comment: “the construction is functorial in F and G: the left vertical arrow”.

> **Stacks 0GQR, functoriality of the left vertical arrow** in `𝓕` and `𝓖`, for a
> quasi-compact quasi-separated 1-morphism of algebraic stacks.

```lean
theorem quasicoherentCupProduct_natural
    (_hqc : IsQuasiCompactMorphism B S hS f) (_hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    {𝓕 𝓕' 𝓖 𝓖' : quasicoherentModules B S hS 𝒳} (a : 𝓕 ⟶ 𝓕') (b : 𝓖 ⟶ 𝓖') :
    (tensorQ𝒴).map ((fQCoh).map a ×ₘ (fQCoh).map b) ≫ quasicoherentCupProduct B S hS f 𝓕' 𝓖' =
      quasicoherentCupProduct B S hS f 𝓕 𝓖 ≫ (fQCoh).map ((tensorQ𝒳).map (a ×ₘ b))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentNaiveCupProduct_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageCupProduct.lean#L428). The attribute's comment: “the construction is functorial in F and G: the arrow c”.

> **Stacks 0GQR, functoriality of the naive relative cup product `c`** in `𝓕` and `𝓖`, for a
> quasi-compact quasi-separated 1-morphism of algebraic stacks.

```lean
theorem quasicoherentNaiveCupProduct_natural
    (_hqc : IsQuasiCompactMorphism B S hS f) (_hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    {𝓕 𝓕' 𝓖 𝓖' : quasicoherentModules B S hS 𝒳} (a : 𝓕 ⟶ 𝓕') (b : 𝓖 ⟶ 𝓖') :
    (tensor𝒴).map ((fStar).map ((i𝒳).map a) ×ₘ (fStar).map ((i𝒳).map b)) ≫ cupC 𝓕' 𝓖' =
      cupC 𝓕 𝓖 ≫ (fStar).map ((i𝒳).map ((tensorQ𝒳).map (a ×ₘ b)))
```

**`Stacks.Cohomology.DegreeZeroCupProduct.naiveRelativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean#L140). The attribute's comment: “the vertical arrow c on the right, for a morphism of ringed topoi”.

> **The naive relative cup product in degree zero**, the map
> `f_*F ⊗_{O_D} f_*G ⟶ f_*(F ⊗_{O_C} G)` adjoint to the comparison of Tag 03EL followed by the
> counit of `f^* ⊣ f_*` in each tensor factor.

```lean
def naiveRelativeCupProduct
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (Functor.uncurry.obj (sheafTensor.{u', v', w', w', w'} Y.O)).obj
          ((pushforwardModules f).obj F, (pushforwardModules f).obj G) ⟶
      (pushforwardModules f).obj
        ((Functor.uncurry.obj (sheafTensor.{u, v, w, w, w} X.O)).obj (F, G))
```

**`Stacks.Cohomology.DegreeZeroCupProduct.quasicoherentRelativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean#L180). The attribute's comment: “the left vertical arrow, over an adjunction with a tensor comparison”.

> The naive relative cup product in degree zero carried through the comparison attached to the
> adjunction `adj : i ⊣ Q` and the tensor comparison `α`: the canonical map
> `A(Q(f_*F), Q(f_*G)) ⟶ Q(f_*F ⊗ f_*G)` followed by `Q` applied to `c`.

```lean
def quasicoherentRelativeCupProduct
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    A.obj (Q.obj ((pushforwardModules f).obj F), Q.obj ((pushforwardModules f).obj G)) ⟶
      Q.obj ((pushforwardModules f).obj
        ((Functor.uncurry.obj (sheafTensor.{u, v, w, w, w} X.O)).obj (F, G)))
```

**`Stacks.Cohomology.DegreeZeroCupProduct.map_quasicoherentRelativeCupProduct_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean#L192). The attribute's comment: “commutativity of the diagram, over an adjunction with a tensor comparison”.

> **The square commutes.**  Going right along the upper horizontal
> arrow — the comparison `α` followed by the counit of `adj` in each tensor factor — and then down
> `c` agrees with going down the left vertical arrow and then right along the counit of `adj`.

```lean
theorem map_quasicoherentRelativeCupProduct_comp_counit
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    i.map (quasicoherentRelativeCupProduct f adj A α F G) ≫
        adj.counit.app ((pushforwardModules f).obj
          (((sheafTensor.{u, v, w, w, w} X.O).obj F).obj G)) =
      α.app (Q.obj ((pushforwardModules f).obj F), Q.obj ((pushforwardModules f).obj G)) ≫
        (Functor.uncurry.obj (sheafTensor.{u', v', w', w', w'} Y.O)).map
            (adj.counit.app ((pushforwardModules f).obj F) ×ₘ
              adj.counit.app ((pushforwardModules f).obj G)) ≫
          naiveRelativeCupProduct f F G
```

**`Stacks.Cohomology.DegreeZeroCupProduct.quasicoherentRelativeCupProduct_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/DegreeZeroCupProductAndCoherator.lean#L207). The attribute's comment: “functoriality in the two modules, over an adjunction with a tensor comparison”.

> **The construction is functorial in the two modules.**

```lean
theorem quasicoherentRelativeCupProduct_natural
    {F F' G G' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)}
    (u : F ⟶ F') (v : G ⟶ G') :
    A.map (Q.map ((pushforwardModules f).map u) ×ₘ Q.map ((pushforwardModules f).map v)) ≫
        quasicoherentRelativeCupProduct f adj A α F' G' =
      quasicoherentRelativeCupProduct f adj A α F G ≫
        Q.map ((pushforwardModules f).map
          ((Functor.uncurry.obj (sheafTensor.{u, v, w, w, w} X.O)).map (u ×ₘ v)))
```

## Tag 0782, a lemma

[Tag 0782](https://stacks.math.columbia.edu/tag/0782) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_quasicoherentLeraySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentLeraySpectralSequence.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentLeraySpectralSequence.lean#L83). The attribute's comment: “the whole statement, with modules at the module universe u of the schemes; cohomology the right derived functors of Hom(𝒪, -), valued in AddCommGrpCat.\{u + 1}”.

> **Stacks 0782.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks and `ℱ` a quasi-coherent `𝒪_𝒳`-module.  There is a spectral sequence with
> `E_2^{p,q} = H^p(𝒴, R^q f_{QCoh,*} ℱ)` converging to `H^{p+q}(𝒳, ℱ)`.
>
> The second page is identified for `p, q ≥ 0`, vanishes outside the first quadrant, and the
> sequence abuts to `H^n(𝒳, ℱ)`.  Here `R^q f_{QCoh,*}` is
> `AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImage` (**Stacks 077A**), and
> `H^p` is the right derived functor of `Hom(𝒪, -)` on modules at the universe `u` of the schemes,
> with values in `AddCommGrpCat.{u + 1}`.

```lean
theorem exists_quasicoherentLeraySpectralSequence
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : quasicoherentModules B S hS 𝒳) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 0,
      (∀ p q : ℕ, Nonempty ((E.page 2 zero_le_two).X ((p : ℤ), (q : ℤ)) ≅
        ((preadditiveCoyoneda.obj (Opposite.op (SheafOfModules.unit _))).rightDerivedPlus
          (p : ℤ)).obj ((quasicoherentInclusion B S hS 𝒴).obj
            ((quasicoherentHigherDirectImage B S hS f q).obj F)))) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page 2 zero_le_two).X (p, q))) ∧
      SpectralSequence.AbutsTo E (fun n =>
        ((preadditiveCoyoneda.obj (Opposite.op (SheafOfModules.unit _))).rightDerivedPlus n).obj
          ((quasicoherentInclusion B S hS 𝒳).obj F))
```

**`Stacks.Cohomology.Leray.exists_quasicoherentLeraySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CoheratorLeraySpectralSequence.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CoheratorLeraySpectralSequence.lean#L348). The attribute's comment: “the spectral sequence H^p(𝒴, R^q f\_\{QCoh,*} ℱ) ⟹ H^\{p+q}(𝒳, ℱ), read in abelian groups FOR A MORPHISM OF RINGED TOPOI, NOT for a morphism of algebraic stacks as the source states it. This is NOT a generalization of the tag: it does not instantiate to the source's setting, because the Leray sequence of 0732 here lives at RingedTopos.\{u, u, u} while the ringed topos of an algebraic stack is RingedTopos.\{u, u+1, u}, so the two cannot be matched up; the three universe blockers are set out in this module's docstring. The tag's own statement, over algebraic stacks, therefore remains undelivered. Further carried here: the coherator Q of 0778, as a coreflection, and the two lemmas the proof cites — 0779 part (2), that the kernel and cokernel of Q 𝓖 ⟶ 𝓖 are parasitic, and 0775 part (1), that a parasitic module has vanishing cohomology — as the hypotheses `hker`, `hcoker` and `hvanish`. 077A, which builds f\_\{QCoh,*} and is where quasi-compactness and quasi-separatedness enter, is not proved and is absent from the library: only its definition R^q f\_\{QCoh,*} = Q ∘ R^q f\_* is reproduced”. References: SGA 4 V (5.3), “more general”; SGA 4 V (5.4), “special case”.

> **Stacks 0782, the Leray spectral sequence for the quasi-coherent direct image**, read in
> abelian groups.  Let `f : (Sh(C), 𝒪_C) → (Sh(D), 𝒪_D)` be a morphism of ringed topoi standing
> for a quasi-compact quasi-separated morphism `f : 𝒳 → 𝒴` of algebraic stacks, and let `K` be a
> bounded below complex of `𝒪_C`-modules, standing for the quasi-coherent module `ℱ` placed in
> degree zero.  Suppose given
>
> * a coreflection `incl ⊣ coherator` of `Mod(𝒪_D)` onto a category `𝒬`: this is the coherator
>   of **Stacks 0778**, `Q : LQCoh^fbc(𝒪_𝒴) ⥤ QCoh(𝒪_𝒴)`, with its adjunction, whose counit
>   `Q 𝓖 ⟶ 𝓖` is the adjunction map the source's proof uses;
> * a class `Parasitic` of modules on `D`: the parasitic modules of **Stacks 0773**;
> * `hker` and `hcoker`: the kernel and the cokernel of the counit are parasitic, which is
>   **Stacks 0779** part (2);
> * `hvanish`: a parasitic module has vanishing cohomology, which is **Stacks 0775** part (1).
>
> Then there is a spectral sequence with
>
> `E_2^{p,q} = H^p(𝒴, R^q f_{QCoh,*} ℱ)`
>
> converging to `H^{p+q}(𝒳, ℱ)`, where `R^q f_{QCoh,*}` is
> `Stacks.Cohomology.Leray.quasicoherentHigherDirectImage`, the composite of **Stacks 077A**.
>
> The spectral sequence is the one of **Stacks 0732**,
> `Stacks.Cohomology.Leray.exists_leraySpectralSequence`, and its abutment clause is that
> theorem's abutment clause unchanged.  What is added is the identification of its second page:
> `Stacks.Cohomology.isIso_rightDerivedPlus_map_of_isZero_kernel_cokernel` turns the counit
> `Q(R^q f_* ℱ) ⟶ R^q f_* ℱ`, whose kernel and cokernel are acyclic by `hker`, `hcoker` and
> `hvanish`, into an isomorphism `H^p(𝒴, Q(R^q f_* ℱ)) ≅ H^p(𝒴, R^q f_* ℱ)` in every degree.
> That is precisely the step the source performs and calls formal.
>
> See the module documentation for why the coherator and the two cited lemmas are carried as
> hypotheses rather than instantiated: the Leray spectral sequence of this development is
> available only at `RingedTopos.{u, u, u}`, while the ringed topos of an algebraic stack has
> its site one universe up, and the coherator, the higher direct images and the cohomology of an
> algebraic stack are formalized over three mutually incomparable categories of modules.

```lean
theorem exists_quasicoherentLeraySpectralSequence {𝒬 : Type u₁} [Category.{v₁} 𝒬]
    (incl : 𝒬 ⥤ SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (coherator : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⥤ 𝒬) (adj : incl ⊣ coherator)
    (Parasitic : ObjectProperty (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hvanish : ∀ P : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O), Parasitic P → ∀ p : ℕ,
      IsZero (((globalSectionsAb Y).rightDerivedPlus (p : ℤ)).obj P))
    (hker : ∀ M : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      Parasitic (kernel (adj.counit.app M)))
    (hcoker : ∀ M : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      Parasitic (cokernel (adj.counit.app M)))
    (K : DerivedCategory.Plus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        ((globalSectionsAb Y).rightDerivedPlus p).obj
          (incl.obj ((quasicoherentHigherDirectImage f coherator q).obj K)))) ∧
      SpectralSequence.AbutsTo E (fun n =>
        (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u} n).obj
          ((globalSectionsAb X).rightDerivedFunctorPlus.obj K))
```

## Tag 0783, a lemma

[Tag 0783](https://stacks.math.columbia.edu/tag/0783) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_quasicoherentRelativeLeraySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentRelativeLeraySpectralSequence.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentRelativeLeraySpectralSequence.lean#L271). The attribute's comment: “the spectral sequence E\_2^\{p,q} = R^p g\_\{QCoh,*}(R^q f\_\{QCoh,*} F) converging to R^\{p+q}(g ∘ f)\_\{QCoh,*} F for qcqs morphisms of algebraic stacks, modules at the universe u of the schemes”.

> **Stacks 0783: the relative Leray spectral sequence for the quasi-coherent direct image.**
> Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be quasi-compact and quasi-separated 1-morphisms of algebraic
> stacks and let `ℱ` be a quasi-coherent `𝒪_𝒳`-module. There is a spectral sequence of
> quasi-coherent `𝒪_𝒵`-modules, from its second page on, with
>
> `E_2^{p,q} = R^p g_{QCoh,*}(R^q f_{QCoh,*} ℱ)`
>
> (zero outside the first quadrant) converging to `R^{p+q}(g ∘ f)_{QCoh,*} ℱ`: it abuts to
> `n ↦ R^n(g ∘ f)_{QCoh,*} ℱ`, zero in negative degrees. Here `R^i (-)_{QCoh,*}` is
> `AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHigherDirectImage`, the composite
> `Q ∘ R^i(-)_* ∘ i` of **Stacks 077A**, and `QCoh(𝒪_𝒵)` carries its abelian structure
> `AlgebraicGeometry.Stack.AlgebraicStacks.instAbelianQuasicoherentModules`; modules have sections
> in the universe `u` of the schemes.
>
> The proof is the source's: the Grothendieck spectral sequence of `(g ∘ f)_* = g_* ∘ f_*` on fppf
> modules (Stacks 0734 for stacks), pushed along the coherator `Q_𝒵`, which is exact on
> `LQCoh^fbc(𝒪_𝒵)` (Stacks 0779 (3)) where all of its terms lie from the second page on
> (Stacks 0771 (2), (4)(b)); the second page is identified through the counit
> `Q_𝒴(R^q f_*ℱ) ⟶ R^q f_*ℱ`, whose kernel and cokernel are parasitic (Stacks 0779 (1)), hence
> carried by `R^p g_*` to parasitic modules (Stacks 0775 (2)) which `Q_𝒵` kills.

```lean
theorem exists_quasicoherentRelativeLeraySpectralSequence
    (hfqc : IsQuasiCompactMorphism B S hS f) (hfqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (hgqc : IsQuasiCompactMorphism B S hS g) (hgqs : AlgebraicStacks.IsQuasiSeparated B S hS g)
    (ℱ : quasicoherentModules B S hS 𝒳) :
    ∃ E : CohomologicalSpectralSequence (quasicoherentModules B S hS 𝒵) 2,
      (∀ p q : ℕ, Nonempty ((E.page 2 le_rfl).X ((p : ℤ), (q : ℤ)) ≅
        (quasicoherentHigherDirectImage B S hS g p).obj
          ((quasicoherentHigherDirectImage B S hS f q).obj ℱ))) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page 2 le_rfl).X (p, q))) ∧
      SpectralSequence.AbutsTo E (extendNatByZero fun n =>
        (quasicoherentHigherDirectImage B S hS (f ≫ g) n).obj ℱ)
```

**`Stacks.Cohomology.Leray.exists_quasicoherentRelativeLeraySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CoheratorRelativeLeraySpectralSequence.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CoheratorRelativeLeraySpectralSequence.lean#L337). The attribute's comment: “the E₂ page R^p g\_\{QCoh,*}(R^q f\_\{QCoh,*} ℱ) and convergence, FOR RINGED TOPOI, not algebraic stacks, hence NOT a generalization: 0734 is proved at RingedTopos.\{u,u,u}, a stack's is \{u,u+1,u}. Carried: the 0778 coherators, 0779(3)(2)(1) and 0775(2), the last absent here; 077A is absent too, only its recipe Q ∘ R^i(-)\_* ∘ i is reused. See the module docstring”. References: EGA 0 (12.2.4), “more general”; SGA 2 VIII (3.1), “more general”; SGA 4 V (5.3), “more general”; SGA 4 V (5.4), “more general”; SGA 4½ Arcata (2.3.3), “more general”.

> **Stacks 0783, the relative Leray spectral sequence for the quasi-coherent direct image.**
> Let `f : (Sh(C), 𝒪_C) → (Sh(D), 𝒪_D)` and `g : (Sh(D), 𝒪_D) → (Sh(E), 𝒪_E)` be morphisms of
> ringed topoi standing for quasi-compact quasi-separated morphisms `f : 𝒳 → 𝒴` and `g : 𝒴 → 𝒵` of
> algebraic stacks, with `g ∘ f` presented as their composite by a comparison `τ` of the geometric
> direct images, and let `K` be a bounded below complex of `𝒪_C`-modules, standing for the
> quasi-coherent sheaf `ℱ` placed in degree zero.  Suppose given
>
> * a coreflection `inclY ⊣ coheratorY` of `Mod(𝒪_D)` onto a category `𝒬_Y`: this is the coherator
>   of **Stacks 0778**, `Q_𝒴 : LQCoh^fbc(𝒪_𝒴) ⥤ QCoh(𝒪_𝒴)`, with its adjunction, whose counit
>   `Q_𝒴 𝓖 ⟶ 𝓖` is the adjunction map the source's proof uses;
> * an exact functor `coheratorZ` from `Mod(𝒪_E)` to a category `𝒬_Z`: the coherator of
>   **Stacks 0778** on `𝒵`, exact by **Stacks 0779** part (3), which is the functor the source
>   applies to the whole spectral sequence;
> * a class `Parasitic` of modules on `D`: the parasitic modules of **Stacks 0773**;
> * `hker` and `hcoker`: the kernel and the cokernel of the counit are parasitic, which is
>   **Stacks 0779** part (2);
> * `hvanish`: `Q_𝒵 ∘ R^p g_*` kills a parasitic module, which is **Stacks 0775** part (2)
>   followed by **Stacks 0779** part (1).
>
> Then there is a spectral sequence with
>
> `E_2^{p,q} = R^p g_{QCoh,*}(R^q f_{QCoh,*} ℱ)`
>
> converging to `R^{p+q}(g ∘ f)_{QCoh,*} ℱ`, where the two quasi-coherent higher direct images are
> `Stacks.Cohomology.Leray.quasicoherentRelativeHigherDirectImage` and
> `Stacks.Cohomology.Leray.quasicoherentHigherDirectImage`, the composites of **Stacks 077A**, and
> the abutment is `Q_𝒵` applied to `R^{p+q}(g ∘ f)_*ℱ`, which is the same composite in degree
> `p + q`.
>
> See the module documentation for why the coherators and the cited lemmas are carried as
> hypotheses rather than instantiated.

```lean
theorem exists_quasicoherentRelativeLeraySpectralSequence {𝒬Y : Type u₁} [Category.{v₁} 𝒬Y]
    {𝒬Z : Type u₂} [Category.{v₂} 𝒬Z] [Abelian 𝒬Z]
    (inclY : 𝒬Y ⥤ SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (coheratorY : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⥤ 𝒬Y)
    (adjY : inclY ⊣ coheratorY)
    (coheratorZ : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Z.O) ⥤ 𝒬Z)
    [coheratorZ.Additive] [coheratorZ.PreservesHomology] [coheratorZ.PreservesMonomorphisms]
    (Parasitic : ObjectProperty (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hvanish : ∀ P : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      Parasitic P → ∀ p : ℕ,
        IsZero (coheratorZ.obj (((pushforwardModules g).rightDerivedPlus (p : ℤ)).obj P)))
    (hker : ∀ M : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      Parasitic (kernel (adjY.counit.app M)))
    (hcoker : ∀ M : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      Parasitic (cokernel (adjY.counit.app M)))
    (K : DerivedCategory.Plus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ∃ E : CohomologicalSpectralSequence 𝒬Z 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        (quasicoherentRelativeHigherDirectImage g inclY coheratorZ p).obj
          ((quasicoherentHigherDirectImage f coheratorY q).obj K))) ∧
      SpectralSequence.AbutsTo E (fun n => coheratorZ.obj
        ((DerivedCategory.Plus.homologyFunctor
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Z.O)) n).obj
            ((pushforwardModules gf).rightDerivedFunctorPlus.obj K)))
```

## Tag 0784, a proposition

[Tag 0784](https://stacks.math.columbia.edu/tag/0784) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfSpectralSequenceData_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatCoveringSpectralSequence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatCoveringSpectralSequence.lean#L123). The attribute's comment: “the E₁ form, which is what Sheaves on Stacks 06XJ gives and what makes the first differential the Čech differential; the tag's own text writes E₂. Stated for an arbitrary sheaf of modules rather than only a quasi-coherent one. Carries the hypothesis that `𝒰` has equalizers, as Tag 06XJ does”.

> **Stacks 0784.** Let `f : 𝒰 ⟶ 𝒳` be a `1`-morphism of algebraic stacks which is
> representable by algebraic spaces, surjective, flat and locally of finite presentation, and let
> `F` be a sheaf of `𝒪_𝒳`-modules. Then there is a first-quadrant spectral sequence
> `E₁^{p,q} = H^q_fppf(𝒰ₚ, fₚ^*F) ⇒ H^{p+q}_fppf(𝒳, F)`, where `𝒰ₚ` is the degree `p` term of the
> relative Čech nerve of `f` and `fₚ` its projection to `𝒳`; the identification of the first page
> is `AlgebraicGeometry.Stack.AlgebraicStacks.pageOneIsoModule`.
>
> The source assumes `F` quasi-coherent; the spectral sequence needs no such hypothesis, so it is
> stated here for an arbitrary sheaf of `𝒪_𝒳`-modules, which contains the source's statement.
> No hypothesis that `𝒰` has equalizers is needed.

```lean
theorem exists_fppfSpectralSequenceData_module
    (F : SheafOfModules.{max (u + 1) a} (FibredSite.ringStructureSheafCore B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids SiteKind.fppf)) :
    Nonempty (Stacks.RelativeCech.SpectralSequenceData B S hS 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) SiteKind.fppf
      (fppfAbelianSheaf B S hS F))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.pageOneIsoModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatCoveringSpectralSequence.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatCoveringSpectralSequence.lean#L136). The attribute's comment: “the reading of the E₁ page as the cohomology of the inverse image of the module”.

> **Stacks 0784**, the first page. The term of the spectral sequence of a flat presentation in
> position `(p, q)` is the degree `q` fppf cohomology, on the degree `p` term `𝒰ₚ` of the relative
> Čech nerve, of the inverse image `fₚ^*F` of the module `F`.

```lean
def pageOneIsoModule
    (F : SheafOfModules.{max (u + 1) a} (FibredSite.ringStructureSheafCore B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids SiteKind.fppf))
    (data : Stacks.RelativeCech.SpectralSequenceData B S hS 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) SiteKind.fppf
      (fppfAbelianSheaf B S hS F)) (i j : ℕ) :
    letI := data.continuous i
    (data.sequence.page 1).X ((i : ℤ), (j : ℤ)) ≅
      (Sheaf.functorH (BigFppfOver.associatedTopology B S hS
        (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom) i ⋙ 𝒳.val.val.p) SiteKind.fppf) j).obj
        ((SheafOfModules.toSheaf _).obj
          ((SheafOfModules.restrictAlongContinuous
            (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
              (CatFiberedInGroupoids.homFunctor f.hom) i)
            (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
              𝒳.val.isFiberedInGroupoids SiteKind.fppf)).obj F))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfModuleCechSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatPresentationModuleCohomology.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatPresentationModuleCohomology.lean#L79). The attribute's comment: “for an arbitrary sheaf of modules, which contains the quasi-coherent case; the equalizers of `𝒰` needed by Tag 06XJ are Tag 06WY (3), proved for algebraic stacks”.

> Let `f : 𝒰 ⟶ 𝒳` be a `1`-morphism of algebraic stacks which is representable by algebraic
> spaces, surjective, flat and locally of finite presentation, and let `F` be a sheaf of
> `𝒪_𝒳`-modules (for instance a quasi-coherent one). Then there is a first-quadrant spectral sequence
> `E₁^{p,q} = H^q(𝒰ₚ, fₚ^*F) ⇒ H^{p+q}(𝒳, F)`, where `𝒰ₚ = 𝒰 ×_𝒳 ⋯ ×_𝒳 𝒰` (`p + 1` factors) is the
> degree `p` term of the relative Čech nerve of `f` and `fₚ : 𝒰ₚ ⟶ 𝒳` its projection.
>
> The spectral sequence, its first-quadrant vanishing and its convergence to the cohomology of `F` on
> `𝒳` are the fields of `Stacks.RelativeCech.SpectralSequenceData` for the abelian sheaf underlying
> `F`; the condition on that datum identifies its `E₁` term at `(p, q)` with the degree `q`
> cohomology of the inverse image `fₚ^*F` of the module `F` on `𝒰ₚ`.

```lean
theorem exists_fppfModuleCechSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hflat : IsFlat B S hS f)
    (hlfp : IsLocallyOfFinitePresentation B S hS f)
    (F : SheafOfModules.{max (u + 1) a} (FibredSite.ringStructureSheafCore B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids SiteKind.fppf)) :
    ∃ data : Stacks.RelativeCech.SpectralSequenceData B S hS 𝒳.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) SiteKind.fppf
        ((SheafOfModules.toSheaf _).obj F),
      ∀ p q : ℕ, letI := data.continuous p
        Nonempty ((data.sequence.page 1).X ((p : ℤ), (q : ℤ)) ≅
          (Sheaf.functorH (BigFppfOver.associatedTopology B S hS
            (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
              (CatFiberedInGroupoids.homFunctor f.hom) p ⋙ 𝒳.val.val.p) SiteKind.fppf) q).obj
            ((SheafOfModules.toSheaf _).obj
              ((SheafOfModules.restrictAlongContinuous
                (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
                  (CatFiberedInGroupoids.homFunctor f.hom) p)
                (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
                  𝒳.val.isFiberedInGroupoids SiteKind.fppf)).obj F)))
```

## Tag 0785, a proposition

[Tag 0785](https://stacks.math.columbia.edu/tag/0785) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_quasicoherentCoveringSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentCoveringSpectralSequence.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentCoveringSpectralSequence.lean#L275). The attribute's comment: “the stated terms sit on the first page: the proof applies Q\_𝒴 to the E₁ spectral sequence of 072G, whose first differential is the Čech differential”.

> **Stacks 0785.** Let `f : 𝒰 ⟶ 𝒳` be a 1-morphism of algebraic stacks which is representable
> by algebraic spaces, surjective, flat, locally of finite presentation, quasi-compact and
> quasi-separated, and let `g : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks. For a quasi-coherent `𝒪_𝒳`-module `𝓕` there is a spectral sequence in
> `QCoh(𝒪_𝒴)` with `E₁^{p,q} = R^q (g ∘ fₚ)_{QCoh,*} fₚ^* 𝓕`, vanishing outside the first
> quadrant and abutting to `R^{p+q} g_{QCoh,*} 𝓕`, where `fₚ : 𝒰ₚ ⟶ 𝒳` is the projection of the
> degree `p` term `𝒰ₚ = 𝒰 ×_𝒳 ⋯ ×_𝒳 𝒰` of the Čech nerve of `f`.
>
> The source writes the first page as `E₂`; its proof applies the coherator to the `E₁` spectral
> sequence of **Stacks 072G**, whose first differential is the Čech differential, and that is the
> page on which the stated terms appear.

```lean
theorem exists_quasicoherentCoveringSpectralSequence
    (hrep : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hflat : IsFlat B S hS f)
    (hlfp : IsLocallyOfFinitePresentation B S hS f)
    (hfqc : IsQuasiCompactMorphism B S hS f) (hfqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (hgqc : IsQuasiCompactMorphism B S hS g) (hgqs : AlgebraicStacks.IsQuasiSeparated B S hS g)
    (𝓕 : quasicoherentModules B S hS 𝒳) :
    ∃ D : CohomologicalSpectralSequence (quasicoherentModules B S hS 𝒴) 1,
      (∀ i j : ℕ, Nonempty ((D.page 1 le_rfl).X ((i : ℤ), (j : ℤ)) ≅
        (quasicoherentHigherDirectImage B S hS (cechNerveProjection B S hS f i ≫ g) j).obj
          ((quasicoherentPullback B S hS (cechNerveProjection B S hS f i)).obj 𝓕))) ∧
      (∀ i j : ℤ, i < 0 ∨ j < 0 → IsZero ((D.page 1 le_rfl).X (i, j))) ∧
      SpectralSequence.AbutsTo D (fun n : ℤ => if n < 0 then 0 else
        (quasicoherentHigherDirectImage B S hS g n.toNat).obj 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.pushforwardPageOneIsoQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/QCohCoveringSpectralSequence.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/QCohCoveringSpectralSequence.lean#L141). The attribute's comment: “the reading of the E₁ page as the higher direct image of the inverse image of the quasi-coherent module, the inverse image being taken as a sheaf of modules and the higher direct image being the abelian one along the morphism of sites”.

> **Stacks 0785**, the first page. The term of the covering pushforward spectral sequence of a
> flat presentation in position `(p, q)` is the degree `q` higher direct image along `g ∘ fₚ` of
> the inverse image `fₚ^*𝓕` of the quasi-coherent module `𝓕` on the degree `p` term `𝒰ₚ` of the
> relative Čech nerve of `f`, the inverse image being taken as a sheaf of modules.

```lean
def pushforwardPageOneIsoQuasicoherent
    (𝓕 : FibredSite.quasicoherentModules.{u, u + 1, u, max (u + 1) a} B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids)
    (data : Stacks.RelativeCech.PushforwardSpectralSequenceData B S hS 𝒳.val.val.p
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor g.hom) SiteKind.fppf
      (fppfAbelianSheaf B S hS (fppfQuasicoherentSiteModule B S hS 𝓕))) (i j : ℕ) :
    letI := data.continuous i
    letI := data.cocontinuous i
    letI := data.gCocontinuous
    letI := data.enoughInjectives i
    letI : (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) i ⋙
        CatFiberedInGroupoids.homFunctor g.hom).IsCocontinuous
        (BigFppfOver.associatedTopology B S hS
          (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) i ⋙ 𝒳.val.val.p) SiteKind.fppf)
        (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p SiteKind.fppf) :=
      isCocontinuous_comp (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom) i)
        (CatFiberedInGroupoids.homFunctor g.hom)
        (BigFppfOver.associatedTopology B S hS
          (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) i ⋙ 𝒳.val.val.p) SiteKind.fppf)
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.fppf)
    letI := Stacks.RelativeCech.additive_pushforwardCocontinuous AddCommGrpCat.{max (u + 1) a}
      (BigFppfOver.associatedTopology B S hS
        (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom) i ⋙ 𝒳.val.val.p) SiteKind.fppf)
      (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p SiteKind.fppf)
      (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) i ⋙
        CatFiberedInGroupoids.homFunctor g.hom)
    (data.sequence.page 1).X ((i : ℤ), (j : ℤ)) ≅
      (((Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) i ⋙
          CatFiberedInGroupoids.homFunctor g.hom).sheafPushforwardCocontinuous
            AddCommGrpCat.{max (u + 1) a}
            (BigFppfOver.associatedTopology B S hS
              (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
                (CatFiberedInGroupoids.homFunctor f.hom) i ⋙ 𝒳.val.val.p) SiteKind.fppf)
            (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p SiteKind.fppf)).rightDerived
          j).obj
        ((SheafOfModules.toSheaf _).obj
          ((SheafOfModules.restrictAlongContinuous
            (Stacks.RelativeCech.Tuple.projection 𝒳.val.val.p
              (CatFiberedInGroupoids.homFunctor f.hom) i)
            (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
              𝒳.val.isFiberedInGroupoids SiteKind.fppf)).obj
            (fppfQuasicoherentSiteModule B S hS 𝓕)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.11, Tag 070A](https://stacks.math.columbia.edu/tag/070A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
