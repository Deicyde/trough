---
declaration: section
origin: cited
lean: CategoryTheory.TwoFibreProductOver.FstFiber.objEquiv, CategoryTheory.TwoFibreProductOver.FstFiber.homEquiv, CategoryTheory.TwoFibreProductOver.fst_isFiberedInGroupoids, Stacks.RepresentableMorphism.IsRepresentableMorphism, Stacks.RepresentableMorphism.inducedFiberFunctor_faithful_of_isRepresentableMorphism, CategoryTheory.isRepresentableMorphism_of_faithful_of_isRepresentable, Stacks.RepresentableMorphism.isRepresentableMorphism_diagonal_iff
statement: formalized
proof: formalized
---

# 4.42 Representable 1-morphisms

Section 4.42 of the Stacks Project, [Tag 02Y4](https://stacks.math.columbia.edu/tag/02Y4). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02Y5, a lemma

[Tag 02Y5](https://stacks.math.columbia.edu/tag/02Y5) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.FstFiber.objEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Fibres.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Fibres.lean#L117). The attribute's comment: “(1)”.

> **Stacks 02Y5 (1).**
> The objects of the fibre category of `(𝒞/U) ×_𝒴 𝒳` over an object `f : V ⟶ U` of `𝒞/U` are the
> pairs `(x, φ)` consisting of an object `x` of the fibre `𝒳_V` and a morphism
> `φ : G(f) ⟶ F(x)` of the fibre `𝒴_V`.

```lean
noncomputable def objEquiv (h𝒴 : p𝒴.IsFiberedInGroupoids) :
    (fst (Over.forget U) p𝒳 p𝒴 G F).Fiber f ≃
      Σ x : p𝒳.Fiber f.left, {φ : G.obj f ⟶ F.obj x.1 // p𝒴.IsHomLift (𝟙 f.left) φ}
```

**`CategoryTheory.TwoFibreProductOver.FstFiber.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Fibres.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Fibres.lean#L188). The attribute's comment: “(2)”.

> **Stacks 02Y5 (2).**
> The morphisms of the fibre category of `(𝒞/U) ×_𝒴 𝒳` over an object `f : V ⟶ U` of `𝒞/U` between
> two objects `(x, φ)` and `(x', φ')` are exactly the morphisms `ψ : x ⟶ x'` of the fibre `𝒳_V`
> with `F(ψ) = φ' ∘ φ⁻¹`.

```lean
def homEquiv (A B : (fst (Over.forget U) p𝒳 p𝒴 G F).Fiber f) :
    (A ⟶ B) ≃ {ψ : A.1.y ⟶ B.1.y // p𝒳.IsHomLift (𝟙 f.left) ψ ∧
      F.map ψ = (phiIso A).inv ≫ (phiIso B).hom}
```

## Tag 02Y6, a lemma

[Tag 02Y6](https://stacks.math.columbia.edu/tag/02Y6) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.fst_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/SliceProduct.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/SliceProduct.lean#L77).

> **Stacks 02Y6.** Let `𝒳`, `𝒴` be categories fibred in groupoids over `𝒞`, let `F : 𝒳 ⥤ 𝒴` and
> `G : 𝒞/U ⥤ 𝒴` be 1-morphisms over `𝒞`. Then the first projection of the 2-fibre product
> `(𝒞/U) ×_𝒴 𝒳 ⟶ 𝒞/U` is a category fibred in groupoids over the slice `𝒞/U`.

```lean
theorem TwoFibreProductOver.fst_isFiberedInGroupoids (U : 𝒞) (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞)
    (F : 𝒳 ⥤ 𝒴) (G : Over U ⥤ 𝒴)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hF : F ⋙ p𝒴 = p𝒳) (hG : G ⋙ p𝒴 = Over.forget U) :
    (TwoFibreProductOver.fst (Over.forget U) p𝒳 p𝒴 G F).IsFiberedInGroupoids
```

## Tag 02Y7, a definition

[Tag 02Y7](https://stacks.math.columbia.edu/tag/02Y7) in the Stacks Project.

**`Stacks.RepresentableMorphism.IsRepresentableMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/FibreFunctors.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/FibreFunctors.lean#L142).

> **Stacks 02Y7.** `F : 𝒳 ⥤ 𝒴` (a 1-morphism over `𝒞`) is *representable*, equivalently
> `𝒳` is *relatively representable over* `𝒴`, when for every object `U` of `𝒞` and every
> 1-morphism `G : 𝒞/U ⥤ 𝒴` over `𝒞` (i.e. `G ⋙ q = Over.forget U`), the first projection
> `(𝒞/U) ×_𝒴 𝒳 ⥤ 𝒞/U` of the 2-fibre product over `𝒞` is a representable category fibred in
> groupoids.
>
> The source states this for `𝒳`, `𝒴` fibred in groupoids over `𝒞`; the predicate here does
> not assume that, so it is the same condition stated for an arbitrary 1-morphism and
> specialises to the source's notion.

```lean
def IsRepresentableMorphism (p : 𝒳 ⥤ 𝒞) (q : 𝒴 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒴) : Prop
```

## Tag 02Y8, a lemma

[Tag 02Y8](https://stacks.math.columbia.edu/tag/02Y8) in the Stacks Project.

**`Stacks.RepresentableMorphism.inducedFiberFunctor_faithful_of_isRepresentableMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/FibreFunctors.lean, line 770](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/FibreFunctors.lean#L770).

> **Stacks 02Y8** (Lemma 4.42.4), the stated implication. If `F : 𝒳 ⥤ 𝒴` is a representable
> 1-morphism over `𝒞` between categories fibred in groupoids, then for every object `U` of `𝒞` the
> induced functor on fibre categories `F_U : 𝒳_U ⥤ 𝒴_U` is faithful. The converse is not proved
> here.

```lean
theorem inducedFiberFunctor_faithful_of_isRepresentableMorphism
    (p : 𝒳 ⥤ 𝒞) (q : 𝒴 ⥤ 𝒞)
    (hq : q.IsFiberedInGroupoids)
    (F : 𝒳 ⥤ 𝒴) (hF : F ⋙ q = p)
    (hrep : IsRepresentableMorphism p q F) (U : 𝒞) :
    (inducedFiberFunctor p q F hF U).Faithful
```

## Tag 02Y9, a lemma

[Tag 02Y9](https://stacks.math.columbia.edu/tag/02Y9) in the Stacks Project.

**`CategoryTheory.isRepresentableMorphism_of_faithful_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/MorphismCriterion.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/MorphismCriterion.lean#L46).

> Let `𝒳`, `𝒴` be categories fibred in groupoids over `𝒞`, let `F : 𝒳 ⥤ 𝒴` be a 1-morphism
> over `𝒞` and let `c` be a choice of pullbacks for `𝒴`. If every functor `F_U : 𝒳_U ⥤ 𝒴_U` on
> fibre categories is faithful, and if for every `U` and every object `y` of `𝒴_U` the presheaf on
> `𝒞/U` of isomorphism classes of pairs `(x, φ : f^* y ⟶ F(x))` is representable, then `F` is a
> representable 1-morphism in the sense of Stacks 02Y7.

```lean
theorem isRepresentableMorphism_of_faithful_of_isRepresentable (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞)
    (F : 𝒳 ⥤ 𝒴) (hF : F ⋙ p𝒴 = p𝒳) (h𝒳 : p𝒳.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (c : p𝒴.ChoiceOfPullbacks)
    (hfaithful : ∀ U : 𝒞, (Stacks.RepresentableMorphism.inducedFiberFunctor p𝒳 p𝒴 F hF U).Faithful)
    (hrepresentable : ∀ (U : 𝒞) (y : p𝒴.Fiber U),
      (PairIsoClass.presheaf F c y h𝒳 h𝒴 hF).IsRepresentable) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism p𝒳 p𝒴 F
```

## Tag 02YA, a lemma

[Tag 02YA](https://stacks.math.columbia.edu/tag/02YA) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_diagonal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/DiagonalRepresentable.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/DiagonalRepresentable.lean#L327).

> **Stacks 02YA.** Let `𝒞` be a category with products of pairs and fibre products, and let
> `p : 𝒮 ⥤ 𝒞` be a category fibred in groupoids. The diagonal `𝒮 ⥤ 𝒮 × 𝒮` into the 2-fibre product
> `𝒮 × 𝒮 = 𝒮 ×_𝒞 𝒮` over the final object `𝟭 𝒞` (Stacks 0040) is representable (Stacks 02Y7) if and
> only if, for every object `U` of `𝒞`, every 1-morphism `G : 𝒞/U ⥤ 𝒮` is representable.
>
> The morphisms of `𝒞` and of `𝒮` are taken in one universe.

```lean
theorem isRepresentableMorphism_diagonal_iff [HasBinaryProducts 𝒞] [HasPullbacks 𝒞]
    (hp : p.IsFiberedInGroupoids) :
    IsRepresentableMorphism p (structureFunctor p p (𝟭 𝒞) p p) (diagonal (Functor.comp_id p)) ↔
      ∀ (U : 𝒞) (G : Over U ⥤ 𝒮), G ⋙ p = Over.forget U →
        IsRepresentableMorphism (Over.forget U) p G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.42, Tag 02Y4](https://stacks.math.columbia.edu/tag/02Y4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
