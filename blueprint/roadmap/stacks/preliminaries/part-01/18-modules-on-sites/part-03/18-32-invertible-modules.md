---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.IsInvertible, Stacks.SheafOfModules.Invertible.isInvertible_iff_tensorRightFunctor_isEquivalence, AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank, AlgebraicGeometry.RingedSite.unitsSheaf, AlgebraicGeometry.RingedSite.unitsSheafι_mono, AlgebraicGeometry.RingedSite.exists_unitsSheaf_iff_exists_mul_eq_one, AlgebraicGeometry.RingedSite.unitsSheafι_hom_app_mul, Stacks.SheafOfModules.Invertible.tensorInverseIsoDualSheaf
statement: formalized
proof: formalized
---

# 18.32 Invertible modules

Section 18.32 of the Stacks Project, [Tag 0408](https://stacks.math.columbia.edu/tag/0408). 6 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0409, a definition

[Tag 0409](https://stacks.math.columbia.edu/tag/0409) in the Stacks Project.

**`Stacks.SheafOfModules.IsInvertible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean#L130). The attribute's comment: “invertible”.

> **Stacks Project, Tag 01CS**, equivalently **Tag 0409 (2)**. A sheaf of `O`-modules is
> *invertible* when its tensor functor is an equivalence. The universal property specifies that
> tensor functor independently of any chosen construction of sheafification, hence on every
> site; so the ringed-space form of the definition and the ringed-site form coincide here.

```lean
class IsInvertible
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) : Prop
```

**`Stacks.SheafOfModules.Invertible.isInvertible_iff_tensorRightFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/TensorPower.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/TensorPower.lean#L132). The attribute's comment: “invertible”.

> **Stacks Project, Tag 0409 (2)**, equivalently **Tag 01CS**, in the source's own form: a
> sheaf of `O`-modules `L` is invertible exactly when the functor `F ↦ (F ⊗_O L)^#` of the
> source is an equivalence. The invertibility predicate is phrased through the universal
> property of tensoring on the *left*, so this is the criterion the source states and the
> predicate agreeing, the two tensor functors being identified by `tensorLeftIsoTensorRight`.

```lean
theorem isInvertible_iff_tensorRightFunctor_isEquivalence
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) :
    IsInvertible O hO L ↔ ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).flip.obj
        L).IsEquivalence
```

**`AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FiniteLocallyFreeOfRank.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FiniteLocallyFreeOfRank.lean#L62). The attribute's comment: “rank”. References: EGA 0 (5.4.1), “rank n”.

> A sheaf of modules on a ringed site is finite locally free of rank `r` if it is, over a
> covering family of every object, a coproduct of `r` copies of the structure sheaf. This is the
> rank clause of Stacks 0409.

```lean
abbrev IsFiniteLocallyFreeOfRank (X : RingedSite.{u, v, w})
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (r : ℕ) : Prop
```

**`AlgebraicGeometry.RingedSite.unitsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean#L50). The attribute's comment: “units sheaf”.

> The sheaf of units `O_X^*` of the structure sheaf of a ringed site.

```lean
noncomputable def unitsSheaf (X : RingedSite.{u, v, w}) : Sheaf X.J CommGrpCat.{w}
```

**`AlgebraicGeometry.RingedSite.unitsSheafι_mono`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean#L64). The attribute's comment: “subsheaf”.

> The canonical inclusion of the units sheaf into the structure sheaf is a monomorphism.

```lean
instance unitsSheafι_mono (X : RingedSite.{u, v, w}) : Mono (unitsSheafι X)
```

**`AlgebraicGeometry.RingedSite.exists_unitsSheaf_iff_exists_mul_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean#L84). The attribute's comment: “defining rule”.

> A section belongs to the units subsheaf exactly when it has a right inverse: the units
> subsheaf is `U ↦ {f ∈ O(U) | ∃ g ∈ O(U), fg = 1}`.

```lean
theorem exists_unitsSheaf_iff_exists_mul_eq_one (X : RingedSite.{u, v, w}) (U : X.Cᵒᵖ)
    (f : X.O.obj.obj U) :
    (∃ x : ((unitsSheaf X).obj.obj U : Type w), (unitsSheafι X).hom.app U x = f) ↔
      ∃ g : X.O.obj.obj U, f * g = 1
```

**`AlgebraicGeometry.RingedSite.unitsSheafι_hom_app_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheaf.lean#L103). The attribute's comment: “group law”.

> The group law on the sheaf of units is multiplication: the subsheaf inclusion
> `O_X^* ⟶ O_X` is multiplicative.

```lean
theorem unitsSheafι_hom_app_mul (X : RingedSite.{u, v, w}) (U : X.Cᵒᵖ)
    (x y : (X.O.obj.obj U)ˣ) :
    (unitsSheafι X).hom.app U (x * y) =
      (x : X.O.obj.obj U) * (y : X.O.obj.obj U)
```

## Tag 0B8N, a lemma

[Tag 0B8N](https://stacks.math.columbia.edu/tag/0B8N) in the Stacks Project.

**`Stacks.SheafOfModules.Invertible.tensorInverseIsoDualSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L307). The attribute's comment: “(c)”. References: SGA 6 VIII (3.5), “partial”.

> **Stacks Project, Tag 0B8N (c).** A sheaf of `𝒪`-modules `N` whose tensor product with `L` is
> isomorphic to the structure sheaf is isomorphic to `SheafHom(L, 𝒪)`.
>
> The hypothesis is clause (2) of the tag, so `L` is invertible and the evaluation pairing
> `SheafHom(L, 𝒪) ⊗_𝒪 L ⟶ 𝒪` is an isomorphism by `isIso_evaluation`. That exhibits
> `SheafHom(L, 𝒪)` as a two-sided tensor inverse of `L`, the braiding supplying the other order,
> while the given isomorphism exhibits `N` as one; a two-sided tensor inverse in a monoidal
> category is unique up to isomorphism
> (`CategoryTheory.MonoidalCategory.HasInverse.inv_iso`).

```lean
noncomputable def tensorInverseIsoDualSheaf
    (N : SheafOfModules.{max u v} (TensorSheafification.structureSheaf 𝒪 h𝒪))
    (e : ((Tensor.sheafTensor
      ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ 𝒪 (forget₂ CommRingCat RingCat) h𝒪⟩).obj L).obj N ≅
      SheafOfModules.unit (TensorSheafification.structureSheaf 𝒪 h𝒪)) :
    N ≅ dualSheaf 𝒪 h𝒪 L
```

**`Stacks.SheafOfModules.isFlat_of_isInvertible_ringedSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleEquivalence.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleEquivalence.lean#L207). The attribute's comment: “(a), the flatness half”.

> An invertible sheaf of modules on a ringed site is flat.

```lean
theorem isFlat_of_isInvertible_ringedSite
    (L : SheafOfModules.{w} (TensorSheafification.structureSheaf O.obj hO))
    (hL : IsInvertible O.obj hO L) :
    IsFlat (O := O) L
```

**`Stacks.SheafOfModules.isFinitePresentation_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleFinitePresentation.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleFinitePresentation.lean#L289). The attribute's comment: “(a), the finite-presentation half”.

> **An invertible sheaf of modules is of finite presentation.**
>
> This is the step of Tag 0B8M's converse that Stacks attributes to Tag 0B8K. By Tag 0B8N (b)
> every object of the site has a covering family on whose members `L` is a split subobject of a
> finite product of copies of the structure sheaf, hence has a finite presentation there; the union
> over all objects of those families covers the terminal object, and finite presentation is
> local.
>
> This is also the finite-presentation half of Tag 0B8N (a).

```lean
theorem isFinitePresentation_of_isInvertible
    (hO : Presheaf.IsSheaf J (Stacks.SheafOfModules.TensorSheafification.structureRingPresheaf O))
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) (hL :
      IsInvertible O hO L) :
    L.IsFinitePresentation
```

**`Stacks.SheafOfModules.isInvertible_iff_exists_tensor_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOne.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOne.lean#L298). The attribute's comment: “(1) ⟺ (2)”.

> **Stacks Project, Tag 0B8K and Tag 0B8N, (1) ⟺ (2).** A sheaf of `O`-modules `L` is invertible
> if and only if there is a sheaf of `O`-modules `N` whose tensor product with `L` is isomorphic
> to `O`.
>
> For the forward implication the tensor functor of `L` is an equivalence, so `O` has a preimage `N`
> under it, and the universal property identifies the image of that preimage with `L ⊗_O N`. For the
> converse the isomorphism `L ⊗_O N ≅ O` is turned into a pairing of presheaves of modules by
> composing with the sheafification unit, and `isInvertible_of_pairing` applies.
>
> Tag 0B8K states this for a ringed space and Tag 0B8N for an arbitrary ringed site; the statement
> here is the one on a ringed site, so it carries both.

```lean
theorem isInvertible_iff_exists_tensor_iso_unit
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) :
    IsInvertible O hO L ↔ ∃ N : SheafOfModules.{w}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO),
      Nonempty (((Tensor.sheafTensor.{u, v, w, w, w}
        ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L).obj N ≅
        SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
```

**`Stacks.SheafOfModules.exists_cover_isDirectSummand_finiteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleSummandNoSliceSheafify.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleSummandNoSliceSheafify.lean#L378). The attribute's comment: “(b), invertible\_local\_summand”.

> **Stacks Project, Tag 0B8N (b).** On a cover of any object, an invertible module embeds as a
> direct summand of a finite free module. The two sheafification hypotheses are used only by
> `Stacks.SheafOfModules.isLocallyInjective_of_universal`; none is needed on the slice sites.

```lean
theorem exists_cover_isDirectSummand_finiteFree
    (hO : Presheaf.IsSheaf J (Stacks.SheafOfModules.TensorSheafification.structureRingPresheaf O))
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
      [IsInvertible O hO L] (U : C) :
    ∃ (I : Type (max u v)) (V : I → C) (f : ∀ i, V i ⟶ U),
      Sieve.generate (Presieve.ofArrows V f) ∈ J U ∧
        ∀ i : I, ∃ n : ℕ,
          ∃ s : L.over (V i) ⟶
              ∏ᶜ (fun _ : Fin n ↦
                SheafOfModules.unit ((Stacks.SheafOfModules.TensorSheafification.structureSheaf O
                  hO).over (V i))),
            IsSplitMono s
```

## Tag 0B8P, a lemma

[Tag 0B8P](https://stacks.math.columbia.edu/tag/0B8P) in the Stacks Project.

**`Stacks.SheafOfModules.isInvertible_pullbackModules_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/RingedTopos.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/RingedTopos.lean#L86).

> **Stacks Project, Tag 0B8P.** The pullback of an invertible module along a morphism of
> ringed topoi is invertible.

```lean
theorem isInvertible_pullbackModules_obj (f : RingedToposHom X Y)
    (L : SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    [hL : IsInvertible Y.O.obj (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).property L] :
    IsInvertible X.O.obj (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property
      ((f.pullbackModules).obj L)
```

**`Stacks.SheafOfModules.isInvertible_pullbackModules_obj_ringedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/RingedTopos.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/RingedTopos.lean#L102).

> **Stacks Project, Tag 0B8P** for a morphism of ringed topoi in the two-field sense of Tag
> 01D3 part (2): the pullback of an invertible module is invertible.

```lean
theorem isInvertible_pullbackModules_obj_ringedToposHom
    (f : AlgebraicGeometry.RingedToposHom X Y)
    (L : SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    [IsInvertible Y.O.obj (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).property L] :
    IsInvertible X.O.obj (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property
      ((f.toRingedToposModulesHom.pullbackModules).obj L)
```

**`AlgebraicGeometry.Space.modulePullbackInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean#L234). The attribute's comment: “the inverse image of an invertible module along a morphism of algebraic spaces is invertible”.

> **The inverse image of an invertible module along a morphism of algebraic spaces is
> invertible.**  This is `AlgebraicGeometry.Space.isInvertible_modulePullback_obj`, read through
> the two spellings of invertibility of
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleCompare.lean`.

```lean
theorem modulePullbackInvertible : ModulePullbackInvertible B S hS
```

## Tag 040A, a lemma

[Tag 040A](https://stacks.math.columbia.edu/tag/040A) in the Stacks Project.

**`Stacks.SheafOfModules.Invertible.isIso_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L261). The attribute's comment: “part (2)”. References: EGA 0 (5.4.3), “more general”.

> **Stacks Project, Tag 040A (2), the evaluation clause.** For an invertible sheaf of
> `𝒪`-modules `L` on a ringed site the evaluation pairing `SheafHom(L, 𝒪) ⊗_𝒪 L ⟶ 𝒪` is an
> isomorphism.
>
> The dual is a left dual of `L` by `exactPairingDualSheafOfIsInvertible`, and the evaluation of an
> exact pairing is an isomorphism whenever tensoring on the right by the first object is an
> equivalence, which for an invertible sheaf of modules it is.
>
> A ringed space is a ringed site, so this is also the evaluation clause of Tag 01CT (2); see
> `Stacks.SheafOfModules.isIso_evaluation_of_isInvertible` for that reading.

```lean
theorem isIso_evaluation [IsInvertible 𝒪 h𝒪 L] : IsIso (evaluation 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.Invertible.isIso_tensorSheafBraiding_hom_comp_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L277). The attribute's comment: “part (2)”. References: EGA 0 (5.4.3), “more general”.

> **Stacks Project, Tag 040A (2) and Tag 01CT (2), the evaluation clause in the order the tags
> write it.** The evaluation map `L ⊗_𝒪 SheafHom(L, 𝒪) ⟶ 𝒪` is an isomorphism. It is the canonical
> pairing of `Stacks.SheafOfModules.evaluation`, whose factors come in the order Tag 0FNV writes
> them, preceded by the braiding of the tensor product sheaf, which is what exchanges the two
> factors; in this order it is the trivializing pairing identifying `L^∨` as a tensor inverse of
> `L`.

```lean
theorem isIso_tensorSheafBraiding_hom_comp_evaluation [IsInvertible 𝒪 h𝒪 L] :
    IsIso ((tensorSheafBraiding 𝒪 h𝒪 L (dualSheaf 𝒪 h𝒪 L)).hom ≫ evaluation 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.Invertible.isInvertible_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L287). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 040A (2) and Tag 01CT (2), the invertibility clause.** The dual
> `L^∨ = SheafHom(L, 𝒪)` of an invertible sheaf of `𝒪`-modules is again invertible: the evaluation
> pairing is an isomorphism `L^∨ ⊗_𝒪 L ≅ 𝒪`, which is Tag 0B8K (2) for `L^∨`.

```lean
theorem isInvertible_dualSheaf [IsInvertible 𝒪 h𝒪 L] :
    IsInvertible 𝒪 h𝒪 (dualSheaf 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.tensorProduct_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean#L474). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 01CT (1), Tag 040A (1).** The tensor product of two invertible sheaves
> of modules is invertible.

```lean
theorem tensorProduct_isInvertible
    (L N : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] [IsInvertible O hO N] :
    IsInvertible O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L)).obj N)
