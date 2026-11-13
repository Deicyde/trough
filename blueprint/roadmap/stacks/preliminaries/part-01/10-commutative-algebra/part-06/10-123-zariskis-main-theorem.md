---
declaration: section
origin: cited
lean: RingHom.isIntegralElem_leadingCoeff_mul, RingHom.isIntegralElem_zero, StronglyTranscendental, Algebra.not_quasiFiniteAt_of_isStronglyTranscendental, main_theorem_00q8, isOpen_quasiFiniteLocus, quasiFinite_comap_integralClosure_isOpenEmbedding, quasiFinite_awayMap_integralClosure_bijective
statement: formalized
proof: formalized
---

# 10.123 Zariski's Main Theorem

Section 10.123 of the Stacks Project, [Tag 00PI](https://stacks.math.columbia.edu/tag/00PI). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00PQ, a lemma

[Tag 00PQ](https://stacks.math.columbia.edu/tag/00PQ) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.isIntegralElem_leadingCoeff_mul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.isIntegralElem_leadingCoeff_mul#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L353) (StacksFrontier): “scaling by the leading coefficient makes an element integral”.
- [`RingHom.isIntegralElem_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.isIntegralElem_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L355) (StacksFrontier): “the degenerate case, where the top coefficient vanishes”.

## Tag 00PZ, a definition

[Tag 00PZ](https://stacks.math.columbia.edu/tag/00PZ) in the Stacks Project.

**`StronglyTranscendental`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/StronglyTranscendental.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/QuasiFinite/StronglyTranscendental.lean#L221).

> An element `x : S` is *strongly transcendental over `R`* if for every
> `u : S` and every polynomial `p : R[X]`, the equation `u * p(x) = 0` in `S`
> forces `u * (algebraMap R S) (p.coeff i) = 0` for every coefficient index
> `i`. This is the algebraic version of the Stacks definition.

```lean
def StronglyTranscendental (R S : Type*) [CommRing R] [CommRing S]
    [Algebra R S] (x : S) : Prop
```

## Tag 00Q2, a lemma

[Tag 00Q2](https://stacks.math.columbia.edu/tag/00Q2) in the Stacks Project.

**`Algebra.not_quasiFiniteAt_of_isStronglyTranscendental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/StronglyTranscendental.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/QuasiFinite/StronglyTranscendental.lean#L199). The attribute's comment: “`R ⊂ S` is `[FaithfulSMul R S]` with both rings `[IsReduced]`; `S` finite over `R[x]` is `(Polynomial.aeval x).toRingHom.Finite`; and "not quasi-finite at any prime" is `¬ Algebra.QuasiFiniteAt R q` for an arbitrary prime `q` of `S`. The contrapositive is Mathlib's `Algebra.not_isStronglyTranscendental_of_quasiFiniteAt`, which drops `[IsReduced R]` and `[FaithfulSMul R S]`. See the module docstring.”.

> **Stacks 00Q2.** Let `R ⊂ S` be an inclusion of reduced rings, let `x ∈ S` be strongly
> transcendental over `R`, and assume `S` is finite over `R[x]`. Then `R → S` is not quasi-finite
> at any prime `q` of `S`.

```lean
public theorem not_quasiFiniteAt_of_isStronglyTranscendental {R S : Type*} [CommRing R]
    [CommRing S] [IsReduced R] [IsReduced S] [Algebra R S] [FaithfulSMul R S] {x : S}
    (hx : IsStronglyTranscendental R x) (hx' : (Polynomial.aeval (R := R) x).toRingHom.Finite)
    (q : Ideal S) [q.IsPrime] : ¬ QuasiFiniteAt R q
```

## Tag 00Q8, a lemma

[Tag 00Q8](https://stacks.math.columbia.edu/tag/00Q8) in the Stacks Project.

**`main_theorem_00q8`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ZariskisMainTheorem/Monogenic.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ZariskisMainTheorem/Monogenic.lean#L634).

> Stacks tag 00Q8 (Lemma 10.123.11). For `S = R[X]/I` monogenic over `R` and a
> prime `q ⊂ S` at which `R → S` is quasi-finite, there is an element `g` of the
> integral closure `S'` of `R` in `S` with `g ∉ q` such that the induced map
> `S'_g → S_g` is an isomorphism.

```lean
theorem main_theorem_00q8 (R : Type*) [CommRing R] (I : Ideal (R[X]))
    (q : Ideal (R[X] ⧸ I)) [q.IsPrime]
    (hqf : QuasiFiniteAt (R := R) q) :
    ∃ g : integralClosure R (R[X] ⧸ I), (g : R[X] ⧸ I) ∉ q ∧
      Function.Bijective (QF.locMap (R := R) g)
```

## Tag 00QA, a lemma

[Tag 00QA](https://stacks.math.columbia.edu/tag/00QA) in the Stacks Project.

**`isOpen_quasiFiniteLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Locus.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/QuasiFinite/Locus.lean#L102). References: EGA III (4.4.10), “affine case”; EGA IV (13.1.4), “affine case”; EGA III (4.4.3), “affine case, X' open”; SGA 3 V (7.3), “special case”.

> For a finite-type ring map `R → S`, the locus in `Spec(S)` where `S/R` is quasi-finite is
> open.

```lean
theorem isOpen_quasiFiniteLocus
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S] :
    IsOpen (quasiFiniteLocus R S)
```

## Tag 00QB, a lemma

[Tag 00QB](https://stacks.math.columbia.edu/tag/00QB) in the Stacks Project.

**`quasiFinite_comap_integralClosure_isOpenEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ZariskisMainTheorem.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ZariskisMainTheorem.lean#L568). The attribute's comment: “(1)”.

> The map on spectra `Spec(S) → Spec(S')` induced by the inclusion `S' ↪ S` is an open
> topological embedding: a homeomorphism of `Spec(S)` onto an open subset of `Spec(S')`.

```lean
theorem quasiFinite_comap_integralClosure_isOpenEmbedding
    [Algebra.FiniteType R S] [Algebra.QuasiFinite R S] :
    IsOpenEmbedding (PrimeSpectrum.comap (integralClosure R S).val.toRingHom)
```

**`quasiFinite_awayMap_integralClosure_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ZariskisMainTheorem.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ZariskisMainTheorem.lean#L578). The attribute's comment: “(2)”.

> For every `g ∈ S'` such that the basic open `D(g) ⊆ Spec(S')` is contained in the image of
> `Spec(S) → Spec(S')`, the natural ring homomorphism `S'_g → S_g` induced by `S' ↪ S` is
> bijective.

```lean
theorem quasiFinite_awayMap_integralClosure_bijective
    [Algebra.FiniteType R S] [Algebra.QuasiFinite R S]
    (g : integralClosure R S)
    (hg : (PrimeSpectrum.basicOpen g : Set (PrimeSpectrum (integralClosure R S)))
      ⊆ Set.range (PrimeSpectrum.comap (integralClosure R S).val.toRingHom)) :
    Function.Bijective (Localization.awayMap (integralClosure R S).val.toRingHom g)
```

**`quasiFinite_exists_finite_subalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ZariskisMainTheorem.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ZariskisMainTheorem.lean#L680). The attribute's comment: “(3)”. References: EGA III (4.4.3), “affine case, X=X'”; EGA IV (8.12.6), “affine case”; EGA IV (18.12.13), “affine case”; EGA III (4.4.6), “special case”; EGA IV (8.12.9), “Affine case”; SGA 1 VIII (6.4), “affine case”.

> There is an `R`-subalgebra `S''` of `S`, contained in the integral closure `S'` and finite as
> an `R`-module, such that `Spec(S) → Spec(S'')` is an open topological embedding and
> `S''_g → S_g` is bijective for every `g ∈ S''` whose basic open `D(g)` lies in the image of that
> map.

```lean
theorem quasiFinite_exists_finite_subalgebra
    [Algebra.FiniteType R S] [Algebra.QuasiFinite R S] :
    ∃ S'' : Subalgebra R S, S'' ≤ integralClosure R S ∧ Module.Finite R S'' ∧
      IsOpenEmbedding (PrimeSpectrum.comap S''.val.toRingHom) ∧
      ∀ g : S'', (PrimeSpectrum.basicOpen g : Set (PrimeSpectrum S'')) ⊆
          Set.range (PrimeSpectrum.comap S''.val.toRingHom) →
        Function.Bijective (Localization.awayMap S''.val.toRingHom g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.123, Tag 00PI](https://stacks.math.columbia.edu/tag/00PI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
