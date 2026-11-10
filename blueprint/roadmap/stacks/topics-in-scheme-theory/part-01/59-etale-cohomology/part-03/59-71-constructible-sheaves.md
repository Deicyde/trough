---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsConstructibleSetSheaf, AlgebraicGeometry.IsConstructibleAbelianSheaf, AlgebraicGeometry.IsConstructibleModuleSheaf, AlgebraicGeometry.IsConstructibleAbelianEtaleSheaf, AlgebraicGeometry.IsConstructibleModuleEtaleSheaf, AlgebraicGeometry.isConstructibleFiniteSheaf_iff_exists_stratification, AlgebraicGeometry.isConstructibleModuleSheaf_iff_exists_stratification, AlgebraicGeometry.isConstructibleFiniteSheaf_tfae
statement: formalized
proof: formalized
---

# 59.71 Constructible sheaves

Section 59.71 of the Stacks Project, [Tag 05BE](https://stacks.math.columbia.edu/tag/05BE). 10 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03RW, a definition

[Tag 03RW](https://stacks.math.columbia.edu/tag/03RW) in the Stacks Project.

**`AlgebraicGeometry.IsConstructibleSetSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean#L104). The attribute's comment: “part (1)”. References: SGA 4 IX (2.3), “sheaves of sets”.

> A constructible sheaf of sets on the small étale site.

```lean
public abbrev IsConstructibleSetSheaf (B : BigEtaleSite.{u}) (X : B.Scheme)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) : Prop
```

**`AlgebraicGeometry.IsConstructibleAbelianSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean#L110). The attribute's comment: “part (2)”. References: SGA 4½ Arcata (4.3.2), “(i)”; SGA 4 IX (2.3), “sheaves of groups”.

> A constructible sheaf of abelian groups on the small étale site.

```lean
public abbrev IsConstructibleAbelianSheaf (B : BigEtaleSite.{u}) (X : B.Scheme)
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous AddCommGrpCat.{w}
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) AddCommGrpCat.{w}]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{w}) : Prop
```

**`AlgebraicGeometry.IsConstructibleModuleSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible.lean#L175). The attribute's comment: “part (3)”. References: SGA 4 IX (2.3), “A-modules, A noetherian”.

> A constructible sheaf of modules over a Noetherian ring: on a finite
> constructible stratification of every affine open, it is locally constant of
> finite type.

```lean
public abbrev IsConstructibleModuleSheaf (B : BigEtaleSite.{u}) (X : B.Scheme)
    (R : Type r) [Ring R]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{w} R)
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) (ModuleCat.{w} R)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R)) : Prop
```

**`AlgebraicGeometry.IsConstructibleAbelianEtaleSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/Definition.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/Definition.lean#L85). The attribute's comment: “part (2)”. References: SGA 4 IX (2.3), “special case”; SGA 4½ Arcata (4.3.2).

> **Stacks 03RW (2).** A sheaf of abelian groups `F` on the small étale site of `X` is
> constructible if for every affine open `U ⊆ X` there is a finite decomposition `U = ∐ᵢ Uᵢ` into
> constructible locally closed subschemes such that `F|_{Uᵢ}` is finite locally constant for
> all `i`.

```lean
public abbrev IsConstructibleAbelianEtaleSheaf
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) w}) : Prop
```

**`AlgebraicGeometry.IsConstructibleModuleEtaleSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/Definition.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/Definition.lean#L99). The attribute's comment: “part (3)”.

> **Stacks 03RW (3).** Let `Λ` be a Noetherian ring. A sheaf of `Λ`-modules `F` on the small
> étale site of `X` is constructible if for every affine open `U ⊆ X` there is a finite
> decomposition `U = ∐ᵢ Uᵢ` into constructible locally closed subschemes such that `F|_{Uᵢ}` is of
> finite type and locally constant for all `i`.

```lean
public abbrev IsConstructibleModuleEtaleSheaf (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w} Λ)) : Prop
```

## Tag 095E, a lemma

[Tag 095E](https://stacks.math.columbia.edu/tag/095E) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleFiniteSheaf_iff_exists_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/GlobalStratification.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/GlobalStratification.lean#L142). The attribute's comment: “finite sheaves, stratification”. References: SGA 4 IX (2.4), “(i)”.

> **Stacks 095E, sets and abelian groups: the equivalence of (1) and (3).** On a quasi-compact
> quasi-separated scheme, a sheaf with values in a concrete category is constructible exactly when
> there is one finite partition of the whole scheme by constructible locally closed subschemes on
> each of which its inverse image is finite locally constant.

```lean
public theorem isConstructibleFiniteSheaf_iff_exists_stratification
    (F : Sheaf (SmallEtale.topology B X.obj X.property) D) :
    IsConstructibleFiniteSheaf B X F ↔
      ∃ s : ConstructibleStratification B X ⊤,
        ∀ i, Stacks.ConstantSheaf.IsFiniteLocallyConstant
          (SmallEtale.topology B (s.piece i).obj (s.piece i).property)
          (((smallEtaleBaseChange B (s.inclusion i)).sheafPullback D
            (SmallEtale.topology B X.obj X.property)
            (SmallEtale.topology B (s.piece i).obj (s.piece i).property)).obj F)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_iff_exists_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/GlobalStratification.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/GlobalStratification.lean#L188). The attribute's comment: “module sheaves, stratification”. References: SGA 4 IX (2.4), “(i), modules”.

