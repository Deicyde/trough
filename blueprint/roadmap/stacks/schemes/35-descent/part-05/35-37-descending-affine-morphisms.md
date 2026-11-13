---
declaration: section
origin: cited
lean: AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom, AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isAffineHom, AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom_of_anyIndex, AlgebraicGeometry.DescentData.isFamilyEffective_of_isClosedImmersion
statement: formalized
proof: formalized
---

# 35.37 Descending affine morphisms

Section 35.37 of the Stacks Project, [Tag 0244](https://stacks.math.columbia.edu/tag/0244). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0245, a lemma

[Tag 0245](https://stacks.math.columbia.edu/tag/0245) in the Stacks Project.

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineFpqcFamilyEffective.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AffineFpqcFamilyEffective.lean#L100). The attribute's comment: “for a covering family indexed in the universe of the schemes”. References: SGA 3 IX (2.3), “partial”; SGA 3 VIII (1.7.2), “more general”; SGA 3 X (5.4), “special case”; SGA 3 XXIV (3.11.2), “partial”.

> Let `S` be a scheme, let `{X i ⟶ S}` be a covering family of `S` for the fpqc topology, and
> let `D` be a descent datum relative to that family all of whose structure morphisms `V i ⟶ X i`
> are affine. Then `D` is effective: it is isomorphic to the canonical descent datum of a scheme over
> `S`.

```lean
theorem DescentData.isFamilyEffective_of_isAffineHom {S : Scheme.{u}} {I : Type u}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S) (D : DescentData f)
    (hD : ∀ i, IsAffineHom (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineHomFpqcDescent.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AffineHomFpqcDescent.lean#L85). The attribute's comment: “the case of an affine base”. References: SGA 3 IX (2.3), “partial”; SGA 3 VIII (1.7.2), “(ii), special case”; SGA 3 XXIV (3.11.2), “special case”.

> **[Stacks, Tag 0245](https://stacks.math.columbia.edu/tag/0245) over an affine base.** Let `S`
> be an affine scheme, let `{X i ⟶ S}` be an fpqc covering family and let `D` be a descent datum
> relative to it whose structure morphism over each `X i` is affine. Then `D` is effective: it is
> isomorphic to the canonical descent datum of a scheme over `S`.

```lean
theorem isFamilyEffective_of_forall_isAffineHom {ι : Type u} {S : Scheme.{u}} [IsAffine S]
    {X : ι → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hP : ∀ i, IsAffineHom (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom_of_anyIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FamilyEffectivityLargeIndex.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FamilyEffectivityLargeIndex.lean#L211). The attribute's comment: “for a covering family indexed in an arbitrary universe”. References: SGA 3 IX (2.3), “partial”.

> **Effective descent for affine morphisms along an fpqc covering family indexed in an arbitrary
> universe.** Let `S` be a scheme, let `{X i ⟶ S}` be a covering family of `S` for the fpqc topology,
> indexed by a type in an arbitrary universe, and let `D` be a descent datum relative to that family
> all of whose structure morphisms `V i ⟶ X i` are affine. Then `D` is effective: it is isomorphic to
> the canonical descent datum of a scheme over `S`.

```lean
theorem isFamilyEffective_of_isAffineHom_of_anyIndex {I : Type v} {S : Scheme.{u}}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S) (D : DescentData f)
    (hD : ∀ i, IsAffineHom (D.obj i).hom) : D.IsFamilyEffective
```

## Tag 03I0, a lemma

[Tag 03I0](https://stacks.math.columbia.edu/tag/03I0) in the Stacks Project.

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ClosedImmersionFpqcDescent.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ClosedImmersionFpqcDescent.lean#L78). References: SGA 3 IV (4.7), “partial”; SGA 3 IV (6.4.1), “partial”; SGA 3 VIII (6.4), “Object effectivity”.

> **A descent datum relative to an fpqc covering whose components are closed immersions is
> effective.** Let `S` be a scheme, let `{X i ⟶ S}` be an fpqc covering and let `D` be a descent
> datum relative to it whose structure morphism over each `X i` is a closed immersion. Then `D` is
> isomorphic to the canonical descent datum of a scheme over `S`.
>
> A closed immersion is affine, so this is effective descent for affine morphisms along an fpqc
> covering, Stacks 0245, at a smaller class of morphisms.

```lean
theorem isFamilyEffective_of_isClosedImmersion {I : Type v} {S : Scheme.{u}}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S) (D : DescentData f)
    (hD : ∀ i, IsClosedImmersion (D.obj i).hom) :
    D.IsFamilyEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.37, Tag 0244](https://stacks.math.columbia.edu/tag/0244)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
