---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenMap_mul, AlgebraicGeometry.isOpen_image_mul_of_open, AlgebraicGeometry.isSeparated_of_groupScheme_over_field, AlgebraicGeometry.existsUnique_irreducibleComponent_containing_identity, AlgebraicGeometry.geometricallyIrreducible_irreducibleComponent_of_identity, AlgebraicGeometry.existsUnique_minimalPrime_stalk, AlgebraicGeometry.exists_closedSubgroupScheme_reduction, AlgebraicGeometry.isClosed_range_of_isOpen
statement: formalized
proof: formalized
---

# 39.7 Properties of group schemes over a field

Section 39.7 of the Stacks Project, [Tag 047J](https://stacks.math.columbia.edu/tag/047J). 13 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 047K, a lemma

[Tag 047K](https://stacks.math.columbia.edu/tag/047K) in the Stacks Project.

**`AlgebraicGeometry.isOpenMap_mul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Multiplication.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Multiplication.lean#L54).

> **Stacks Project, Tag 047K.** The multiplication morphism of a group scheme over a field is
> open.

```lean
lemma isOpenMap_mul {K : Type u} [Field K] (G : Over (Spec (.of K))) [GrpObj G] :
    IsOpenMap μ[G].left
```

## Tag 0B7N, a lemma

[Tag 0B7N](https://stacks.math.columbia.edu/tag/0B7N) in the Stacks Project.

**`AlgebraicGeometry.isOpen_image_mul_of_open`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Multiplication.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Multiplication.lean#L84).

> **Stacks Project, Tag 0B7N.** The image of `T × U` under parametrized
> multiplication is open.

```lean
lemma isOpen_image_mul_of_open {k : Type u} [Field k]
    (G T : Over (Spec (.of k))) [GrpObj G] (ψ : T ⟶ G)
    (U : G.left.Opens) :
    IsOpen (Set.image (lift (fst T G ≫ ψ) (snd T G) ≫ μ[G]).left.base
      ((snd T G).left.base ⁻¹' (U : Set G.left)))
```

## Tag 047L, a lemma

[Tag 047L](https://stacks.math.columbia.edu/tag/047L) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_of_groupScheme_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Separated.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Separated.lean#L45). References: SGA 3 VIB (1.1), “(2), special case”; SGA 3 VIB (6.2.4); SGA 3 VIII (6.5), “partial”.

> **Stacks Project, Tag 047L.** The underlying scheme of a group scheme over a field is
> separated.

```lean
theorem isSeparated_of_groupScheme_over_field {k : Type u} [Field k]
    (G : Grp (Over (Spec (.of k)))) : G.X.left.IsSeparated
```

## Tag 047M, a lemma

[Tag 047M](https://stacks.math.columbia.edu/tag/047M) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_irreducibleComponent_containing_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentityComponent.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentityComponent.lean#L283). The attribute's comment: “identity\_component\_unique”. References: SGA 3 VIA (2.4), “(i) irred., base field”; SGA 3 VIA (2.6.5), “(a)”.

> **Stacks Project, Tag 047M.** A group scheme over a field has a unique irreducible
> component containing its identity point.

```lean
theorem existsUnique_irreducibleComponent_containing_identity
    {k : Type u} [Field k] {G : Scheme.{u}} (f : G ⟶ Spec (.of k))
    [GrpObj (Over.mk f)] :
    ∃! Z : irreducibleComponents G,
      (η[Over.mk f]).left (IsLocalRing.closedPoint k) ∈ (Z : Set G)
```

**`AlgebraicGeometry.geometricallyIrreducible_irreducibleComponent_of_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentityComponentGeometric.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentityComponentGeometric.lean#L125). The attribute's comment: “identity\_component\_geometrically\_irreducible”. References: SGA 3 VIA (2.4), “(i) geom. irred., field”; SGA 3 VIA (2.6.5), “(ii) geom. irreducible”; SGA 3 VIA (2.6.2).

> **Stacks Project, Tag 047M.** An irreducible component of a group scheme over a field
> which contains the identity is geometrically irreducible over that field.

```lean
theorem geometricallyIrreducible_irreducibleComponent_of_identity
    (k : Type u) [Field k] (G : Scheme.{u}) (f : G ⟶ Spec (.of k))
    [GrpObj (Over.mk f)] (Z : irreducibleComponents G)
    (he : Set.range (η[Over.mk f]).left ⊆ Z.1) :
    GeometricallyIrreducible
      ((Scheme.IdealSheafData.vanishingIdeal
        (⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩ :
          TopologicalSpace.Closeds G)).subschemeι ≫ f)
```

**`AlgebraicGeometry.existsUnique_minimalPrime_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/LocalMinimalPrime.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/LocalMinimalPrime.lean#L183). The attribute's comment: “local\_unique\_minimal\_prime”.

> **Stacks Project, Tag 047M.** Every local ring of a group scheme over a field has a
> unique minimal prime ideal.

```lean
theorem existsUnique_minimalPrime_stalk (k : Type u) [Field k]
    (G : Grp (Over (Spec (CommRingCat.of k)))) (g : G.X.left) :
    ∃! p : Ideal (G.X.left.presheaf.stalk g),
      p ∈ minimalPrimes (G.X.left.presheaf.stalk g)
```

## Tag 047R, a lemma

[Tag 047R](https://stacks.math.columbia.edu/tag/047R) in the Stacks Project.

**`AlgebraicGeometry.exists_closedSubgroupScheme_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/Reduction.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/Reduction.lean#L49). References: SGA 3 VIA (0.2), “perfect k: G\_red ≤ G”; SGA 3 VIA (5.6), “more general”; SGA 3 VIB (12.1), “Over the base field”; SGA 3 XII (1.0), “partial”.

> The reduction of a group scheme over a perfect field is a closed subgroup scheme.

```lean
theorem exists_closedSubgroupScheme_reduction
    {k : Type u} [Field k] [PerfectField k]
    (G : Grp (Over (Spec (.of k)))) :
    let I := Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds G.X.left)
    ∃ H : ClosedSubgroupScheme G,
      ∃ e : Over.mk (I.subschemeι ≫ G.X.hom) ≅ H.carrier.X,
        Over.homMk I.subschemeι = e.hom ≫ H.ι.hom.hom
```

## Tag 047S, a lemma

[Tag 047S](https://stacks.math.columbia.edu/tag/047S) in the Stacks Project.

**`AlgebraicGeometry.isClosed_range_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/OpenImage.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/OpenImage.lean#L141).

> **Stacks Project, Tag 047S.** An open image of a homomorphism of group schemes over a
> field is closed.

```lean
theorem isClosed_range_of_isOpen {k : Type u} [Field k]
    {G' G : Grp (Over (Spec (.of k)))} (ψ : G' ⟶ G)
    (hopen : IsOpen (Set.range ψ.hom.hom.left.base)) :
    IsClosed (Set.range ψ.hom.hom.left.base)
```

## Tag 047T, a lemma

[Tag 047T](https://stacks.math.columbia.edu/tag/047T) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Immersion.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Immersion.lean#L140).

> **Stacks Project, Tag 047T.** Every immersion of group schemes over a field is a closed
> immersion.

```lean
theorem isClosedImmersion_of_isImmersion {k : Type u} [Field k]
    {G' G : Grp (Over (Spec (.of k)))} (i : G' ⟶ G)
    [IsImmersion i.hom.hom.left] : IsClosedImmersion i.hom.hom.left
```

## Tag 0B7P, a lemma

[Tag 0B7P](https://stacks.math.columbia.edu/tag/0B7P) in the Stacks Project.

**`AlgebraicGeometry.compactSpace_of_irreducibleSpace_grpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/QuasiCompact.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/QuasiCompact.lean#L278). References: SGA 3 VIA (0.5.1); SGA 3 VIA (2.6.5), “more general”.

> **Stacks Project, Tag 0B7P.** An irreducible group scheme over a field is quasi-compact.

```lean
instance compactSpace_of_irreducibleSpace_grpObj
    (k : Type u) [Field k] (G : Over (Spec (.of k))) [GrpObj G]
    [IrreducibleSpace G.left] : CompactSpace G.left
```

## Tag 0B7Q, a lemma

[Tag 0B7Q](https://stacks.math.columbia.edu/tag/0B7Q) in the Stacks Project.

**`AlgebraicGeometry.irreducibleSpace_of_connectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Irreducible.lean, line 764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Irreducible.lean#L764). References: SGA 3 VIB (5.8.1), “X = G acting on itself”; SGA 3 VIA (2.4), “(i), special case”; SGA 3 VIA (2.6.5), “(iii)”.

> A connected group scheme over a field is irreducible.

```lean
theorem irreducibleSpace_of_connectedSpace
    {k : Type u} [Field k] (G : Over (Spec (.of k))) [GrpObj G]
    [ConnectedSpace G.left] : IrreducibleSpace G.left
```

## Tag 0B7R, a proposition

[Tag 0B7R](https://stacks.math.columbia.edu/tag/0B7R) in the Stacks Project.

**`AlgebraicGeometry.identityComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L359). The attribute's comment: “construction”. References: EGA IV (15.6.10); SGA 3 VIA (2.6.5), “(i) existence of G^0”; SGA 6 XIII (4.1), “G^0 over a field”; SGA 3 VIA (2.3).

> The canonical closed subgroup scheme whose support is the connected component of
> the identity of `G`.

```lean
noncomputable def identityComponent (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k)))) : ClosedSubgroupScheme G
```

**`AlgebraicGeometry.identityComponent_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L397). The attribute's comment: “part (1): flatness”. References: SGA 3 VIA (2.6.5), “(i)(b) flatness”.

> The inclusion of the identity component is flat.

```lean
theorem identityComponent_flat (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k)))) :
    Flat (identityComponent k G).ι.hom.hom.left
```

**`AlgebraicGeometry.identityComponent_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L404). The attribute's comment: “part (2): support”.

> The underlying set of the identity subgroup is the connected component of the identity.

```lean
theorem identityComponent_range (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k)))) :
    Set.range (identityComponent k G).ι.hom.hom.left =
      connectedComponent (identityPoint k G)
```

**`AlgebraicGeometry.identityComponent_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L416). The attribute's comment: “part (3): geometric irreducibility”. References: EGA IV (15.6.10), “partial”; SGA 3 VIA (2.4), “(i), special case”; SGA 3 VIA (2.6.2); SGA 3 VIA (2.6.5).

> The identity component is geometrically irreducible over the field.

```lean
theorem identityComponent_geometricallyIrreducible (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k)))) :
    GeometricallyIrreducible (identityComponent k G).carrier.X.hom