> **Stacks 095E, modules: the equivalence of (1) and (3).** On a quasi-compact quasi-separated
> scheme, a sheaf of modules over a commutative ring is constructible exactly when there is one
> finite partition of the whole scheme by constructible locally closed subschemes on each of which
> its inverse image is locally constant with finitely generated values.

```lean
public theorem isConstructibleModuleSheaf_iff_exists_stratification
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R)) :
    IsConstructibleModuleSheaf B X R F ↔
      ∃ s : ConstructibleStratification B X ⊤,
        ∀ i, Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant R
          (SmallEtale.topology B (s.piece i).obj (s.piece i).property)
          (((smallEtaleBaseChange B (s.inclusion i)).sheafPullback (ModuleCat.{w} R)
            (SmallEtale.topology B X.obj X.property)
            (SmallEtale.topology B (s.piece i).obj (s.piece i).property)).obj F)
```

**`AlgebraicGeometry.isConstructibleFiniteSheaf_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocal.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocal.lean#L431). References: SGA 4 IX (2.4), “(i), (ii)”.

> **Stacks 095E for sheaves of sets and of abelian groups.** For a sheaf on the small étale site
> of a quasi-compact quasi-separated scheme the following are equivalent: it is constructible; it is
> constructible after restriction to each member of some open cover; and there is one constructible
> stratification of the whole scheme on each stratum of which its inverse image is finite locally
> constant.
>
> Finite local constancy is closed under isomorphism and stable under inverse image along an
> arbitrary morphism of small étale sites, by
> `AlgebraicGeometry.isFiniteLocallyConstant_smallEtaleSheafPullback_of_overPost`, which is
> Tag 093R, so `AlgebraicGeometry.isStratifiedSheaf_tfae` applies to it.

```lean
public theorem isConstructibleFiniteSheaf_tfae (Z : B.Scheme)
    [CompactSpace Z.obj] [QuasiSeparatedSpace Z.obj]
    (G : Sheaf (SmallEtale.topology B Z.obj Z.property) A) :
    List.TFAE
      [ IsConstructibleFiniteSheaf B Z G,
        ∃ (J : Type (u + 1)) (Y : J → B.Scheme) (g : ∀ j, Y j ⟶ Z),
          (∀ j, IsOpenImmersion (B.inclusion.map (g j))) ∧
          (Set.univ = ⋃ j, Set.range (B.inclusion.map (g j)).base) ∧
          ∀ j, IsConstructibleFiniteSheaf B (Y j)
            (((smallEtaleBaseChange B (g j)).sheafPullback A
              (SmallEtale.topology B Z.obj Z.property)
              (SmallEtale.topology B (Y j).obj (Y j).property)).obj G),
        ∃ s : ConstructibleStratification B Z ⊤, ∀ i,
          Stacks.ConstantSheaf.IsFiniteLocallyConstant (FD := FA) (CD := CA)
            (SmallEtale.topology B (s.piece i).obj (s.piece i).property)
            (((smallEtaleBaseChange B (s.inclusion i)).sheafPullback A
              (SmallEtale.topology B Z.obj Z.property)
              (SmallEtale.topology B (s.piece i).obj (s.piece i).property)).obj G) ]
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocal.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocal.lean#L483). References: SGA 4 IX (2.4), “special case”.

> For a sheaf of modules over a Noetherian ring on the small étale site of a quasi-compact
> quasi-separated scheme the following are equivalent: it is constructible; it is constructible
> after restriction to each member of some open cover; and there is one constructible stratification
> of the whole scheme on each stratum of which its inverse image is locally constant with finitely
> generated values.

```lean
public theorem isConstructibleModuleSheaf_tfae (Z : B.Scheme)
    [CompactSpace Z.obj] [QuasiSeparatedSpace Z.obj]
    (G : Sheaf (SmallEtale.topology B Z.obj Z.property) (ModuleCat.{w} R)) :
    List.TFAE
      [ IsConstructibleModuleSheaf B Z R G,
        ∃ (J : Type (u + 1)) (Y : J → B.Scheme) (g : ∀ j, Y j ⟶ Z),
          (∀ j, IsOpenImmersion (B.inclusion.map (g j))) ∧
          (Set.univ = ⋃ j, Set.range (B.inclusion.map (g j)).base) ∧
          ∀ j, IsConstructibleModuleSheaf B (Y j) R
            (((smallEtaleBaseChange B (g j)).sheafPullback (ModuleCat.{w} R)
              (SmallEtale.topology B Z.obj Z.property)
              (SmallEtale.topology B (Y j).obj (Y j).property)).obj G),
        ∃ s : ConstructibleStratification B Z ⊤, ∀ i,
          Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant R
            (SmallEtale.topology B (s.piece i).obj (s.piece i).property)
            (((smallEtaleBaseChange B (s.inclusion i)).sheafPullback (ModuleCat.{w} R)
              (SmallEtale.topology B Z.obj Z.property)
              (SmallEtale.topology B (s.piece i).obj (s.piece i).property)).obj G) ]
```

## Tag 09YR, a lemma

