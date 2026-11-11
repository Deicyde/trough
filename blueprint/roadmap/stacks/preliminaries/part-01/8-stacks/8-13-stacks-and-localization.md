---
declaration: section
origin: cited
lean: CategoryTheory.Over.isStack_forget_iff_isSheaf, CategoryTheory.Functor.isStack_comp_forget, CategoryTheory.Over.stackConstructionHomEquiv, CategoryTheory.Over.stackConstructionHom₂Equiv, CategoryTheory.Over.isStack_of_comp_forget, CategoryTheory.Over.stackConstructionObjEquiv
statement: formalized
proof: formalized
---

# 8.13 Stacks and localization

Section 8.13 of the Stacks Project, [Tag 04WT](https://stacks.math.columbia.edu/tag/04WT). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04WU, a lemma

[Tag 04WU](https://stacks.math.columbia.edu/tag/04WU) in the Stacks Project.

**`CategoryTheory.Over.isStack_forget_iff_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/OverIsStack.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/OverIsStack.lean#L312).

> Let `(𝒞, J)` be a site and let `U` be an object of `𝒞`. The localization `j_U : 𝒞/U ⥤ 𝒞` is a
> stack over `𝒞` if and only if the representable presheaf `h_U` is a sheaf.

```lean
theorem isStack_forget_iff_isSheaf (J : GrothendieckTopology 𝒞) :
    (Over.forget U).IsStack J ↔ Presheaf.IsSheaf J (yoneda.obj U)
```

## Tag 04WV, a lemma

[Tag 04WV](https://stacks.math.columbia.edu/tag/04WV) in the Stacks Project.

**`CategoryTheory.Functor.isStack_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L246).

> **Construction A for stacks.** Let `U` be an object of `𝒞` whose representable presheaf `h_U`
> is a sheaf, and let `p : 𝒮 ⥤ 𝒞/U` be a stack over the site `(𝒞/U, J.over U)`. Then
> `j_! p = p ⋙ j_U : 𝒮 ⥤ 𝒞` is a stack over `(𝒞, J)`.

```lean
theorem isStack_comp_forget (p : 𝒳 ⥤ Over U) {J : GrothendieckTopology 𝒞}
    (hU : Presheaf.IsSheaf J (yoneda.obj U)) (hp : p.IsStack (J.over U)) :
    (p ⋙ Over.forget U).IsStack J
```

**`CategoryTheory.Over.stackConstructionHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L589).

> **Construction A is bijective on 1-morphisms**, and is the identity on the underlying
> functor.

```lean
def stackConstructionHomEquiv
    (𝒮 𝒮' : BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U)) :
    (𝒮 ⟶ 𝒮') ≃
      StackPairHom U J hU (stackConstructionA U J hU 𝒮) (stackConstructionA U J hU 𝒮')
```

**`CategoryTheory.Over.stackConstructionHom₂Equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L629).

> **Construction A is bijective on 2-morphisms**, and is the identity on the underlying morphism
> of functors.

```lean
def stackConstructionHom₂Equiv
    {𝒮 𝒮' : BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U)} (f g : 𝒮 ⟶ 𝒮') :
    (f ⟶ g) ≃ StackPairHom₂ U J hU (stackConstructionHomEquiv U J hU 𝒮 𝒮' f)
      (stackConstructionHomEquiv U J hU 𝒮 𝒮' g)
```

**`CategoryTheory.Over.isStack_of_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksOverSlice.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/StacksOverSlice.lean#L305).

> **Construction B of Stacks 04WV, at the level of stacks.** Let `U` be an object of `𝒞` whose
> representable presheaf `h_U` is a sheaf, and let `p : 𝒮 ⥤ 𝒞/U` be a functor whose composite with
> the localization functor `j_U` is a stack over `(𝒞, J)`. Then `p` itself is a stack over the site
> `(𝒞/U, J.over U)`. This is the source's "in this case it is automatically the case that
> `p : 𝒯 → 𝒞/U` is a stack over `𝒞/U`".
>
> The proof is by reduction to three results rather than by a clause-by-clause verification:
>
> * the pushforward `j_U^q 𝒮` of `q = p ⋙ j_U` along `j_U` is a stack over `(𝒞/U, J.over U)`, by
>   Stacks 04WC (`CategoryTheory.StrictPullback.isStack_structureFunctor`), `j_U` being a continuous
>   functor of sites;
> * the full subcategory of `j_U^q 𝒮` cut out by `CategoryTheory.Over.LiesOverSlice` is a stack, by
>   Stacks 04TU (`CategoryTheory.Functor.IsStack.fullSubcategory`); **this is the only place the
>   hypothesis that `h_U` is a sheaf is used**, in
>   `CategoryTheory.Over.locallyClosed_liesOverSlice`;
> * `𝒮` is isomorphic to that full subcategory as a category over `𝒞/U`, so it is a stack by
>   Stacks 042W (`CategoryTheory.BasedCategory.Equivalence.isStack`).
>
> Two costs of this route, both stated here rather than hidden.
>
> * It carries the hypothesis `[HasPullbacks 𝒞]`, which Stacks 04WV does not. It is inherited from
>   Stacks 04WC, whose proof genuinely uses fibre products in the source site
>   (`CategoryTheory.StrictPullback.glue`); the source's notion of a morphism of sites (Stacks 00WU)
>   asks for them, and Mathlib's `Functor.IsContinuous` does not. So this is Construction B for a
>   site with fibre products, which is a mild weakening of 04WV.
> * The universes are *not* pinned, and the earlier note here saying they were is superseded. The
>   pushforward lives in `Type (max u₁ v₁ u₂)` with morphisms in `max v₁ v₂`, and `𝒮` used to be
>   given there so that it and the full subcategory of the pushforward coincide; but the transport
>   of the stack condition does not need that, because `CategoryTheory.BasedCategory.Equivalence`
>   and Stacks 042W relate two categories over `𝒞` in independent object and morphism universes
>   (`CategoryTheory.BasedCategory.isStack_iff_of_equivalence`), and
>   `CategoryTheory.Over.toSliceFullSub` and `CategoryTheory.Over.fromSliceFullSub` are already
>   stated at the file's general `{𝒮 : Type u₂} [Category.{v₂} 𝒮]`. So the statement below is given
>   at that generality. The previously pinned case is recompiled as an instance of it, at the two
>   universe settings where it is used: `CategoryTheory.Over.isStack_map_iff` and
>   `CategoryTheory.Over.isStack_of_comp_forget_slice` keep their own statements unchanged and only
>   their explicit universe applications of this result move.

```lean
theorem isStack_of_comp_forget [HasPullbacks 𝒞] {𝒮 : Type u₂} [Category.{v₂} 𝒮]
    (p : 𝒮 ⥤ Over U) {J : GrothendieckTopology 𝒞}
    (hU : Presheaf.IsSheaf J (yoneda.obj U)) (hq : (p ⋙ Over.forget U).IsStack J) :
    p.IsStack (J.over U)
```

**`CategoryTheory.Over.stackConstructionObjEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksOverSlice.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/StacksOverSlice.lean#L425).

> **Constructions A and B of Stacks 04WV are mutually inverse on objects.** A pair `(𝒯, p)`
> carries no information beyond `p`, because "`p` is a 1-morphism of categories over `𝒞`" says
> exactly that the structure functor of `𝒯` is `p ⋙ j_U`; and the two stack conditions agree, by
> `CategoryTheory.Functor.isStack_comp_forget` in one direction and
> `CategoryTheory.Over.isStack_of_comp_forget` in the other.
>
> Together with `CategoryTheory.Over.stackConstructionHomEquiv` and
> `CategoryTheory.Over.stackConstructionHom₂Equiv`, which are bijections on 1-morphisms and on
> 2-morphisms compatible with identities, composition and whiskering, this exhibits Constructions A
> and B as mutually inverse functors of the two 2-categories.

```lean
def stackConstructionObjEquiv :
    BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U) ≃ StackPair U J hU
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.13, Tag 04WT](https://stacks.math.columbia.edu/tag/04WT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
