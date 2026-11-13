---
declaration: section
origin: cited
lean: LiftAcyclic.exists_lift_acyclic_complex, StacksDraft.Perfect.exists_boundedAbove_lift_representing, StacksDraft.Perfect.exists_boundedAbove_projective_lift_representing, StacksDraft.Perfect.isPseudoCoherent_derivedExtensionScalars_iff, StacksDraft.Perfect.exists_boundedAbove_isStablyFree_lift_representing, StacksDraft.Perfect.exists_unique_boundedAbove_free_complex_representing, StacksDraft.Perfect.exists_away_bounded_free_complex_representing, StacksDraft.Perfect.exists_away_iso_biprod_trivial_complexes
statement: formalized
proof: formalized
---

# 15.77 Lifting complexes

Section 15.77 of the Stacks Project, [Tag 0BC8](https://stacks.math.columbia.edu/tag/0BC8). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BC9, a lemma

[Tag 0BC9](https://stacks.math.columbia.edu/tag/0BC9) in the Stacks Project.

**`LiftAcyclic.exists_lift_acyclic_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/LiftAcyclicComplex.lean, line 888](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/LiftAcyclicComplex.lean#L888).

> **Stacks 0BC9**.
> A bounded above acyclic complex of `R/I`-modules with terms of the form `P/IP` has a bounded
> above acyclic lift over `R` with terms satisfying `P`, whose reduction is isomorphic to the given
> complex as a complex of `R/I`-modules.

```lean
theorem exists_lift_acyclic_complex
    (P : ModuleCat.{max v u} R → Prop)
    (hPprojective : ∀ M, P M → Module.Projective R M)
    (hPcomplement : ∀ M₁ M₂, P M₁ → P (M₁ ⊞ M₂) → P M₂)
    (hPsurjective : ∀ (M₁ M₂ : ModuleCat.{max v u} R) (f : M₁ ⟶ M₂),
      P M₁ → P M₂ →
      Function.Surjective
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).map f).hom) →
      Function.Surjective f.hom)
    (E : CochainComplex (ModuleCat.{max v u} (R ⧸ I)) ℤ)
    (hbdd : ∃ b, E.IsStrictlyLE b) (hac : ∀ i, E.ExactAt i)
    (hterms : ∀ i, ∃ M, P M ∧ Nonempty
      (E.X i ≅ (ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).obj M)) :
    ∃ PC : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∀ i, P (PC.X i)) ∧ (∃ b, PC.IsStrictlyLE b) ∧
      (∀ i, PC.ExactAt i) ∧
      Nonempty
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj PC ≅ E)
```

## Tag 0BCA, a lemma

[Tag 0BCA](https://stacks.math.columbia.edu/tag/0BCA) in the Stacks Project.

**`StacksDraft.Perfect.exists_boundedAbove_lift_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Lifting.lean, line 792](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Lifting.lean#L792).

> **Stacks 0BCA.** Let `I ⊆ R` and let `P` be a class of projective `R`-modules, closed under
> finite direct sums and complementary summands, such that surjectivity modulo `I` lifts to
> surjectivity. A bounded above complex `E` of `R / I`-modules whose terms are reductions of
> modules in `P`, and which represents `K ⊗ᴸ[R] R / I`, lifts to a bounded above complex with
> terms in `P` representing `K`, provided `K` already has some such representative.

```lean
theorem exists_boundedAbove_lift_representing
    {R : Type u} [CommRing R] (I : Ideal R)
    (P : ModuleCat.{max v u} R → Prop)
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (E : CochainComplex (ModuleCat.{max v u} (R ⧸ I)) ℤ)
    (hPprojective : ∀ M, P M → Module.Projective R M)
    (hPsum : ∀ M₁ M₂, (P M₁ ∧ P (M₁ ⊞ M₂)) ↔ (P M₁ ∧ P M₂))
    (hPsurjective : ∀ (M₁ M₂ : ModuleCat.{max v u} R) (f : M₁ ⟶ M₂),
      P M₁ → P M₂ →
      Function.Surjective
          (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).map f).hom) →
        Function.Surjective f.hom)
    (hEbdd : ∃ b, E.IsStrictlyLE b)
    (hEterms : ∀ i, ∃ M, P M ∧ Nonempty
      (E.X i ≅
        (ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).obj M))
    (hErep : Nonempty
      ((DerivedCategory.Q).obj E ≅
        (totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hKrep : ∃ KC : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∀ i, P (KC.X i)) ∧ (∃ b, KC.IsStrictlyLE b) ∧
        Nonempty ((DerivedCategory.Q).obj KC ≅ K)) :
    ∃ PC : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∀ i, P (PC.X i)) ∧
      (∃ b, PC.IsStrictlyLE b) ∧
      Nonempty
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj PC ≅ E) ∧
      Nonempty ((DerivedCategory.Q).obj PC ≅ K)
```

## Tag 09AR, a lemma

[Tag 09AR](https://stacks.math.columbia.edu/tag/09AR) in the Stacks Project.

**`StacksDraft.Perfect.exists_boundedAbove_projective_lift_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/NilpotentLifting.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/NilpotentLifting.lean#L698). References: SGA 5 XV (3.Lemma1), “existence of L', v, w”.

> **Stacks 09AR.** Let `I` be a nilpotent ideal of a commutative ring `R` and let `K` be an
> object of `D(R)`. A bounded above complex `E` of projective `R ⧸ I`-modules representing
> `K ⊗ᴸ[R] R ⧸ I` lifts to a bounded above complex `P` of projective `R`-modules representing `K`,
> with `P ⊗[R] R ⧸ I` isomorphic to `E`.

```lean
public theorem exists_boundedAbove_projective_lift_representing
    {R : Type u} [CommRing R] (I : Ideal R)
    (E : CochainComplex (ModuleCat.{max v u} (R ⧸ I)) ℤ)
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (hEbdd : ∃ b : ℤ, E.IsStrictlyLE b)
    (hEprojective : ∀ i : ℤ, Module.Projective (R ⧸ I) (E.X i))
    (hErep : Nonempty
      ((DerivedCategory.Q).obj E ≅
        (totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hI : IsNilpotent I) :
    ∃ P : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∃ b : ℤ, P.IsStrictlyLE b) ∧
      (∀ i : ℤ, Module.Projective R (P.X i)) ∧
      Nonempty ((DerivedCategory.Q).obj P ≅ K) ∧
      Nonempty
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj P ≅ E)
```

## Tag 0H76, a lemma

[Tag 0H76](https://stacks.math.columbia.edu/tag/0H76) in the Stacks Project.

**`StacksDraft.Perfect.isPseudoCoherent_derivedExtensionScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/NilpotentLifting.lean, line 811](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/NilpotentLifting.lean#L811). References: SGA 6 I (2.16.2), “(i), punctual”.

> **Stacks 0H76.** Derived extension of scalars along a surjective map of commutative rings
> with nilpotent kernel preserves *and reflects* pseudo-coherence.
>
> Preservation is [stacks 0650]. Reflection is [stacks 09AR]: a bounded above finite projective
> representative of the reduction, which exists by [stacks 064U], lifts to a bounded above
> projective representative of `K`, whose terms are finite because their extensions of scalars
> are and the kernel is nilpotent.

```lean
public theorem isPseudoCoherent_derivedExtensionScalars_iff
    {R' R : Type u} [CommRing R'] [CommRing R] (f : R' →+* R)
    (hf : Function.Surjective f) (hnil : IsNilpotent (RingHom.ker f))
    (K : DerivedCategory (ModuleCat.{max v u} R')) :
    PseudoCoherence.IsPseudoCoherent
        ((totalDerivedExtensionScalars.{u, u, v} f).functor.obj K) ↔
      PseudoCoherence.IsPseudoCoherent K
```

## Tag 0BCB, a lemma

[Tag 0BCB](https://stacks.math.columbia.edu/tag/0BCB) in the Stacks Project.

**`StacksDraft.Perfect.exists_boundedAbove_isStablyFree_lift_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Lifting.lean, line 1054](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Lifting.lean#L1054).

> **Stacks 0BCB.** Let `I ⊆ R` be an ideal every element of whose coset `1 + I` is a unit. A
> bounded above complex `E` of finite stably free `R ⧸ I`-modules representing `K ⊗ᴸ[R] R ⧸ I`, for
> a pseudo-coherent object `K` of `D(R)`, lifts to a bounded above complex `P` of finite stably free
> `R`-modules representing `K` with `P ⊗[R] R ⧸ I` isomorphic to `E`. Moreover `P` is free in every
> degree in which `E` is free.

```lean
theorem exists_boundedAbove_isStablyFree_lift_representing
    {R : Type u} [CommRing R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (E : CochainComplex (ModuleCat.{max v u} (R ⧸ I)) ℤ)
    (hEbdd : ∃ b, E.IsStrictlyLE b)
    (hEterms : ∀ i, Module.Finite (R ⧸ I) (E.X i) ∧ Module.IsStablyFree (R ⧸ I) (E.X i))
    (hErep : Nonempty ((DerivedCategory.Q).obj E ≅
      (totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hI : ∀ x ∈ I, IsUnit (1 + x)) :
    ∃ P : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∀ i, Module.Finite R (P.X i) ∧ Module.IsStablyFree R (P.X i)) ∧
      (∃ b, P.IsStrictlyLE b) ∧
      Nonempty
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj P ≅ E) ∧
      Nonempty ((DerivedCategory.Q).obj P ≅ K) ∧
      (∀ i, Module.Free (R ⧸ I) (E.X i) → Module.Free R (P.X i))
```

## Tag 0BCC, a lemma

[Tag 0BCC](https://stacks.math.columbia.edu/tag/0BCC) in the Stacks Project.

**`StacksDraft.Perfect.exists_unique_boundedAbove_free_complex_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/MinimalRepresentative/LocalRing.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/MinimalRepresentative/LocalRing.lean#L558).

> **Stacks 0BCC.** Let `K` be a pseudo-coherent object of the derived category of a commutative
> local ring `R` with residue field `κ`. Its cohomology after derived extension of scalars to `κ` is
> finite dimensional in every degree and vanishes above some degree `b`. Moreover `K` is represented
> by a complex vanishing above `b` whose term in degree `i` is free of rank
> `dim_κ Hⁱ(K ⊗ᴸ_R κ)`, and any two complexes with these prescribed terms representing `K` are
> isomorphic as complexes.

```lean
theorem exists_unique_boundedAbove_free_complex_representing
    {R : Type u} [CommRing R] [IsLocalRing R]
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) :
    let k := IsLocalRing.ResidueField R
    let H := fun i : ℤ =>
      (DerivedCategory.homologyFunctor (ModuleCat.{max v u} k) i).obj
        ((totalDerivedExtensionScalars.{u, u, v} (IsLocalRing.residue R)).functor.obj K)
    let IsModel := fun P : CochainComplex (ModuleCat.{max v u} R) ℤ =>
      (∀ i, Nonempty (P.X i ≅
        ModuleCat.of R (ULift.{v} (Fin (Module.finrank k (H i)) → R)))) ∧
      Nonempty ((DerivedCategory.Q).obj P ≅ K)
    (∀ i, Module.Finite k (H i)) ∧
      ∃ b : ℤ, (∀ i, b < i → IsZero (H i)) ∧
        ∃ P : CochainComplex (ModuleCat.{max v u} R) ℤ,
          P.IsStrictlyLE b ∧ IsModel P ∧
            ∀ F G, IsModel F → IsModel G → Nonempty (F ≅ G)
```

## Tag 0BCD, a lemma

[Tag 0BCD](https://stacks.math.columbia.edu/tag/0BCD) in the Stacks Project.

**`StacksDraft.Perfect.exists_away_bounded_free_complex_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/MinimalRepresentative/PrincipalNeighbourhood.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/MinimalRepresentative/PrincipalNeighbourhood.lean#L322).

> **Stacks 0BCD.** Let `R` be a commutative ring, `p` a prime of `R` and `K` a perfect object of
> `D(R)`. The dimensions `dᵢ = dim_{κ(p)} Hⁱ(K ⊗ᴸ_R κ(p))` are finite and only finitely many of them
> are nonzero, and there is an `f ∈ R` outside `p` together with a strictly bounded complex over
> `R_f` whose term in degree `i` is free of rank exactly `dᵢ` and which represents
> `K ⊗ᴸ_R R_f`.

```lean
theorem exists_away_bounded_free_complex_representing
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max v u} R)) (hK : IsPerfect K) :
    let k := p.ResidueField
    let H := fun i : ℤ =>
      (DerivedCategory.homologyFunctor (ModuleCat.{max v u} k) i).obj
        ((totalDerivedExtensionScalars.{u, u, v} (algebraMap R k)).functor.obj K)
    (∀ i, Module.Finite k (H i)) ∧
      {i | Module.finrank k (H i) ≠ 0}.Finite ∧
      ∃ f : R, f ∉ p ∧
        ∃ (P : CochainComplex (ModuleCat.{max v u} (Localization.Away f)) ℤ) (a b : ℤ),
          P.IsStrictlyGE a ∧ P.IsStrictlyLE b ∧
            (∀ i, Nonempty (P.X i ≅ ModuleCat.of (Localization.Away f)
              (ULift.{v} (Fin (Module.finrank k (H i)) → Localization.Away f)))) ∧
            Nonempty ((DerivedCategory.Q).obj P ≅
              (totalDerivedExtensionScalars.{u, u, v}
                (algebraMap R (Localization.Away f))).functor.obj K)
```

## Tag 0F9V, a lemma

[Tag 0F9V](https://stacks.math.columbia.edu/tag/0F9V) in the Stacks Project.

**`StacksDraft.Perfect.exists_away_iso_biprod_trivial_complexes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/MinimalRepresentative/TrivialSummands.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/MinimalRepresentative/TrivialSummands.lean#L595).

> **Stacks 0F9V.** Two bounded complexes of finite projective modules representing
> isomorphic derived objects become isomorphic as complexes over some principal localization,
> after adjoining finite direct sums of trivial two-term complexes on both sides.

```lean
theorem exists_away_iso_biprod_trivial_complexes
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (M N : CochainComplex (ModuleCat.{max v u} R) ℤ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hNbounded : ∃ a b : ℤ, N.IsStrictlyGE a ∧ N.IsStrictlyLE b)
    (hMterms : ∀ i, Module.Finite R (M.X i) ∧ Projective (M.X i))
    (hNterms : ∀ i, Module.Finite R (N.X i) ∧ Projective (N.X i))
    (hMN : Nonempty ((DerivedCategory.Q).obj M ≅ (DerivedCategory.Q).obj N)) :
    ∃ f : R, f ∉ p ∧
      let S := Localization.Away f
      let F := (ModuleCat.extendScalars.{u, u, max v u} (algebraMap R S)).mapHomologicalComplex
        (ComplexShape.up ℤ)
      let IsTrivialSum := fun P : CochainComplex (ModuleCat.{max v u} S) ℤ =>
        ∃ (n : ℕ) (degree : Fin n → ℤ),
          Nonempty (P ≅ ∏ᶜ fun j => CochainComplex.mappingCone
            (𝟙 ((CochainComplex.singleFunctor (ModuleCat.{max v u} S) (degree j)).obj
              (ModuleCat.of S (ULift.{v} S)))))
      ∃ P Q : CochainComplex (ModuleCat.{max v u} S) ℤ,
        IsTrivialSum P ∧ IsTrivialSum Q ∧ Nonempty (F.obj M ⊞ P ≅ F.obj N ⊞ Q)
```

## Tag 0BCE, a lemma

[Tag 0BCE](https://stacks.math.columbia.edu/tag/0BCE) in the Stacks Project.

**`StacksDraft.Perfect.exists_boundedAbove_finiteProjective_lift_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/NilpotentLifting.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/NilpotentLifting.lean#L267).

> **Stacks 0BCE.** Let `(R, I)` be a henselian pair and let `K` be a pseudo-coherent object of
> `D(R)`. A bounded above complex `E` of finite projective `R ⧸ I`-modules representing
> `K ⊗ᴸ[R] R ⧸ I` lifts to a bounded above complex `P` of finite projective `R`-modules
> representing `K` with `P ⊗[R] R ⧸ I` isomorphic to `E`. Moreover `P` is free in every degree in
> which `E` is free.

```lean
theorem exists_boundedAbove_finiteProjective_lift_representing
    {R : Type u} [CommRing R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (E : CochainComplex (ModuleCat.{max v u} (R ⧸ I)) ℤ)
    (hEbdd : ∃ b, E.IsStrictlyLE b)
    (hEterms : ∀ i,
      Module.Finite (R ⧸ I) (E.X i) ∧ Module.Projective (R ⧸ I) (E.X i))
    (hErep : Nonempty
      ((DerivedCategory.Q).obj E ≅
        (totalDerivedExtensionScalars.{u, u, v} (Ideal.Quotient.mk I)).functor.obj K))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hI : HenselianPair R I) :
    ∃ P : CochainComplex (ModuleCat.{max v u} R) ℤ,
      (∀ i, Module.Finite R (P.X i) ∧ Module.Projective R (P.X i)) ∧
      (∃ b, P.IsStrictlyLE b) ∧
      Nonempty
        (((ModuleCat.extendScalars.{u, u, max v u} (Ideal.Quotient.mk I)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj P ≅ E) ∧
      Nonempty ((DerivedCategory.Q).obj P ≅ K) ∧
      (∀ i, Module.Free (R ⧸ I) (E.X i) → Module.Free R (P.X i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.77, Tag 0BC8](https://stacks.math.columbia.edu/tag/0BC8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
