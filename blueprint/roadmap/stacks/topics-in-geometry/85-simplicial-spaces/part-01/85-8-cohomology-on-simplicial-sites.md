---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.simplicialIntegerResolution, CategoryTheory.SimplicialSiteSituation.simplicialIntegerComplex, CategoryTheory.SimplicialSiteSituation.cechSectionsComplex, CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation, CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation_app_mono, CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation_app_injective, CategoryTheory.SimplicialSiteSituation.cechSectionsComplex_exactAt_of_injective, CategoryTheory.SimplicialSiteSituation.cechSectionsComplex_shortComplexZero_exact
statement: formalized
proof: formalized
---

# 85.8 Cohomology on simplicial sites

Section 85.8 of the Stacks Project, [Tag 0D76](https://stacks.math.columbia.edu/tag/0D76). 6 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09WI, a lemma

[Tag 09WI](https://stacks.math.columbia.edu/tag/09WI) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.simplicialIntegerResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolution.lean, line 2511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolution.lean#L2511). The attribute's comment: “the resolution”. References: SGA 4 VIII (8.2), “resolution of Z”.

> **Stacks 09WI.** The lower shriek images of the constant integer sheaves form an
> alternating-face resolution of the constant integer sheaf on the total site.

```lean
noncomputable def simplicialIntegerResolution (S : SimplicialSiteSituation.{u}) :
    SimplicialIntegerResolution S
```

**`CategoryTheory.SimplicialSiteSituation.simplicialIntegerComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolution.lean, line 2528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/IntegerResolution.lean#L2528). The attribute's comment: “the complex”.

> The alternating-face chain complex `… → g_{2!} Z → g_{1!} Z → g_{0!} Z` of the simplicial
> resolution of Stacks 09WI.

```lean
noncomputable abbrev simplicialIntegerComplex (S : SimplicialSiteSituation.{u}) :
    ChainComplex (Sheaf S.totalTopology Ab.{u}) ℕ
```

## Tag 0D77, a lemma

[Tag 0D77](https://stacks.math.columbia.edu/tag/0D77) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.cechSectionsComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L225). The attribute's comment: “the canonical complex”.

> The canonical complex `Γ(C_0, F_0) → Γ(C_1, F_1) → Γ(C_2, F_2) → …` of an abelian sheaf `F`
> on the total site of a simplicial site, functorially in `F`. Its augmentation by `Γ(C_total, F)`
> is `cechSectionsAugmentation`.

```lean
def cechSectionsComplex : Sheaf S.totalTopology Ab.{u} ⥤ CochainComplex Ab.{u} ℕ
```

**`CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L260). The attribute's comment: “the augmentation”.

> The augmentation `Γ(C_total, F) → Γ(C_0, F_0)` of the canonical complex, natural in the
> abelian sheaf `F`. It is the canonical restriction of a global section to
> simplicial degree zero; see `cechSectionsAugmentation_eq`.

```lean
def cechSectionsAugmentation :
    Sheaf.Γ S.totalTopology Ab.{u} ⟶ S.componentSectionsFunctor ⦋0⦌
```

**`CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation_app_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L298). The attribute's comment: “exactness in degree -1”.

> Exactness in degree `-1`: the augmentation `Γ(C_total, F) → Γ(C_0, F_0)` of the canonical
> complex is a monomorphism.

```lean
theorem cechSectionsAugmentation_app_mono (F : Sheaf S.totalTopology Ab.{u}) :
    Mono ((S.cechSectionsAugmentation).app F)
```

**`CategoryTheory.SimplicialSiteSituation.cechSectionsAugmentation_app_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L309). The attribute's comment: “exactness in degree -1”.

> Exactness in degree `-1`, concretely: the augmentation `Γ(C_total, F) → Γ(C_0, F_0)` of the
> canonical complex is injective.

```lean
theorem cechSectionsAugmentation_app_injective (F : Sheaf S.totalTopology Ab.{u}) :
    Function.Injective ((S.cechSectionsAugmentation).app F)
```

