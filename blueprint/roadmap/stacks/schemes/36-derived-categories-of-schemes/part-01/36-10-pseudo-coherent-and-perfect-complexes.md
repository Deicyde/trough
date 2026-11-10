---
declaration: section
origin: cited
lean: AlgebraicGeometry.isQuasicoherent_homology_of_isPseudoCoherentFrom, AlgebraicGeometry.exists_local_epi_homology_of_isPseudoCoherentFrom, AlgebraicGeometry.isQuasicoherentDerived_of_isPseudoCoherent, AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_tilde_iff, AlgebraicGeometry.RingedSpace.isPseudoCoherent_tilde_iff, AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_tilde_iff_locallySmall, AlgebraicGeometry.RingedSpace.isPseudoCoherent_tilde_iff_locallySmall, Stacks.AffineTilde.isPseudoCoherentFrom_of_isPseudoCoherentFrom_tildeComplex
statement: formalized
proof: formalized
---

# 36.10 Pseudo-coherent and perfect complexes

Section 36.10 of the Stacks Project, [Tag 08E4](https://stacks.math.columbia.edu/tag/08E4). 9 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08E5, a lemma

[Tag 08E5](https://stacks.math.columbia.edu/tag/08E5) in the Stacks Project.

**`AlgebraicGeometry.isQuasicoherent_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean#L133). The attribute's comment: “cohomology above m”.

> Let `X` be a scheme and let `E` be an `m`-pseudo-coherent object of `D(𝒪_X)`. Then the
> cohomology sheaf `H^i(E)` is a quasi-coherent `𝒪_X`-module for every `i > m`.

```lean
public theorem isQuasicoherent_homology_of_isPseudoCoherentFrom (X : Scheme.{u})
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace)]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace)) (m i : ℤ)
    (hE : RingedSpace.IsPseudoCoherentFrom (X := X.toRingedSpace) E m) (hi : m < i) :
    ((DerivedCategory.homologyFunctor
      (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace) i).obj E).IsQuasicoherent
```

**`AlgebraicGeometry.exists_local_epi_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean#L176). The attribute's comment: “cohomology in degree m, locally”.

> Let `X` be a scheme and let `E` be an `m`-pseudo-coherent object of `D(𝒪_X)`. Then every point
> of `X` has an open neighbourhood `U` on which `H^m(E)` is a quotient of a quasi-coherent
> `𝒪_U`-module.
>
> **Stacks erratum.** The source states this clause globally — that `H^m(E)` is a quotient of a
> quasi-coherent module on all of `X` — and that is false; the corrected clause is the local one
> stated here.
>
> The counterexample is on `X = Spec k[x, y]`. With `L = V(x)`, `i : L → X` and
> `Q = i_* i^{-1}𝒪_X` the pushforward of the *ordinary* inverse image of `𝒪_X`, the function
> `g = x - y(y-1)` — the equation of the irreducible curve through `p0 = (0, 0)` and
> `p1 = (0, 1)` — is invertible on `Q` over `U ∩ V`, where `U = X ∖ {p0}` and `V = X ∖ {p1}`.
> Gluing `Q|_U` to `Q|_V` along `a = g b` gives an `𝒪_X`-module `F` that is locally cyclic, so
> `F[0]` is `0`-pseudo-coherent, yet every global section of `F` vanishes in the fibre at `p1` by
> the valuation along `g = 0`; as `X` is affine, no quasi-coherent module surjects onto `F`.
> Quasi-compactness and quasi-separatedness would not have rescued the global form: `Spec k[x, y]`
> has both.

```lean
public theorem exists_local_epi_homology_of_isPseudoCoherentFrom (X : Scheme.{u})
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace)]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace)) (m : ℤ)
    (hE : RingedSpace.IsPseudoCoherentFrom (X := X.toRingedSpace) E m) (x : X) :
    ∃ U : X.Opens, x ∈ U ∧ ∃ M : U.toScheme.Modules, M.IsQuasicoherent ∧
      ∃ f : M ⟶ (Scheme.Modules.restrictFunctor U.ι).obj
        ((DerivedCategory.homologyFunctor
          (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace) m).obj E), Epi f
```

**`AlgebraicGeometry.isQuasicoherentDerived_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/QuasicoherentCohomology.lean#L196). The attribute's comment: “pseudo-coherent objects”.

> A pseudo-coherent object of `D(𝒪_X)` on a scheme has quasi-coherent cohomology in every
> degree, that is, it belongs to `D_QCoh(𝒪_X)`.

```lean
public theorem isQuasicoherentDerived_of_isPseudoCoherent (X : Scheme.{u})
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace)]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent
        (StrictlyPerfect.structureSheafOfRings X.toRingedSpace)) E
```

## Tag 08E7, a lemma

[Tag 08E7](https://stacks.math.columbia.edu/tag/08E7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_tilde_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/Affine.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/Affine.lean#L444). The attribute's comment: “m-pseudo-coherent”.

> **Tag 08E7 for `m`-pseudo-coherence.** A complex of `A`-modules is `m`-pseudo-coherent exactly
> when the complex of `𝒪`-modules it determines on `Spec A` is `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentFrom_tilde_iff {A : Type u} [CommRing A]
    (M : CochainComplex (ModuleCat.{u} A) ℤ) (m : ℤ) :
    IsPseudoCoherentFrom (X := (Spec (CommRingCat.of A)).toRingedSpace)
        (DerivedCategory.Q.obj
          (((tilde.functor (CommRingCat.of A) :
            ModuleCat.{u} A ⥤ OXMod.{u, u} (Spec (CommRingCat.of A)).toRingedSpace
            ).mapHomologicalComplex (ComplexShape.up ℤ)).obj M)) m ↔
      StacksDraft.PseudoCoherence.IsPseudoCoherentFrom (DerivedCategory.Q.obj M) m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherent_tilde_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/Affine.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/Affine.lean#L480). The attribute's comment: “pseudo-coherent”.

> **Tag 08E7 for pseudo-coherence.** A complex of `A`-modules is pseudo-coherent exactly when the
> complex of `𝒪`-modules it determines on `Spec A` is pseudo-coherent. Both sides are equivalent to
> the conjunction over all degrees of the fixed-degree condition: on the module side by Stacks 064W,
> on the sheaf side because Tag 08CC part (2) lets the one complex representing the object serve as
> the `m`-pseudo-coherent representative for every `m`.

