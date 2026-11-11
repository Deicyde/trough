---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAffineHom_iff_isAffineHom_of_isThickening_unconditional, AlgebraicGeometry.Space.isIntegralHom_iff_isIntegralHom_of_isThickening_unconditional, AlgebraicGeometry.Space.isSeparated_iff_and_isQuasiSeparated_iff_of_isThickening, AlgebraicGeometry.Space.universallyInjective_iff_universallyInjective_of_isThickening, AlgebraicGeometry.Space.universallyOpen_iff_universallyOpen_of_isThickening, AlgebraicGeometry.Space.relativelyRepresentable_iff_relativelyRepresentable_of_isThickening_unconditional, AlgebraicGeometry.Space.isSurjective_iff_isSurjective_of_isThickening, AlgebraicGeometry.Space.isQuasiSeparated_iff_isQuasiSeparated_of_isThickening
statement: formalized
proof: formalized
---

# 76.10 Morphisms of thickenings

Section 76.10 of the Stacks Project, [Tag 0CG4](https://stacks.math.columbia.edu/tag/0CG4). 3 tags here are carried by 44 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09ZY, a lemma

[Tag 09ZY](https://stacks.math.columbia.edu/tag/09ZY) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_iff_isAffineHom_of_isThickening_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L309). The attribute's comment: “part (1): affine”.

> **Stacks 09ZY, part (1).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is affine if and only if the morphism on the ambient spaces
> is.

```lean
theorem isAffineHom_iff_isAffineHom_of_isThickening_unconditional
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsAffineHom B S hS f.left ↔ IsAffineHom B S hS f.right
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_isIntegralHom_of_isThickening_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L320). The attribute's comment: “part (5): integral”.

> **Stacks 09ZY, part (5).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is integral if and only if the morphism on the ambient spaces
> is.

```lean
theorem isIntegralHom_iff_isIntegralHom_of_isThickening_unconditional
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsIntegralHom B S hS f.left ↔ IsIntegralHom B S hS f.right
```

**`AlgebraicGeometry.Space.isSeparated_iff_and_isQuasiSeparated_iff_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L331). The attribute's comment: “part (6): separated, and quasi-separated”.

> **Stacks 09ZY, part (6).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is separated if and only if the morphism on the ambient spaces
> is, and it is quasi-separated if and only if the morphism on the ambient spaces is.

```lean
theorem isSeparated_iff_and_isQuasiSeparated_iff_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    (IsSeparated B S hS f.left ↔ IsSeparated B S hS f.right) ∧
      (IsQuasiSeparated B S hS f.left ↔ IsQuasiSeparated B S hS f.right)
```

**`AlgebraicGeometry.Space.universallyInjective_iff_universallyInjective_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L344). The attribute's comment: “part (7): universally injective”.

> **Stacks 09ZY, part (7).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is universally injective if and only if the morphism on the
> ambient spaces is.

```lean
theorem universallyInjective_iff_universallyInjective_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    UniversallyInjective B S hS f.left ↔ UniversallyInjective B S hS f.right
```

**`AlgebraicGeometry.Space.universallyOpen_iff_universallyOpen_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L355). The attribute's comment: “part (8): universally open”.

> **Stacks 09ZY, part (8).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is universally open if and only if the morphism on the ambient
> spaces is.

```lean
theorem universallyOpen_iff_universallyOpen_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    UniversallyOpen B S hS f.left ↔ UniversallyOpen B S hS f.right
```

**`AlgebraicGeometry.Space.relativelyRepresentable_iff_relativelyRepresentable_of_isThickening_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismProperties.lean#L366). The attribute's comment: “part (9): representable”.

> **Stacks 09ZY, part (9).** In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is representable if and only if the morphism on the ambient
> spaces is.

```lean
theorem relativelyRepresentable_iff_relativelyRepresentable_of_isThickening_unconditional
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    yoneda.relativelyRepresentable f.left ↔ yoneda.relativelyRepresentable f.right
```

**`AlgebraicGeometry.Space.isSurjective_iff_isSurjective_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Morphisms.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Morphisms.lean#L53). The attribute's comment: “surjective”.