**`CategoryTheory.SimplicialSiteSituation.cechSectionsComplex_exactAt_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L377). The attribute's comment: “exactness in positive degrees for an injective sheaf”.

> Exactness in positive degrees for an injective sheaf: if `F` is an injective abelian sheaf on
> the total site, the canonical complex `Γ(C_0, F_0) → Γ(C_1, F_1) → Γ(C_2, F_2) → …` is exact at
> `Γ(C_n, F_n)` for every `n > 0`.

```lean
theorem cechSectionsComplex_exactAt_of_injective (F : Sheaf S.totalTopology Ab.{u})
    [Injective F] (n : ℕ) (hn : 0 < n) :
    ((S.cechSectionsComplex).obj F).ExactAt n
```

**`CategoryTheory.SimplicialSiteSituation.cechSectionsComplex_shortComplexZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/SectionsComplex.lean#L401). The attribute's comment: “exactness in degree 0”.

> Exactness in degree `0`: the sequence `Γ(C_total, F) → Γ(C_0, F_0) → Γ(C_1, F_1)` is exact
> at `Γ(C_0, F_0)`.

```lean
theorem cechSectionsComplex_shortComplexZero_exact (F : Sheaf S.totalTopology Ab.{u}) :
    (ShortComplex.mk ((S.cechSectionsAugmentation).app F)
      (((S.cechSectionsComplex).obj F).d 0 1)
      (S.cechSectionsAugmentation_comp_d F)).Exact
```

## Tag 09WJ, a lemma

