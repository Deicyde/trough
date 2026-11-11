---
declaration: section
origin: cited
lean: AlgebraicGeometry.existsUnique_open_of_isSubterminal_topos, AlgebraicGeometry.existsUnique_open_of_isSubterminal, AlgebraicGeometry.SmallEtale.etaleGerm_eq_zero_iff_mem_zeroOpen, AlgebraicGeometry.SmallEtale.map_eq_zero_iff_range_subset_zeroOpen, AlgebraicGeometry.SmallEtale.zeroOpen, AlgebraicGeometry.SmallEtale.map_eq_zero_iff_le_zeroOpen, AlgebraicGeometry.SmallEtale.supportSection, AlgebraicGeometry.supportSection
statement: formalized
proof: formalized
---

# 59.31 Supports of abelian sheaves

Section 59.31 of the Stacks Project, [Tag 04FQ](https://stacks.math.columbia.edu/tag/04FQ). 5 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04HV, a lemma

[Tag 04HV](https://stacks.math.columbia.edu/tag/04HV) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_open_of_isSubterminal_topos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/ExistenceClause.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/ExistenceClause.lean#L465). The attribute's comment: “the case of a subterminal object of the topos of `AlgebraicGeometry.smallEtaleRingedSite`, whose sections are of `Type u`; this is `AlgebraicGeometry.existsUnique_open_of_isSubterminal`, which carries the tag in its own generality `Type (max u v)`, instantiated at `v := u` with no transport in between”.

> **Stacks 04HV for a subterminal object of the topos of the small étale ringed site.** A
> subsheaf of the final object of `(Sh(S_étale), 𝒪_S)` is represented by exactly one open
> subscheme of `S`.
>
> This is `AlgebraicGeometry.existsUnique_open_of_isSubterminal` with its free sections universe
> instantiated at the universe `u` of the sections of
> `AlgebraicGeometry.smallEtaleRingedSite`, a `RingedSite.{u + 1, u, u}`.  Nothing is transported:
> `CategoryTheory.IsSubterminal` is a condition in the sheaf category and the representability
> conclusion is about the same sheaf, and the two sides are the same category, because
> `AlgebraicGeometry.RingedTopos.Topos` of that ringed site *is*
> `CategoryTheory.Sheaf (SmallEtale.topology B S hS) (Type u)`.

```lean
theorem existsUnique_open_of_isSubterminal_topos (X : B.Scheme)
    (F : (RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property)).Topos)
    (hF : IsSubterminal F) :
    ∃! W : X.obj.Opens,
      Nonempty (F ≅
        (presheafToSheaf (SmallEtale.topology B X.obj X.property) (Type u)).obj
          ((SmallEtale.inclusion B X.obj X.property ⋙
            Over.post (X := B.obj X.obj X.property) B.inclusion).op ⋙
            uliftYoneda.{u}.obj (Over.mk W.ι)))
```

**`AlgebraicGeometry.existsUnique_open_of_isSubterminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubterminalSheaves.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubterminalSheaves.lean#L722).

> A subterminal sheaf on the small étale site is represented by a unique open
> subscheme of the base.

```lean
public theorem existsUnique_open_of_isSubterminal
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : smallEtaleTopos.{u, max (u + 1) v} B S hS)
    (hF : IsSubterminal F) :
    ∃! W : S.Opens,
      Nonempty (F ≅
        (presheafToSheaf (SmallEtale.topology B S hS)
          (Type (max (u + 1) v))).obj
          ((SmallEtale.inclusion B S hS ⋙
            Over.post (X := B.obj S hS) B.inclusion).op ⋙
            uliftYoneda.{max (u + 1) v}.obj (Over.mk W.ι)))
```

## Tag 04FR, a lemma

[Tag 04FR](https://stacks.math.columbia.edu/tag/04FR) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.etaleGerm_eq_zero_iff_mem_zeroOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkVanishing.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FiniteSupportStalkVanishing.lean#L89). The attribute's comment: “part (3): a germ vanishes exactly when the lift lands in the zero locus”.

> **Stacks 04FR, part (3).** A germ vanishes exactly when the lift lands in the maximal open
> zero locus of the section.
>
> A geometric point `ū` of the object `W` of the small étale site is a lift `q` to `W` of a geometric
> point `t` of `S`, the relation `t = (W → S) ∘ ū` of the source being the defining condition on a
> lift; so quantifying over `t` and over `q` is quantifying over the geometric points of `W`. The
> germ `etaleGerm … t F.obj W q a` is the source's class of `(U, ū, σ)` in `F_s̄`, and
> `zeroOpen … W a` is the source's `W`, so this is the asserted equivalence
> `(U, ū, σ) = 0 in F_s̄ ↔ ū ∈ W`.
>
> The coefficient universe `v` is free, which is more general than the source; `UnivLE.{u, v}` and
> the existence of the colimit are what that extra generality costs, and both are automatic
> instances at `v = u`, so at the source's generality the statement carries no hypothesis. They are
> size conditions for the stalk to be formed at all, not mathematical hypotheses: `etaleGerm` is a
> colimit injection and does not typecheck without the colimit.

```lean
public theorem etaleGerm_eq_zero_iff_mem_zeroOpen (W : SmallEtale B S hS)
    (q : (geometricPointFiber B S hS t).obj W) (a : F.obj.obj (op W)) :
    etaleGerm B S hS t F.obj W q a = 0 ↔
      q.1.base default ∈
        (zeroOpen B S hS F W a : Set ((SmallEtale.toScheme B S hS).obj W))
```

**`AlgebraicGeometry.SmallEtale.map_eq_zero_iff_range_subset_zeroOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L552). The attribute's comment: “part (2): vanishing over the image”. References: SGA 2 XIV (1.8.2.1), “abelian, image criterion”.

