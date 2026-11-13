---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.CoveringFamilies.IsCovering, Stacks.CategoryTheory.Hypercovering.CoveringFamilies.IsCoveringOver, Stacks.CategoryTheory.Hypercovering.IsSiteCovering.comp, Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.comp, Stacks.CategoryTheory.Hypercovering.IsSiteCovering.exists_hasPullback_pullback_snd, Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.exists_hasPullback_pullback_snd, Stacks.CategoryTheory.Hypercovering.IsSiteCovering.prod_map, Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.prod_map
statement: formalized
proof: formalized
---

# 25.3 Hypercoverings

Section 25.3 of the Stacks Project, [Tag 01FZ](https://stacks.math.columbia.edu/tag/01FZ). 8 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01G3, a definition

[Tag 01G3](https://stacks.math.columbia.edu/tag/01G3) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.CoveringFamilies.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean#L157). The attribute's comment: “the definition for SR(C)”.

> **Stacks Project, Tag 01G3.** A morphism of semi-representable objects is covering when
> every one of its fibre families is a covering family of the site. The target is allowed to be an
> arbitrary formal coproduct, as it is for a matching object.

```lean
abbrev IsCovering (Cov : CoveringFamilies.{s, w} C) {U : SetFamily.{w} C}
    {V : FormalCoproduct.{w + 1} C} (f : U.toFormalCoproduct ⟶ V) : Prop
```

**`Stacks.CategoryTheory.Hypercovering.CoveringFamilies.IsCoveringOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean#L164). The attribute's comment: “the definition for SR(C, X)”.

> **Stacks Project, Tag 01G3.** A morphism of semi-representable objects over `X` is covering
> when every one of its underlying fibre families is a covering family of the site.

```lean
abbrev IsCoveringOver (Cov : CoveringFamilies.{s, w} C)
    {X : C} {U : SetFamily.{w} (Over X)} {V : FormalCoproduct.{w + 1} (Over X)}
    (f : U.toFormalCoproduct ⟶ V) : Prop
```

## Tag 01G4, a lemma

[Tag 01G4](https://stacks.math.columbia.edu/tag/01G4) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.IsSiteCovering.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L122). The attribute's comment: “part (1), for `SR(C)`, over an arbitrary site”.

> **Stacks Project, Tag 01G4, part (1).** A composition of coverings in `SR(C)` is a
> covering.

```lean
theorem IsSiteCovering.comp (J : Precoverage C) [J.IsStableUnderComposition]
    {U V W : FormalCoproduct.{w} C} {f : U ⟶ V} {g : V ⟶ W}
    (hf : IsSiteCovering J f) (hg : IsSiteCovering J g) : IsSiteCovering J (f ≫ g)
```

**`Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L142). The attribute's comment: “part (1), for `SR(C, X)`, over an arbitrary site”.

> **Stacks Project, Tag 01G4, part (1)**, for `SR(C, X)`. A composition of coverings in
> `SR(C, X)` is a covering.

```lean
theorem IsSiteCoveringOver.comp (J : Precoverage C) [J.IsStableUnderComposition] {X : C}
    {U V W : FormalCoproduct.{w} (Over X)} {f : U ⟶ V} {g : V ⟶ W}
    (hf : IsSiteCoveringOver J f) (hg : IsSiteCoveringOver J g) :
    IsSiteCoveringOver J (f ≫ g)
```

**`Stacks.CategoryTheory.Hypercovering.IsSiteCovering.exists_hasPullback_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L218). The attribute's comment: “part (2), for `SR(C)`, over an arbitrary site”.

> **Stacks Project, Tag 01G4, part (2).** If `K ⟶ L` is a covering in `SR(C)` and `L' ⟶ L`
> is a morphism, then the fibre product `K ×_L L'` exists and its projection to `L'` is a
> covering.

```lean
theorem IsSiteCovering.exists_hasPullback_pullback_snd (J : Precoverage C) [J.HasIsos]
    [J.IsStableUnderComposition] [J.IsStableUnderBaseChange] [J.HasPullbacks]
    {K L L' : FormalCoproduct.{w} C} {f : K ⟶ L} (hf : IsSiteCovering J f) (g : L' ⟶ L) :
    ∃ _ : HasPullback f g, IsSiteCovering J (pullback.snd f g)
```

**`Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.exists_hasPullback_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L283). The attribute's comment: “part (2), for `SR(C, X)`, over an arbitrary site”.

> **Stacks Project, Tag 01G4, part (2)**, for `SR(C, X)`. If `K ⟶ L` is a covering in
> `SR(C, X)` and `L' ⟶ L` is a morphism, then the fibre product `K ×_L L'` exists and its
> projection to `L'` is a covering.

```lean
theorem IsSiteCoveringOver.exists_hasPullback_pullback_snd (J : Precoverage C) [J.HasIsos]
    [J.IsStableUnderComposition] [J.IsStableUnderBaseChange] [J.HasPullbacks] {X : C}
    {K L L' : FormalCoproduct.{w} (Over X)} {f : K ⟶ L} (hf : IsSiteCoveringOver J f)
    (g : L' ⟶ L) :
    ∃ _ : HasPullback f g, IsSiteCoveringOver J (pullback.snd f g)
```

**`Stacks.CategoryTheory.Hypercovering.IsSiteCovering.prod_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L297). The attribute's comment: “part (3), for `SR(C)`, over an arbitrary site with products of pairs”.

> **Stacks Project, Tag 01G4, part (3).** If `C` has products of pairs and `A ⟶ B`,
> `K ⟶ L` are coverings in `SR(C)`, then `A × K ⟶ B × L` is a covering. The products in `SR(C)`
> are those of `FormalCoproduct.instHasBinaryProducts` (Tag 01G2).

```lean
theorem IsSiteCovering.prod_map (J : Precoverage C) [J.HasIsos] [J.IsStableUnderComposition]
    [J.IsStableUnderBaseChange] [J.HasPullbacks] [HasBinaryProducts C]
    {A B K L : FormalCoproduct.{w} C} {f : A ⟶ B} {g : K ⟶ L}
    (hf : IsSiteCovering J f) (hg : IsSiteCovering J g) : IsSiteCovering J (prod.map f g)
```

**`Stacks.CategoryTheory.Hypercovering.IsSiteCoveringOver.prod_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SiteCovering.lean#L312). The attribute's comment: “part (3), for `SR(C, X)`, over an arbitrary site with fibre products”.

> **Stacks Project, Tag 01G4, part (3)**, for `SR(C, X)`. If `C` has fibre products and
> `A ⟶ B`, `K ⟶ L` are coverings in `SR(C, X)`, then `A × K ⟶ B × L` is a covering. The products
> in `SR(C, X)` are those of `FormalCoproduct.instHasBinaryProducts` (Tag 01G2) over the products
> of `Over X`, which are fibre products over `X`.

```lean
theorem IsSiteCoveringOver.prod_map (J : Precoverage C) [J.HasIsos]
    [J.IsStableUnderComposition] [J.IsStableUnderBaseChange] [HasPullbacks C] {X : C}
    {A B K L : FormalCoproduct.{w} (Over X)} {f : A ⟶ B} {g : K ⟶ L}
    (hf : IsSiteCoveringOver J f) (hg : IsSiteCoveringOver J g) :
    IsSiteCoveringOver J (prod.map f g)
```

## Tag 01G5, a definition

[Tag 01G5](https://stacks.math.columbia.edu/tag/01G5) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.CoveringFamilies.IsHypercovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoveringFamilies.lean#L186). References: SGA 4 V (7.3.3), “object case, no type p”.

> **Stacks Project, Tag 01G5.** A hypercovering of `X` for the site's covering families: the
> degree-zero family is one of the covering families of `X`, and all fibres of the successive
> matching morphisms are covering families of the site. The coskeleton is computed in formal
> coproducts, after including the set-indexed families.

```lean
abbrev IsHypercovering (Cov : CoveringFamilies.{s, w} C) {X : C}
    (K : SimplicialObject (SetFamily.{w} (Over X))) : Prop
```

## Tag 01G6, an example

[Tag 01G6](https://stacks.math.columbia.edu/tag/01G6) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isCoveringOver_terminal_from_power`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L286). The attribute's comment: “condition (1) of Definition 01G5, for the degree-zero term of the Čech object”.

> **Stacks Project, Tag 01G6**, condition (1) of Definition 01G5 for the Čech construction.
> If the family `U` covers `X` then so does its `α`-fold power for a one-element index type `α`,
> which is the degree-zero term of the Čech object of `U`: that term is `U` again, its component
> at `i` being a product of one copy of the component of `U` at `i default`.

```lean
theorem isCoveringOver_terminal_from_power (J : Pretopology C) {X : C}
    (U : FormalCoproduct.{w} (Over X)) (α : Type) [Unique α] [HasProductsOfShape α (Over X)]
    (hU : IsCoveringOver J (terminal.from U)) :
    IsCoveringOver J (terminal.from (U.power α))
```

**`Stacks.CategoryTheory.Hypercovering.IsCechHypercovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L328). The attribute's comment: “the definition of a Čech hypercovering”.

> **Stacks Project, Tag 01G6.** A simplicial object `K` of `SR(C, X)` is a *Čech
> hypercovering* of `X` when its degree-zero family `K_0` covers `X` and `K` is the zeroth
> coskeleton of `K_0`, that is, when `K` is isomorphic to `cosk₀ U` for a zero-truncated
> simplicial object `U` of `SR(C, X)`.

```lean
abbrev IsCechHypercovering (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X))) : Prop
```

**`Stacks.CategoryTheory.Hypercovering.IsCechHypercovering.isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L339). The attribute's comment: “condition (2) of Definition 01G5 by Tag 018B, hence the hypercovering property”.