[Tag 09WJ](https://stacks.math.columbia.edu/tag/09WJ) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.derivedSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean#L202). The attribute's comment: “the spectral sequence for K in D^+(C\_total), as a functor of K”.

> **Stacks 09WJ, the spectral sequence.** For an object `K` of `D^+(C_total)` there is a
> cohomological spectral sequence, functorial in `K`: the right derived functor, along the
> localization of the bounded below homotopy category at the quasi-isomorphisms, of the spectral
> sequence of the double complex `A^{q,p} = Γ(C_p, Z^q_p)` read from its first page.
>
> A bounded below complex of injectives `I^•` representing `K` is exactly an object at which the
> unit of this right derived functor is invertible
> (`isIso_derivedSpectralSequenceUnit_app`), so the value at `K` *is* the spectral sequence of the
> double complex `A^{q,p} = Γ(C_p, I^q_p)` of the source's proof.

```lean
def derivedSpectralSequence :
    DerivedCategory.Plus (Sheaf S.totalTopology Ab.{u}) ⥤
      CohomologicalSpectralSequence Ab.{u} 1
```

**`CategoryTheory.SimplicialSiteSituation.derivedSpectralSequence_pageOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean#L395). The attribute's comment: “the first page E\_1^\{p,q} = H^q(C\_p, K\_p) for K in D^+(C\_total), naturally in K”.

> **Stacks 09WJ, the first page.** `E_1^{p,q} = H^q(C_p, K_p)`: the first page of the spectral
> sequence of Stacks 09WJ at `(p, q)` is the sheaf cohomology on the component site `C_p` of the
> restriction of `K` to `C_p`, naturally in the object `K` of `D^+(C_total)`.
>
> Together with `isZero_derivedPageOne_d_of_ne`, which pins the shape of
> `d_1^{p,q} : E_1^{p,q} → E_1^{p+1,q}`, this is the first page and the first differential of
> Stacks 09WJ.

```lean
def derivedSpectralSequence_pageOneIso :
    S.derivedSpectralSequence ⋙ pageOneEval (n : ℤ) q ≅
      S.componentDerivedCohomologyFunctor n q
```

**`CategoryTheory.SimplicialSiteSituation.isZero_derivedPageOne_d_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean#L411). The attribute's comment: “the first differential d\_1^\{p,q} : E\_1^\{p,q} → E\_1^\{p+1,q} for K in D^+(C\_total)”.

> **Stacks 09WJ, the first differential.** `d_1^{p,q} : E_1^{p,q} → E_1^{p+1,q}`: the
> differential of the first page out of the bidegree `(p, q)` lands in the bidegree `(p + 1, q)`,
> every other component being zero. Together with the type of
> `CategoryTheory.SimplicialSiteSituation.derivedSpectralSequence`, which provides
> `d (p, q) (p + 1, q) : E_1^{p,q} ⟶ E_1^{p+1,q}`, this is the shape of `d_1` that Stacks 09WJ
> asserts.

```lean
theorem isZero_derivedPageOne_d_of_ne (K : DerivedCategory.Plus (Sheaf S.totalTopology Ab.{u}))
    (p q p' q' : ℤ) (h : (p', q') ≠ (p + 1, q)) :
    ((S.derivedSpectralSequence.obj K).page 1 le_rfl).d (p, q) (p', q') = 0
```

**`CategoryTheory.SimplicialSiteSituation.derivedSpectralSequence_abutsTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagDerived.lean#L488). The attribute's comment: “the abutment H^\{p+q}(C\_total, K) for K in D^+(C\_total)”.

> **Stacks 09WJ, the convergence.** The spectral sequence of Stacks 09WJ abuts to
> `H^{p+q}(C_total, K)`: its infinity page at `(p, q)` is the `p`-th graded piece of a finite
> filtration of the sheaf cohomology of the total site in degree `p + q`.
>
> Every object of `D^+(C_total)` is represented by a bounded below complex of injective abelian
> sheaves -- the inclusion of the bounded below homotopy category of complexes of injectives into
> `D^+(C_total)` is essentially surjective -- and at such a complex the convergence is
> `derivedSpectralSequence_abutsTo_of_injective`.

```lean
theorem derivedSpectralSequence_abutsTo
    (K : DerivedCategory.Plus (Sheaf S.totalTopology Ab.{u})) :
    CategoryTheory.SpectralSequence.AbutsTo (S.derivedSpectralSequence.obj K)
      (fun n => (S.totalDerivedCohomologyFunctor n).obj K)
```

**`CategoryTheory.SimplicialSiteSituation.cohomologySpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean#L168). The attribute's comment: “the spectral sequence, for an abelian sheaf on the total site, functorial in it”.

> **Stacks 09WJ, the spectral sequence.** For an abelian sheaf `F` on the total site of a
> simplicial-site situation there is a cohomological spectral sequence, functorial in `F`: the
> spectral sequence of the filtration by the simplicial coordinate of the double complex
> `A^{q,p} = Γ(C_p, I^q_p)` of the chosen injective resolution of `F`, presented from its first
> page.
>
> The functor laws hold because filtered homotopic morphisms of double complexes induce the same
> maps on the pages from the first on; an injective resolution is functorial only up to homotopy,
> which is why the presentation starts at the first page.

```lean
def cohomologySpectralSequence :
    Sheaf S.totalTopology Ab.{u} ⥤ CohomologicalSpectralSequence Ab.{u} 1
```

**`CategoryTheory.SimplicialSiteSituation.cohomologySpectralSequence_pageOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean#L298). The attribute's comment: “the first page E\_1^\{p,q} = H^q(C\_p, F\_p) for an abelian sheaf, naturally in it”.

> **Stacks 09WJ, the first page.** `E_1^{p,q} = H^q(C_p, F_p)`: the first page of the spectral
> sequence of the simplicial-site situation at `(p, q)` is the sheaf cohomology of the restriction
> of `F` to the component site `C_p`, naturally in the abelian sheaf `F`.
>
> Together with
> `CategoryTheory.SimplicialSiteSituation.pageOneIsoColumnHomology_hom_d`, which identifies
> `d_1^{p,q} : E_1^{p,q} → E_1^{p+1,q}` with the differential of the complex of Stacks 0D77, this
> is the first page and the first differential of Stacks 09WJ.

```lean
def cohomologySpectralSequence_pageOneIso :
    S.pageOneFunctor n q ≅ S.componentCohomologyFunctor ⦋n⦌ q
```

**`CategoryTheory.SimplicialSiteSituation.isZero_pageOne_d_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean#L323). The attribute's comment: “the first differential d\_1^\{p,q} : E\_1^\{p,q} → E\_1^\{p+1,q}”.

> **Stacks 09WJ, the first differential.** `d_1^{p,q} : E_1^{p,q} → E_1^{p+1,q}`: the
> differential of the first page out of the bidegree `(p, q)` lands in the bidegree `(p + 1, q)`,
> every other component being zero. Together with the type of
> `CategoryTheory.SimplicialSiteSituation.cohomologySpectralSequence`, which provides
> `d (p, q) (p + 1, q) : E_1^{p,q} ⟶ E_1^{p+1,q}`, this is the shape of `d_1` that Stacks 09WJ
> asserts.
>
> What that differential *is* under the identification of the first page is
> `CategoryTheory.SimplicialSiteSituation.pageOneIsoColumnHomology_hom_d`: up to the sign
> `(-1)^q`, the map induced on `H^q` by the differential of the complex of Stacks 0D77.

```lean
theorem isZero_pageOne_d_of_ne (F : Sheaf S.totalTopology Ab.{u}) (p q p' q' : ℤ)
    (h : (p', q') ≠ (p + 1, q)) :
    (((S.cohomologySpectralSequence).obj F).page 1 le_rfl).d (p, q) (p', q') = 0
```

**`CategoryTheory.SimplicialSiteSituation.cohomologySpectralSequence_abutsTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceTagSheaf.lean#L364). The attribute's comment: “the abutment H^\{p+q}(C\_total, F) for an abelian sheaf”.

> **Stacks 09WJ, the convergence.** The spectral sequence of the simplicial-site situation
> abuts to `H^{p+q}(C_total, F)`: its infinity page at `(p, q)` is the `p`-th graded piece of a
> finite filtration of the sheaf cohomology of the total site in degree `p + q`.
>
> This is `sectionsSpectralSequence_abutsTo_total`, whose abutment is the cohomology of the total
> complex of `A^{•,•}`, transported along the comparison of Stacks 0133 and read from the first
> page.

```lean
theorem cohomologySpectralSequence_abutsTo :
    CategoryTheory.SpectralSequence.AbutsTo
      ((S.cohomologySpectralSequence).obj F) (S.totalCohomologyZ F)
```

## Tag 0H0V, a remark

[Tag 0H0V](https://stacks.math.columbia.edu/tag/0H0V) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.sectionsProductSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean#L362). The attribute's comment: “the spectral sequence of the filtration by the simplicial coordinate of the product totalization, for a complex that is not bounded below; the identification of the first page with `H^q(C_p, K_p)` is not carried”.

> **Stacks 0H0V**, the spectral sequence. For a cochain complex `Z^•` of abelian sheaves on
> the total site of a simplicial-site situation, with no boundedness hypothesis, the filtration
> `F^i Tot_π^n = ∏_{p + q = n, p ≥ i} Γ(C_p, Z^q_p)` of the product totalization of
> `A^{p,q} = Γ(C_p, Z^q_p)` by the simplicial coordinate has a spectral sequence.
>
> For `Z^•` a K-injective complex of injectives representing `K` in `D(C_total)` this is the
> spectral sequence the source constructs; as in the source, no convergence is asserted.

```lean
def sectionsProductSpectralSequence : CohomologicalSpectralSequence Ab.{u} 0
```

**`CategoryTheory.SimplicialSiteSituation.sectionsProductSpectralSequenceZeroPageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean#L372). The attribute's comment: “the zeroth page of the spectral sequence is `Γ(C_p, Z^q_p)`”.

> **`E_0^{p,q} = Γ(C_p, Z^q_p)`**: the zeroth page of the spectral sequence of Stacks 0H0V is
> the complex of sections over `C_p` of the restriction of `Z^q`.
>
> The isomorphism is pinned by
> `HomologicalComplex₂.π_productTotalColumnZeroPageIso_hom`: it carries the class of an element of
> `F^p Tot_π^{p+q}` to its component in simplicial degree `p`.

```lean
def sectionsProductSpectralSequenceZeroPageIso (p : ℕ) (q : ℤ) :
    ((S.sectionsProductSpectralSequence Z).page 0 le_rfl).X ((p : ℤ), q) ≅
      (S.componentSectionsFunctor ⦋p⦌).obj (Z.X q)
```

**`CategoryTheory.SimplicialSiteSituation.sectionsProductSpectralSequenceOnePageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequence.lean#L381). The attribute's comment: “the first page of the spectral sequence is `H^q(Γ(C_p, Z^•_p))`”.

> **`E_1^{p,q} = H^q(Γ(C_p, Z^•_p))`**: the first page of the spectral sequence of Stacks 0H0V
> is the `q`-th cohomology of the complex of sections over `C_p` of the restriction of `Z^•`,
> not the `H^q(C_p, K_p)` of the statement of Stacks 0H0V.

```lean
def sectionsProductSpectralSequenceOnePageIso (p : ℕ) (q : ℤ) :
    ((S.sectionsProductSpectralSequence Z).page 1 zero_le_one).X ((p : ℤ), q) ≅
      (((S.componentSectionsFunctor ⦋p⦌).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj Z).homology q
```

**`CategoryTheory.SimplicialSiteSituation.sectionsProductSpectralSequencePageOneAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L253). The attribute's comment: “the first page of the spectral sequence is `H^q(C_p, K_p)`, for a complex that is not bounded below”.

> **Stacks 0H0V, the first page: `E_1^{p,q} = H^q(C_p, K_p)`.** For `I^•` a K-injective complex
> of abelian sheaves on the total site representing `K` in `D(C_total)`, the first page of the
> spectral sequence of the filtration by the simplicial coordinate of the product totalization of
> `A^{p,q} = Γ(C_p, I^q_p)` is the cohomology of the component site `C_p` of the restriction `K_p`.
>
> No boundedness hypothesis is made on `I^•`, as in the source. Cohomology is written in its
> derived-Hom form, and `K_p` is the restriction of `K = Q(I^•)` to the component in simplicial
> degree `p`; the proof uses that restriction to a component preserves K-injectivity, which is
> Stacks 09WH.

```lean
def sectionsProductSpectralSequencePageOneAddEquiv
    (I : CochainComplex (Sheaf S.totalTopology Ab.{u}) ℤ) [I.IsKInjective] (p : ℕ) (q : ℤ) :
    (((S.sectionsProductSpectralSequence I).page 1 zero_le_one).X ((p : ℤ), q)) ≃+
      ((DerivedCategory.singleFunctor (Sheaf (S.componentTopology ⦋p⦌) Ab.{u}) 0).obj
          (integerSheaf (S.componentTopology ⦋p⦌)) ⟶
        ((S.componentRestrictionDerived ⦋p⦌).obj (DerivedCategory.Q.obj I))⟦q⟧)
```

**`CategoryTheory.SimplicialSiteSituation.quasiIso_totalSectionsToProductTotal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L313). The attribute's comment: “`Tot_π(A^{•,•}) = RΓ(C_total, K)` for a K-injective representative, as a quasi-isomorphism of complexes”.

> **Stacks 0H0V, `Tot_π(A^{•,•}) = RΓ(C_total, K)`.** For `I^•` a K-injective complex of
> abelian sheaves on the total site, the comparison from the complex of global sections
> `Γ(C_total, I^•)` — which is `RΓ(C_total, K)` for `K = Q(I^•)` — to the product totalization of
> `A^{p,q} = Γ(C_p, I^q_p)` is a quasi-isomorphism.
>
> This is the source's chain of equalities. The global sections complex is the Hom complex out of
> the constant integer sheaf `Z`, which is `R Hom(Z, K)`; the integral resolution
> `… → g_{2!}Z → g_{1!}Z → g_{0!}Z` of Stacks 09WI resolves `Z`, so for the K-injective target
> `I^•` the Hom complex out of it computes the same thing; and that Hom complex is the product
> totalization of `A^{p,q} = Hom(g_{p!}Z, I^q) = Γ(C_p, I^q_p)`. No boundedness hypothesis is made
> on `I^•`: K-injectivity is what replaces it.

```lean
instance quasiIso_totalSectionsToProductTotal
    (I : CochainComplex (Sheaf S.totalTopology Ab.{u}) ℤ) [I.IsKInjective] :
    QuasiIso (S.totalSectionsToProductTotal I)
```

**`CategoryTheory.SimplicialSiteSituation.sectionsProductTotalHomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L328). The attribute's comment: “`H^n(Tot_π(A^{•,•})) = H^n(C_total, K)` for a K-injective representative”.