> A section pulls back to zero along an arbitrary arrow of the small étale site precisely when
> the image of that arrow is contained in its maximal Zariski open zero locus.

```lean
public theorem map_eq_zero_iff_range_subset_zeroOpen
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (σ : F.obj.obj (op U))
    (V : SmallEtale B S hS) (f : V ⟶ U) :
    F.obj.map f.op σ = 0 ↔
      Set.range ((SmallEtale.toScheme B S hS).map f).base ⊆
        (zeroOpen B S hS F U σ : Set ((SmallEtale.toScheme B S hS).obj U))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SmallEtale.zeroOpen`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L188), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L395) (StacksFrontier): “part (1): maximal open zero locus”.
- [`AlgebraicGeometry.SmallEtale.map_eq_zero_iff_le_zeroOpen`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L272), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L397) (StacksFrontier): “part (1): vanishing and maximality on Zariski opens”.

## Tag 04FS, a definition

[Tag 04FS](https://stacks.math.columbia.edu/tag/04FS) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.supportSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L196). The attribute's comment: “support of a section”. References: SGA 4 VIII (6.6), “support of a section”.

> The support of a section of an abelian sheaf on the small étale site is the complement of its
> maximal Zariski open zero locus.

```lean
public def supportSection (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s : F.obj.obj (op U)) :
    Set ((SmallEtale.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.SmallEtale.map_eq_zero_iff_le_zeroOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L272). The attribute's comment: “support of a section”. References: SGA 2 XIV (1.8.2.1), “abelian, s'=0”.

> Along an open immersion of the small étale site, a section restricts to zero precisely when the
> image is contained in the maximal zero open.

```lean
public theorem map_eq_zero_iff_le_zeroOpen
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s : F.obj.obj (op U))
    (V : SmallEtale B S hS) (f : V ⟶ U)
    [IsOpenImmersion ((SmallEtale.toScheme B S hS).map f)] :
    F.obj.map f.op s = 0 ↔
      ((SmallEtale.toScheme B S hS).map f).opensRange ≤ zeroOpen B S hS F U s
```

**`AlgebraicGeometry.supportSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSection.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSection.lean#L136). The attribute's comment: “support\_section”.

> The support of a section is the complement of its maximal Zariski open
> zero locus.

```lean
public def supportSection (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s : F.obj.obj (op U)) :
    Set ((SmallEtale.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.zero_restrict_iff_image_le_zeroOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSection.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSection.lean#L146). The attribute's comment: “support\_section”.

> On an open immersion, the section vanishes precisely when the image is
> contained in the maximal zero open.

```lean
public theorem zero_restrict_iff_image_le_zeroOpen (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s : F.obj.obj (op U))
    (V : SmallEtale B S hS) (f : V ⟶ U)
    [IsOpenImmersion ((SmallEtale.toScheme B S hS).map f)] :
    F.obj.map f.op s = 0 ↔
  ((SmallEtale.toScheme B S hS).map f).opensRange ≤ zeroOpen B S hS F U s
