---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsImmersion.of_comp, AlgebraicGeometry.QuasiCompact.of_comp, AlgebraicGeometry.IsClosedImmersion.of_comp, AlgebraicGeometry.IsImmersion.isImmersion_iff_exists_of_quasiCompact, AlgebraicGeometry.exists_openImmersion_closedImmersion_factorization_of_isReduced, Stacks.Immersion.NotOpenThenClosed.chartIdeal, Stacks.Immersion.NotOpenThenClosed.puncturedSpectrum, Stacks.Immersion.NotOpenThenClosed.nonextendableIdealSheaf
statement: formalized
proof: formalized
---

# 29.3 Immersions

Section 29.3 of the Stacks Project, [Tag 07RJ](https://stacks.math.columbia.edu/tag/07RJ). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07RK, a lemma

[Tag 07RK](https://stacks.math.columbia.edu/tag/07RK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L331) (StacksFrontier): “(1); also the immersion part of (2)”. References: EGA I (5.3.13); EGA I (5.3.14), “more general”; EGA I (5.5.12), “special case”; EGA IV (8.12.2), “more general”; EGA IV (16.2.3), “more general”; SGA 6 VIII (1.3), “(iv)”; SGA 6 VIII (1.8), “partial”.
- [`AlgebraicGeometry.QuasiCompact.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L332) (StacksFrontier): “(2), quasi-compactness of Z → Y when Y → X is quasi-separated”. References: EGA I (5.5.12), “(i), special case”; EGA I (6.3.4), “(v)”; EGA I (6.6.4), “more general”; EGA II (8.14.6), “more general”; EGA IV (1.1.2), “more general”; EGA IV (1.2.4); EGA IV (1.5.4), “(v)”; EGA IV (18.12.13), “more general”; SGA 3 VIB (11.1), “partial”; SGA 3 VIB (12.9), “Quasi-compactness of ρ”; SGA 4 VI (1.9.1), “(iv), special case”.
- [`AlgebraicGeometry.IsClosedImmersion.of_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.of_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L334) (StacksFrontier): “(3)”. References: EGA I (5.4.4); EGA I (5.4.6), “more general”; EGA I (5.5.12), “(i), special case”; EGA IV (17.9.3), “partial”; SGA 1 II (4.17), “more general”; SGA 3 VIB (5.6.3), “(i) ⇒ (ii)”; SGA 3 VIB (11.18.1), “more general”.

## Tag 01QV, a lemma

[Tag 01QV](https://stacks.math.columbia.edu/tag/01QV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.isImmersion_iff_exists_of_quasiCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.isImmersion_iff_exists_of_quasiCompact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L135) (StacksFrontier): “the forward implication”.

## Tag 03DQ, a lemma

[Tag 03DQ](https://stacks.math.columbia.edu/tag/03DQ) in the Stacks Project.

**`AlgebraicGeometry.exists_openImmersion_closedImmersion_factorization_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/Immersions.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/Immersions.lean#L57). References: EGA I (5.2.3), “factorization only”.

> An immersion of a reduced scheme factors as an open immersion followed by a closed
> immersion.

```lean
theorem exists_openImmersion_closedImmersion_factorization_of_isReduced
    {Z X : Scheme.{u}} (f : Z ⟶ X) [IsImmersion f] [IsReduced Z] :
    ∃ (Y : Scheme.{u}) (j : Z ⟶ Y) (i : Y ⟶ X),
      IsOpenImmersion j ∧ IsClosedImmersion i ∧ j ≫ i = f
```

## Tag 01QW, an example

[Tag 01QW](https://stacks.math.columbia.edu/tag/01QW) in the Stacks Project.

**`Stacks.Immersion.NotOpenThenClosed.chartIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L94). The attribute's comment: “chart ideals”.

> The ideal cutting out the closed subscheme on the `n`-th standard chart: it is generated by
> the `n`-th variable minus one, the `(n + 1)`-st powers of the earlier variables, and all later
> variables.

```lean
public def chartIdeal (k : Type u) [Field k] (n : ℕ) : Ideal (polynomialRing k)
```

**`Stacks.Immersion.NotOpenThenClosed.puncturedSpectrum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L128). The attribute's comment: “union of standard opens”.

> The union of the standard opens: the complement of the point at which every variable
> vanishes.

```lean
public abbrev puncturedSpectrum (k : Type u) [Field k] :
    (ambientSpectrum k).Opens
```

**`Stacks.Immersion.NotOpenThenClosed.nonextendableIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L507). The attribute's comment: “glued quasi-coherent ideal sheaf”.

> The ideal sheaf glued from the specified ideals on the standard-open cover.

```lean
public noncomputable def nonextendableIdealSheaf (k : Type u) [Field k] :
    { J : (puncturedSpectrum k).toScheme.IdealSheafData //
      ∀ n : ℕ,
        IsClosedImmersion
          (pullback.snd (J.subschemeι ≫ (puncturedSpectrum k).ι)
            (coordinateOpen k n).ι) ∧
        (pullback.snd (J.subschemeι ≫ (puncturedSpectrum k).ι)
          (coordinateOpen k n).ι).ker =
          ((Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (chartIdeal k n)))).ker).comap
            (coordinateOpen k n).ι }
```

**`Stacks.Immersion.NotOpenThenClosed.counterexampleImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L524). The attribute's comment: “associated morphism”.

> The immersion of the closed subscheme of the punctured spectrum into the ambient affine
> scheme.

```lean
public noncomputable def counterexampleImmersion (k : Type u) [Field k] :
    (nonextendableIdealSheaf k).1.subscheme ⟶ ambientSpectrum k
```

**`Stacks.Immersion.NotOpenThenClosed.chartIdeal_overlap_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L530). The attribute's comment: “unit ideal on distinct chart overlaps”.

> Away from two distinct variables, the indicated chart ideal is the unit ideal.

```lean
public theorem chartIdeal_overlap_top (k : Type u) [Field k] (n m : ℕ) (hnm : n ≠ m) :
    (chartIdeal k n).map
      (algebraMap (polynomialRing k)
        (Localization.Away ((MvPolynomial.X n : polynomialRing k) *
          MvPolynomial.X m))) = ⊤
```

**`Stacks.Immersion.NotOpenThenClosed.iInf_chartIdeal_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L594). The attribute's comment: “intersection of chart ideals”.

> The chart ideals have zero intersection in the original polynomial ring.

```lean
public theorem iInf_chartIdeal_eq_bot (k : Type u) [Field k] :
    (⨅ n : ℕ, chartIdeal k n) = ⊥
```

**`Stacks.Immersion.NotOpenThenClosed.counterexampleImmersion_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L623). The attribute's comment: “immersion”.