> **Stacks 0H0V, `Tot_π(A^{•,•}) = RΓ(C_total, K)` degreewise on cohomology**:
> `H^n(Tot_π(A^{•,•})) = H^n(C_total, K)`.
>
> Cohomology is written in its derived-Hom form, so the right-hand side is literally the source's
> `R Hom(Z, K)` in degree `n`, which is `RΓ(C_total, K)` because the first equality of the source
> "holds in any site".

```lean
def sectionsProductTotalHomologyAddEquiv
    (I : CochainComplex (Sheaf S.totalTopology Ab.{u}) ℤ) [I.IsKInjective] (n : ℤ) :
    ((S.sectionsProductTotal I).homology n) ≃+
      ((DerivedCategory.singleFunctor (Sheaf S.totalTopology Ab.{u}) 0).obj S.totalIntegerSheaf ⟶
        (DerivedCategory.Q.obj I)⟦n⟧)
```

**`CategoryTheory.SimplicialSiteSituation.quasiIso_globalSectionsToProductTotal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L355). The attribute's comment: “`Γ(C_total, I^•) = Tot_π(A^{•,•})` for a K-injective complex, as a quasi-isomorphism of complexes”.

> **Stacks 0H0V, `Γ(C_total, I^•) = Tot_π(A^{•,•})`.** For `I^•` a K-injective complex of
> abelian sheaves on the total site, the comparison from its complex of global sections to the
> product totalization of `A^{p,q} = Γ(C_p, I^q_p)` is a quasi-isomorphism. This is the previous
> statement with its source written as the complex of global sections rather than as the Hom
> complex out of the constant integer sheaf.

```lean
instance quasiIso_globalSectionsToProductTotal
    (I : CochainComplex (Sheaf S.totalTopology Ab.{u}) ℤ) [I.IsKInjective] :
    QuasiIso (S.globalSectionsToProductTotal I)
