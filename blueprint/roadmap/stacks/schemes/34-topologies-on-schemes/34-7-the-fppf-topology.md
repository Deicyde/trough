---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.fppfPrecoverage, AlgebraicGeometry.coveringPrecoverage_le_of_isFiner, AlgebraicGeometry.Scheme.smoothPrecoverage_le_fppfPrecoverage, AlgebraicGeometry.Scheme.etalePrecoverage_le_fppfPrecoverage, AlgebraicGeometry.Scheme.syntomicPrecoverage_le_fppfPrecoverage, Scheme.zariskiPrecoverage_le_fppfPrecoverage, AlgebraicGeometry.Scheme.Hom.singleton_mem_fppfPrecoverage, AlgebraicGeometry.Scheme.instIsStableUnderCompositionFppfPrecoverage
statement: formalized
proof: formalized
---

# 34.7 The fppf topology

Section 34.7 of the Stacks Project, [Tag 021L](https://stacks.math.columbia.edu/tag/021L). 13 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 021M, a definition

[Tag 021M](https://stacks.math.columbia.edu/tag/021M) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.fppfPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.fppfPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L23) (StacksFrontier). References: SGA 4 IV (8.5.5); SGA 4 XVII (0.10), “partial”; SGA 7 VIII (0.2), “partial”.

## Tag 021N, a lemma

[Tag 021N](https://stacks.math.columbia.edu/tag/021N) in the Stacks Project.

**`AlgebraicGeometry.coveringPrecoverage_le_of_isFiner`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L119). The attribute's comment: “the five precoverages of schemes are nested along the chain of topologies”. References: SGA 3 IV (6.6), “Diagram 6.6.1”.

> **Stacks 021N and its companions.**  Along the chain, the precoverages of jointly surjective
> families of schemes are nested: an open immersion is étale, an étale morphism is smooth, a smooth
> morphism is syntomic, and a syntomic morphism is flat and locally of finite presentation.

```lean
public theorem coveringPrecoverage_le_of_isFiner (h : τ.IsFiner τ') :
    Scheme.precoverage (coveringMorphismProperty τ') ≤
      Scheme.precoverage (coveringMorphismProperty τ)
```

**`AlgebraicGeometry.Scheme.smoothPrecoverage_le_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean#L45). The attribute's comment: “smooth coverings”.

> **Stacks 021N.** Every smooth covering family is an fppf covering family.

```lean
public theorem smoothPrecoverage_le_fppfPrecoverage :
    Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}) ≤
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.Scheme.etalePrecoverage_le_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean#L54). The attribute's comment: “étale coverings”.

> **Stacks 021N.** Every étale covering family is an fppf covering family.

```lean
public theorem etalePrecoverage_le_fppfPrecoverage :
    Scheme.etalePrecoverage ≤ Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.Scheme.syntomicPrecoverage_le_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L78). The attribute's comment: “syntomic coverings”.

> **Stacks 021N.** Every syntomic covering family is an fppf covering family: a syntomic
> morphism is flat by Stacks 01UL and locally of finite presentation by Stacks 01UK.

```lean
public theorem syntomicPrecoverage_le_fppfPrecoverage :
    Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}) ≤ Scheme.fppfPrecoverage
```

Declarations registered for the tag:

- [`Scheme.zariskiPrecoverage_le_fppfPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.zariskiPrecoverage_le_fppfPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Coverings.lean#L60) (StacksFrontier): “Zariski coverings”.

## Tag 021O, a lemma

