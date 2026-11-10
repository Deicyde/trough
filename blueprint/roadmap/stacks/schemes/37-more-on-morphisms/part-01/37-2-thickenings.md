---
declaration: section
origin: cited
lean: Stacks.Thickenings.IsThickening, Stacks.Thickenings.IsFirstOrderThickening, Stacks.Thickenings.IsFiniteOrderThickening, Stacks.Thickenings.IsNthOrderThickening, CategoryTheory.Arrow.Hom, Stacks.Thickenings.firstOrderThickening_squareZeroExtension, Stacks.Thickenings.squareZeroExtension_realization, Stacks.Thickenings.isAffine_of_isThickening_of_surjective_appTop
statement: formalized
proof: formalized
---

# 37.2 Thickenings

Section 37.2 of the Stacks Project, [Tag 04EW](https://stacks.math.columbia.edu/tag/04EW). 6 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04EX, a definition

[Tag 04EX](https://stacks.math.columbia.edu/tag/04EX) in the Stacks Project.

**`Stacks.Thickenings.IsThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings.lean#L71). The attribute's comment: “part (1): thickening”.

> A **thickening** is a closed immersion `i : X ⟶ X'` whose underlying map of topological
> spaces is surjective, so that the closed subscheme `X` and the ambient scheme `X'` have the
> same underlying topological space.

```lean
abbrev IsThickening {X X' : Scheme.{u}} (i : X ⟶ X') : Prop
```

**`Stacks.Thickenings.IsFirstOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings.lean#L77). The attribute's comment: “part (2): first-order thickening”.

> A **first-order thickening** is a closed immersion whose kernel ideal sheaf is
> square-zero.

```lean
abbrev IsFirstOrderThickening {X X' : Scheme.{u}} (i : X ⟶ X') : Prop
```

**`Stacks.Thickenings.IsFiniteOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings.lean#L83). The attribute's comment: “part (3): finite-order thickening”.

> A **finite-order thickening** is a closed immersion whose kernel ideal sheaf is
> nilpotent.

```lean
abbrev IsFiniteOrderThickening {X X' : Scheme.{u}} (i : X ⟶ X') : Prop
```

**`Stacks.Thickenings.IsNthOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings.lean#L89). The attribute's comment: “part (4): nth-order thickening”.

> An **`n`th-order thickening** is a closed immersion whose kernel ideal sheaf has vanishing
> `(n+1)`st power.

```lean
abbrev IsNthOrderThickening {X X' : Scheme.{u}} (n : ℕ) (i : X ⟶ X') : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Arrow.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Arrow.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Thickenings.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings.lean#L124) (StacksFrontier): “parts (5) and (6): morphisms of thickenings, also over a base”.

## Tag 05YV, a lemma

[Tag 05YV](https://stacks.math.columbia.edu/tag/05YV) in the Stacks Project.

**`Stacks.Thickenings.firstOrderThickening_squareZeroExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/SquareZeroExtension/OfFirstOrderThickening.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/SquareZeroExtension/OfFirstOrderThickening.lean#L425). The attribute's comment: “converse: every first-order thickening has this form”.

> Every first-order thickening over a base is obtained from a square-zero extension.

```lean
public theorem firstOrderThickening_squareZeroExtension {X Y S : Scheme.{u}}
    (i : X ⟶ Y) (g : Y ⟶ S) (hi : Stacks.Thickenings.IsFirstOrderThickening i) :
    ∃ E : SquareZeroExtension (i ≫ g),
      ∃ r : Realization E, r.ambient = Y ∧ HEq r.immersion i ∧ HEq r.toBase g
```

**`Stacks.Thickenings.squareZeroExtension_realization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/SquareZeroExtension/Realization.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/SquareZeroExtension/Realization.lean#L744). The attribute's comment: “construction from a square-zero extension”.

> A square-zero extension with quasi-coherent kernel gives a first-order thickening.

```lean
public theorem squareZeroExtension_realization {X S : Scheme.{u}} {f : X ⟶ S}
    (E : SquareZeroExtension f) : Nonempty (Realization E)
```

## Tag 06AD, a lemma

[Tag 06AD](https://stacks.math.columbia.edu/tag/06AD) in the Stacks Project.

**`Stacks.Thickenings.isAffine_of_isThickening_of_surjective_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningAffine.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningAffine.lean#L190).

> **A thickening of an affine scheme whose map on global sections is surjective has affine
> ambient scheme.**  This is [Stacks Project, Tag 06AD] with its cohomological content — the
> surjectivity of `i.appTop` — as the explicit hypothesis `hsurj`, which is the only thing assumed:
> everything else in the tag is proved here, through the affineness criterion of
> [Stacks Project, Tag 01QF].  The hypothesis is not needed for the tag itself: it is dropped in
> `Stacks.Thickenings.isAffine_of_isThickening`, which proves Tag 06AD outright from
> [Stacks Project, Tag 01ZT].

```lean
theorem isAffine_of_isThickening_of_surjective_appTop [IsAffine X] {i : X ⟶ X'}
    (hi : IsThickening i) (hsurj : Function.Surjective i.appTop.hom) : IsAffine X'
```

**`Stacks.Thickenings.isAffine_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningAffineFirstOrder.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningAffineFirstOrder.lean#L199). The attribute's comment: “the finite-order case, the second proof the source gives (EGA I, Prop 5.1.9)”.

> **Any finite-order thickening of an affine scheme is affine.** The adic filtration of the
> defining ideal sheaf interpolates between the closed subscheme and the ambient scheme by
> first-order thickenings.

```lean
theorem isAffine_of_isFiniteOrderThickening {i : X ⟶ X'} (hi : IsFiniteOrderThickening i)
    [IsAffine X] : IsAffine X'
```

**`Stacks.Thickenings.isAffine_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Affine.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Affine.lean#L39).

> **A thickening of an affine scheme is affine.** A closed immersion is a finite morphism, and
> a thickening is surjective, so this is the affineness of the target of a finite surjective
> morphism with affine source.

```lean
theorem isAffine_of_isThickening {X X' : Scheme.{u}} {i : X ⟶ X'} (hi : IsThickening i)
    [IsAffine X] : IsAffine X'
```

## Tag 09ZU, a lemma

[Tag 09ZU](https://stacks.math.columbia.edu/tag/09ZU) in the Stacks Project.

**`Stacks.Thickenings.baseChangeHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean#L237). The attribute's comment: “canonical morphism of thickenings”.

> The canonical morphism from the base change of a thickening `i : S ⟶ S'` along
> `f : X' ⟶ S'` to `i` itself: the commutative square given by the pullback.

```lean
noncomputable def baseChangeHom {S S' X' : Scheme.{u}}
    (i : S ⟶ S') (f : X' ⟶ S') :
    Arrow.mk (pullback.snd i f) ⟶ Arrow.mk i
```

**`Stacks.Thickenings.isThickening_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean#L244). The attribute's comment: “base change of thickenings”.

> Thickenings of schemes are stable under arbitrary base change.

```lean
instance isThickening_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsThickening : MorphismProperty Scheme.{u})
```

**`Stacks.Thickenings.isFirstOrderThickening_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean#L253). The attribute's comment: “base change of first-order thickenings”.

> First-order thickenings of schemes are stable under arbitrary base change.

```lean
instance isFirstOrderThickening_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsFirstOrderThickening : MorphismProperty Scheme.{u})
```

**`Stacks.Thickenings.isFiniteOrderThickening_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean#L267). The attribute's comment: “base change of finite-order thickenings”.

> Finite-order thickenings of schemes are stable under arbitrary base change.

```lean
instance isFiniteOrderThickening_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsFiniteOrderThickening : MorphismProperty Scheme.{u})
```

**`Stacks.Thickenings.isThickening_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean#L134). The attribute's comment: “a base change of a thickening is a thickening”. References: EGA I (4.3.2), “thickenings”.

> **A base change of a thickening is a thickening.** If `i : Z ⟶ Y` is a thickening and the
> square with sides `f' : P ⟶ X`, `g' : P ⟶ Z`, `f : X ⟶ Y` and `i` is a pullback square, then `f'`
> is a thickening.

```lean
theorem isThickening_of_isPullback {f' : P ⟶ X} {g' : P ⟶ Z} {f : X ⟶ Y} {i : Z ⟶ Y}
    (h : IsPullback f' g' f i) (hi : IsThickening i) : IsThickening f'
```

**`Stacks.Thickenings.isNthOrderThickening_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean#L143). The attribute's comment: “a base change of an nth-order thickening is an nth-order thickening”.

> **A base change of an `n`th-order thickening is an `n`th-order thickening.** If `i` is an
> `n`th-order thickening and the square with sides `f'`, `g'`, `f` and `i` is a pullback square, then
> `f'` is an `n`th-order thickening.

```lean
theorem isNthOrderThickening_of_isPullback {f' : P ⟶ X} {g' : P ⟶ Z} {f : X ⟶ Y} {i : Z ⟶ Y}
    {n : ℕ} (h : IsPullback f' g' f i) (hi : IsNthOrderThickening n i) :
    IsNthOrderThickening n f'
```

**`Stacks.Thickenings.isFirstOrderThickening_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean#L152). The attribute's comment: “a base change of a first-order thickening is a first-order thickening”.

> **A base change of a first-order thickening is a first-order thickening.** If `i` is a
> first-order thickening and the square with sides `f'`, `g'`, `f` and `i` is a pullback square, then
> `f'` is a first-order thickening.

```lean
theorem isFirstOrderThickening_of_isPullback {f' : P ⟶ X} {g' : P ⟶ Z} {f : X ⟶ Y} {i : Z ⟶ Y}
    (h : IsPullback f' g' f i) (hi : IsFirstOrderThickening i) :
    IsFirstOrderThickening f'
```

**`Stacks.Thickenings.isFiniteOrderThickening_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/BaseChange.lean#L161). The attribute's comment: “a base change of a finite-order thickening is a finite-order thickening”.

> **A base change of a finite-order thickening is a finite-order thickening.** If `i` is a
> finite-order thickening and the square with sides `f'`, `g'`, `f` and `i` is a pullback square,
> then `f'` is a finite-order thickening.

```lean
theorem isFiniteOrderThickening_of_isPullback {f' : P ⟶ X} {g' : P ⟶ Z} {f : X ⟶ Y} {i : Z ⟶ Y}
    (h : IsPullback f' g' f i) (hi : IsFiniteOrderThickening i) :
    IsFiniteOrderThickening f'
```

## Tag 0BPE, a lemma

[Tag 0BPE](https://stacks.math.columbia.edu/tag/0BPE) in the Stacks Project.

**`Stacks.Thickenings.isThickening_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Stability.lean#L275).

> A composite of thickenings is a thickening.

```lean
theorem isThickening_comp {X Y Z : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsThickening f) (hg : IsThickening g) : IsThickening (f ≫ g)
```

## Tag 0BPF, a lemma

[Tag 0BPF](https://stacks.math.columbia.edu/tag/0BPF) in the Stacks Project.

**`Stacks.Thickenings.isThickening_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/FpqcLocal.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/FpqcLocal.lean#L64). The attribute's comment: “thickenings”.

> **Stacks Project, Tag 0BPF.** Being a thickening is fpqc local on the target: a morphism
> whose base changes along the members of an fpqc covering of the target are all thickenings is
> itself a thickening.

```lean
instance isThickening_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsThickening : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

**`Stacks.Thickenings.isFirstOrderThickening_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/FpqcLocal.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/FpqcLocal.lean#L146). The attribute's comment: “first-order thickenings”.

> **Stacks Project, Tag 0BPF.** Being a first-order thickening is fpqc local on the target: a
> morphism whose base changes along the members of an fpqc covering of the target are all
> first-order thickenings is itself a first-order thickening.

```lean
instance isFirstOrderThickening_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsFirstOrderThickening : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.2, Tag 04EW](https://stacks.math.columbia.edu/tag/04EW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