```

## Tag 040B, a lemma

[Tag 040B](https://stacks.math.columbia.edu/tag/040B) in the Stacks Project.

**`Stacks.SheafOfModules.essentiallySmall_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/EssentiallySmall/Invertible.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/EssentiallySmall/Invertible.lean#L249).

> **Stacks 040B.** The invertible sheaves of modules on a ringed site form an essentially
> small class: there is a set of invertible modules such that every invertible module is
> isomorphic to exactly one of them. Equivalently, the isomorphism classes of invertible
> `O`-modules form a set of size `max u v w`.
>
> The two instance hypotheses are the standing hypotheses of the invertible-module API of this
> development — they are what makes the sheafified tensor product and the locally bijective
> pairing of Tag 0B8N available — and they are satisfied wherever Tag 01CX builds the Picard
> group.

```lean
theorem essentiallySmall_isInvertible
    (O : Cᵒᵖ ⥤ CommRingCat.{w})
    (hO : Presheaf.IsSheaf J (Stacks.SheafOfModules.TensorSheafification.structureRingPresheaf O)) :
    ObjectProperty.EssentiallySmall.{max u v w} (IsInvertible O hO)
```

## Tag 040C, a definition

[Tag 040C](https://stacks.math.columbia.edu/tag/040C) in the Stacks Project.

**`Stacks.SheafOfModules.Picard.PicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L170). The attribute's comment: “the Picard group”. References: EGA IV (21.3.2), “Pic(X) definition”; SGA 6 X (5.1), “Pic(X) definition”.

> The Picard group of `O`: the group of isomorphism classes of
> invertible sheaves of `O`-modules, as a small type.

```lean
noncomputable def PicardGroup : Type (max (max u v) w)
```

**`Stacks.SheafOfModules.Picard.instAddCommGroupPicardGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L176). The attribute's comment: “abelian group structure”.

