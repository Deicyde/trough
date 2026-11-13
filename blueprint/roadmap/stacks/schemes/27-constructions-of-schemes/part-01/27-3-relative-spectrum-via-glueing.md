---
declaration: section
origin: cited
lean: Stacks.RelativeSpec.RelativeSpecSituation, Stacks.RelativeSpec.isPullback_specMap_restriction, Stacks.RelativeSpec.specMap_restriction_comp, Stacks.RelativeSpec.relativeSpectrum, Stacks.RelativeSpec.existsUnique_relativeSpectrumIso, Stacks.RelativeSpec.gluedSpectrum, Stacks.RelativeSpec.existsUnique_gluedSpectrumIso
statement: formalized
proof: formalized
---

# 27.3 Relative spectrum via glueing

Section 27.3 of the Stacks Project, [Tag 01LL](https://stacks.math.columbia.edu/tag/01LL). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01LM, a situation

[Tag 01LM](https://stacks.math.columbia.edu/tag/01LM) in the Stacks Project.

**`Stacks.RelativeSpec.RelativeSpecSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean#L207).

> A scheme equipped with a quasi-coherent sheaf of commutative
> algebras over its structure sheaf.

```lean
structure RelativeSpecSituation
```

## Tag 01LN, a lemma

[Tag 01LN](https://stacks.math.columbia.edu/tag/01LN) in the Stacks Project.

**`Stacks.RelativeSpec.isPullback_specMap_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean#L221).

> For nested affine opens `U ⊆ U'` of the base of a relative spectrum situation, the square
> formed by the spectra of the sections of the quasi-coherent algebra, the two open subschemes,
> and their canonical restriction morphisms is cartesian.

```lean
theorem isPullback_specMap_restriction (s : RelativeSpecSituation.{u})
    (U U' : s.base.Opens) (hU : IsAffineOpen U) (hU' : IsAffineOpen U') (h : U ≤ U') :
    IsPullback
      (Spec.map (s.algebra.right.obj.map (homOfLE h).op))
      (Spec.map (s.algebra.hom.hom.app (.op U)) ≫ hU.isoSpec.inv)
      (Spec.map (s.algebra.hom.hom.app (.op U')) ≫ hU'.isoSpec.inv)
      (s.base.homOfLE h)
```

## Tag 01LO, a lemma

[Tag 01LO](https://stacks.math.columbia.edu/tag/01LO) in the Stacks Project.

**`Stacks.RelativeSpec.specMap_restriction_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/QuasicoherentSquare.lean#L237). The attribute's comment: “the composite of the restriction morphisms of spectra of sections is the restriction morphism”.

> For opens `U ⊆ U' ⊆ U''` of the base of a relative spectrum situation, the composition of
> the morphisms `Spec A(U) ⟶ Spec A(U')` and `Spec A(U') ⟶ Spec A(U'')` of
> `Stacks.RelativeSpec.isPullback_specMap_restriction` is the morphism `Spec A(U) ⟶ Spec A(U'')`
> of the same lemma.

```lean
theorem specMap_restriction_comp (s : RelativeSpecSituation.{u}) {U U' U'' : s.base.Opens}
    (h : U ≤ U') (h' : U' ≤ U'') :
    Spec.map (s.algebra.right.obj.map (homOfLE h).op) ≫
        Spec.map (s.algebra.right.obj.map (homOfLE h').op) =
      Spec.map (s.algebra.right.obj.map (homOfLE (h.trans h')).op)
```

## Tag 01LP, a lemma

[Tag 01LP](https://stacks.math.columbia.edu/tag/01LP) in the Stacks Project.

**`Stacks.RelativeSpec.relativeSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Construction.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/Construction.lean#L123). References: EGA II (1.3.1), “existence”; EGA IV (21.12.1), “more general”; SGA 3 I (4.2).

> **Stacks Project, Tag 01LP**, existence. The affine spectra of the sections of a
> quasi-coherent algebra glue to a scheme over the base, with the prescribed inverse images and
> the prescribed transition morphisms.
>
> The glued scheme and its structure morphism are
> `Stacks.AffineAlgebraEquivalence.relativeSpec` and
> `Stacks.AffineAlgebraEquivalence.relativeSpecToBase`; the content added here is that its
> charts satisfy properties (1) and (2) of the tag.

```lean
def relativeSpectrum : RelativeSpectrum s
```

**`Stacks.RelativeSpec.existsUnique_relativeSpectrumIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Construction.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/Construction.lean#L280).

> **Stacks Project, Tag 01LP**, uniqueness. Any two relative spectra of the same
> quasi-coherent algebra admit a unique isomorphism over the base compatible with all the
> charts.

```lean
theorem existsUnique_relativeSpectrumIso (X Y : RelativeSpectrum s) :
    ∃! e : X.scheme ≅ Y.scheme,
      (e.hom ≫ Y.toBase = X.toBase) ∧ ∀ U, X.chart U ≫ e.hom = Y.chart U
```

**`Stacks.RelativeSpec.gluedSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Glueing.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/Glueing.lean#L95). The attribute's comment: “existence and local properties”. References: EGA II (1.3.1), “existence”; SGA 3 I (4.2).

> **Stacks Project, Tag 01LP, parts (1) and (2).** The affine spectra of the sections of a
> quasi-coherent algebra glue to a scheme over the base, with the prescribed inverse images and
> transition open immersions.

```lean
noncomputable def gluedSpectrum (s : RelativeSpecSituation.{u}) : GluedSpectrum s
```

**`Stacks.RelativeSpec.existsUnique_gluedSpectrumIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Glueing.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpec/Glueing.lean#L248). The attribute's comment: “uniqueness”.

> **Stacks Project, Tag 01LP, uniqueness.** Any two schemes over the base carrying the affine
> charts of the relative spectrum admit a unique isomorphism over the base that respects all the
> charts.

```lean
theorem _root_.Stacks.RelativeSpec.existsUnique_gluedSpectrumIso
    (s : RelativeSpecSituation.{u}) (X Y : GluedSpectrum s) :
    ∃! e : X.scheme ≅ Y.scheme,
      (e.hom ≫ Y.toBase = X.toBase) ∧ (∀ U, X.chart U ≫ e.hom = Y.chart U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.3, Tag 01LL](https://stacks.math.columbia.edu/tag/01LL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