[Tag 09YR](https://stacks.math.columbia.edu/tag/09YR) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleFiniteSheaf_of_constructible_immersion_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ImmersionCover.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ImmersionCover.lean#L310). The attribute's comment: “sets and abelian groups”.

> **Stacks 09YR, for sheaves of sets and of abelian groups.** On a quasi-compact quasi-separated
> scheme, a sheaf with values in a concrete category is constructible as soon as there are
> constructible locally closed subschemes covering the scheme on each of which its inverse image is
> constructible.

```lean
public theorem isConstructibleFiniteSheaf_of_constructible_immersion_cover
    (F : Sheaf (SmallEtale.topology B X.obj X.property) D)
    {I : Type*} (T : I → B.Scheme) (j : ∀ i, T i ⟶ X)
    (hj : ∀ i, IsImmersion (B.inclusion.map (j i)))
    (hc : ∀ i, Topology.IsConstructible (Set.range (B.inclusion.map (j i)).base))
    (hcover : (Set.univ : Set X.obj) = ⋃ i, Set.range (B.inclusion.map (j i)).base)
    (hF : ∀ i, IsConstructibleFiniteSheaf B (T i)
      (((smallEtaleBaseChange B (j i)).sheafPullback D
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B (T i).obj (T i).property)).obj F)) :
    IsConstructibleFiniteSheaf B X F
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_constructible_immersion_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ImmersionCover.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ImmersionCover.lean#L361). The attribute's comment: “modules over a Noetherian ring”.

> **Stacks 09YR, for sheaves of modules over a Noetherian ring.** On a quasi-compact
> quasi-separated scheme, a sheaf of modules over a Noetherian ring is constructible as soon as there
> are constructible locally closed subschemes covering the scheme on each of which its inverse image
> is constructible.

```lean
public theorem isConstructibleModuleSheaf_of_constructible_immersion_cover
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R))
    {I : Type*} (T : I → B.Scheme) (j : ∀ i, T i ⟶ X)
    (hj : ∀ i, IsImmersion (B.inclusion.map (j i)))
    (hc : ∀ i, Topology.IsConstructible (Set.range (B.inclusion.map (j i)).base))
    (hcover : (Set.univ : Set X.obj) = ⋃ i, Set.range (B.inclusion.map (j i)).base)
    (hF : ∀ i, IsConstructibleModuleSheaf B (T i) R
      (((smallEtaleBaseChange B (j i)).sheafPullback (ModuleCat.{w} R)
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B (T i).obj (T i).property)).obj F)) :
    IsConstructibleModuleSheaf B X R F
```

## Tag 095F, a lemma

[Tag 095F](https://stacks.math.columbia.edu/tag/095F) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleFiniteSheaf_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean#L125). The attribute's comment: “sets and abelian groups”.

> **Stacks 095F for sheaves of sets and of abelian groups.** Let `X` be a scheme covered by the
> images of open immersions `U k ⟶ X`. A sheaf with values in a concrete category whose restriction
> to every `U k` is constructible is constructible.

```lean
public theorem isConstructibleFiniteSheaf_of_openCover (X : B.Scheme)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) D)
    {I : Type*} (U : I → B.Scheme) (j : ∀ k, U k ⟶ X)
    (hj : ∀ k, IsOpenImmersion (B.inclusion.map (j k)))
    (hcover : Set.univ = ⋃ k, Set.range (B.inclusion.map (j k)).base)
    (hlocal : ∀ k, IsConstructibleFiniteSheaf B (U k)
      (((smallEtaleBaseChange B (j k)).sheafPullback D
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B (U k).obj (U k).property)).obj F)) :
    IsConstructibleFiniteSheaf B X F
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean#L195). The attribute's comment: “modules over a Noetherian ring”.

> **Stacks 095F for sheaves of modules over a Noetherian ring.** Let `X` be a scheme covered by
> the images of open immersions `U k ⟶ X`. A sheaf of modules over a Noetherian ring whose
> restriction to every `U k` is constructible is constructible.

```lean
public theorem isConstructibleModuleSheaf_of_openCover (X : B.Scheme)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R))
    {I : Type*} (U : I → B.Scheme) (j : ∀ k, U k ⟶ X)
    (hj : ∀ k, IsOpenImmersion (B.inclusion.map (j k)))
    (hcover : Set.univ = ⋃ k, Set.range (B.inclusion.map (j k)).base)
    (hlocal : ∀ k, IsConstructibleModuleSheaf B (U k) R
      (((smallEtaleBaseChange B (j k)).sheafPullback (ModuleCat.{w} R)
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B (U k).obj (U k).property)).obj F)) :
    IsConstructibleModuleSheaf B X R F
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isConstructibleFiniteSheaf_iff_forall_restrict`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean#L165), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocalCriterionTag.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocalCriterionTag.lean#L22) (StacksFrontier): “sets and abelian groups: constructible iff constructible on every member of any open covering”.
- [`AlgebraicGeometry.isConstructibleModuleSheaf_iff_forall_restrict`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiDescent.lean#L236), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocalCriterionTag.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZariskiLocalCriterionTag.lean#L26) (StacksFrontier): “Noetherian-ring modules: constructible iff constructible on every member of any open covering”.

## Tag 095G, a lemma

[Tag 095G](https://stacks.math.columbia.edu/tag/095G) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleFiniteSheaf_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/InverseImage.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/InverseImage.lean#L259). The attribute's comment: “sets and abelian groups”.

> **Stacks 095G for sheaves of sets and of abelian groups.** The inverse image of a constructible
> sheaf with values in a concrete category along an arbitrary morphism of schemes is
> constructible.

```lean
public theorem isConstructibleFiniteSheaf_pullback {X Y : B.Scheme} (f : X ⟶ Y)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) D)
    (hF : IsConstructibleFiniteSheaf B Y F) :
    IsConstructibleFiniteSheaf B X
      (((smallEtaleBaseChange B f).sheafPullback D
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).obj F)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/InverseImage.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/InverseImage.lean#L302). The attribute's comment: “modules over a Noetherian ring”.

> **Stacks 095G for sheaves of modules over a Noetherian ring.** The inverse image of a
> constructible sheaf of modules over a Noetherian ring along an arbitrary morphism of schemes is
> constructible.

```lean
public theorem isConstructibleModuleSheaf_pullback {X Y : B.Scheme} (f : X ⟶ Y)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) (ModuleCat.{w} R))
    (hF : IsConstructibleModuleSheaf B Y R F) :
    IsConstructibleModuleSheaf B X R
      (((smallEtaleBaseChange B f).sheafPullback (ModuleCat.{w} R)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).obj F)