```

**`CategoryTheory.SimplicialSiteSituation.unboundedSpectralSequence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L369). The attribute's comment: “the spectral sequence of an arbitrary object of the unbounded derived category of the total site”.

> **Stacks 0H0V, the spectral sequence of an object `K` of `D(C_total)` with no boundedness
> hypothesis**: the spectral sequence of
> `CategoryTheory.SimplicialSiteSituation.sectionsProductSpectralSequence` for the chosen
> K-injective complex with injective terms representing `K`.

```lean
abbrev unboundedSpectralSequence (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    CohomologicalSpectralSequence Ab.{u} 0
```

**`CategoryTheory.SimplicialSiteSituation.unboundedSpectralSequencePageOneAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L381). The attribute's comment: “the first page is `E_1^{p,q} = H^q(C_p, K_p)`, for an arbitrary object of the unbounded derived category of the total site”.

> **Stacks 0H0V, the first page: `E_1^{p,q} = H^q(C_p, K_p)`** for an arbitrary object `K` of
> `D(C_total)`.
>
> The first differential of the first page of a cohomological spectral sequence has bidegree
> `(1, 0)` by construction, so under this identification it is a map
> `H^q(C_p, K_p) → H^q(C_{p + 1}, K_{p + 1})`, as the source's reference to Stacks 09WJ asks.

```lean
def unboundedSpectralSequencePageOneAddEquiv
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) (p : ℕ) (q : ℤ) :
    (((S.unboundedSpectralSequence K).page 1 zero_le_one).X ((p : ℤ), q)) ≃+
      ((DerivedCategory.singleFunctor (Sheaf (S.componentTopology ⦋p⦌) Ab.{u}) 0).obj
          (integerSheaf (S.componentTopology ⦋p⦌)) ⟶
        ((S.componentRestrictionDerived ⦋p⦌).obj K)⟦q⟧)