> **Stacks Project, Tag 01G6**, condition (2) of Definition 01G5 and the hypercovering
> property. A Čech hypercovering of `X` is a hypercovering of `X`: its degree-zero family covers
> `X` by definition, and each of its matching morphisms is an isomorphism, hence covering, because
> `cosk₀ U` is `n`-coskeletal for every `n` (Tag 018B).

```lean
theorem IsCechHypercovering.isHypercovering {J : Pretopology C} {X : C}
    {K : SimplicialObject (FormalCoproduct.{w} (Over X))} (hK : IsCechHypercovering J K) :
    IsHypercovering J K
```

**`Stacks.CategoryTheory.Hypercovering.isCechHypercovering_cech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L363). The attribute's comment: “the Čech object of a covering family is a Čech hypercovering”.

> **Stacks Project, Tag 01G6.** The Čech object of a covering family of `X` is a Čech
> hypercovering of `X`: its degree-zero term is the covering family again, and it is
> `0`-coskeletal, hence isomorphic to the zeroth coskeleton of that term.

```lean
theorem isCechHypercovering_cech (J : Pretopology C) {X : C}
    (A : FormalCoproduct.{w} (Over X)) (hA : IsCoveringOver J (terminal.from A)) :
    let : HasTerminal (Over X) := Over.over_hasTerminal X
    let : HasBinaryProducts (Over X) :=
      Over.ConstructProducts.over_binaryProduct_of_pullback
    let : HasFiniteProducts (Over X) := hasFiniteProducts_of_has_binary_and_terminal
    IsCechHypercovering J A.cech