```

## Tag 03RZ, a lemma

[Tag 03RZ](https://stacks.math.columbia.edu/tag/03RZ) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleSetSheaf_limit_colimit_and_isWeakSerreClass_abelian_and_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsAndWeakSerre.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsAndWeakSerre.lean#L85). The attribute's comment: “the whole tag: part (1) finite limits and finite colimits of constructible sheaves of sets are constructible, part (2) the constructible abelian sheaves are a weak Serre subcategory, part (3) the constructible sheaves of modules over a Noetherian ring are a weak Serre subcategory. Unconditional: no hypothesis on the scheme and no instance the source does not name; part (3)'s ring is a Ring rather than a CommRing, which is more general than the source, and its Noetherian hypothesis is used by part (3) alone. The four component registrations are retained.”. References: SGA 4 IX (2.6).

> **Stacks 03RZ.** Let `X` be a scheme of a big étale site and `Λ` a Noetherian ring. Then
>
> 1. a finite limit and a finite colimit of constructible sheaves of sets on the small étale site
>    of `X` are constructible;
> 2. the constructible abelian sheaves on that site form a weak Serre subcategory of all abelian
>    sheaves on it; and
> 3. the constructible sheaves of `Λ`-modules on that site form a weak Serre subcategory of all
>    sheaves of `Λ`-modules on it.
>
> This is the whole tag in one statement, under no hypothesis on `X` and none on `Λ` beyond the
> source's own Noetherianness, which part (3) alone uses. Each part is proved by the theorem that
> states it alone: `AlgebraicGeometry.isConstructibleSetSheaf_limit` and
> `AlgebraicGeometry.isConstructibleSetSheaf_colimit` for part (1),
> `AlgebraicGeometry.constructibleAbelianSheaf_isWeakSerreClass` for part (2), and
> `AlgebraicGeometry.SmallEtale.isWeakSerreClass_isConstructibleModuleSheaf` for part (3). Those
> four registrations are retained, each stating its own part.
>
> The three parts are independent facts and not a chain: part (1) is about sheaves of sets and is
> not used for parts (2) and (3), which reduce to Tag 093U (2) and Tag 093U (3) respectively, so
> the conjunction asserts strictly more than any one of them.

```lean
public theorem isConstructibleSetSheaf_limit_colimit_and_isWeakSerreClass_abelian_and_module
    (B : BigEtaleSite.{u}) (X : B.Scheme) (Λ : Type r) [Ring Λ] [IsNoetherianRing Λ] :
    (∀ (I : Type v) [SmallCategory I] [FinCategory I]
        (F : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))),
        (∀ i, IsConstructibleSetSheaf B X (F.obj i)) →
          IsConstructibleSetSheaf B X (limit F) ∧
            IsConstructibleSetSheaf B X (colimit F)) ∧
      ObjectProperty.IsWeakSerreClass
        (fun F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1} =>
          IsConstructibleAbelianSheaf B X F) ∧
      ObjectProperty.IsWeakSerreClass
        (fun F : Sheaf (SmallEtale.topology B X.obj X.property)
          (ModuleCat.{max (u + 1) w} Λ) => IsConstructibleModuleSheaf B X Λ F)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean#L135). The attribute's comment: “constructible_sets_finite_limits_colimits”. References: SGA 4 IX (2.6), “(i bis) finite limits”.

> **Stacks 03RZ for sheaves of sets, finite limits.** A finite limit of constructible sheaves
> of sets on the small étale site of a scheme is constructible.

