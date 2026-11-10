---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAffineHom_inner_iff_outer, AlgebraicGeometry.Stack.isIntegralHom_inner_iff_outer, AlgebraicGeometry.Stack.isQuasiSeparated_inner_iff_outer, AlgebraicGeometry.Stack.isSeparated_inner_iff_outer, AlgebraicGeometry.Stack.thickeningMorphism_inner_iff_outer, AlgebraicGeometry.Stack.isRepresentableMorphism_inner_iff_outer, AlgebraicGeometry.Stack.universallyClosed_inner_iff_outer, AlgebraicGeometry.Stack.universallyOpen_inner_iff_outer
statement: formalized
proof: formalized
---

# 106.4 Morphisms of thickenings

Section 106.4 of the Stacks Project, [Tag 0CJ8](https://stacks.math.columbia.edu/tag/0CJ8). 1 tag here is carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CJ9, a lemma

[Tag 0CJ9](https://stacks.math.columbia.edu/tag/0CJ9) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAffineHom_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismAffineIntegral.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismAffineIntegral.lean#L216). The attribute's comment: “part (1): affine”.

> **Stacks 0CJ9, part (1).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is affine (**Stacks 0CHQ**) if and only
> if the ambient 1-morphism `f'` is.
>
> Representability by algebraic spaces is part (12) of the tag; affineness in the sense of Stacks
> 04XB is `AlgebraicGeometry.Stack.hasRelativeProperty_outer_of_inner` and
> `AlgebraicGeometry.Stack.hasRelativeProperty_inner_of_outer` at
> `AlgebraicGeometry.Space.affineMorphismProperty`, with the cancellation
> `AlgebraicGeometry.Space.isAffineHom_of_comp_of_isClosedImmersion_of_isSurjective`.

```lean
theorem isAffineHom_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.IsAffineHom B S hS m.inner ↔ AlgebraicStacks.IsAffineHom B S hS m.outer
```

**`AlgebraicGeometry.Stack.isIntegralHom_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismAffineIntegral.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismAffineIntegral.lean#L242). The attribute's comment: “part (5): integral”.

> **Stacks 0CJ9, part (5).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is integral (**Stacks 0CHU**) if and
> only if the ambient 1-morphism `f'` is.
>
> The argument is that of part (1) at `AlgebraicGeometry.Space.integralMorphismProperty`, with the
> cancellation `AlgebraicGeometry.Space.isIntegralHom_of_comp_of_isClosedImmersion_of_isSurjective`
> (Stacks 0415 splits integrality into affineness and universal closedness, which both cancel).

```lean
theorem isIntegralHom_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.IsIntegralHom B S hS m.inner ↔
      AlgebraicStacks.IsIntegralHom B S hS m.outer
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean#L95). The attribute's comment: “part (10): quasi-separated”.

> **Stacks 0CJ9, part (10), the quasi-separated half.** In a morphism of thickenings
> `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`, the restricted 1-morphism `f` is
> quasi-separated (**Stacks 04YW**) if and only if the ambient 1-morphism `f'` is.
>
> As in the source, this is a condition on the relative diagonals, which form a morphism of
> thickenings (**Stacks 0BPU**), and it is clauses (d) and (g) of **Stacks 0BPV**:
> `AlgebraicGeometry.Stack.isQuasiSeparated_outer_of_inner` and
> `AlgebraicGeometry.Stack.isQuasiSeparated_inner_of_outer`.

```lean
theorem isQuasiSeparated_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.IsQuasiSeparated B S hS m.inner ↔
      AlgebraicStacks.IsQuasiSeparated B S hS m.outer
```

**`AlgebraicGeometry.Stack.isSeparated_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean#L108). The attribute's comment: “part (10): separated”.

> **Stacks 0CJ9, part (10), the separated half.** In a morphism of thickenings
> `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`, the restricted 1-morphism `f` is
> separated (**Stacks 04YW**) if and only if the ambient 1-morphism `f'` is.
>
> Separatedness is properness of the relative diagonal, and this is clause (q) of **Stacks 0BPV**:
> `AlgebraicGeometry.Stack.isSeparated_outer_of_inner` and
> `AlgebraicGeometry.Stack.isSeparated_inner_of_outer`.

```lean
theorem isSeparated_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.IsSeparated B S hS m.inner ↔ AlgebraicStacks.IsSeparated B S hS m.outer
```

**`AlgebraicGeometry.Stack.thickeningMorphism_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismProperties.lean#L132).

> **Stacks 0CJ9.** Let `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` be a morphism of thickenings of
> algebraic stacks over `S`, `f = m.inner` and `f' = m.outer`. Then
> (1) `f` is affine if and only if `f'` is affine,
> (2) `f` is surjective if and only if `f'` is surjective,
> (3) `f` is quasi-compact if and only if `f'` is quasi-compact,
> (4) `f` is universally closed if and only if `f'` is universally closed,
> (5) `f` is integral if and only if `f'` is integral,
> (6) `f` is universally injective if and only if `f'` is universally injective,
> (7) `f` is universally open if and only if `f'` is universally open,
> (8) `f` is quasi-DM if and only if `f'` is quasi-DM,
> (9) `f` is DM if and only if `f'` is DM,
> (10) `f` is quasi-separated if and only if `f'` is quasi-separated, and `f` is separated if and
> only if `f'` is separated,
> (11) `f` is representable if and only if `f'` is representable,
> (12) `f` is representable by algebraic spaces if and only if `f'` is representable by algebraic
> spaces.
>
> The conjuncts are, in order, the twelve items of the source; item (13) ("add more here") states
> nothing.

```lean
theorem thickeningMorphism_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    (AlgebraicStacks.IsAffineHom B S hS m.inner ↔ AlgebraicStacks.IsAffineHom B S hS m.outer) ∧
    (IsSurjective B S hS m.inner ↔ IsSurjective B S hS m.outer) ∧
    (IsQuasiCompactMorphism B S hS m.inner ↔ IsQuasiCompactMorphism B S hS m.outer) ∧
    (AlgebraicStacks.UniversallyClosed B S hS m.inner ↔
      AlgebraicStacks.UniversallyClosed B S hS m.outer) ∧
    (AlgebraicStacks.IsIntegralHom B S hS m.inner ↔
      AlgebraicStacks.IsIntegralHom B S hS m.outer) ∧
    (UniversallyInjective B S hS m.inner ↔ UniversallyInjective B S hS m.outer) ∧
    (AlgebraicStacks.UniversallyOpen B S hS m.inner ↔
      AlgebraicStacks.UniversallyOpen B S hS m.outer) ∧
    (AlgebraicStacks.IsQuasiDM B S hS m.inner ↔ AlgebraicStacks.IsQuasiDM B S hS m.outer) ∧
    (IsDM B S hS m.inner ↔ IsDM B S hS m.outer) ∧
    ((AlgebraicStacks.IsQuasiSeparated B S hS m.inner ↔
        AlgebraicStacks.IsQuasiSeparated B S hS m.outer) ∧
      (AlgebraicStacks.IsSeparated B S hS m.inner ↔
        AlgebraicStacks.IsSeparated B S hS m.outer)) ∧
    (Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor m.inner.hom) ↔
      Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳'.val.val.p 𝒴'.val.val.p
        (CatFiberedInGroupoids.homFunctor m.outer.hom)) ∧
    (IsRepresentableByAlgebraicSpaces B S hS m.inner.hom.hom ↔
      IsRepresentableByAlgebraicSpaces B S hS m.outer.hom.hom)
```

**`AlgebraicGeometry.Stack.isRepresentableMorphism_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismRepresentable.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismRepresentable.lean#L131). The attribute's comment: “part (11): representable”.

> **Stacks 0CJ9, part (11).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is representable (by schemes,
> **Stacks 02Y7**) if and only if the ambient 1-morphism `f'` is.

```lean
theorem isRepresentableMorphism_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor m.inner.hom) ↔
      Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳'.val.val.p 𝒴'.val.val.p
        (CatFiberedInGroupoids.homFunctor m.outer.hom)
```

**`AlgebraicGeometry.Stack.universallyClosed_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean#L295). The attribute's comment: “part (4): universally closed”.

> **Stacks 0CJ9, part (4).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is universally closed (**Stacks 0513**)
> if and only if the ambient 1-morphism `f'` is.
>
> The base changes of `f` and of `f'` are compared by the thickenings of
> `AlgebraicGeometry.Stack.exists_isThickening_baseChange_comp` and
> `AlgebraicGeometry.Stack.exists_isThickening_baseChange_outer`, which are homeomorphisms on points
> (**Stacks 0CJ7**).

```lean
theorem universallyClosed_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.UniversallyClosed B S hS m.inner ↔
      AlgebraicStacks.UniversallyClosed B S hS m.outer
```

**`AlgebraicGeometry.Stack.universallyOpen_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean#L338). The attribute's comment: “part (7): universally open”.

> **Stacks 0CJ9, part (7).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is universally open (**Stacks 06U2**)
> if and only if the ambient 1-morphism `f'` is. The argument is that of part (4).

```lean
theorem universallyOpen_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    AlgebraicStacks.UniversallyOpen B S hS m.inner ↔
      AlgebraicStacks.UniversallyOpen B S hS m.outer
```

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningMorphismTopologicalProperties.lean#L383). The attribute's comment: “part (3): quasi-compact”.

> **Stacks 0CJ9, part (3).** In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of
> algebraic stacks over `S`, the restricted 1-morphism `f` is quasi-compact (**Stacks 050U**) if
> and only if the ambient 1-morphism `f'` is.
>
> Quasi-compactness of an algebraic stack is compactness of its space of points (**Stacks 04YB**),
> and the base changes of `f` and of `f'` are compared by the thickenings of
> `AlgebraicGeometry.Stack.exists_isThickening_baseChange_comp` and
> `AlgebraicGeometry.Stack.exists_isThickening_baseChange_outer`.

```lean
theorem isQuasiCompactMorphism_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    IsQuasiCompactMorphism B S hS m.inner ↔ IsQuasiCompactMorphism B S hS m.outer
```

**`AlgebraicGeometry.Stack.isQuasiDM_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L355). The attribute's comment: “item (8): quasi-DM”.

> In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`,
> the 1-morphism `f` is quasi-DM if and only if `f'` is quasi-DM.

```lean
theorem isQuasiDM_inner_iff_outer :
    AlgebraicStacks.IsQuasiDM B S hS m.inner ↔ AlgebraicStacks.IsQuasiDM B S hS m.outer
```

**`AlgebraicGeometry.Stack.isDM_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L369). The attribute's comment: “item (9): DM”.

> In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`,
> the 1-morphism `f` is Deligne–Mumford if and only if `f'` is Deligne–Mumford.

```lean
theorem isDM_inner_iff_outer : IsDM B S hS m.inner ↔ IsDM B S hS m.outer
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L409). The attribute's comment: “item (12): representable by algebraic spaces”.

> In a morphism of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`,
> the 1-morphism `f` is representable by algebraic spaces if and only if `f'` is.

```lean
theorem isRepresentableByAlgebraicSpaces_inner_iff_outer :
    IsRepresentableByAlgebraicSpaces B S hS m.inner.hom.hom ↔
      IsRepresentableByAlgebraicSpaces B S hS m.outer.hom.hom
```

**`AlgebraicGeometry.Stack.isSurjective_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSurjective.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSurjective.lean#L113). The attribute's comment: “part (2): surjective”.

> **Stacks 0CJ9, part (2).** In a morphism of thickenings of algebraic stacks over `S`, the
> restricted 1-morphism is surjective if and only if the ambient 1-morphism is surjective.
>
> Surjectivity is a condition on the map of sets of points of **Stacks 04ZS**, the restriction
> square induces a commutative square of those maps, and the two vertical maps of that square —
> the thickenings — are bijective.

```lean
theorem isSurjective_inner_iff_outer {𝒳 𝒳' 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    {i : 𝒳 ⟶ 𝒳'} {j : 𝒴 ⟶ 𝒴'} {hi : IsThickening i} {hj : IsThickening j}
    (m : ThickeningMorphism i j hi hj) :
    IsSurjective B S hS m.inner ↔ IsSurjective B S hS m.outer
```

**`AlgebraicGeometry.Stack.universallyInjective_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversallyInjective.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversallyInjective.lean#L285). The attribute's comment: “part (6): universally injective”.

> **Stacks 0CJ9, part (6).** In a morphism of thickenings of algebraic stacks over `S`, the
> restricted 1-morphism is universally injective if and only if the ambient 1-morphism is
> universally injective.

```lean
theorem universallyInjective_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    UniversallyInjective B S hS m.inner ↔ UniversallyInjective B S hS m.outer
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.4, Tag 0CJ8](https://stacks.math.columbia.edu/tag/0CJ8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