```

**`AlgebraicGeometry.supportSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSheaf.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSheaf.lean#L76). The attribute's comment: “support\_sheaf”.

> The points of a scheme at which a geometric stalk of an abelian étale
> sheaf is nonzero.

```lean
public def supportSheaf : Set S
```

**`AlgebraicGeometry.mem_supportSheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSheaf.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportSheaf.lean#L133). The attribute's comment: “support\_sheaf”. References: SGA 4 VIII (6.6), “support of a sheaf”.

> Nonvanishing of a stalk is independent of the geometric point above `x`.

```lean
public theorem mem_supportSheaf_iff (p : GeometricPoint S) (x : S)
    (hp : GeometricPoint.LiesOver p x) :
    x ∈ supportSheaf B S hS F ↔
      ¬ IsZero (etaleStalk B S hS p
        (F.obj ⋙ AddCommGrpCat.uliftFunctor.{u, v}))
```

## Tag 04FT, a lemma

[Tag 04FT](https://stacks.math.columbia.edu/tag/04FT) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isClosed_supportSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L621). The attribute's comment: “the support of a section is closed”.

> The support of a section of an abelian étale sheaf is closed.

```lean
public theorem isClosed_supportSection
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s : F.obj.obj (op U)) :
    IsClosed (supportSection B S hS F U s)
```

**`AlgebraicGeometry.SmallEtale.supportSection_add_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L629). The attribute's comment: “the support of a sum of sections”.

> The support of a sum of sections is contained in the union of their supports.

```lean
public theorem supportSection_add_subset
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (U : SmallEtale B S hS) (s s' : F.obj.obj (op U)) :
    supportSection B S hS F U (s + s') ⊆
      supportSection B S hS F U s ∪ supportSection B S hS F U s'
```

**`AlgebraicGeometry.SmallEtale.supportSection_map_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSections.lean#L659). The attribute's comment: “the support under a morphism of sheaves”.

> A morphism of abelian sheaves cannot enlarge the support of a section.

```lean
public theorem supportSection_map_subset
    (F G : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{v})
    (φ : F ⟶ G) (U : SmallEtale B S hS) (s : F.obj.obj (op U)) :
    supportSection B S hS G U (φ.hom.app (op U) s) ⊆ supportSection B S hS F U s
```

**`AlgebraicGeometry.supportSheaf_eq_iUnion_image_supportSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean#L134). The attribute's comment: “part (4)”.

> **Stacks 04FT, part (4).** The support of an abelian sheaf on the small étale site is the
> union, over all objects of the site and all sections of the sheaf over them, of the images in the
> base scheme of the supports of those sections.

```lean
public theorem supportSheaf_eq_iUnion_image_supportSection :
    AlgebraicGeometry.supportSheaf B S hS F =
      ⋃ (U : SmallEtale B S hS), ⋃ (a : F.obj.obj (op U)),
        (B.inclusion.map U.obj.hom).base '' supportSection B S hS F U a
```

**`AlgebraicGeometry.supportSheaf_subset_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean#L163). The attribute's comment: “part (5)”.

> **Stacks 04FT, part (5).** If a map of abelian sheaves on the small étale site is surjective,
> that is locally surjective, then the support of its target is contained in the support of its
> source.

```lean
public theorem supportSheaf_subset_of_isLocallySurjective (φ : F ⟶ G)
    [Sheaf.IsLocallySurjective φ] :
    AlgebraicGeometry.supportSheaf B S hS G ⊆ AlgebraicGeometry.supportSheaf B S hS F
```

**`AlgebraicGeometry.supportSheaf_subset_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean#L192). The attribute's comment: “part (6)”.

> **Stacks 04FT, part (6).** If a map of abelian sheaves on the small étale site is injective,
> then the support of its source is contained in the support of its target.

```lean
public theorem supportSheaf_subset_of_injective (φ : F ⟶ G)
    (hφ : ∀ U, Function.Injective (φ.hom.app U)) :
    AlgebraicGeometry.supportSheaf B S hS F ⊆ AlgebraicGeometry.supportSheaf B S hS G
```