> In a morphism of thickenings of algebraic spaces over `S` the
> map on the closed subspaces is surjective if and only if the map on the ambient spaces is.

```lean
theorem isSurjective_iff_isSurjective_of_isThickening
    {X Y : AlgebraicSpaces B S hS} {G : Subfunctor X.1} {H : Subfunctor Y.1}
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsSurjective B S hS f.left ↔ IsSurjective B S hS f.right
```

**`AlgebraicGeometry.Space.isQuasiSeparated_iff_isQuasiSeparated_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/QuasiSeparatedTransfer.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/QuasiSeparatedTransfer.lean#L152). The attribute's comment: “part (6): the quasi-separated half”.

> **Stacks 09ZY, the quasi-separated half of part (6).** In a morphism of thickenings of
> algebraic spaces over `S` the morphism on the closed subspaces is quasi-separated if and only if
> the morphism on the ambient spaces is.
>
> The separated half of the same part is
> `AlgebraicGeometry.Space.isSeparated_iff_isSeparated_of_isThickening`; together they are the
> whole of part (6).

```lean
theorem isQuasiSeparated_iff_isQuasiSeparated_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsQuasiSeparated B S hS f.left ↔ IsQuasiSeparated B S hS f.right
```

**`AlgebraicGeometry.Space.universallyClosed_iff_universallyClosed_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean#L223). The attribute's comment: “part (4): universally closed”.

> In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is universally closed if and only if the morphism on the
> ambient spaces is.

```lean
theorem universallyClosed_iff_universallyClosed_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    UniversallyClosed B S hS f.left ↔ UniversallyClosed B S hS f.right
```

**`AlgebraicGeometry.Space.isQuasiCompact_iff_isQuasiCompact_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean#L234). The attribute's comment: “part (3): quasi-compact”.

> In a morphism of thickenings of algebraic spaces over `S` the
> morphism on the closed subspaces is quasi-compact if and only if the morphism on the ambient
> spaces is.

```lean
theorem isQuasiCompact_iff_isQuasiCompact_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsQuasiCompact B S hS f.left ↔ IsQuasiCompact B S hS f.right
```

**`AlgebraicGeometry.Space.isSeparated_iff_isSeparated_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SeparatedAndClosed.lean#L244). The attribute's comment: “part (6): the separated half only, not quasi-separated”.

> In a morphism of thickenings of algebraic spaces over `S` the morphism on the closed
> subspaces is separated if and only if the morphism on the ambient spaces is.

```lean
theorem isSeparated_iff_isSeparated_of_isThickening
    (hG : IsThickening B S hS X G) (hH : IsThickening B S hS Y H)
    (f : Arrow.mk G.ι ⟶ Arrow.mk H.ι) :
    IsSeparated B S hS f.left ↔ IsSeparated B S hS f.right
```

## Tag 09ZZ, a lemma