```

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_cech_of_isCoveringOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L383). The attribute's comment: “the Čech object of a covering family is a hypercovering”.

> **Stacks Project, Tag 01G6.** The Čech object of a covering family `{U_i → X}_{i ∈ I}` of `X`
> is a hypercovering of `X`. Its degree-`n` term is the family of the `(n + 1)`-fold fibre products
> `U_{i_0} ×_X ⋯ ×_X U_{i_n}` over `X`, indexed by `I^{n + 1}`; see `FormalCoproduct.cech_obj`,
> `FormalCoproduct.power_I` and `FormalCoproduct.power_obj`. The one-member case is
> `isHypercovering_cech`, Tag 0GMA.

```lean
theorem isHypercovering_cech_of_isCoveringOver (J : Pretopology C) {X : C}
    (A : FormalCoproduct.{w} (Over X)) (hA : IsCoveringOver J (terminal.from A)) :
    let : HasTerminal (Over X) := Over.over_hasTerminal X
    let : HasBinaryProducts (Over X) :=
      Over.ConstructProducts.over_binaryProduct_of_pullback
    let : HasFiniteProducts (Over X) := hasFiniteProducts_of_has_binary_and_terminal
    IsHypercovering J A.cech
```

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_cosk_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L409). The attribute's comment: “the hypercovering property in the `cosk₀` form”.

> **Stacks Project, Tag 01G6**, in the `cosk₀` shape in which the source states it: the zeroth
> coskeleton of a zero-truncated simplicial object of `SR(C, X)` is a hypercovering of `X` as soon
> as its degree-zero family covers `X`. The degree-zero family of `cosk₀ U` is `U` up to the
> isomorphism given by the counit of the coskeletal adjunction; the covering hypothesis is stated
> for `cosk₀ U` itself because a covering family of a pretopology need not stay covering under an
> arbitrary isomorphism of `SR(C, X)` — see the implementation notes.
>
> This is a convenience restatement, not the tag's assertion, and its hypothesis placement is not
> claimed to be optimal: the counit comparison at level `0` is a limit over a one-object,
> one-morphism indexing category, so it is of the objectwise shape that
> `isCoveringOver_terminal_from_of_objFun` transports, and stating the hypothesis on `U` itself is
> expected to be reachable by that route — it would need an explicit description of the pointwise
> right Kan extension at degree `0`, which is not developed here. For the covering family itself
> as the hypothesis, use `isHypercovering_cech_of_isCoveringOver`, which carries the source's own
> hypothesis and whose Čech object is `0`-coskeletal and therefore of this form.

```lean
theorem isHypercovering_cosk_zero (J : Pretopology C) {X : C}
    (U : SimplicialObject.Truncated (FormalCoproduct.{w} (Over X)) 0)
    (hU : IsCoveringOver J
      (terminal.from (((SimplicialObject.Truncated.cosk 0).obj U).obj (op ⦋0⦌)))) :
    IsHypercovering J ((SimplicialObject.Truncated.cosk 0).obj U)