**`AlgebraicGeometry.isClosed_supportSection_and_supportSheaf_eq_iUnion_image_supportSection_and_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSheafSections.lean#L247).

> **Stacks Project, Tag 04FT.** Let `S` be a scheme, let `F` be an abelian sheaf on the small
> étale site of `S`, let `U` be an object of that site and let `σ ∈ F(U)`. Then
>
> 1. the support of `σ` is closed in `U`;
> 2. the support of `σ + σ'` is contained in the union of the supports of `σ` and `σ'`, for every
>    `σ' ∈ F(U)`;
> 3. for every map `φ : F ⟶ G` of abelian sheaves on the site, the support of `φ(σ)` is contained
>    in the support of `σ`;
> 4. the support of `F` is the union of the images in `S` of the supports of all local sections
>    of `F`;
> 5. if `φ : F ⟶ G` is surjective then the support of `G` is contained in the support of `F`;
> 6. if `φ : F ⟶ G` is injective then the support of `F` is contained in the support of `G`,
>
> the support of a section being `AlgebraicGeometry.SmallEtale.supportSection` of Stacks 04FS and
> the support of a sheaf being `AlgebraicGeometry.supportSheaf`.
>
> This is the whole tag in one statement, under exactly the source's hypotheses: nothing beyond the
> site, the sheaf, the object and the section is assumed, and the further sheaf `G` and map `φ` of
> parts (3), (5) and (6) are quantified where the source introduces them. Surjectivity in part (5)
> is local surjectivity, `CategoryTheory.Sheaf.IsLocallySurjective`, which is what makes a map of
> abelian sheaves an epimorphism; injectivity in part (6) is injectivity on every group of sections.
> Each part is proved by the theorem of this chapter that states it alone:
> `AlgebraicGeometry.SmallEtale.isClosed_supportSection`,
> `AlgebraicGeometry.SmallEtale.supportSection_add_subset` and
> `AlgebraicGeometry.SmallEtale.supportSection_map_subset`, in
> `StacksFrontier.AlgebraicGeometry.Etale.SupportSections`, for parts (1), (2) and (3); and
> `AlgebraicGeometry.supportSheaf_eq_iUnion_image_supportSection`,
> `AlgebraicGeometry.supportSheaf_subset_of_isLocallySurjective` and
> `AlgebraicGeometry.supportSheaf_subset_of_injective`, above, for parts (4), (5) and (6). Those six
> registrations are retained, each stating its own part of the tag.

```lean
public theorem isClosed_supportSection_and_supportSheaf_eq_iUnion_image_supportSection_and_subset
    (U : SmallEtale B S hS) (σ : F.obj.obj (op U)) :
    IsClosed (supportSection B S hS F U σ) ∧
      (∀ σ' : F.obj.obj (op U), supportSection B S hS F U (σ + σ') ⊆
        supportSection B S hS F U σ ∪ supportSection B S hS F U σ') ∧
      (∀ φ : F ⟶ G, supportSection B S hS G U (φ.hom.app (op U) σ) ⊆
        supportSection B S hS F U σ) ∧
      (AlgebraicGeometry.supportSheaf B S hS F =
        ⋃ (V : SmallEtale B S hS), ⋃ (a : F.obj.obj (op V)),
          (B.inclusion.map V.obj.hom).base '' supportSection B S hS F V a) ∧
      (∀ φ : F ⟶ G, Sheaf.IsLocallySurjective φ →
        AlgebraicGeometry.supportSheaf B S hS G ⊆ AlgebraicGeometry.supportSheaf B S hS F) ∧
      (∀ φ : F ⟶ G, (∀ V, Function.Injective (φ.hom.app V)) →
        AlgebraicGeometry.supportSheaf B S hS F ⊆ AlgebraicGeometry.supportSheaf B S hS G)
```

## Tag 04FU, a lemma

[Tag 04FU](https://stacks.math.columbia.edu/tag/04FU) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isClosed_supportSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/SupportSheaf.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/SupportSheaf.lean#L165).

> **Stacks 04FU.** The support of a sheaf of rings on the small étale site is closed: a ring
> is zero exactly when its unit is zero, so the support of a sheaf of rings is the support of its
> unit section, which is closed.

```lean
public theorem isClosed_supportSheaf :
    IsClosed (supportSheaf B S hS (toAddCommGrp B S hS F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.31, Tag 04FQ](https://stacks.math.columbia.edu/tag/04FQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