[Tag 09ZZ](https://stacks.math.columbia.edu/tag/09ZZ) in the Stacks Project.

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isLocallyOfFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/CartesianFiniteOrderMorphism.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/CartesianFiniteOrderMorphism.lean#L281). The attribute's comment: “part (2), locally of finite type; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (2).** Local finite type is invariant under a cartesian morphism of
> thickenings of algebraic spaces whose target thickening is of finite order: the map between the
> smaller spaces is locally of finite type exactly when the map between the ambient spaces is.
>
> The hypothesis is the finite order of the target thickening `Y ⊂ Y'`, which is stronger than
> the finite order of the source thickening `X ⊂ X'` that the tag's text states; see the
> implementation notes of this file.

```lean
theorem isLocallyOfFiniteType_iff (M : CartesianFiniteOrderMorphismOfThickenings B S hS) :
    IsLocallyOfFiniteType B S hS M.f ↔ IsLocallyOfFiniteType B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isLocallyQuasiFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean#L146). The attribute's comment: “part (3), locally quasi-finite; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (3).** Local quasi-finiteness is invariant under a cartesian morphism of
> thickenings of algebraic spaces whose target thickening is of finite order: the map between the
> smaller spaces is locally quasi-finite exactly when the map between the ambient spaces is.
>
> The hypothesis is the finite order of the target thickening `Y ⊂ Y'`, which is stronger than
> the finite order of the source thickening `X ⊂ X'` that the tag's text states; see the
> implementation notes of this file.

```lean
theorem isLocallyQuasiFinite_iff (M : CartesianFiniteOrderMorphismOfThickenings B S hS) :
    IsLocallyQuasiFinite B S hS M.f ↔ IsLocallyQuasiFinite B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isUnramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean#L168). The attribute's comment: “part (6), unramified; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (6).** Unramifiedness is invariant under a cartesian morphism of
> thickenings of algebraic spaces whose target thickening is of finite order: the map between the
> smaller spaces is unramified exactly when the map between the ambient spaces is.
>
> The hypothesis is the finite order of the target thickening `Y ⊂ Y'`, which is stronger than
> the finite order of the source thickening `X ⊂ X'` that the tag's text states; see the
> implementation notes of this file.

```lean
theorem isUnramified_iff (M : CartesianFiniteOrderMorphismOfThickenings B S hS) :
    IsUnramified B S hS M.f ↔ IsUnramified B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean#L248). The attribute's comment: “part (7), proper; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (7).** Properness is invariant under a cartesian morphism of thickenings
> of algebraic spaces whose target thickening is of finite order.
>
> Properness is the conjunction of separatedness, local finite type, quasi-compactness and
> universal closedness. The first, third and fourth are invariant under an arbitrary morphism of
> thickenings, by parts (6), (3) and (4) of Stacks 09ZY, and the second is part (2) of this
> tag.

```lean
theorem isProper_iff : IsProper B S hS M.f ↔ IsProper B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean#L272). The attribute's comment: “part (8), finite; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (8).** Finiteness is invariant under a cartesian morphism of thickenings
> of algebraic spaces whose target thickening is of finite order.
>
> By Stacks 0A4X a morphism of algebraic spaces is finite exactly when it is proper and locally
> quasi-finite, and both of those are invariant: properness by part (7) of this tag and local
> quasi-finiteness by part (3).

```lean
theorem isFinite_iff : IsFinite B S hS M.f ↔ IsFinite B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isClosedImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean#L313). The attribute's comment: “part (1), closed immersion; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (1).** Being a closed immersion is invariant under a cartesian morphism
> of thickenings of algebraic spaces whose target thickening is of finite order.
>
> The implication from the ambient morphism to the morphism of smaller spaces is base change
> along the cartesian square. In the other direction, Stacks 05W8 characterises closed immersions
> of algebraic spaces as the universally closed, unramified, universally injective morphisms, and
> each of those three conditions is invariant: universal closedness by part (4) of Stacks 09ZY,
> unramifiedness by part (6) of this tag, and universal injectivity because
> `X ⟶ Y ⟶ Y'` equals `X ⟶ X' ⟶ Y'`, the inclusions of the two thickenings are universally
> injective closed immersions and the source inclusion is surjective.

```lean
theorem isClosedImmersion_iff :
    IsClosedImmersion B S hS M.f ↔ IsClosedImmersion B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismImmersions.lean#L419). The attribute's comment: “part (10), immersion; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (10).** Being an immersion is invariant under a cartesian morphism of
> thickenings of algebraic spaces whose target thickening is of finite order.
>
> The implication from the ambient morphism to the morphism of smaller spaces is base change
> along the cartesian square. In the other direction, Stacks 04CE factors the immersion `f` as a
> closed immersion into the open subspace of `Y` complementary to the boundary of the image of
> `f`, and `isImmersion_right_of_isClosedImmersion_into_openSubspace` above turns that
> factorisation into an immersion factorisation of `f'` using part (1).

```lean
theorem isImmersion_iff : IsImmersion B S hS M.f ↔ IsImmersion B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismMonomorphism.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismMonomorphism.lean#L299). The attribute's comment: “part (9), monomorphism; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (9).** Being a monomorphism is invariant under a cartesian morphism of
> thickenings of algebraic spaces whose target thickening is of finite order: the map between the
> smaller spaces is a monomorphism exactly when the map between the ambient spaces is.
>
> The implication from the ambient morphism to the morphism of smaller spaces is base change
> along the cartesian square. In the other direction, the first projection of `X' ×_{Y'} X'` is a
> monomorphism by `mono_pullback_fst` and a split epimorphism retracted by the diagonal of `f'`,
> hence an isomorphism, and a morphism whose kernel pair has invertible first projection is a
> monomorphism.