```lean
public theorem isConstructibleSetSheaf_limit
    (F : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
    (hF : ∀ i, IsConstructibleSetSheaf B X (F.obj i)) :
    IsConstructibleSetSheaf B X (limit F)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean#L148). The attribute's comment: “constructible_sets_finite_limits_colimits”. References: SGA 4 IX (2.6), “(i bis) finite colimits”.

> **Stacks 03RZ for sheaves of sets, finite colimits.** A finite colimit of constructible
> sheaves of sets on the small étale site of a scheme is constructible.

```lean
public theorem isConstructibleSetSheaf_colimit
    (F : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
    (hF : ∀ i, IsConstructibleSetSheaf B X (F.obj i)) :
    IsConstructibleSetSheaf B X (colimit F)
```

**`AlgebraicGeometry.SmallEtale.isWeakSerreClass_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLimitsSets.lean#L213). The attribute's comment: “constructible_modules_weak_serre”. References: SGA 4 IX (2.6).

> **Stacks 03RZ (3).** For `Λ` a Noetherian ring, the constructible sheaves of `Λ`-modules on
> the small étale site of a scheme form a weak Serre subcategory of all sheaves of `Λ`-modules on
> that site. There is no hypothesis on the scheme.
>
> The proof is the five term form of the weak Serre condition,
> `CategoryTheory.ObjectProperty.isWeakSerreClass_iff_prop_obj₂_of_exact`. Given an exact
> `ℱ₀ ⟶ ℱ₁ ⟶ ℱ₂ ⟶ ℱ₃ ⟶ ℱ₄` with the four outer terms constructible, fix an affine open and
> stratify all four of them on one constructible stratification of it with
> `AlgebraicGeometry.exists_stratification_isStratifiedSheaf_forall`. Inverse image to a stratum is
> exact by `AlgebraicGeometry.preservesFiniteLimits_smallEtaleSheafPullback_moduleCat`, so the
> restricted five term sequence is still exact, and on a stratum constructibility is local
> constancy of finite type, which is a weak Serre condition by Tag 093U (3). Hence the restriction
> of `ℱ₂` to each stratum is locally constant of finite type, which is constructibility of `ℱ₂`.

```lean
public theorem SmallEtale.isWeakSerreClass_isConstructibleModuleSheaf :
    ObjectProperty.IsWeakSerreClass
      (fun F : Sheaf (SmallEtale.topology B X.obj X.property)
        (ModuleCat.{max (u + 1) w} Λ) => IsConstructibleModuleSheaf B X Λ F)
```

**`AlgebraicGeometry.constructibleAbelianSheaf_isWeakSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/WeakSerreAbelian.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/WeakSerreAbelian.lean#L213). The attribute's comment: “constructible_abelian_weak_serre”. References: SGA 4 IX (2.6), “(ii)+ker/coker abelian”.

> **Stacks 03RZ for abelian sheaves.** The constructible sheaves of abelian groups on the small
> étale site of a scheme form a weak Serre subcategory of all abelian sheaves on that site.

```lean
public instance constructibleAbelianSheaf_isWeakSerreClass :
    ObjectProperty.IsWeakSerreClass
      (fun F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1} =>
        IsConstructibleAbelianSheaf B X F)
```

## Tag 09YS, a lemma

[Tag 09YS](https://stacks.math.columbia.edu/tag/09YS) in the Stacks Project.

**`AlgebraicGeometry.isConstructible_setOf_surjective_etaleStalk_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean#L385). The attribute's comment: “part (1), surjectivity”.

> **Stacks 09YS, part (1), surjectivity.** Let `X` be a quasi-compact quasi-separated scheme.
> For a map of constructible sheaves of sets on the small étale site of `X`, the set of points of
> `X` at which the induced map of geometric stalks is surjective is constructible.

```lean
public theorem isConstructible_setOf_surjective_etaleStalk_map
    (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))} (φ : F ⟶ G)
    (hF : IsConstructibleSetSheaf B X F) (hG : IsConstructibleSetSheaf B X G) :
    IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
      Function.Surjective
        ((etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).map φ.hom)}
```

**`AlgebraicGeometry.isConstructible_setOf_injective_etaleStalk_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean#L400). The attribute's comment: “part (1), injectivity”.

> **Stacks 09YS, part (1), injectivity.** Let `X` be a quasi-compact quasi-separated scheme.
> For a map of constructible sheaves of sets on the small étale site of `X`, the set of points of
> `X` at which the induced map of geometric stalks is injective is constructible.

```lean
public theorem isConstructible_setOf_injective_etaleStalk_map
    (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))} (φ : F ⟶ G)
    (hF : IsConstructibleSetSheaf B X F) (hG : IsConstructibleSetSheaf B X G) :
    IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
      Function.Injective
        ((etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).map φ.hom)}
```

**`AlgebraicGeometry.isConstructible_setOf_etaleStalk_map_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean#L416). The attribute's comment: “part (1), isomorphic to a given map of sets”.

> **Stacks 09YS, part (1), prescribed isomorphism class.** Let `X` be a quasi-compact
> quasi-separated scheme and let `m₀` be a map of sets. For a map of constructible sheaves of sets
> on the small étale site of `X`, the set of points of `X` at which the induced map of geometric
> stalks is isomorphic to `m₀` is constructible.

```lean
public theorem isConstructible_setOf_etaleStalk_map_iso {A₀ : Type v} {C₀ : Type w}
    (m₀ : A₀ → C₀) (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))} (φ : F ⟶ G)
    (hF : IsConstructibleSetSheaf B X F) (hG : IsConstructibleSetSheaf B X G) :
    IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
      ∃ (b : (etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).obj F.obj ≃ A₀)
        (d : (etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).obj G.obj ≃ C₀),
        ∀ z, d ((etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).map φ.hom z) =
          m₀ (b z)}
```

**`AlgebraicGeometry.isConstructible_supportSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean#L541). The attribute's comment: “part (2)”.

> **Stacks 09YS, part (2).** Let `X` be a quasi-compact quasi-separated scheme. The support of
> a constructible abelian sheaf on the small étale site of `X` is constructible.

```lean
public theorem isConstructible_supportSheaf (B : BigEtaleSite.{u}) (X : B.Scheme)
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] [UnivLE.{u, w}]
    [∀ (Z : B.Scheme) (V : SmallEtale B Z.obj Z.property),
      HasWeakSheafify ((SmallEtale.topology B Z.obj Z.property).over V) AddCommGrpCat.{w}]
    [∀ (Z : B.Scheme) (V : SmallEtale B Z.obj Z.property),
      ((SmallEtale.topology B Z.obj Z.property).over V).WEqualsLocallyBijective
        AddCommGrpCat.{w}]
    [∀ (Y Z : B.Scheme) (f : Z ⟶ Y),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous AddCommGrpCat.{w}
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B Z.obj Z.property)).IsRightAdjoint]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{w})
    (hF : IsConstructibleAbelianSheaf B X F) :
    IsConstructible (supportSheaf B X.obj X.property F)
