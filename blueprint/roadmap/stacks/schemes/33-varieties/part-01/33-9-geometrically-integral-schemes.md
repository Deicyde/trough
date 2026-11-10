---
declaration: section
origin: cited
lean: AlgebraicGeometry.GeometricallyPointwiseIntegralAt, AlgebraicGeometry.GeometricallyPointwiseIntegral, AlgebraicGeometry.geometricallyIntegral_iff_isIntegral_pullback, AlgebraicGeometry.GeometricallyIntegral, AlgebraicGeometry.GeometricallyIntegral.eq_geometricallyReduced_inf_geometricallyIrreducible, Stacks.AlgebraicGeometry.ProperSectionsGeom.componentwiseArtinianDecomposition, Stacks.AlgebraicGeometry.ProperSectionsGeom.isGeometricallyIrreducible_globalSections_of_isProper, Stacks.AlgebraicGeometry.ProperSectionsGeom.isGeometricallyIrreducible_globalSections_of_geometricallyIrreducible
statement: formalized
proof: formalized
---

# 33.9 Geometrically integral schemes

Section 33.9 of the Stacks Project, [Tag 0366](https://stacks.math.columbia.edu/tag/0366). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 020H, a definition

[Tag 020H](https://stacks.math.columbia.edu/tag/020H) in the Stacks Project.

**`AlgebraicGeometry.GeometricallyPointwiseIntegralAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean#L57). The attribute's comment: “part (1)”.

> A morphism `f : X ⟶ Y` is geometrically pointwise integral at `x : X` if, after every
> base change from the spectrum of a field, every point above `x` has an integral local ring.

```lean
public abbrev GeometricallyPointwiseIntegralAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X) :
    Prop
```

**`AlgebraicGeometry.GeometricallyPointwiseIntegral`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean#L66). The attribute's comment: “part (2)”.

> A morphism is geometrically pointwise integral if it is geometrically pointwise integral
> at every point of its source.

```lean
public abbrev GeometricallyPointwiseIntegral {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.geometricallyIntegral_iff_isIntegral_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean#L132). The attribute's comment: “part (3)”. References: EGA IV (4.6.2).

> A scheme `X` over a field `k` is geometrically integral if and only if the base change
> `X_{k'}` is integral for every field extension `k'/k`.

```lean
public theorem geometricallyIntegral_iff_isIntegral_pullback {k : Type u} [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    GeometricallyIntegral f ↔
      ∀ (K : Type u) [Field K] [Algebra k K],
        IsIntegral (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.GeometricallyIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.GeometricallyIntegral#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Integral.lean#L142) (StacksFrontier): “part (3)”. References: EGA IV (4.6.2), “more general”; SGA 6 XII (1.2), “partial”.

## Tag 038K, a lemma

[Tag 038K](https://stacks.math.columbia.edu/tag/038K) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.GeometricallyIntegral.eq_geometricallyReduced_inf_geometricallyIrreducible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.GeometricallyIntegral.eq_geometricallyReduced_inf_geometricallyIrreducible#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch33.lean#L55) (StacksFrontier). References: EGA IV (4.6.2), “more general”; EGA IV (4.6.14), “special case”; SGA 3 XIX (2.1), “partial”.

## Tag 0BUG, a lemma

[Tag 0BUG](https://stacks.math.columbia.edu/tag/0BUG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.componentwiseArtinianDecomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Components.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Components.lean#L151). The attribute's comment: “clause (2): for an ARBITRARY proper scheme over a field, the global functions are a product of Artinian local algebras over that field with one factor for each connected component. The index set is the set of connected components itself, the product is finite because a proper scheme over a field is a Noetherian space, and the isomorphism is pinned to be simultaneous restriction, so the factor at a component is the ring of functions on that component. Openness of the components replaces the source's correspondence between primitive idempotents and components; the product decomposition is the sheaf condition for a disjoint open cover; each factor is Artinian because it is a quotient of the global functions, finite over the base field by clause (1), and local because its component is connected.”.

> **[Stacks, Tag 0BUG] (2).** The ring of global functions on a scheme proper over a field `k`
> is a finite product of Artinian local `k`-algebras, with one factor for each connected component
> of `X`, the factor at a component being the ring of functions on that component and the
> isomorphism being simultaneous restriction.
>
> No hypothesis beyond properness: `X` need not be connected, reduced, normal or integral, and the
> structure morphism need not be affine.

```lean
def componentwiseArtinianDecomposition [IsProper f] :
    GlobalSectionsComponentDecomposition k f
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.isGeometricallyIrreducible_globalSections_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Connected.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Connected.lean#L116). The attribute's comment: “clause (5): for a GEOMETRICALLY CONNECTED proper scheme over a field k, the global sections are geometrically irreducible over k: every base change to a field extension of k has irreducible spectrum.”.

> **[Stacks, Tag 0BUG] (5).** Let `X` be a geometrically connected proper scheme over a field
> `k`. Then the ring of global sections of `X`, with its canonical `k`-algebra structure, is
> geometrically irreducible over `k`.

```lean
theorem isGeometricallyIrreducible_globalSections_of_isProper
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [GeometricallyConnected f] [IsProper f] :
    letI : Algebra k Γ(X, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    Algebra.IsGeometricallyIrreducible k Γ(X, ⊤)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.isGeometricallyIrreducible_globalSections_of_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Connected.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Connected.lean#L161). The attribute's comment: “clause (6): for a GEOMETRICALLY IRREDUCIBLE proper scheme over a field k, the global sections are geometrically irreducible over k. The source deduces this clause from clause (5) by the remark that a geometrically irreducible scheme is geometrically connected, and that is what is done here: every base change has an irreducible, hence connected, underlying space.”.

> **[Stacks, Tag 0BUG] (6).** Let `X` be a geometrically *irreducible* proper scheme over a
> field `k`. Then the ring of global sections of `X`, with its canonical `k`-algebra structure, is
> geometrically irreducible over `k`.
>
> A geometrically irreducible morphism is geometrically connected, every base change of it having
> an irreducible and hence connected underlying space, so this is clause (5) applied to the same
> `X`.

```lean
theorem isGeometricallyIrreducible_globalSections_of_geometricallyIrreducible
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [GeometricallyIrreducible f] [IsProper f] :
    letI : Algebra k Γ(X, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    Algebra.IsGeometricallyIrreducible k Γ(X, ⊤)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.isField_globalSections_of_connectedSpace_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ConnectedLocal.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ConnectedLocal.lean#L101). The attribute's comment: “special case of clauses (2) and (3): X connected and reduced, where the ring of global functions is a field”.

> The ring of global functions on a connected *reduced* scheme proper over a field is a
> field.
>
> This is clauses (2) and (3) read at a single connected component: a reduced Artinian local ring
> is a field. The clauses in full are `componentwiseArtinianDecomposition` (clause (2)) and
> `globalSectionsFieldDecomposition_of_isReduced` (clause (3)).

```lean
theorem isField_globalSections_of_connectedSpace_of_isReduced
    [IsProper f] [ConnectedSpace X] [AlgebraicGeometry.IsReduced X] : IsField Γ(X, ⊤)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.isSeparable_globalSections_of_connectedSpace_of_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ConnectedLocal.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ConnectedLocal.lean#L115). The attribute's comment: “special case of clauses (2), (3) and (4): X connected and geometrically reduced, where the field of global functions is separable over k”.

> The field of global functions on a connected *geometrically reduced* scheme proper over a
> field `k` is separable over `k`.
>
> This is clauses (2), (3) and (4) read at a single connected component. The clauses in full are
> stated by other declarations, among them `GlobalSectionsFieldDecomposition.factor_isSeparable`
> (clause (4)).

```lean
theorem isSeparable_globalSections_of_connectedSpace_of_geometricallyReduced
    [IsProper f] [ConnectedSpace X] [GeometricallyReduced f] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    Algebra.IsSeparable k Γ(X, ⊤)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.isIso_globalSections_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedConnected.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedConnected.lean#L136). The attribute's comment: “clause (7): for a GEOMETRICALLY REDUCED and GEOMETRICALLY CONNECTED proper scheme over a field k, the global sections are k. The equality A = k is stated canonically, as the induced homomorphism from k to the global sections being an isomorphism. Geometric irreducibility of the global sections (clause (5)) makes the extension purely inseparable; geometric reducedness of a stalk makes it separable (Tag 030W, Tag 035W); a purely inseparable separable extension is trivial. No finiteness of the global sections over k is used.”.

> **[Stacks, Tag 0BUG] (7).** The canonical homomorphism from a field to the global sections
> of a geometrically reduced, geometrically connected proper scheme over that field is an
> isomorphism.
>
> This is the whole of clause (7): the source's conclusion `A = k` is the assertion that the
> homomorphism `k ⟶ Γ(X, 𝒪_X)` induced by the structure morphism is an isomorphism, the standard
> identification `Γ(Spec k, 𝒪) ≅ k` being part of that map.

```lean
theorem isIso_globalSections_of_isProper
    [GeometricallyReduced f] [GeometricallyConnected f] [IsProper f] :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.moduleFinite_globalSections_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedSections.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedSections.lean#L118). The attribute's comment: “clause (1): the global sections of an arbitrary proper scheme over a field form a finite module over that field, with no integrality, connectedness, normality, reducedness or affineness hypothesis. Finiteness of coherent cohomology over a field (Tag 02O6) plus coherence of the structure sheaf (Tag 01XZ), with the degree-zero identification of cohomology and sections supplied here from left exactness of global sections.”.

> **[Stacks, Tag 0BUG] (1).** The ring of global functions on a scheme proper over a field `k`
> is a finite `k`-module, for the `k`-algebra structure the structure morphism induces.
>
> No hypothesis beyond properness: the scheme need not be integral, connected, normal or reduced,
> and the structure morphism need not be affine.

```lean
theorem moduleFinite_globalSections_of_isProper [IsProper f] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    Module.Finite k Γ(X, ⊤)
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.globalSectionsFieldDecomposition_of_isReduced`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedSections.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/ReducedSections.lean#L139). The attribute's comment: “clause (3): for a REDUCED proper scheme over a field, the presentation of the global sections as a finite product of finite field extensions of the base field. Clause (1) makes the ring Artinian; an Artinian reduced ring is the product of its residue fields. Reducedness only, where the library's normal-case decomposition needs each connected component irreducible. Separability of the factors is clause (4) and is not asserted here.”.

> **[Stacks, Tag 0BUG] (3).** The ring of global functions on a *reduced* scheme proper over a
> field `k` is a finite product of finite field extensions of `k`.
>
> The hypothesis is reducedness of `X`, weaker than the normality assumed by
> `AlgebraicGeometry.globalSectionsFieldDecomposition_of_isNormal`, which this supersedes.

```lean
def globalSectionsFieldDecomposition_of_isReduced [IsProper f] [IsReduced X] :
    GlobalSectionsFieldDecomposition k X f
```

**`Stacks.AlgebraicGeometry.ProperSectionsGeom.GlobalSectionsFieldDecomposition.factor_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Separable.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSectionsGeom/Separable.lean#L182). The attribute's comment: “clause (4): for a GEOMETRICALLY REDUCED proper scheme over a field k, every field factor of a presentation of the global sections as a finite product of finite field extensions of k (clause (3)) is separable over k. The decomposition is an argument, so the conclusion holds for every such presentation, in particular the one clause (3) constructs.”.

> Every field factor in a finite product decomposition of the global sections of a
> geometrically reduced proper scheme is separable over the base field.
> Together with `GlobalSectionsFieldDecomposition.factorModuleFinite`, this says that every factor
> is a finite separable extension.

```lean
theorem GlobalSectionsFieldDecomposition.factor_isSeparable
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] [GeometricallyReduced f] (D : GlobalSectionsFieldDecomposition k X f)
    (i : Fin D.numFactors) : Algebra.IsSeparable k (D.factor i)
```

**`AlgebraicGeometry.isIso_globalSections_of_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean#L85). The attribute's comment: “clause (8): for a GEOMETRICALLY INTEGRAL proper scheme over a field k, the global sections are k. The equality A = k is stated canonically, as the induced homomorphism from k to the global sections being an isomorphism. The source deduces this clause from clause (7): a geometrically integral morphism is geometrically reduced, and geometrically connected because every base change of it has an integral, hence irreducible, hence connected, underlying space.”.

> The canonical homomorphism from a field to the global sections of a geometrically integral
> proper scheme over that field is an isomorphism.

```lean
theorem isIso_globalSections_of_geometricallyIntegral
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [GeometricallyIntegral f] [IsProper f] :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)
```

## Tag 0FD1, a lemma

[Tag 0FD1](https://stacks.math.columbia.edu/tag/0FD1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperGeomConnected.geometricallyConnected_toSpecΓ_of_isProper_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GeomConnectedFibres/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GeomConnectedFibres/Basic.lean#L135). References: EGA III (4.3.4), “special case”.

> **Stacks Project, Tag 0FD1.** If `X` is proper over a field, then the canonical morphism
> from `X` to the spectrum of its ring of global sections has geometrically connected fibres.

```lean
theorem geometricallyConnected_toSpecΓ_of_isProper_over_field (k : Type u) [Field k]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsProper f] :
    GeometricallyConnected X.toSpecΓ
```

## Tag 0FD2, a lemma

[Tag 0FD2](https://stacks.math.columbia.edu/tag/0FD2) in the Stacks Project.

**`AlgebraicGeometry.isIso_globalSections_iff_geometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean#L64).

> A proper geometrically reduced scheme over a field has only constant global functions
> exactly when it is geometrically connected.

```lean
theorem isIso_globalSections_iff_geometricallyConnected
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] [GeometricallyReduced f] :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop) ↔ GeometricallyConnected f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.9, Tag 0366](https://stacks.math.columbia.edu/tag/0366)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
