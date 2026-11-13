---
declaration: section
origin: cited
lean: Algebra.exists_etale_finite_factors_positiveDim_remainder, HenselianLocalRing, HenselianLocalRing.TFAE, IsAdicComplete.henselianRing, IsLocalRing.henselian_tfae, exists_algEquiv_pi_henselianLocalRing_of_module_finite, StrictlyHenselianLocalRing, Stacks.EtaleCohomology.exists_algEquiv_pi_puncturedKummerAlgebra
statement: formalized
proof: formalized
---

# 59.32 Henselian rings

Section 59.32 of the Stacks Project, [Tag 03QD](https://stacks.math.columbia.edu/tag/03QD). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03QE, a theorem

[Tag 03QE](https://stacks.math.columbia.edu/tag/03QE) in the Stacks Project.

**`Algebra.exists_etale_finite_factors_positiveDim_remainder`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalStructureFibreDimension.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalStructureFibreDimension.lean#L184). References: EGA IV (18.12.1), “affine case”.

> After an étale base change preserving the residue field at `p`, a finite type
> algebra splits into finitely many finite factors, each with exactly one prime
> over `p'`, and a factor whose fibre has no zero-dimensional irreducible
> component.

```lean
theorem exists_etale_finite_factors_positiveDim_remainder
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (p : Ideal R) [p.IsPrime] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R')
      (p' : Ideal R') (_ : p'.IsPrime) (_ : p'.LiesOver p)
      (n : ℕ) (e : Fin (n + 1) → R' ⊗[R] S)
      (_ : CompleteOrthogonalIdempotents e)
      (r : Fin n → Ideal (R' ⊗[R] S))
      (_ : ∀ i, (r i).IsPrime) (_ : ∀ i, (r i).LiesOver p'),
      Function.Bijective (Ideal.ResidueField.mapₐ p p' (Algebra.ofId _ _) (p'.over_def p)) ∧
      (∀ i : Fin n, Module.Finite R' (Localization.Away (e i.castSucc))) ∧
      (∀ i : Fin n, e i.castSucc ∉ r i) ∧
      (∀ (i : Fin n) (q : Ideal (R' ⊗[R] S)), q.IsPrime → q.LiesOver p' →
        e i.castSucc ∉ q → q = r i) ∧
      (∀ Z ∈ irreducibleComponents
          (PrimeSpectrum (p'.Fiber (Localization.Away (e (Fin.last n))))),
        1 ≤ topologicalKrullDim Z)
```

## Tag 03QF, a definition

[Tag 03QF](https://stacks.math.columbia.edu/tag/03QF) in the Stacks Project.

Declarations registered for the tag:

- [`HenselianLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HenselianLocalRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L322) (StacksFrontier). References: EGA IV (18.5.8), “special case”; SGA 4 VIII (4.1); SGA 4 XII (6.13), “special case”.
- [`HenselianLocalRing.TFAE`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HenselianLocalRing.TFAE#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L323) (StacksFrontier): “Stacks' formulation, with `a₀` in the residue field (item 2)”.

## Tag 03QG, a theorem

[Tag 03QG](https://stacks.math.columbia.edu/tag/03QG) in the Stacks Project.

Declarations registered for the tag:

- [`IsAdicComplete.henselianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsAdicComplete.henselianRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L327) (StacksFrontier): “for `I = maximalIdeal R`, `HenselianRing R (maximalIdeal R)` is the condition of 03QF”. References: EGA IV (18.5.14), “more general”; EGA IV (18.5.16), “more general”; SGA 3 X (4.0), “Recall 4.0”.

## Tag 03QH, a theorem

[Tag 03QH](https://stacks.math.columbia.edu/tag/03QH) in the Stacks Project.

**`IsLocalRing.henselian_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Characterizations.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Characterizations.lean#L318). References: EGA IV (18.5.13), “a'') existence half”; EGA IV (18.5.9), “(ii)”; EGA IV (18.5.11), “a), a'), b)”; SGA 4 VIII (4.1), “(i), (iii), (iv)”; SGA 3 X (4.5), “special case”; SGA 7 IX (2.2.3), “(4), special case”.

> **Stacks 03QH.** The five standard characterizations of a henselian local ring:
> henselianness, coprime factorization lifting, decomposition of module-finite algebras,
> splitting the finite part of finite type algebras, and splitting pointed étale
> algebras.

```lean
theorem henselian_tfae (R : Type u) [CommRing R] [IsLocalRing R] :
    List.TFAE [HenselianLocalRing R,
      HasCoprimeFactorizationLifting R,
      FiniteAlgebrasSplitIntoLocalFactors.{u, v} R,
      FiniteTypeAlgebrasSplitOffFiniteLocalFactors.{u, v} R,
      PointedEtaleAlgebrasSplit.{u, v} R]
```

## Tag 03QJ, a lemma

[Tag 03QJ](https://stacks.math.columbia.edu/tag/03QJ) in the Stacks Project.

**`exists_algEquiv_pi_henselianLocalRing_of_module_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/FiniteAlgebras.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/FiniteAlgebras.lean#L44). References: EGA IV (18.5.10), “R henselian local”; EGA IV (18.5.9), “(ii) necessity”; EGA IV (18.5.11), “(F), partial”; EGA IV (18.6.7), “special case”; SGA 4 VIII (4.1), “(i), forward direction”.

> A finite algebra over a henselian local ring is a finite product of
> henselian local rings, each finite over the base.

```lean
theorem exists_algEquiv_pi_henselianLocalRing_of_module_finite
    (R : Type u) [CommRing R] [HenselianLocalRing R]
    (A : Type v) [CommRing A] [Algebra R A] [Module.Finite R A] :
    ∃ (ι : Type v) (_ : Finite ι) (B : ι → Type v)
      (_ : ∀ i, CommRing (B i)) (_ : ∀ i, Algebra R (B i))
      (_ : ∀ i, HenselianLocalRing (B i)),
      (∀ i, Module.Finite R (B i)) ∧ Nonempty (A ≃ₐ[R] ∀ i, B i)
```

## Tag 03QK, a definition

[Tag 03QK](https://stacks.math.columbia.edu/tag/03QK) in the Stacks Project.

**`StrictlyHenselianLocalRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/StrictlyHenselian.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/StrictlyHenselian.lean#L35). References: SGA 7 XIII (0.2), “(0.2.3) ring case”; SGA 4 VIII (4.2), “(i)”; SGA 7 I (0.0.2), “ring case”.

> A commutative ring is strictly henselian if it is a henselian local ring and its
> residue field is separably closed.

```lean
class StrictlyHenselianLocalRing (R : Type*) [CommRing R] : Prop extends
  HenselianLocalRing R, IsSepClosed (IsLocalRing.ResidueField R)
```

## Tag 03QI, an example

[Tag 03QI](https://stacks.math.columbia.edu/tag/03QI) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_algEquiv_pi_puncturedKummerAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean#L390). The attribute's comment: “classification of étale algebras”.

> Every étale algebra over `ℂ⟦t⟧` is a finite product of trivial factors and
> punctured Kummer extensions of positive degree.

```lean
theorem exists_algEquiv_pi_puncturedKummerAlgebra
    (A : Type*) [CommRing A] [Algebra (PowerSeries ℂ) A]
    [Algebra.Etale (PowerSeries ℂ) A] :
    ∃ (ι κ : Type*) (_ : Finite ι) (_ : Finite κ) (n : κ → ℕ),
      (∀ j, 0 < n j) ∧
      Nonempty (A ≃ₐ[PowerSeries ℂ]
        (ι → PowerSeries ℂ) × (∀ j, puncturedKummerAlgebra (n j)))
```

**`Stacks.EtaleCohomology.etale_puncturedKummerAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean#L436). The attribute's comment: “étaleness of the Kummer extensions”.

> A punctured Kummer extension of positive degree is étale over `ℂ⟦t⟧`.

```lean
theorem etale_puncturedKummerAlgebra (n : ℕ) (hn : 0 < n) :
    Algebra.Etale (PowerSeries ℂ) (puncturedKummerAlgebra n)
```

**`Stacks.EtaleCohomology.isUnit_parameter_puncturedKummerAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean#L468). The attribute's comment: “factorization through the punctured spectrum”.

> The parameter is invertible on a punctured Kummer extension, so its spectrum
> maps into `D(t)`.

```lean
theorem isUnit_parameter_puncturedKummerAlgebra (n : ℕ) :
    IsUnit (algebraMap (PowerSeries ℂ) (puncturedKummerAlgebra n) PowerSeries.X)
```

**`Stacks.EtaleCohomology.etaleCover_has_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComplexPowerSeries.lean#L487). The attribute's comment: “refinement by the identity cover”.

> An étale covering of `Spec ℂ⟦t⟧` has a member whose structure morphism
> admits a section, so the identity cover refines it.

```lean
theorem etaleCover_has_section
    (𝒰 : (Spec (.of (PowerSeries ℂ))).Cover Scheme.etalePrecoverage) :
    ∃ i : 𝒰.I₀, ∃ s : Spec (.of (PowerSeries ℂ)) ⟶ 𝒰.X i,
      s ≫ 𝒰.f i = 𝟙 (Spec (.of (PowerSeries ℂ)))
```

## Tag 03QL, a theorem

[Tag 03QL](https://stacks.math.columbia.edu/tag/03QL) in the Stacks Project.

**`IsLocalRing.henselizationTower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/HenselizationTower.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/HenselizationTower.lean#L195). The attribute's comment: “existence, flat local maps, and parts (1), (2), and (4)”.

> The canonical henselization/strict-henselization tower associated to a local ring and a
> chosen separable closure of its residue field.

```lean
public noncomputable def henselizationTower (R : Type u) [CommRing R] [IsLocalRing R]
    (κsep : Type v) [Field κsep] [Algebra (ResidueField R) κsep]
    [IsSepClosure (ResidueField R) κsep] : HenselizationTower R κsep
```

**`HenselianLocalRing.existsUnique_isLocalHom_of_ind_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Canonicity.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Canonicity.lean#L57). The attribute's comment: “canonicity of the map from the henselization”. References: EGA IV (18.6.6), “(ii)”; SGA 4 VIII (4.1), “partial”.

> **The universal property of the henselization, in existential form** (Stacks 04GS). Let
> `(R, 𝔪, κ)` be a local ring, let `Rh` be a local `R`-algebra with `R → Rh` local which is a
> filtered colimit of étale `R`-algebras and has residue field `κ`, and let `Sh` be a henselian
> local ring with `R → Sh` local. Then there is exactly one `R`-algebra map `Rh → Sh` that is a
> local ring map. This is what makes the maps `R → R^h → R^{sh}` of Tag 03QL canonical: applied
> to `Rh = R^h` and `Sh = R^{sh}` it pins the map out of the henselization uniquely.

```lean
public theorem HenselianLocalRing.existsUnique_isLocalHom_of_ind_etale
    {R : Type u} {Rh : Type v} {Sh : Type w} [CommRing R] [CommRing Rh] [CommRing Sh]
    [IsLocalRing R]
    [IsLocalRing Rh] [HenselianLocalRing Sh] [Algebra R Rh] [Algebra R Sh]
    [IsLocalHom (algebraMap R Rh)] [IsLocalHom (algebraMap R Sh)]
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rh)))
    (hres : Function.Surjective (ResidueField.map (algebraMap R Rh))) :
    ∃! f : Rh →ₐ[R] Sh, IsLocalHom f
```

Declarations registered for the tag:

- [`IsLocalRing.IsHenselization.map_maximalIdeal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/Defs.lean#L414), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/HenselizationTower.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/HenselizationTower.lean#L282) (StacksFrontier): “part (3): maximal ideals”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.32, Tag 03QD](https://stacks.math.columbia.edu/tag/03QD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