```lean
public theorem isPseudoCoherent_tilde_iff {A : Type u} [CommRing A]
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    IsPseudoCoherent (X := (Spec (CommRingCat.of A)).toRingedSpace)
        (DerivedCategory.Q.obj
          (((tilde.functor (CommRingCat.of A) :
            ModuleCat.{u} A ⥤ OXMod.{u, u} (Spec (CommRingCat.of A)).toRingedSpace
            ).mapHomologicalComplex (ComplexShape.up ℤ)).obj M)) ↔
      StacksDraft.PseudoCoherence.IsPseudoCoherent (DerivedCategory.Q.obj M)
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_tilde_iff_locallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/AffineLocallySmall.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/AffineLocallySmall.lean#L172). The attribute's comment: “m-pseudo-coherent, at the locally small derived category”.

> **Tag 08E7 for `m`-pseudo-coherence, at the locally small derived category.** A complex of
> `A`-modules is `m`-pseudo-coherent exactly when the complex of `𝒪`-modules it determines on
> `Spec A` is `m`-pseudo-coherent as an object of the derived category of `𝒪_{Spec A}`-modules
> whose morphisms are in `Type u`. That is the derived category at which derived sheafification and
> the affine base-change comparison are stated.

```lean
public theorem isPseudoCoherentFrom_tilde_iff_locallySmall {A : Type u} [CommRing A]
    (M : CochainComplex (ModuleCat.{u} A) ℤ) (m : ℤ) :
    IsPseudoCoherentFrom (X := (Spec (CommRingCat.of A)).toRingedSpace)
        (DerivedCategory.Q.obj
          (((tilde.functor (CommRingCat.of A) :
            ModuleCat.{u} A ⥤ OXMod.{u, u} (Spec (CommRingCat.of A)).toRingedSpace
            ).mapHomologicalComplex (ComplexShape.up ℤ)).obj M)) m ↔
      StacksDraft.PseudoCoherence.IsPseudoCoherentFrom (DerivedCategory.Q.obj M) m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherent_tilde_iff_locallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/AffineLocallySmall.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentFrom/AffineLocallySmall.lean#L187). The attribute's comment: “pseudo-coherent, at the locally small derived category”.

> **Tag 08E7 for pseudo-coherence, at the locally small derived category.** A complex of
> `A`-modules is pseudo-coherent exactly when the complex of `𝒪`-modules it determines on `Spec A`
> is pseudo-coherent as an object of the derived category of `𝒪_{Spec A}`-modules whose morphisms
> are in `Type u`.

```lean
public theorem isPseudoCoherent_tilde_iff_locallySmall {A : Type u} [CommRing A]
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    IsPseudoCoherent (X := (Spec (CommRingCat.of A)).toRingedSpace)
        (DerivedCategory.Q.obj
          (((tilde.functor (CommRingCat.of A) :
            ModuleCat.{u} A ⥤ OXMod.{u, u} (Spec (CommRingCat.of A)).toRingedSpace
            ).mapHomologicalComplex (ComplexShape.up ℤ)).obj M)) ↔
      StacksDraft.PseudoCoherence.IsPseudoCoherent (DerivedCategory.Q.obj M)
```

**`Stacks.AffineTilde.isPseudoCoherentFrom_of_isPseudoCoherentFrom_tildeComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildeConverse.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildeConverse.lean#L215). The attribute's comment: “m-pseudo-coherent, the direction from sheaves to modules”.

> **Stacks 08E7, the direction from sheaves to modules.** If the object of `D(𝒪_{Spec R})`
> determined by a complex `M^•` of `R`-modules is `m`-pseudo-coherent (Stacks 08CB (3)), then `M^•`
> is `m`-pseudo-coherent as a complex of `R`-modules (Stacks 064Q (1)).
>
> The standard opens over which the localization of `M^•` is `m`-pseudo-coherent generate the unit
> ideal, because every point of `Spec R` lies in one of them; a finite subfamily still does, and
> Stacks 066D descends `m`-pseudo-coherence along it.

```lean
theorem isPseudoCoherentFrom_of_isPseudoCoherentFrom_tildeComplex
    (h : AlgebraicGeometry.RingedSpace.IsPseudoCoherentFrom
      (X := (Spec R).toRingedSpace) (DerivedCategory.Q.obj (tildeComplex M)) m) :
    IsPseudoCoherentFrom (DerivedCategory.Q.obj M) m
```

**`Stacks.AffineTilde.isPseudoCoherent_of_isPseudoCoherent_tildeComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildeConverse.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildeConverse.lean#L241). The attribute's comment: “pseudo-coherent, the direction from sheaves to modules”.

> **Stacks 08E7, the direction from sheaves to modules, all degrees at once.** If the object of
> `D(𝒪_{Spec R})` determined by a complex `M^•` of `R`-modules is pseudo-coherent (Stacks 08CB (3)),
> then `M^•` is pseudo-coherent as a complex of `R`-modules (Stacks 064Q (2)).
>
> Both notions are `m`-pseudo-coherence for every `m` — at the level of sheaves by definition, at
> the level of modules by Stacks 064U
> (`StacksDraft.PseudoCoherence.pseudoCoherent_iff_all`) — so this is the previous result applied
> degree by degree, with the representative the hypothesis supplies serving for all degrees.

```lean
theorem isPseudoCoherent_of_isPseudoCoherent_tildeComplex
    (h : AlgebraicGeometry.RingedSpace.IsPseudoCoherent
      (X := (Spec R).toRingedSpace) (DerivedCategory.Q.obj (tildeComplex M))) :
    IsPseudoCoherent (DerivedCategory.Q.obj M)
```

**`Stacks.AffineTilde.isPseudoCoherentFrom_tildeComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildePseudoCoherent.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildePseudoCoherent.lean#L142). The attribute's comment: “m-pseudo-coherent, the direction from modules to sheaves”.

> **Stacks 08E7, the direction from modules to sheaves.** If a complex `M^•` of `R`-modules is
> `m`-pseudo-coherent (Stacks 064Q (1)), then the object of `D(𝒪_{Spec R})` it determines is
> `m`-pseudo-coherent (Stacks 08CB (3)).

```lean
theorem isPseudoCoherentFrom_tildeComplex (M : CochainComplex (ModuleCat.{u} R) ℤ) (m : ℤ)
    (h : StacksDraft.PseudoCoherence.IsPseudoCoherentFrom (DerivedCategory.Q.obj M) m) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherentFrom
      (X := (Spec R).toRingedSpace) (DerivedCategory.Q.obj (tildeComplex M)) m