```

**`Stacks.CategoryTheory.Hypercovering.isLimitWidePullbackConePowerObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L427). The attribute's comment: “the terms in `C`: each component is the fibre product over `X` of its factors”.

> **Stacks Project, Tag 01G6**, the terms clause read in `C`. The component at `i : α → I` of
> the `α`-fold power of the family `A = {U_i → X}` is a product taken in `Over X`; its underlying
> object of `C` is the fibre product over `X` of the `U_{i a}`. Precisely, the cone in `C` with
> apex that underlying object, projections the underlying morphisms of the product projections of
> `Over X` and base the structure morphism to `X`, is a limit of the wide cospan of the structure
> morphisms `U_{i a} → X`.
>
> Together with `FormalCoproduct.cech_obj`, `FormalCoproduct.power_I` and
> `FormalCoproduct.power_obj` this is the source's formula
> `K_n = {U_{i_0} ×_X ⋯ ×_X U_{i_n} → X}` indexed by `I^{n + 1}`: take `α = Fin (n + 1)`.

```lean
noncomputable def isLimitWidePullbackConePowerObj {X : C} (A : FormalCoproduct.{w} (Over X))
    (α : Type) [Finite α] :
    let : HasTerminal (Over X) := Over.over_hasTerminal X
    let : HasBinaryProducts (Over X) :=
      Over.ConstructProducts.over_binaryProduct_of_pullback
    let : HasFiniteProducts (Over X) := hasFiniteProducts_of_has_binary_and_terminal
    ∀ i : α → A.I, IsLimit (WidePullbackCone.mk (f := fun a ↦ (A.obj (i a)).hom)
      ((A.power α).obj i).hom (fun a ↦ (Pi.π (A.obj ∘ i) a).left)
      fun a ↦ Over.w (Pi.π (A.obj ∘ i) a))
```

Declarations registered for the tag:

- [`FormalCoproduct.cech_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FormalCoproduct.cech_obj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L451) (StacksFrontier): “the terms: the degree-`n` term is the `(n + 1)`-fold power”.
- [`FormalCoproduct.power_I`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FormalCoproduct.power_I#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L453) (StacksFrontier): “the terms: the index set `I^{n + 1}`”.
- [`FormalCoproduct.power_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FormalCoproduct.power_obj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Cech.lean#L454) (StacksFrontier): “the terms: the fibre product over `X` of the indexed components”.

## Tag 0GM9, an example

[Tag 0GM9](https://stacks.math.columbia.edu/tag/0GM9) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.associatedSimplicialObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/FromSimplicialObject.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/FromSimplicialObject.lean#L172). The attribute's comment: “the associated simplicial object”.

> **Stacks Project, Tag 0GM9.** The one-summand simplicial semi-representable object associated
> to an augmented simplicial object of the site.

```lean
def associatedSimplicialObject :
    SimplicialObject (FormalCoproduct.{w} (Over X))
```

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_associatedSimplicialObject_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/FromSimplicialObject.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/FromSimplicialObject.lean#L682). The attribute's comment: “the covering characterization”.

> **Stacks Project, Tag 0GM9.** The simplicial semi-representable object over `X` associated to
> an augmented simplicial object `U ⟶ X` is a hypercovering exactly when the augmentation in degree
> zero, the degree-one morphism to `U₀ ×_X U₀`, and every higher matching morphism generate a
> covering presieve of the site.

```lean
theorem isHypercovering_associatedSimplicialObject_iff (J : Pretopology C) :
    IsHypercovering J (associatedSimplicialObject U a) ↔
      (Presieve.singleton (a.app (Opposite.op (SimplexCategory.mk 0))) ∈ J X) ∧
      (Presieve.singleton (oneSimplexToFiberProduct U a) ∈
        J (pullback (a.app (Opposite.op (SimplexCategory.mk 0)))
          (a.app (Opposite.op (SimplexCategory.mk 0))))) ∧
      ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
        J ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj
          (Opposite.op (SimplexCategory.mk (n + 1)))).left)
```

## Tag 0GMA, an example

[Tag 0GMA](https://stacks.math.columbia.edu/tag/0GMA) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_cech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean#L211). The attribute's comment: “the hypercovering property”.

> **Stacks Project, Tag 0GMA.** The Čech object of a covering morphism is a hypercovering of
> its target.

```lean
theorem isHypercovering_cech (J : Pretopology C) {U X : C} (f : U ⟶ X)
    (hf : Presieve.singleton f ∈ J.coverings X) :
    let : HasTerminal (Over X) := Over.over_hasTerminal X
    let : HasBinaryProducts (Over X) :=
      Over.ConstructProducts.over_binaryProduct_of_pullback
    let : HasFiniteProducts (Over X) := hasFiniteProducts_of_has_binary_and_terminal
    IsHypercovering J ((FormalCoproduct.incl (Over X)).obj (Over.mk f)).cech
```

Declarations registered for the tag:

- [`FormalCoproduct.cech`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FormalCoproduct.cech#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean#L54) (StacksFrontier): “the Čech simplicial construction”.
- [`FormalCoproduct.cech_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FormalCoproduct.cech_obj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CechOfCovering.lean#L55) (StacksFrontier): “the terms”.

## Tag 01G7, a lemma

[Tag 01G7](https://stacks.math.columbia.edu/tag/01G7) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.small_hypercoverings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Small.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/Small.lean#L92).

> **Stacks Project, Tag 01G7.** Hypercoverings of an object of a site with
> fibre products form a set.

```lean
public theorem small_hypercoverings (Cov : CoveringFamilies.{s, w} C) (X : C) :
    Small.{max s u v w}
      {K : SimplicialObject (SetFamily.{w} (Over X)) //
        CoveringFamilies.IsHypercovering Cov K}
```

## Tag 01G9, a lemma

[Tag 01G9](https://stacks.math.columbia.edu/tag/01G9) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.locallySurjective_augmentation_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean, line 853](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean#L853). The attribute's comment: “part (1)”.

> The degree-zero augmentation of the simplicial presheaf associated to a hypercovering is
> locally surjective.

```lean
theorem locallySurjective_augmentation_of_isHypercovering
    (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K) :
    Presheaf.IsLocallySurjective J.toGrothendieck
      ((associatedAugmentedSimplicialPresheafOver K).hom.app
        (Opposite.op (SimplexCategory.mk 0)))
```

**`Stacks.CategoryTheory.Hypercovering.locallySurjective_oneMatchingMap_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean, line 880](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean#L880). The attribute's comment: “part (2)”.

> The map from one-simplices to the fibre product of two copies of the presheaf of vertices
> over the representable presheaf of `X` is locally surjective.

```lean
theorem locallySurjective_oneMatchingMap_of_isHypercovering
    (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K) :
    Presheaf.IsLocallySurjective J.toGrothendieck
      (oneMatchingMap (associatedAugmentedSimplicialPresheafOver K).left
        (associatedAugmentedSimplicialPresheafOver K).right
        (associatedAugmentedSimplicialPresheafOver K).hom)
```

**`Stacks.CategoryTheory.Hypercovering.locallySurjective_higherMatchingMap_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean, line 896](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocallySurjective.lean#L896). The attribute's comment: “part (3)”.

> Every higher matching map of the simplicial presheaf associated to a hypercovering is
> locally surjective.

```lean
theorem locallySurjective_higherMatchingMap_of_isHypercovering
    (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K) (n : ℕ) (hn : 1 ≤ n) :
    Presheaf.IsLocallySurjective J.toGrothendieck
      (((SimplicialObject.coskAdj n).unit.app
        (associatedAugmentedSimplicialPresheafOver K).left).app
          (Opposite.op (SimplexCategory.mk (n + 1))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.3, Tag 01FZ](https://stacks.math.columbia.edu/tag/01FZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
