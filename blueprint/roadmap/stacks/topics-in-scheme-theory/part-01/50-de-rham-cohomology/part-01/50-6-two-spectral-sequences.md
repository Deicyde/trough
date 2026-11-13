---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.hodgeToDeRhamFirstPage, AlgebraicGeometry.SheafOfModules.exists_hodgeToDeRham_and_conjugate_spectralSequences, AlgebraicGeometry.SheafOfModules.nonempty_deRhamCohomologyAbelian_zero_iso_kernel, AlgebraicGeometry.SheafOfModules.nonempty_deRhamCohomologyAbelian_zero_iso_cohomologySheaf, AlgebraicGeometry.SheafOfModules.exists_exact_deRhamCohomologyAbelian_one_two, AlgebraicGeometry.Scheme.Hom.exists_hodgeToDeRham_and_conjugate_spectralSequences
statement: formalized
proof: formalized
---

# 50.6 Two spectral sequences

Section 50.6 of the Stacks Project, [Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FM6, the section

[Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeToDeRhamFirstPage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRham.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRham.lean#L99). The attribute's comment: “the rows E\_1^\{•,q} of the first page of the Hodge-to-de Rham spectral sequence as cochain complexes: E\_1^\{p,q} = H^q(X, Ω^p) with d\_1 induced by the de Rham differential; the spectral sequences are exists\_hodgeToDeRham\_and\_conjugate\_spectralSequences”. References: SGA 7 XXII (3.3), “First page of (3.3.2)”.

> **The `q`-th row `E_1^{•, q}` of the first page of the Hodge-to-de Rham spectral sequence of
> Stacks Section 0FM6.** The term in position `p` is the Hodge cohomology group
> `H^q(X, Ω^p_{𝒪_X/A})` and the differential `d_1^{p, q} : H^q(X, Ω^p) ⟶ H^q(X, Ω^{p + 1})` is the
> map induced by the de Rham differential `d : Ω^p ⟶ Ω^{p + 1}`; it squares to zero because the de
> Rham differential does.

```lean
abbrev hodgeToDeRhamFirstPage (q : ℕ) : CochainComplex AddCommGrpCat.{u} ℕ
```

**`AlgebraicGeometry.SheafOfModules.exists_hodgeToDeRham_and_conjugate_spectralSequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean#L109). The attribute's comment: “the two spectral sequences of a Cartan-Eilenberg resolution of the de Rham complex (Tag 015J for Γ(X, -)), both bounded and converging to H^*\_dR(X/S): the Hodge-to-de Rham spectral sequence with E\_1^\{p,q} = H^q(X, Ω^p) and d\_1 induced by d, and the conjugate spectral sequence with E\_2^\{p,q} = H^p(X, H^q(Ω^•)); the resolution is taken in abelian sheaves, the category in which H^*\_dR(X/S) is computed”.

> **The Hodge-to-de Rham and the conjugate spectral sequences** of Stacks Section 0FM6.
>
> There are two cohomological spectral sequences `E₁` (starting at the page `0`) and `E₂` such that
>
> * `E₁` is the Hodge-to-de Rham spectral sequence: its first page is
>   `E_1^{p,q} = H^q(X, Ω^p_{X/S})`, and under this identification `d_1^{p,q}` is the map
>   `H^q(X, Ω^p_{X/S}) → H^q(X, Ω^{p+1}_{X/S})` induced by the de Rham differential;
> * `E₂` is the conjugate spectral sequence: its second page is `E_2^{p,q} = H^p(X, 𝓗^q)`, with
>   `𝓗^q = H^q(Ω^•_{X/S})` the `q`-th cohomology sheaf of the de Rham complex;
> * both are bounded, and both converge to `H^*_{dR}(X/S)`: every `H^n_{dR}(X/S)` carries a finite
>   decreasing filtration whose graded pieces are the terms `E_∞^{p, n - p}`.
>
> Both come from [Stacks, Tag 015J] applied to `Γ(X, -)` and a Cartan-Eilenberg resolution of the
> de Rham complex ([Stacks, Tag 015I]).

```lean
theorem exists_hodgeToDeRham_and_conjugate_spectralSequences :
    ∃ E₁ E₂ : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∃ α : ∀ p q : ℤ, (E₁.page 1 zero_le_one).X (p, q) ≅
          ((sectionsFunctor X.carrier ⊤).rightDerivedPlus q).obj
            ((deRhamAbelianComplexInt B D).X p),
        ∀ p q : ℤ, (E₁.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (α (p + 1) q).hom =
          (α p q).hom ≫ ((sectionsFunctor X.carrier ⊤).rightDerivedPlus q).map
            ((deRhamAbelianComplexInt B D).d p (p + 1))) ∧
      Nonempty (∀ p q : ℤ, (E₂.page 2 zero_le_two).X (p, q) ≅
        ((sectionsFunctor X.carrier ⊤).rightDerivedPlus p).obj
          ((deRhamAbelianComplexInt B D).homology q)) ∧
      IsBounded E₁ ∧ IsBounded E₂ ∧
      SpectralSequence.AbutsTo E₁ (deRhamCohomologyAbelian B D) ∧
      SpectralSequence.AbutsTo E₂ (deRhamCohomologyAbelian B D)
```

**`AlgebraicGeometry.SheafOfModules.nonempty_deRhamCohomologyAbelian_zero_iso_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean#L189). The attribute's comment: “the conclusion read off the Hodge-to-de Rham spectral sequence in degree 0: H^0\_dR(X/S) = Ker(d : H^0(X, O\_X) → H^0(X, Ω^1\_\{X/S})), with O\_X = Ω^0\_\{X/S} the degree 0 term of the de Rham complex”.

> **`H^0_{dR}(X/S) = Ker(d : H^0(X, 𝒪_X) → H^0(X, Ω^1_{X/S}))`**, read off the Hodge-to-de Rham
> spectral sequence of Stacks Section 0FM6: in total degree `0` only `E_2^{0,0}` survives, and
> `E_2^{0,0}` is the kernel of `d_1^{0,0} : H^0(X, Ω^0_{X/S}) → H^0(X, Ω^1_{X/S})`, the map induced on
> `H^0(X, -)` by the de Rham differential `d : Ω^0_{X/S} = 𝒪_X → Ω^1_{X/S}`.

```lean
theorem nonempty_deRhamCohomologyAbelian_zero_iso_kernel :
    Nonempty (deRhamCohomologyAbelian B D 0 ≅
      kernel (((sectionsFunctor X.carrier ⊤).rightDerivedPlus 0).map
        ((deRhamAbelianComplexInt B D).d 0 1)))
```

**`AlgebraicGeometry.SheafOfModules.nonempty_deRhamCohomologyAbelian_zero_iso_cohomologySheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean#L236). The attribute's comment: “the conclusion read off the conjugate spectral sequence in degree 0: H^0\_dR(X/S) = H^0(X, H^0), with H^0 = H^0(Ω^•\_\{X/S}) the zeroth cohomology sheaf”.

> **`H^0_{dR}(X/S) = H^0(X, 𝓗^0)`**, read off the conjugate spectral sequence of Stacks Section
> 0FM6: in total degree `0` only `E_2^{0,0} = H^0(X, 𝓗^0)` survives, where `𝓗^0 = H^0(Ω^•_{X/S})`
> is the zeroth cohomology sheaf of the de Rham complex.

```lean
theorem nonempty_deRhamCohomologyAbelian_zero_iso_cohomologySheaf :
    Nonempty (deRhamCohomologyAbelian B D 0 ≅
      ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 0).obj
        ((deRhamAbelianComplexInt B D).homology 0))
```

**`AlgebraicGeometry.SheafOfModules.exists_exact_deRhamCohomologyAbelian_one_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean#L254). The attribute's comment: “the exact sequence read off the conjugate spectral sequence in degree 1: 0 → H^1(X, H^0) → H^1\_dR(X/S) → H^0(X, H^1) → H^2(X, H^0) → H^2\_dR(X/S)”.

> **The exact sequence of Stacks Section 0FM6 in degrees `1` and `2`**, read off the conjugate
> spectral sequence: with `𝓗^q = H^q(Ω^•_{X/S})` the cohomology sheaves of the de Rham complex,
> there is an exact sequence
> `0 → H^1(X, 𝓗^0) → H^1_{dR}(X/S) → H^0(X, 𝓗^1) → H^2(X, 𝓗^0) → H^2_{dR}(X/S)`.
> It is the five term exact sequence of the first-quadrant spectral sequence
> `E_2^{p,q} = H^p(X, 𝓗^q) ⇒ H^{p+q}_{dR}(X/S)`, the third map being `d_2^{0,1}`.

```lean
theorem exists_exact_deRhamCohomologyAbelian_one_two :
    ∃ (a : ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 1).obj
          ((deRhamAbelianComplexInt B D).homology 0) ⟶ deRhamCohomologyAbelian B D 1)
      (b : deRhamCohomologyAbelian B D 1 ⟶ ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 0).obj
          ((deRhamAbelianComplexInt B D).homology 1))
      (c : ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 0).obj
          ((deRhamAbelianComplexInt B D).homology 1) ⟶
        ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 2).obj
          ((deRhamAbelianComplexInt B D).homology 0))
      (t : ((sectionsFunctor X.carrier ⊤).rightDerivedPlus 2).obj
          ((deRhamAbelianComplexInt B D).homology 0) ⟶ deRhamCohomologyAbelian B D 2)
      (hab : a ≫ b = 0) (hbc : b ≫ c = 0) (hct : c ≫ t = 0),
      Mono a ∧ (ShortComplex.mk a b hab).Exact ∧ (ShortComplex.mk b c hbc).Exact ∧
        (ShortComplex.mk c t hct).Exact
```

**`AlgebraicGeometry.Scheme.Hom.exists_hodgeToDeRham_and_conjugate_spectralSequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/TwoSpectralSequences.lean#L294). The attribute's comment: “for a morphism of schemes X → S: the Hodge-to-de Rham spectral sequence E\_1^\{p,q} = H^q(X, Ω^p\_\{X/S}) with d\_1 induced by d, and the conjugate spectral sequence E\_2^\{p,q} = H^p(X, H^q(Ω^•\_\{X/S})), both bounded and converging to H^*\_dR(X/S)”.

> **The Hodge-to-de Rham and the conjugate spectral sequences of a morphism of schemes**
> `f : X → S` (Stacks Section 0FM6): two bounded spectral sequences converging to
> `H^*_{dR}(X/S)` (`AlgebraicGeometry.Scheme.Hom.deRhamCohomology`), the first with
> `E_1^{p,q} = H^q(X, Ω^p_{X/S})` and `d_1` induced by the de Rham differential, the second with
> `E_2^{p,q} = H^p(X, 𝓗^q)`. This is
> `AlgebraicGeometry.SheafOfModules.exists_hodgeToDeRham_and_conjugate_spectralSequences` for
> `f^{-1}𝒪_S ⟶ 𝒪_X`.

```lean
theorem exists_hodgeToDeRham_and_conjugate_spectralSequences :
    ∃ E₁ E₂ : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∃ α : ∀ p q : ℤ, (E₁.page 1 zero_le_one).X (p, q) ≅
          ((Stacks.Cohomology.Leray.sectionsFunctor X.carrier ⊤).rightDerivedPlus q).obj
            ((SheafOfModules.deRhamAbelianComplexInt (deRhamAlgebras f)
              (SheafOfModules.deRhamDifferential (deRhamAlgebras f))).X p),
        ∀ p q : ℤ, (E₁.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (α (p + 1) q).hom =
          (α p q).hom ≫ ((Stacks.Cohomology.Leray.sectionsFunctor X.carrier ⊤).rightDerivedPlus
            q).map ((SheafOfModules.deRhamAbelianComplexInt (deRhamAlgebras f)
              (SheafOfModules.deRhamDifferential (deRhamAlgebras f))).d p (p + 1))) ∧
      Nonempty (∀ p q : ℤ, (E₂.page 2 zero_le_two).X (p, q) ≅
        ((Stacks.Cohomology.Leray.sectionsFunctor X.carrier ⊤).rightDerivedPlus p).obj
          ((SheafOfModules.deRhamAbelianComplexInt (deRhamAlgebras f)
            (SheafOfModules.deRhamDifferential (deRhamAlgebras f))).homology q)) ∧
      IsBounded E₁ ∧ IsBounded E₂ ∧
      SpectralSequence.AbutsTo E₁ (f.deRhamCohomology) ∧
      SpectralSequence.AbutsTo E₂ (f.deRhamCohomology)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.6, Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
