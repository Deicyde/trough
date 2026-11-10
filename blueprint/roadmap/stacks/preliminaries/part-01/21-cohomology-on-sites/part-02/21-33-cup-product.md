---
declaration: section
origin: cited
lean: Stacks.Cohomology.CupProductAndDerivedPushforward.naiveCupProduct_relativeCupProduct, Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct_relativeCupProduct, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_assoc_canonical, Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_assoc, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_assoc, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_braiding_unconditional, Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_braiding, Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_braiding
statement: formalized
proof: formalized
---

# 21.33 Cup product

Section 21.33 of the Stacks Project, [Tag 0FPJ](https://stacks.math.columbia.edu/tag/0FPJ). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FPK, a lemma

[Tag 0FPK](https://stacks.math.columbia.edu/tag/0FPK) in the Stacks Project.

**`Stacks.Cohomology.CupProductAndDerivedPushforward.naiveCupProduct_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforward.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforward.lean#L298). The attribute's comment: “variant: the special case of a morphism of ringed topoi presented by a morphism of sites; the tag for an arbitrary morphism of ringed topoi is Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct_relativeCupProduct”.

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

**`Stacks.Cohomology.CupProductAndDerivedPushforwardOfToposHom.naiveCupProduct_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforwardOfToposHom.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CupProductAndDerivedPushforwardOfToposHom.lean#L279). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.{u, u, u}, for all unbounded complexes K, M; the statement carries no hypothesis or class argument”.

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

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_assoc_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativity.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativity.lean#L212). The attribute's comment: “associativity of the relative cup product, unconditionally, over the canonical associativity constraints of the two derived tensor products (derivedAssociator, the associator of the monoidal structure of Tag 0FPT whose tensor product is the derived tensor product of Tag 06YU on the nose): their naturality is derivedAssociator_naturality and the associativity law of the comparison of Tag 07A4 for them, which the source's proof uses silently, is pullbackTensorComparisonAssociative”.

> The relative cup product is associative: for all `K`, `L`, `M` in `D(𝒪)` the square
>
> ```
> (Rf_*K ⊗' Rf_*L) ⊗' Rf_*M --→ Rf_*(K ⊗ L) ⊗' Rf_*M --→ Rf_*((K ⊗ L) ⊗ M)
>           |                                                     |
>           | a                                                   | Rf_*a
>           ↓                                                     ↓
> Rf_*K ⊗' (Rf_*L ⊗' Rf_*M) --→ Rf_*K ⊗' Rf_*(L ⊗ M) --→ Rf_*(K ⊗ (L ⊗ M))
> ```
>
> commutes in `D(𝒪')`. The four unlabelled arrows are relative cup products in one or the other
> tensor factor; the two edges `a` are the canonical associativity constraints `derivedAssociator`
> of `⊗^L_{𝒪'}` and `⊗^L_𝒪`.

```lean
theorem relativeCupProduct_assoc_canonical (K L M : DerivedModules X.O) :
    (uncurriedDerivedTensor Y).map
          (relativeCupProduct f hmos K L ×ₘ 𝟙 ((derivedPushforward f).obj M)) ≫
        relativeCupProduct f hmos ((uncurriedDerivedTensor X).obj (K, L)) M ≫
          (derivedPushforward f).map (derivedAssociator X K L M).hom =
      (derivedAssociator Y ((derivedPushforward f).obj K) ((derivedPushforward f).obj L)
            ((derivedPushforward f).obj M)).hom ≫
        (uncurriedDerivedTensor Y).map
            (𝟙 ((derivedPushforward f).obj K) ×ₘ relativeCupProduct f hmos L M) ≫
          relativeCupProduct f hmos K ((uncurriedDerivedTensor X).obj (L, M))
```

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativityOfToposHom.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductAssociativityOfToposHom.lean#L176). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.{u, u, u}, for all K, L, M in D(𝒪); the edges a are the associativity constraints derivedAssociator of Tag 0FPT and the statement carries no hypothesis or class argument; the associativity law of the comparison of Tag 07A4, which the source's proof uses silently, is pullbackTensorComparisonAssociative”.

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

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean#L387). The attribute's comment: “associativity of the relative cup product, with the associativity constraints of the two derived tensor products supplied as data and their naturality and the monoidality of the comparison of Tag 07A4 for them carried as explicit hypotheses: this development has neither the symmetric monoidal structure of Tag 0FPT assembled nor that monoidality”.

> **[Stacks, Tag 0FPL].**  The relative cup product of [Stacks, Tag 0B6C] is associative: for
> `K`, `L`, `M` in `D(𝒪)` the square
>
> ```
> (Rf_*K ⊗' Rf_*L) ⊗' Rf_*M --→ Rf_*(K ⊗ L) ⊗' Rf_*M --→ Rf_*((K ⊗ L) ⊗ M)
>           |                                                     ↑
>           ↓                                                     |
> Rf_*K ⊗' (Rf_*L ⊗' Rf_*M) --→ Rf_*K ⊗' Rf_*(L ⊗ M) --→ Rf_*(K ⊗ (L ⊗ M))
> ```
>
> commutes in `D(𝒪')`.  The upper route contracts `K ⊗ L` first, the lower route contracts
> `L ⊗ M` first; the two are different composites.
>
> The source draws the square with `⊗^L` strictly associative, so the associativity constraints
> are explicit here: `aY` is the one for `⊗^L_{𝒪'}` and `aX` the one for `⊗^L_𝒪`.  The hypotheses
> beyond the source are `haX`, the naturality of `aX`, and `hcomp`, the compatibility of the
> comparison of [Stacks, Tag 07A4] with the two constraints — i.e. that `Lf^*` is a monoidal
> functor for it.  The source gets both from the symmetric monoidal structure of
> [Stacks, Tag 0FPT], which this development does not assemble.

```lean
theorem relativeCupProduct_assoc
    (aY : ∀ P Q S : DerivedModules Y.O,
      (uncurriedDerivedTensor Y).obj ((uncurriedDerivedTensor Y).obj (P, Q), S) ⟶
        (uncurriedDerivedTensor Y).obj (P, (uncurriedDerivedTensor Y).obj (Q, S)))
    (aX : ∀ U V W : DerivedModules X.O,
      (uncurriedDerivedTensor X).obj ((uncurriedDerivedTensor X).obj (U, V), W) ≅
        (uncurriedDerivedTensor X).obj (U, (uncurriedDerivedTensor X).obj (V, W)))
    (haX : ∀ {U U' V V' W W' : DerivedModules X.O} (u : U ⟶ U') (v : V ⟶ V') (w : W ⟶ W'),
      (aX U V W).hom ≫
          (uncurriedDerivedTensor X).map (u ×ₘ (uncurriedDerivedTensor X).map (v ×ₘ w)) =
        (uncurriedDerivedTensor X).map ((uncurriedDerivedTensor X).map (u ×ₘ v) ×ₘ w) ≫
          (aX U' V' W').hom)
    (hcomp : ∀ P Q S : DerivedModules Y.O,
      (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app
            ((uncurriedDerivedTensor Y).obj (P, Q), S) ≫
          (uncurriedDerivedTensor X).map
            ((Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app (P, Q) ×ₘ
              𝟙 ((derivedPullback f).obj S)) ≫
          (aX ((derivedPullback f).obj P) ((derivedPullback f).obj Q)
            ((derivedPullback f).obj S)).hom =
        (derivedPullback f).map (aY P Q S) ≫
          (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app
            (P, (uncurriedDerivedTensor Y).obj (Q, S)) ≫
          (uncurriedDerivedTensor X).map (𝟙 ((derivedPullback f).obj P) ×ₘ
            (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app (Q, S)))
    (K L M : DerivedModules X.O) :
    (uncurriedDerivedTensor Y).map
          (relativeCupProduct f hmos K L ×ₘ 𝟙 ((derivedPushforward f).obj M)) ≫
        relativeCupProduct f hmos ((uncurriedDerivedTensor X).obj (K, L)) M =
      aY ((derivedPushforward f).obj K) ((derivedPushforward f).obj L)
            ((derivedPushforward f).obj M) ≫
        (uncurriedDerivedTensor Y).map
            (𝟙 ((derivedPushforward f).obj K) ×ₘ relativeCupProduct f hmos L M) ≫
          relativeCupProduct f hmos K ((uncurriedDerivedTensor X).obj (L, M)) ≫
            (derivedPushforward f).map (aX K L M).inv
```

## Tag 0FPM, a lemma

[Tag 0FPM](https://stacks.math.columbia.edu/tag/0FPM) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_braiding_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraiding.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraiding.lean#L238). The attribute's comment: “the whole tag, unconditionally: for a morphism of ringed topoi and all K, L in D(𝒪), the commutativity square of the relative cup product commutes. ψ on both edges is the genuine commutativity constraint of Tag 0FPT (canonicalBraidingHom, the braiding of canonicalDerivedSymmetric, whose tensor product is the derived tensor product of Tag 06YU on the nose) rather than a symmetry supplied as data, and its naturality is proved rather than assumed. The one-time hypothesis PullbackTensorComparisonBraided -- that the comparison of Tag 07A4 is braided, i.e. that Lf^* is a braided and not merely a monoidal functor -- is now proved too, as pullbackTensorComparisonBraided, by descent along Tag 06YS from a pair of K-flat complexes with flat terms through the braided clause of Tag 03EL on modules”.

> **[Stacks, Tag 0FPM].**  The relative cup product of [Stacks, Tag 0B6C] is commutative: for
> a morphism of ringed topoi `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')` and **all** `K, L` in `D(𝒪)` the
> square
>
> ```
> Rf_*K ⊗^L_{𝒪'} Rf_*L --cup--→ Rf_*(K ⊗^L_𝒪 L)
>         | ψ                          | Rf_*ψ
>         ↓                            ↓
> Rf_*L ⊗^L_{𝒪'} Rf_*K --cup--→ Rf_*(L ⊗^L_𝒪 K)
> ```
>
> commutes in `D(𝒪')`.  The horizontal arrows are the relative cup product, the left edge is `ψ`
> at `(Rf_*K, Rf_*L)` and the right edge is `Rf_*` applied to `ψ` at `(K, L)`, exactly as the
> source draws them.  `ψ` is the commutativity constraint of [Stacks, Tag 0FPT],
> `Stacks.SheafOfModules.DerivedMonoidal.canonicalBraidingHom`, on each of the two derived
> categories — not a symmetry supplied as data — and no hypothesis is placed on `K` or `L`.
>
> Nothing is assumed.  The braidedness of the comparison of [Stacks, Tag 07A4], which is the whole
> content of the tag, is `pullbackTensorComparisonBraided` above.

```lean
theorem relativeCupProduct_braiding_unconditional (K L : DerivedModules X.O) :
    relativeCupProduct f hmos K L ≫
        (derivedPushforward f).map (canonicalBraidingHom X.O K L) =
      canonicalBraidingHom Y.O ((derivedPushforward f).obj K) ((derivedPushforward f).obj L) ≫
        relativeCupProduct f hmos L K
```

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_braiding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraidingOfToposHom.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBraidingOfToposHom.lean#L182). The attribute's comment: “the whole tag, for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.{u, u, u}, for all K, L in D(𝒪); ψ on both edges is the commutativity constraint of Tag 0FPT and the statement carries no hypothesis or class argument”.

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

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_braiding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean#L449). The attribute's comment: “commutativity of the relative cup product, with the commutativity constraints of the two derived tensor products supplied as data and their naturality and the compatibility of the comparison of Tag 07A4 with them carried as explicit hypotheses: this development has neither the symmetric monoidal structure of Tag 0FPT assembled nor that compatibility”.

> **[Stacks, Tag 0FPM].**  The relative cup product of [Stacks, Tag 0B6C] is commutative: for
> `K`, `L` in `D(𝒪)` the square
>
> ```
> Rf_*K ⊗' Rf_*L --cup--→ Rf_*(K ⊗ L)
>       | ψ                     | Rf_*ψ
>       ↓                       ↓
> Rf_*L ⊗' Rf_*K --cup--→ Rf_*(L ⊗ K)
> ```
>
> commutes in `D(𝒪')`.  The left edge is the commutativity constraint `sY` of `⊗^L_{𝒪'}` at the
> pair `(Rf_*K, Rf_*L)`; the right edge is `Rf_*` applied to the commutativity constraint `sX` of
> `⊗^L_𝒪` at `(K, L)`.  These are the source's `ψ` and `Rf_*ψ`, and they are different maps.
>
> The constraint of [Stacks, Tag 0FPT] is supplied as data on each side, because this development
> has it only one pair of objects at a time and not as part of an assembled monoidal structure
> (`Stacks.DerivedTensor.RingedSite.DerivedTensorProduct.braidingIso`).  The hypotheses beyond the
> source are `hsX`, its naturality, and `hcomp`, the compatibility of the comparison of
> [Stacks, Tag 07A4] with the two constraints — i.e. that `Lf^*` is a braided functor for it.

```lean
theorem relativeCupProduct_braiding
    (sY : ∀ P Q : DerivedModules Y.O,
      (uncurriedDerivedTensor Y).obj (P, Q) ⟶ (uncurriedDerivedTensor Y).obj (Q, P))
    (sX : ∀ U V : DerivedModules X.O,
      (uncurriedDerivedTensor X).obj (U, V) ⟶ (uncurriedDerivedTensor X).obj (V, U))
    (hsX : ∀ {U U' V V' : DerivedModules X.O} (u : U ⟶ U') (v : V ⟶ V'),
      (uncurriedDerivedTensor X).map (u ×ₘ v) ≫ sX U' V' =
        sX U V ≫ (uncurriedDerivedTensor X).map (v ×ₘ u))
    (hcomp : ∀ P Q : DerivedModules Y.O,
      (derivedPullback f).map (sY P Q) ≫
          (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app (Q, P) =
        (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmos).hom.app (P, Q) ≫
          sX ((derivedPullback f).obj P) ((derivedPullback f).obj Q))
    (K L : DerivedModules X.O) :
    relativeCupProduct f hmos K L ≫ (derivedPushforward f).map (sX K L) =
      sY ((derivedPushforward f).obj K) ((derivedPushforward f).obj L) ≫
        relativeCupProduct f hmos L K
```

## Tag 0FPN, a lemma

[Tag 0FPN](https://stacks.math.columbia.edu/tag/0FPN) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCoherence.lean#L545). The attribute's comment: “compatibility of the relative cup product with composition, with R(f' ∘ f)_* realized as the composite Rf_* ⋙ Rf'_* and its adjunction the composite adjunction of Tag 0DV0 (the source's equality edge), and the comparison of Tag 07A4 for the composite taken to be the composite of the two comparisons, for every pair of composable morphisms of sites”.

> **[Stacks, Tag 0FPN].**  The relative cup product of [Stacks, Tag 0B6C] is compatible with
> composition: for `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')`, `f' : (Sh(C'), 𝒪') ⟶ (Sh(C''), 𝒪'')` and
> `K`, `L` in `D(𝒪)` the diagram
>
> ```
> R(f'f)_*K ⊗'' R(f'f)_*L  ====  Rf'_*Rf_*K ⊗'' Rf'_*Rf_*L
>         |                                  |
>         ↓                                  ↓
> R(f'f)_*(K ⊗ L)  ====  Rf'_*Rf_*(K ⊗ L)  ←--  Rf'_*(Rf_*K ⊗' Rf_*L)
> ```
>
> commutes in `D(𝒪'')`: the cup product for the composite is the cup product for `f'` at
> `(Rf_*K, Rf_*L)` followed by `Rf'_*` of the cup product for `f`.
>
> **How the source's `@{=}` edges are handled.**  The source draws the two horizontal edges as
> equalities `R(f' ∘ f)_* = Rf'_* ∘ Rf_*`.  In this development the two functors are not equal:
> they are isomorphic by
> `Stacks.Cohomology.DerivedBaseChangePasting.derivedPushforwardCompIso`.  Accordingly
> `R(f' ∘ f)_*` is realized here as the composite `Rf_* ⋙ Rf'_*` with the composite
> adjunction `L(f')^* ⋙ Lf^* ⊣ Rf_* ⋙ Rf'_*` of `CategoryTheory.Adjunction.comp`, whose counit is
> the composition of the two counits — which is exactly the identification the source's proof
> appeals to ([Stacks, Tag 0DV0]).  With that realization the two `@{=}` edges are identities and
> no isomorphism is absorbed silently.  The comparison for the composite is correspondingly the
> composite comparison `compComparison`, the monoidal structure of the composite of two monoidal
> functors.  The statement holds for every pair of composable morphisms of ringed topoi that are
> morphisms of sites.
>
> Transporting this statement to `relativeCupProduct (f'.comp f)` — the cup product built from
> `DerivedPullbackOnRingedTopoi.derivedAdjunction (f'.comp f)` and
> `Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso (f'.comp f)` — would additionally
> require the compatibility of [Stacks, Tag 07A4] with composition of morphisms of ringed topoi,
> which this development does not have.  The same gap is recorded on
> `derivedBaseChangeMap_projectionFormulaMap_square` in
> `Stacks.Cohomology.ProjectionFormulaOnRingedTopoi`.

```lean
theorem relativeCupProduct_comp (K L : DerivedModules X.O) :
    adjunctionCupProduct
        ((DerivedPullbackOnRingedTopoi.derivedAdjunction f' hmosf').comp
          (DerivedPullbackOnRingedTopoi.derivedAdjunction f hmosf))
        (uncurriedDerivedTensor Z) (uncurriedDerivedTensor X)
        (compComparison (uncurriedDerivedTensor X) (uncurriedDerivedTensor Y)
          (uncurriedDerivedTensor Z)
          (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f hmosf).hom
          (Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso f' hmosf').hom) K L =
      relativeCupProduct f' hmosf' ((derivedPushforward f).obj K)
            ((derivedPushforward f).obj L) ≫
        (derivedPushforward f').map (relativeCupProduct f hmosf K L)
```

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct_comp_pushforwardCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionOfToposHom.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionOfToposHom.lean#L136). The attribute's comment: “for morphisms of ringed topoi in the two-field sense of Tag 01D3, part (2) -- morphisms of the underlying topoi together with the structure maps, with no continuous functor between the underlying sites and no morphism-of-sites hypothesis; the left edge is the relative cup product of Tag 0B6C for f' ∘ f and the two equality edges of the source are the components of the composition isomorphism of derived pushforward, the conjugate of the Tag 0D6D isomorphism”.

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

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_comp_pushforwardCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionTransport.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductCompositionTransport.lean#L160). The attribute's comment: “the square at the composite morphism itself, with no carried input: the left edge is the relative cup product of Tag 0B6C for f' ∘ f and the two equality edges of the source are the components of the composition isomorphism of derived pushforward, the conjugate of the Tag 0D6D isomorphism”.

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

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBaseChangeOfToposHom.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductBaseChangeOfToposHom.lean#L103).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