```

**`AlgebraicGeometry.isConstructible_support_moduleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocus.lean#L573). The attribute's comment: “part (3)”.

> **Stacks 09YS, part (3).** Let `X` be a quasi-compact quasi-separated scheme and let `Λ` be a
> Noetherian ring. The support of a constructible sheaf of `Λ`-modules on the small étale site of
> `X` — the set of points carrying a nonzero geometric stalk — is constructible.

```lean
public theorem isConstructible_support_moduleSheaf (B : BigEtaleSite.{u}) (X : B.Scheme)
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (Λ : Type r) [CommRing Λ]
    [IsNoetherianRing Λ] [UnivLE.{u, w}]
    [PreservesFilteredColimitsOfSize.{max u w, max u w} (forget (ModuleCat.{max u w} Λ))]
    [∀ (Z : B.Scheme) (V : SmallEtale B Z.obj Z.property),
      HasWeakSheafify ((SmallEtale.topology B Z.obj Z.property).over V) (ModuleCat.{max u w} Λ)]
    [∀ (Z : B.Scheme) (V : SmallEtale B Z.obj Z.property),
      ((SmallEtale.topology B Z.obj Z.property).over V).WEqualsLocallyBijective
        (ModuleCat.{max u w} Λ)]
    [∀ (Y Z : B.Scheme) (f : Z ⟶ Y),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{max u w} Λ)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B Z.obj Z.property)).IsRightAdjoint]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max u w} Λ))
    (hF : IsConstructibleModuleSheaf B X Λ F) :
    IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
      ¬ IsZero (etaleStalk B X.obj X.property t F.obj)}
```

**`AlgebraicGeometry.isConstructible_etaleStalk_map_loci_and_supports`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocusLociAndSupports.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StalkLocusLociAndSupports.lean#L68). The attribute's comment: “parts (1), (2) and (3), as the conjunction of the three constructibility claims”.

> **Stacks 09YS.** Let `X` be a quasi-compact quasi-separated scheme.
>
> 1. For a map `φ : F ⟶ G` of constructible sheaves of sets on the small étale site of `X`, each of
>    the three sets of points of `X` at which the induced map of geometric stalks is surjective, is
>    injective, or is isomorphic to a prescribed map of sets `m₀`, is constructible.
> 2. The support of a constructible abelian sheaf on the small étale site of `X` is constructible.
> 3. For `Λ` a Noetherian ring, the support of a constructible sheaf of `Λ`-modules on the small
>    étale site of `X` is constructible.
>
> Sheaves of sets have values in the universe `u + 1` of the site; abelian sheaves, resp. sheaves of
> `Λ`-modules for `Λ : Type r`, have values in any universe containing that of the site, resp. that
> of the site and of `Λ`. The statement has no hypothesis beyond the source's: every coefficient
> condition the general parts `isConstructible_supportSheaf` and
> `isConstructible_support_moduleSheaf` assume is proved at these universes inside the proof.
>
> Part (1) is `isConstructible_setOf_surjective_etaleStalk_map`,
> `isConstructible_setOf_injective_etaleStalk_map` and `isConstructible_setOf_etaleStalk_map_iso`,
> part (2) is `isConstructible_supportSheaf` and part (3) is
> `isConstructible_support_moduleSheaf`.

```lean
public theorem isConstructible_etaleStalk_map_loci_and_supports (B : BigEtaleSite.{u})
    (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] :
    (∀ (F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) (φ : F ⟶ G),
        IsConstructibleSetSheaf B X F → IsConstructibleSetSheaf B X G →
        IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
            Function.Surjective
              ((etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).map φ.hom)} ∧
          IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
            Function.Injective
              ((etaleStalkPresheafFunctor B X.obj X.property t (Type (u + 1))).map φ.hom)} ∧
          ∀ (A₀ : Type v) (C₀ : Type w₀) (m₀ : A₀ → C₀),
            IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
              ∃ (b : (etaleStalkPresheafFunctor B X.obj X.property t
                  (Type (u + 1))).obj F.obj ≃ A₀)
                (d : (etaleStalkPresheafFunctor B X.obj X.property t
                  (Type (u + 1))).obj G.obj ≃ C₀),
                ∀ z, d ((etaleStalkPresheafFunctor B X.obj X.property t
                  (Type (u + 1))).map φ.hom z) = m₀ (b z)}) ∧
      (∀ F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{max (u + 1) w},
          IsConstructibleAbelianSheaf B X F →
            IsConstructible (supportSheaf B X.obj X.property F)) ∧
      ∀ (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ]
        (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r w} Λ)),
        IsConstructibleModuleSheaf B X Λ F →
          IsConstructible {x : X.obj | ∃ t : GeometricPoint X.obj, t.LiesOver x ∧
            ¬ IsZero (etaleStalk B X.obj X.property t F.obj)}
```

## Tag 095P, a lemma