```

**`Stacks.AffineTilde.isPseudoCoherent_tildeComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildePseudoCoherent.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildePseudoCoherent.lean#L159). The attribute's comment: “pseudo-coherent, the direction from modules to sheaves”.

> **Stacks 08E7, the direction from modules to sheaves, all degrees at once.** If a complex
> `M^•` of `R`-modules is pseudo-coherent (Stacks 064Q (2)), then the object of `D(𝒪_{Spec R})` it
> determines is pseudo-coherent (Stacks 08CB (3)).
>
> Both notions of pseudo-coherence are `m`-pseudo-coherence for every `m` — at the level of modules
> by Stacks 064U
> (`StacksDraft.PseudoCoherence.pseudoCoherent_iff_all`), at the level of sheaves by definition —
> so this follows from `Stacks.AffineTilde.isPseudoCoherentComplexFrom_tildeComplex` degree by
> degree, with the single representative `\widetilde{M^•}` serving for all degrees.

```lean
theorem isPseudoCoherent_tildeComplex (M : CochainComplex (ModuleCat.{u} R) ℤ)
    (h : StacksDraft.PseudoCoherence.IsPseudoCoherent (DerivedCategory.Q.obj M)) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherent
      (X := (Spec R).toRingedSpace) (DerivedCategory.Q.obj (tildeComplex M))
```

## Tag 08E8, a lemma

