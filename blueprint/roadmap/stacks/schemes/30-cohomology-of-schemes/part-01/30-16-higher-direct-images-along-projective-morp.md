---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProperAmpleCohomology.exists_epi_biproduct_tensorPowModule, Stacks.AlgebraicGeometry.ProperAmpleCohomology.exists_isZero_Hgroup_tensorPowTwist, Stacks.AlgebraicGeometry.ProperAmpleCohomology.coherent_proper_ample, Stacks.AlgebraicGeometry.ProperAmpleCohomology.moduleFinite_cohomology, Stacks.AlgebraicGeometry.AmpleTwistAcyclicity.exists_isZero_rightDerivedPlus_pushforward_tensorPowModule, AlgebraicGeometry.LocallyProjectiveCoherentImage.isCoherent_rightDerived_of_isLocallyProjective
statement: formalized
proof: formalized
---

# 30.16 Higher direct images along projective morphisms

Section 30.16 of the Stacks Project, [Tag 0B5S](https://stacks.math.columbia.edu/tag/0B5S). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B5T, a lemma

[Tag 0B5T](https://stacks.math.columbia.edu/tag/0B5T) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperAmpleCohomology.exists_epi_biproduct_tensorPowModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/Basic.lean#L67). The attribute's comment: “clause (2), the surjection from a finite direct sum of tensor powers; clauses (1), (3), (4) and (5) are not covered”.

> Let `f : X ⟶ S` be proper with `S` Noetherian, let `ℒ` be an ample invertible `𝒪_X`-module
> and let `ℱ` be a coherent `𝒪_X`-module. Then there are a finite index type `ι`, exponents
> `d : ι → ℤ` and a surjection `⨁_{j ∈ ι} ℒ ^⊗ dⱼ ↠ ℱ`.

```lean
theorem exists_epi_biproduct_tensorPowModule {X S : Scheme.{u}} (f : X ⟶ S)
    [AlgebraicGeometry.IsNoetherian S] [IsProper f] (F L : X.Modules)
    [_root_.SheafOfModules.IsCoherent F]
    [IsInvertibleModule X L] (hL : IsAmple X L) :
    ∃ (ι : Type u) (_ : Finite ι) (d : ι → ℤ)
      (b : Bicone fun j : ι => tensorPowModule X L (d j)) (_ : b.IsBilimit)
      (p : b.pt ⟶ F), Epi p
```

**`Stacks.AlgebraicGeometry.ProperAmpleCohomology.exists_isZero_Hgroup_tensorPowTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/Basic.lean#L84). The attribute's comment: “clause (4), the eventual vanishing of the higher cohomology of the high twists of a coherent module, with one exponent serving every positive degree”.

> Let `R` be a Noetherian ring, let `f : X ⟶ Spec R` be proper, let `ℒ` be an ample invertible
> `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module. Then there is a `d₀` with
>
> `H ᵖ(X, ℱ ⊗ ℒ ^⊗ d) = 0` for every `d ≥ d₀` and every `p > 0`.

```lean
theorem exists_isZero_Hgroup_tensorPowTwist {X : Scheme.{u}} {R : Type u}
    [CommRing R] [IsNoetherianRing R] (f : X ⟶ Spec (CommRingCat.of R)) [IsProper f]
    (F L : X.Modules) [_root_.SheafOfModules.IsCoherent F] [IsInvertibleModule X L]
    (hL : IsAmple X L) :
    ∃ d₀ : ℕ, ∀ d p : ℕ, d₀ ≤ d → 0 < p →
      IsZero (Hgroup X.ringCatSheaf ⊤ p
        (Stacks.RelativeVeryAmple.tensorModules X F (tensorPowModule X L (d : ℤ))))
```

**`Stacks.AlgebraicGeometry.ProperAmpleCohomology.coherent_proper_ample`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/CoherentProperAmple.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/CoherentProperAmple.lean#L112). The attribute's comment: “all five clauses: the section ring is a finitely generated R-algebra, a finite direct sum of tensor powers of L surjects onto F, the cohomology of F is a finite R-module in every degree, the higher cohomology of the high twists of F vanishes, and the graded module of twisted sections in degrees at least k is a finite module over the section ring”.

> **[Stacks, Tag 0B5T].** Let `R` be a Noetherian ring, let `f : X ⟶ Spec R` be proper, let `ℒ`
> be an ample invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module. Then all five of the
> tag's assertions hold:
>
> 1. the graded ring `A = ⨁_{d ≥ 0} H⁰(X, ℒ ^⊗ d)` is a finitely generated `R`-algebra;
> 2. there are a finite index type `ι`, exponents `d : ι → ℤ` and a surjection
>    `⨁_{j ∈ ι} ℒ ^⊗ dⱼ ↠ ℱ`;
> 3. `H ᵖ(X, ℱ)` is a finite `R`-module for every `p`;
> 4. there is a `d₀` with `H ᵖ(X, ℱ ⊗ ℒ ^⊗ d) = 0` for every `d ≥ d₀` and every `p > 0`;
> 5. for every `k ∈ ℤ` the graded `A`-module `⨁_{d ≥ k} H⁰(X, ℱ ⊗ ℒ ^⊗ d)` is a finite `A`-module.
>
> See the module documentation for the spelling of each clause. The five components are
> `ringHomFiniteType_sectionRing`, `exists_epi_biproduct_tensorPowModule_of_isAmple`,
> `moduleFinite_cohomology_of_isProper`, `exists_isZero_Hgroup_tensorPowTwist` and
> `moduleFinite_twistModule`.

```lean
theorem coherent_proper_ample {X : Scheme.{u}} {R : Type u} [CommRing R] [IsNoetherianRing R]
    (f : X ⟶ Spec (CommRingCat.of R)) [IsProper f] (F L : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.Ample.IsAmple X L) :
    RingHom.FiniteType
        ((sectionRingZeroHom X L).comp (specAlgebraRingHom R f)) ∧
      (∃ (ι : Type u) (_ : Finite ι) (d : ι → ℤ)
        (b : Bicone fun j : ι => Stacks.Ample.tensorPowModule X L (d j)) (_ : b.IsBilimit)
        (p : b.pt ⟶ F), Epi p) ∧
      (∀ p : ℕ, Module.Finite R
        ((ModuleCat.restrictScalars (specAlgebraRingHom R f)).obj (cohomologyOf X p F))) ∧
      (∃ d₀ : ℕ, ∀ d p : ℕ, d₀ ≤ d → 0 < p →
        IsZero (Hgroup X.ringCatSheaf ⊤ p
          (Stacks.RelativeVeryAmple.tensorModules X F
            (Stacks.Ample.tensorPowModule X L (d : ℤ))))) ∧
      (∀ k : ℤ, Module.Finite (sectionRing L)
        (twistModule (F ⊗ Stacks.Ample.tensorPowModule X L k) L))
```

**`Stacks.AlgebraicGeometry.ProperAmpleCohomology.moduleFinite_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/CohomologyFinite.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperAmpleCohomology/CohomologyFinite.lean#L95). The attribute's comment: “clause (3), the finiteness of the cohomology of a coherent module over the Noetherian base ring”.

> **Clause (3) of [Stacks, Tag 0B5T].** Let `R` be a Noetherian ring, let `f : X ⟶ Spec R` be
> proper, let `ℒ` be an ample invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module. Then
> `Hᵖ(X, ℱ)` is a finite `R`-module for every `p`.
>
> This is `moduleFinite_cohomology_of_isProper` with the tag's remaining hypotheses bound; the
> ample invertible module is not used, and the more general statement is the one to apply. The
> tag's clause (3) is recorded here so that it sits on a declaration stating the clause in the
> tag's own setting.

```lean
theorem moduleFinite_cohomology {X : Scheme.{u}} {R : Type u} [CommRing R] [IsNoetherianRing R]
    (f : X ⟶ Spec (CommRingCat.of R)) [IsProper f] (F L : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [IsInvertibleModule X L] (_hL : IsAmple X L) (p : ℕ) :
    Module.Finite R ((ModuleCat.restrictScalars (specAlgebraRingHom R f)).obj
      (cohomologyOf X p F))
```

## Tag 02O1, a lemma

[Tag 02O1](https://stacks.math.columbia.edu/tag/02O1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AmpleTwistAcyclicity.exists_isZero_rightDerivedPlus_pushforward_tensorPowModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleTwistAcyclicity/Basic.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleTwistAcyclicity/Basic.lean#L350).

> **[Stacks, Tag 02O1], with no hypothesis.** Let `f : X ⟶ S` be a proper morphism of schemes
> with `S` Noetherian, let `ℱ` be a coherent `𝒪_X`-module and let `ℒ` be an invertible
> `𝒪_X`-module ample relative to `f`. Then there is an `n₀` such that for all `n ≥ n₀`,
>
> `R ᵖ f_* (ℱ ⊗ ℒ ^⊗ n) = 0` for every `p > 0`,
>
> with the **one** bound `n₀` serving every positive degree.
>
> This is
> `Stacks.AlgebraicGeometry.RelativeAmpleTwistVanishing`
> `.exists_isZero_rightDerivedPlus_pushforward_tensorPowModule` with its hypothesis `haffine`
> discharged by `vanishingOverAffineBase`.

```lean
theorem exists_isZero_rightDerivedPlus_pushforward_tensorPowModule {X S : Scheme.{u}} (f : X ⟶ S)
    [AlgebraicGeometry.IsNoetherian S] [IsProper f] (F L : X.Modules) [F.IsCoherent]
    [IsInvertibleModule X L] (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    ∃ n₀ : ℕ, ∀ n p : ℕ, n₀ ≤ n → 0 < p →
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus (p : ℤ)).obj
        (tensorModules X F (tensorPowModule X L (n : ℤ))))
```

## Tag 02O4, a lemma

[Tag 02O4](https://stacks.math.columbia.edu/tag/02O4) in the Stacks Project.

**`AlgebraicGeometry.LocallyProjectiveCoherentImage.isCoherent_rightDerived_of_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocallyProjectiveCoherentImage/Basic.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocallyProjectiveCoherentImage/Basic.lean#L155).

> **[Stacks, Tag 02O4].** For `S` locally Noetherian, `f : X ⟶ S` locally H-projective and `ℱ`
> a coherent `𝒪_X`-module, the higher direct image `R^i f_* ℱ` is coherent for every `i ≥ 0`.
>
> Local H-projectivity supplies an open cover of `S` over whose members `f` is H-projective — the
> definition states this for `pullback.snd f (𝒰.f i)`, which is isomorphic as an arrow to
> `f ∣_ (𝒰.f i).opensRange` — and coherence of a higher direct image is local on the base.

```lean
theorem isCoherent_rightDerived_of_isLocallyProjective {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] (hf : IsLocallyProjectiveMorphism f) (F : X.Modules)
    (hF : F.IsCoherent) (i : ℕ) :
    (((Scheme.Modules.pushforward f).rightDerived i).obj F).IsCoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.16, Tag 0B5S](https://stacks.math.columbia.edu/tag/0B5S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