```

**`AlgebraicGeometry.identityComponent_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L443). The attribute's comment: “part (4): quasi-compactness”. References: SGA 3 VIA (2.6.2), “quasi-compactness”; SGA 3 VIA (2.6.5), “(ii) quasi-compact”; SGA 3 VIA (2.4), “(ii), base field”; SGA 3 VIB (3.9), “special case”.

> The identity component is quasi-compact.

```lean
theorem identityComponent_compactSpace (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k)))) :
    CompactSpace (identityComponent k G).carrier.X.left
```

**`AlgebraicGeometry.identityComponent_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/IdentitySubgroup.lean#L453). The attribute's comment: “canonicality”.

> Any flat closed subgroup scheme supported on the identity component is uniquely
> isomorphic to the identity component over `G`.

```lean
theorem identityComponent_unique (k : Type u) [Field k]
    (G : Grp (Over (Spec (.of k))))
    (H : ClosedSubgroupScheme G)
    [Flat H.ι.hom.hom.left]
    (hH : Set.range H.ι.hom.hom.left =
      connectedComponent (identityPoint k G)) :
    ∃! φ : H.carrier ≅ (identityComponent k G).carrier,
      φ.hom ≫ (identityComponent k G).ι = H.ι
```

## Tag 0B7T, a lemma

[Tag 0B7T](https://stacks.math.columbia.edu/tag/0B7T) in the Stacks Project.

**`AlgebraicGeometry.isHomeomorph_pullback_to_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AffineLimits.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AffineLimits.lean#L442).