```lean
theorem mono_iff : Mono M.f ↔ Mono M.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.isLocallyOfFiniteType_and_hasRelativeDimension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismRelativeDimension.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismRelativeDimension.lean#L139). The attribute's comment: “part (4), locally of finite type of relative dimension d, stated as the conjunction of local finite type and relative dimension d which is what that property means; the finite-order hypothesis is on the TARGET thickening Y ⊆ Y', which is strictly stronger than the source hypothesis X ⊆ X' in the tag's text, so this is a weaker theorem than the tag announces. It is the hypothesis the tag's own proof uses: it reduces to Tag 09ZW, which puts finite order on the target, and says 'by induction on the order of the thickening we may assume that Y ⊆ Y' is a first order thickening'. Cartesianness plus target finite order gives source finite order by Tag 09ZX, but not conversely”.

> **Stacks 09ZZ, part (4).** Being locally of finite type of relative dimension `d` is
> invariant under a cartesian morphism of thickenings of algebraic spaces whose target thickening
> is of finite order: the map between the smaller spaces is locally of finite type of relative
> dimension `d` exactly when the map between the ambient spaces is.
>
> The property is the conjunction of local finite type and relative dimension `d`, and the
> statement is that conjunction. Its first half is part (2) of the same tag.
>
> The hypothesis is the finite order of the target thickening `Y ⊂ Y'`, which is stronger than
> the finite order of the source thickening `X ⊂ X'` that the tag's text states; see the
> implementation notes of this file.

```lean
theorem isLocallyOfFiniteType_and_hasRelativeDimension_iff
    (M : CartesianFiniteOrderMorphismOfThickenings B S hS) (d : ℕ) :
    (IsLocallyOfFiniteType B S hS M.f ∧ HasRelativeDimension d B S hS M.f) ↔
      (IsLocallyOfFiniteType B S hS M.f' ∧ HasRelativeDimension d B S hS M.f')
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isLocallyOfFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean#L324). The attribute's comment: “part (2): f is locally of finite type iff f' is”.

> **Stacks 09ZZ, part (2).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is locally of finite
> type exactly when the map between the ambient spaces is.

```lean
theorem isLocallyOfFiniteType_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsLocallyOfFiniteType B S hS M.f ↔ IsLocallyOfFiniteType B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isLocallyQuasiFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean#L335). The attribute's comment: “part (3): f is locally quasi-finite iff f' is”.

> **Stacks 09ZZ, part (3).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is locally quasi-finite
> exactly when the map between the ambient spaces is.

```lean
theorem isLocallyQuasiFinite_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsLocallyQuasiFinite B S hS M.f ↔ IsLocallyQuasiFinite B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isUnramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean#L346). The attribute's comment: “part (6): f is unramified iff f' is”.

> **Stacks 09ZZ, part (6).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is unramified exactly
> when the map between the ambient spaces is.

```lean
theorem isUnramified_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsUnramified B S hS M.f ↔ IsUnramified B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isLocallyOfFiniteType_and_hasRelativeDimension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean#L376). The attribute's comment: “part (4): f is locally of finite type of relative dimension d iff f' is, the property being the conjunction of local finite type and relative dimension d”.

> **Stacks 09ZZ, part (4).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is locally of finite
> type of relative dimension `d` exactly when the map between the ambient spaces is.

