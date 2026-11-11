---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exists_singleton_affine_weaklyContractible_hypercovering, AlgebraicGeometry.ProEtale.exists_singleton_weaklyContractible_hypercovering_unconditional, AlgebraicGeometry.ProEtale.exists_singleton_weaklyContractible_hypercovering, AlgebraicGeometry.ProEtale.SmallProetale.exists_weaklyContractible_hypercovering, AlgebraicGeometry.ProEtale.SmallProetale.exists_affine_weaklyContractible_hypercovering, Stacks.CategoryTheory.Hypercovering.exists_singleton_weaklyContractible_hypercovering_finiteDisjointUnions, Stacks.CategoryTheory.Hypercovering.exists_singleton_weaklyContractible_hypercovering_of_prop_finiteDisjointUnions, Stacks.CategoryTheory.Hypercovering.derivedSectionsIsoHypercoverTotalComplex
statement: formalized
proof: formalized
---

# 61.14 Weakly contractible hypercoverings

Section 61.14 of the Stacks Project, [Tag 09A0](https://stacks.math.columbia.edu/tag/09A0). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09A1, a lemma

[Tag 09A1](https://stacks.math.columbia.edu/tag/09A1) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_singleton_affine_weaklyContractible_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/QcqsWeaklyContractibleHypercovering.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/QcqsWeaklyContractibleHypercovering.lean#L204). The attribute's comment: “(2), at the library's big pro-etale site”.

> **Stacks Project, Tag 09A1 (2).** Every quasi-compact quasi-separated object `U` of a chosen
> big pro-étale site admits a hypercovering each of whose terms is a one-element family on an
> affine weakly contractible object of the site covering `U`.
>
> The construction of Stacks 09A1 is run in the quasi-compact quasi-separated pro-étale site, where
> the one-element coverings by affine weakly contractible objects of Stacks 0F4P are available, and
> the hypercovering obtained there is transported to the big site by Stacks 0DAZ along the
> inclusion, which is continuous and preserves fibre products.

```lean
theorem exists_singleton_affine_weaklyContractible_hypercovering (U : B.Scheme)
    [CompactSpace U.obj] [QuasiSeparatedSpace U.obj] :
    ∃ K : SimplicialObject (FormalCoproduct.{u + 1} (Over U)),
      IsHypercovering B.topology.toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            IsAffine ((K.obj (op ⦋n⦌)).obj i).left.obj ∧
            B.topology.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈
              B.topology.toPretopology U
```

**`AlgebraicGeometry.ProEtale.exists_singleton_weaklyContractible_hypercovering_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercovering.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercovering.lean#L200). The attribute's comment: “(1), at the library's big pro-etale site”.

> **Stacks Project, Tag 09A1 (1).** Every object `U` of a chosen big pro-étale site admits a
> hypercovering each of whose terms is a one-element family on a weakly contractible object of the
> site covering `U`.
>
> The one-element coverings by weakly contractible objects are those of Stacks 0F4P, supplied by
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering`. The two hypotheses on
> disjoint unions are discharged here: that taking finite disjoint unions preserves coverings
> because the summands of a finite disjoint union cover it, and that a finite disjoint union of
> weakly contractible objects is weakly contractible.

```lean
theorem exists_singleton_weaklyContractible_hypercovering_unconditional (U : B.Scheme) :
    ∃ K : SimplicialObject (FormalCoproduct.{u + 1} (Over U)),
      IsHypercovering B.topology.toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            B.topology.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈
              B.topology.toPretopology U
```

**`AlgebraicGeometry.ProEtale.exists_singleton_weaklyContractible_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercovering.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercovering.lean#L227). The attribute's comment: “(1), at the library's big pro-etale site. The one-element weakly contractible covering is Tag 0F4P, discharged here; hunions and the two instance hypotheses are Tag 0DB2's own hypotheses, propagated”.

> **Stacks Project, Tag 09A1 (1).** Every object `U` of a chosen big pro-étale site admits a
> hypercovering each of whose terms is a one-element family on a weakly contractible object of the
> site covering `U`.
>
> The one-element coverings by weakly contractible objects are those of Stacks 0F4P, supplied by
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering`; the hypotheses on
> disjoint unions are those of Stacks 0DB2, together with the weak contractibility of a finite
> disjoint union of weakly contractible objects.

```lean
theorem exists_singleton_weaklyContractible_hypercovering (U : B.Scheme)
    [HasFiniteCoproducts (Over U)]
    [ObjectProperty.IsClosedUnderFiniteLimits
      (fun A : FormalCoproduct.{u + 1} (Over U) ↦ HasCoproduct A.obj)]
    [PreservesFiniteLimits (takeUnions.{u + 1, u, u + 1} (C := Over U))]
    (hunions : TakeUnionsFinPreservesCoverings.{u + 1} B.topology U)
    (sum_weaklyContractible :
      SumMemFin.{u + 1} {V : B.Scheme | B.topology.IsWeaklyContractible V} U) :
    ∃ K : SimplicialObject (FormalCoproduct.{u + 1} (Over U)),
      IsHypercovering B.topology.toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            B.topology.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈
              B.topology.toPretopology U
```

**`AlgebraicGeometry.ProEtale.SmallProetale.exists_weaklyContractible_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercoveringSmall.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercoveringSmall.lean#L113). The attribute's comment: “(1)”.

> **Stacks Project, Tag 09A1 (1).** Let `S` be a scheme in a chosen big pro-étale site. Every
> object `U` of the small pro-étale site `S_proétale` admits a hypercovering `K` of `U` in
> `S_proétale` such that each term `K_n` consists of a single weakly contractible object of
> `S_proétale` covering `U`.

```lean
theorem exists_weaklyContractible_hypercovering (U : SmallProetale B S hS) :
    ∃ K : SimplicialObject (FormalCoproduct.{w} (Over U)),
      IsHypercovering (topology B S hS).toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            (topology B S hS).IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈
              (topology B S hS).toPretopology U
```

**`AlgebraicGeometry.ProEtale.SmallProetale.exists_affine_weaklyContractible_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercoveringSmall.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleHypercoveringSmall.lean#L201). The attribute's comment: “(2)”.

> **Stacks Project, Tag 09A1 (2).** Let `S` be a scheme in a chosen big pro-étale site. Every
> quasi-compact and quasi-separated object `U` of the small pro-étale site `S_proétale` admits a
> hypercovering `K` of `U` in `S_proétale` such that each term `K_n` consists of a single affine
> and weakly contractible object of `S_proétale` covering `U`.

```lean
theorem exists_affine_weaklyContractible_hypercovering (U : SmallProetale B S hS)
    [CompactSpace ((toScheme B S hS).obj U)] [QuasiSeparatedSpace ((toScheme B S hS).obj U)] :
    ∃ K : SimplicialObject (FormalCoproduct.{w} (Over U)),
      IsHypercovering (topology B S hS).toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            IsAffine ((toScheme B S hS).obj ((K.obj (op ⦋n⦌)).obj i).left) ∧
            (topology B S hS).IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈
              (topology B S hS).toPretopology U
```

**`Stacks.CategoryTheory.Hypercovering.exists_singleton_weaklyContractible_hypercovering_finiteDisjointUnions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/WeaklyContractibleHypercovering.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/WeaklyContractibleHypercovering.lean#L388). The attribute's comment: “(1), for a general site: the one-element weakly contractible covering is the hypothesis exists\_singleton\_cover (Tag 0F4P), and hunions is the remaining hypothesis of the library's Tag 0DB2, propagated”.

> **Stacks Project, Tag 09A1 (1).** On a site with fibre products in which every object has a
> one-element covering by a weakly contractible object, every object `X` admits a hypercovering
> each of whose terms is a single weakly contractible object covering `X`.
>
> The disjoint unions taken degreewise are governed by the hypotheses of Tag 0DB2 and by the fact
> that a finite disjoint union of weakly contractible objects is weakly contractible.

```lean
theorem exists_singleton_weaklyContractible_hypercovering_finiteDisjointUnions
    (hunions : TakeUnionsFinPreservesCoverings.{w} T X)
    (sum_weaklyContractible : SumMemFin.{w} {V : C | T.IsWeaklyContractible V} X)
    (exists_singleton_cover : ∀ Y : C, ∃ (V : C) (f : V ⟶ Y),
      T.IsWeaklyContractible V ∧ Presieve.singleton f ∈ T.toPretopology Y) :
    ∃ K : SimplicialObject (FormalCoproduct.{w} (Over X)),
      IsHypercovering T.toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            T.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈ T.toPretopology X
```

**`Stacks.CategoryTheory.Hypercovering.exists_singleton_weaklyContractible_hypercovering_of_prop_finiteDisjointUnions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/WeaklyContractibleHypercovering.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/WeaklyContractibleHypercovering.lean#L417). The attribute's comment: “(2), with the object property P as a parameter: the source states it for affineness on the quasi-compact quasi-separated pro-etale site, which is constructed in StacksFrontier/AlgebraicGeometry/ProEtale/Site/Qcqs.lean, and (2) itself is proved at a chosen big pro-etale site as AlgebraicGeometry.ProEtale.exists\_singleton\_affine\_weaklyContractible\_hypercovering. That instantiation runs exists\_singleton\_hypercovering\_objects\_in\_finiteDisjointUnions rather than this lemma, because the weak contractibility carried here is that of the site being worked in, while the source's — and the library statement's — is that of the ambient pro-etale site. Instantiating this lemma at the big site with P := affine would be vacuous, since a non-quasi-compact object has no one-element affine cover. Same carried hypotheses as (1)”.

> **Stacks Project, Tag 09A1 (2).** The same construction run with a further property `P` of
> objects stable under the disjoint unions taken, such as affineness on the site of quasi-compact
> and quasi-separated objects: every object `X` admits a hypercovering each of whose terms is a
> single object satisfying `P`, weakly contractible, and covering `X`.

```lean
theorem exists_singleton_weaklyContractible_hypercovering_of_prop_finiteDisjointUnions (P : Set C)
    (hunions : TakeUnionsFinPreservesCoverings.{w} T X)
    (sum_mem : SumMemFin.{w} {V : C | V ∈ P ∧ T.IsWeaklyContractible V} X)
    (exists_singleton_cover : ∀ Y : C, ∃ (V : C) (f : V ⟶ Y),
      V ∈ P ∧ T.IsWeaklyContractible V ∧ Presieve.singleton f ∈ T.toPretopology Y) :
    ∃ K : SimplicialObject (FormalCoproduct.{w} (Over X)),
      IsHypercovering T.toPretopology K ∧
        ∀ n : ℕ, ∃ i : (K.obj (op ⦋n⦌)).I,
          (∀ j : (K.obj (op ⦋n⦌)).I, j = i) ∧
            ((K.obj (op ⦋n⦌)).obj i).left ∈ P ∧
            T.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left ∧
            Presieve.singleton ((K.obj (op ⦋n⦌)).obj i).hom ∈ T.toPretopology X
```

## Tag 09A2, a lemma

[Tag 09A2](https://stacks.math.columbia.edu/tag/09A2) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.derivedSectionsIsoHypercoverTotalComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/HypercoverTotalComplex.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/HypercoverTotalComplex.lean#L686).

> A hypercovering by weakly contractible objects computes the derived
> sections of any bounded-below complex of abelian sheaves.

```lean
public noncomputable def derivedSectionsIsoHypercoverTotalComplex
    [Small.{v} C]
    [HasSheafify J.toGrothendieck (Type v)]
    [HasSheafify J.toGrothendieck AddCommGrpCat.{max u v w}]
    [J.toGrothendieck.WEqualsLocallyBijective AddCommGrpCat.{max u v w}]
    [EnoughInjectives (Sheaf J.toGrothendieck AddCommGrpCat.{max u v w})]
    (hK : IsHypercovering J K)
    (hweak : ∀ n : ℕ, ∀ i : (K.obj (op ⦋n⦌)).I,
      J.toGrothendieck.IsWeaklyContractible ((K.obj (op ⦋n⦌)).obj i).left)
    (E : CochainComplex.Plus (Sheaf J.toGrothendieck AddCommGrpCat.{max u v w})) :
    DerivedCategory.Plus.ι.obj
      ((sheafSectionsFunctor J U).rightDerivedFunctorPlus.obj
        (DerivedCategory.Plus.Q.obj E)) ≅
      DerivedCategory.Q.obj (hypercoverTotalComplex J U K E)
```

## Tag 09A3, a lemma

[Tag 09A3](https://stacks.math.columbia.edu/tag/09A3) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.preservesColimitsOfShape_discrete_derivedSectionsPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean#L522). The attribute's comment: “direct sums, as preservation of colimit cocones indexed by a discrete category; same hypotheses as the cofan form below”.

> Derived sections over `U` commute with direct sums: every colimit cocone on a family of
> objects of `D⁺(Sh(J, Ab))` is carried by `RΓ(U, -) : D⁺(Sh(J, Ab)) ⥤ D(Ab)` to a colimit cocone
> in `D(Ab)`.

```lean
public theorem preservesColimitsOfShape_discrete_derivedSectionsPlus
    (hK : IsHypercovering J K) (hcov : IsSingletonExactQuasiCompact J U K) (ι : Type u) :
    PreservesColimitsOfShape (Discrete ι)
      ((sheafSectionsFunctor J U).rightDerivedFunctorPlus ⋙ DerivedCategory.Plus.ι)
```

**`Stacks.CategoryTheory.Hypercovering.isColimit_mapCofan_derivedSectionsPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean#L631). The attribute's comment: “direct sums, at an object of a general site admitting a hypercovering by one-element families on quasi-compact objects with exact sections --- which is what Tag 09A1 provides for the pro-etale site of a quasi-compact quasi-separated scheme, modulo the hypotheses that Tag 09A1 itself carries in this library”.

> Let `U` be an object of a site admitting a hypercovering each of whose terms is a one-element
> family on a quasi-compact object over which taking sections of abelian sheaves is exact. Then
> `RΓ(U, -) : D⁺(Sh(J, Ab)) ⥤ D(Ab)` commutes with direct sums: if `S`, together with maps
> `E i ⟶ S`, is the direct sum of a family `E` of bounded below objects, then `RΓ(U, S)` with the
> images of those maps is the direct sum of the `RΓ(U, E i)` in `D(Ab)`.

```lean
public noncomputable def isColimit_mapCofan_derivedSectionsPlus
    (hK : IsHypercovering J K) (hcov : IsSingletonExactQuasiCompact J U K)
    {ι : Type u}
    {E : ι → DerivedCategory.Plus (Sheaf J.toGrothendieck AddCommGrpCat.{u})}
    {S : DerivedCategory.Plus (Sheaf J.toGrothendieck AddCommGrpCat.{u})}
    (inj : ∀ i, E i ⟶ S) (hc : IsColimit (Cofan.mk S inj)) :
    IsColimit (Cofan.mk (DerivedCategory.Plus.ι.obj
        ((sheafSectionsFunctor J U).rightDerivedFunctorPlus.obj S))
      (fun i => DerivedCategory.Plus.ι.map
        ((sheafSectionsFunctor J U).rightDerivedFunctorPlus.map (inj i))))
```

**`Stacks.CategoryTheory.Hypercovering.isHomotopyColimit_derivedSectionsPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedSectionsCoproducts.lean#L650). The attribute's comment: “homotopy colimits, under the same hypotheses on the hypercovering as the direct sums half”.

> Derived sections over `U` carry a homotopy colimit of a system of bounded below complexes of
> abelian sheaves to a homotopy colimit in `D(Ab)`.

```lean
public theorem isHomotopyColimit_derivedSectionsPlus
    (hK : IsHypercovering J K) (hcov : IsSingletonExactQuasiCompact J U K)
    (F : ℕ ⥤ DerivedCategory.Plus (Sheaf J.toGrothendieck AddCommGrpCat.{u}))
    [HasCoproduct F.obj]
    {X : DerivedCategory.Plus (Sheaf J.toGrothendieck AddCommGrpCat.{u})}
    [HasCoproduct (F ⋙ (sheafSectionsFunctor J U).rightDerivedFunctorPlus ⋙
      DerivedCategory.Plus.ι).obj]
    (h : Pretriangulated.IsHomotopyColimit F X) :
    Pretriangulated.IsHomotopyColimit
      (F ⋙ (sheafSectionsFunctor J U).rightDerivedFunctorPlus ⋙ DerivedCategory.Plus.ι)
      (((sheafSectionsFunctor J U).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.ι).obj X)
```

**`AlgebraicGeometry.ProEtale.derivedGlobalSections_preservesCoproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedGlobalSectionsDirectSums.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedGlobalSectionsDirectSums.lean#L305). The attribute's comment: “direct sums, for the derived global sections of the small pro-etale site of a quasi-compact quasi-separated scheme, as preservation of colimit cocones indexed by a discrete category with an arbitrary index type”.

> **Stacks 09A3, direct sums.** Let `X` be a quasi-compact and quasi-separated scheme. Then
>
> > `RΓ(X, -) : D⁺(X_pro-étale) ⥤ D(Ab)`
>
> commutes with direct sums: every colimit cocone on a family of objects of `D⁺(X_pro-étale)`
> indexed by a discrete category is carried to a colimit cocone in `D(Ab)`.
>
> The statement quantifies over colimit cocones rather than preserving a coproduct functor: an
> arbitrary direct sum of bounded below objects need not be bounded below, so `D⁺(X_pro-étale)`
> has no coproducts, and the source itself conditions on `⊕ E i` being an object of `D⁺`.
>
> The index type is arbitrary. The family is reduced to its nonzero members, which form a set
> small in the universe at which the sheaf category is Grothendieck abelian, and there
> `preservesColimit_derivedGlobalSections_of_isGE` applies, the common lower bound coming from
> the direct sum itself.

```lean
theorem derivedGlobalSections_preservesCoproducts (I : Type i₀) :
    PreservesColimitsOfShape (Discrete I)
      ((Sheaf.Γ (Scheme.ProEt.topology X)
        AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.ι)
```

**`AlgebraicGeometry.ProEtale.derivedGlobalSections_preservesHomotopyColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedGlobalSectionsDirectSums.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedGlobalSectionsDirectSums.lean#L343). The attribute's comment: “homotopy colimits, for the derived global sections of the small pro-etale site of a quasi-compact quasi-separated scheme”.

> **Stacks 09A3, homotopy colimits.** Let `X` be a quasi-compact and quasi-separated scheme.
> Then `RΓ(X, -) : D⁺(X_pro-étale) ⥤ D(Ab)` carries a homotopy colimit of a system of objects of
> `D⁺(X_pro-étale)` to a homotopy colimit in `D(Ab)`.
>
> This follows formally from the direct sums half: the functor is triangulated, and a homotopy
> colimit is defined by a distinguished triangle whose first vertex is a direct sum.

```lean
theorem derivedGlobalSections_preservesHomotopyColimits
    (F : ℕ ⥤ DerivedCategory.Plus (Sheaf (Scheme.ProEt.topology X)
      AddCommGrpCat.{max (u + 1) v}))
    {K : DerivedCategory.Plus (Sheaf (Scheme.ProEt.topology X)
      AddCommGrpCat.{max (u + 1) v})}
    [HasCoproduct F.obj]
    [HasCoproduct (F ⋙ (Sheaf.Γ (Scheme.ProEt.topology X)
      AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus ⋙
      DerivedCategory.Plus.ι).obj]
    (hK : Pretriangulated.IsHomotopyColimit F K) :
    Pretriangulated.IsHomotopyColimit
      (F ⋙ (Sheaf.Γ (Scheme.ProEt.topology X)
        AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.ι)
      (((Sheaf.Γ (Scheme.ProEt.topology X)
        AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.ι).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.14, Tag 09A0](https://stacks.math.columbia.edu/tag/09A0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