> Let `k` be a field and let `A` be a filtered colimit of
> `k`-algebras that are finite products of copies of `k`.  For any scheme `X` over `k`, the
> canonical map from the underlying space of `Spec A ×_k X` to `|Spec A| × |X|` is a
> homeomorphism.

```lean
theorem isHomeomorph_pullback_to_product
    (k A : Type u) [Field k] [CommRing A] [Algebra k A]
    (hA : IsFilteredColimitOfFiniteProducts k A)
    (X : Scheme.{u}) (f : X ⟶ Spec (of k)) :
    IsHomeomorph (fun x :
      (pullback (Spec.map (ofHom (algebraMap k A))) f : Scheme.{u}) ↦
        ((pullback.fst (Spec.map (ofHom (algebraMap k A))) f).base x,
          (pullback.snd (Spec.map (ofHom (algebraMap k A))) f).base x))
```

## Tag 0B7U, a lemma

[Tag 0B7U](https://stacks.math.columbia.edu/tag/0B7U) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_range_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/CompactImageAffineOpen.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/CompactImageAffineOpen.lean#L1151).

> **Stacks Project, Tag 0B7U.** The image in a Jacobson group scheme of the spectrum of a
> filtered colimit of finite products of the algebraically closed ground field is contained in an
> affine open, provided every closed point of the group scheme is rational over the ground field.

```lean
theorem exists_affineOpen_range_subset
    (k A : Type u) [Field k] [IsAlgClosed k] [CommRing A] [Algebra k A]
    (G : Grp (Over (Spec (CommRingCat.of k))))
    [JacobsonSpace G.X.left]
    (hclosed : ∀ x : G.X.left, IsClosed ({x} : Set G.X.left) →
      ∃ p : Over.mk (𝟙 (Spec (CommRingCat.of k))) ⟶ G.X,
        p.left.base (⊥ : PrimeSpectrum k) = x)
    (hA : IsFilteredColimitOfFiniteProducts k A)
    (f : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap k A))) ⟶ G.X) :
    ∃ U : G.X.left.Opens, IsAffineOpen U ∧ Set.range f.left.base ⊆ U
```

## Tag 047U, a lemma

[Tag 047U](https://stacks.math.columbia.edu/tag/047U) in the Stacks Project.

**`AlgebraicGeometry.exists_openSubgroupScheme_isClosed_iUnion_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/CountableUnionOfAffines.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverFieldProperties/CountableUnionOfAffines.lean#L337).

> **Stacks Project, Tag 047U.** A group scheme over a field has an open and closed subscheme
> which is a countable union of affine opens; it can be taken to be an open subgroup scheme.

```lean
theorem exists_openSubgroupScheme_isClosed_iUnion_affineOpens
    (G : Grp (Over (Spec (.of k)))) :
    ∃ (H : OpenSubgroupScheme G) (V : ℕ → G.X.left.Opens),
      IsOpen (Set.range H.ι.hom.hom.left.base) ∧
      IsClosed (Set.range H.ι.hom.hom.left.base) ∧
      Set.range η[G.X].left.base ⊆ Set.range H.ι.hom.hom.left.base ∧
      (∀ n, IsAffineOpen (V n)) ∧
      Set.range H.ι.hom.hom.left.base = ⋃ n, (V n : Set G.X.left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.7, Tag 047J](https://stacks.math.columbia.edu/tag/047J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
