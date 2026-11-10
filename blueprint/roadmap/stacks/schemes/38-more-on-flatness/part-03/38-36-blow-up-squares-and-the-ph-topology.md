---
declaration: section
origin: cited
lean: AlgebraicGeometry.BlowUpSquare, AlgebraicGeometry.BlowUpSquare.isPullback, Scheme.IdealSheafData.comapIso, AlgebraicGeometry.BigPHOver.isPullback_map_of_blowUpSquare, AlgebraicGeometry.BigPHOver.bijective_map_of_isThickening
statement: formalized
proof: formalized
---

# 38.36 Blow up squares and the ph topology

Section 38.36 of the Stacks Project, [Tag 0EW0](https://stacks.math.columbia.edu/tag/0EW0). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EV5, an equation

[Tag 0EV5](https://stacks.math.columbia.edu/tag/0EV5) in the Stacks Project.

**`AlgebraicGeometry.BlowUpSquare`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean#L66).

> The data fixed by a blowup square: a closed centre of finite presentation in its base
> scheme. The other corners and all the arrows are canonically determined.

```lean
public structure BlowUpSquare
```

**`AlgebraicGeometry.BlowUpSquare.isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean#L124). The attribute's comment: “the blow up square”. References: SGA 6 0 (6.Lemma3), “partial”; SGA 6 VII (3.7), “more general”.

> **Stacks Project, Tag 0EV5.** The blowup square
>
> ```
> E ⟶ X'
> ↓    ↓ b
> Z ⟶ X
> ```
>
> commutes and is cartesian: the exceptional divisor `E` is the inverse image `b⁻¹(Z)` of the
> centre, hence the fibre product of the blowup morphism `b` and the inclusion of the centre.
> Commutativity alone is `AlgebraicGeometry.BlowUpSquare.isPullback.w`.

```lean
public theorem isPullback :
    IsPullback s.exceptionalInclusion s.exceptionalProjection s.blowUpMorphism
      s.centerInclusion
```

Declarations registered for the tag:

- [`Scheme.IdealSheafData.comapIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.IdealSheafData.comapIso#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Basic.lean#L61) (StacksFrontier): “cartesian square”.

## Tag 0EW1, a lemma

[Tag 0EW1](https://stacks.math.columbia.edu/tag/0EW1) in the Stacks Project.

**`AlgebraicGeometry.BigPHOver.isPullback_map_of_blowUpSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/PhSheaf.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/PhSheaf.lean#L498).

> **Stacks Project, Tag 0EW1.** Let `F` be a sheaf of sets on a big ph site over `S`. For every
> blow up square in that site — a closed centre `Z ⊆ X` of finite presentation, the blowup
> `b : X' ⟶ X` of `X` in `Z`, and the exceptional divisor `E = b⁻¹(Z)` — the square of restriction
> maps `F(X) → F(Z) → F(E)` and `F(X) → F(X') → F(E)` is cartesian in the category of sets.

```lean
public theorem isPullback_map_of_blowUpSquare
    (B : BigPHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigPHOver B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigPHOver.topology B S hS) F)
    {X X' Z E : BigPHOver B S hS}
    (b : X' ⟶ X) (z : Z ⟶ X) (p : E ⟶ X') (e : E ⟶ Z)
    (I : ((BigPHOver.toScheme B S hS).obj X).IdealSheafData)
    (hI : FinitePresentation I.subschemeι)
    (hb : Nonempty (Over.mk ((BigPHOver.toScheme B S hS).map b) ≅ Over.mk (blowUpToBase I)))
    (hZ : Nonempty (Over.mk ((BigPHOver.toScheme B S hS).map z) ≅ Over.mk I.subschemeι))
    (hSquare : IsPullback
      ((BigPHOver.toScheme B S hS).map e) ((BigPHOver.toScheme B S hS).map p)
      ((BigPHOver.toScheme B S hS).map z) ((BigPHOver.toScheme B S hS).map b)) :
    IsPullback (F.map z.op) (F.map b.op) (F.map e.op) (F.map p.op)
```

## Tag 0EW2, a lemma

[Tag 0EW2](https://stacks.math.columbia.edu/tag/0EW2) in the Stacks Project.

**`AlgebraicGeometry.BigPHOver.bijective_map_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/PhThickening.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/PhThickening.lean#L52).

> **Stacks Project, Tag 0EW2.** Restriction of a ph sheaf along a thickening is a bijection
> of sections.

```lean
theorem BigPHOver.bijective_map_of_isThickening
    (B : BigPHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : Sheaf (BigPHOver.topology B S hS) (Type v))
    {X X' : BigPHOver B S hS} (i : X ⟶ X')
    (hi : Stacks.Thickenings.IsThickening ((BigPHOver.toScheme B S hS).map i)) :
    Function.Bijective (F.obj.map i.op)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.36, Tag 0EW0](https://stacks.math.columbia.edu/tag/0EW0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
