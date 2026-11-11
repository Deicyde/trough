---
declaration: section
origin: cited
lean: Module.projective_of_flat_of_projective_quotient_of_associatedPrimes, Module.Flat.projective_of_finiteType_of_geometricallyIntegral_fibres, Algebra.projective_of_geometricallyIntegral_fibres
statement: formalized
proof: formalized
---

# 38.9 Projective modules

Section 38.9 of the Stacks Project, [Tag 05DN](https://stacks.math.columbia.edu/tag/05DN). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05DP, a lemma

[Tag 05DP](https://stacks.math.columbia.edu/tag/05DP) in the Stacks Project.

**`Module.projective_of_flat_of_projective_quotient_of_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveOfFlatOverComplete.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveOfFlatOverComplete.lean#L87). The attribute's comment: “`N/IN` is `N ⧸ I • ⊤`; the contraction `𝔭 = R ∩ 𝔮` is `PrimeSpectrum.comap (algebraMap R S) 𝔮` and `κ(𝔭)` its `ResidueField`; the condition `IS + 𝔮 ≠ S` is the join of ideals being different from `⊤`.”.

> **Stacks Project, Tag 05DP.** Let `R` be a Noetherian ring, `I`-adically complete, let `S` be
> a finite type `R`-algebra and let `N` be a finite `S`-module which is flat over `R`. If `N/IN` is
> projective over `R/I` and `IS + 𝔮 ≠ S` for every prime `𝔮` of `S` which is an associated prime of
> the fibre `N ⊗[R] κ(𝔭)` with `𝔭 = R ∩ 𝔮`, then `N` is projective as an `R`-module.

```lean
theorem projective_of_flat_of_projective_quotient_of_associatedPrimes (R : Type u) (S : Type v)
    [CommRing R] [CommRing S] [Algebra R S] (I : Ideal R) (N : Type w) [AddCommGroup N]
    [Module S N] [Module R N] [IsScalarTower R S N] [IsNoetherianRing R] [IsAdicComplete I R]
    [Algebra.FiniteType R S] [Module.Finite S N] [Module.Flat R N]
    (hprojective : Module.Projective (R ⧸ I) (N ⧸ I • (⊤ : Submodule R N)))
    (hassociated : ∀ q : PrimeSpectrum S, q.asIdeal ∈ associatedPrimes S
        (N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) →
      I.map (algebraMap R S) ⊔ q.asIdeal ≠ ⊤) :
    Module.Projective R N
```

## Tag 05FS, a lemma

[Tag 05FS](https://stacks.math.columbia.edu/tag/05FS) in the Stacks Project.

**`Module.Flat.projective_of_finiteType_of_geometricallyIntegral_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveOfIntegralFibres.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveOfIntegralFibres.lean#L207).

> **Stacks Project, Tag 05FS.** A flat finite type algebra over a Noetherian ring whose fibres
> are geometrically integral is projective as a module over its base ring.

```lean
theorem Module.Flat.projective_of_finiteType_of_geometricallyIntegral_fibres
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [Algebra.FiniteType R S] [Module.Flat R S]
    (h : ∀ (p : Ideal R) [p.IsPrime],
      letI : Algebra p.ResidueField (S ⊗[R] p.ResidueField) :=
        Algebra.TensorProduct.rightAlgebra
      Algebra.IsGeometricallyIntegral p.ResidueField (S ⊗[R] p.ResidueField)) :
    Module.Projective R S
```

## Tag 05FT, a lemma

[Tag 05FT](https://stacks.math.columbia.edu/tag/05FT) in the Stacks Project.

**`Algebra.projective_of_geometricallyIntegral_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/ReducedFibreFromSmoothLocus.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/ReducedFibreFromSmoothLocus.lean#L188).

> **Stacks Project, Tag 05FT.** Let `R → S` be flat and of finite presentation and suppose that
> every fibre ring `S ⊗[R] κ(p)` is geometrically integral over `κ(p)`. Then `S` is a projective
> `R`-module.
>
> This is `Algebra.projective_of_geometricallyIntegral_fibres_of_isConstructible_reduced` with its
> hypothesis — constructibility of the geometrically reduced fibre locus over a Noetherian base,
> the affine case of Stacks 0579 — discharged by
> `Algebra.isConstructible_geometricallyReducedFibreLocus'`. The irreducible half was
> discharged by `Algebra.isConstructible_geometricallyIrreducibleFibreLocus_of_finiteType`, the
> affine case of the level set `n = 1` of Stacks 055B.

```lean
public theorem projective_of_geometricallyIntegral_fibres {R S : Type u} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FinitePresentation R S] [Module.Flat R S]
    (h : ∀ (p : Ideal R) [p.IsPrime],
      letI : Algebra p.ResidueField (S ⊗[R] p.ResidueField) :=
        Algebra.TensorProduct.rightAlgebra
      Algebra.IsGeometricallyIntegral p.ResidueField (S ⊗[R] p.ResidueField)) :
    Module.Projective R S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.9, Tag 05DN](https://stacks.math.columbia.edu/tag/05DN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
