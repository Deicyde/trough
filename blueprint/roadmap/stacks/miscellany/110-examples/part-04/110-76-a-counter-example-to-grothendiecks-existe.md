---
declaration: section
origin: cited
lean: AlgebraicGeometry.counterexamples_algebraization_of_not_isSeparated
statement: formalized
proof: formalized
---

# 110.76 A counter example to Grothendieck's existence theorem

Section 110.76 of the Stacks Project, [Tag 0ARE](https://stacks.math.columbia.edu/tag/0ARE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ARF, a lemma

[Tag 0ARF](https://stacks.math.columbia.edu/tag/0ARF) in the Stacks Project.

**`AlgebraicGeometry.counterexamples_algebraization_of_not_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NonSeparatedAlgebraizationCounterexamples.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NonSeparatedAlgebraizationCounterexamples.lean#L68). The attribute's comment: “all three counterexamples: (1) 088E fails without separatedness, (2) Coh\_\{X/Y} of 09DS and 08WC is not algebraic for a flat morphism of finite presentation which is not separated, (3) Quot\_\{F/X/B} of 09TU (F = O\_X of finite presentation) is not an algebraic space for such a morphism; witness: Spec k[[t]] with its closed point doubled”.

> **Stacks 0ARF.** Counterexamples to algebraization of coherent sheaves without separatedness:
>
> 1. Grothendieck's existence theorem (Stacks 088E) fails without separatedness: it is not true
>    that for every Noetherian ring `A` complete with respect to an ideal `I` and every morphism
>    `f : X ⟶ Spec A` locally of finite type and quasi-compact, the completion functor from coherent
>    `𝒪_X`-modules with support proper over `A` to coherent `I`-adic systems with support proper
>    over `A` is an equivalence;
> 2. there is a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S`, of finite presentation
>    and flat but not separated, whose stack of coherent sheaves `Coh_{X/Y}` is not an algebraic
>    stack (so Stacks 09DS and 08WC fail without separatedness);
> 3. there is a Quot situation `f : X ⟶ B` over a scheme `S`, of finite presentation and flat but not
>    separated, with `F` of finite presentation, such that the functor `Quot_{F/X/B}` has a model in
>    the universe of the site but no model is an algebraic space (so Stacks 09TU fails without
>    separatedness).

```lean
theorem counterexamples_algebraization_of_not_isSeparated :
    (¬ ∀ (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
        {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] [QuasiCompact f],
        (Stacks.Algebraization.completionFunctorProperOver A I f).IsEquivalence) ∧
    (∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (D : Space.CoherentSituation B S hS),
      Space.IsFlat B S hS D.f.hom ∧ ¬ Space.IsSeparated B S hS D.f.hom ∧
        ¬ Stack.IsAlgebraicStack.{u, w} B S hS D.coherentCFG.val) ∧
    (∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (D : Space.QuotSituation B S hS),
      Space.IsFlat B S hS D.f.hom ∧ ¬ Space.IsSeparated B S hS D.f.hom ∧
        D.F.IsFinitePresentationOnSite ∧ Nonempty (Space.QuotSitePresheafModel D) ∧
        ∀ N : Space.QuotSitePresheafModel D, ¬ IsAlgebraicSpace B S hS N.presheaf)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.76, Tag 0ARE](https://stacks.math.columbia.edu/tag/0ARE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