> The abelian group structure on the Picard group; its addition is the tensor product sheaf,
> by `classOf_tensor`.

```lean
noncomputable instance instAddCommGroupPicardGroup : AddCommGroup (PicardGroup O hO)
```

**`Stacks.SheafOfModules.Picard.classOf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L181). The attribute's comment: “class of an invertible module”. References: EGA IV (21.3.2), “cl(L)”.

> The class in the Picard group of an invertible sheaf of modules.

```lean
noncomputable abbrev classOf (L : SheafOfModules.{w}
  (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    (hL : IsInvertible O hO L) : PicardGroup O hO
```

**`Stacks.SheafOfModules.Picard.classOf_eq_classOf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L200). The attribute's comment: “elements are isomorphism classes of invertible modules”. References: EGA IV (21.3.2), “cl(L)=cl(L') iff iso”.

> Two invertible sheaves of modules determine the same Picard class exactly when they are
> isomorphic, so the elements of the Picard group are the isomorphism classes.

```lean
theorem classOf_eq_classOf_iff (L N : SheafOfModules.{w}
  (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    (hL : IsInvertible O hO L) (hN : IsInvertible O hO N) :
    classOf O hO L hL = classOf O hO N hN ↔ Nonempty (L ≅ N)
```

**`Stacks.SheafOfModules.Picard.classOf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L211). The attribute's comment: “addition is tensor product”.

> Addition in the Picard group is the tensor product sheaf.

```lean
theorem classOf_tensor (L N : SheafOfModules.{w}
  (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    (hL : IsInvertible O hO L) (hN : IsInvertible O hO N)
    (hLN : IsInvertible O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
        (L)).obj (N)))) :
    classOf O hO L hL + classOf O hO N hN =
      classOf O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
          (L)).obj (N))) hLN
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.32, Tag 0408](https://stacks.math.columbia.edu/tag/0408)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
