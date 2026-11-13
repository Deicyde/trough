---
declaration: section
origin: cited
lean: SheafOfModules.IsGoodToposBaseChange, SheafOfModules.dgExtensionByZeroRegular_isGoodToposBaseChange, SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_right, SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_left, SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_middle, SheafOfModules.DifferentialGradedModule.PullbackData.preservesColimitsOfSize_functor, SheafOfModules.RelativeTensor.isColimit_dgTensorFunctor_mapCocone, SheafOfModules.RelativeTensor.isKFlat_of_isColimit
statement: formalized
proof: formalized
---

# 24.23 Flat resolutions

Section 24.23 of the Stacks Project, [Tag 0FSA](https://stacks.math.columbia.edu/tag/0FSA). 9 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FSA, the section

[Tag 0FSA](https://stacks.math.columbia.edu/tag/0FSA) in the Stacks Project.

**`SheafOfModules.IsGoodToposBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeDifferentialGradedModuleToposPullback.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeDifferentialGradedModuleToposPullback.lean#L431).

> **A good right differential graded module**, with condition (3) read over the source's own
> base changes. A right differential graded `A`-module is good when it is flat as a graded
> module, K-flat, and for **every** base
> change along a morphism of ringed topoi — a second ringed topos `X`, a morphism of ringed topoi
> `f : X ⟶ Y`, a sheaf of differential graded algebras `B` on `X` and a **unital** homomorphism
> `ψ : A ⟶ f_*B`, which is the adjoint form of the source's `φ : f⁻¹A ⟶ B` — a pullback of `P`
> **exists**, as an object corepresenting `Q ↦ Hom_A(P, f_{*,ψ}Q)`, and every such object is flat
> as a graded module and K-flat.
>
> This is the quantification of Tag 0FSA's condition (3), binder for binder: a morphism of ringed
> topoi, a differential graded algebra on its source, a homomorphism over it, and conditions (1)
> and (2) required of the base-changed module. Nothing weaker and nothing stronger is quantified;
> in particular condition (3) is **not** vacuous and **not** an assumption of the sought-for
> isomorphism, the existential conjunct being part of the conclusion, and the second conjunct then
> transports to every chosen pullback by `Functor.CorepresentableBy.uniqueUpToIso`.
>
> The direct image of sheaves of modules is `toposDirectImageModules f`, whose lax monoidal
> structure is `toposDirectImageModules_laxMonoidal` — unconditional, the coherence of Tag 03EL
> being proved in `RingedToposPullbackCoherence.lean` — so the target `f_*B` of `ψ` is formed from
> `f` alone and no monoidal datum is quantified beside it.
>
> This is **not** `SheafOfModules.DifferentialGradedModule.IsGood` with its binders rewritten, and
> the two are **incomparable**, which is why no implication between them is proved here in either
> direction. `IsGood` quantifies bare functors of the two underlying categories: such a functor
> induces no morphism of topoi and yet can carry a `PullbackData` — the identity functor of a site
> at the trivial topology does, every presheaf being a sheaf there — so `IsGood` has clauses this
> definition has none at. In the other direction a morphism of topoi need not be induced by any
> functor of the two given sites, only by one of a site equivalent to the target (Tag 03CR, the
> first step of the source's own proof of Tag 0FSB), so `IsGood` has no clause at such a base
> change. What the two do share is conditions (1) and (2), verbatim; `isGradedFlat` and `isKFlat`
> below are the comparison that exists.
>
> `IsGoodCocontinuousBaseChange` and `IsGoodSiteBaseChange` restrict `IsGood`'s condition (3) to
> fewer base changes, so each is implied by `IsGood` and each is incomparable with this definition
> for the second of the two reasons above: a morphism of topoi induced by no functor of the two
> given sites is a clause of this definition and of neither of theirs.
>
> **Two restrictions on condition (3), stated rather than hidden.** First, the second ringed topos
> carries `HasSheafify X.J (Type w)` and `HasSheafify X.J AddCommGrpCat.{w}`, together with the
> three `GrothendieckTopology.HasSheafCompose` instances a morphism of ringed topoi and its direct
> image need. The sheafification of abelian groups is what the relative tensor product of the
> conclusion needs; the sheafification of types is what lets a sheaf of graded sets and its degree
> fibres be formed there, and it is the instance the proof for `A[S]` consumes. Mathlib supplies
> both at `Type (max u v)` for a site `C : Type u` with `[Category.{v} C]`, so they hold wherever
> the source's sites live, but a reading of condition (3) *without* them would be strictly stronger
> and this is not it. Second, the coefficient universe `w` is common to the two ringed topoi, where
> `Stacks.Sheaves.RingedToposModules.RingedToposHom` allows them independent; that boundary comes
> from the differential graded transport and is recorded in
> `DifferentialGradedToposDirectImage.lean`. Neither restriction is a hypothesis on a functor
> between the two underlying categories — there is none — and neither is a smallness assumption.

```lean
def IsGoodToposBaseChange (P : DifferentialGradedModule.{w, w, w} A) : Prop
```

## Tag 0FSB, a lemma

[Tag 0FSB](https://stacks.math.columbia.edu/tag/0FSB) in the Stacks Project.

**`SheafOfModules.dgExtensionByZeroRegular_isGoodToposBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodExtensionByZeroToposBaseChange.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodExtensionByZeroToposBaseChange.lean#L256).

> **Tag 0FSB: the extension by zero `j_!A_U` of the restriction of `A` to the slice site at `U`
> is a good right differential graded `A`-module.** It is flat as a graded module, it is K-flat,
> and after every base change along a morphism of ringed topoi a pullback of it exists and every
> pullback of it is again flat as a graded module and K-flat.
>
> Conditions (1) and (2) are the two theorems of
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodExtensionByZero.lean`, which run the source's
> argument from Tags 0FRB, 0FRX and 0FSB. Condition (3) is Tag 0FSG's, read through the
> identification of `j_!A_U` with the free differential graded module on the sheaf represented by
> `U` in degree zero.

```lean
theorem dgExtensionByZeroRegular_isGoodToposBaseChange :
    IsGoodToposBaseChange.{u, v₁, u₁} (dgExtensionByZeroRegular.{u} Y.O U A)
```

## Tag 0FSC, a lemma

[Tag 0FSC](https://stacks.math.columbia.edu/tag/0FSC) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean#L124). The attribute's comment: “the third term: if the first and the middle term of an admissible short exact sequence are good in the sense of 0FSA (`SheafOfModules.IsGoodToposBaseChange`, condition (3) over every morphism of ringed topoi), so is the third”.

> **Tag 0FSC, the third term.** If the first and the middle term of an admissible short exact
> sequence of right differential graded modules are good in the sense of Tag 0FSA, so is the third.
>
> Conditions (1) and (2) are two out of three for flatness and K-flatness. For condition (3) at a
> base change `(f, B, ψ)`: the third term is the cokernel of the first map, so a pullback of it is
> the cokernel of the pullbacks of the first two, a pullback being a value of a partial left adjoint
> of the direct image; and every pullback of it sits in the pullback of the sequence, which is an
> admissible short exact sequence whose first two terms are flat and K-flat.

```lean
theorem isGoodToposBaseChange_right (h : IsAdmissibleShortExact f g)
    (hK : IsGoodToposBaseChange.{w, v₁, u₁} K) (hL : IsGoodToposBaseChange.{w, v₁, u₁} L) :
    IsGoodToposBaseChange.{w, v₁, u₁} M
```

**`SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean#L155). The attribute's comment: “the first term: if the middle and the third term of an admissible short exact sequence are good in the sense of 0FSA (`SheafOfModules.IsGoodToposBaseChange`, condition (3) over every morphism of ringed topoi), so is the first”.

> **Tag 0FSC, the first term.** If the middle and the third term of an admissible short exact
> sequence of right differential graded modules are good in the sense of Tag 0FSA, so is the first.
>
> The shift `K[1]` is the third term of the admissible short exact sequence
> `0 → C(1_M) → C(g) → K[1] → 0`, whose first two terms are cones of morphisms between good
> modules and hence good; so `K[1]` is good by the third-term case, and `K` is good with it.

```lean
theorem isGoodToposBaseChange_left (h : IsAdmissibleShortExact f g)
    (hL : IsGoodToposBaseChange.{w, v₁, u₁} L) (hM : IsGoodToposBaseChange.{w, v₁, u₁} M) :
    IsGoodToposBaseChange.{w, v₁, u₁} K
```

**`SheafOfModules.DifferentialGradedModule.IsAdmissibleShortExact.isGoodToposBaseChange_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedAdmissibleTopos.lean#L172). The attribute's comment: “the middle term: if the two outer terms of an admissible short exact sequence are good in the sense of 0FSA (`SheafOfModules.IsGoodToposBaseChange`, condition (3) over every morphism of ringed topoi), so is the middle one”.

> **Tag 0FSC, the middle term.** If the two outer terms of an admissible short exact sequence of
> right differential graded modules are good in the sense of Tag 0FSA, so is the middle one.
>
> The shift `L[1]` is the cone of the connecting morphism `δ : M ⟶ K[1]`, a morphism between good
> modules, so it is good, and `L` is good with it.

```lean
theorem isGoodToposBaseChange_middle (h : IsAdmissibleShortExact f g)
    (hK : IsGoodToposBaseChange.{w, v₁, u₁} K) (hM : IsGoodToposBaseChange.{w, v₁, u₁} M) :
    IsGoodToposBaseChange.{w, v₁, u₁} L
```

## Tag 0FSD, a lemma

[Tag 0FSD](https://stacks.math.columbia.edu/tag/0FSD) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.PullbackData.preservesColimitsOfSize_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPullbackColimits.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPullbackColimits.lean#L77). The attribute's comment: “colimits commute with pullback: the pullback along a morphism of ringed sites preserves every colimit, being the left adjoint of the direct image”.

> **The pullback of sheaves of differential graded modules along a morphism of ringed sites
> preserves colimits of every shape.** The pullback is a left adjoint, the direct image along the
> morphism being its right adjoint, and a left adjoint preserves colimits.

```lean
theorem preservesColimitsOfSize_functor : PreservesColimitsOfSize.{w, w'} P.functor
```

**`SheafOfModules.RelativeTensor.isColimit_dgTensorFunctor_mapCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean#L127). The attribute's comment: “the relative tensor product with a fixed left differential graded module commutes, as a functor to complexes, with the colimits of right differential graded modules”.

> **The relative tensor product `- ⊗_A N` carries a colimit cocone of right differential
> graded modules to a colimit cocone of complexes of `O`-modules.** A cocone of complexes is
> colimiting as soon as it is in every degree, and in degree `n` the functor is the composite of
> forgetting the differential, a left adjoint, with degree `n` of the relative tensor product of
> graded modules.

```lean
noncomputable def isColimit_dgTensorFunctor_mapCocone
    (N : LeftDifferentialGradedModule.{t, m, m} A) {K : D ⥤ DifferentialGradedModule.{t, m, m} A}
    {c : Cocone K} (hc : IsColimit c) : IsColimit ((dgTensorFunctor N).mapCocone c)
```

**`SheafOfModules.RelativeTensor.isKFlat_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean#L142). The attribute's comment: “a colimit of K-flat right differential graded modules is K-flat, the K-flatness half of the lemma, for an index category whose colimits of sheaves of modules are exact”.

> **A colimit of K-flat right differential graded modules is K-flat**, along any shape whose
> colimits of sheaves of modules are exact.

```lean
theorem isKFlat_of_isColimit {K : D ⥤ DifferentialGradedModule.{t, m, m} A} {c : Cocone K}
    (hc : IsColimit c) (hK : ∀ d : D, IsKFlat (K.obj d)) : IsKFlat c.pt
```

**`SheafOfModules.RelativeTensor.isKFlat_of_isColimitCofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean#L152). The attribute's comment: “an arbitrary direct sum of K-flat right differential graded modules is K-flat, the K-flatness half of the direct sum clause”.

> **An arbitrary direct sum of K-flat right differential graded modules is K-flat.**

```lean
theorem isKFlat_of_isColimitCofan {ι : Type m} {P : ι → DifferentialGradedModule.{t, m, m} A}
    {c : Cofan P} (hc : IsColimit c) (hP : ∀ i, IsKFlat (P i)) : IsKFlat c.pt
```

**`SheafOfModules.RelativeTensor.isKFlat_of_isColimit_isFiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean#L160). The attribute's comment: “a filtered colimit of K-flat right differential graded modules is K-flat, the K-flatness half of the filtered colimit clause”.

> **A filtered colimit of K-flat right differential graded modules is K-flat.**

```lean
theorem isKFlat_of_isColimit_isFiltered {D : Type m} [SmallCategory D] [IsFiltered D]
    {K : D ⥤ DifferentialGradedModule.{t, m, m} A} {c : Cocone K} (hc : IsColimit c)
    (hK : ∀ d : D, IsKFlat (K.obj d)) : IsKFlat c.pt
```

**`SheafOfModules.DifferentialGradedModule.isGradedFlat_and_isKFlat_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedColimit.lean#L181). The attribute's comment: “flatness of the underlying graded module and K-flatness pass to a colimit of right differential graded modules, for an index category whose colimits of sheaves of modules are exact”.

> Flatness of the underlying graded module and K-flatness pass together to a colimit of right
> differential graded modules, along any shape whose colimits of sheaves of modules are exact.
> This is the conjunction that appears both as conditions (1) and (2) of
> `IsGoodCocontinuousBaseChange` and as its condition (3) after a base change.

```lean
theorem isGradedFlat_and_isKFlat_of_isColimit {D : Type m} [Category.{m} D]
    [HasColimitsOfShape D (SheafOfModules.{m} (toRingCat J Osharp))]
    [HasExactColimitsOfShape D (SheafOfModules.{m} (toRingCat J Osharp))]
    {K : D ⥤ DifferentialGradedModule.{t, m, m} A} {c : Cocone K} (hc : IsColimit c)
    (hK : ∀ d : D, RelativeTensor.IsGradedFlat (GradedModule.ofDifferentialGraded (K.obj d)) ∧
      RelativeTensor.IsKFlat (K.obj d)) :
    RelativeTensor.IsGradedFlat (GradedModule.ofDifferentialGraded c.pt) ∧
      RelativeTensor.IsKFlat c.pt
```

**`SheafOfModules.isGoodToposBaseChange_of_isColimitCofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedToposDirectSum.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedToposDirectSum.lean#L67).

> **An arbitrary direct sum of good right differential graded modules is good**, goodness being
> `SheafOfModules.IsGoodToposBaseChange`: conditions (1) and (2) of Tag 0FSA together with
> condition (3) read over the morphisms of ringed topoi out of the base.

```lean
theorem isGoodToposBaseChange_of_isColimitCofan {ι : Type w}
    {P : ι → DifferentialGradedModule.{w, w, w} A} {c : Cofan P} (hc : IsColimit c)
    (hP : ∀ i, IsGoodToposBaseChange.{w, v₁, u₁} (P i)) :
    IsGoodToposBaseChange.{w, v₁, u₁} c.pt
```

**`SheafOfModules.isGoodToposBaseChange_of_isColimit_isFiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedToposDirectSum.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedToposDirectSum.lean#L79).

> **A filtered colimit of good right differential graded modules is good**, goodness being
> `SheafOfModules.IsGoodToposBaseChange`.

```lean
theorem isGoodToposBaseChange_of_isColimit_isFiltered {D : Type w} [SmallCategory D]
    [IsFiltered D] {K : D ⥤ DifferentialGradedModule.{w, w, w} A} {c : Cocone K}
    (hc : IsColimit c) (hK : ∀ d : D, IsGoodToposBaseChange.{w, v₁, u₁} (K.obj d)) :
    IsGoodToposBaseChange.{w, v₁, u₁} c.pt
```

**`SheafOfModules.RelativeTensor.isGradedFlat_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean#L101). The attribute's comment: “a colimit of flat right graded modules is flat, the graded-flatness half of the lemma, for an index category whose colimits of sheaves of modules are exact”.

> **A colimit of flat right graded modules is flat**, along any shape whose colimits of
> sheaves of modules are exact.

```lean
theorem isGradedFlat_of_isColimit {K : D ⥤ GradedModule.{t, m, m} A} {c : Cocone K}
    (hc : IsColimit c) (hK : ∀ d : D, IsGradedFlat (K.obj d)) : IsGradedFlat c.pt
```

**`SheafOfModules.RelativeTensor.isGradedFlat_of_isColimitCofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean#L141). The attribute's comment: “an arbitrary direct sum of flat right graded modules is flat, the graded-flatness half of the direct sum clause”.

> **An arbitrary direct sum of flat right graded modules is flat.**

```lean
theorem isGradedFlat_of_isColimitCofan {ι : Type m} {P : ι → GradedModule.{t, m, m} A}
    {c : Cofan P} (hc : IsColimit c) (hP : ∀ i, IsGradedFlat (P i)) : IsGradedFlat c.pt
```

**`SheafOfModules.RelativeTensor.isGradedFlat_of_isColimit_isFiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedFlatColimit.lean#L149). The attribute's comment: “a filtered colimit of flat right graded modules is flat, the graded-flatness half of the filtered colimit clause”.

> **A filtered colimit of flat right graded modules is flat.**

```lean
theorem isGradedFlat_of_isColimit_isFiltered {D : Type m} [SmallCategory D] [IsFiltered D]
    {K : D ⥤ GradedModule.{t, m, m} A} {c : Cocone K} (hc : IsColimit c)
    (hK : ∀ d : D, IsGradedFlat (K.obj d)) : IsGradedFlat c.pt
```

## Tag 0FSE, a lemma

[Tag 0FSE](https://stacks.math.columbia.edu/tag/0FSE) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_flat_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionQuotient.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionQuotient.lean#L376). The attribute's comment: “the resolution is built from M alone: the first stage of the tower of Tag 0FSH, the twisted extension of the free module on the closed sections of M by the free module on the boundary pairs of its homomorphism to M. Clause (2) is concluded as surjectivity on the sections killed by the differential, which is stronger than surjectivity of Ker(d\_P) to Ker(d\_M), and also as an epimorphism on the sheaves of cocycles. Clause (3) is concluded here as conditions (1) and (2) of the definition of good in Section 0FSA, flatness of the underlying graded module and K-flatness, over a ringed site and with the ring universe and the module universe independent, and the whole of condition (3) for this same module is concluded over a ringed topos by exists\_good\_surjection”.

> **Tag 0FSE.** Every right differential graded `A`-module `M` receives a homomorphism from a
> right differential graded `A`-module which is surjective, which is surjective on the sheaves of
> cocycles, and whose source is flat as a graded module and K-flat.
>
> The source is the first stage of the tower of the first proof of Tag 0FSH: the twisted extension
> of the free differential graded module on the sheaf of graded sets of closed sections of `M` by
> the free module on the sheaf of graded sets of boundary pairs of its homomorphism to `M`. It is
> built from `M` alone.
>
> Clause (2) is available on sections as well, as
> `SheafOfModules.DifferentialGradedModule.exists_closed_preimage_towerStepMap`: every local
> section of `M^n` killed by the differential is the image of a local section of the source killed
> by the differential. Clause (3) is read here as conditions (1) and (2) of the definition of good
> in Section 0FSA, flatness of the underlying graded module and K-flatness, over a ringed site and
> with the ring universe and the module universe independent;
> `SheafOfModules.DifferentialGradedModule.exists_good_surjection` concludes the same three clauses
> for the same module with the third at the whole of goodness, over a ringed topos.

```lean
theorem exists_flat_surjection (M : DifferentialGradedModule.{t, m, m} A) :
    ∃ (Q : DifferentialGradedModule.{t, m, m} A) (π : Q ⟶ M),
      (∀ n : ℤ, Epi (π.toHomologicalComplex.f n)) ∧
        (∀ n : ℤ, Epi (HomologicalComplex.cyclesMap π.toHomologicalComplex n)) ∧
          RelativeTensor.IsGradedFlat (GradedModule.ofDifferentialGraded Q) ∧
            RelativeTensor.IsKFlat Q
```

**`SheafOfModules.DifferentialGradedModule.exists_good_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionToposQuotient.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionToposQuotient.lean#L124).

> **Tag 0FSE.** Every right differential graded `A`-module `M` receives a homomorphism from a
> right differential graded `A`-module which is surjective, which is surjective on the sheaves of
> cocycles, and whose source is good — `SheafOfModules.IsGoodToposBaseChange`, which is flat as a
> graded module, K-flat, and such that along every morphism of ringed topoi out of the base, every
> sheaf of differential graded algebras on its source and every unital homomorphism over it a
> pullback exists and is again flat and K-flat.
>
> The source is the first stage of the tower of the first proof of Tag 0FSH: the twisted extension
> of the free differential graded module on the sheaf of graded sets of closed sections of `M` by
> the free module on the sheaf of graded sets of boundary pairs of its homomorphism to `M`. It is
> built from `M` alone.
>
> Clause (2) is available on sections as well, as
> `SheafOfModules.DifferentialGradedModule.exists_closed_preimage_towerStepMap`: every local
> section of `M^n` killed by the differential is the image of a local section of the source killed
> by the differential.
>
> `SheafOfModules.DifferentialGradedModule.exists_flat_surjection` is the same three clauses with
> the third read as conditions (1) and (2) of Section 0FSA alone, over a ringed site and with the
> ring universe and the module universe independent.

```lean
theorem exists_good_surjection [HasWeakSheafify Y.J (Type w)]
    (M : DifferentialGradedModule.{w, w, w} A) :
    ∃ (Q : DifferentialGradedModule.{w, w, w} A) (π : Q ⟶ M),
      (∀ n : ℤ, Epi (π.toHomologicalComplex.f n)) ∧
        (∀ n : ℤ, Epi (HomologicalComplex.cyclesMap π.toHomologicalComplex n)) ∧
          IsGoodToposBaseChange.{w, v₁, u₁} Q
```

## Tag 0FSF, a remark

[Tag 0FSF](https://stacks.math.columbia.edu/tag/0FSF) in the Stacks Project.

**`Stacks.SheafOfGradedSets`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModule.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModule.lean#L181). The attribute's comment: “sheaf\_of\_graded\_sets”.

> A sheaf of graded sets on a site: a sheaf of sets together with a degree morphism to the
> constant sheaf of integers.

```lean
structure SheafOfGradedSets (J : GrothendieckTopology C) [HasWeakSheafify J (Type w)]
```

**`SheafOfModules.freeGradedModuleData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModule.lean, line 1770](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModule.lean#L1770). The attribute's comment: “free\_graded\_mathcal\_a\_module\_mathcal\_a\_mathcal\_s”.

> **The free graded `A`-module on a sheaf of graded sets**, with its presentation, its
> generators, its universal property and — whenever `A` is the graded algebra underlying a
> differential graded algebra — its closed-generator differential.

```lean
noncomputable def freeGradedModuleData : FreeGradedModuleData A S
```

## Tag 0FSG, a lemma

[Tag 0FSG](https://stacks.math.columbia.edu/tag/0FSG) in the Stacks Project.

**`SheafOfModules.freeDGModule_isGoodToposBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeDifferentialGradedModuleToposPullback.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeDifferentialGradedModuleToposPullback.lean#L502). The attribute's comment: “the free differential graded module on a sheaf of graded sets is good, with condition (3) of 0FSA read over morphisms of ringed topoi”.

> **Tag 0FSG: the free differential graded module `A[S]` on a sheaf of graded sets is good**, at
> the source's own quantification. Conditions (1) and (2) are the two unconditional theorems of
> `FreeGradedModuleFlat.lean`; condition (3) is the corepresentability of `B[f⁻¹S]` together with
> the flatness of every object corepresenting the same functor, which is
> `SheafOfModules.nonempty_corepresentableBy_and_flat` at the geometric direct image. There is no
> hypothesis beyond those under which `A[S]` exists.

```lean
theorem freeDGModule_isGoodToposBaseChange [HasWeakSheafify Y.J (Type w)]
    (S : Stacks.SheafOfGradedSets.{w} Y.J) :
    IsGoodToposBaseChange.{w, v₁, u₁} (freeDGModule S A)
```

**`SheafOfModules.freeDGModule_isGradedFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModuleFlat/FlatAndKFlat.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModuleFlat/FlatAndKFlat.lean#L483). The attribute's comment: “condition (1) of good (Stacks 0FSA) for the free graded module A[S] on a sheaf of graded sets: the underlying graded module is flat. No hypotheses; the source's own argument. Condition (2) is SheafOfModules.freeDGModule\_isKFlat in this file; condition (3) is not proved here, and goodness is concluded at SheafOfModules.freeDGModule\_isGoodToposBaseChange, where condition (3) is read over morphisms of ringed topoi as 0FSA states it. At the three site-indexed readings IsGood, IsGoodCocontinuousBaseChange and IsGoodSiteBaseChange condition (3) is still open -- see the implementation notes”.

> **Tag 0FSG, condition (1) of Tag 0FSA.** The graded module underlying the free differential
> graded `A`-module `A[S]` on a sheaf of graded sets is flat. The differential plays no part: the
> underlying graded module of `A[S]` as a differential graded module **is** the free graded module
> on `S` over the graded algebra underlying `A`, so this is
> `SheafOfModules.freeGradedModule_isGradedFlat`.

```lean
theorem freeDGModule_isGradedFlat (D : DifferentialGradedAlgebra.{t, m} (toRingCat J Osharp))
    (S : SheafOfGradedSets.{m} J) :
    RelativeTensor.IsGradedFlat (GradedModule.ofDifferentialGraded (freeDGModule S D))
```

**`SheafOfModules.freeDGModule_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModuleFlat/FlatAndKFlat.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeGradedModuleFlat/FlatAndKFlat.lean#L519). The attribute's comment: “condition (2) of good (Stacks 0FSA) for the free differential graded module D[S] on a sheaf of graded sets: D[S] tensor\_D N is acyclic for every acyclic left differential graded D-module N. No hypotheses; the source's own argument. Condition (1) is SheafOfModules.freeDGModule\_isGradedFlat in this file; condition (3) is not proved here, and goodness is concluded at SheafOfModules.freeDGModule\_isGoodToposBaseChange, where condition (3) is read over morphisms of ringed topoi as 0FSA states it. At the three site-indexed readings IsGood, IsGoodCocontinuousBaseChange and IsGoodSiteBaseChange condition (3) is still open -- see the implementation notes”.

> **Tag 0FSG, condition (2) of Tag 0FSA.** The free differential graded `D`-module `D[S]` on a
> sheaf of graded sets is K-flat: `D[S] ⊗_D N` is acyclic for every acyclic left differential
> graded `D`-module `N`.
>
> The proof is the source's. Degree `n` of `D[S] ⊗_D N` is the free graded module `N[S]` on `S`
> with coefficients in `N`, by `SheafOfModules.freeTensorCoeffIso`, and under that identification
> the differential is the signed degree-raising map of `N[S]`, by
> `SheafOfModules.freeTensorCoeff_dgTensorDiff`. Exactness in degree `n + 1` is then the exactness
> of a short complex of pieces of `N[S]` twisted by the sign automorphism, which
> `SheafOfModules.coeffPiece_exact_sign` deduces from the exactness of `N` in the three adjacent
> degrees; the transports matching the degrees of the three terms are
> `SheafOfModules.coeffCastPieceIso`.

```lean
theorem freeDGModule_isKFlat : RelativeTensor.IsKFlat (freeDGModule S D)
```

## Tag 0FSH, a lemma

[Tag 0FSH](https://stacks.math.columbia.edu/tag/0FSH) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_good_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionToposTower.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionToposTower.lean#L138).

> **Tag 0FSH: every right differential graded `A`-module receives a quasi-isomorphism from a
> good one.** Goodness is `SheafOfModules.IsGoodToposBaseChange`: flat as a graded module, K-flat,
> and a pullback exists and is again flat and K-flat along every morphism of ringed topoi out of
> the base, every sheaf of differential graded algebras on its source and every unital
> homomorphism over it.
>
> The source's tower is built here rather than assumed: the first stage is the free differential
> graded module on the sheaf of graded sets of closed sections of `M`, good by Tag 0FSG; each
> further stage is the twisted extension of the previous one by the free module on the boundary
> pairs of its homomorphism to `M`, good by
> `SheafOfModules.cone_freeDGModule_isGoodToposBaseChange` since a twisted extension is the cone of
> a homomorphism out of a free module; and the resolution is the colimit of the resulting sequence,
> good by `SheafOfModules.isGoodToposBaseChange_of_isColimit_nat`, the sequential shape being
> filtered.

```lean
theorem exists_good_quasiIso [HasWeakSheafify Y.J (Type w)]
    (M : DifferentialGradedModule.{w, w, w} A) :
    ∃ (Q : DifferentialGradedModule.{w, w, w} A) (f : Q ⟶ M),
      QuasiIso f.toHomologicalComplex ∧ IsGoodToposBaseChange.{w, v₁, u₁} Q
```

**`SheafOfModules.DifferentialGradedModule.exists_flat_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionTower.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodDifferentialGradedResolutionTower.lean#L150). The attribute's comment: “the tower of the first proof, built from M alone: the free differential graded module on the sheaf of graded sets of closed sections of M, then the twisted extensions by the free modules on the boundary pairs of each stage, then the colimit. The ring universe and the module universe stay independent here; at a common universe the same tower reaches the full goodness of Section 0FSA in SheafOfModules.DifferentialGradedModule.exists\_good\_quasiIso”.

> **Every right differential graded `A`-module receives a quasi-isomorphism from a right
> differential graded `A`-module which is flat as a graded module and K-flat.**
>
> The source's tower is built here rather than assumed: the first stage is the free differential
> graded module on the sheaf of graded sets of closed sections of `M`, each further stage is the
> twisted extension of the previous one by the free module on the boundary pairs of its
> homomorphism to `M`, and the resolution is the colimit of the resulting sequence.

```lean
theorem exists_flat_quasiIso (M : DifferentialGradedModule.{t, m, m} A) :
    ∃ (Q : DifferentialGradedModule.{t, m, m} A) (f : Q ⟶ M),
      QuasiIso f.toHomologicalComplex ∧
        RelativeTensor.IsGradedFlat (GradedModule.ofDifferentialGraded Q) ∧
          RelativeTensor.IsKFlat Q
```

## Tag 0FSI, a lemma

[Tag 0FSI](https://stacks.math.columbia.edu/tag/0FSI) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.acyclic_dgTensor_of_isGood_of_acyclic_topos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodAcyclicDifferentialGradedToposPullback.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodAcyclicDifferentialGradedToposPullback.lean#L123). The attribute's comment: “part (1)”.

> **Tag 0FSI (1).** *"Let `(C, O)` be a ringed site. Let `A` be a sheaf of differential graded
> algebras on `(C, O)`. Let `P` be a good acyclic right differential graded `A`-module. Then for any
> differential graded left `A`-module `N` the tensor product `P ⊗_A N` is acyclic."*
>
> Goodness is `SheafOfModules.IsGoodToposBaseChange`, the definition of Tag 0FSA.

```lean
theorem acyclic_dgTensor_of_isGood_of_acyclic_topos {Y : AlgebraicGeometry.RingedTopos.{u, u, u}}
    {A : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O)}
    {P : DifferentialGradedModule.{u, u, u} A} (good : IsGoodToposBaseChange.{u, u, u} P)
    (acyclic : P.complex.Acyclic) (N : LeftDifferentialGradedModule.{u, u, u} A) :
    (RelativeTensor.dgTensor P N).Acyclic
```

**`SheafOfModules.DifferentialGradedModule.exists_toposCorepresentableBy_and_acyclic_and_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodAcyclicDifferentialGradedToposPullback.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GoodAcyclicDifferentialGradedToposPullback.lean#L141). The attribute's comment: “part (2)”.

> **Tag 0FSI (2).** *"Let `(C, O)` be a ringed site. Let `A` be a sheaf of differential graded
> algebras on `(C, O)`. Let `P` be a good acyclic right differential graded `A`-module. Then for any
> morphism `(f, f♯) : (Sh(C'), O') ⟶ (Sh(C), O)` of ringed topoi and any differential graded
> `O'`-algebra `A'` and any map `φ : f⁻¹A ⟶ A'` of differential graded `f⁻¹O`-algebras the pullback
> `f^*P` is acyclic and good."*
>
> The map `φ` is written in its adjoint form, a unital `ψ : A ⟶ f_*A'`. The pullback `f^*P` along
> `(f, A', ψ)` is an object corepresenting `Q ↦ Hom_A(P, f_{*,ψ}Q)`: one exists, and every one is
> acyclic and good, goodness being `SheafOfModules.IsGoodToposBaseChange`, the definition of
> Tag 0FSA.

```lean
theorem exists_toposCorepresentableBy_and_acyclic_and_isGood
    {X Y : AlgebraicGeometry.RingedTopos.{u, u, u}}
    {A : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O)}
    {P : DifferentialGradedModule.{u, u, u} A} (good : IsGoodToposBaseChange.{u, u, u} P)
    (acyclic : P.complex.Acyclic) (f : RingedToposHom X Y)
    (A' : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O))
    (ψ : A ⟶ toposPushforwardAlgebra (toposDirectImageModules (X := X) (Y := Y) f) A')
    (hψ : ψ.IsUnital) :
    (∃ T : DifferentialGradedModule.{u, u, u} A',
        Nonempty ((toposPushforward (toposDirectImageModules (X := X) (Y := Y) f) ψ hψ ⋙
          coyoneda.obj (Opposite.op P)).CorepresentableBy T)) ∧
      ∀ T : DifferentialGradedModule.{u, u, u} A',
        (toposPushforward (toposDirectImageModules (X := X) (Y := Y) f) ψ hψ ⋙
            coyoneda.obj (Opposite.op P)).CorepresentableBy T →
          T.complex.Acyclic ∧ IsGoodToposBaseChange.{u, u, u} T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.23, Tag 0FSA](https://stacks.math.columbia.edu/tag/0FSA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