[Tag 08E8](https://stacks.math.columbia.edu/tag/08E8) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherentFrom_iff_coherent_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Noetherian/CoherentHomology.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Noetherian/CoherentHomology.lean#L137). The attribute's comment: “equivalence in degree m”. References: SGA 6 I (3.5), “b), Noetherian scheme”.

> **Stacks Project, Tag 08E8.** Let `X` be a Noetherian scheme, let `E` be an object of
> `D_QCoh(𝒪_X)` and let `m` be an integer. Then `E` is `m`-pseudo-coherent if and only if `Hⁱ(E)`
> is coherent for every `i ≥ m` and vanishes for `i ≫ 0`.

```lean
public theorem isPseudoCoherentFrom_iff_coherent_homology (X : Scheme.{u}) [IsNoetherian X]
    (E : (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory)
    (m : ℤ) :
    RingedSpace.IsPseudoCoherentFrom (X := X.toRingedSpace) E.1 m ↔
      ((∀ i : ℤ, m ≤ i →
          ((DerivedCategory.homologyFunctor X.Modules i).obj E.1).IsCoherent) ∧
        DerivedCategoryB.IsBoundedAbove E.1)
```

**`AlgebraicGeometry.isPseudoCoherent_iff_boundedAbove_coherent_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Noetherian/CoherentHomology.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Noetherian/CoherentHomology.lean#L158). The attribute's comment: “identification with D⁻\_Coh”. References: SGA 6 I (3.5), “b) last claim, Noeth X”.

> **Stacks Project, Tag 08E8, the final statement.** On a Noetherian scheme an object of
> `D_QCoh(𝒪_X)` is pseudo-coherent if and only if it is bounded above and all of its cohomology
> sheaves are coherent, that is, if and only if it is an object of `D⁻_Coh(𝒪_X)`.

```lean
public theorem isPseudoCoherent_iff_boundedAbove_coherent_homology (X : Scheme.{u})
    [IsNoetherian X]
    (E : (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory) :
    RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E.1 ↔
      (DerivedCategoryB.IsBoundedAbove E.1 ∧
        ∀ i : ℤ,
          ((DerivedCategory.homologyFunctor X.Modules i).obj E.1).IsCoherent)
```

## Tag 08E9, a lemma

[Tag 08E9](https://stacks.math.columbia.edu/tag/08E9) in the Stacks Project.

**`AlgebraicGeometry.hasTorAmplitude_tilde_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedTildeTorAmplitude.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedTildeTorAmplitude.lean#L286). The attribute's comment: “part (1)”.

> **Stacks 08E9 (1).** Let `X = Spec R` be an affine scheme and let `M` be an object of `D(R)`.
> Then the associated object `M̃` of `D(𝒪_X)` has Tor amplitude in `[a, b]` if and only if `M` has
> Tor amplitude in `[a, b]`.

```lean
theorem hasTorAmplitude_tilde_iff (M : DerivedCategory (ModuleCat.{u} R)) (a b : ℤ) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude (Spec R).toRingedSpace
        ((tilde.functor R).mapDerivedCategory.obj M) a b ↔
      StacksDraft.TorAmplitude.HasTorAmplitudeCanonical R M a b
```

**`AlgebraicGeometry.hasFiniteTorDimension_tilde_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedTildeTorAmplitude.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedTildeTorAmplitude.lean#L320). The attribute's comment: “part (2)”.

> **Stacks 08E9 (2).** Let `X = Spec R` be an affine scheme and let `M` be an object of `D(R)`.
> Then the associated object `M̃` of `D(𝒪_X)` has finite Tor dimension if and only if `M` has finite
> Tor dimension.

```lean
theorem hasFiniteTorDimension_tilde_iff (M : DerivedCategory (ModuleCat.{u} R)) :
    Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension (Spec R).toRingedSpace
        ((tilde.functor R).mapDerivedCategory.obj M) ↔
      StacksDraft.TorAmplitude.HasFiniteTorDimensionCanonical R M
```

## Tag 0DHY, a lemma

[Tag 0DHY](https://stacks.math.columbia.edu/tag/0DHY) in the Stacks Project.

**`AlgebraicGeometry.AffineRelativeTorAmplitude.hasTorAmplitude_relativeComplex_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeTorAmplitudeAffine.lean, line 1104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeTorAmplitudeAffine.lean#L1104). The attribute's comment: “part (1)”.

> **Stacks 0DHY, part (1).** Let `f : Spec A ⟶ Spec R` be the morphism of affine schemes of a
> ring map `R → A`, let `M^•` be a complex of `A`-modules and let `E` be the complex of
> `f^{-1}𝒪_{Spec R}`-modules attached to it. Then `E` has Tor amplitude in `[a, b]` over
> `f^{-1}𝒪_{Spec R}` if and only if `M^•`, read as a complex of `R`-modules, has Tor amplitude in
> `[a, b]` over `R`.
>
> Tor amplitude on the sheaf side is tested at the fibres of the topological points by
> `hasTorAmplitude_iff_forall_pointFiber`, where it becomes the Tor amplitude of the localisation
> of `M^•` at each prime of `A` over the corresponding localisation of `R`
> (`hasTorAmplitudeCanonical_derivedModuleFiber_iff`); that family of conditions is Tor amplitude
> over `R` by `hasTorAmplitudeCanonical_restrictScalars_iff_forall_isPrime`.

```lean
theorem hasTorAmplitude_relativeComplex_iff (M : CochainComplex (ModuleCat.{u} A) ℤ) (a b : ℤ) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude (relativeRingedSpace R A)
        (DerivedCategory.Q.obj (relativeComplex R A M)) a b ↔
      HasTorAmplitudeCanonical R (DerivedCategory.Q.obj
        (((ModuleCat.restrictScalars (algebraMap R A)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj M)) a b
```

**`AlgebraicGeometry.AffineRelativeTorAmplitude.locallyHasFiniteTorDimension_relativeComplex_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeTorAmplitudeAffine.lean, line 1126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeTorAmplitudeAffine.lean#L1126). The attribute's comment: “part (2)”.

> **Stacks 0DHY, part (2).** In the situation of part (1), the complex `E` of
> `f^{-1}𝒪_{Spec R}`-modules locally has finite Tor dimension if and only if `M^•`, read as a
> complex of `R`-modules, has finite Tor dimension over `R`.
>
> The space `Spec A` is quasi-compact, so locally finite Tor dimension is Tor amplitude in a
> single interval (`locallyHasFiniteTorDimension_iff_hasFiniteTorDimension`), and part (1)
> translates each interval.

```lean
theorem locallyHasFiniteTorDimension_relativeComplex_iff
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    LocallyHasFiniteTorDimension (relativeRingedSpace R A)
        (DerivedCategory.Q.obj (relativeComplex R A M)) ↔
      HasFiniteTorDimensionCanonical R (DerivedCategory.Q.obj
        (((ModuleCat.restrictScalars (algebraMap R A)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj M))
```

## Tag 08EA, a lemma

[Tag 08EA](https://stacks.math.columbia.edu/tag/08EA) in the Stacks Project.

**`AlgebraicGeometry.hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorAmplitudeQuasiCoherentTestsGlobal.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TorAmplitudeQuasiCoherentTestsGlobal.lean#L143).

> **Stacks 08EA.** Let `X` be a quasi-separated scheme, `E` an object of `D_QCoh(𝒪_X)` and
> `a ≤ b`. The following are equivalent:
>
> 1. `E` has Tor amplitude in `[a, b]`;
> 2. `H^i(E ⊗^L_{𝒪_X} ℱ) = 0` for `i ∉ [a, b]` and every quasi-coherent `𝒪_X`-module `ℱ`.
>
> Neither direction uses `a ≤ b`.

```lean
theorem hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent {X : Scheme.{u}}
    [QuasiSeparatedSpace X] (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace)) (a b : ℤ)
    (hqc : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj E).IsQuasicoherent) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace E a b ↔
      Stacks.Cohomology.TorAmplitude.HasTorAmplitudeOnQuasicoherent X.toRingedSpace E a b
```

## Tag 08EB, a lemma

[Tag 08EB](https://stacks.math.columbia.edu/tag/08EB) in the Stacks Project.

**`AlgebraicGeometry.isPerfect_tilde_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedTildePerfect.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedTildePerfect.lean#L134).

> **Stacks 08EB.** Let `X = Spec R` be an affine scheme and let `M` be an object of `D(R)`. Then
> the associated object `M̃` of `D(𝒪_X)` is a perfect object of `D(𝒪_X)` if and only if `M` is a
> perfect object of `D(R)`.

```lean
theorem isPerfect_tilde_iff (M : DerivedCategory (ModuleCat.{u} R)) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect
        ((tilde.functor R).mapDerivedCategory.obj M) ↔
      StacksDraft.Perfect.IsPerfect M
```

**`AlgebraicGeometry.isPerfect_tilde_iff_of_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedTildePerfect.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedTildePerfect.lean#L184).

> **Stacks 08EB at an arbitrary pair of chosen derived categories.** Let `X = Spec R` be an
> affine scheme and let `M` be an object of `D(R)`, for any chosen model of `D(R)` and any chosen
> model of `D(𝒪_X)`, with the two morphism universes unrelated. Then the associated object `M̃` of
> `D(𝒪_X)` is a perfect object of `D(𝒪_X)` if and only if `M` is a perfect object of `D(R)`.

```lean
theorem isPerfect_tilde_iff_of_model [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    [hS : HasDerivedCategory.{w'} (Spec R).Modules] (M : DerivedCategory (ModuleCat.{u} R)) :
    @Stacks.Cohomology.PerfectComplexes.IsPerfect (Spec R).toRingedSpace hS
        ((tilde.functor R).mapDerivedCategory.obj M) ↔
      StacksDraft.Perfect.IsPerfect M
```

## Tag 0A6H, a lemma

[Tag 0A6H](https://stacks.math.columbia.edu/tag/0A6H) in the Stacks Project.

**`AlgebraicGeometry.affineDerivedTildeHomComparison_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/Comparison.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/Comparison.lean#L624). The attribute's comment: “(3)(b) K perfect and L arbitrary: the canonical comparison is the inverse of the isomorphism”.

> **The canonical comparison agrees with clause (3)(b).** For `K` perfect it is the inverse
> of the isomorphism `affinePerfectDerivedSheafHomIso`, hence invertible. This is what identifies
> the comparison as the morphism whose invertibility clause (3)(b) asserts, rather than as some
> morphism between the right two objects: the two are equal because they agree on bounded
> finite-projective sources with K-injective targets, where both are the five-fold model
> composite, and because both are natural.

```lean
public theorem affineDerivedTildeHomComparison_perfect (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.Perfect.IsPerfect K) :
    affineDerivedTildeHomComparison R K L =
      (affinePerfectDerivedSheafHomIso R K L hK).inv
```

**`AlgebraicGeometry.affinePerfectDerivedSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean#L607). The attribute's comment: “(3)(b) K perfect and L arbitrary”.

> **Stacks 0A6H, clause (3), case (b).** Let `R` be a commutative ring, `X = Spec R`, and let
> `K`, `L` be objects of `D(R)` with `K` perfect. Then the derived internal Hom of the derived
> sheafifications is the derived sheafification of the derived Hom over `R`:
>
> `R𝓗om_{𝒪_X}(K̃, L̃)  ≅  (R Hom_R(K, L))~`.
>
> The object `L` is arbitrary. The isomorphism is not an arbitrary one: it is
> pinned down on bounded finite-projective representatives by
> `affinePerfectDerivedSheafHomIso_model`, and it is natural in both arguments by
> `affinePerfectDerivedSheafHomIso_natural_left` and `_natural_right`.

```lean
public def affinePerfectDerivedSheafHomIso (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.Perfect.IsPerfect K) :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).obj
        (op ((tildeDer R).obj K))).obj ((tildeDer R).obj L) ≅
      (tildeDer R).obj
        ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.obj (op K, L))
```

**`AlgebraicGeometry.affinePerfectDerivedSheafHomIso_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean#L622). The attribute's comment: “(3)(b) K perfect and L arbitrary”.

> **The normalization of clause (3)(b).** On a bounded complex `P` of finite projective
> modules the comparison is the sheafification of the ordinary Hom-complex comparison
> `affineHomComplexTildeIso`, read through the [Stacks, Tag 08JH] comparison on the sheaf side and
> the [Stacks, Tag 0A66] comparison on the module side. This identifies the isomorphism, not just
> its source and target.

```lean
public theorem affinePerfectDerivedSheafHomIso_model (R : CommRingCat.{u})
    (P L : CochainComplex (ModuleCat.{u} R) ℤ) (b : ℤ)
    [P.IsStrictlyLE b] [∀ i, Projective (P.X i)] [∀ i, Module.Finite R (P.X i)]
    (hP : {i : ℤ | ¬ IsZero (P.X i)}.Finite)
    (hK : StacksDraft.Perfect.IsPerfect (DerivedCategory.Q.obj P)) :
    strictlyPerfectHomComparison (specSite R) (specRHom R)
          ((tildeCx R).obj P) ((tildeCx R).obj L) ≫
        ((specRHom R).hom.map ((tilde.functor R).mapDerivedCategoryFactors.hom.app P).op).app
          (DerivedCategory.Q.obj ((tildeCx R).obj L)) ≫
        ((specRHom R).hom.obj (op ((tildeDer R).obj (DerivedCategory.Q.obj P)))).map
          ((tilde.functor R).mapDerivedCategoryFactors.inv.app L) ≫
        (affinePerfectDerivedSheafHomIso R (DerivedCategory.Q.obj P)
          (DerivedCategory.Q.obj L) hK).hom ≫
        (tildeDer R).map (StacksDraft.DerivedHom.projectiveHomComparison.iso P L b).hom ≫
        (tilde.functor R).mapDerivedCategoryFactors.hom.app
          (CochainComplex.HomComplexR R P L) =
      (DerivedCategory.Q.mapIso (affineHomComplexTildeIso R P L hP)).hom
```

**`AlgebraicGeometry.affinePerfectDerivedSheafHomIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean#L652). The attribute's comment: “(3)(b) K perfect and L arbitrary”.

> **Clause (3)(b) is natural in the target.**

```lean
public theorem affinePerfectDerivedSheafHomIso_natural_right (R : CommRingCat.{u})
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.Perfect.IsPerfect K)
    {L L' : DerivedCategory (ModuleCat.{u} R)} (g : L ⟶ L') :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).obj
          (op ((tildeDer R).obj K))).map ((tildeDer R).map g) ≫
        (affinePerfectDerivedSheafHomIso R K L' hK).hom =
      (affinePerfectDerivedSheafHomIso R K L hK).hom ≫
        (tildeDer R).map
          ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.map (𝟙 (op K), g))
```

**`AlgebraicGeometry.affinePerfectDerivedSheafHomIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedHom/PerfectSource.lean#L677). The attribute's comment: “(3)(b) K perfect and L arbitrary”.

> **Clause (3)(b) is contravariantly natural in the perfect source.**

```lean
public theorem affinePerfectDerivedSheafHomIso_natural_left (R : CommRingCat.{u})
    {K K' : DerivedCategory (ModuleCat.{u} R)} (f : K' ⟶ K)
    (hK : StacksDraft.Perfect.IsPerfect K)
    (hK' : StacksDraft.Perfect.IsPerfect K')
    (L : DerivedCategory (ModuleCat.{u} R)) :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).map
          ((tildeDer R).map f).op).app ((tildeDer R).obj L) ≫
        (affinePerfectDerivedSheafHomIso R K' L hK').hom =
      (affinePerfectDerivedSheafHomIso R K L hK).hom ≫
        (tildeDer R).map
          ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.map (f.op, 𝟙 L))
```

**`AlgebraicGeometry.AffineExt.cohomologySheaf_isSheafification_extPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineExtCohomologySheaf.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineExtCohomologySheaf.lean#L71). The attribute's comment: “(4) the n-th cohomology sheaf of RHom(K~, L~) on Spec A is the sheaf of modules associated to the presheaf D(f) ↦ Ext^n\_\{A\_f}(K ⊗ A\_f, L ⊗ A\_f), through the canonical A\_f-linear comparison maps”.

> Let `A` be a commutative ring, let `K`, `L` be objects of `D(A)` and let `n` be an integer.
> The `n`-th cohomology sheaf of `R𝓗om(K̃, L̃)` on `Spec A` is the sheaf of `𝒪_{Spec A}`-modules
> associated to the presheaf `D(f) ↦ Ext^n_{A_f}(K ⊗_A A_f, L ⊗_A A_f)` on the principal opens of
> `Spec A`: the canonical maps `Ext^n_{A_f}(K ⊗_A A_f, L ⊗_A A_f) ⟶ Γ(D(f), Hⁿ(R𝓗om(K̃, L̃)))`,
> one for every `f : A`, which are `A_f`-linear
> (`AlgebraicGeometry.AffineExt.extToCohomologySheafLinear`),
> * commute with restriction, the restriction of `Ext` classes from `D(f)` to `D(g) ⊆ D(f)` being
>   derived base change along `A_f ⟶ A_g`;
> * are locally surjective: every section of `Hⁿ(R𝓗om(K̃, L̃))` over `D(f)` is, around every point of
>   `D(f)`, the restriction of the image of an `Ext` class over a smaller principal open;
> * are locally injective: an `Ext` class over `D(f)` with zero image restricts to zero over a
>   principal open around every point of `D(f)`.
>
> Here `A_f = Γ(Spec A, D(f))` is the localization of `A` away from `f`, which is also the ring of
> sections of `𝒪_{Spec A}` over `D(f)`. The objects `K` and `L` are arbitrary.

```lean
theorem cohomologySheaf_isSheafification_extPresheaf (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R)) (n : ℤ) :
    (∀ (f g : R) (h : basicOpen R g ≤ basicOpen R f) (α : localizedExt R K L f n),
        (cohomologySheaf R K L n).presheaf.map (homOfLE h).op
            (extToCohomologySheafLinear R K L n f α) =
          extToCohomologySheafLinear R K L n g (localizedExtRestrict R K L h n α)) ∧
      (∀ (f : R) (s : Γ(cohomologySheaf R K L n, basicOpen R f)) (x : Spec R),
        x ∈ basicOpen R f → ∃ (g : R) (h : basicOpen R g ≤ basicOpen R f),
          x ∈ basicOpen R g ∧ ∃ α, extToCohomologySheafLinear R K L n g α =
            (cohomologySheaf R K L n).presheaf.map (homOfLE h).op s) ∧
      (∀ (f : R) (α : localizedExt R K L f n), extToCohomologySheafLinear R K L n f α = 0 →
        ∀ x : Spec R, x ∈ basicOpen R f → ∃ (g : R) (h : basicOpen R g ≤ basicOpen R f),
          x ∈ basicOpen R g ∧ localizedExtRestrict R K L h n α = 0)
```

**`AlgebraicGeometry.affinePseudoCoherentDerivedSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean#L761). The attribute's comment: “(3)(a) K pseudo-coherent and L bounded below”.

> **[Stacks, Tag 0A6H] (3)(a).** Let `R` be a commutative ring, `X = Spec R`, and let `K`, `L`
> be objects of `D(R)` with `K` pseudo-coherent and `L` bounded below. Then the derived internal
> Hom of the derived sheafifications of `K` and `L` is the derived sheafification of the derived
> Hom `RHom_R(K, L)`:
>
> `RSheafHom_{𝒪_X}(K̃, L̃) ≅ (RHom_R(K, L))~`.
>
> The comparison is not an arbitrary isomorphism. `K` is replaced by a bounded-above
> representative with finite free terms and `L` by a bounded-below K-injective representative;
> there the sheaf side is computed by the ordinary internal Hom complex (Stacks 08I5) and the
> module side by the ordinary Hom complex (Stacks 0A66), and the comparison is the one pinned
> degreewise by the affine internal-Hom isomorphism of [Stacks, Tag 01I8]. The representatives
> are definite choices, so the construction is a function of its arguments, and it is natural in
> both of them (`affinePseudoCoherentDerivedSheafHomIso_natural_left` and
> `affinePseudoCoherentDerivedSheafHomIso_natural_right`). The canonical comparison
> `AlgebraicGeometry.affineDerivedTildeHomComparison` in the other direction is an isomorphism under
> the same hypotheses, `isIso_affineDerivedTildeHomComparison_of_isPseudoCoherent`.

```lean
noncomputable def affinePseudoCoherentDerivedSheafHomIso (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hL : (DerivedCategory.TStructure.t).plus L) :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).obj
        (op ((tilde.functor R).mapDerivedCategory.obj K))).obj
          ((tilde.functor R).mapDerivedCategory.obj L) ≅
      (tilde.functor R).mapDerivedCategory.obj
        ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.obj (op K, L))
