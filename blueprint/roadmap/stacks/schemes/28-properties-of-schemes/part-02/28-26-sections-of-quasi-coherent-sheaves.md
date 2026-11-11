---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSectionsData, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_restrict_ι, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_injective_of_fg, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_surjective, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_injective, Stacks.AlgebraicGeometry.IdealPowerSections.isIso_canonicalMapToSections, Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapModuloAnnihilator_bijective
statement: formalized
proof: formalized
---

# 28.26 Sections of quasi-coherent sheaves

Section 28.26 of the Stacks Project, [Tag 01PL](https://stacks.math.columbia.edu/tag/01PL). 3 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01PM, a lemma

[Tag 01PM](https://stacks.math.columbia.edu/tag/01PM) in the Stacks Project.

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSectionsData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean#L370). The attribute's comment: “canonical\_map”.

> **Stacks Project, Tag 01PM (`canonical_map`).** The canonical map
> `colim_n Hom_A(I ^ n, M) → Γ(Spec(A) \ V(I), M̃)`.

```lean
public noncomputable def canonicalMapToSectionsData : CanonicalMapToSectionsData A I M
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean#L389). The attribute's comment: “canonical\_map”.

> The canonical map, with its local evaluation rule supplied by the construction.

```lean
public noncomputable def canonicalMapToSections :
    colimit (idealPowersHom A I M) ⟶ sectionsOnComplement A I M
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_restrict_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean#L396). The attribute's comment: “canonical\_map”.

> On every basic open `D(f)` with `f ∈ I`, a colimit representative `φ` has image
> `φ(fⁿ)/fⁿ`.

```lean
public theorem canonicalMapToSections_restrict_ι (n : ℕ)
    (φ : (I ^ n : Ideal A) →ₗ[A] M) (f : A) (hf : f ∈ I) :
    restrictToBasicOpen A I M f hf
      (canonicalMapToSections A I M (colimit.ι (idealPowersHom A I M) n φ)) =
        basicOpenFraction A M f n (φ ⟨f ^ n, Ideal.pow_mem_pow hf n⟩)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_injective_of_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSections/Basic.lean#L481). The attribute's comment: “injective”.

> **Stacks Project, Tag 01PM (`injective`).** The canonical map
> `colim_n Hom_A(I ^ n, M) → Γ(Spec(A) \ V(I), M̃)` is injective when `I` is finitely generated.

```lean
public theorem canonicalMapToSections_injective_of_fg (hI : I.FG) :
    Function.Injective (canonicalMapToSections A I M)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSections/Surjectivity.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSections/Surjectivity.lean#L693). The attribute's comment: “surjectivity when no nonzero element of M is annihilated by I”.

> **Surjectivity in the torsion-free case.** If `I` is finitely generated and annihilates no
> nonzero element of `M`, the canonical map `colim_n Hom_A(I ^ n, M) ⟶ Γ(Spec(A) \ V(I), M̃)` is
> surjective.

```lean
public theorem canonicalMapToSections_surjective (hI : I.FG)
    (hM : ∀ y : M, (∀ a ∈ I, a • y = 0) → y = 0) :
    Function.Surjective (canonicalMapToSections A I M)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapToSections_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSectionsComparison/Basic.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSectionsComparison/Basic.lean#L169). The attribute's comment: “injectivity”.

> For a finitely generated ideal `I` the canonical map
> `colim_n Hom_A(I ^ n, M) → Γ(Spec(A) \ V(I), M̃)` is injective.

```lean
public theorem canonicalMapToSections_injective (hI : I.FG) :
    Function.Injective (canonicalMapToSections A I M)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.isIso_canonicalMapToSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSectionsSurjective/Basic.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSectionsSurjective/Basic.lean#L253). The attribute's comment: “torsionfree\_isomorphism”.

> **Stacks Project, Tag 01PM (`torsionfree_isomorphism`).** Let `I` be a finitely generated
> ideal of `A`. If no nonzero element of `M` is annihilated by all of `I`, then the canonical map
> `colim_n Hom_A(I ^ n, M) → Γ(Spec(A) \ V(I), M̃)` is an isomorphism.
>
> The hypothesis is the vanishing of `Submodule.torsionBySet A M I`, the submodule of elements
> annihilated by every element of `I`; in the source it is used exactly to see that all of the
> submodules `Mₙ` vanish, so that the general isomorphism of [Stacks, Tag 01PM] reduces to the
> canonical map itself.

```lean
public theorem isIso_canonicalMapToSections (hI : I.FG)
    (hM : Submodule.torsionBySet A M (I : Ideal A) = ⊥) :
    IsIso (canonicalMapToSections A I M)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.canonicalMapModuloAnnihilator_bijective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/IdealPowerQuotientIso.lean, line 981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/IdealPowerQuotientIso.lean#L981). The attribute's comment: “general\_isomorphism”.

> **Stacks Project, Tag 01PM (`general_isomorphism`).** For a finitely generated ideal `I`
> the canonical map from the direct limit of `Hom_A(I ^ n, M / Mₙ)` to the sections of `M̃` on
> `Spec(A) \ V(I)` is bijective.

```lean
public lemma canonicalMapModuloAnnihilator_bijective (hI : I.FG) :
    Function.Bijective (canonicalMapModuloAnnihilator A I M)
```

**`Stacks.AlgebraicGeometry.IdealPowerSections.idealPowersHomModuloAnnihilatorColimitIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/IdealPowerQuotientIso.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/IdealPowerQuotientIso.lean#L990). The attribute's comment: “general\_isomorphism”.

> **Stacks Project, Tag 01PM (`general_isomorphism`).** For a finitely generated ideal `I`,
> the direct limit of `Hom_A(I ^ n, M / Mₙ)` is canonically isomorphic to the sections of `M̃`
> on `Spec(A) \ V(I)`.

```lean
public noncomputable def idealPowersHomModuloAnnihilatorColimitIsoSections (hI : I.FG) :
    colimit (idealPowersHomModuloAnnihilator A I M) ≅ sectionsOnComplement A I M
```

Declarations registered for the tag:

- [`Submodule.torsionBySet`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.torsionBySet#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/IdealPowerTorsion.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/IdealPowerTorsion.lean#L30) (StacksFrontier): “i\_power\_annihilator\_submodules”.

## Tag 01PN, an example

[Tag 01PN](https://stacks.math.columbia.edu/tag/01PN) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PrincipalIdealCounterexample.fractionSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean#L282). The attribute's comment: “first example: the section y/x on Spec(A) minus V(x), A = k[x,y,z\_n]/(x^n z\_n)”.

> The fraction `y/x`, as a section of `𝒪` on the complement of `V(x)`.

```lean
noncomputable def fractionSection :
    sectionsOnComplement (counterexampleRing k) (principalIdeal k) (counterexampleRing k)
```

**`Stacks.AlgebraicGeometry.PrincipalIdealCounterexample.fractionSection_restrict`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean#L290). The attribute's comment: “first example: that section restricts on D(x) to the fraction y/x”.

> On `D(x)`, which is all of the complement of `V(x)`, the section is the fraction `y/x`.

```lean
lemma fractionSection_restrict :
    restrictToBasicOpen (counterexampleRing k) (principalIdeal k) (counterexampleRing k)
        (x k) (x_mem_principalIdeal k) (fractionSection k) =
      basicOpenFraction (counterexampleRing k) (counterexampleRing k) (x k) 1 (y k)
```

**`Stacks.AlgebraicGeometry.PrincipalIdealCounterexample.fractionSection_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean#L299). The attribute's comment: “first example: y/x is not in the range of the map from colim\_n Hom\_A((x)^n, A)”.

> The fraction `y/x` is not obtained from a map out of any power of `(x)`.

```lean
theorem fractionSection_not_mem_range :
    fractionSection k ∉ Set.range (canonicalMapToSections (counterexampleRing k)
      (principalIdeal k) (counterexampleRing k))
```

**`Stacks.AlgebraicGeometry.PrincipalIdealCounterexample.canonicalMapToSections_not_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean#L350). The attribute's comment: “first example: the canonical map for I = (x) is not surjective”.

> The canonical map is not surjective for the principal ideal `(x)`.

```lean
theorem canonicalMapToSections_not_surjective :
    ¬ Function.Surjective (canonicalMapToSections (counterexampleRing k)
      (principalIdeal k) (counterexampleRing k))
```

**`Stacks.AlgebraicGeometry.PrincipalIdealCounterexample.canonicalMapToSections_not_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PrincipalIdealCounterexample.lean#L357). The attribute's comment: “first example: the canonical map for I = (x) is not an isomorphism”.

> The canonical map is not an isomorphism for the principal ideal `(x)`.

```lean
theorem canonicalMapToSections_not_isIso :
    ¬ IsIso (canonicalMapToSections (counterexampleRing k)
      (principalIdeal k) (counterexampleRing k))
```

**`Stacks.AlgebraicGeometry.TwoGeneratorCounterexample.gluedFractionSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean#L548). The attribute's comment: “two\_generator\_counterexample”.

> The section on `D(f) ∪ D(g)` to which the fractions `x/f` and `y/g` glue.

```lean
noncomputable def gluedFractionSection :
    sectionsOnComplement (counterexampleRing k) (twoGeneratorIdeal k)
      (counterexampleRing k)
```

**`Stacks.AlgebraicGeometry.TwoGeneratorCounterexample.gluedFractionSection_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean#L554). The attribute's comment: “two\_generator\_counterexample”.

> `f` times the glued section is `x`, i.e. the section restricts to `x/f` on `D(f)`.

```lean
theorem gluedFractionSection_f :
    f k • gluedFractionSection k =
      toComplement (counterexampleRing k) (twoGeneratorIdeal k)
        (counterexampleRing k) (x k)
```

**`Stacks.AlgebraicGeometry.TwoGeneratorCounterexample.gluedFractionSection_g`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean#L561). The attribute's comment: “two\_generator\_counterexample”.

> `g` times the glued section is `y`, i.e. the section restricts to `y/g` on `D(g)`.

```lean
theorem gluedFractionSection_g :
    g k • gluedFractionSection k =
      toComplement (counterexampleRing k) (twoGeneratorIdeal k)
        (counterexampleRing k) (y k)
```

**`Stacks.AlgebraicGeometry.TwoGeneratorCounterexample.gluedFractionSection_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean#L672). The attribute's comment: “two\_generator\_counterexample”.

> The glued fraction section is not obtained from a map out of any power of `(f,g)`.

```lean
theorem gluedFractionSection_not_mem_range :
    gluedFractionSection k ∉ Set.range (canonicalMapToSections (counterexampleRing k)
      (twoGeneratorIdeal k) (counterexampleRing k))
```

**`Stacks.AlgebraicGeometry.TwoGeneratorCounterexample.canonicalMapToSections_not_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean, line 743](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwoGeneratorCounterexample.lean#L743). The attribute's comment: “two\_generator\_counterexample”.

> The canonical map is not an isomorphism for the ideal `(f,g)`.

```lean
theorem canonicalMapToSections_not_isIso :
    ¬ IsIso (canonicalMapToSections (counterexampleRing k)
      (twoGeneratorIdeal k) (counterexampleRing k))
```

## Tag 01PQ, a lemma

[Tag 01PQ](https://stacks.math.columbia.edu/tag/01PQ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Injectivity.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Injectivity.lean#L449). The attribute's comment: “canonical\_map”.

> The canonical map `colim_n Hom_{𝒪_X}(Iⁿ, F) ⟶ Γ(X \ V(I), F)`.

```lean
noncomputable def canonicalMapToSections (I : X.IdealSheafData) (F : X.Modules) :
    Limits.colimit (idealPowHomSystem I F) ⟶ Γ(F, (I.support.compl : X.Opens))
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSections_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Injectivity.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Injectivity.lean#L467). The attribute's comment: “injective: the FIRST display colim Hom(Iⁿ, F) → Γ(U, F) is injective; X quasi-compact, I quasi-coherent of finite type, F quasi-coherent. The second display is canonicalMapToSectionsQuotient\_bijective”.

> For a quasi-compact scheme `X`, a quasi-coherent sheaf of ideals `I` of finite type and a
> quasi-coherent `𝒪_X`-module `F`, the canonical map `colim_n Hom_{𝒪_X}(Iⁿ, F) → Γ(X \ V(I), F)`
> is injective.

```lean
theorem canonicalMapToSections_injective [CompactSpace X] (I : X.IdealSheafData)
    (hFT : ∀ V : X.affineOpens, (I.ideal V).FG) (F : X.Modules) [F.IsQuasicoherent] :
    Function.Injective (canonicalMapToSections I F)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSectionsQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientColimit.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientColimit.lean#L187). The attribute's comment: “canonical map of the second display, colim Hom(Iⁿ, F/F\_n) → Γ(U, F)”.

> The canonical map `colim_n Hom_{𝒪_X}(Iⁿ, F/F_n) ⟶ Γ(X \ V(I), F)`, where `F_n` is the
> subsheaf of sections annihilated by `Iⁿ`, sending the class of `φ` to the section of `F`
> corresponding to `φ(1)`.

```lean
noncomputable def canonicalMapToSectionsQuotient :
    Limits.colimit (idealPowHomQuotientSystem I F) ⟶ Γ(F, (I.support.compl : X.Opens))
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSectionsQuotient_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientColimit.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientColimit.lean#L204). The attribute's comment: “second display colim Hom(Iⁿ, F/F\_n) → Γ(U, F) is injective; X quasi-compact, I of finite type; surjectivity is canonicalMapToSectionsQuotient\_surjective”.

> For a quasi-compact scheme `X`, a quasi-coherent sheaf of ideals `I` of finite type and a
> quasi-coherent `𝒪_X`-module `F`, the canonical map
> `colim_n Hom_{𝒪_X}(Iⁿ, F/F_n) → Γ(X \ V(I), F)` is injective.

```lean
theorem canonicalMapToSectionsQuotient_injective [CompactSpace X] :
    Function.Injective (canonicalMapToSectionsQuotient I F hFG)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSectionsQuotient_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean#L208). The attribute's comment: “clause (c), surjectivity of the second display colim Hom(Iⁿ, F/F\_n) → Γ(U, F); X quasi-compact and quasi-separated, I quasi-coherent of finite type, F quasi-coherent, F\_n the subsheaf annihilated by Iⁿ. No torsion hypothesis.”.

> **Stacks Project, Tag 01PQ, second display, surjectivity.** For a quasi-compact and
> quasi-separated scheme `X`, a quasi-coherent sheaf of ideals `I` of finite type and a
> quasi-coherent `𝒪_X`-module `F`, the canonical map
> `colim_n Hom_{𝒪_X}(Iⁿ, F/F_n) → Γ(X ∖ V(I), F)` is surjective.
>
> Quasi-separatedness of `X` is used exactly here, as in the source: it is what makes the pairwise
> intersections of a finite affine covering again finitely covered by affine opens, hence what
> bounds the exponent needed for the local morphisms to agree.

```lean
theorem canonicalMapToSectionsQuotient_surjective [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsQuasicoherent]
    (hFG : ∀ V : X.affineOpens, (I.ideal V).FG) :
    Function.Surjective (canonicalMapToSectionsQuotient I F hFG)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSectionsQuotient_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean#L231). The attribute's comment: “clause (c): the second display colim Hom(Iⁿ, F/F\_n) → Γ(U, F) is an isomorphism; X quasi-compact and quasi-separated, I quasi-coherent of finite type, F quasi-coherent”.

> **Stacks Project, Tag 01PQ, clause (c).** Let `X` be a quasi-compact and quasi-separated
> scheme, let `I ⊂ 𝒪_X` be a quasi-coherent sheaf of ideals of finite type, let `Z = V(I)` and
> `U = X ∖ Z`, let `F` be a quasi-coherent `𝒪_X`-module and let `F_n ⊂ F` be the subsheaf of
> sections annihilated by `Iⁿ`.  Then the canonical map
>
> `colim_n Hom_{𝒪_X}(Iⁿ, F/F_n) ⟶ Γ(U, F)`
>
> is an isomorphism.
>
> Injectivity is `canonicalMapToSectionsQuotient_injective` and needs only quasi-compactness;
> surjectivity is `canonicalMapToSectionsQuotient_surjective` and is where quasi-separatedness
> enters.

```lean
theorem canonicalMapToSectionsQuotient_bijective [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsQuasicoherent]
    (hFG : ∀ V : X.affineOpens, (I.ideal V).FG) :
    Function.Bijective (canonicalMapToSectionsQuotient I F hFG)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.isIso_canonicalMapToSectionsQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean#L247). The attribute's comment: “clause (c): the second display colim Hom(Iⁿ, F/F\_n) → Γ(U, F) is an isomorphism in AddCommGrpCat; X quasi-compact and quasi-separated, I quasi-coherent of finite type, F quasi-coherent”.

> **Stacks Project, Tag 01PQ, clause (c), categorically.** The canonical map
> `colim_n Hom_{𝒪_X}(Iⁿ, F/F_n) ⟶ Γ(X ∖ V(I), F)` is an isomorphism of abelian groups, for `X`
> quasi-compact and quasi-separated, `I` quasi-coherent of finite type and `F` quasi-coherent.
>
> This is `canonicalMapToSectionsQuotient_bijective` read in `AddCommGrpCat`, where a bijective
> morphism is invertible.

```lean
theorem isIso_canonicalMapToSectionsQuotient [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsQuasicoherent]
    (hFG : ∀ V : X.affineOpens, (I.ideal V).FG) :
    IsIso (canonicalMapToSectionsQuotient I F hFG)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSections_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Surjectivity.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/Surjectivity.lean#L519). The attribute's comment: “surjective (F\_n = 0)”.

> **Stacks Project, Tag 01PQ (`surjective`), the case `F_N = 0`.** Let `X` be a quasi-compact
> scheme, let `I` be a quasi-coherent sheaf of ideals of finite type and let `F` be a
> quasi-coherent `𝒪_X`-module with **no `I`-power torsion**, that is, with
> `F_N = 0` for every `N`.  Then the canonical map
> `colim_n Hom_{𝒪_X}(Iⁿ, F) → Γ(X \ V(I), F)` is surjective.
>
> Together with `canonicalMapToSections_injective` this is the second assertion of Tag 01PQ in the
> case `F_N = 0`, where `F/F_N = F`; the general assertion, which needs the quotient sheaves
> `F/F_N`, is
> `Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSectionsQuotient_bijective` of
> `StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/QuotientSurjectivity.lean`.  Note that
> quasi-separatedness of `X` is not needed for the torsion-free case proved here: the source
> glues the local morphisms over a finite cover of the pairwise intersections, whereas here the
> local sections to be glued are *unique*, by the absence of torsion, so no comparison over the
> intersections is required.

```lean
theorem canonicalMapToSections_surjective [CompactSpace X] (I : X.IdealSheafData)
    (hFT : ∀ V : X.affineOpens, (I.ideal V).FG) (F : X.Modules) [F.IsQuasicoherent]
    (hTF : NoIdealTorsion I F) :
    Function.Surjective (canonicalMapToSections I F)
```

**`Stacks.LocalCohomology.canonicalMapToSections_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CanonicalSectionsInjective.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CanonicalSectionsInjective.lean#L605). The attribute's comment: “injectivity”.

> **Stacks Project, Tag 01PQ (injectivity).** The canonical map from the colimit of
> homomorphisms out of the powers of a finite-type ideal sheaf on a quasi-compact scheme to the
> sections of a quasi-coherent module on the complement of the support is injective.

```lean
public theorem canonicalMapToSections_injective {X : Scheme.{u}} [CompactSpace X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsQuasicoherent]
    [((idealPowerMultiple I 1 (unitModule X)).toModules).IsFiniteType] :
    Function.Injective (canonicalMapToSections I F).1
```

**`AlgebraicGeometry.idealPowerAnnihilator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/IdealPowerAnnihilator.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/IdealPowerAnnihilator.lean#L159). The attribute's comment: “ideal\_power\_annihilator\_subsheaf”.

> The subsheaf of `F` whose local sections are annihilated by the `n`-th power of the
> ideal subsheaf `I`.

```lean
noncomputable def idealPowerAnnihilator
    (I : (SheafOfModules.unit.{u} X.ringCatSheaf).Submodule) (F : X.Modules) (n : ℕ) :
    F.Submodule
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.26, Tag 01PL](https://stacks.math.columbia.edu/tag/01PL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
