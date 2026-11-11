---
declaration: section
origin: cited
lean: Stacks.Thickenings.isPseudoCoherent_of_derivedPullback, Stacks.Thickenings.isQuasicoherent_homology_of_isPseudoCoherent_derivedPullback_specMap, Stacks.Thickenings.isPseudoCoherent_of_isPullback_of_isFiniteOrderThickening, Stacks.Thickenings.isRelativelyPerfect_of_isPullback_of_isFiniteOrderThickening, AlgebraicGeometry.Scheme.Hom.exists_finset_affineOpens_mvPolynomial_surjective_chartHom_of_universallyClosed, AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_of_isPerfectRelativeTo_closedFibre_of_genuine, AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_canonical_of_closedFibre, AlgebraicGeometry.exists_specializes_mem_range_pullback_snd_quotientMk
statement: formalized
proof: formalized
---

# 37.71 Relatively perfect objects

Section 37.71 of the Stacks Project, [Tag 0DJW](https://stacks.math.columbia.edu/tag/0DJW). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DJX, a lemma

[Tag 0DJX](https://stacks.math.columbia.edu/tag/0DJX) in the Stacks Project.

**`Stacks.Thickenings.isPseudoCoherent_of_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Thickening.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Thickening.lean#L154). The attribute's comment: “the whole statement, unconditionally: pseudo-coherence of K' in D(𝒪\_\{X'}) from pseudo-coherence of Li^*K', for a finite-order thickening i : X ⟶ X' of schemes, at the standard derived category”. References: SGA 6 I (2.16.2), “(i), special case”.

> **Pseudo-coherence descends along a finite-order thickening of schemes.** Let `i : X ⟶ X'` be
> a closed immersion whose kernel ideal sheaf is nilpotent and let `K'` be an object of `D(𝒪_{X'})`
> such that `K = Li^*K'` is pseudo-coherent. Then `K'` is pseudo-coherent.
>
> Pseudo-coherence of `K'` is a local condition on `X'`, so it is enough to produce it over an
> affine open `U` of `X'`. Over the chart `Spec Γ(X', U)` the thickening becomes `Spec` of the
> surjection `i.app U`, whose kernel is nilpotent because a power of the kernel ideal sheaf
> vanishes; the hypothesis travels to that chart because derived pullback preserves
> pseudo-coherence and the two ways around the square `Spec Γ(X', U) ← Spec Γ(X, i⁻¹U)` over `i`
> agree. The affine case then applies, and its conclusion comes back to `U` along
> `AlgebraicGeometry.IsAffineOpen.isoSpec`, again by preservation of pseudo-coherence under derived
> pullback, this time along the inverse.

```lean
theorem isPseudoCoherent_of_derivedPullback {X X' : Scheme.{u}} (i : X ⟶ X')
    (hi : IsFiniteOrderThickening i)
    (K' : DerivedCategory (OXMod.{u, u} X'.toRingedSpace))
    (hK : AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := X.toRingedSpace)
      ((derivedPullback i.toLRSHom.toShHom).obj K')) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := X'.toRingedSpace) K'
```

**`Stacks.Thickenings.isQuasicoherent_homology_of_isPseudoCoherent_derivedPullback_specMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/ThickeningQuasicoherent.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/ThickeningQuasicoherent.lean#L530). The attribute's comment: “the quasi-coherence of the cohomology, in the affine case”.

> **The quasi-coherence half of [Stacks, Tag 0DJX] in the affine case.** Let `f : R ⟶ S` be a
> surjection of commutative rings with nilpotent kernel, so that `i = Spec f` is a finite-order
> thickening, and let `A` be an object of `D(𝒪_{Spec R})` whose derived pullback `Li^*A` is
> pseudo-coherent. Then every cohomology sheaf of `A` is quasi-coherent, that is, `A` lies in
> `D_QCoh(𝒪_{Spec R})`.
>
> This is the first paragraph of the source's proof. The dévissage is on the kernel ideal
> `I = ker f`: writing `P` for the property of an `R`-module `N` that `Ñ[0] ⊗ᴸ_{𝒪_{Spec R}} A` has
> quasi-coherent cohomology, `Stacks.Thickenings.prop_of_isNilpotent_of_smul_eq_bot` reduces `P` for
> every module — in particular for `R` itself, where the unit of the derived tensor product
> identifies `𝒪_{Spec R}[0] ⊗ᴸ A` with `A` — to `P` for a module annihilated by `I`.
>
> *The inductive step.* `P` is stable under extensions: a short exact sequence of `R`-modules
> becomes a short exact sequence of `𝒪_{Spec R}`-modules, `M ↦ M̃` being exact
> (`AlgebraicGeometry.tilde.preservesFiniteLimits`), hence a distinguished triangle
> (`CategoryTheory.ShortComplex.ShortExact.singleTriangle_distinguished`); the derived tensor
> product is exact in its left variable, so tensoring with `A` keeps the triangle distinguished;
> and the quasi-coherent modules form a weak Serre subcategory ([Stacks, Tag 01LA]), so the middle
> vertex of a distinguished triangle whose outer vertices lie in `D_QCoh` lies in `D_QCoh`.
>
> *The base case.* A module `N` annihilated by `I` is the restriction of scalars of an `S`-module
> `M` (`Stacks.Thickenings.exists_restrictScalars_iso_of_smul_eq_bot`), and then
> `Ñ ≅ i_*(M̃)` (`Stacks.Descent.restrictScalarsCompTildeIso`). The projection formula for the
> closed embedding `i`, in the form
> `exists_iso_derivedPushforward_derivedTensor_obj`, produces `D` in `D(𝒪_{Spec S})` with
> `i_*(M̃)[0] ⊗ᴸ_{𝒪_{Spec R}} A ≅ Ri_*D` and `D ≅ M̃[0] ⊗ᴸ_{𝒪_{Spec S}} Li^*A`; the second
> factor of the latter is in `D_QCoh(𝒪_{Spec S})` by [Stacks, Tag 08E5], the first because `M̃` is
> quasi-coherent, so `D` is by [Stacks, Tag 08DX] in the form
> `isQuasicoherent_homology_specDerivedTensor`, and `Ri_*D` is by [Stacks, Tag 08D5].
>
> Note that `i_* = Ri_*` here, which is `derivedPushforwardQIsoOfIsClosedEmbedding`, and that no
> identification of the isomorphism with the canonical projection-formula morphism of
> [Stacks, Tag 0B53] is needed: only membership in `D_QCoh` is transported.

```lean
public theorem isQuasicoherent_homology_of_isPseudoCoherent_derivedPullback_specMap
    (hf : Function.Surjective f.hom) (hnil : IsNilpotent (RingHom.ker f.hom))
    (A : DerivedCategory (StrictlyPerfect.OXMod.{u, u} (Spec R).toRingedSpace))
    (hA : AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := (Spec S).toRingedSpace)
      ((derivedPullback (Spec.map f).toLRSHom.toShHom).obj A)) :
    ∀ n : ℤ, ((DerivedCategory.homologyFunctor (Spec R).Modules n).obj A).IsQuasicoherent
```

## Tag 0DJY, a lemma

[Tag 0DJY](https://stacks.math.columbia.edu/tag/0DJY) in the Stacks Project.

**`Stacks.Thickenings.isPseudoCoherent_of_isPullback_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectThickening.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectThickening.lean#L535). The attribute's comment: “the pseudo-coherence conjunct of the conclusion; the Tor-dimension conjunct is not proved — see the implementation notes of this module”.

> **The pseudo-coherence conjunct of Stacks 0DJY.** In a cartesian diagram of schemes with
> `i : X ⟶ X'`, `f : X ⟶ Y`, `f' : X' ⟶ Y'` and `j : Y ⟶ Y'`, with `j` a finite-order thickening,
> an object `E'` of `D(𝒪_{X'})` whose derived pullback `Li^*E'` is pseudo-coherent is itself
> pseudo-coherent.
>
> A base change of a finite-order thickening is a finite-order thickening (Stacks 09ZU), so `i` is
> one, and the conclusion is Stacks 0DJX. Neither flatness nor local finite presentation of `f'` is
> used, and the family of derived tensor products plays no role, so neither appears.
>
> This is the first of the two conjuncts of the conclusion of Stacks 0DJY. The second, locally
> finite Tor dimension over `f'^{-1}𝒪_{Y'}`, is not proved here; its local content is
> `Stacks.Thickenings.hasTorAmplitudeCanonical_derivedStalk_of_isPullback` above, and what is
> missing between the two is recorded in the implementation notes of this file.

```lean
public theorem isPseudoCoherent_of_isPullback_of_isFiniteOrderThickening
    {X X' Y Y' : Scheme.{u}} (i : X ⟶ X') (f : X ⟶ Y) (f' : X' ⟶ Y') (j : Y ⟶ Y')
    (hpb : IsPullback i f f' j) (hj : IsFiniteOrderThickening j)
    (E' : DerivedCategory (OXMod.{u, u} X'.toRingedSpace))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace)
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        i.toLRSHom.toShHom).obj E')) :
    RingedSpace.IsPseudoCoherent (X := X'.toRingedSpace) E'
```

**`Stacks.Thickenings.isRelativelyPerfect_of_isPullback_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectThickeningTorDimension.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectThickeningTorDimension.lean#L252).

> **Stacks 0DJY at the canonical derived tensor products.** Consider a cartesian diagram of
> schemes with `i : X ⟶ X'`, `f : X ⟶ Y`, `f' : X' ⟶ Y'` and `j : Y ⟶ Y'`, in which `f'` is flat and
> locally of finite presentation and `j` is a finite-order thickening. Let `E'` be an object of
> `D(𝒪_{X'})`. If `E = Li^*E'` is `Y`-perfect, then `E'` is `Y'`-perfect, relative perfectness being
> `AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect` — Stacks 0DI0 read at the canonical derived
> tensor products — on both sides.

```lean
public theorem isRelativelyPerfect_of_isPullback_of_isFiniteOrderThickening
    {X X' Y Y' : Scheme.{u}} {i : X ⟶ X'} {f : X ⟶ Y} {f' : X' ⟶ Y'} {j : Y ⟶ Y'}
    (hpb : IsPullback i f f' j) (hj : IsFiniteOrderThickening j)
    [Flat f'] [LocallyOfFinitePresentation f']
    (E' : DerivedCategory (OXMod.{u, u} X'.toRingedSpace)) :
    haveI : Flat f := MorphismProperty.of_isPullback (P := @Flat) hpb inferInstance
    haveI : LocallyOfFinitePresentation f :=
      MorphismProperty.of_isPullback (P := @LocallyOfFinitePresentation) hpb inferInstance
    f.IsRelativelyPerfect
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          i.toLRSHom.toShHom).obj E') →
      f'.IsRelativelyPerfect E'
```

## Tag 0DJZ, a lemma

[Tag 0DJZ](https://stacks.math.columbia.edu/tag/0DJZ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.exists_finset_affineOpens_mvPolynomial_surjective_chartHom_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonChart.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonChart.lean#L184). The attribute's comment: “the covering step with which the proof opens: for `f : X ⟶ Spec R` universally closed and locally of finite type, finitely many affine opens cover `X` and the sections over each are a quotient of a polynomial algebra over `R` in finitely many variables”. References: EGA I (6.6.3), “special case”; EGA IV (1.5.1), “(a) ⇒ (c), special case”.

> **The covering step of Stacks 0DJZ.** Let `R` be a ring and let `f : X ⟶ Spec R` be
> universally closed and locally of finite type. Then finitely many affine opens cover `X`, and over
> each the sections are a quotient of a polynomial algebra `R[x_1, …, x_d]` in finitely many
> variables, compatibly with the structure map that `f` induces.
>
> The source's proof of Stacks 0DJZ opens with this: *choose a finite affine open covering
> `X = U_1 ∪ … ∪ U_n`; for each `i` we can choose a closed immersion `U_i → 𝐀^{d_i}_S`*. For an
> affine `U_i`, giving a closed immersion into `𝐀^{d_i}_S` over `S` is the same as giving a
> surjection `R[x_1, …, x_{d_i}] ⟶ Γ(X, U_i)` of `R`-algebras, and the surjection is the form the
> fibrewise criterion of Stacks 0DJH consumes, so it is the form exported here.
>
> Quasi-compactness of `X` comes from universal closedness of `f`: the import
> `Mathlib.AlgebraicGeometry.Morphisms.UniversallyClosed` carries an instance making a universally
> closed morphism quasi-compact, and `Spec R` is quasi-compact, so
> `AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace` applies. Properness is not asked
> for; universal closedness and local finite type are all the source's proof of this step uses, and
> they are also the hypotheses under which the sibling module
> `StacksFrontier.AlgebraicGeometry.Perfect.RelativelyPerfectJacobsonSpecialization` proves the
> specialization step.

```lean
public theorem exists_finset_affineOpens_mvPolynomial_surjective_chartHom_of_universallyClosed
    [LocallyOfFiniteType f] [UniversallyClosed f] :
    ∃ s : Finset X.affineOpens, (⨆ V ∈ s, (V : X.Opens)) = ⊤ ∧
      ∀ V ∈ s, ∃ (d : ℕ) (ψ : MvPolynomial (Fin d) R →+* Γ(X, V.1)),
        Function.Surjective ψ ∧ ψ.comp MvPolynomial.C = chartHom f V.1
```

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_of_isPerfectRelativeTo_closedFibre_of_genuine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonDescent.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonDescent.lean#L218).

> **Stacks 0DJZ.** Let `R` be a ring and `I` an ideal contained in its Jacobson radical; set
> `S = Spec R` and `S₀ = Spec (R/I)`. Let `f : X ⟶ S` be proper, flat and locally of finite
> presentation and let `X₀ = S₀ ×_S X`. Let `E` be a pseudo-coherent object of `D(𝒪_X)`. If the
> derived restriction `E₀` of `E` to `X₀` is `S₀`-perfect, then `E` is `S`-perfect.
>
> Relative perfectness is read at families of certified derived tensor products on the open
> subspaces of the inverse-image ringed spaces, pinned to the tensor product of sheaves of modules,
> which is the tensor product of the source's definition.

```lean
theorem isPerfectRelativeTo_of_isPerfectRelativeTo_closedFibre_of_genuine [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] (hI : I ≤ (⊥ : Ideal R).jacobson)
    (D : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage (Spec (CommRingCat.of R)).toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{u + 1, u}
        ((RingedSpace.inverseImage (Spec (CommRingCat.of R)).toRingedSpace f.base).restrict
          U.isOpenEmbedding))
    (hD : IsGenuineRelativeTensorFamily f D)
    (D₀ : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage (Spec (CommRingCat.of (R ⧸ I))).toRingedSpace
          (closedFibreToBase f I).base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{u + 1, u}
        ((RingedSpace.inverseImage (Spec (CommRingCat.of (R ⧸ I))).toRingedSpace
          (closedFibreToBase f I).base).restrict U.isOpenEmbedding))
    (hD₀ : IsGenuineRelativeTensorFamily (closedFibreToBase f I) D₀)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (hE₀ : (closedFibreToBase f I).IsPerfectRelativeTo D₀
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (closedFibreToTotal f I).toLRSHom.toShHom).obj E)) :
    f.IsPerfectRelativeTo D E
```

**`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_canonical_of_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonDescent.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonDescent.lean#L249).

> **Stacks 0DJZ at the canonical derived tensor products.** Let `R` be a ring and `I` an ideal
> contained in its Jacobson radical; set `S = Spec R` and `S₀ = Spec (R/I)`. Let `f : X ⟶ S` be
> proper, flat and locally of finite presentation and let `X₀ = S₀ ×_S X`. Let `E` be a
> pseudo-coherent object of `D(𝒪_X)`. If the derived restriction `E₀` of `E` to `X₀` is
> `S₀`-perfect, then `E` is `S`-perfect, relative perfectness being read at the canonical derived
> tensor products on both sides.

```lean
theorem isPerfectRelativeTo_canonical_of_closedFibre [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] (hI : I ≤ (⊥ : Ideal R).jacobson)
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (hE₀ : (closedFibreToBase f I).IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage (Spec (CommRingCat.of (R ⧸ I))).toRingedSpace
          (closedFibreToBase f I).base))
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (closedFibreToTotal f I).toLRSHom.toShHom).obj E)) :
    f.IsPerfectRelativeTo
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage (Spec (CommRingCat.of R)).toRingedSpace f.base)) E
```

**`AlgebraicGeometry.exists_specializes_mem_range_pullback_snd_quotientMk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonSpecialization.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectJacobsonSpecialization.lean#L111). The attribute's comment: “the specialization step of the proof: universal closedness of `f` and `I` inside the Jacobson radical force every point of `X` to specialize to a point of `X₀ = Spec (R/I) ×_{Spec R} X`”.

> **Stacks 0DJZ, the specialization step.** Let `I` be an ideal of `R` contained in the
> Jacobson radical, let `f : X ⟶ Spec R` be universally closed and let
> `X₀ = Spec (R/I) ×_{Spec R} X`. Then every point of `X` specializes to a point lying in the
> image of `X₀ ⟶ X`.

```lean
public theorem exists_specializes_mem_range_pullback_snd_quotientMk
    {R : Type u} [CommRing R] {X : Scheme.{u}} (f : X ⟶ Spec (CommRingCat.of R))
    [UniversallyClosed f] {I : Ideal R} (hI : I ≤ (⊥ : Ideal R).jacobson) (x : X) :
    ∃ x₀ : X, x ⤳ x₀ ∧ x₀ ∈
      Set.range (pullback.snd (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) f).base
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.71, Tag 0DJW](https://stacks.math.columbia.edu/tag/0DJW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