```

**`AlgebraicGeometry.affinePseudoCoherentDerivedSheafHomIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean, line 889](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean#L889). The attribute's comment: “(3)(a) K pseudo-coherent and L bounded below”.

> **[Stacks, Tag 0A6H] (3)(a).** The affine comparison is contravariantly natural in the
> pseudo-coherent argument.

```lean
theorem affinePseudoCoherentDerivedSheafHomIso_natural_left (R : CommRingCat.{u})
    {K K' L : DerivedCategory (ModuleCat.{u} R)}
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hK' : StacksDraft.PseudoCoherence.IsPseudoCoherent K')
    (hL : (DerivedCategory.TStructure.t).plus L) (f : K' ⟶ K) :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).map
        ((tilde.functor R).mapDerivedCategory.map f).op).app
          ((tilde.functor R).mapDerivedCategory.obj L) ≫
      (affinePseudoCoherentDerivedSheafHomIso R K' L hK' hL).hom =
    (affinePseudoCoherentDerivedSheafHomIso R K L hK hL).hom ≫
      (tilde.functor R).mapDerivedCategory.map
        ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.map
          (f.op, 𝟙 L))
```

**`AlgebraicGeometry.affinePseudoCoherentDerivedSheafHomIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean, line 914](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean#L914). The attribute's comment: “(3)(a) K pseudo-coherent and L bounded below”.

> **[Stacks, Tag 0A6H] (3)(a).** The affine comparison is covariantly natural in the
> bounded-below argument.

```lean
theorem affinePseudoCoherentDerivedSheafHomIso_natural_right (R : CommRingCat.{u})
    {K L L' : DerivedCategory (ModuleCat.{u} R)}
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hL : (DerivedCategory.TStructure.t).plus L)
    (hL' : (DerivedCategory.TStructure.t).plus L') (g : L ⟶ L') :
    ((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).obj
        (op ((tilde.functor R).mapDerivedCategory.obj K))).map
          ((tilde.functor R).mapDerivedCategory.map g) ≫
      (affinePseudoCoherentDerivedSheafHomIso R K L' hK hL').hom =
    (affinePseudoCoherentDerivedSheafHomIso R K L hK hL).hom ≫
      (tilde.functor R).mapDerivedCategory.map
        ((StacksDraft.DerivedHom.derivedHomAdjunction (R := R)).hom.map
          (𝟙 (op K), g))
```

**`AlgebraicGeometry.isIso_affineDerivedTildeHomComparison_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean, line 995](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePseudoCoherentDerivedHom.lean#L995). The attribute's comment: “(3)(a) K pseudo-coherent and L bounded below: the canonical comparison is an isomorphism”.

> **[Stacks, Tag 0A6H] (3)(a), for the canonical comparison.** Let `R` be a commutative ring,
> `X = Spec R`, and let `K`, `L` be objects of `D(R)` with `K` pseudo-coherent and `L` bounded below.
> Then the canonical comparison
>
> `(RHom_R(K, L))~ ⟶ R𝓗om_{𝒪_X}(K̃, L̃)`
>
> of `AlgebraicGeometry.affineDerivedTildeHomComparison` is an isomorphism.

```lean
theorem isIso_affineDerivedTildeHomComparison_of_isPseudoCoherent (R : CommRingCat.{u})
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hL : (DerivedCategory.TStructure.t).plus L) :
    IsIso (affineDerivedTildeHomComparison R K L)
```

**`AlgebraicGeometry.derivedCategoryB_derivedSheafHom_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPerfectHomQuasicoherent.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPerfectHomQuasicoherent.lean#L125). The attribute's comment: “part (2) on an arbitrary scheme: the derived internal Hom out of a perfect object into an object of D\_QCoh has quasi-coherent cohomology sheaves”.

> **Stacks Project, Tag 0A6H, part (2).** Let `Y` be a scheme, let `E` be a perfect object of
> `D(𝒪_Y)` and let `F` be an object of `D_QCoh(𝒪_Y)`. Then the derived internal Hom
> `R𝓗om_{𝒪_Y}(E, F)` lies in `D_QCoh(𝒪_Y)`: all of its cohomology sheaves are quasi-coherent.
>
> The affine opens of `Y` cover it, so by the locality of quasi-coherence it is enough to see that
> each cohomology sheaf restricts to a quasi-coherent module on every affine open `U`. Restriction
> along `U.ι` commutes with the derived internal Hom by [Stacks, Tag 08DL], keeps `E` perfect by
> [Stacks, Tag 09UA] and keeps `F` in `D_QCoh`, so the restriction is the derived internal Hom of
> the restrictions on the affine scheme `U`, where
> `derivedCategoryB_derivedSheafHom_of_isPerfect_of_isAffine` applies.

```lean
theorem derivedCategoryB_derivedSheafHom_of_isPerfect (Y : Scheme.{u})
    (E F : DerivedCategory (StructureSheafModules Y.sheaf))
    (hE : RingedSpace.IsPerfect (X := Y.toRingedSpace) E)
    (hF : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf) F) :
    DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent Y.ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj (op E)).obj F)
