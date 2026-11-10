---
declaration: section
origin: cited
lean: TopologicalRing.IsTopologicallyOfFiniteType, AlgebraicGeometry.FormalSpace.isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap, AlgebraicGeometry.FormalSpace.exists_isPullback_isFiniteTypeULift_formalSpectrumMap_stage, AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_of_isTaut, AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAndQuasiCompact_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal, AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal, AlgebraicGeometry.FormalSpace.isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap', AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_iff_isTaut_and_isTopologicallyOfFiniteType
statement: formalized
proof: formalized
---

# 87.29 Algebras topologically of finite type

Section 87.29 of the Stacks Project, [Tag 0ALL](https://stacks.math.columbia.edu/tag/0ALL). 9 tags here are carried by 33 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ANS, a definition

[Tag 0ANS](https://stacks.math.columbia.edu/tag/0ANS) in the Stacks Project.

**`TopologicalRing.IsTopologicallyOfFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/RestrictedPowerSeries.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/RestrictedPowerSeries.lean#L44).

> A ring homomorphism `φ : A →+* B` is *topologically of finite type* if there is an
> `A`-algebra map from a polynomial algebra in finitely many variables to `B` with dense image.

```lean
public abbrev IsTopologicallyOfFiniteType {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace B] (φ : A →+* B) : Prop
```

## Tag 0ANT, a lemma

[Tag 0ANT](https://stacks.math.columbia.edu/tag/0ANT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean#L383). The attribute's comment: “the implication (1) ⟹ (2) with tautness carried as a hypothesis: for a taut continuous homomorphism of weakly admissible topological rings over `S` whose formal spectrum map is of finite type, the homomorphism is topologically of finite type. Tautness is not deduced from (1), and (2) ⟹ (1) is not asserted; see the module docstring.”.

> **Stacks 0ANT, (1) ⟹ (2), granted tautness.** Let `φ : A ⟶ C` be a taut continuous
> homomorphism of weakly admissible topological rings over `S`. If `Spf (φ)` is of finite type,
> then `C` is topologically of finite type over `A`. Tautness is a hypothesis rather than a
> conclusion because this library has only one implication of Stacks 0AN5; the implication
> (2) ⟹ (1) is not asserted.

```lean
theorem isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (hf : RingHom.IsTaut f.toRingHom) (hFT : IsFiniteType B S hS (formalSpectrumMap hA f)) :
    TopologicalRing.IsTopologicallyOfFiniteType f.toRingHom
```

**`AlgebraicGeometry.FormalSpace.exists_isPullback_isFiniteTypeULift_formalSpectrumMap_stage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean#L416). The attribute's comment: “the stage half of the implication (2) ⟹ (1): for a homomorphism satisfying condition (a) of Stacks 0ANU — tautness together with finite type modulo every weak ideal of definition, which condition (2) implies — the base change of the formal spectrum map along the point cut out by a thickening stage is represented by an object of the site and is of finite type. Condition (1) itself quantifies over every scheme-valued point of `Spf A`, not only those factoring through a stage, and is not asserted; see the module docstring.”.

> **Stacks 0ANT, the stage half of (2) ⟹ (1).** Let `φ : A ⟶ C` be a continuous
> homomorphism of weakly admissible topological rings over `S` which is taut and of finite type
> modulo every weak ideal of definition, and let `I` be a weak ideal of definition of `A`. Then
> the base change of `Spf (φ)` along the point of `Spf A` cut out by the thickening stage
> `Spec (A ⧸ I)` is represented by an object of the site, and the representing morphism is of
> finite type.

```lean
theorem exists_isPullback_isFiniteTypeULift_formalSpectrumMap_stage
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (h : TopologicalRing.FiniteTypeModuloEveryWeakIdeal f.toRingHom)
    (I : Ideal A) (hI : TopologicalRing.IsWeakIdealOfDefinition I) :
    ∃ (V : BigFppfOver B S hS)
      (p : V ⟶ (BigAffineFppf.inclusion B S hS).obj (D.stage ⟨I, hI⟩))
      (q : (uliftYoneda.{u + 1}).obj V ⟶
        (sheafToPresheaf (BigFppfOver.topology B S hS) (Type (u + 1))).obj (formalSpectrum E)),
      IsPullback q ((uliftYoneda.{u + 1}).map p)
        ((sheafToPresheaf (BigFppfOver.topology B S hS) (Type (u + 1))).map
          (formalSpectrumMap hA f))
        ((sheafifiedYonedaObjIso B S hS
            ((BigAffineFppf.inclusion B S hS).obj (D.stage ⟨I, hI⟩))).hom ≫
          (sheafToPresheaf (BigFppfOver.topology B S hS) (Type (u + 1))).map
            (formalSpectrumInclusion D ⟨I, hI⟩)) ∧
      Space.IsFiniteTypeULift.{u + 1} B S hS ((uliftYoneda.{u + 1}).map p)
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_of_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeAllPoints.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeAllPoints.lean#L189). The attribute's comment: “the implication (2) ⟹ (1): a taut continuous homomorphism of weakly admissible topological rings over `S` whose target is topologically of finite type over its source has formal spectrum map of finite type, at every scheme-valued point of the target and not only at those factoring through a thickening stage. That the two formal spectra are affine formal algebraic spaces is Stacks 0AIF for a weakly admissible ring and belongs to the situation of the lemma, whose condition (1) speaks of a finite type morphism of them.”.

> **Stacks 0ANT, the implication (2) ⟹ (1).** Let `φ : A ⟶ C` be a continuous homomorphism of
> weakly admissible topological rings over `S` which is taut and such that `C` is topologically of
> finite type over `A`. Then `Spf (φ) : Spf C ⟶ Spf A` is of finite type.
>
> The base change of `Spf (φ)` along a point of `Spf A` out of an affine object of the site is an
> affine morphism of finite type of the site, and those two properties are Zariski local at the
> target, so the charts over the affine opens of an arbitrary test object glue.

```lean
theorem isFiniteType_formalSpectrumMap_of_isTaut
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (hD : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    (hE : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum E))
    (htaut : RingHom.IsTaut f.toRingHom)
    (hfin : TopologicalRing.IsTopologicallyOfFiniteType f.toRingHom) :
    IsFiniteType B S hS (formalSpectrumMap hA f)
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAndQuasiCompact_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean#L171). The attribute's comment: “the implication (2) ⟹ (1) with its conclusion unrestricted: the base change of the formal spectrum map is taken along an arbitrary scheme-valued point of `Spf A`, not only along one factoring through a thickening stage. Condition (1) is concluded as Definition 0AM4, part (2), verbatim; what the argument produces is condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — and Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, carries it to Definition 0AM4, part (2), unconditionally. Condition (2) is taken in the form of condition (a) of Stacks 0ANU, `TopologicalRing.FiniteTypeModuloEveryWeakIdeal`, which is what the source's proof of this implication derives from condition (2) in its first sentence; that derivation is `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType` and assumes no countability, so this implication is the source's with its hypothesis weakened. Condition (a) implies condition (2) back, with no countability assumption either, by `TopologicalRing.isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal`; condition (2) verbatim is the hypothesis of this implication as it appears in `AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_iff_isTaut_and_isTopologicallyOfFiniteType`”.

> **Stacks 0ANT, the implication (2) ⟹ (1).** Let `φ : A ⟶ C` be a continuous homomorphism
> of weakly admissible topological rings over `S` which is taut and of finite type modulo every
> weak ideal of definition. Then `Spf (φ) : Spf C ⟶ Spf A` is of finite type in the sense of
> Definition 0AM4, part (2): locally of finite type — representable by algebraic spaces, with
> its base change along *every* scheme-valued point of `Spf A` a morphism of algebraic spaces
> which is locally of finite type — and quasi-compact in the sense of Definition 0AJC.
>
> What the argument produces is condition (2) of Stacks 0AJJ: representability by algebraic
> spaces together with every base change along a scheme-valued point of `Spf A` being a
> morphism of algebraic spaces of finite type. Stacks 0AJJ,
> `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, carries that to
> Definition 0AM4, part (2), and is unconditional.
>
> Over a point whose source is quasi-compact the Bootstrap condition is the source's own
> computation, `AlgebraicGeometry.FormalSpace.compactPullbackRepresentable_formalSpectrumMap`;
> the passage to an arbitrary point is the locality of the three conditions on the target.

```lean
theorem isLocallyOfFiniteTypeAndQuasiCompact_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (h : TopologicalRing.FiniteTypeModuloEveryWeakIdeal f.toRingHom) :
    IsFiniteType' B S hS (formalSpectrumMap hA f)
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean#L199). The attribute's comment: “the implication (2) ⟹ (1) for the local condition of Stacks 0AM4 part (1), with the base change taken along an arbitrary scheme-valued point of `Spf A`; condition (2) is taken in the form of condition (a) of Stacks 0ANU, as on `AlgebraicGeometry.FormalSpace.isLocallyOfFiniteTypeAndQuasiCompact_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal`”.

> **Stacks 0ANT, the implication (2) ⟹ (1)**, read for the local condition: a continuous
> homomorphism of weakly admissible topological rings over `S` which is taut and of finite type
> modulo every weak ideal of definition has formal spectrum map locally of finite type, with the
> base change taken along an arbitrary scheme-valued point of `Spf A`.

```lean
theorem isLocallyOfFiniteType_formalSpectrumMap_of_finiteTypeModuloEveryWeakIdeal
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (h : TopologicalRing.FiniteTypeModuloEveryWeakIdeal f.toRingHom) :
    IsLocallyOfFiniteType B S hS (formalSpectrumMap hA f)
```

**`AlgebraicGeometry.FormalSpace.isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean#L226). The attribute's comment: “the implication (1) ⟹ (2) in full, with condition (1) read as Definition 0AM4, part (2), verbatim: both halves of condition (2) are deduced from condition (1). Tautness is the implication (1) ⟹ (3) of Stacks 0AN5, `AlgebraicGeometry.FormalSpace.isTaut_of_isRepresentableByAlgebraicSpaces_formalSpectrumMap`, applied to the representability by algebraic spaces that being locally of finite type contains. No hypothesis beyond the source's: that implication of Stacks 0AN5 carries no side condition, because the library's Stacks 0AKN consumes of a formal spectrum only its presentation by affine thickenings, which is its construction”.

> **Stacks 0ANT, the implication (1) ⟹ (2).** Let `φ : A ⟶ C` be a continuous homomorphism
> of weakly admissible topological rings over `S`. If `Spf (φ)` is of finite type — Definition
> 0AM4, part (2), verbatim — then `φ` is taut and `C` is topologically of finite type over `A`.
>
> Tautness is the implication (1) ⟹ (3) of Stacks 0AN5 applied to the representability that
> being locally of finite type contains, and that implication carries no side condition. Only
> the locally-of-finite-type half of condition (1) is used, here and in the ring-theoretic half
> `AlgebraicGeometry.FormalSpace.finiteType_quotientMap_of_isFiniteType_formalSpectrumMap`, so
> no comparison with condition (2) of Stacks 0AJJ is needed.

```lean
theorem isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (hFT : IsFiniteType' B S hS (formalSpectrumMap hA f)) :
    RingHom.IsTaut f.toRingHom ∧
      TopologicalRing.IsTopologicallyOfFiniteType f.toRingHom
```

**`AlgebraicGeometry.FormalSpace.isFiniteType_formalSpectrumMap_iff_isTaut_and_isTopologicallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean#L301). The attribute's comment: “the equivalence, with condition (1) read as Definition 0AM4, part (2), verbatim and condition (2) read verbatim as tautness together with being topologically of finite type. The forward implication is `AlgebraicGeometry.FormalSpace.isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'` and uses only the locally-of-finite-type half of condition (1); the backward implication goes through condition (a) of Stacks 0ANU by `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType` and then produces condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — and reaches Definition 0AM4, part (2), through Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, which is unconditional. No countability assumption is made: condition (2) and condition (a) of Stacks 0ANU imply one another outright, by `TopologicalRing.isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal` and `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType`. No hypothesis beyond the source's: the implication (1) ⟹ (3) of Stacks 0AN5 that the forward direction needs carries no side condition, the library's Stacks 0AKN consuming of a formal spectrum only its presentation by affine thickenings”.

> **Stacks 0ANT, the equivalence**, with both conditions read verbatim. Let `φ : A ⟶ C` be a
> continuous homomorphism of weakly admissible topological rings over `S`. Then `Spf (φ)` is of
> finite type — Definition 0AM4, part (2) — exactly when `φ` is taut and topologically of finite
> type.
>
> The forward implication is
> `isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'` and uses only the
> locally-of-finite-type half of condition (1). The backward implication
> passes through condition (a) of Stacks 0ANU by
> `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType` and then
> produces condition (2) of Stacks 0AJJ, reaching Definition 0AM4, part (2), through
> Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, which is
> unconditional.
>
> Condition (2) and condition (a) of Stacks 0ANU are interchangeable here with no countability
> assumption, in both directions: condition (a) implies condition (2) by
> `TopologicalRing.isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal`, for which
> weak pre-admissibility of the source suffices, and condition (2) implies condition (a) by
> `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType`. Condition (2)
> *is* condition (c) of Stacks 0ANU, so this identification is the half of that lemma which
> needs no countability; what the countable generation in the hypothesis of Stacks 0ANU —
> a morphism of `WAdm^count` — is spent on in `TopologicalRing.finiteType_tfae` are its
> conditions (b), the cofinal form of condition (a), and (d), the restricted power series
> presentation, and neither appears here. Both of those uses are of the source's filter, so
> `TopologicalRing.finiteType_tfae` assumes countable generation of that filter only.
>
> Nothing beyond the source's hypotheses is assumed. The forward implication needs the
> implication (1) ⟹ (3) of Stacks 0AN5, which carries no side condition because the library's
> Stacks 0AKN consumes of a formal spectrum only its presentation by affine thickenings,
> `AlgebraicGeometry.FormalSpace.hasThickeningPresentation_formalSpectrum`.

```lean
theorem isFiniteType_formalSpectrumMap_iff_isTaut_and_isTopologicallyOfFiniteType
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E) :
    IsFiniteType' B S hS (formalSpectrumMap hA f) ↔
      RingHom.IsTaut f.toRingHom ∧
        TopologicalRing.IsTopologicallyOfFiniteType f.toRingHom
```

**`AlgebraicGeometry.FormalSpace.isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautOfRepresentableByAlgebraicSpaces.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TautOfRepresentableByAlgebraicSpaces.lean#L72). The attribute's comment: “the implication (1) ⟹ (2): for a continuous homomorphism of weakly admissible topological rings over `S` whose formal spectrum map is of finite type, the homomorphism is taut and is topologically of finite type. That the two formal spectra are affine formal algebraic spaces is Stacks 0AIF for a weakly admissible ring and belongs to the situation of the lemma, whose condition (1) speaks of a finite type morphism of them.”.

> Let `φ : A ⟶ C` be a continuous homomorphism of weakly admissible topological rings over
> `S`, so that `Spf A` and `Spf C` are affine formal algebraic spaces. If `Spf (φ)` is of finite
> type, then `φ` is taut and `C` is topologically of finite type over `A`.

```lean
theorem isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (f : ContinuousHom D E)
    (hD : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    (hE : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum E))
    (hFT : IsFiniteType B S hS (formalSpectrumMap hA f)) :
    RingHom.IsTaut f.toRingHom ∧
      TopologicalRing.IsTopologicallyOfFiniteType f.toRingHom
```

## Tag 0AL1, a lemma

[Tag 0AL1](https://stacks.math.columbia.edu/tag/0AL1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.finiteTypeAlgebraSystemAntiEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/FiniteTypeClassification/AntiEquivalence.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/FiniteTypeClassification/AntiEquivalence.lean#L541). The attribute's comment: “anti-equivalence”.

> **Stacks 0AL1.** Let `X` be a McQuillan affine formal algebraic space over `S` presented as
> the formal spectrum of a weakly admissible topological ring `A`, and let `J` be a fundamental
> system of weak ideals of definition of `A`. The category of inverse systems of finite type
> algebras over the quotients of `J` is anti-equivalent to the category of finite type morphisms
> to `X` from affine formal algebraic spaces.

```lean
noncomputable def finiteTypeAlgebraSystemAntiEquivalence
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (A : Type u) [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A]
    (_hA : TopologicalRing.IsWeaklyAdmissible A)
    (X : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) (Type (u + 1)))
    (hX : HasSomeSurjectivePresentation B S hS X)
    (P : WeakIdealColimitPresentation B S hS A X)
    (I : Type v) [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (J : IdealBasis A I) :
    (FiniteTypeAlgebraSystem A I J)ᵒᵖ ≌ AffineFiniteTypeOver B S hS X
```

## Tag 0AJK, a remark

[Tag 0AJK](https://stacks.math.columbia.edu/tag/0AJK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.FiniteTypeAlgebraSystem.exists_uniform_generatedBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/UniformGenerators.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/UniformGenerators.lean#L210). The attribute's comment: “part (3), the asserted sentence: for the inverse system `(B_λ)` of finite type `A / I_λ`-algebras that Stacks 0AL1 attaches to a finite type morphism `Y → X = Spf(A)` of affine formal algebraic spaces, there is a fixed integer `r` such that `B_λ` is generated by `r` elements over `A / I_λ` for all `λ`. The clause of part (3) citing Stacks 0AL1 for the presentation `Y = colim Spec(B_λ)` is covered by the anti-equivalence itself; the question part (3) goes on to ask, whether there is an example in which `Y` is not McQuillan, is a question and is not asserted anywhere.”.

> **Stacks 0AJK, part (3): the uniform generator bound.** For an inverse system `(B_λ)` of
> finite type algebras over the quotients of `A` by a fundamental system of weak ideals of
> definition — the system Stacks 0AL1 attaches to a finite type morphism `Y → Spf(A)` of affine
> formal algebraic spaces — there is a single integer `r`, independent of `λ`, such that `B_λ` is
> generated by `r` elements over `A / I_λ` for every `λ`.
>
> The index `r` is produced from one member of the system, chosen using nonemptiness of the index,
> and transported to an arbitrary member through a common upper bound.

```lean
theorem exists_uniform_generatedBy [Nonempty I] [IsDirected I (· ≤ ·)]
    (P : FiniteTypeAlgebraSystem A I J) :
    ∃ r : ℕ, ∀ i : I, P.GeneratedBy r i
```

**`AlgebraicGeometry.FormalSpace.exists_taut_formalSpectrumMap_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean#L212). The attribute's comment: “part (1), every assertion of the item: for a closed immersion `f : Y → X` into `X = Spf(A)`, the source `Y` is McQuillan (condition (4) of Stacks 0AIC) and `f` corresponds to a continuous homomorphism `φ : A → B` of weakly admissible topological rings, `Y ≅ Spf(B)` with `f = Spf(φ)` through that isomorphism, which is taut, has closed kernel `K` and has dense image. The source `Y` is an arbitrary fppf sheaf here, which generalizes the item's affine formal algebraic space. The question the item ends with, which conditions on `A` force `B = (A/K)^∧`, is a question and is asserted nowhere. Part (2) of the remark is a question in its entirety and asserts nothing.”.

> **Stacks 0AJK, part (1).** Let `A` be a weakly admissible topological ring over `S` whose
> formal spectrum `X = Spf(A)` is an affine formal algebraic space, and let `f : Y ⟶ X` be a
> closed immersion. Then `Y` is a McQuillan affine formal algebraic space, and `f` corresponds to
> a continuous homomorphism `φ : A ⟶ B` of weakly admissible topological rings — `Y` is
> identified with `Spf(B)` and `f` with `Spf(φ)` — which is taut, whose kernel is a closed ideal
> of `A`, and whose image is dense in `B`.

```lean
theorem exists_taut_formalSpectrumMap_of_isClosedImmersion
    (hA : TopologicalRing.IsWeaklyAdmissible A) (D : QuotientSystem B S hS A)
    (hX : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    {Y : FppfSheaf B S hS} (f : Y ⟶ formalSpectrum D) (hf : IsClosedImmersion B S hS f) :
    HasSomeSurjectivePresentation B S hS Y ∧
      ∃ (C : Type u) (_ : CommRing C) (_ : TopologicalSpace C) (_ : IsTopologicalRing C)
        (_ : IsLinearTopology C C) (E : QuotientSystem B S hS C),
        TopologicalRing.IsWeaklyAdmissible C ∧
          ∃ (e : Y ≅ formalSpectrum E) (g : ContinuousHom D E),
            f = e.hom ≫ formalSpectrumMap hA g ∧ RingHom.IsTaut g.toRingHom ∧
              IsClosed (RingHom.ker g.toRingHom : Set A) ∧ DenseRange g.toRingHom
```

**`AlgebraicGeometry.FormalSpace.exists_finiteTypeAlgebraSystem_uniform_generatedBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean#L249). The attribute's comment: “part (3), every assertion of the item: a finite type morphism `f : Y → X` of affine formal algebraic spaces with `X = Spf(A)` gives `Y = colim Spec(B_λ)` for an object `(B_λ)` of the category `𝒞` of Stacks 0AL1, namely the object the anti-equivalence of Stacks 0AL1 sends to `f` (that functor is the colimit of the spectra of the terms), and one integer `r` generates every `B_λ` over `A/I_λ`. The question the item ends with, whether there is an example in which `Y` is not McQuillan, is a question and is asserted nowhere.”.

> **Stacks 0AJK, part (3).** Let `A` be a weakly admissible topological ring over `S` whose
> formal spectrum `X = Spf(A)` is an affine formal algebraic space, let `(I_λ)` be a fundamental
> system of weak ideals of definition of `A`, and let `f : Y ⟶ X` be a morphism of finite type
> from an affine formal algebraic space. Then `Y = colim Spec(B_λ)` for an object `(B_λ)` of the
> category `𝒞` of Stacks 0AL1 — the inverse system which the anti-equivalence of Stacks 0AL1
> sends to `f` — and there is a single integer `r` such that `B_λ` is generated by `r` elements
> over `A/I_λ` for every `λ`.

```lean
theorem exists_finiteTypeAlgebraSystem_uniform_generatedBy
    (hA : TopologicalRing.IsWeaklyAdmissible A) (D : QuotientSystem B S hS A)
    (hX : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    (I : Type v) [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)] (J : IdealBasis A I)
    {Y : FppfSheaf B S hS} (hY : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS Y)
    (f : Y ⟶ formalSpectrum D) (hf : IsFiniteType B S hS f) :
    ∃ P : FiniteTypeAlgebraSystem A I J,
      Nonempty ((finiteTypeAlgebraSystemAntiEquivalence B S hS A hA (formalSpectrum D)
          (hasSomeSurjectivePresentation_formalSpectrum_of_isAffine B S hS hA D hX)
          D.weakIdealColimitPresentation I J).functor.obj (Opposite.op P) ≅
            ⟨Over.mk f, hY, hf⟩) ∧
        ∃ r : ℕ, ∀ i : I, P.GeneratedBy r i
```

**`AlgebraicGeometry.FormalSpace.exists_taut_isTopologicallyOfFiniteType_affineSpace_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsIntoMcQuillanAffine.lean#L286). The attribute's comment: “part (4), every assertion of the item: for a finite type `f : Y → X = Spf(A)` with `Y` McQuillan, `f` corresponds to a continuous homomorphism `φ : A → B` of weakly admissible topological rings, `Y ≅ Spf(B)` with `f = Spf(φ)` through that isomorphism; `φ` is taut, which is derived from `f` being of finite type through Stacks 0AN5 and 0AKN; `B` is topologically of finite type over `A`; and `f` factors as `Y → 𝔸ʳ_X → X` with `𝔸ʳ_X = Spf A{x_1, ..., x_r}` the formal spectrum of the completion of `A[x_1, ..., x_r]` over the weak ideals of definition of `A`, the second arrow `Spf` of the canonical map and the first a closed immersion, both its source and its target being McQuillan affine formal algebraic spaces. The item's closing remark that questions (1) and (2) are then in force for `Y → 𝔸ʳ_X` asserts nothing further.”.

> **Stacks 0AJK, part (4).** Let `A` be a weakly admissible topological ring over `S` whose
> formal spectrum `X = Spf(A)` is an affine formal algebraic space, and let `f : Y ⟶ X` be a
> morphism of finite type with `Y` a McQuillan affine formal algebraic space. Then `f`
> corresponds to a continuous homomorphism `φ : A ⟶ B` of weakly admissible topological rings —
> `Y` is identified with `Spf(B)` and `f` with `Spf(φ)` — which is taut and makes `B`
> topologically of finite type over `A`. In other words `f` factors as
> `Y ⟶ 𝔸ʳ_X ⟶ X`, where `𝔸ʳ_X = Spf A{x₁, …, xᵣ}` maps to `X` by `Spf` of the canonical
> homomorphism and the first arrow is a closed immersion of McQuillan affine formal algebraic
> spaces.

```lean
theorem exists_taut_isTopologicallyOfFiniteType_affineSpace_factorization
    (hA : TopologicalRing.IsWeaklyAdmissible A) (D : QuotientSystem B S hS A)
    (hX : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D))
    {Y : FppfSheaf B S hS} (hYM : HasSomeSurjectivePresentation B S hS Y)
    (f : Y ⟶ formalSpectrum D) (hf : IsFiniteType B S hS f) :
    ∃ (C : Type u) (_ : CommRing C) (_ : TopologicalSpace C) (_ : IsTopologicalRing C)
      (_ : IsLinearTopology C C) (E : QuotientSystem B S hS C),
      TopologicalRing.IsWeaklyAdmissible C ∧
        ∃ (e : Y ≅ formalSpectrum E) (g : ContinuousHom D E),
          f = e.hom ≫ formalSpectrumMap hA g ∧ RingHom.IsTaut g.toRingHom ∧
            TopologicalRing.IsTopologicallyOfFiniteType g.toRingHom ∧
            ∃ (r : ℕ) (E' : QuotientSystem B S hS
                (TopologicalRing.CompletionOver (MvPolynomial.C : A →+* MvPolynomial (Fin r) A)))
              (π : ContinuousHom D E') (ι : ContinuousHom E' E),
              π.toRingHom = TopologicalRing.CompletionOver.canonicalMap MvPolynomial.C ∧
                HasSomeSurjectivePresentation B S hS (formalSpectrum E') ∧
                IsClosedImmersion B S hS (formalSpectrumMap
                  (TopologicalRing.completionOver_isWeaklyAdmissible MvPolynomial.C hA) ι) ∧
                f = e.hom ≫ formalSpectrumMap
                  (TopologicalRing.completionOver_isWeaklyAdmissible MvPolynomial.C hA) ι ≫
                    formalSpectrumMap hA π
```

Declarations registered for the tag:

- [`finiteTypeAlgebraSystemAntiEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finiteTypeAlgebraSystemAntiEquivalence#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/UniformGenerators.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/UniformGenerators.lean#L226) (StacksFrontier): “part (3), the clause citing Stacks 0AL1: a morphism `f : Y → X = Spf(A)` of affine formal algebraic spaces which is of finite type corresponds to an object `(B_λ)` of the category `𝒞`, so that `Y = colim Spec(B_λ)`. The uniform bound part (3) asserts next, that one integer `r` generates every `B_λ` over `A/I_λ`, is `AlgebraicGeometry.FormalSpace.FiniteTypeAlgebraSystem.exists_uniform_generatedBy` in this file. The question part (3) closes with, whether there is an example in which `Y` is not McQuillan, is a question and is asserted nowhere.”.
- [`hasSomeSurjectivePresentation_of_isClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=hasSomeSurjectivePresentation_of_isClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L160) (StacksFrontier): “part (1), the conclusion that `Y` is McQuillan: the source of a closed immersion of formal algebraic spaces whose target is a McQuillan affine formal algebraic space is again a McQuillan affine formal algebraic space. Part (1)'s conclusions about the presenting homomorphism `φ : A → B` are tagged separately. The question part (1) raises, which conditions on `A` force `B = (A/K)^∧`, is a question and is asserted nowhere.”.
- [`isClosed_ker_toRingHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isClosed_ker_toRingHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L331) (StacksFrontier): “part (1), the conclusion that the kernel `K ⊂ A` of the homomorphism `φ : A → B` presenting a closed immersion is a closed ideal. It is proved here in the stronger form that needs only continuity of the homomorphism and separatedness of its target, so no closed-immersion hypothesis appears.”.
- [`denseRange_of_isClosedImmersion_formalSpectrumMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=denseRange_of_isClosedImmersion_formalSpectrumMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillan.lean#L391) (StacksFrontier): “part (1), the conclusion that the image `φ(A)` of the homomorphism `φ : A → B` presenting a closed immersion is dense in `B`. Whether `φ` is moreover surjective and open, equivalently whether `B` is the quotient `A/K` itself, is the question part (2) of the remark raises and is asserted nowhere.”.
- [`hasSomeSurjectivePresentation_of_isClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=hasSomeSurjectivePresentation_of_isClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L46) (StacksFrontier): “part (1), the conclusion that `Y` is McQuillan: the source of a closed immersion of formal algebraic spaces whose target is a McQuillan affine formal algebraic space is again a McQuillan affine formal algebraic space. Part (1)'s three conclusions about the presenting homomorphism `φ : A → B` — that it is taut, that its kernel `K` is closed and that its image is dense — are tagged separately on `AlgebraicGeometry.FormalSpace.isTaut_of_isClosedImmersion_formalSpectrumMap`, `AlgebraicGeometry.FormalSpace.isClosed_ker_toRingHom` and `AlgebraicGeometry.FormalSpace.denseRange_of_isClosedImmersion_formalSpectrumMap`. The question part (1) raises, which conditions on `A` force `B = (A/K)^∧`, is a question and is asserted nowhere.”.
- [`isClosed_ker_toRingHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isClosed_ker_toRingHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L72) (StacksFrontier): “part (1), the conclusion that the kernel `K ⊂ A` of the homomorphism `φ : A → B` presenting a closed immersion is a closed ideal. It is proved here in the stronger form that needs only continuity of the homomorphism and separatedness of its target, so no closed-immersion hypothesis appears.”.
- [`denseRange_of_isClosedImmersion_formalSpectrumMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=denseRange_of_isClosedImmersion_formalSpectrumMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L78) (StacksFrontier): “part (1), the conclusion that the image `φ(A)` of the homomorphism `φ : A → B` presenting a closed immersion is dense in `B`. Whether `φ` is moreover surjective and open, equivalently whether `B` is the quotient `A/K` itself, is the question part (2) of the remark raises and is asserted nowhere.”.
- [`isTaut_of_isClosedImmersion_formalSpectrumMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTaut_of_isClosedImmersion_formalSpectrumMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L100) (StacksFrontier): “part (1), the conclusion that the homomorphism `φ : A → B` presenting a closed immersion is taut.”.
- [`exists_formalSpectrumMap_of_isClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_formalSpectrumMap_of_isClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionMcQuillanRefined.lean#L228) (StacksFrontier): “part (1), the conclusion that `f` corresponds to a continuous homomorphism `φ : A → B` of weakly admissible topological rings: a closed immersion `f` into `X = Spf(A)` whose source `Y` is a formal algebraic space is `Spf(φ)` for a weakly admissible `B` presenting `Y`, read through the identification of `Y` with `Spf(B)`. The three conclusions part (1) draws about `φ` are tagged on `AlgebraicGeometry.FormalSpace.isTaut_of_isClosedImmersion_formalSpectrumMap`, `AlgebraicGeometry.FormalSpace.isClosed_ker_toRingHom` and `AlgebraicGeometry.FormalSpace.denseRange_of_isClosedImmersion_formalSpectrumMap`, and that `Y` is McQuillan on `AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_of_isClosedImmersion`.”.
- [`isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteType.lean#L393) (StacksFrontier): “part (4), the conclusion that `B` is topologically of finite type over `A` for a finite type `f : Y → X` with `Y` McQuillan, and with it part (4)'s restatement that `f` factors as `Y → A^r_X → X` with the first arrow a closed immersion: the conclusion `TopologicalRing.IsTopologicallyOfFiniteType` produces the integer `r` together with a homomorphism `A[x_1, ..., x_r] → B` restricting to `φ` on constants and having dense image, which is that factorization and the dense image of its first arrow. Tautness of `φ`, part (4)'s other conclusion, is carried here as a hypothesis rather than deduced, as the clause of Stacks 0ANT on this declaration records. Part (4) closes by observing that questions (1) and (2) are then in force for `Y → A^r_X`; those are questions and are asserted nowhere.”.
- [`isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap'#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFiniteTypeRepresentable.lean#L239) (StacksFrontier): “part (4), both of its conclusions, for a finite type `f : Y → X` with `Y` McQuillan: the homomorphism `f` comes from is taut, and its target is topologically of finite type over its source -- `φ : A → B` in the source's letters, `φ : A ⟶ C` here, the formal spectrum of a weakly admissible topological ring being McQuillan by construction. With the second goes part (4)'s restatement that `f` factors as `Y → A^r_X → X` with the first arrow a closed immersion: the conclusion `TopologicalRing.IsTopologicallyOfFiniteType` produces the integer `r` together with a homomorphism `A[x_1, ..., x_r] → C` restricting to `φ` on constants and having dense image, which is that factorization and the dense image of its first arrow. Neither conclusion is carried as a hypothesis: tautness is deduced from finite type, by the implication (1) ⟹ (3) of Stacks 0AN5. Part (4) closes by observing that questions (1) and (2) are then in force for `Y → A^r_X`; those are questions and are asserted nowhere.”.
- [`isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautOfRepresentableByAlgebraicSpaces.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TautOfRepresentableByAlgebraicSpaces.lean#L87) (StacksFrontier): “part (4) in full. For a finite type `f : Y → X` with `Y` McQuillan, the homomorphism `φ : A → B` presenting `f` is taut and `B` is topologically of finite type over `A`, which are part (4)'s two conclusions; and with the second comes part (4)'s restatement that `f` factors as `Y → A^r_X → X` with the first arrow a closed immersion of McQuillan affine formal algebraic spaces, since `TopologicalRing.IsTopologicallyOfFiniteType` produces the integer `r` together with a homomorphism `A[x_1, ..., x_r] → B` restricting to `φ` on constants and having dense image, which is that factorization and the dense image of its first arrow. Part (4) closes by observing that questions (1) and (2) are then in force for `Y → A^r_X`; those are questions and are asserted nowhere.”.

## Tag 0AQI, a lemma

[Tag 0AQI](https://stacks.math.columbia.edu/tag/0AQI) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAffine_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean#L118). The attribute's comment: “that Y is a countably indexed affine formal algebraic space”.

> **Stacks 0AQI**, the first conclusion. The source of a closed immersion of fppf sheaves over
> `S` whose target is a countably indexed affine formal algebraic space is again a countably
> indexed affine formal algebraic space.

```lean
theorem isCountablyIndexedAffine_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (hX : IsCountablyIndexedAffine B S hS X) (f : Y ⟶ X)
    (hf : IsClosedImmersion B S hS f) :
    IsCountablyIndexedAffine B S hS Y
```

**`AlgebraicGeometry.FormalSpace.exists_spfPresentation_continuousHom_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean#L151). The attribute's comment: “that f corresponds to a morphism of WAdm^count”.

> **Stacks 0AQI**, the correspondence part of the second conclusion. A closed immersion
> `f : Y ⟶ X` of fppf sheaves over `S` whose target is a countably indexed affine formal
> algebraic space is, after identifying `X` with `Spf A` and `Y` with `Spf C` for objects `A` and
> `C` of `WAdm^count`, the formal spectrum of a continuous homomorphism `A ⟶ C` over `S`, itself
> again a closed immersion.

```lean
theorem exists_spfPresentation_continuousHom_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (hX : IsCountablyIndexedAffine B S hS X) (f : Y ⟶ X)
    (hf : IsClosedImmersion B S hS f) :
    ∃ (P : SpfPresentation B S hS X) (Q : SpfPresentation B S hS Y)
      (hA : TopologicalRing.IsWeaklyAdmissible P.ring),
      (nhds (0 : P.ring)).IsCountablyGenerated ∧
      TopologicalRing.IsWeaklyAdmissible Q.ring ∧
      (nhds (0 : Q.ring)).IsCountablyGenerated ∧
      ∃ (eX : X ≅ formalSpectrum P.system) (eY : Y ≅ formalSpectrum Q.system)
        (g : ContinuousHom P.system Q.system),
        IsClosedImmersion B S hS (formalSpectrumMap hA g) ∧
          f = eY.hom ≫ formalSpectrumMap hA g ≫ eX.inv
```

**`AlgebraicGeometry.FormalSpace.isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean#L196). The attribute's comment: “the quotient by a closed ideal, given the tautness of Stacks 0AN5”.

> **Stacks 0AQI**, the quotient part of the second conclusion. Let `A` be an object of
> `WAdm^count`, that is, a weakly admissible topological ring over `S` with a countable
> fundamental system of neighbourhoods of `0`, let `C` be weakly admissible, and let
> `g : A ⟶ C` be a continuous homomorphism over `S` whose formal spectrum is a closed immersion.
> If `g` is taut, then `K = ker g` is a closed ideal of `A` and `g` identifies `A/K` with `C`
> topologically, so the closed immersion is `Spf` of `A ⟶ A/K`.
>
> Tautness is the one hypothesis not proved here: it is the implication (1) ⟹ (3) of
> **Stacks 0AN5**, which this library does not carry. Everything else is proved.

```lean
theorem isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hC : TopologicalRing.IsWeaklyAdmissible C)
    (hcount : (nhds (0 : A)).IsCountablyGenerated)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C} (g : ContinuousHom D E)
    (hg : IsClosedImmersion B S hS (formalSpectrumMap hA g))
    (htaut : RingHom.IsTaut g.toRingHom) :
    IsClosed (RingHom.ker g.toRingHom : Set A) ∧
      ∃ e : (A ⧸ RingHom.ker g.toRingHom) ≃+* C,
        (∀ a : A, e (Ideal.Quotient.mk (RingHom.ker g.toRingHom) a) = g.toRingHom a) ∧
          IsHomeomorph e
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAffine_and_exists_closedIdealQuotient_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexed.lean#L235). The attribute's comment: “given the tautness of Stacks 0AN5”.

> **Stacks 0AQI** in full, given the implication (1) ⟹ (3) of **Stacks 0AN5** as the
> hypothesis `hAN5`. Let `X` be a countably indexed affine formal algebraic space over `S` and
> let `f : Y ⟶ X` be a closed immersion of fppf sheaves over `S`. Then `Y` is a countably indexed
> affine formal algebraic space, and `f` is `Spf` of a continuous homomorphism `g : A ⟶ C` of
> objects of `WAdm^count` whose kernel `K` is a closed ideal of `A` and which identifies `A/K`
> with `C` topologically; that is, `f` corresponds to `A ⟶ A/K`.
>
> The hypothesis `hAN5` is exactly the implication of Stacks 0AN5 that a continuous homomorphism
> of weakly admissible topological rings over `S` whose formal spectrum is a closed immersion —
> hence representable by algebraic spaces — is taut. It is the one input this library does not
> carry; the unconditional halves of the lemma are
> `AlgebraicGeometry.FormalSpace.isCountablyIndexedAffine_of_isClosedImmersion` and
> `AlgebraicGeometry.FormalSpace.exists_spfPresentation_continuousHom_of_isClosedImmersion`.

```lean
theorem isCountablyIndexedAffine_and_exists_closedIdealQuotient_of_isClosedImmersion
    (hAN5 : ∀ {A C : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
      [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
      [IsLinearTopology C C] (hA : TopologicalRing.IsWeaklyAdmissible A)
      (_hC : TopologicalRing.IsWeaklyAdmissible C)
      {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C} (g : ContinuousHom D E),
      IsClosedImmersion B S hS (formalSpectrumMap hA g) → RingHom.IsTaut g.toRingHom)
    {X Y : FppfSheaf B S hS} (hX : IsCountablyIndexedAffine B S hS X) (f : Y ⟶ X)
    (hf : IsClosedImmersion B S hS f) :
    IsCountablyIndexedAffine B S hS Y ∧
      ∃ (P : SpfPresentation B S hS X) (Q : SpfPresentation B S hS Y)
        (hA : TopologicalRing.IsWeaklyAdmissible P.ring),
        (nhds (0 : P.ring)).IsCountablyGenerated ∧
        TopologicalRing.IsWeaklyAdmissible Q.ring ∧
        ∃ (eX : X ≅ formalSpectrum P.system) (eY : Y ≅ formalSpectrum Q.system)
          (g : ContinuousHom P.system Q.system),
          IsClosed (RingHom.ker g.toRingHom : Set P.ring) ∧
          (∃ e : (P.ring ⧸ RingHom.ker g.toRingHom) ≃+* Q.ring,
            (∀ a : P.ring,
              e (Ideal.Quotient.mk (RingHom.ker g.toRingHom) a) = g.toRingHom a) ∧
            IsHomeomorph e) ∧
          f = eY.hom ≫ formalSpectrumMap hA g ≫ eX.inv
```

**`AlgebraicGeometry.FormalSpace.IsClosedImmersion.isCountablyIndexedAffine_and_exists_closedIdealQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexedQuotient.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexedQuotient.lean#L44).

> Let `X` be a countably indexed affine formal algebraic space over `S` and let `f : Y ⟶ X` be a
> closed immersion of fppf sheaves over `S`. Then `Y` is a countably indexed affine formal algebraic
> space, and `f` is `Spf` of a continuous homomorphism `g : A ⟶ C` of objects of `WAdm^count` whose
> kernel `K` is a closed ideal of `A` and which identifies `A/K` with `C` topologically; that is, `f`
> corresponds to `A ⟶ A/K`.

```lean
theorem IsClosedImmersion.isCountablyIndexedAffine_and_exists_closedIdealQuotient
    {X Y : FppfSheaf B S hS} (hX : IsCountablyIndexedAffine B S hS X) (f : Y ⟶ X)
    (hf : IsClosedImmersion B S hS f) :
    IsCountablyIndexedAffine B S hS Y ∧
      ∃ (P : SpfPresentation B S hS X) (Q : SpfPresentation B S hS Y)
        (hA : TopologicalRing.IsWeaklyAdmissible P.ring),
        (nhds (0 : P.ring)).IsCountablyGenerated ∧
        TopologicalRing.IsWeaklyAdmissible Q.ring ∧
        ∃ (eX : X ≅ formalSpectrum P.system) (eY : Y ≅ formalSpectrum Q.system)
          (g : ContinuousHom P.system Q.system),
          IsClosed (RingHom.ker g.toRingHom : Set P.ring) ∧
          (∃ e : (P.ring ⧸ RingHom.ker g.toRingHom) ≃+* Q.ring,
            (∀ a : P.ring,
              e (Ideal.Quotient.mk (RingHom.ker g.toRingHom) a) = g.toRingHom a) ∧
            IsHomeomorph e) ∧
          f = eY.hom ≫ formalSpectrumMap hA g ≫ eX.inv
```

**`AlgebraicGeometry.FormalSpace.isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexedRefined.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCountablyIndexedRefined.lean#L62). The attribute's comment: “the quotient by a closed ideal”.

> Let `A` be an object of `WAdm^count`, that is, a weakly admissible topological ring over `S`
> with a countable fundamental system of neighbourhoods of `0`, let `C` be weakly admissible, and let
> `g : A ⟶ C` be a continuous homomorphism over `S` whose formal spectrum is a closed immersion.
> Then `K = ker g` is a closed ideal of `A` and `g` identifies `A/K` with `C` topologically, so the
> closed immersion is `Spf` of `A ⟶ A/K`.

```lean
theorem isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion'
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hC : TopologicalRing.IsWeaklyAdmissible C)
    (hcount : (nhds (0 : A)).IsCountablyGenerated)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C} (g : ContinuousHom D E)
    (hg : IsClosedImmersion B S hS (formalSpectrumMap hA g)) :
    IsClosed (RingHom.ker g.toRingHom : Set A) ∧
      ∃ e : (A ⧸ RingHom.ker g.toRingHom) ≃+* C,
        (∀ a : A, e (Ideal.Quotient.mk (RingHom.ker g.toRingHom) a) = g.toRingHom a) ∧
          IsHomeomorph e
```

**`AlgebraicGeometry.FormalSpace.hasSurjectiveOnPullbackCharts_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionCharts.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionCharts.lean#L675). The attribute's comment: “the surjectivity clause alone, on the pullback charts of a closed immersion, carrying nothing: the chart map is a closed immersion by Stacks 0GHX, conjugation by the presenting isomorphisms of the two charts preserves that, the implication (1) implies (3) of Stacks 0AN5 makes the chart homomorphism taut -- its two HasLargeSite conditions being free on chart rings, which are adic and carry quotient systems, by mk_lt_cutoff_of_quotientSystem_of_isAdic and hasLargeSite_of_mk_lt_cutoff -- and the quotient part of Stacks 0AQI, isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion, turns the tautness into the presentation of the chart ring as a quotient. The adic and topologically finite type clauses of Stacks 0AQI are not asserted”.

> **The chart homomorphisms of a closed immersion are surjective**, carrying nothing beyond
> the closed immersion itself. This is the surjectivity clause of **Stacks 0AQI** on the pullback
> charts of `f`.
>
> The chart map `t : U ⟶ V` is a closed immersion because closed immersions are stable under base
> change (**Stacks 0GHX**, `AlgebraicGeometry.FormalSpace.isClosedImmersion_of_isPullback`), and
> conjugating it by the presenting isomorphisms of the two charts leaves a closed immersion, an
> isomorphism square being cartesian; so `Spf g` is a closed immersion. Its representability is
> the first component of the closed-immersion predicate of Stacks 0ANP, so the implication
> (1) ⟹ (3) of **Stacks 0AN5**,
> `AlgebraicGeometry.FormalSpace.isTaut_of_isRepresentableByAlgebraicSpacesULift_formalSpectrumMap`,
> makes `g` taut. That implication carries the two set-theoretic conditions
> `AlgebraicGeometry.FormalSpace.QuotientSystem.HasLargeSite`, and both are free here: the chart
> rings are Noetherian with adic topologies carrying quotient systems, so
> `AlgebraicGeometry.FormalSpace.mk_lt_cutoff_of_quotientSystem_of_isAdic` bounds each by the
> cutoff of the site and
> `AlgebraicGeometry.FormalSpace.hasLargeSite_of_mk_lt_cutoff` supplies the condition. This is why
> the surjectivity clause of Stacks 0AQI is not a missing input: it is blocked on nothing.
>
> The passage from tautness to the presentation of the chart ring as a quotient is then the
> quotient part of Stacks 0AQI,
> `AlgebraicGeometry.FormalSpace.isClosed_ker_and_quotientKerEquiv_of_isClosedImmersion`, whose
> remaining inputs are free as well: the source is adic, so the powers of an ideal of definition
> are a countable fundamental system of neighbourhoods of zero, and the target is weakly
> admissible by `TopologicalRing.isWeaklyAdmissible_of_isAdic` applied to the ideal of definition
> for which it is adically complete. Surjectivity is read off the resulting ring equivalence
> `A ⧸ ker g ≃+* C`, which agrees with `g` on representatives.

```lean
theorem hasSurjectiveOnPullbackCharts_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f) :
    HasSurjectiveOnPullbackCharts B S hS f
```

## Tag 0ANU, a lemma

[Tag 0ANU](https://stacks.math.columbia.edu/tag/0ANU) in the Stacks Project.

**`TopologicalRing.finiteType_tfae'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/Equivalences.lean, line 684](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/Equivalences.lean#L684). The attribute's comment: “equivalent_conditions”.

> The four finite-type conditions for a morphism of countably indexed weakly admissible rings
> are equivalent.
>
> Stacks 0ANU states this for an arrow of `WAdm^count`, both rings weakly admissible with a
> countable fundamental system of neighbourhoods of zero. Countable generation is assumed here
> of the source only, which is strictly weaker and so covers every arrow of `WAdm^count`. The
> hypothesis is spent twice and both times on the source: on condition (b), the cofinal form, by
> `finiteTypeModuloEveryWeakIdeal_to_cofinal`, and on condition (d), the restricted power series
> presentation, by `restrictedPowerSeriesPresentation_of_taut_dense`. Condition (c) costs no
> countability at all — it is condition (2) of Stacks 0ANT verbatim, and
> `isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal` gets it from condition (a) for
> any weakly pre-admissible source.

```lean
public theorem finiteType_tfae' (φ : B →+* A) (hφ : Continuous φ)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hBcount : (nhds (0 : B)).IsCountablyGenerated) :
    List.TFAE [
      FiniteTypeModuloEveryWeakIdeal φ,
      FiniteTypeModuloCofinalWeakIdeals φ,
      RingHom.IsTaut φ ∧ TopologicalRing.IsTopologicallyOfFiniteType φ,
      HasRestrictedPowerSeriesPresentation φ]
```

**`TopologicalRing.topologicallyFiniteType_localizationPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean#L329). The attribute's comment: “local_property”.

> Tautness together with topological finite type ascends along a completed étale localization
> diagram of countably indexed weakly admissible rings.

```lean
public theorem topologicallyFiniteType_localizationPreserves :
    LocalizationPreserves.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
```

**`TopologicalRing.topologicallyFiniteType_faithfullyFlatDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean#L345). The attribute's comment: “local_property”.

> Tautness together with topological finite type descends along a completed étale localization
> diagram whose upper horizontal ring map is faithfully flat.

```lean
public theorem topologicallyFiniteType_faithfullyFlatDescent :
    FaithfullyFlatDescent.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
```

**`TopologicalRing.topologicallyFiniteType_finiteProductPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean#L426). The attribute's comment: “local_property”.

> Tautness together with topological finite type is preserved by finite products of
> targets.

```lean
public theorem topologicallyFiniteType_finiteProductPreserves :
    FiniteProductPreserves.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
```

**`TopologicalRing.topologicallyFiniteType_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocal.lean#L439). The attribute's comment: “local_property”.

> Tautness together with topological finite type is a local property of morphisms of
> countably indexed weakly admissible topological rings.

```lean
public theorem topologicallyFiniteType_propertyIsLocal :
    PropertyIsLocal.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
```

**`TopologicalRing.topologicallyFiniteType_isomorphismInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocalRefined.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocalRefined.lean#L146). The attribute's comment: “local_property”.

> Tautness together with topological finite type is independent of the presentations of the
> source and the target.

```lean
public theorem topologicallyFiniteType_isomorphismInvariant :
    IsomorphismInvariant.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
      IsCountablyWeaklyAdmissible
```

**`TopologicalRing.topologicallyFiniteType_propertyIsLocal'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocalRefined.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeIsLocalRefined.lean#L166). The attribute's comment: “local_property”.

> Tautness together with topological finite type is a local property of morphisms of countably
> indexed weakly admissible topological rings.

```lean
public theorem topologicallyFiniteType_propertyIsLocal' :
    PropertyIsLocal'.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f ∧ IsTopologicallyOfFiniteType f)
```

## Tag 0CB6, a lemma

[Tag 0CB6](https://stacks.math.columbia.edu/tag/0CB6) in the Stacks Project.

**`TopologicalRing.finiteTypeModuloEveryWeakIdeal_iff_exists_idealOfDefinition`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/IdealOfDefinition.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteType/IdealOfDefinition.lean#L46).

> For a pre-admissible source, finite type modulo every weak ideal of definition is equivalent
> to finite type modulo some ideal of definition, with tautness in both conditions.

```lean
public lemma finiteTypeModuloEveryWeakIdeal_iff_exists_idealOfDefinition
    {B A : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A]
    (φ : B →+* A) (hB : TopologicalRing.IsPreAdmissible B) :
    TopologicalRing.FiniteTypeModuloEveryWeakIdeal φ ↔
      (RingHom.IsTaut φ ∧
        ∃ J : Ideal B, TopologicalRing.IsIdealOfDefinition J ∧
          (Ideal.quotientMap (I := J) (Ideal.closure (J.map φ)) φ
            (Ideal.map_le_iff_le_comap.mp subset_closure)).FiniteType)
```

## Tag 0ANV, a lemma

[Tag 0ANV](https://stacks.math.columbia.edu/tag/0ANV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_tfae_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationAffine.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationAffine.lean#L115). The attribute's comment: “the equivalence at the source's hypotheses: `f` an arbitrary morphism of affine formal algebraic spaces with countably indexed target. Countable indexing of the source is derived from condition (1) by Stacks 0AKN and Stacks 0AKP, the presentations as formal spectra by Stacks 0AN1 and the presenting homomorphism by Stacks 0AN0. Condition (3) is the existence of such presentations of `X` and `Y` by rings of `WAdm^count` and of a continuous homomorphism with formal spectrum map `f` satisfying the conditions of Stacks 0ANU, in the forms (a) and (c)”.

> **Stacks 0ANV.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> with `Y` countably indexed. Then `f` being locally of finite type, `f` being of finite type in
> the sense of Definition 0AM4, part (2), and `f` corresponding to a morphism `B → A` of
> `WAdm^{count}` satisfying the equivalent conditions of Stacks 0ANU — taken in the two forms
> (a), of finite type modulo every weak ideal of definition, and (c), taut and topologically of
> finite type — are all equivalent.
>
> As in the source, the source `X` is not assumed countably indexed. If `f` is locally of finite
> type it is representable by algebraic spaces, hence affine by **Stacks 0AKN**, and `X` is then
> countably indexed by **Stacks 0AKP**; the two steps together are clause (1) of Stacks 0AKQ,
> `AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isRepresentable'`. Both spaces are then
> formal spectra of rings of `WAdm^{count}` by **Stacks 0AN1**,
> `AlgebraicGeometry.FormalSpace.exists_quotientSystem_of_isCountablyIndexed`, and `f` is the
> formal spectrum map of a continuous homomorphism by **Stacks 0AN0**,
> `AlgebraicGeometry.FormalSpace.existsUnique_continuousHom_formalSpectrumMap_eq`. The equivalence
> for that homomorphism is **Stacks 0ANT** together with Stacks 0ANU, in the form
> `AlgebraicGeometry.FormalSpace.formalSpectrumMap_finiteType_tfae_countablyWeaklyAdmissible`.
> Being locally of finite type upgrades to being of finite type by Stacks 0AKN,
> `AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.isFiniteType_of_isAffineFormal`, and
> Stacks 0AJJ.

```lean
theorem isLocallyOfFiniteType_tfae_of_isAffineFormalAlgebraicSpace {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) (hYc : IsCountablyIndexed B S hS Y) :
    List.TFAE
      [IsLocallyOfFiniteType B S hS f,
        IsFiniteType' B S hS f,
        CorrespondsToCountablyWeaklyAdmissibleMap B S hS
          (fun φ ↦ TopologicalRing.FiniteTypeModuloEveryWeakIdeal φ) f,
        CorrespondsToCountablyWeaklyAdmissibleMap B S hS
          TopologicalRing.IsTautTopologicallyOfFiniteTypeHom f]
```

**`AlgebraicGeometry.FormalSpace.chartPropertyIsLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationRefined.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationRefined.lean#L129). The attribute's comment: “the equivalence, read on countably indexed affine charts rather than on formal spectra: a map of countably indexed affine formal algebraic spaces over `S` is locally of finite type exactly when every morphism of `WAdm^{count}` presenting it is taut and topologically of finite type”.

> A map of countably indexed affine formal algebraic spaces over `S` is locally of finite
> type exactly when every morphism of `WAdm^{count}` presenting it is taut and topologically of
> finite type.
>
> A countably indexed affine formal algebraic space is the formal spectrum of a weakly admissible
> topological ring with a countable fundamental system of neighbourhoods of zero — item (6) of
> Stacks 0AIK — and a map of formal spectra comes from a unique continuous homomorphism by Stacks
> 0AN0, so the chart condition is never vacuous here and both directions are the corresponding
> implications of Stacks 0ANV for that homomorphism. The implication out of being locally of
> finite type is Stacks 0AN5 (1) ⟹ (3) for tautness together with the implication (1) ⟹ (2) of
> Stacks 0ANT, the two being combined in
> `isTaut_and_isTopologicallyOfFiniteType_of_isFiniteType_formalSpectrumMap` once Stacks 0AKN has
> upgraded locally of finite type to of finite type; the implication back is the implication
> (2) ⟹ (1) of Stacks 0ANT, `isFiniteType_formalSpectrumMap_of_isTaut`. Being locally of finite
> type is carried across the two comparison isomorphisms by Stacks 0AQ4, an isomorphism being
> representable étale.

```lean
theorem chartPropertyIsLocallyOfFiniteType :
    ChartPropertyIsLocallyOfFiniteType B S hS
```

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap_finiteType_tfae_countablyWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationVariants.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationVariants.lean#L107). The attribute's comment: “the equivalence, under the source's hypotheses exactly: only the target `Spf A` is assumed countably indexed, by `hAcount`. Condition (3) is taken in the two forms (a) and (c) of Stacks 0ANU, each conjoined with membership of the source ring in `WAdm^count`, which is what `f corresponds to a morphism of WAdm^count` still asserts once the target ring's membership is the standing hypothesis. That membership is a conclusion of conditions (1) and (2) rather than an assumption: every one of the four conditions supplies tautness, and a taut continuous homomorphism carries a countable fundamental system of open ideals from source ring to target ring by Stacks 0GX6, `RingHom.isCountablyGenerated_nhds_zero_of_isTaut` — which replaces the source's appeal to Stacks 0AKN and Stacks 0AKP and, like the library's Stacks 0AKN, needs no affineness of the two formal spectra. The finite type condition is Definition 0AM4, part (2), verbatim; the implication (2) ⟹ (1) of Stacks 0ANT concludes it through condition (2) of Stacks 0AJJ — representable by algebraic spaces plus of finite type in the Bootstrap sense of Stacks 03XZ — which Stacks 0AJJ, `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`, identifies with Definition 0AM4, part (2), unconditionally. The two forms of condition (3) are identified with no countability assumption, by `TopologicalRing.isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal` and `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType`, so Stacks 0ANU's own countability hypotheses are not needed here; the implication (1) ⟹ (3) of Stacks 0AN5 that supplies tautness, `AlgebraicGeometry.FormalSpace.isTaut_of_isRepresentableByAlgebraicSpaces_formalSpectrumMap`, carries no side condition either”.

> **Stacks 0ANV.** Let `φ : A ⟶ C` be a continuous homomorphism of weakly admissible
> topological rings over `S` and assume the neighbourhood filter of zero of `A` — the target
> `Spf A` — countably generated. Then `Spf (φ) : Spf C → Spf A` being locally of finite type,
> `Spf (φ)` being of finite type in the sense of Definition 0AM4, part (2), `φ` being a
> morphism of `WAdm^{count}` of finite type modulo every weak ideal of definition, and `φ`
> being a morphism of `WAdm^{count}` which is taut and topologically of finite type are all
> equivalent.
>
> Only the target is assumed countably indexed, as in the source. That the source `Spf C` is
> countably indexed is part of what condition (3) asserts — membership of `φ` in
> `WAdm^{count}` — and so is a conclusion of conditions (1) and (2), not a hypothesis; the
> target's own membership is the standing hypothesis `hAcount` together with `hA`. The step
> that produces it is Stacks 0GX6,
> `RingHom.isCountablyGenerated_nhds_zero_of_isTaut`: a taut continuous homomorphism carries a
> countable fundamental system of open ideals from source ring to target ring, and every one of
> the four conditions supplies tautness. This replaces the appeal to Stacks 0AKN and Stacks
> 0AKP that the source makes, and like them it needs no affineness of the two formal spectra.
>
> The last two conditions are conditions (a) and (c) of Stacks 0ANU, each conjoined with
> membership in `WAdm^{count}`. They are identified here without any countability assumption,
> by `TopologicalRing.isTopologicallyOfFiniteType_of_finiteTypeModuloEveryWeakIdeal` — for
> which weak pre-admissibility of `A` suffices — and
> `TopologicalRing.finiteTypeModuloEveryWeakIdeal_of_topologicallyOfFiniteType`, so Stacks
> 0ANU's own countability hypotheses are not needed. With `hAcount` and the `WAdm^{count}`
> conjunct in hand, Stacks 0ANU identifies these two with its remaining conditions (b) and (d)
> as well, which is why reading condition (3) off either form is faithful.
>
> The implication from locally of finite type to condition (a) splits into tautness, which is
> the implication (1) ⟹ (3) of Stacks 0AN5, and finite type of the stage quotient maps, which
> is the ring-theoretic half of Stacks 0ANT; the implication from condition (a) back is the
> implication (2) ⟹ (1) of Stacks 0ANT, and being locally of finite type is the first half of
> the conjunction that being of finite type is.
>
> The quasi-compactness of Definition 0AJC that the second condition contains is not
> established directly anywhere in the cycle: the implication (2) ⟹ (1) of Stacks 0ANT
> produces condition (2) of Stacks 0AJJ,
> `AlgebraicGeometry.FormalSpace.IsBootstrapFiniteType`, whose quasi-compactness assertion is
> the Bootstrap one, and Stacks 0AJJ identifies that condition with Definition 0AM4, part (2),
> unconditionally; see
> `AlgebraicGeometry.FormalSpace.isFiniteType_iff_isBootstrapFiniteType`.
>
> Nothing beyond the source's hypotheses is assumed. The tautness step is the implication
> (1) ⟹ (3) of Stacks 0AN5,
> `AlgebraicGeometry.FormalSpace.isTaut_of_isRepresentableByAlgebraicSpaces_formalSpectrumMap`,
> which carries no side condition of its own.

```lean
theorem formalSpectrumMap_finiteType_tfae_countablyWeaklyAdmissible {A C : Type u} [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A] [CommRing C]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (hAcount : (nhds (0 : A)).IsCountablyGenerated)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C) (g : ContinuousHom D E) :
    List.TFAE
      [IsLocallyOfFiniteType B S hS (formalSpectrumMap hA g),
        IsFiniteType' B S hS (formalSpectrumMap hA g),
        TopologicalRing.IsCountablyWeaklyAdmissible C ∧
          TopologicalRing.FiniteTypeModuloEveryWeakIdeal g.toRingHom,
        TopologicalRing.IsCountablyWeaklyAdmissible C ∧
          RingHom.IsTaut g.toRingHom ∧
            TopologicalRing.IsTopologicallyOfFiniteType g.toRingHom]
```

## Tag 0ANW, a lemma

[Tag 0ANW](https://stacks.math.columbia.edu/tag/0ANW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_tfae'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationRefined.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteTypeCharacterizationRefined.lean#L199). The attribute's comment: “the equivalence of its four conditions, at the source's own hypotheses. The presented refinement of a covering of the source is the library's `hasEtaleRefinementOfSourceCover_isCountablyWeaklyAdmissible` (Stacks 0AJ2, quasi-compactness of an affine formal algebraic space and Stacks 0AN8) and the implication (2) ⟹ (1) of Stacks 0AKX is the library's `isCountablyIndexed_of_isRepresentableEtale_of_isLocallyCountablyIndexed`”.

> For a morphism `f : X ⟶ Y` of locally countably indexed formal algebraic spaces over `S`,
> the condition that every affine representable étale square over `f` carry a taut, topologically
> of finite type morphism of `WAdm^{count}`, the existence of an affine étale covering of `Y`
> together with affine étale coverings of the fibre products of its members with `X` on which
> that condition holds, the existence of an affine étale covering of `X` whose members factor
> through affine representable étale charts of `Y` by such morphisms, and `f` being locally of
> finite type, are all equivalent.
>
> The first three are the three conditions of Stacks 0ANG for the class of countably indexed
> weakly admissible topological rings and the property of being taut and topologically of finite
> type, which Stacks 0ANU makes a local property of such arrows; the comparison with the fourth is
> Stacks 0ANV on charts together with the implications (1) ⟹ (3) and (4) ⟹ (5) ⟹ (1) of Stacks
> 0ANL.

```lean
theorem isLocallyOfFiniteType_tfae' {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y) :
    List.TFAE
      [HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.IsTautTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterTargetCover B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.IsTautTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterSourceCover B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible
          TopologicalRing.IsTautTopologicallyOfFiniteTypeHom f,
        IsLocallyOfFiniteType B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.29, Tag 0ALL](https://stacks.math.columbia.edu/tag/0ALL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
