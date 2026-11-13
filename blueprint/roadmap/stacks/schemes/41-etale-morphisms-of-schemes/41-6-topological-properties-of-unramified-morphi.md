---
declaration: section
origin: cited
lean: AlgebraicGeometry.Unramified.section_isOpenImmersion, AlgebraicGeometry.Unramified.section_isOpenImmersion_and_isClosedImmersion, AlgebraicGeometry.Unramified.isClopen_range_section, AlgebraicGeometry.isOpenImmersion_of_isSection, AlgebraicGeometry.isClosedImmersion_of_isSection_of_isSeparated, AlgebraicGeometry.isClopen_range_of_isSection, Stacks.AlgebraicGeometry.RelativeProjSeparated.isClosedImmersion_of_section, AlgebraicGeometry.Unramified.section_isIso_onto_connectedComponent
statement: formalized
proof: formalized
---

# 41.6 Topological properties of unramified morphisms

Section 41.6 of the Stacks Project, [Tag 024S](https://stacks.math.columbia.edu/tag/024S). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 024T, a proposition

[Tag 024T](https://stacks.math.columbia.edu/tag/024T) in the Stacks Project.

**`AlgebraicGeometry.Unramified.section_isOpenImmersion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L57). The attribute's comment: “part (1)”.

> A section of an unramified morphism is an open immersion.

```lean
public lemma section_isOpenImmersion {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Unramified f] (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) :
    IsOpenImmersion s
```

**`AlgebraicGeometry.Unramified.section_isOpenImmersion_and_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L81). The attribute's comment: “part (3)”. References: EGA IV (17.9.3), “more general”; SGA 3 VIB (5.6.3), “(i) ⇒ (ii), special case”.

> A section of an unramified separated morphism is both an open immersion and a closed
> immersion.

```lean
public theorem section_isOpenImmersion_and_isClosedImmersion {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Unramified f] [IsSeparated f] (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) :
    IsOpenImmersion s ∧ IsClosedImmersion s
```

**`AlgebraicGeometry.Unramified.isClopen_range_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L88). The attribute's comment: “part (3), the image”.

> The image of a section of an unramified separated morphism is open and closed.

```lean
public theorem isClopen_range_section {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Unramified f] [IsSeparated f] (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) :
    IsClopen (Set.range s)
```

**`AlgebraicGeometry.isOpenImmersion_of_isSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean#L85). The attribute's comment: “part (1): a section of an unramified morphism is an open immersion”.

> **Stacks Project, Tag 024T, part (1).** A section of an unramified morphism is an open
> immersion.

```lean
theorem isOpenImmersion_of_isSection (hs : s ≫ g = 𝟙 S) [Unramified g] :
    IsOpenImmersion s
```

**`AlgebraicGeometry.isClosedImmersion_of_isSection_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean#L98). The attribute's comment: “part (2): a section of a separated morphism is a closed immersion”. References: EGA I (5.4.6); SGA 3 VIB (5.6.3), “(i) ⇒ (ii)”.

> **Stacks Project, Tag 024T, part (2).** A section of a separated morphism is a closed
> immersion.

```lean
theorem isClosedImmersion_of_isSection_of_isSeparated (hs : s ≫ g = 𝟙 S) [IsSeparated g] :
    IsClosedImmersion s
```

**`AlgebraicGeometry.isClopen_range_of_isSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Sections.lean#L106). The attribute's comment: “part (3): a section of an unramified separated morphism is open and closed”.

> **Stacks Project, Tag 024T, part (3).** A section of an unramified separated morphism is open
> and closed: its image is an open and closed subset of the source.

```lean
theorem isClopen_range_of_isSection (hs : s ≫ g = 𝟙 S) [Unramified g] [IsSeparated g] :
    IsClopen (Set.range s.base)
```

**`Stacks.AlgebraicGeometry.RelativeProjSeparated.isClosedImmersion_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjSeparated/Basic.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjSeparated/Basic.lean#L108). The attribute's comment: “part (2)”. References: EGA I (5.4.4), “special case”; EGA I (5.4.6); EGA IV (16.2.3), “special case”; SGA 3 II (4.11.4), “more general”; SGA 3 VIB (5.1), “more general”; SGA 3 VIB (5.6.3), “(i) ⇒ (ii)”.

> **A section of a separated morphism of schemes is a closed immersion.**

```lean
public theorem isClosedImmersion_of_section {X Y : Scheme.{u}} (f : X ⟶ Y) [IsSeparated f]
    (σ : Y ⟶ X) (hσ : σ ≫ f = 𝟙 Y) : IsClosedImmersion σ
```

## Tag 024U, a theorem

[Tag 024U](https://stacks.math.columbia.edu/tag/024U) in the Stacks Project.

**`AlgebraicGeometry.Unramified.section_isIso_onto_connectedComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L125). The attribute's comment: “sections are component isomorphisms”. References: EGA IV (17.4.9), “section is comp. iso”; EGA IV (17.9.4), “iso onto conn. component”; SGA 1 I (5.3), “section iso onto comp”.