> The closed subscheme of the punctured spectrum is an immersion in the ambient spectrum.

```lean
public theorem counterexampleImmersion_isImmersion (k : Type u) [Field k] :
    IsImmersion (counterexampleImmersion k)
```

**`Stacks.Immersion.NotOpenThenClosed.counterexampleImmersion_no_open_closed_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/NotOpenThenClosed.lean#L721). The attribute's comment: “failure of open-then-closed factorization”.

> This immersion cannot factor as an open immersion followed by a closed immersion.

```lean
public theorem counterexampleImmersion_no_open_closed_factorization
    (k : Type u) [Field k] :
    ¬ ∃ (T : Scheme.{u})
        (g : (nonextendableIdealSheaf k).1.subscheme ⟶ T)
        (h : T ⟶ ambientSpectrum k),
        IsOpenImmersion g ∧ IsClosedImmersion h ∧
          g ≫ h = counterexampleImmersion k
```

## Tag 0FCZ, a lemma

[Tag 0FCZ](https://stacks.math.columbia.edu/tag/0FCZ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.instIsZariskiLocalAtTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.instIsZariskiLocalAtTarget#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L153) (StacksFrontier): “being an immersion is Zariski-local on the target”. References: EGA I (4.2.4), “(a), special case”; EGA II (3.8.1), “more general”.
- [`AlgebraicGeometry.IsZariskiLocalAtTarget.of_forall_source_exists_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsZariskiLocalAtTarget.of_forall_source_exists_preimage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L155) (StacksFrontier): “the source-point criterion for target-local properties”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.3, Tag 07RJ](https://stacks.math.columbia.edu/tag/07RJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