```

**`CategoryTheory.SimplicialSiteSituation.unboundedProductTotalHomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/CohomologySpectralSequenceUnbounded.lean#L398). The attribute's comment: “`H^n(Tot_π(A^{•,•})) = H^n(C_total, K)` for an arbitrary object of the unbounded derived category of the total site”.

> **Stacks 0H0V, `Tot_π(A^{•,•}) = RΓ(C_total, K)`** for an arbitrary object `K` of
> `D(C_total)`, degreewise on cohomology.

```lean
def unboundedProductTotalHomologyAddEquiv
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) (n : ℤ) :
    ((S.sectionsProductTotal (S.totalKInjectiveModel K)).homology n) ≃+
      ((DerivedCategory.singleFunctor (Sheaf S.totalTopology Ab.{u}) 0).obj S.totalIntegerSheaf ⟶
        K⟦n⟧)
```

## Tag 0H0W, a lemma

[Tag 0H0W](https://stacks.math.columbia.edu/tag/0H0W) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.subsingleton_hom_totalIntegerSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/VanishingCohomology.lean, line 704](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/VanishingCohomology.lean#L704). The attribute's comment: “part (1): vanishing of H^0”.

> **Stacks 0H0W (1).** In the situation of Stacks 09WE, let `K` be an object of
> `D(C_total)`. If `H^{-p}(C_p, K_p) = 0` for all `p ≥ 0`, then `H^0(C_total, K) = 0`.
>
> Cohomology is written in its derived-Hom form: `H^i(C, K)` is the group of morphisms from the
> constant integer sheaf of `C`, placed in degree zero, to `K[i]`; and the restriction `K_p` of
> `K` to the component in simplicial degree `p` is `componentRestrictionDerived S ⦋p⦌` applied
> to `K`.

```lean
theorem subsingleton_hom_totalIntegerSheaf
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u}))
    (h : ∀ p : ℕ, Subsingleton
      ((DerivedCategory.singleFunctor (Sheaf (S.componentTopology ⦋p⦌) Ab.{u}) 0).obj
          (integerSheaf (S.componentTopology ⦋p⦌)) ⟶
        ((componentRestrictionDerived S ⦋p⦌).obj K)⟦-(p : ℤ)⟧)) :
    Subsingleton ((DerivedCategory.singleFunctor (Sheaf S.totalTopology Ab.{u}) 0).obj
      S.totalIntegerSheaf ⟶ K)
```

**`CategoryTheory.SimplicialSiteSituation.subsingleton_hom_totalIntegerSheaf_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/VanishingCohomology.lean, line 745](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/VanishingCohomology.lean#L745). The attribute's comment: “part (2): vanishing of RΓ”.

> **Stacks 0H0W (2).** In the situation of Stacks 09WE, let `K` be an object of
> `D(C_total)`. If `RΓ(C_p, K_p) = 0` for all `p ≥ 0`, then `RΓ(C_total, K) = 0`.
>
> Vanishing of `RΓ` is the vanishing of every cohomology group, written in derived-Hom form as in
> `subsingleton_hom_totalIntegerSheaf`.

```lean
theorem subsingleton_hom_totalIntegerSheaf_shift
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u}))
    (h : ∀ (p : ℕ) (i : ℤ), Subsingleton
      ((DerivedCategory.singleFunctor (Sheaf (S.componentTopology ⦋p⦌) Ab.{u}) 0).obj
          (integerSheaf (S.componentTopology ⦋p⦌)) ⟶
        ((componentRestrictionDerived S ⦋p⦌).obj K)⟦i⟧)) (i : ℤ) :
    Subsingleton ((DerivedCategory.singleFunctor (Sheaf S.totalTopology Ab.{u}) 0).obj
      S.totalIntegerSheaf ⟶ K⟦i⟧)
