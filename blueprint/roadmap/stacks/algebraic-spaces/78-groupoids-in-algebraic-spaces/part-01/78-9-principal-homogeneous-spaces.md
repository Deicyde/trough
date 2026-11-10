---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsPseudoTorsor, AlgebraicGeometry.IsTrivialPseudoTorsor, AlgebraicGeometry.Space.isPseudoTorsor_iff_points, AlgebraicGeometry.Space.isTrivialPseudoTorsor_iff_exists_section, AlgebraicGeometry.isTrivial_iff_exists_globalSection, AlgebraicGeometry.Space.IsPrincipalHomogeneousSpace, AlgebraicGeometry.Space.IsFppfTorsor, AlgebraicGeometry.Space.IsSyntomicTorsor
statement: formalized
proof: formalized
---

# 78.9 Principal homogeneous spaces

Section 78.9 of the Stacks Project, [Tag 04TV](https://stacks.math.columbia.edu/tag/04TV). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04TW, a definition

[Tag 04TW](https://stacks.math.columbia.edu/tag/04TW) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsPseudoTorsor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L61), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L75) (StacksFrontier): “part (1): pseudo-torsor”.
- [`AlgebraicGeometry.IsTrivialPseudoTorsor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L68), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L76) (StacksFrontier): “part (2): trivial pseudo-torsor”.

## Tag 04TX, a lemma

[Tag 04TX](https://stacks.math.columbia.edu/tag/04TX) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoTorsor_iff_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L136). The attribute's comment: “pointwise_characterization”. References: SGA 3 IV (6.7), “(i) <=> (ii)”; SGA 3 IV (5.1.0), “pointwise criterion”; SGA 3 III (0.1), “fppf site presheaves”.

> A pseudo-torsor is characterized by simple transitivity on the points of every test scheme
> over its base presheaf.

```lean
theorem isPseudoTorsor_iff_points
    (𝒞 : BigFppfSite.{u}) (S : Scheme.{u}) (hS : 𝒞.Contains S)
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (G X : Over B) [GrpObj G] [ModObj G X] :
    IsPseudoTorsor G X ↔
      ∀ (T : BigFppfOver 𝒞 S hS) (b : yoneda.obj T ⟶ B)
        (x y : (Over.mk b : Over B) ⟶ X),
        ∃! g : (Over.mk b : Over B) ⟶ G, g • x = y
```

**`AlgebraicGeometry.Space.isTrivialPseudoTorsor_iff_exists_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L180). The attribute's comment: “part (2): trivial iff the structure morphism has a section”.

> A pseudo-torsor is trivial if and only if its structure morphism to the base presheaf has a
> section.

```lean
theorem isTrivialPseudoTorsor_iff_exists_section
    (𝒞 : BigFppfSite.{u}) (S : Scheme.{u}) (hS : 𝒞.Contains S)
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (G X : Over B) [GrpObj G] [ModObj G X] (hX : IsPseudoTorsor G X) :
    IsTrivialPseudoTorsor G X ↔ ∃ s : B ⟶ X.left, s ≫ X.hom = 𝟙 B
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isTrivial_iff_exists_globalSection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Torsor.lean#L87), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L78) (StacksFrontier): “trivial_iff_section”.

## Tag 04TY, a definition

[Tag 04TY](https://stacks.math.columbia.edu/tag/04TY) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPrincipalHomogeneousSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L224). The attribute's comment: “part (1): principal homogeneous space”. References: SGA 3 IV (5.1.5), “alg. spaces, fpqc”; SGA 3 IV (6.5), “fpqc row”; SGA 3 IV (5.1), “princ. homog. bundle”; SGA 3 VIB (10.15), “G-torsor, fpqc T”; SGA 1 XI (4.1).

> A *principal homogeneous space* under a group algebraic space `G` over `B` is a pseudo-torsor
> which has sections after an fpqc covering of `B`.

```lean
abbrev IsPrincipalHomogeneousSpace : Prop
```

**`AlgebraicGeometry.Space.IsFppfTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L231). The attribute's comment: “part (2): fppf torsor”. References: SGA 3 IV (5.1.5), “alg. spaces, fppf”; SGA 3 VIB (10.15), “G-torsor, fppf T”.

> A pseudo-torsor which has sections after an fppf covering of the base.

```lean
abbrev IsFppfTorsor : Prop
```

**`AlgebraicGeometry.Space.IsSyntomicTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L236). The attribute's comment: “part (2): syntomic torsor”.

> A pseudo-torsor which has sections after a syntomic covering of the base.

```lean
abbrev IsSyntomicTorsor : Prop
```

**`AlgebraicGeometry.Space.IsSmoothTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L241). The attribute's comment: “part (2): smooth torsor”.