```lean
theorem isLocallyOfFiniteType_and_hasRelativeDimension_iff
    (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) (d : ℕ) :
    (IsLocallyOfFiniteType B S hS M.f ∧ HasRelativeDimension d B S hS M.f) ↔
      (IsLocallyOfFiniteType B S hS M.f' ∧ HasRelativeDimension d B S hS M.f')
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isZero_sheafOfDifferentials_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphism.lean#L413). The attribute's comment: “part (5): Ω\_\{X/Y} = 0 iff Ω\_\{X'/Y'} = 0, for the sheaves of differentials of Tag 04CT”.

> **Stacks 09ZZ, part (5).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the sheaf of differentials `Ω_{X/Y}` of the map between
> the smaller spaces vanishes exactly when the sheaf of differentials `Ω_{X'/Y'}` of the map
> between the ambient spaces does.
>
> By Stacks 04G9 each vanishing is formal unramifiedness of the corresponding morphism, and
> `formallyUnramified_iff` compares those.

```lean
theorem isZero_sheafOfDifferentials_iff
    (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsZero (sheafOfDifferentials B S hS M.smallHom) ↔
      IsZero (sheafOfDifferentials B S hS M.ambientHom)
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean#L98). The attribute's comment: “part (7): f is proper iff f' is”.

> **Stacks 09ZZ, part (7).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is proper exactly when
> the map between the ambient spaces is.

```lean
theorem isProper_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsProper B S hS M.f ↔ IsProper B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean#L114). The attribute's comment: “part (8): f is finite iff f' is”.

> **Stacks 09ZZ, part (8).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is finite exactly when
> the map between the ambient spaces is.

```lean
theorem isFinite_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsFinite B S hS M.f ↔ IsFinite B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isClosedImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean#L140). The attribute's comment: “part (1): f is a closed immersion iff f' is”.

> **Stacks 09ZZ, part (1).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is a closed immersion
> exactly when the map between the ambient spaces is.
>
> By Stacks 05W8 a closed immersion is a universally closed, unramified, universally injective
> morphism. Universal closedness transfers by Stacks 09ZY and unramifiedness by part (6); the
> composite `X ⟶ Y ⟶ Y'` is universally injective, it equals `X ⟶ X' ⟶ Y'`, and `X ⟶ X'` is
> surjective, so `f'` is universally injective.

```lean
theorem isClosedImmersion_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsClosedImmersion B S hS M.f ↔ IsClosedImmersion B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.isImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean#L226). The attribute's comment: “part (10): f is an immersion iff f' is”.

> **Stacks 09ZZ, part (10).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is an immersion exactly
> when the map between the ambient spaces is.
>
> Stacks 04CE factors the immersion `f` as a closed immersion into an open subspace of `Y`, and
> `isImmersion_right_of_isClosedImmersion_into_openSubspace` turns that into an immersion
> factorisation of `f'`.

```lean
theorem isImmersion_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    IsImmersion B S hS M.f ↔ IsImmersion B S hS M.f'
```

**`AlgebraicGeometry.Space.CartesianSourceFiniteOrderMorphismOfThickenings.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SourceFiniteOrderMorphismImmersions.lean#L304). The attribute's comment: “part (9): f is a monomorphism iff f' is”.

> **Stacks 09ZZ, part (9).** In a cartesian morphism of thickenings of algebraic spaces whose
> source thickening is of finite order, the map between the smaller spaces is a monomorphism
> exactly when the map between the ambient spaces is.
>
> If `f` is a monomorphism, the first projection of `X' ×_{Y'} X'` is a monomorphism by
> `mono_pullback_fst_of_mono` and a split epimorphism retracted by the diagonal, hence an
> isomorphism, so `f'` is a monomorphism. The converse is base change.

```lean
theorem mono_iff (M : CartesianSourceFiniteOrderMorphismOfThickenings B S hS) :
    Mono M.f ↔ Mono M.f'
```

## Tag 0BPJ, a lemma