> A section of a separated unramified morphism onto a connected target is an isomorphism onto
> a connected component of its source.

```lean
public theorem section_isIso_onto_connectedComponent {X Y : Scheme.{u}}
    [ConnectedSpace Y] (f : X ⟶ Y) [Unramified f] [IsSeparated f]
    (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) :
    ∃ (U : X.Opens) (sU : Y ⟶ U.toScheme),
      (∃ x : X, (U : Set X) = connectedComponent x) ∧ IsIso sU ∧ sU ≫ U.ι = s
```

**`AlgebraicGeometry.Unramified.sections_equiv_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L172). The attribute's comment: “bijective correspondence”. References: EGA IV (17.9.4), “bijection g ↦ g(Y)”; EGA IV (17.4.9), “bijection g↦g(Y)”; SGA 1 I (5.3), “bijection with comps”.

> Sections correspond to the connected components on which the morphism is an isomorphism; the
> component corresponding to a section is exactly its image.

```lean
public theorem sections_equiv_connectedComponents {X Y : Scheme.{u}}
    [ConnectedSpace Y] (f : X ⟶ Y) [Unramified f] [IsSeparated f] :
    ∃ e : {s : Y ⟶ X // s ≫ f = 𝟙 Y} ≃
      {U : X.Opens // (∃ x : X, (U : Set X) = connectedComponent x) ∧ IsIso (U.ι ≫ f)},
      ∀ s, ((e s).1 : Set X) = Set.range (fun y : Y => s.1 y)
```

**`AlgebraicGeometry.Unramified.section_eq_of_common_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L226). The attribute's comment: “uniqueness through a point”. References: EGA IV (17.4.9), “"In particular" clause”; EGA IV (17.9.4), “injectivity of g↦g(Y)”; SGA 1 I (5.3), “determined by one point”.

> At most one section of a separated unramified morphism passes through a given point of its
> source.

```lean
public theorem section_eq_of_common_point {X Y : Scheme.{u}}
    [ConnectedSpace Y] (f : X ⟶ Y) [Unramified f] [IsSeparated f]
    (s t : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) (ht : t ≫ f = 𝟙 Y)
    (x : X) (y z : Y) (hsy : s y = x) (htz : t z = x) : s = t
```

## Tag 024V, a proposition

[Tag 024V](https://stacks.math.columbia.edu/tag/024V) in the Stacks Project.

**`AlgebraicGeometry.Unramified.eq_of_residueFieldMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Sections.lean#L249). References: SGA 1 I (5.4).

> Two morphisms from a connected scheme to a separated unramified scheme over a base are equal
> if they induce the same point and the same residue-field map there.

```lean
public theorem eq_of_residueFieldMap_eq {S X Y : Scheme.{u}} (π : X ⟶ S)
    [Unramified π] [IsSeparated π] [ConnectedSpace Y]
    (f g : Y ⟶ X) (hover : f ≫ π = g ≫ π) (y : Y) (hy : f y = g y)
    (hκ : f.residueFieldMap y = (X.residueFieldCongr hy).hom ≫ g.residueFieldMap y) :
    f = g
```

## Tag 0AKI, a lemma

[Tag 0AKI](https://stacks.math.columbia.edu/tag/0AKI) in the Stacks Project.

**`AlgebraicGeometry.Unramified.finite_morphisms_over_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Finiteness.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/UnramifiedTopological/Finiteness.lean#L123).

> There are finitely many morphisms over a Noetherian base from a Noetherian scheme to a
> quasi-compact unramified scheme.

```lean
public theorem finite_morphisms_over_of_unramified {S X Y : Scheme.{u}}
    (π : X ⟶ S) (g : Y ⟶ S) [IsNoetherian S] [IsNoetherian Y]
    [QuasiCompact π] [Unramified π] :
    Set.Finite {f : Y ⟶ X | f ≫ π = g}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.6, Tag 024S](https://stacks.math.columbia.edu/tag/024S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