```

**`AlgebraicGeometry.isLocallyBoundedBelow_derivedSheafHom_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPseudoCoherentHomLocallyBounded.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPseudoCoherentHomLocallyBounded.lean#L95). The attribute's comment: “part (1) on an arbitrary scheme: the derived internal Hom out of a pseudo-coherent object into an object of D⁺\_QCoh is locally bounded below”.

> Let `Y` be a scheme, let `E` be a pseudo-coherent object of `D(𝒪_Y)` and let `F` be an
> object of `D⁺_QCoh(𝒪_Y)`. Then `R𝓗om_{𝒪_Y}(E, F)` is locally bounded below: every point of `Y`
> has an open neighbourhood over which the cohomology sheaves vanish in all sufficiently negative
> degrees.

```lean
theorem isLocallyBoundedBelow_derivedSheafHom_of_isPseudoCoherent (Y : Scheme.{u})
    (E F : DerivedCategory (StructureSheafModules Y.sheaf))
    (hE : RingedSpace.IsPseudoCoherent (X := Y.toRingedSpace) E)
    (hF : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf) F) :
    RingedSpace.IsLocallyBoundedBelow Y.toRingedSpace
      (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj (op E)).obj F)
```

**`AlgebraicGeometry.derivedCategoryB_derivedSheafHom_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPseudoCoherentHomQuasicoherent.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeSheafPseudoCoherentHomQuasicoherent.lean#L168). The attribute's comment: “part (1) on an arbitrary scheme: the derived internal Hom out of a pseudo-coherent object into an object of D⁺\_QCoh has quasi-coherent cohomology sheaves”.

> **Stacks Project, Tag 0A6H, part (1).** Let `Y` be a scheme, let `E` be a pseudo-coherent
> object of `D(𝒪_Y)` and let `F` be an object of `D⁺_QCoh(𝒪_Y)`. Then the derived internal Hom
> `R𝓗om_{𝒪_Y}(E, F)` lies in `D_QCoh(𝒪_Y)`: all of its cohomology sheaves are quasi-coherent.
>
> The affine opens of `Y` cover it, so by the locality of quasi-coherence it is enough to see that
> each cohomology sheaf restricts to a quasi-coherent module on every affine open `U`. Restriction
> along `U.ι` commutes with the derived internal Hom by [Stacks, Tag 08DL], keeps `E`
> pseudo-coherent by [Stacks, Tag 08CC] and keeps `F` in `D⁺_QCoh`, so the restriction is the
> derived internal Hom of the restrictions on the affine scheme `U`, where
> `derivedCategoryB_derivedSheafHom_of_isPseudoCoherent_of_isAffine` applies.

```lean
theorem derivedCategoryB_derivedSheafHom_of_isPseudoCoherent (Y : Scheme.{u})
    (E F : DerivedCategory (StructureSheafModules Y.sheaf))
    (hE : RingedSpace.IsPseudoCoherent (X := Y.toRingedSpace) E)
    (hF : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf) F) :
    DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent Y.ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj (op E)).obj F)