[Tag 0BPJ](https://stacks.math.columbia.edu/tag/0BPJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_of_cartesianMorphismOfThickenings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean#L110). The attribute's comment: “locally\_quasi\_finite”.

> **Stacks 0BPJ, part (1).** Being locally quasi-finite is invariant under a cartesian
> morphism of thickenings of algebraic spaces whose two component maps are locally of finite
> type.

```lean
theorem isLocallyQuasiFinite_iff_of_cartesianMorphismOfThickenings
    (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    IsLocallyQuasiFinite B S hS T.f ↔ IsLocallyQuasiFinite B S hS T.f'
```

**`AlgebraicGeometry.Space.formallyUnramifiedCharts_iff_of_cartesianMorphismOfThickenings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean#L125). The attribute's comment: “vanishing\_differentials”.

> **Stacks 0BPJ, part (4).** In a cartesian morphism of thickenings of algebraic spaces whose
> two component maps are locally of finite type, the module of relative differentials of `f`
> vanishes exactly when the module of relative differentials of `f'` does.
>
> The vanishing of `Ω_{X/Y}` is expressed by the condition that the morphism of schemes in every
> commuting square of étale charts of `f` is formally unramified, which on an affine chart is the
> vanishing of the Kähler differentials of the corresponding ring map.

```lean
theorem formallyUnramifiedCharts_iff_of_cartesianMorphismOfThickenings
    (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) T.f ↔
      HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) T.f'
```

**`AlgebraicGeometry.Space.locallyQuasiFiniteProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalPropertiesPointTest.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalPropertiesPointTest.lean#L66). The attribute's comment: “part (1): locally quasi-finite, at the Section 04XB point test”.

> **Stacks 0BPJ, part (1), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is locally quasi-finite if
> and only if `f'` is locally quasi-finite.
>
> The square is given by morphisms of the category of algebraic spaces over `S` and the three
> properties by morphism properties of that category.

```lean
theorem locallyQuasiFiniteProperty_iff_of_cartesianSquareOfThickeningHoms
    {X X' Y Y' : AlgebraicSpaces B S hS} {i : X ⟶ X'} {j : Y ⟶ Y'} {f : X ⟶ Y} {f' : X' ⟶ Y'}
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    locallyQuasiFiniteProperty B S hS f ↔ locallyQuasiFiniteProperty B S hS f'
```

**`AlgebraicGeometry.Space.formallyUnramifiedCharts_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalPropertiesPointTest.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalPropertiesPointTest.lean#L85). The attribute's comment: “part (4): vanishing relative differentials, at the Section 04XB point test”.

> **Stacks 0BPJ, part (4), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `Ω_{X/Y} = 0` if and only if
> `Ω_{X'/Y'} = 0`, the vanishing of the relative differentials being expressed, as in
> `AlgebraicGeometry.Space.formallyUnramifiedCharts_iff_of_cartesianMorphismOfThickenings`, by
> formal unramifiedness of the morphism of schemes in every commuting square of étale charts.
>
> The square is given by morphisms of the category of algebraic spaces over `S`.

```lean
theorem formallyUnramifiedCharts_iff_of_cartesianSquareOfThickeningHoms
    {X X' Y Y' : AlgebraicSpaces B S hS} {i : X ⟶ X'} {j : Y ⟶ Y'} {f : X ⟶ Y} {f' : X' ⟶ Y'}
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) f.hom ↔
      HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyUnramified.{u} :
          MorphismProperty Scheme.{u}) f'.hom
```

**`AlgebraicGeometry.Space.properProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/ProperFinite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/ProperFinite.lean#L60). The attribute's comment: “part (8): proper, at the Section 04XB point test”.

> Let `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over
> `S` with `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is proper if and
> only if `f'` is proper.

```lean
theorem properProperty_iff_of_cartesianSquareOfThickeningHoms
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    properProperty B S hS f ↔ properProperty B S hS f'
```

**`AlgebraicGeometry.Space.finiteMorphismProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/ProperFinite.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/ProperFinite.lean#L81). The attribute's comment: “part (2): finite, at the Section 04XB point test”.

> Let `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over
> `S` with `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is finite if and
> only if `f'` is finite.

