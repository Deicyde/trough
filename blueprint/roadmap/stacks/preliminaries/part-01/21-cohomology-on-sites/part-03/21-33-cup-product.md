---
declaration: section
origin: cited
lean: Stacks.Cohomology.CupProductAndDerivedPushforward.naiveCupProduct_relativeCupProduct, Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct_relativeCupProduct, Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_assoc, Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_braiding, Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_comp_pushforwardCompIso, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_comp_pushforwardCompIso, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_baseChange_square
statement: formalized
proof: formalized
---

# 21.33 Cup product

Section 21.33 of the Stacks Project, [Tag 0FPJ](https://stacks.math.columbia.edu/tag/0FPJ). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FPK, a lemma

[Tag 0FPK](https://stacks.math.columbia.edu/tag/0FPK) in the Stacks Project.

**`Stacks.Cohomology.CupProductAndDerivedPushforward.naiveCupProduct_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforward.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforward.lean#L298). The attribute's comment: “variant: the special case of a morphism of ringed topoi presented by a morphism of sites; the tag for an arbitrary morphism of ringed topoi is Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct\_relativeCupProduct”.

> **Stacks 0FPK, site-presented.**  For a morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` presented by a morphism of sites and
> unbounded cochain complexes `K`, `M` of `O_C`-modules, the hexagon
>
> ```
> f_*K ⊗^L_{O_D} f_*M ───────────→ Rf_*K ⊗^L_{O_D} Rf_*M
>         │                                 │
>         ↓                                 ↓
> Tot(f_*K ⊗_{O_D} f_*M)            Rf_*(K ⊗^L_{O_C} M)
>         │                                 │
>         ↓                                 ↓
> f_*Tot(K ⊗_{O_C} M) ───────────→ Rf_*Tot(K ⊗_{O_C} M)
> ```
>
> commutes in `D(O_D)`.  Its horizontal edges and its top right edge are the comparison
> `f_* ⟶ Rf_*`; the top left and bottom right edges are the canonical map from the derived tensor
> product to the ordinary total tensor complex of Stacks 06YU; the middle left edge is the naive
> cup product and the middle right edge is the relative cup product of Stacks 0B6C.

```lean
theorem naiveCupProduct_relativeCupProduct
    (K M : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    (canonicalDerivedTensorProduct Y.O).toTensor ((pushforwardComplex f).obj K)
          ((pushforwardComplex f).obj M) ≫
        DerivedCategory.Q.map (naiveCupProduct f hmos K M) ≫
        pushforwardComparisonQ f (HomologicalComplex.mapBifunctor K M
          (Stacks.SheafOfModules.Tensor.sheafTensor X.O) (ComplexShape.up ℤ)) =
      bifunctorMap (derivedTensorProductFunctor Y.O) (pushforwardComparisonQ f K)
            (pushforwardComparisonQ f M) ≫
        relativeCupProduct f hmos (DerivedCategory.Q.obj K) (DerivedCategory.Q.obj M) ≫
        (derivedPushforward f).map ((canonicalDerivedTensorProduct X.O).toTensor K M)
```

**`Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforwardOfToposHom.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforwardOfToposHom.lean#L279). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.\{u, u, u}, for all unbounded complexes K, M; the statement carries no hypothesis or class argument”.

> **Stacks 0FPK.**  For a morphism of ringed topoi `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` — a
> morphism of the underlying topoi together with the structure map, with no functor between the
> underlying sites — and unbounded cochain complexes `K`, `M` of `O_C`-modules, the hexagon
>
> ```
> f_*K ⊗^L_{O_D} f_*M ───────────→ Rf_*K ⊗^L_{O_D} Rf_*M
>         │                                 │
>         ↓                                 ↓
> Tot(f_*K ⊗_{O_D} f_*M)            Rf_*(K ⊗^L_{O_C} M)
>         │                                 │
>         ↓                                 ↓
> f_*Tot(K ⊗_{O_C} M) ───────────→ Rf_*Tot(K ⊗_{O_C} M)
> ```
>
> commutes in `D(O_D)`.  Its horizontal edges and its top right edge are the comparison
> `f_* ⟶ Rf_*`; the top left and bottom right edges are the canonical map from the derived tensor
> product to the ordinary total tensor complex of Stacks 06YU; the middle left edge is the naive
> cup product and the middle right edge is the relative cup product of Stacks 0B6C.
>
> The statement has no hypothesis and no class argument of its own: instance search supplies
> every class argument of `naiveCupProduct_relativeCupProduct_of_instances`.

```lean
theorem naiveCupProduct_relativeCupProduct {X Y : RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    (K M : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    (canonicalDerivedTensorProduct Y.O).toTensor ((pushforwardComplex f).obj K)
          ((pushforwardComplex f).obj M) ≫
        DerivedCategory.Q.map (naiveCupProduct f K M) ≫
        pushforwardComparisonQ f (HomologicalComplex.mapBifunctor K M
          (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} X.O) (ComplexShape.up ℤ)) =
      bifunctorMap (derivedTensorProductFunctor Y.O) (pushforwardComparisonQ f K)
            (pushforwardComparisonQ f M) ≫
        relativeCupProduct f (DerivedCategory.Q.obj K) (DerivedCategory.Q.obj M) ≫
        (derivedPushforward f).map ((canonicalDerivedTensorProduct X.O).toTensor K M)
```

## Tag 0FPL, a lemma

[Tag 0FPL](https://stacks.math.columbia.edu/tag/0FPL) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativityOfToposHom.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativityOfToposHom.lean#L181). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.\{u, u, u}, for all K, L, M in D(𝒪); the edges a are the associativity constraints derivedAssociator of Tag 0FPT and the statement has no hypothesis or class argument; the associativity law of the comparison of Tag 07A4, which the source's proof uses silently, is pullbackTensorComparisonAssociative”.

> **[Stacks, Tag 0FPL].**  The relative cup product of [Stacks, Tag 0B6C] is associative.  Let
> `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')` be a morphism of ringed topoi: a morphism of the underlying
> topoi together with the structure map.  Then for **all** `K`, `L`, `M` in `D(𝒪)` the square
>
> ```
> (Rf_*K ⊗' Rf_*L) ⊗' Rf_*M --→ Rf_*(K ⊗ L) ⊗' Rf_*M --→ Rf_*((K ⊗ L) ⊗ M)
>           |                                                     |
>           | a                                                   | Rf_*a
>           ↓                                                     ↓
> Rf_*K ⊗' (Rf_*L ⊗' Rf_*M) --→ Rf_*K ⊗' Rf_*(L ⊗ M) --→ Rf_*(K ⊗ (L ⊗ M))
> ```
>
> commutes in `D(𝒪')`.  The four unlabelled arrows are relative cup products in one or the other
> tensor factor; the two edges `a` are the associativity constraints `derivedAssociator` of
> `⊗^L_{𝒪'}` and `⊗^L_𝒪`, the associators of the monoidal structures of [Stacks, Tag 0FPT] whose
> tensor product is the derived tensor product of [Stacks, Tag 06YU] on the nose; they appear
> because the source draws its square with `⊗^L` strictly associative.
>
> The statement has no hypothesis and no class argument of its own.  The associativity law of the
> comparison of [Stacks, Tag 07A4] that the source's proof uses silently is
> `pullbackTensorComparisonAssociative`, proved above.

```lean
theorem relativeCupProduct_assoc {X Y : RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    (K L M : DerivedModules X.O) :
    (uncurriedDerivedTensor Y).map
          (relativeCupProduct f K L ×ₘ 𝟙 ((derivedPushforward f).obj M)) ≫
        relativeCupProduct f ((uncurriedDerivedTensor X).obj (K, L)) M ≫
          (derivedPushforward f).map (derivedAssociator X K L M).hom =
      (derivedAssociator Y ((derivedPushforward f).obj K) ((derivedPushforward f).obj L)
            ((derivedPushforward f).obj M)).hom ≫
        (uncurriedDerivedTensor Y).map
            (𝟙 ((derivedPushforward f).obj K) ×ₘ relativeCupProduct f L M) ≫
          relativeCupProduct f K ((uncurriedDerivedTensor X).obj (L, M))
```

## Tag 0FPM, a lemma

[Tag 0FPM](https://stacks.math.columbia.edu/tag/0FPM) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_braiding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraidingOfToposHom.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraidingOfToposHom.lean#L184). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.\{u, u, u}, for all K, L in D(𝒪); ψ on both edges is the commutativity constraint of Tag 0FPT and the statement carries no hypothesis or class argument”.

> **[Stacks, Tag 0FPM].** The relative cup product of [Stacks, Tag 0B6C] is commutative. Let
> `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')` be a morphism of ringed topoi: a morphism of the underlying
> topoi together with the structure map. Then for **all** `K, L` in `D(𝒪)` the square
>
> ```
> Rf_*K ⊗^L_{𝒪'} Rf_*L --cup--→ Rf_*(K ⊗^L_𝒪 L)
>         | ψ                          | Rf_*ψ
>         ↓                            ↓
> Rf_*L ⊗^L_{𝒪'} Rf_*K --cup--→ Rf_*(L ⊗^L_𝒪 K)
> ```
>
> commutes in `D(𝒪')`. The horizontal arrows are the relative cup product. The left edge is `ψ` at
> `(Rf_*K, Rf_*L)` and the right edge is `Rf_*` applied to `ψ` at `(K, L)`, as the source draws
> them. `ψ` is the commutativity constraint of [Stacks, Tag 0FPT] on each of the two derived
> categories.
>
> The statement has no hypothesis and no class argument of its own.

```lean
theorem relativeCupProduct_braiding {X Y : RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    relativeCupProduct f K L ≫ (derivedPushforward f).map (canonicalBraidingHom X.O K L) =
      canonicalBraidingHom Y.O ((derivedPushforward f).obj K) ((derivedPushforward f).obj L) ≫
        relativeCupProduct f L K
```

## Tag 0FPN, a lemma

[Tag 0FPN](https://stacks.math.columbia.edu/tag/0FPN) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_comp_pushforwardCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionOfToposHom.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionOfToposHom.lean#L136). The attribute's comment: “for morphisms of ringed topoi in the two-field sense of Tag 01D3, part (2) -- morphisms of the underlying topoi together with the structure maps, with no continuous functor between the underlying sites and no morphism-of-sites hypothesis; the left edge is the relative cup product of Tag 0B6C for f' ∘ f and the two equality edges of the source are the components of the composition isomorphism of derived pushforward, the conjugate of the Tag 0D6D isomorphism”.

> **[Stacks, Tag 0FPN].**  Let `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')` and
> `f' : (Sh(C'), 𝒪') ⟶ (Sh(C''), 𝒪'')` be morphisms of ringed topoi.  The relative cup product of
> [Stacks, Tag 0B6C] is compatible with composition: for all `K`, `L` in `D(𝒪)` the diagram
>
> ```
> R(f'f)_*K ⊗'' R(f'f)_*L --c⊗c--→ Rf'_*Rf_*K ⊗'' Rf'_*Rf_*L
>         |                                   |
>         ↓ cup for f'∘f                      ↓ cup for f'
> R(f'f)_*(K ⊗ L) --c--→ Rf'_*Rf_*(K ⊗ L) ←--Rf'_*(cup for f)-- Rf'_*(Rf_*K ⊗' Rf_*L)
> ```
>
> commutes in `D(𝒪'')`.  The left edge is the relative cup product of the composite `f' ∘ f`; the
> two edges `c` the source draws as equalities `R(f' ∘ f)_* = Rf'_*Rf_*` are the components of the
> composition isomorphism `derivedPushforwardCompIsoOfAdjoints`, the conjugate of the isomorphism of
> [Stacks, Tag 0D6D] (`conjugateEquiv_derivedPullbackCompIso_hom`).
>
> There is no hypothesis beyond the two morphisms of ringed topoi and the ambient instances making
> the derived categories and derived tensor products exist.

```lean
theorem relativeCupProduct_comp_pushforwardCompIso (K L : DerivedModules X.O) :
    relativeCupProduct (RingedToposHom.comp (X := X) f' f) K L ≫
        (derivedPushforwardCompIsoOfAdjoints f f').inv.app
          ((uncurriedDerivedTensor X).obj (K, L)) =
      (uncurriedDerivedTensor Z).map
          ((derivedPushforwardCompIsoOfAdjoints f f').inv.app K ×ₘ
            (derivedPushforwardCompIsoOfAdjoints f f').inv.app L) ≫
        relativeCupProduct f' ((derivedPushforward f).obj K) ((derivedPushforward f).obj L) ≫
          (derivedPushforward f').map (relativeCupProduct f K L)
```

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_comp_pushforwardCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionTransport.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionTransport.lean#L165). The attribute's comment: “the square at the composite morphism itself, with no carried input: the left edge is the relative cup product of Tag 0B6C for f' ∘ f and the two equality edges of the source are the components of the composition isomorphism of derived pushforward, the conjugate of the Tag 0D6D isomorphism”.

> For
> `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')`, `f' : (Sh(C'), 𝒪') ⟶ (Sh(C''), 𝒪'')` and `K`, `L` in `D(𝒪)`
> the diagram
>
> ```
> R(f'f)_*K ⊗'' R(f'f)_*L --c⊗c--→ Rf'_*Rf_*K ⊗'' Rf'_*Rf_*L
>         |                                   |
>         ↓ cup for f'∘f                      ↓ cup for f'
> R(f'f)_*(K ⊗ L) --c--→ Rf'_*Rf_*(K ⊗ L) ←--Rf'_*(cup for f)-- Rf'_*(Rf_*K ⊗' Rf_*L)
> ```
>
> commutes in `D(𝒪'')`. The left-hand vertical arrow is the relative cup product for the composite
> morphism `f' ∘ f` itself, and the two horizontal edges `c` are the components of the composition
> isomorphism `derivedPushforwardCompIso`.
>
> The proof transports `relativeCupProduct_comp`, the same square for the composite adjunction
> `Rf_* ⋙ Rf'_*` with the composite of the two comparisons of [Stacks, Tag 07A4], along the
> composition isomorphism, using the compatibility of the comparison of [Stacks, Tag 07A4] with
> composition, `Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso_hom_app_comp`.

```lean
theorem relativeCupProduct_comp_pushforwardCompIso (K L : DerivedModules X.O) :
    relativeCupProduct (f'.comp f)
          (RingedToposSiteHom.isMorphismOfSites_comp_u f f' hmosf hmosf') K L ≫
        (derivedPushforwardCompIso f f' hmosf hmosf').inv.app
          ((uncurriedDerivedTensor X).obj (K, L)) =
      (uncurriedDerivedTensor Z).map
          ((derivedPushforwardCompIso f f' hmosf hmosf').inv.app K ×ₘ
            (derivedPushforwardCompIso f f' hmosf hmosf').inv.app L) ≫
        relativeCupProduct f' hmosf' ((derivedPushforward f).obj K)
              ((derivedPushforward f).obj L) ≫
          (derivedPushforward f').map (relativeCupProduct f hmosf K L)
```

## Tag 0H9A, a lemma

[Tag 0H9A](https://stacks.math.columbia.edu/tag/0H9A) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBaseChangeOfToposHom.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBaseChangeOfToposHom.lean#L103).

> **[Stacks, Tag 0H9A].**  For a commutative square of morphisms of ringed topoi
>
> ```
>                 g'
>   (Sh(C'), 𝒪_{C'}) --→ (Sh(C), 𝒪_C)
>         |  f'                |  f
>         v                    v
>   (Sh(D'), 𝒪_{D'}) --→ (Sh(D), 𝒪_D)
>                 g
> ```
>
> and arbitrary `K`, `L` in `D(𝒪_C)`, the relative cup product of [Stacks, Tag 0B6C] is compatible
> with the square: the composite down the left (the comparison of [Stacks, Tag 07A4] for `g`, then
> the base change map of [Stacks, Tag 07A7] in each tensor factor) and along the bottom (the
> relative cup product for `f'`) equals the composite along the top (`Lg^*` of the relative cup
> product for `f`) and down the right (the base change map, then `R(f')_*` of the comparison of
> [Stacks, Tag 07A4] for `g'`), as maps
> `Lg^*(Rf_*K ⊗^L Rf_*L) ⟶ R(f')_*(L(g')^*K ⊗^L L(g')^*L)` in `D(𝒪_{D'})`.
>
> The four morphisms are morphisms of ringed topoi in the sense of Tag 01D3, part (2), and the
> only hypothesis on them is the commutativity `h` of the square.  The relative cup product of
> Tag 0B6C is written out as `adjunctionCupProduct` of the derived adjunction of Tag 07A6 and the
> comparison of Tag 07A4.

```lean
theorem relativeCupProduct_baseChange_square
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullbackTensorIso g).hom.app
          ((Stacks.Cohomology.DerivedPushforward.derivedPushforward f).obj K,
            (Stacks.Cohomology.DerivedPushforward.derivedPushforward f).obj L) ≫
        (Functor.uncurry.obj (derivedTensorProductFunctor Y'.O)).map
            (Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap f g' f' g h K ×ₘ
              Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap f g' f' g h L) ≫
          adjunctionCupProduct (Stacks.Cohomology.DerivedPullbackOfToposHom.derivedAdjunction f')
            (Functor.uncurry.obj (derivedTensorProductFunctor Y'.O))
            (Functor.uncurry.obj (derivedTensorProductFunctor X'.O))
            (Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullbackTensorIso f').hom
            ((Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback g').obj K)
            ((Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback g').obj L) =
      (Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback g).map
          (adjunctionCupProduct (Stacks.Cohomology.DerivedPullbackOfToposHom.derivedAdjunction f)
            (Functor.uncurry.obj (derivedTensorProductFunctor Y.O))
            (Functor.uncurry.obj (derivedTensorProductFunctor X.O))
            (Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullbackTensorIso f).hom K L) ≫
        Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap f g' f' g h
            (((derivedTensorProductFunctor X.O).obj K).obj L) ≫
          (Stacks.Cohomology.DerivedPushforward.derivedPushforward f').map
            ((Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullbackTensorIso g').hom.app
              (K, L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.33, Tag 0FPJ](https://stacks.math.columbia.edu/tag/0FPJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