> A pseudo-torsor which has sections after a smooth covering of the base.

```lean
abbrev IsSmoothTorsor : Prop
```

**`AlgebraicGeometry.Space.IsEtaleTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L250). The attribute's comment: “parts (2), (3): étale torsor and quasi-isotriviality”. References: SGA 3 IV (5.1.5), “alg. spaces, étale”; SGA 3 IV (6.5), “étale row”; SGA 3 VIB (10.15), “G-torsor, étale T”.

> A pseudo-torsor which has sections after an étale covering of the base; for a principal
> homogeneous space this is quasi-isotriviality.

```lean
abbrev IsEtaleTorsor : Prop
```

**`AlgebraicGeometry.Space.IsZariskiTorsor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/PseudoTorsors.lean#L258). The attribute's comment: “parts (2), (4): Zariski torsor and local triviality”. References: SGA 1 XI (4.7), “more general”; SGA 3 IV (6.5), “(Zar) row”.

> A pseudo-torsor which has sections after a Zariski covering of the base; for a principal
> homogeneous space this is local triviality.

```lean
abbrev IsZariskiTorsor : Prop
```

## Tag 04TZ, a lemma

[Tag 04TZ](https://stacks.math.columbia.edu/tag/04TZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isFppfTorsor_iff_siteTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsor.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FppfTorsor.lean#L398). The attribute's comment: “the whole statement: the biconditional over the base `S` itself, with the site-side condition read in the sense of Tag 03AH”.

> **Stacks 04TZ.** An action of a group algebraic space over `S` on an algebraic space over
> `S` is an fppf torsor exactly when it is a torsor on the big fppf site of `S`.

```lean
theorem isFppfTorsor_iff_siteTorsor
    (hB : IsAlgebraicSpace B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)))
    (G X : Over (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace B S hS G.left) (hX : IsAlgebraicSpace B S hS X.left) :
    IsFppfTorsor B S hS (⊤_ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) hB G X hG hX ↔
      IsSiteTorsor B S hS G X
```

## Tag 0DSK, a lemma

[Tag 0DSK](https://stacks.math.columbia.edu/tag/0DSK) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_of_isPseudoTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PseudoTorsorProperties.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PseudoTorsorProperties.lean#L126). The attribute's comment: “the unramified case”.

> **Stacks 0DSK.** A pseudo-torsor under an unramified group algebraic space is unramified
> over the base, provided it is locally of finite type over the base.

```lean
theorem isUnramified_of_isPseudoTorsor (𝒞 : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : 𝒞.Contains S) {B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u}
    (hB : IsAlgebraicSpace 𝒞 S hS B) (G : GroupAlgebraicSpace 𝒞 S hS B hB) (X : Over B)
    [ModObj G.obj.X X] (hX : IsAlgebraicSpace 𝒞 S hS X.left)
    (hXFiniteType : IsLocallyOfFiniteType 𝒞 S hS X.hom)
    (hG : IsUnramified 𝒞 S hS G.obj.X.hom) (hPseudo : IsPseudoTorsor G.obj.X X) :
    IsUnramified 𝒞 S hS X.hom
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isPseudoTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PseudoTorsorProperties.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PseudoTorsorProperties.lean#L255). The attribute's comment: “the locally quasi-finite case”.

> **Stacks 0DSK.** A pseudo-torsor under a locally quasi-finite group algebraic space is
> locally quasi-finite over the base, provided it is locally of finite type over the base.
>
> The shear map identifies the second projection of `X ×_B X` with that of `G ×_B X`, which is a
> base change of `G ⟶ B`, so the projection is locally quasi-finite; that is the only use of the
> torsor structure, and
> `AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isLocallyQuasiFinite_pullbackSnd` is the rest
> of the argument.

```lean
theorem isLocallyQuasiFinite_of_isPseudoTorsor (𝒞 : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : 𝒞.Contains S) {B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u}
    (hB : IsAlgebraicSpace 𝒞 S hS B) (G : GroupAlgebraicSpace 𝒞 S hS B hB) (X : Over B)
    [ModObj G.obj.X X] (hX : IsAlgebraicSpace 𝒞 S hS X.left)
    (hXFiniteType : IsLocallyOfFiniteType 𝒞 S hS X.hom)
    (hG : IsLocallyQuasiFinite 𝒞 S hS G.obj.X.hom) (hPseudo : IsPseudoTorsor G.obj.X X) :
    IsLocallyQuasiFinite 𝒞 S hS X.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.9, Tag 04TV](https://stacks.math.columbia.edu/tag/04TV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