```lean
theorem finiteMorphismProperty_iff_of_cartesianSquareOfThickeningHoms
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    finiteMorphismProperty B S hS f ↔ finiteMorphismProperty B S hS f'
```

**`AlgebraicGeometry.Space.CartesianLocallyFiniteTypeMorphismOfThickenings.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean#L102). The attribute's comment: “part (8): f is proper iff f' is”.

> **Stacks 0BPJ, part (8).** In a cartesian morphism of thickenings of algebraic spaces whose
> two component maps are locally of finite type, the map between the smaller spaces is proper
> exactly when the map between the ambient spaces is.

```lean
theorem isProper_iff (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    IsProper B S hS T.f ↔ IsProper B S hS T.f'
```

**`AlgebraicGeometry.Space.CartesianLocallyFiniteTypeMorphismOfThickenings.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean#L118). The attribute's comment: “part (2): f is finite iff f' is”.

> **Stacks 0BPJ, part (2).** In a cartesian morphism of thickenings of algebraic spaces whose
> two component maps are locally of finite type, the map between the smaller spaces is finite
> exactly when the map between the ambient spaces is.

```lean
theorem isFinite_iff (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    IsFinite B S hS T.f ↔ IsFinite B S hS T.f'
```

**`AlgebraicGeometry.Space.CartesianLocallyFiniteTypeMorphismOfThickenings.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean#L209). The attribute's comment: “part (6): f is a monomorphism iff f' is”.

> **Stacks 0BPJ, part (6).** In a cartesian morphism of thickenings of algebraic spaces whose
> two component maps are locally of finite type, the map between the smaller spaces is a
> monomorphism exactly when the map between the ambient spaces is.
>
> If `f` is a monomorphism, the first projection of `X' ×_{Y'} X'` is a monomorphism by
> `mono_pullback_fst_of_mono` and a split epimorphism retracted by the diagonal, hence an
> isomorphism, so `f'` is a monomorphism. The converse is base change.

```lean
theorem mono_iff (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    Mono T.f ↔ Mono T.f'
```

**`AlgebraicGeometry.Space.closedImmersionProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean#L141). The attribute's comment: “part (3): closed immersion, at the Section 04XB point test”.

> **Stacks 0BPJ, part (3), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is a closed immersion if and
> only if `f'` is a closed immersion.

```lean
theorem closedImmersionProperty_iff_of_cartesianSquareOfThickeningHoms
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    closedImmersionProperty B S hS f ↔ closedImmersionProperty B S hS f'
```

**`AlgebraicGeometry.Space.immersionProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean#L287). The attribute's comment: “part (7): immersion, at the Section 04XB point test”.

> **Stacks 0BPJ, part (7), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is an immersion if and only
> if `f'` is an immersion.

```lean
theorem immersionProperty_iff_of_cartesianSquareOfThickeningHoms
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    immersionProperty B S hS f ↔ immersionProperty B S hS f'
```

**`AlgebraicGeometry.Space.mono_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean#L344). The attribute's comment: “part (6): monomorphism, at the Section 04XB point test”.

> **Stacks 0BPJ, part (6), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is a monomorphism if and
> only if `f'` is a monomorphism.
>
> The direction from `f'` to `f` is base change. In the other direction, `f'` is a monomorphism as
> soon as the first projection of `X' ×_{Y'} X'` is an isomorphism, and that projection is
> obtained as follows. Pull the thickening `i : X ⟶ X'` back along the first projection; the
> resulting square
>
> ```
> X ×_{X'} (X' ×_{Y'} X') --→ X
> |                           |
> ↓                           ↓
> X' ×_{Y'} X' ------fst-----→ X'
> ```
>
> is again a cartesian morphism of thickenings with both horizontal maps locally of finite type,
> and its upper map is an *isomorphism*: a section of the upper left corner is a pair `(a, b)` of
> sections of `X'` with `f'(a) = f'(b)` and `a` a section of `X`, the cartesian square of the
> given morphism of thickenings exhibits `b` as a second factorisation of that pair through `X`
> with the same image under `f`, and monomorphy of `f` identifies the two. An isomorphism is a
> closed immersion, so part (3) above makes `fst` a closed immersion, hence a monomorphism; it is
> also split by the diagonal of `f'`, and a monomorphism which is a split epimorphism is an
> isomorphism.
>
> This is the argument of
> `AlgebraicGeometry.Space.CartesianFiniteOrderMorphismOfThickenings.mono_iff` for part (9) of
> **Stacks 09ZZ**, with part (3) above in place of part (1) of that tag; the source's own proof of
> this case instead compares the conormal sheaf of the diagonal of `f` with that of `f'`, which
> needs the algebraic-space form of **Stacks 08S2** and so is not available here.

