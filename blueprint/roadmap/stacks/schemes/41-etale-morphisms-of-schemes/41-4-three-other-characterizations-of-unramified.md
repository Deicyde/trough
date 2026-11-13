---
declaration: section
origin: cited
lean: AlgebraicGeometry.stalkwiseUnramifiedAt_tfae, AlgebraicGeometry.stalkwiseUnramifiedAt_iff_hasDifferentialPresentationAt, AlgebraicGeometry.stalkwiseUnramifiedAt_tfae₄
statement: formalized
proof: formalized
---

# 41.4 Three other characterizations of unramified morphisms

Section 41.4 of the Stacks Project, [Tag 024O](https://stacks.math.columbia.edu/tag/024O). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 024P, a theorem

[Tag 024P](https://stacks.math.columbia.edu/tag/024P) in the Stacks Project.

**`AlgebraicGeometry.stalkwiseUnramifiedAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedCharacterizations.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedCharacterizations.lean#L123). The attribute's comment: “equivalence of conditions (1), (2) and (4)”. References: EGA IV (17.4.2), “Y loc. Noetherian, at x”; EGA IV (17.4.1), “Y loc. Noeth.; a),b),c)”.

> **Stacks Project, Tag 024P.** Let `Y` be a locally Noetherian scheme, `f : X ⟶ Y` a morphism
> locally of finite type and `x` a point of `X`. Then `f` is unramified at `x` if and only if the
> stalk at `x` of the sheaf of relative differentials of `f` vanishes, and if and only if the
> diagonal `Δ_{X/Y}` is a local isomorphism at `x`.

```lean
theorem stalkwiseUnramifiedAt_tfae (f : X ⟶ Y) [IsLocallyNoetherian Y] [LocallyOfFiniteType f]
    (x : X) :
    List.TFAE [
      StalkwiseUnramifiedAt f x,
      Subsingleton ((Scheme.Hom.relativeDifferentials f).presheaf.stalk x),
      ∃ U : X.Opens, x ∈ U ∧ IsOpenImmersion (U.ι ≫ pullback.diagonal f)]
```

**`AlgebraicGeometry.stalkwiseUnramifiedAt_iff_hasDifferentialPresentationAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedDifferentialPresentation.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedDifferentialPresentation.lean#L251). The attribute's comment: “equivalence of conditions (1) and (3)”.

> **Stacks Project, Tag 024P, condition (3).** For a morphism locally of finite type to a
> locally Noetherian scheme, unramifiedness at `x` is equivalent to the existence of a local closed
> immersion into an affine space over an open of the target whose defining ideal has generating
> differentials at the image of `x`.

```lean
theorem stalkwiseUnramifiedAt_iff_hasDifferentialPresentationAt (f : X ⟶ Y)
    [IsLocallyNoetherian Y] [LocallyOfFiniteType f] (x : X) :
    StalkwiseUnramifiedAt f x ↔ HasDifferentialPresentationAt f x
```

**`AlgebraicGeometry.stalkwiseUnramifiedAt_tfae₄`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedDifferentialPresentation.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/UnramifiedDifferentialPresentation.lean#L274). The attribute's comment: “equivalence of conditions (1), (2), (3) and (4)”.

> **Stacks Project, Tag 024P.** Let `Y` be a locally Noetherian scheme, `f : X ⟶ Y` a morphism
> locally of finite type and `x` a point of `X`. The following are equivalent: `f` is unramified at
> `x`; the stalk at `x` of the sheaf of relative differentials of `f` vanishes; `f` restricts near
> `x` to a closed immersion into an affine space over an open of `Y` whose defining ideal has
> generating differentials at the image of `x`; and the diagonal `Δ_{X/Y}` is a local isomorphism
> at `x`.

```lean
theorem stalkwiseUnramifiedAt_tfae₄ (f : X ⟶ Y) [IsLocallyNoetherian Y] [LocallyOfFiniteType f]
    (x : X) :
    List.TFAE [
      StalkwiseUnramifiedAt f x,
      Subsingleton ((Scheme.Hom.relativeDifferentials f).presheaf.stalk x),
      HasDifferentialPresentationAt f x,
      ∃ U : X.Opens, x ∈ U ∧ IsOpenImmersion (U.ι ≫ pullback.diagonal f)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.4, Tag 024O](https://stacks.math.columbia.edu/tag/024O)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