[Tag 095P](https://stacks.math.columbia.edu/tag/095P) in the Stacks Project.

**`AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleAbelianSheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianEssentiallyConstantColimit.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianEssentiallyConstantColimit.lean#L109). The attribute's comment: “part (2), sheaves of abelian groups”.

> **Stacks 095P, part (2).** Let `X` be a quasi-compact quasi-separated scheme and let
> `F = colim_{i ∈ I} F_i` be a filtered colimit of abelian sheaves on `X_étale`. If `F` and all the
> `F_i` are constructible, then the ind-object `F_i` is essentially constant with value `F`.
>
> Nothing is assumed. Abelian groups are `ULift ℤ`-modules, a ring which is Noetherian and lives in
> the coefficient universe, so the system is carried to one of sheaves of modules by
> `AlgebraicGeometry.isConstructibleModuleSheaf_uliftIntEquivalence`, part (3) of the tag applies to
> it with nothing assumed, and the witness is brought back along the equivalence of sheaf
> categories, which preserves the colimit and is fully faithful.

```lean
public theorem exists_isEssentiallyConstantWith_of_isConstructibleAbelianSheaf_colimit
    (X : B.Scheme) [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    {I : Type v} [Category.{v'} I] [IsFiltered I] [EssentiallySmall.{u + 1} I]
    (F : I ⥤ Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1})
    (t : Cocone F) (ht : IsColimit t)
    (hF : ∀ i, IsConstructibleAbelianSheaf B X (F.obj i))
    (hcolim : IsConstructibleAbelianSheaf B X t.pt) :
    ∃ (i : I) (r : t.pt ⟶ F.obj i),
      EssentiallyConstantInd.IsEssentiallyConstantWith F t i r
```

**`AlgebraicGeometry.isEssentiallyConstantWith_of_isConstructibleAbelianSheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/EssentiallyConstantColimit.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/EssentiallyConstantColimit.lean#L126). The attribute's comment: “part (2), sheaves of abelian groups”.

> **Stacks 095P, part (2).** Let `X` be a quasi-compact quasi-separated scheme and let
> `F = colim_{i ∈ I} F_i` be a filtered colimit of abelian sheaves on `X_étale`. If `F` and all the
> `F_i` are constructible, then the ind-object `F_i` is essentially constant with value `F`.
>
> Nothing beyond the instance hypotheses is assumed: the input of the sheaves-of-abelian-groups case
> of Stacks 09Z4, Stacks 095N for `ℤ`-modules, is
> `AlgebraicGeometry.hasFiniteShriekPresentation_of_isConstructibleModuleSheaf_int`.

```lean
public theorem isEssentiallyConstantWith_of_isConstructibleAbelianSheaf_colimit
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V) AddCommGrpCat.{u + 1}]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{u + 1} ℤ)
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V) (ModuleCat.{u + 1} ℤ)]
    {I : Type v} [Category.{v'} I] [IsFiltered I] [EssentiallySmall.{u + 1} I]
    (F : I ⥤ Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1})
    (t : Cocone F) (ht : IsColimit t)
    (hF : ∀ i, IsConstructibleAbelianSheaf B X (F.obj i))
    (hcolim : IsConstructibleAbelianSheaf B X t.pt) :
    ∃ (i : I) (r : t.pt ⟶ F.obj i),
      EssentiallyConstantInd.IsEssentiallyConstantWith F t i r
```

**`AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleModuleSheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleEssentiallyConstantColimit.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleEssentiallyConstantColimit.lean#L43). The attribute's comment: “part (3), with 095N discharged”.

> Let `X` be a quasi-compact quasi-separated scheme, let `Λ` be a
> Noetherian ring, and let `F = colim_{i ∈ I} F_i` be a filtered colimit of sheaves of `Λ`-modules
> on `X_étale`. If `F` and all the `F_i` are constructible, then the ind-object `F_i` is essentially
> constant with value `F`.

```lean
public theorem exists_isEssentiallyConstantWith_of_isConstructibleModuleSheaf_colimit
    (B : BigEtaleSite.{u}) (X : B.Scheme) (R : Type (u + 1)) [CommRing R] [IsNoetherianRing R]
    [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{u + 1} R)
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V) (ModuleCat.{u + 1} R)]
    {I : Type v} [Category.{v'} I] [IsFiltered I] [EssentiallySmall.{u + 1} I]
    (F : I ⥤ Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R))
    (t : Cocone F) (ht : IsColimit t)
    (hF : ∀ i, IsConstructibleModuleSheaf B X R (F.obj i))
    (hcolim : IsConstructibleModuleSheaf B X R t.pt) :
    ∃ (i : I) (r : t.pt ⟶ F.obj i),
      EssentiallyConstantInd.IsEssentiallyConstantWith F t i r
```

**`AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleSetSheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SetEssentiallyConstantColimit.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SetEssentiallyConstantColimit.lean#L45). The attribute's comment: “part (1), sheaves of sets”.

> Let `X` be a quasi-compact quasi-separated scheme and let `F = colim_{i ∈ I} F_i` be a
> filtered colimit of sheaves of sets on `X_étale`. If `F` and all the `F_i` are constructible, then
> the ind-object `F_i` is essentially constant with value `F`.

```lean
public theorem exists_isEssentiallyConstantWith_of_isConstructibleSetSheaf_colimit
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    {I : Type v} [Category.{v'} I] [IsFiltered I] [EssentiallySmall.{u + 1} I]
    (F : I ⥤ Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1)))
    (t : Cocone F) (ht : IsColimit t)
    (hF : ∀ i, IsConstructibleSetSheaf B X (F.obj i))
    (hcolim : IsConstructibleSetSheaf B X t.pt) :
    ∃ (i : I) (r : t.pt ⟶ F.obj i),
      EssentiallyConstantInd.IsEssentiallyConstantWith F t i r
```

**`AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleModuleSheaf_colimit'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean#L298). The attribute's comment: “part (3), for a Noetherian coefficient ring in any universe”.

> **Stacks 095P, part (3), for a coefficient ring in any universe.** A filtered colimit of
> constructible sheaves of `R`-modules whose value is constructible is essentially constant as an
> ind-object.
>
> The cocone is carried to `Shrink.{u + 1} R`-modules by the equivalence of sheaf categories,
> which preserves the colimit, and the witness found there is brought back by
> `CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantWith.of_equivalence`.

```lean
public theorem exists_isEssentiallyConstantWith_of_isConstructibleModuleSheaf_colimit'
    [IsNoetherianRing R] [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    {I : Type v} [Category.{v₀} I] [IsFiltered I] [EssentiallySmall.{u + 1} I]
    (F : I ⥤ Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R))
    (t : Cocone F) (ht : IsColimit t)
    (hF : ∀ i, IsConstructibleModuleSheaf B X R (F.obj i))
    (hcolim : IsConstructibleModuleSheaf B X R t.pt) :
    ∃ (i : I) (r : t.pt ⟶ F.obj i),
      EssentiallyConstantInd.IsEssentiallyConstantWith F t i r
```

## Tag 095I, a lemma

[Tag 095I](https://stacks.math.columbia.edu/tag/095I) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleModuleEtaleSheaf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/TensorProduct.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/TensorProduct.lean#L55).

> **Stacks 095I.** Let `X` be a scheme and `Λ` a Noetherian ring. The tensor product of two
> constructible sheaves of `Λ`-modules on `X_étale` is a constructible sheaf of `Λ`-modules.

```lean
public theorem isConstructibleModuleEtaleSheaf_tensor (B : BigEtaleSite.{u}) (X : B.Scheme)
    (Λ : Type (max (u + 1) w)) [CommRing Λ] [IsNoetherianRing Λ]
    (F G : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w} Λ))
    (hF : IsConstructibleModuleEtaleSheaf B X Λ F) (hG : IsConstructibleModuleEtaleSheaf B X Λ G) :
    IsConstructibleModuleEtaleSheaf B X Λ (F ⊗ G)