```

**`AlgebraicGeometry.derivedCategoryBPlus_derivedSheafHom_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean#L75). The attribute's comment: “part (1) with the lower bound, on an arbitrary scheme, for a cohomologically bounded-above pseudo-coherent first argument”.

> Let `Z` be a scheme, let `E` be an object of `D(𝒪_Z)` which is pseudo-coherent and
> cohomologically bounded above, and let `F` lie in `D⁺_QCoh(𝒪_Z)`.  Then `R𝓗om_{𝒪_Z}(E, F)` lies
> in `D⁺_QCoh(𝒪_Z)`.

```lean
theorem derivedCategoryBPlus_derivedSheafHom_of_isPseudoCoherent (Z : Scheme.{u})
    (E F : DerivedCategory (StructureSheafModules Z.sheaf))
    (hE : RingedSpace.IsPseudoCoherent (X := Z.toRingedSpace) E)
    (hE' : DerivedCategoryB.IsBoundedAbove E)
    (hF : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent Z.ringCatSheaf) F) :
    DerivedCategoryB.derivedCategoryBPlus (SheafOfModules.isQuasicoherent Z.ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom Z.sheaf).obj (op E)).obj F)
```

## Tag 0ATN, a lemma

[Tag 0ATN](https://stacks.math.columbia.edu/tag/0ATN) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorHomDiagonal_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPerfect.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPerfect.lean#L333). The attribute's comment: “part (1)”.

> **Stacks 0ATN part (1): the diagonal of Stacks 0BYS is an isomorphism at a perfect source.**
> For objects `K`, `L`, `M` of `D(O)` with `M` perfect,
>
> `K ⊗^L_O RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_O L)`
>
> is an isomorphism.
>
> The only hypothesis is `X.IsPerfect M`, the site-level notion of Stacks 08G5: there is a complex
> `N` representing `M` and a covering of the site on each member of which the restriction of `N`
> receives a quasi-isomorphism from a strictly perfect complex. Nothing is assumed of `K` or `L`.
>
> The instances in the ambient variable block are setup, not hypotheses on the lemma: a ringed site
> whose slices admit sheafification and on which the tensor product of sheaves of modules is
> additive and totalisable is what it takes for the objects in the statement — the derived tensor
> product, the derived internal Hom, and their restrictions to the slices appearing in the
> definition of perfection — to exist at all. A class needed only by the proof would have been an
> extra hypothesis, and there is none.

```lean
theorem isIso_derivedTensorHomDiagonal_of_isPerfect
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hM : X.IsPerfect M) :
    IsIso (derivedTensorHomDiagonal X K L M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorHomDiagonal_of_isPerfect_tensorFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPerfectTensorFactor.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPerfectTensorFactor.lean#L227). The attribute's comment: “part (2)”.

> **Stacks 0ATN part (2): the diagonal of Stacks 0BYS is an isomorphism at a perfect tensor
> factor.** For objects `K`, `L`, `M` of `D(O)` with `K` perfect,
>
> `K ⊗^L_O RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_O L)`
>
> is an isomorphism.
>
> The only hypothesis is `X.IsPerfect K`, the site-level notion of Stacks 08G5: there is a complex
> `A₀` representing `K` and a covering of the site on each member of which the restriction of `A₀`
> receives a quasi-isomorphism from a strictly perfect complex. Nothing is assumed of `L` or `M`.
> This is the same notion, with the same slack, that part (1) assumes of `M`.
>
> The instances in the ambient variable block are setup, not hypotheses on the lemma, exactly as
> for part (1): a ringed site whose slices admit sheafification and on which the tensor product of
> sheaves of modules is additive and totalisable is what it takes for the objects named in the
> statement to exist. A class needed only by the proof would have been an extra hypothesis, and
> there is none.
>
> The K-flat resolution is taken of `A₀` itself rather than of the chosen K-flat model of `K`, so
> that the comparison between the criterion's model and the complex the covering resolves is a
> quasi-isomorphism of complexes and the slice-level input can be assembled from chain maps.

```lean
theorem isIso_derivedTensorHomDiagonal_of_isPerfect_tensorFactor
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K) :
    IsIso (derivedTensorHomDiagonal X K L M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorHomDiagonal_of_isPseudoCoherent_of_hasTorAmplitudeGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPseudoCoherent.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPseudoCoherent.lean#L396). The attribute's comment: “part (3), with the tensor factor of Tor amplitude in [a, ∞) rather than of finite Tor dimension”.

> **The diagonal of Stacks 0BYS is an isomorphism at a pseudo-coherent source, a
> cohomologically bounded-below target and a tensor factor of Tor amplitude in `[a, ∞)`.** For
> objects `K`, `L`, `M` of `D(O)` with `M` pseudo-coherent, the cohomology of `L` vanishing in
> degrees `≪ 0` and `K` of Tor amplitude in `[a, ∞)`,
>
> `K ⊗^L_O RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_O L)`
>
> is an isomorphism.
>
> Pseudo-coherence is `AlgebraicGeometry.RingedSite.IsPseudoCoherent`, Tor amplitude in `[a, ∞)`
> is `Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitudeGE` for the canonical derived
> tensor product, and boundedness below is vanishing of the cohomology sheaves in degrees `≪ 0`.

```lean
public theorem isIso_derivedTensorHomDiagonal_of_isPseudoCoherent_of_hasTorAmplitudeGE
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (a : ℤ)
    (hM : X.IsPseudoCoherent M)
    (hL : DerivedCategoryB.IsBoundedBelow L)
    (hK : Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitudeGE
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct X) K a) :
    IsIso (derivedTensorHomDiagonal X K L M)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedTensorHomDiagonal_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPseudoCoherent.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonalPseudoCoherent.lean#L468). The attribute's comment: “part (3)”.

> **Stacks 0ATN part (3): the diagonal of Stacks 0BYS is an isomorphism at a pseudo-coherent
> source, a cohomologically bounded-below target and a tensor factor of finite Tor dimension.**
> For objects `K`, `L`, `M` of `D(O)` with `M` pseudo-coherent, the cohomology of `L` vanishing in
> degrees `≪ 0` and `K` of finite Tor dimension,
>
> `K ⊗^L_O RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_O L)`
>
> is an isomorphism.
>
> The three hypotheses are the site-level notions: pseudo-coherence is
> `AlgebraicGeometry.RingedSite.IsPseudoCoherent` of Stacks 08FT, finite Tor dimension is
> `Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension` of Stacks 08FZ for the
> canonical derived tensor product, and boundedness below is vanishing of the cohomology sheaves
> in degrees `≪ 0`.

```lean
public theorem isIso_derivedTensorHomDiagonal_of_isPseudoCoherent
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hM : X.IsPseudoCoherent M)
    (hL : DerivedCategoryB.IsBoundedBelow L)
    (hK : Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct X) K) :
    IsIso (derivedTensorHomDiagonal X K L M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.10, Tag 08E4](https://stacks.math.columbia.edu/tag/08E4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
