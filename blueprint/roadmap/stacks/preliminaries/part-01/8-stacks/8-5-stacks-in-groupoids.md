---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsStackInGroupoids, CategoryTheory.Functor.stackInGroupoids_tfae, CategoryTheory.Functor.IsStack.isStackInGroupoids_stronglyCartesianOver, CategoryTheory.BasedCategory.isFiberedInGroupoids_and_isStack_iff_of_equivalence, CategoryTheory.StackInGroupoids, CategoryTheory.StackInGroupoids.bicategory, CategoryTheory.StackInGroupoids.homEquivBasedFunctor, CategoryTheory.StackInGroupoids.twoHomEquivBasedNatTrans
statement: formalized
proof: formalized
---

# 8.5 Stacks in groupoids

Section 8.5 of the Stacks Project, [Tag 02ZH](https://stacks.math.columbia.edu/tag/02ZH). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02ZI, a definition

[Tag 02ZI](https://stacks.math.columbia.edu/tag/02ZI) in the Stacks Project.

**`CategoryTheory.Functor.IsStackInGroupoids`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean#L236).

> A functor `p : 𝒮 ⥤ 𝒞` is a stack in groupoids over the site `(𝒞, J)` if
> 1. `p` is fibred in groupoids;
> 2. for all `x y` over `U`, the presheaf `Isom(x, y)` satisfies the sheaf condition for every
>    covering family of `J`, with overlaps given by fibre products; and
> 3. every descent datum relative to a covering family of `J` is effective.
>
> A covering family `{ f i : V i ⟶ U }` is one whose generated sieve `Sieve.ofArrows V f` lies in
> `J U`.

```lean
structure IsStackInGroupoids (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : Prop
```

## Tag 02ZJ, a lemma

[Tag 02ZJ](https://stacks.math.columbia.edu/tag/02ZJ) in the Stacks Project.

**`CategoryTheory.Functor.stackInGroupoids_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/GroupoidTFAE.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/GroupoidTFAE.lean#L100).

> **Stacks 02ZJ.** Let `(𝒞, J)` be a site and let `p : 𝒮 ⥤ 𝒞` be a category over `𝒞`. The
> following are equivalent:
> (1) `p` is a stack in groupoids over `𝒞`, that is `p` is fibred in groupoids, the presheaves
>     `Isom(x, y)` on `𝒞/U` are sheaves, and every descent datum relative to a covering is
>     effective (Stacks 02ZI);
> (2) `p` is a stack over `𝒞` and all its fibre categories are groupoids;
> (3) `p` is fibred in groupoids over `𝒞` and is a stack over `𝒞`.

```lean
public theorem stackInGroupoids_tfae (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) :
    List.TFAE
      [ ∃ h : p.IsFiberedInGroupoids,
          haveI : p.IsFibered := h.isFibered
          (∀ (U : 𝒞) (x y : p.Fiber U),
              Presheaf.IsSheaf (J.over U) (p.isomPresheaf x y)) ∧ p.HasEffectiveDescent J,
        p.IsStack J ∧ ∀ U : 𝒞, IsGroupoid (p.Fiber U),
        p.IsFiberedInGroupoids ∧ p.IsStack J ]
```

## Tag 03YI, a lemma

[Tag 03YI](https://stacks.math.columbia.edu/tag/03YI) in the Stacks Project.

**`CategoryTheory.Functor.IsStack.isStackInGroupoids_stronglyCartesianOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/GroupoidOfStack.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/GroupoidOfStack.lean#L421).

> **The category fibred in groupoids associated to a stack is a stack in groupoids.** Let
> `(𝒞, J)` be a site and let `p : 𝒮 ⥤ 𝒞` be a stack (Stacks 026F). Let `p' : 𝒮' ⥤ 𝒞` be the category
> fibred in groupoids associated to `𝒮` constructed in Stacks 03WQ: the objects of `𝒮'` are those
> of `𝒮`, its morphisms are the strongly cartesian morphisms of `𝒮`, and `p'` is the restriction
> of `p`. Then
> `p'` is a stack in groupoids (Stacks 02ZI): it is fibred in groupoids, its presheaves `Isom(x, y)`
> are sheaves, and every descent datum relative to a covering family of `J` is effective.

```lean
public theorem IsStack.isStackInGroupoids_stronglyCartesianOver
    {p : 𝒮 ⥤ 𝒞} {J : GrothendieckTopology 𝒞} (hp : p.IsStack J) :
    haveI : p.IsFibered := hp.isFibered
    haveI : (stronglyCartesianOver p).IsMultiplicative :=
      stronglyCartesianOver_isMultiplicative p
    IsStackInGroupoids.{w} (wideSubcategoryInclusion (stronglyCartesianOver p) ⋙ p) J
```

## Tag 042X, a lemma

[Tag 042X](https://stacks.math.columbia.edu/tag/042X) in the Stacks Project.

**`CategoryTheory.BasedCategory.isFiberedInGroupoids_and_isStack_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/GroupoidTransport.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/GroupoidTransport.lean#L119).

> **Stacks 042X**. Let `(𝒞, J)` be a site and let `𝒳`, `𝒴` be categories over `𝒞`. If `𝒳` and
> `𝒴` are equivalent as categories over `𝒞`, then `𝒳` is a stack in groupoids over `𝒞` if and only
> if `𝒴` is.
>
> "Stack in groupoids" is read as clause (3) of Stacks 02ZJ, fibred in groupoids together with being
> a stack, which is the reading 042X's proof uses; the two conjuncts transport by
> `BasedCategory.isFiberedInGroupoids_iff_of_equivalence` and by Stacks 042W,
> `BasedCategory.isStack_iff_of_equivalence`.

```lean
theorem BasedCategory.isFiberedInGroupoids_and_isStack_iff_of_equivalence
    (e : BasedCategory.Equivalence 𝒳 𝒴) (J : GrothendieckTopology 𝒞) :
    𝒳.p.IsFiberedInGroupoids ∧ 𝒳.p.IsStack J ↔
      𝒴.p.IsFiberedInGroupoids ∧ 𝒴.p.IsStack J
```

## Tag 02ZK, a definition

[Tag 02ZK](https://stacks.math.columbia.edu/tag/02ZK) in the Stacks Project.

**`CategoryTheory.StackInGroupoids`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean#L137). The attribute's comment: “(1)”.

> **Stacks 02ZK (1)**.
> An object of the 2-category of stacks in groupoids over the site `(𝒞, J)`: a category over `𝒞`
> whose structure functor is a stack in groupoids.

```lean
structure StackInGroupoids (𝒞 : Type u₁) [Category.{v₁} 𝒞] (J : GrothendieckTopology 𝒞)
```

**`CategoryTheory.StackInGroupoids.bicategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean#L153).

> **Stacks 02ZK**.
> The 2-category of stacks in groupoids over the site `(𝒞, J)`: the sub-2-category of the
> 2-category of stacks over `𝒞` (Stacks 02ZG) whose objects are the stacks in groupoids. Since
> every morphism of a category fibred in groupoids is strongly cartesian, no condition is imposed
> on a 1-morphism beyond being a functor over `𝒞` — see
> `CategoryTheory.StackInGroupoids.isFibredOneMorphism` — so this is the full sub-2-category of the
> 2-category `BasedCategory 𝒞` of categories over `𝒞` spanned by the stacks in groupoids.

```lean
instance StackInGroupoids.bicategory :
    Bicategory (StackInGroupoids.{w, v₁, v₂, u₁, u₂} 𝒞 J)
```

**`CategoryTheory.StackInGroupoids.homEquivBasedFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean#L167). The attribute's comment: “(2)”.

> **Stacks 02ZK (2)**.
> The 1-morphisms of the 2-category of stacks in groupoids are the functors over `𝒞`: a
> 1-morphism `𝒳 ⟶ 𝒴` is the same thing as a `BasedFunctor`, that is a functor `G` with
> `p' ∘ G = p`.

```lean
def homEquivBasedFunctor : (𝒳 ⟶ 𝒴) ≃ (𝒳.toBasedCategory ⥤ᵇ 𝒴.toBasedCategory)
```

**`CategoryTheory.StackInGroupoids.twoHomEquivBasedNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Groupoid.lean#L178). The attribute's comment: “(3)”.

> **Stacks 02ZK (3)**.
> The 2-morphisms of the 2-category of stacks in groupoids are the morphisms of functors whose
> components lie over identities: a 2-morphism `F ⟶ G` is the same thing as a `BasedNatTrans`,
> that is a morphism of functors `t` with `p'(t_x) = 𝟙 (p x)` for every object `x`.

```lean
def twoHomEquivBasedNatTrans {𝒳 𝒴 : StackInGroupoids.{w, v₁, v₂, u₁, u₂} 𝒞 J} (F G : 𝒳 ⟶ 𝒴) :
    (F ⟶ G) ≃ BasedNatTrans F.hom G.hom
```

## Tag 02ZL, a lemma

[Tag 02ZL](https://stacks.math.columbia.edu/tag/02ZL) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isStack_isFiberedInGroupoids_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/SetoidTwoFibreProduct.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/SetoidTwoFibreProduct.lean#L125).

> **Stacks 02ZL.** The 2-fibre product of stacks in groupoids over a site `(𝒞, J)` is a stack in
> groupoids: the construction of Stacks 0040 does not leave the 2-category of stacks in groupoids.
>
> "Stack in groupoids" is spelled out as its two conditions, being a stack over `(𝒞, J)` and being
> fibred in groupoids, because the library's `CategoryTheory.Functor.IsStackInGroupoids` is a second,
> unrelated rendering of the notion (see the implementation notes of
> `StacksFrontier.CategoryTheory.Sites.Stack.Setoid`). The first condition is Stacks 026G and the second
> is Stacks 0041; the hypotheses on `F` and `G` are only that they are strictly over `𝒞`, since a
> functor over `𝒞` into a category fibred in groupoids automatically preserves strongly cartesian
> morphisms.

```lean
theorem isStack_isFiberedInGroupoids_structureFunctor {J : GrothendieckTopology 𝒞}
    (h𝒳 : Functor.IsStack p𝒳 J) (h𝒴 : Functor.IsStack p𝒴 J) (h𝒮 : Functor.IsStack p𝒮 J)
    (g𝒳 : p𝒳.IsFiberedInGroupoids) (g𝒴 : p𝒴.IsFiberedInGroupoids)
    (g𝒮 : p𝒮.IsFiberedInGroupoids) (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) :
    Functor.IsStack (structureFunctor p𝒳 p𝒴 p𝒮 F G) J ∧
      (structureFunctor p𝒳 p𝒴 p𝒮 F G).IsFiberedInGroupoids
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.5, Tag 02ZH](https://stacks.math.columbia.edu/tag/02ZH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