[Tag 021O](https://stacks.math.columbia.edu/tag/021O) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.singleton_mem_fppfPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.singleton_mem_fppfPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L24) (StacksFrontier): “(1) isomorphisms”. References: SGA 3 IV (6.3.2), “partial”; SGA 3 VIIA (8.1.4), “Converse clause”; SGA 3 VIA (3.3.3), “more general”; SGA 3 VIB (10.8).
- [`AlgebraicGeometry.Scheme.instIsStableUnderCompositionFppfPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsStableUnderCompositionFppfPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L25) (StacksFrontier): “(2) composition”.
- [`AlgebraicGeometry.Scheme.instIsStableUnderBaseChangeFppfPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsStableUnderBaseChangeFppfPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L27) (StacksFrontier): “(3) base change”. References: EGA IV (20.6.9), “special case”.

## Tag 021P, a lemma

[Tag 021P](https://stacks.math.columbia.edu/tag/021P) in the Stacks Project.

**`AlgebraicGeometry.exists_standardFppf_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean#L51). The attribute's comment: “the finite affine refinement; the tag's further assertion that each member may be chosen open affine inside one of the given members is not claimed”.

> Every covering sieve of an affine object of a big fppf site is refined by a chosen covering
> family which is a standard fppf covering, that is, by a finite family of flat morphisms of finite
> presentation, jointly surjective, whose sources are affine over the affine target.

```lean
theorem exists_standardFppf_refinement
    (B : AlgebraicGeometry.BigFppfSite.{u})
    {T : B.Schemes} [IsAffine (B.inclusion.obj T)] {R : Sieve T}
    (hR : R ∈ B.topology T) :
    ∃ Q : PreZeroHypercover T,
      B.IsCovering ⟨T, Q⟩ ∧
      AlgebraicGeometry.IsStandardFppfCovering
        (fun i ↦ B.inclusion.obj (Q.X i)) (fun i ↦ B.inclusion.map (Q.f i)) ∧
      Q.presieve₀ ≤ R
```

## Tag 021Q, a definition

[Tag 021Q](https://stacks.math.columbia.edu/tag/021Q) in the Stacks Project.

**`AlgebraicGeometry.IsStandardFppfCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L78).

> A family `fᵢ : Uᵢ ⟶ T` is a **standard fppf covering** if it is finite, its
> source and target schemes are affine, every `fᵢ` is flat and of finite presentation,
> and the images of the `fᵢ` cover `T`.

```lean
public structure IsStandardFppfCovering {T : Scheme.{u}} {I : Type v}
    (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 021R, a definition

[Tag 021R](https://stacks.math.columbia.edu/tag/021R) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L110).

> A big fppf site, retaining all choices in the construction: the initial set of schemes
> and coverings, the size cutoff defining its underlying full subcategory, and the bounded family
> of fppf coverings of Stacks 000X.

```lean
structure BigFppfSite
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SchemeBelow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L220) (StacksFrontier).
- [`AlgebraicGeometry.schemeBelowInclusion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L221) (StacksFrontier).

## Tag 03WX, a lemma

[Tag 03WX](https://stacks.math.columbia.edu/tag/03WX) in the Stacks Project.

**`AlgebraicGeometry.exists_isCovering_tautologicallyEquivalent_standardFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean#L148). The attribute's comment: “standard_equivalence”.

> A standard fppf covering of an object of a big fppf site is tautologically equivalent to a
> covering belonging to that site.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_standardFppfCovering
    (B : AlgebraicGeometry.BigFppfSite.{u}) (T : B.Schemes)
    (U : PreZeroHypercover.{w} (B.inclusion.obj T))
    (hU : U.presieve₀ ∈ Scheme.fppfPrecoverage (B.inclusion.obj T))
    (hstandard : AlgebraicGeometry.IsStandardFppfCovering U.X U.f) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U (V.map B.inclusion)
```

**`AlgebraicGeometry.exists_isCovering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean#L167). The attribute's comment: “zariski_equivalence”.

> A Zariski covering of an object of a big fppf site is tautologically equivalent to a
> covering belonging to that site.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_openCover
    (B : AlgebraicGeometry.BigFppfSite.{u}) (T : B.Schemes)
    (U : (B.inclusion.obj T).OpenCover.{w}) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.toPreZeroHypercover
          (V.map B.inclusion)
```

**`AlgebraicGeometry.exists_isCovering_refining_fppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/StandardCoverings.lean#L194). The attribute's comment: “site_refinement”.

> An arbitrary fppf covering of an object of a big fppf site is refined by a covering
> belonging to that site.

```lean
public theorem exists_isCovering_refining_fppfCovering
    (B : AlgebraicGeometry.BigFppfSite.{u}) (T : B.Schemes)
    (E : PreZeroHypercover.{w} (B.inclusion.obj T))
    (hE : E.presieve₀ ∈ Scheme.fppfPrecoverage (B.inclusion.obj T)) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧ Nonempty ((V.map B.inclusion).Hom E)
```

## Tag 021S, a definition

[Tag 021S](https://stacks.math.columbia.edu/tag/021S) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L232). The attribute's comment: “part (1), category”. References: SGA 4 XVII (0.10), “big fppf site”.

> The big fppf category over `S`: the slice of the chosen big fppf category over its
> object `S`.

```lean
public abbrev BigFppfOver
```

**`AlgebraicGeometry.BigFppfOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L247). The attribute's comment: “part (1), coverings”.

> A family in the slice covers when its underlying family covers in the chosen big fppf
> site.

```lean
public abbrev IsCovering (E : Covering (BigFppfOver B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineFppf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L270). The attribute's comment: “part (2), category”.

> The big affine fppf category over `S`: the full subcategory of the big fppf category over
> `S` on objects with affine underlying scheme.

```lean
public abbrev BigAffineFppf
```

**`AlgebraicGeometry.BigAffineFppf.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf.lean#L296). The attribute's comment: “part (2), coverings”.

> A family in the big affine category covers exactly when it is a covering of the big fppf
> site over `S` and is standard fppf.

```lean
public abbrev IsCovering (E : Covering (BigAffineFppf B S hS)) : Prop
```

## Tag 021T, a lemma

[Tag 021T](https://stacks.math.columbia.edu/tag/021T) in the Stacks Project.

**`AlgebraicGeometry.bigAffineFppf_isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/BigSite.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/BigSite.lean#L112).

> **Stacks 021T.** Standard fppf coverings of affine schemes over `S` satisfy the site
> axioms.

```lean
public theorem bigAffineFppf_isSite (B : AlgebraicGeometry.BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    IsSite (AlgebraicGeometry.BigAffineFppf.IsCovering B S hS)
```

## Tag 021U, a lemma

[Tag 021U](https://stacks.math.columbia.edu/tag/021U) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSite.hasPullbacks_schemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L104). The attribute's comment: “fibre products in the big fppf site”.

> The underlying category of a big fppf site admits fibre products.

```lean
public theorem BigFppfSite.hasPullbacks_schemes : HasPullbacks B.Schemes
```

**`AlgebraicGeometry.hasPullbacks_bigFppfOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L111). The attribute's comment: “fibre products in the big fppf slice”.

> The big fppf category over `S` admits fibre products.

```lean
public theorem hasPullbacks_bigFppfOver :
    HasPullbacks (AlgebraicGeometry.BigFppfOver B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_bigFppfOverToScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L117). The attribute's comment: “preservation by the big fppf slice functor to schemes”.

> The canonical functor from the big fppf category over `S` to the category of all schemes
> preserves fibre products.

```lean
public theorem preservesPullbacks_bigFppfOverToScheme :
    PreservesLimitsOfShape WalkingCospan
      (AlgebraicGeometry.BigFppfOver.toScheme B S hS)
```

**`AlgebraicGeometry.isTerminal_mkId_bigFppfOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L124). The attribute's comment: “the final object of the big fppf slice is S / S”.

> The final object of the big fppf category over `S` is `S / S`, the identity of `S` viewed as
> an object over `S`.

```lean
public noncomputable def isTerminal_mkId_bigFppfOver :
    IsTerminal (C := AlgebraicGeometry.BigFppfOver B S hS) (Over.mk (𝟙 (B.obj hS)))
```

**`AlgebraicGeometry.hasPullbacks_bigAffineFppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L149). The attribute's comment: “fibre products in the big affine fppf site”.

> The category of affine objects in the big fppf category over `S` admits fibre products.

```lean
public instance hasPullbacks_bigAffineFppf :
    HasPullbacks (AlgebraicGeometry.BigAffineFppf B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_bigAffineFppfToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L162). The attribute's comment: “preservation by the big affine fppf functor to schemes”.

> The canonical functor from affine objects over `S` to schemes preserves fibre products.

```lean
public instance preservesPullbacks_bigAffineFppfToScheme :
    PreservesLimitsOfShape WalkingCospan
      (AlgebraicGeometry.BigAffineFppf.toScheme B S hS)
```

Declarations registered for the tag:

- [`schemeSizeBelow_isClosedUnderLimitsOfShape_walkingCospan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=schemeSizeBelow_isClosedUnderLimitsOfShape_walkingCospan#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L89) (StacksFrontier): “closure of size-bounded schemes under fibre products”.
- [`CategoryTheory.Limits.createsLimitsOfShapeFullSubcategoryInclusion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.createsLimitsOfShapeFullSubcategoryInclusion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L106) (StacksFrontier): “preservation by the big fppf site inclusion”.

## Tag 021V, a lemma

[Tag 021V](https://stacks.math.columbia.edu/tag/021V) in the Stacks Project.

**`AlgebraicGeometry.bigAffineFppfInclusion_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean#L235). The attribute's comment: “cocontinuity”.

> The inclusion of affine objects over `S` in a chosen big fppf site is cocontinuous.

```lean
public instance bigAffineFppfInclusion_isCocontinuous
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (AlgebraicGeometry.BigAffineFppf.inclusion B S hS).IsCocontinuous
      (AlgebraicGeometry.BigAffineFppf.topology B S hS)
      (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.bigAffineFppfInclusion_isDenseSubsite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Equivalence.lean#L296). The attribute's comment: “equivalence of topoi”.

> The inclusion of affine objects over `S` in a chosen big fppf site is a dense subsite, so the
> induced morphism of sheaf topoi is an equivalence.

```lean
public instance bigAffineFppfInclusion_isDenseSubsite
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (AlgebraicGeometry.BigAffineFppf.inclusion B S hS).IsDenseSubsite
      (AlgebraicGeometry.BigAffineFppf.topology B S hS)
      (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Tag 021W, a lemma

[Tag 021W](https://stacks.math.columbia.edu/tag/021W) in the Stacks Project.

**`AlgebraicGeometry.bigFppfMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L105). The attribute's comment: “the morphism of topoi”.

> **Stacks 021W.** The morphism of big fppf topoi induced by postcomposition along
> `f`.

```lean
public noncomputable def bigFppfMorphism :
    MorphismOfTopoi
      (Sheaf (B.topology.over T) (Type (u + 1)))
      (Sheaf (B.topology.over S) (Type (u + 1)))
```

**`AlgebraicGeometry.bigFppfLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L120). The attribute's comment: “existence of lower shriek”.

> **Stacks 021W.** The left adjoint of the inverse image is sheaf pullback along
> postcomposition.

```lean
public noncomputable def bigFppfLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (B.topology.over T) (B.topology.over S) ⊣
        (bigFppfMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.bigFppfLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L133). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 021W.** The left adjoint of the inverse image preserves fibre products.

```lean
public instance bigFppfLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (B.topology.over T) (B.topology.over S))
```

**`AlgebraicGeometry.bigFppfLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L144). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 021W.** The left adjoint of the inverse image preserves equalizers.

```lean
public instance bigFppfLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (B.topology.over T) (B.topology.over S))
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L54) (StacksFrontier): “the postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L55) (StacksFrontier): “the base-change functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L56) (StacksFrontier): “the base-change adjunction”.
- [`CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L57) (StacksFrontier): “cocontinuity of postcomposition”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L59) (StacksFrontier): “continuity of postcomposition”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L61) (StacksFrontier): “continuity of base change”.
- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L63) (StacksFrontier): “the inverse-image formula”.
- [`CategoryTheory.Adjunction.sheafPushforwardCocontinuousIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/MorphismOfTopoi.lean#L65) (StacksFrontier): “the direct-image formula”.

## Tag 021X, a lemma

[Tag 021X](https://stacks.math.columbia.edu/tag/021X) in the Stacks Project.

**`AlgebraicGeometry.bigFppfMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean#L94). The attribute's comment: “canonical direct-image comparison”.

> **Stacks 021X.** Composition of the morphisms of big fppf topoi agrees, naturally on
> sheaves, with the morphism attached to the composite map of schemes.

```lean
public noncomputable def bigFppfMorphism_comp_pushforwardIso
    (B : AlgebraicGeometry.BigFppfSite.{u}) {X Y Z : B.Schemes}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    (bigFppfMorphism B X Z (f ≫ g)).pushforward ≅
      ((bigFppfMorphism B Y Z g).comp
        (bigFppfMorphism B X Y f)).pushforward
```

**`AlgebraicGeometry.bigFppfMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean#L113). The attribute's comment: “canonical inverse-image comparison”.

> **Stacks 021X.** The inverse-image comparison is the mate of the direct-image
> comparison.

```lean
public noncomputable def bigFppfMorphism_comp_inverseImageIso
    (B : AlgebraicGeometry.BigFppfSite.{u}) {X Y Z : B.Schemes}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    (bigFppfMorphism B X Z (f ≫ g)).inverseImage ≅
      ((bigFppfMorphism B Y Z g).comp
        (bigFppfMorphism B X Y f)).inverseImage
```

**`AlgebraicGeometry.bigFppfMorphism_comp_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/Composition.lean#L127). The attribute's comment: “compatibility with the adjunction”.

> **Stacks 021X.** The two canonical comparisons respect the units of the geometric
> morphisms.

```lean
public theorem bigFppfMorphism_comp_adjunction
    (B : AlgebraicGeometry.BigFppfSite.{u}) {X Y Z : B.Schemes}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (V : Sheaf (B.topology.over Z) (Type (u + 1))) :
    let h := bigFppfMorphism B X Z (f ≫ g)
    let k := (bigFppfMorphism B Y Z g).comp
      (bigFppfMorphism B X Y f)
    h.adj.unit.app V ≫
        h.pushforward.map ((bigFppfMorphism_comp_inverseImageIso B f g).hom.app V) ≫
        (bigFppfMorphism_comp_pushforwardIso B f g).hom.app
          (k.inverseImage.obj V) = k.adj.unit.app V
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.7, Tag 021L](https://stacks.math.columbia.edu/tag/021L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
