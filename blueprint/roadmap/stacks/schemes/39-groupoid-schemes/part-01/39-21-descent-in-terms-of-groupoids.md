---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsCartesian, AlgebraicGeometry.CartesianOver, AlgebraicGeometry.CartesianOver.Hom, AlgebraicGeometry.nonempty_cartesianOverEquivariantEquivalenceData, AlgebraicGeometry.cartesianOverEquivalenceEquivariantScheme, AlgebraicGeometry.cartesianOverEquivDescentDatum, AlgebraicGeometry.cartesianOverPairGroupoidEquivDescentDatum
statement: formalized
proof: formalized
---

# 39.21 Descent in terms of groupoids

Section 39.21 of the Stacks Project, [Tag 0APC](https://stacks.math.columbia.edu/tag/0APC). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0APD, a definition

[Tag 0APD](https://stacks.math.columbia.edu/tag/0APD) in the Stacks Project.

**`AlgebraicGeometry.IsCartesian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean#L45). The attribute's comment: “the cartesian condition”.

> A morphism of groupoid schemes is cartesian if its square of source maps is a pullback.

```lean
abbrev IsCartesian {S : Scheme.{u}} {G H : GroupoidScheme S}
    (F : GroupoidScheme.Hom G H) : Prop
```

**`AlgebraicGeometry.CartesianOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean#L51). The attribute's comment: “groupoid schemes cartesian over a fixed groupoid scheme”.

> A groupoid scheme cartesian over a fixed groupoid scheme `H`.

```lean
structure CartesianOver {S : Scheme.{u}} (H : GroupoidScheme S)
```

**`AlgebraicGeometry.CartesianOver.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Cartesian.lean#L62). The attribute's comment: “morphisms cartesian over a fixed groupoid scheme”.

> A morphism of groupoid schemes cartesian over `H` is a morphism compatible with both
> components of the structure morphisms to `H`.

```lean
structure CartesianOver.Hom {S : Scheme.{u}} {H : GroupoidScheme S}
    (X Y : CartesianOver H)
```

## Tag 0APE, a lemma

[Tag 0APE](https://stacks.math.columbia.edu/tag/0APE) in the Stacks Project.

**`AlgebraicGeometry.nonempty_cartesianOverEquivariantEquivalenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Equivariant/Equivalence.lean, line 719](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Equivariant/Equivalence.lean#L719). The attribute's comment: “the equivalence with the forward construction in the proof”.

> There is an equivalence between groupoid schemes cartesian over `G` and equivariant schemes
> for `G` satisfying the equations of `CartesianOverEquivariantEquivalenceData` on objects, descent
> isomorphisms, and morphisms.

```lean
theorem nonempty_cartesianOverEquivariantEquivalenceData
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    Nonempty (CartesianOverEquivariantEquivalenceData G)
```

**`AlgebraicGeometry.cartesianOverEquivalenceEquivariantScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Equivariant/Equivalence.lean, line 757](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Equivariant/Equivalence.lean#L757).

> Cartesian groupoid schemes over `G` are equivalent to schemes over the
> object scheme of `G` endowed with a normalized cocyclic pullback isomorphism.

```lean
noncomputable def cartesianOverEquivalenceEquivariantScheme
    {S : Scheme.{u}} (G : GroupoidScheme S) :
    CartesianOver G ≌ EquivariantScheme G
```

## Tag 0APF, a lemma

[Tag 0APF](https://stacks.math.columbia.edu/tag/0APF) in the Stacks Project.

**`AlgebraicGeometry.cartesianOverEquivDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/PairGroupoidDescent.lean, line 769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/PairGroupoidDescent.lean#L769). The attribute's comment: “the equivalence for the base scheme equal to the target of `f`”.

> Groupoid schemes cartesian over the pair groupoid `(X, X ×_S X, s, t, c)`, as a groupoid
> scheme over `S`, are the same thing as descent data relative to `X/S`.

```lean
def cartesianOverEquivDescentDatum (f : X ⟶ S) :
    CartesianOver (pairGroupoid f) ≌ DescentDatum f
```

**`AlgebraicGeometry.cartesianOverPairGroupoidEquivDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/PairGroupoidDescentGeneral.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/PairGroupoidDescentGeneral.lean#L62). The attribute's comment: “the equivalence for a morphism of schemes over a base `S`, the general case”.

> **Tag 0APF.**  Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of schemes over `S`,
> the structure morphism of `Y` being `g : Y ⟶ S`.  Groupoid schemes over `S` cartesian over the
> pair groupoid `(X, X ×_Y X, \mathrm{pr}_1, \mathrm{pr}_0, \mathrm{pr}_{02})` are the same thing
> as descent data relative to `X/Y`.

```lean
def cartesianOverPairGroupoidEquivDescentDatum {S Y X : Scheme.{u}} (g : Y ⟶ S) (f : X ⟶ Y) :
    CartesianOver ((pairGroupoid f).pushforward g) ≌ DescentDatum f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.21, Tag 0APC](https://stacks.math.columbia.edu/tag/0APC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