```

**`Stacks.EtaleCohomology.isConstructibleModuleSheaf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/TensorProduct.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/TensorProduct.lean#L111).

> **Stacks 095I.** The tensor product of two constructible sheaves of `Λ`-modules on the small
> étale site of a scheme, for `Λ` a Noetherian ring, is a constructible sheaf of `Λ`-modules.

```lean
theorem isConstructibleModuleSheaf_tensor (B : BigEtaleSite.{u}) (X : B.Scheme)
    (Λ : Type (max (u + 1) w)) [CommRing Λ] [IsNoetherianRing Λ]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{max (u + 1) w} Λ)
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    (F G : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w} Λ))
    (hF : IsConstructibleModuleSheaf B X Λ F) (hG : IsConstructibleModuleSheaf B X Λ G) :
    IsConstructibleModuleSheaf B X Λ (F ⊗ G)
```

## Tag 0GKB, a lemma

[Tag 0GKB](https://stacks.math.columbia.edu/tag/0GKB) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleModuleSheaf_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ExtensionOfScalars.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ExtensionOfScalars.lean#L209).

> Extension of scalars along a homomorphism of Noetherian rings preserves
> constructibility on the small étale site.

```lean
public theorem isConstructibleModuleSheaf_extendScalars
    (B : BigEtaleSite.{u}) (X : B.Scheme)
    (R : Type r) (S : Type s) [CommRing R] [CommRing S]
    [IsNoetherianRing R] [IsNoetherianRing S] (f : R →+* S)
    [HasWeakSheafify (SmallEtale.topology B X.1 X.property)
      (ModuleCat.{max r s w} S)]
    [∀ (A T : B.Scheme) (g : T ⟶ A),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous
        (ModuleCat.{max r s w} R)
        (SmallEtale.topology B A.1 A.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V)
        (ModuleCat.{max r s w} R)]
    [∀ (A T : B.Scheme) (g : T ⟶ A),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous
        (ModuleCat.{max r s w} S)
        (SmallEtale.topology B A.1 A.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V)
        (ModuleCat.{max r s w} S)]
    (F : Sheaf (SmallEtale.topology B X.1 X.property)
      (ModuleCat.{max r s w} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsConstructibleModuleSheaf B X S
      ((extendScalarsSheaf (SmallEtale.topology B X.1 X.property) R S f).obj F)
```

**`AlgebraicGeometry.SmallEtale.isConstructibleModuleSheaf_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstructibleExtendScalars.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstructibleExtendScalars.lean#L279).

> **Stacks 0GKB.** Extension of scalars along a homomorphism of Noetherian rings preserves
> constructibility of a sheaf of modules on the small étale site.

```lean
public theorem isConstructibleModuleSheaf_extendScalars
    (B : BigEtaleSite.{u}) (X : B.Scheme)
    (R : Type r) (S : Type s) [CommRing R] [CommRing S]
    [IsNoetherianRing R] [IsNoetherianRing S] (f : R →+* S)
    [HasWeakSheafify (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max r s w} S)]
    [∀ (A T : B.Scheme) (g : T ⟶ A),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous
        (ModuleCat.{max r s w} R)
        (SmallEtale.topology B A.obj A.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V)
        (ModuleCat.{max r s w} R)]
    [∀ (A T : B.Scheme) (g : T ⟶ A),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous
        (ModuleCat.{max r s w} S)
        (SmallEtale.topology B A.obj A.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V)
        (ModuleCat.{max r s w} S)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max r s w} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsConstructibleModuleSheaf B X S
      ((Sheaf.composeAndSheafify (SmallEtale.topology B X.obj X.property)
        (ModuleCat.extendScalars.{r, s, max r s w} f)).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.71, Tag 05BE](https://stacks.math.columbia.edu/tag/05BE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
