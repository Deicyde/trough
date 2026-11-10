---
declaration: section
origin: cited
lean: StacksDraft.InjectiveDimension.HasInjectiveAmplitude, StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension, StacksDraft.InjectiveDimension.hasInjectiveAmplitude_iff_ext_vanishing_iff_quotient_vanishing, StacksDraft.InjectiveDimension.dedekindDomain_ideal_projective_and_bounded_complex_splitting, StacksDraft.InjectiveDimension.dualNumber_residueField_infinite_injectiveDimension, StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_of_bounded, StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_iff_quotient_ext_vanishing, StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_iff_residueField_ext_vanishing
statement: formalized
proof: formalized
---

# 15.71 Injective dimension

Section 15.71 of the Stacks Project, [Tag 0A5R](https://stacks.math.columbia.edu/tag/0A5R). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A5S, a definition

[Tag 0A5S](https://stacks.math.columbia.edu/tag/0A5S) in the Stacks Project.

**`StacksDraft.InjectiveDimension.HasInjectiveAmplitude`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension.lean#L44). The attribute's comment: “injective amplitude”. References: SGA 6 I (5.7), “(i) definition”.

> An object of a derived category has *injective amplitude in `[a, b]`* if it is isomorphic
> to the image of a cochain complex which vanishes below `a` and above `b` and whose terms are
> injective.

```lean
public def HasInjectiveAmplitude (K : DerivedCategory C) (a b : ℤ) : Prop
```

**`StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension.lean#L51). The attribute's comment: “finite injective dimension”.

> An object of a derived category has *finite injective dimension* if it has injective
> amplitude in some finite integer interval.

```lean
public def HasFiniteInjectiveDimension (K : DerivedCategory C) : Prop
```

## Tag 0A5T, a lemma

[Tag 0A5T](https://stacks.math.columbia.edu/tag/0A5T) in the Stacks Project.

**`StacksDraft.InjectiveDimension.hasInjectiveAmplitude_iff_ext_vanishing_iff_quotient_vanishing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Criteria.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Criteria.lean#L362). References: EGA 0 (17.2.1), “partial”.

> **Stacks 0A5T.** An object of the derived category of modules has injective amplitude in
> `[a, b]` if and only if its Ext groups from all modules vanish in degrees outside `[a, b]`; this
> is in turn equivalent to testing the same vanishing only on quotients by ideals.

```lean
public lemma hasInjectiveAmplitude_iff_ext_vanishing_iff_quotient_vanishing
    {R : Type u} [CommRing R] [Small.{v} R] [HasDerivedCategory (ModuleCat.{v} R)]
    (K : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ) :
    (HasInjectiveAmplitude K a b ↔
      ∀ (N : ModuleCat.{v} R) (i : ℤ), i < a ∨ b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) K i)) ∧
    ((∀ (N : ModuleCat.{v} R) (i : ℤ), i < a ∨ b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) K i)) ↔
      ∀ (I : Ideal R) (i : ℤ), i < a ∨ b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj
              (ModuleCat.of R (Shrink.{v} (R ⧸ I)))) K i))
```

## Tag 0EX0, an example

[Tag 0EX0](https://stacks.math.columbia.edu/tag/0EX0) in the Stacks Project.

**`StacksDraft.InjectiveDimension.dedekindDomain_ideal_projective_and_bounded_complex_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Examples.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Examples.lean#L464).

> **Stacks 0EX0.** Ideals over a Dedekind domain are finite projective. Hence cyclic modules
> have projective dimension at most one, every module has injective dimension at most one, all Ext
> groups in degrees at least two vanish, and every bounded derived object is isomorphic to the
> finite direct sum of its cohomologies placed in their degrees.

```lean
public theorem dedekindDomain_ideal_projective_and_bounded_complex_splitting
    (R : Type u) [CommRing R] [IsDedekindDomain R] [Small.{v} R] :
    (∀ I : Ideal R, Module.Finite R I ∧ Module.Projective R I) ∧
      (∀ I : Ideal R,
        HasProjectiveDimensionLE (ModuleCat.of R (Shrink.{v} (R ⧸ I))) 1) ∧
      (∀ M : ModuleCat.{v} R, HasInjectiveDimensionLE M 1) ∧
      (∀ (M N : ModuleCat.{v} R) (i : ℕ), 2 ≤ i →
        Subsingleton (Abelian.Ext M N i)) ∧
      ∀ (K : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ), K.IsGE a → K.IsLE b →
        Nonempty (K ≅ ⨁ fun i : Finset.Icc a b =>
          (DerivedCategory.singleFunctor (ModuleCat.{v} R) i.1).obj
            ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i.1).obj K))
```

## Tag 0A5U, an example

[Tag 0A5U](https://stacks.math.columbia.edu/tag/0A5U) in the Stacks Project.

**`StacksDraft.InjectiveDimension.dualNumber_residueField_infinite_injectiveDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Examples.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Examples.lean#L422).

> **Stacks 0A5U.** Let `R` be the ring of dual numbers over a field and let `M = R/(ε)`.
> Then `R` is injective as an `R`-module, `M` is quasi-isomorphic to the left-unbounded complex of
> copies of `R` whose differentials are multiplication by `ε`, and `M` has infinite injective
> dimension.

```lean
public theorem dualNumber_residueField_infinite_injectiveDimension (k : Type u) [Field k] :
    let R := DualNumber k
    let M := ModuleCat.of R (R ⧸ Ideal.span ({DualNumber.eps} : Set R))
    Module.Injective R R ∧
      (∃ (K : CochainComplex (ModuleCat R) ℤ)
          (e : ∀ (i : ℤ) (_ : i ≤ 0), K.X i ≅ ModuleCat.of R R)
          (q : K ⟶ (CochainComplex.singleFunctor (ModuleCat R) 0).obj M),
        QuasiIso q ∧
          (q.f 0 = (e 0 (by omega)).hom ≫
            ModuleCat.ofHom (Submodule.mkQ (Ideal.span ({DualNumber.eps} : Set R)))) ∧
          (∀ (i : ℤ) (hi : i < 0),
            (e i (by omega)).hom ≫ ModuleCat.ofHom (LinearMap.mulLeft R DualNumber.eps) =
              K.d i (i + 1) ≫ (e (i + 1) (by omega)).hom) ∧
          (∀ (i : ℤ), 0 < i → IsZero (K.X i))) ∧
      (∀ n : ℕ, ¬ HasInjectiveDimensionLE M n)
```

## Tag 0A5V, a lemma

[Tag 0A5V](https://stacks.math.columbia.edu/tag/0A5V) in the Stacks Project.

**`StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_of_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Criteria.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Criteria.lean#L505).

> **Stacks 0A5V.** A bounded object of the derived category of modules has finite injective
> dimension if all its cohomology modules have finite injective dimension. Likewise, a derived
> object represented by a bounded complex whose terms all have finite injective dimension has
> finite injective dimension.

```lean
public theorem hasFiniteInjectiveDimension_of_bounded
    {R : Type u} [CommRing R] [Small.{v} R] [HasDerivedCategory (ModuleCat.{v} R)]
    (K : DerivedCategory (ModuleCat.{v} R)) :
    ((∃ a b : ℤ, K.IsGE a ∧ K.IsLE b) →
      (∀ i : ℤ, ∃ n : ℕ,
        HasInjectiveDimensionLE
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K) n) →
      HasFiniteInjectiveDimension K) ∧
    (∀ (L : CochainComplex (ModuleCat.{v} R) ℤ),
      Nonempty (DerivedCategory.Q.obj L ≅ K) →
      (∃ a b : ℤ, L.IsStrictlyGE a ∧ L.IsStrictlyLE b) →
      (∀ i : ℤ, ∃ n : ℕ, HasInjectiveDimensionLE (L.X i) n) →
      HasFiniteInjectiveDimension K)
```

## Tag 0DW2, a lemma

[Tag 0DW2](https://stacks.math.columbia.edu/tag/0DW2) in the Stacks Project.

**`StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_iff_quotient_ext_vanishing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Noetherian.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Noetherian.lean#L451).

> **Stacks 0DW2.** For a bounded below complex with finite cohomology over a Noetherian ring,
> finite injective dimension can be tested by uniform high-degree Ext vanishing against the
> quotients by all ideals containing an ideal in the Jacobson radical.

```lean
public lemma hasFiniteInjectiveDimension_iff_quotient_ext_vanishing
    {R : Type u} [CommRing R] [IsNoetherianRing R] [Small.{v} R]
    (I : Ideal R) (hI : I ≤ Ideal.jacobson (⊥ : Ideal R))
    (K : DerivedCategory.Plus (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, Module.Finite R
      ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj
        (DerivedCategory.Plus.ι.obj K))) :
    HasFiniteInjectiveDimension (DerivedCategory.Plus.ι.obj K) ↔
      ∃ b : ℤ, ∀ (J : Ideal R), I ≤ J → ∀ i : ℤ, b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj
              (ModuleCat.of R (Shrink.{v} (R ⧸ J))))
            (DerivedCategory.Plus.ι.obj K) i)
```

## Tag 0AVJ, a lemma

[Tag 0AVJ](https://stacks.math.columbia.edu/tag/0AVJ) in the Stacks Project.

**`StacksDraft.InjectiveDimension.hasFiniteInjectiveDimension_iff_residueField_ext_vanishing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InjectiveDimension/Noetherian.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InjectiveDimension/Noetherian.lean#L498).

> **Stacks 0AVJ.** A bounded below complex with finite cohomology over a Noetherian local ring
> has finite injective dimension if and only if its Ext groups from the residue field vanish in all
> sufficiently high degrees.

```lean
public lemma hasFiniteInjectiveDimension_iff_residueField_ext_vanishing
    {R : Type u} [CommRing R] [IsLocalRing R] [IsNoetherianRing R] [Small.{v} R]
    (K : DerivedCategory.Plus (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, Module.Finite R
      ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj
        (DerivedCategory.Plus.ι.obj K))) :
    HasFiniteInjectiveDimension (DerivedCategory.Plus.ι.obj K) ↔
      ∃ b : ℤ, ∀ i : ℤ, b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj
              (ModuleCat.of R (Shrink.{v} (R ⧸ IsLocalRing.maximalIdeal R))))
            (DerivedCategory.Plus.ι.obj K) i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.71, Tag 0A5R](https://stacks.math.columbia.edu/tag/0A5R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
