---
declaration: section
origin: cited
lean: CategoryTheory.TranslationDiagram.outerIso, CategoryTheory.nonempty_translationDiagram, CategoryTheory.surjective_inducedHom_tfae, CategoryTheory.surjective_inducedHom_tfae_of_fiberIso, CategoryTheory.inducedHom_comp_eq_one_iff_forall_isFiniteCoproductOfTerminal, CategoryTheory.comp_hom_eq_one_iff_forall_isFiniteCoproductOfTerminal, Stacks.FundamentalGroup.galoisExact_iff_categorical_conditions, Stacks.FundamentalGroup.galoisExact_iff_categorical_conditions_of_fiberIso
statement: formalized
proof: formalized
---

# 58.4 Functors and homomorphisms

Section 58.4 of the Stacks Project, [Tag 0BTQ](https://stacks.math.columbia.edu/tag/0BTQ). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BTR, an equation

[Tag 0BTR](https://stacks.math.columbia.edu/tag/0BTR) in the Stacks Project.

**`CategoryTheory.TranslationDiagram.outerIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TranslationDiagram.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TranslationDiagram.lean#L70). The attribute's comment: “the outer rectangle”.

> The outer rectangle of the diagram 2-commutes: restricting first along `h` and then along `h'`
> agrees with the composite functor `H ⋙ H'`.

```lean
public def outerIso (D : TranslationDiagram F F' F'' H H') :
    (PreGaloisCategory.functorToContAction F ⋙ ContAction.res FintypeCat D.left.hom) ⋙
        ContAction.res FintypeCat D.right.hom ≅
      H ⋙ H' ⋙ PreGaloisCategory.functorToContAction F''
```

**`CategoryTheory.nonempty_translationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TranslationDiagram.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TranslationDiagram.lean#L83). The attribute's comment: “the two 2-commutative squares”.

> Two composable exact functors between Galois categories admit fibre-functor isomorphisms whose
> induced continuous homomorphisms fit into a 2-commutative diagram over the categories of finite
> continuous actions.

```lean
public theorem nonempty_translationDiagram
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w}) (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H : C ⥤ C') (H' : C' ⥤ C'')
    (hH : exactFunctor C C' H) (hH' : exactFunctor C' C'' H') :
    Nonempty (TranslationDiagram F F' F'' H H')
```

## Tag 0BN6, a lemma

[Tag 0BN6](https://stacks.math.columbia.edu/tag/0BN6) in the Stacks Project.

**`CategoryTheory.surjective_inducedHom_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Surjectivity.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Surjectivity.lean#L325). References: SGA 1 V (6.9), “more general”; SGA 1 V (6.10), “a) <=> fully faithful”.

> The five characterizations of surjectivity of the homomorphism induced by an exact functor
> between Galois categories.

```lean
public theorem surjective_inducedHom_tfae
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (H : C ⥤ C') (_hH : exactFunctor C C' H) (t : H ⋙ F' ≅ F)
    (d : GaloisFunctorData F F' H t)
    (star : C) (star' : C') (hstar : IsTerminal star) (hstar' : IsTerminal star')
    (hHstar : IsTerminal (H.obj star)) :
    List.TFAE
      [ Function.Surjective d.hom,
        Nonempty H.FullyFaithful,
        ∀ X : C, PreGaloisCategory.IsConnected X →
          PreGaloisCategory.IsConnected (H.obj X),
        ∀ X : C, PreGaloisCategory.IsConnected X →
          Nonempty (star' ⟶ H.obj X) → Nonempty (star ⟶ X),
        ∀ X : C, Function.Bijective (mapFromTerminal H hstar' hHstar X) ]
```

**`CategoryTheory.surjective_inducedHom_tfae_of_fiberIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Surjectivity.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Surjectivity.lean#L369). References: SGA 1 V (6.9), “more general”; SGA 1 V (6.10), “a) <=> fully faithful”.

> The five characterizations of surjectivity of the homomorphism induced by an exact functor
> between Galois categories.
>
> This is the form of the statement in which nothing beyond the exact functor `H`, the two Galois
> categories and their chosen final objects is assumed: the continuous homomorphism of the
> functoriality diagram is the one produced from the fibre-functor isomorphism `t`, and the
> image of the chosen final object is seen to be final using exactness of `H`.

```lean
public theorem surjective_inducedHom_tfae_of_fiberIso
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (H : C ⥤ C') (hH : exactFunctor C C' H) (t : H ⋙ F' ≅ F)
    (star : C) (star' : C') (hstar : IsTerminal star) (hstar' : IsTerminal star') :
    List.TFAE
      [ Function.Surjective (galoisFunctorDataOfFiberIso F F' H t).hom,
        Nonempty H.FullyFaithful,
        ∀ X : C, PreGaloisCategory.IsConnected X →
          PreGaloisCategory.IsConnected (H.obj X),
        ∀ X : C, PreGaloisCategory.IsConnected X →
          Nonempty (star' ⟶ H.obj X) → Nonempty (star ⟶ X),
        ∀ X : C, Function.Bijective
          (mapFromTerminal H hstar' (isTerminalObjOfExactFunctor H hH hstar) X) ]
```

## Tag 0BS8, a lemma

[Tag 0BS8](https://stacks.math.columbia.edu/tag/0BS8) in the Stacks Project.

**`CategoryTheory.inducedHom_comp_eq_one_iff_forall_isFiniteCoproductOfTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/InducedHomTrivialComposite.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/InducedHomTrivialComposite.lean#L50). The attribute's comment: “for every choice of fibre-functor isomorphisms; continuity of the induced homomorphisms and the 2-commutative squares are constructed, not assumed”. References: SGA 1 V (6.5), “more general”.

> **Stacks Project, Tag 0BS8.** Let `H : C ⥤ C'` and `H' : C' ⥤ C''` be functors between
> Galois categories with fibre functors `F`, `F'`, `F''`, and let `t : H ⋙ F' ≅ F` and
> `t' : H' ⋙ F'' ≅ F'` be isomorphisms of fibre functors, with induced homomorphisms
> `h : Aut F' →* Aut F` and `h' : Aut F'' →* Aut F'`. Then `h ∘ h'` is trivial if and only if every
> object in the image of `H ⋙ H'` is a finite coproduct of terminal objects.

```lean
public theorem inducedHom_comp_eq_one_iff_forall_isFiniteCoproductOfTerminal
    {C : Type u} [Category.{v} C] {C' : Type u'} [Category.{v'} C']
    {C'' : Type u''} [Category.{v''} C'']
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w}) (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H : C ⥤ C') (H' : C' ⥤ C'') (t : H ⋙ F' ≅ F) (t' : H' ⋙ F'' ≅ F') :
    (inducedHom F F' H t).comp (inducedHom F' F'' H' t') = 1 ↔
      ∀ X : C, IsFiniteCoproductOfTerminal ((H ⋙ H').obj X)
```

**`CategoryTheory.comp_hom_eq_one_iff_forall_isFiniteCoproductOfTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TrivialComposite.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/TrivialComposite.lean#L180). References: SGA 1 V (6.5).

> The composite homomorphism associated to two successive functors of Galois categories is
> trivial exactly when every object in the image of the composite functor is a finite coproduct of
> terminal objects.

```lean
public theorem comp_hom_eq_one_iff_forall_isFiniteCoproductOfTerminal
    {C : Type u} [Category.{v} C] {C' : Type u'} [Category.{v'} C']
    {C'' : Type u''} [Category.{v''} C'']
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H : C ⥤ C') (H' : C' ⥤ C'')
    (t : H ⋙ F' ≅ F) (t' : H' ⋙ F'' ≅ F')
    (d : GaloisFunctorData F F' H t)
    (d' : GaloisFunctorData F' F'' H' t') :
    d.hom.toMonoidHom.comp d'.hom.toMonoidHom = 1 ↔
      ∀ X : C, IsFiniteCoproductOfTerminal ((H ⋙ H').obj X)
```

## Tag 0BS9, a lemma

[Tag 0BS9](https://stacks.math.columbia.edu/tag/0BS9) in the Stacks Project.

**`Stacks.FundamentalGroup.galoisExact_iff_categorical_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryExactSequence.lean, line 725](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryExactSequence.lean#L725).

> **Stacks 0BS9.** For composable exact functors between Galois categories, exactness of the
> induced sequence of automorphism groups is equivalent both to the essential-image criterion and to
> its epimorphic-cover variant.

```lean
theorem galoisExact_iff_categorical_conditions
    {C : Type u} [Category.{v} C]
    {C' : Type u'} [Category.{v'} C']
    {C'' : Type u''} [Category.{v''} C'']
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H : C ⥤ C') (H' : C' ⥤ C'')
    (_hH : exactFunctor C C' H) (_hH' : exactFunctor C' C'' H')
    (t : H ⋙ F' ≅ F) (t' : H' ⋙ F'' ≅ F')
    (d : GaloisFunctorData F F' H t)
    (d' : GaloisFunctorData F' F'' H' t') :
    List.TFAE
      [ IsExactSequence d'.hom d.hom,
        Nonempty H.FullyFaithful ∧
          ∀ X' : C',
            (H.essImage X' ↔ IsFiniteCoproductOfTerminal (H'.obj X')),
        Nonempty H.FullyFaithful ∧
          (∀ X : C, IsFiniteCoproductOfTerminal ((H ⋙ H').obj X)) ∧
          (∀ X' : C', IsFiniteCoproductOfTerminal (H'.obj X') →
            ∃ (X : C) (f : H.obj X ⟶ X'), Epi f) ]
```

**`Stacks.FundamentalGroup.galoisExact_iff_categorical_conditions_of_fiberIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryExactSequence.lean, line 798](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryExactSequence.lean#L798).

> **Stacks 0BS9.** For composable exact functors between Galois categories, exactness of the
> induced sequence of automorphism groups is equivalent both to the essential-image criterion and to
> its epimorphic-cover variant.
>
> This is the form of the statement in which no part of the functoriality data is assumed: the two
> continuous homomorphisms are the ones produced from the fibre-functor isomorphisms `t` and `t'`,
> whose continuity and whose 2-isomorphisms of the two functoriality squares are constructed by
> `CategoryTheory.galoisFunctorDataOfFiberIso`.

```lean
theorem galoisExact_iff_categorical_conditions_of_fiberIso
    {C : Type u} [Category.{v} C]
    {C' : Type u'} [Category.{v'} C']
    {C'' : Type u''} [Category.{v''} C'']
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H : C ⥤ C') (H' : C' ⥤ C'')
    (hH : exactFunctor C C' H) (hH' : exactFunctor C' C'' H')
    (t : H ⋙ F' ≅ F) (t' : H' ⋙ F'' ≅ F') :
    List.TFAE
      [ IsExactSequence (galoisFunctorDataOfFiberIso F' F'' H' t').hom
          (galoisFunctorDataOfFiberIso F F' H t).hom,
        Nonempty H.FullyFaithful ∧
          ∀ X' : C',
            (H.essImage X' ↔ IsFiniteCoproductOfTerminal (H'.obj X')),
        Nonempty H.FullyFaithful ∧
          (∀ X : C, IsFiniteCoproductOfTerminal ((H ⋙ H').obj X)) ∧
          (∀ X' : C', IsFiniteCoproductOfTerminal (H'.obj X') →
            ∃ (X : C) (f : H.obj X ⟶ X'), Epi f) ]
```

## Tag 0BN7, a lemma

[Tag 0BN7](https://stacks.math.columbia.edu/tag/0BN7) in the Stacks Project.

**`CategoryTheory.injective_inducedHom_iff_exists_epi_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Injectivity.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Injectivity.lean#L134). References: SGA 1 V (6.8).

> The induced homomorphism is injective precisely when every connected target object admits
> an epimorphic cover that is a subobject of the image of a source object.

```lean
public theorem injective_inducedHom_iff_exists_epi_mono
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (H : C ⥤ C') (t : H ⋙ F' ≅ F)
    (d : GaloisFunctorData F F' H t) :
    Function.Injective d.hom ↔
      ∀ X'' : C', PreGaloisCategory.IsConnected X'' →
        ∃ (X' : C) (Y'' : C') (p : Y'' ⟶ X'') (i : Y'' ⟶ H.obj X'),
          Epi p ∧ Mono i
```

**`CategoryTheory.injective_inducedHom_iff_exists_epi_mono_of_fiberIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Injectivity.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/Injectivity.lean#L402). References: SGA 1 V (6.8).

> The induced homomorphism is injective precisely when every connected target object admits
> an epimorphic cover that is a subobject of the image of a source object.
>
> This is the form of the statement in which no part of the functoriality data is assumed: the
> continuous homomorphism of the diagram is the one produced from the fibre-functor isomorphism
> `t`, whose continuity and whose 2-isomorphism of the functoriality square are constructed.

```lean
public theorem injective_inducedHom_iff_exists_epi_mono_of_fiberIso
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (H : C ⥤ C') (t : H ⋙ F' ≅ F) :
    Function.Injective (galoisFunctorDataOfFiberIso F F' H t).hom ↔
      ∀ X'' : C', PreGaloisCategory.IsConnected X'' →
        ∃ (X' : C) (Y'' : C') (p : Y'' ⟶ X'') (i : Y'' ⟶ H.obj X'),
          Epi p ∧ Mono i
```

## Tag 0BTS, a lemma

[Tag 0BTS](https://stacks.math.columbia.edu/tag/0BTS) in the Stacks Project.

**`CategoryTheory.normal_range_iff_connected_image_finite_coproduct_of_terminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/NormalImage.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FunctorsHomomorphisms/NormalImage.lean#L197).

> Normality of the image of the homomorphism induced by an exact functor of Galois categories
> is equivalent to the terminal-object criterion on images of connected objects.

```lean
public theorem normal_range_iff_connected_image_finite_coproduct_of_terminal
    {C' : Type u'} [Category.{v'} C'] {C'' : Type u''} [Category.{v''} C'']
    (F' : C' ⥤ FintypeCat.{w}) (F'' : C'' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F')]
    [IsGaloisCategory (setValuedFiberFunctor F'')]
    (H' : C' ⥤ C'')
    (t' : H' ⋙ F'' ≅ F') (d' : GaloisFunctorData F' F'' H' t') :
    (MonoidHom.range d'.hom.toMonoidHom).Normal ↔
      ∀ X' : C', PreGaloisCategory.IsConnected X' →
        (∃ Z : C'', Nonempty (IsTerminal Z) ∧ Nonempty (Z ⟶ H'.obj X')) →
          IsFiniteCoproductOfTerminal (H'.obj X')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.4, Tag 0BTQ](https://stacks.math.columbia.edu/tag/0BTQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