```

## Tag 0DBZ, a lemma

[Tag 0DBZ](https://stacks.math.columbia.edu/tag/0DBZ) in the Stacks Project.

**`Stacks.Cohomology.SimplicialComponent.cohomologyObj_iso_component`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumNaturality/ComponentCohomology.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumNaturality/ComponentCohomology.lean#L142).

> **Stacks 0DBZ.** Cohomology over an object of one simplicial component agrees with cohomology
> over the corresponding object of the total site, with coefficients restricted to that component.
>
> The restriction is the pullback of sheaves along the cocontinuous component inclusion. This is
> Stacks 03YU statement 2 — `Stacks.Cohomology.BiggerSite.cohomologyObjIso`, read at an arbitrary
> `Ext` universe as `cohomologyObjIsoExtUniv` — applied to the component inclusion, whose exactness
> hypothesis is Stacks 09WG (7),
> `Stacks.Sites.ComponentSumFormula.preservesMonomorphisms_sheafPullback_componentFunctor`.

```lean
def cohomologyObj_iso_component
    (S : SimplicialSiteSituation.{u}) (n : SimplexCategory) (U : S.component n)
    [HasSheafify S.totalTopology Ab.{u}]
    [HasSheafify (S.componentTopology n) Ab.{u}]
    [HasExt.{w} (Sheaf S.totalTopology Ab.{u})]
    [HasExt.{w} (Sheaf (S.componentTopology n) Ab.{u})]
    (F : Sheaf S.totalTopology Ab.{u}) (p : ℕ) :
    Sheaf.H'.{w, u, u} F p ((SimplicialSiteSituation.componentFunctor S n).obj U) ≅
      Sheaf.H'.{w, u, u}
        (((SimplicialSiteSituation.componentFunctor S n).sheafPullbackCocontinuous
          Ab.{u} (S.componentTopology n) S.totalTopology).obj F) p U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.8, Tag 0D76](https://stacks.math.columbia.edu/tag/0D76)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