```lean
theorem mono_iff_of_cartesianSquareOfThickeningHoms
    (hi : IsThickeningHom B S hS i) (_hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (_hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    Mono f ↔ Mono f'
```

**`AlgebraicGeometry.Space.isUnramified_iff_of_cartesianMorphismOfThickenings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Unramified.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Unramified.lean#L118). The attribute's comment: “unramified”.

> Being unramified is invariant under a cartesian morphism of thickenings of algebraic spaces
> whose two component maps are locally of finite type.

```lean
theorem isUnramified_iff_of_cartesianMorphismOfThickenings
    (T : CartesianLocallyFiniteTypeMorphismOfThickenings B S hS) :
    IsUnramified B S hS T.f ↔ IsUnramified B S hS T.f'
```

**`AlgebraicGeometry.Space.unramifiedMorphismProperty_iff_of_cartesianSquareOfThickeningHoms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/UnramifiedPointTest.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/UnramifiedPointTest.lean#L60). The attribute's comment: “part (5): unramified, at the Section 04XB point test”.

> **Stacks 0BPJ, part (5), at the point test of Section 04XB.** Let
> `(f, f') : (X ⊂ X') → (Y ⊂ Y')` be a morphism of thickenings of algebraic spaces over `S` with
> `f` and `f'` locally of finite type and `X = Y ×_{Y'} X'`. Then `f` is unramified if and only if
> `f'` is unramified.
>
> The two thickenings are given as morphisms `i : X ⟶ X'` and `j : Y ⟶ Y'` of the category of
> algebraic spaces over `S` (`AlgebraicGeometry.Space.IsThickeningHom`) and the three properties
> as morphism properties of that category, which is the shape the point test of **Stacks 03YK**
> reads a property of morphisms of algebraic spaces in; see
> `AlgebraicGeometry.Stack.HasRelativeProperty`. The equivalence itself is
> `AlgebraicGeometry.Space.isUnramified_iff_of_cartesianMorphismOfThickenings`, the same statement
> with the two smaller spaces presented as subfunctors of the two ambient ones.

```lean
theorem unramifiedMorphismProperty_iff_of_cartesianSquareOfThickeningHoms
    {X X' Y Y' : AlgebraicSpaces B S hS} {i : X ⟶ X'} {j : Y ⟶ Y'} {f : X ⟶ Y} {f' : X' ⟶ Y'}
    (hi : IsThickeningHom B S hS i) (hj : IsThickeningHom B S hS j) (hsq : IsPullback f i j f')
    (hft : locallyOfFiniteTypeProperty B S hS f)
    (hft' : locallyOfFiniteTypeProperty B S hS f') :
    unramifiedMorphismProperty B S hS f ↔ unramifiedMorphismProperty B S hS f'
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isClosedImmersion_iff_of_cartesianMorphismOfThickenings`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean#L167), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean#L222) (StacksFrontier): “part (3): f is a closed immersion iff f' is”.
- [`AlgebraicGeometry.Space.isImmersion_iff_of_cartesianMorphismOfThickenings`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesImmersions.lean#L271), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/SpacesFiniteProperMono.lean#L225) (StacksFrontier): “part (7): f is an immersion iff f' is”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.10, Tag 0CG4](https://stacks.math.columbia.edu/tag/0CG4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
