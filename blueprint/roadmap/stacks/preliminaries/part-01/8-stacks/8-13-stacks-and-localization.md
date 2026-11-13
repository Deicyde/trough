---
declaration: section
origin: cited
lean: CategoryTheory.Over.isStack_forget_iff_isSheaf, CategoryTheory.Over.isStack_of_isStack_comp_forget, CategoryTheory.Over.basedStackEquivStackPair, CategoryTheory.Functor.isStack_comp_forget, CategoryTheory.Over.stackConstructionHomEquiv, CategoryTheory.Over.stackConstructionHom₂Equiv
statement: formalized
proof: formalized
---

# 8.13 Stacks and localization

Section 8.13 of the Stacks Project, [Tag 04WT](https://stacks.math.columbia.edu/tag/04WT). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04WU, a lemma

[Tag 04WU](https://stacks.math.columbia.edu/tag/04WU) in the Stacks Project.

**`CategoryTheory.Over.isStack_forget_iff_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/OverIsStack.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/OverIsStack.lean#L312).

> Let `(𝒞, J)` be a site and let `U` be an object of `𝒞`. The localization `j_U : 𝒞/U ⥤ 𝒞` is a
> stack over `𝒞` if and only if the representable presheaf `h_U` is a sheaf.

```lean
theorem isStack_forget_iff_isSheaf (J : GrothendieckTopology 𝒞) :
    (Over.forget U).IsStack J ↔ Presheaf.IsSheaf J (yoneda.obj U)
```

## Tag 04WV, a lemma

[Tag 04WV](https://stacks.math.columbia.edu/tag/04WV) in the Stacks Project.

**`CategoryTheory.Over.isStack_of_isStack_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StackOfCompForget.lean, line 666](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/StackOfCompForget.lean#L666).

> **Construction B of Stacks 04WV, at the level of stacks, for an arbitrary site.** Let `U` be an
> object of `𝒞` whose representable presheaf `h_U` is a sheaf, and let `p : 𝒮 ⥤ 𝒞/U` be a functor
> whose composite with the localization functor `j_U` is a stack over `(𝒞, J)`. Then `p` itself is a
> stack over the site `(𝒞/U, J.over U)`. This is the source's "in this case it is automatically the
> case that `p : 𝒯 → 𝒞/U` is a stack over `𝒞/U`".
>
> No fibre products are assumed in `𝒞`: the proof checks the three conditions of Stacks 026F directly.
> A covering sieve of `A` in `𝒞/U` is `(overEquiv A).symm R'` for a covering sieve `R'` of `A.left` in
> `𝒞`, every object of `𝒞` mapping to `A.left` being automatically over `U`. Condition (1) is
> `CategoryTheory.Functor.isFibered_of_comp_forget`; condition (2) is
> `CategoryTheory.Over.isMorSheaf_of_isMorSheaf_comp_forget`, through the description of sheaves of
> morphisms by gluing; and for condition (3) a descent datum for `p` is read as the descent datum
> `CategoryTheory.Over.sliceDatum` for `p ⋙ j_U`, whose effectivity gives back that of the original
> one by `CategoryTheory.Over.isEffective_of_isEffective_sliceDatum`. **The sheaf hypothesis on `h_U`
> is used only there**, to see that the descended object lies over `A`. Compare
> `CategoryTheory.Over.isStack_of_comp_forget`, the same statement under `[HasPullbacks 𝒞]`.

```lean
theorem isStack_of_isStack_comp_forget (p : 𝒮 ⥤ Over U) {J : GrothendieckTopology 𝒞}
    (hU : Presheaf.IsSheaf J (yoneda.obj U)) (hq : (p ⋙ Over.forget U).IsStack J) :
    p.IsStack (J.over U)
```

**`CategoryTheory.Over.basedStackEquivStackPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StackOfCompForget.lean, line 733](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/StackOfCompForget.lean#L733).

> **Constructions A and B of Stacks 04WV are mutually inverse on objects**, for an arbitrary site
> `(𝒞, J)` and an object `U` whose representable presheaf is a sheaf. A pair `(𝒯, p)` carries no
> information beyond `p`, because "`p` is a 1-morphism of categories over `𝒞`" says exactly that the
> structure functor of `𝒯` is `p ⋙ j_U`; and the two stack conditions agree, by
> `CategoryTheory.Functor.isStack_comp_forget` in one direction and
> `CategoryTheory.Over.isStack_of_isStack_comp_forget` in the other.
>
> Together with `CategoryTheory.Over.stackConstructionHomEquiv` and
> `CategoryTheory.Over.stackConstructionHom₂Equiv`, which are bijections on 1-morphisms and on
> 2-morphisms compatible with identities, composition and whiskering, this exhibits Constructions A
> and B as mutually inverse functors of the two 2-categories.

```lean
def basedStackEquivStackPair :
    BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U) ≃ StackPair U J hU
```

**`CategoryTheory.Functor.isStack_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L249).

> **Construction A for stacks.** Let `U` be an object of `𝒞` whose representable presheaf `h_U`
> is a sheaf, and let `p : 𝒮 ⥤ 𝒞/U` be a stack over the site `(𝒞/U, J.over U)`. Then
> `j_! p = p ⋙ j_U : 𝒮 ⥤ 𝒞` is a stack over `(𝒞, J)`.

```lean
theorem isStack_comp_forget (p : 𝒳 ⥤ Over U) {J : GrothendieckTopology 𝒞}
    (hU : Presheaf.IsSheaf J (yoneda.obj U)) (hp : p.IsStack (J.over U)) :
    (p ⋙ Over.forget U).IsStack J
```

**`CategoryTheory.Over.stackConstructionHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L592).

> **Construction A is bijective on 1-morphisms**, and is the identity on the underlying
> functor.

```lean
def stackConstructionHomEquiv
    (𝒮 𝒮' : BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U)) :
    (𝒮 ⟶ 𝒮') ≃
      StackPairHom U J hU (stackConstructionA U J hU 𝒮) (stackConstructionA U J hU 𝒮')
```

**`CategoryTheory.Over.stackConstructionHom₂Equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/StacksAndLocalization.lean#L632).

> **Construction A is bijective on 2-morphisms**, and is the identity on the underlying morphism
> of functors.

```lean
def stackConstructionHom₂Equiv
    {𝒮 𝒮' : BasedStack.{v₁, v₁, max u₁ v₁, max u₁ v₁} (Over U) (J.over U)} (f g : 𝒮 ⟶ 𝒮') :
    (f ⟶ g) ≃ StackPairHom₂ U J hU (stackConstructionHomEquiv U J hU 𝒮 𝒮' f)
      (stackConstructionHomEquiv U J hU 𝒮 𝒮' g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.13, Tag 04WT](https://stacks.math.columbia.edu/tag/04WT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
