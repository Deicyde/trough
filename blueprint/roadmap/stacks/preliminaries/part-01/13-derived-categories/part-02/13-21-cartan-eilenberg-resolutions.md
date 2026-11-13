---
declaration: section
origin: cited
lean: CochainComplex.CartanEilenbergResolution, CochainComplex.exists_cartanEilenbergResolution, CochainComplex.CartanEilenbergResolution.spectralSequences_rightDerivedPlus
statement: formalized
proof: formalized
---

# 13.21 Cartan-Eilenberg resolutions

Section 13.21 of the Stacks Project, [Tag 015G](https://stacks.math.columbia.edu/tag/015G). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 015H, a definition

[Tag 015H](https://stacks.math.columbia.edu/tag/015H) in the Stacks Project.

**`CochainComplex.CartanEilenbergResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Basic.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Basic.lean#L52). References: EGA 0 (11.4.2), “injective, bdd below”.

> A Cartan-Eilenberg resolution of a cochain complex `K` in an abelian category: a double
> complex `I` of injective objects, vanishing in first degrees `≪ 0` and in negative second
> degrees, together with an augmentation `ε` from `K` placed in second degree `0`, such that
> the complexes `I^{p,•}`, `Ker(d₁^{p,•})`, `Im(d₁^{p,•})` and `H^p_I(I^{•,•})` are
> injective resolutions of `K^p`, `Ker(d_K^p)`, `Im(d_K^p)` and `H^p(K^•)`.

```lean
public structure CartanEilenbergResolution (K : CochainComplex C ℤ)
```

## Tag 015I, a lemma

[Tag 015I](https://stacks.math.columbia.edu/tag/015I) in the Stacks Project.

**`CochainComplex.exists_cartanEilenbergResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean, line 751](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean#L751). References: EGA 0 (11.4.2), “bounded below case”; SGA 2 VIII (1.4), “existence of resolution”.

> **Existence of Cartan-Eilenberg resolutions.** A cochain complex `K` over an abelian
> category with enough injectives which is strictly `≥ n` admits a Cartan-Eilenberg
> resolution whose double complex is strictly `≥ n` in the first direction.

```lean
public theorem _root_.CochainComplex.exists_cartanEilenbergResolution {C : Type u}
    [Category.{v} C] [Abelian C] [EnoughInjectives C] (K : CochainComplex C ℤ) (n : ℤ)
    [CochainComplex.IsStrictlyGE K n] :
    ∃ I : CochainComplex.CartanEilenbergResolution K,
      CochainComplex.IsStrictlyGE I.bicomplex n
```

## Tag 015J, a lemma

[Tag 015J](https://stacks.math.columbia.edu/tag/015J) in the Stacks Project.

**`CochainComplex.CartanEilenbergResolution.spectralSequences_rightDerivedPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Convergence.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Convergence.lean#L84). The attribute's comment: “the two spectral sequences are those of `Tot(F(I))` filtered by the first and the second coordinate; convergence to `H^*(RF(K^•))` is stated as convergence to `H^*(Tot(F(I)))` in the sense of 012U, with finite induced filtrations, together with an isomorphism `H^n(Tot(F(I))) ≅ H^n(RF(K^•))` and the abutment of both spectral sequences to `H^*(RF(K^•))`; `F` is only assumed additive”.

> **The spectral sequences of a Cartan-Eilenberg resolution** ([Stacks, Tag 015J]). Let
> `F : 𝒜 ⥤ ℬ` be an additive functor of abelian categories, `𝒜` having enough injectives, let `K^•`
> be a bounded below complex of `𝒜`, let `I^{•,•}` be a Cartan-Eilenberg resolution of `K^•` and let
> `('E_r, 'd_r)_{r ≥ 0}` and `(''E_r, ''d_r)_{r ≥ 0}` be the two spectral sequences of the double
> complex `L = F(I^{•,•})`, those of `Tot(L)` filtered by the first and by the second coordinate.
> Then
> * `'E_1^{p,q} ≅ R^qF(K^p)`, the differential `'d_1^{p,q}` being `R^qF(d_K^p)`;
> * `''E_1^{p,q} ≅ F(H^q_I(I^{•,•})^p)`, the differential `''d_1^{p,q}` being `(-1)^q` times `F`
>   of the differential of `H^q_I(I^{•,•})`, an injective resolution of `H^q(K^•)`;
> * `''E_2^{p,q} ≅ R^pF(H^q(K^•))`;
> * both spectral sequences are bounded;
> * both converge to `H^*(Tot(L))` in the sense of [Stacks, Tag 012U], and the filtrations they
>   induce on each `H^n(Tot(L))` are finite;
> * `H^n(Tot(L)) ≅ H^n(RF(K^•))`, and each spectral sequence abuts to `H^*(RF(K^•))`: every
>   `H^n(RF(K^•))` carries a finite decreasing filtration whose graded pieces are the terms
>   `E_∞^{p, n - p}`.

```lean
public theorem _root_.CochainComplex.CartanEilenbergResolution.spectralSequences_rightDerivedPlus
    {A : Type u} {B : Type u'} [Category.{v} A] [Category.{v'} B] [Abelian A] [Abelian B]
    [HasDerivedCategory.{w} A] [HasDerivedCategory.{w'} B] (F : A ⥤ B) [F.Additive]
    [EnoughInjectives A] {K : CochainComplex A ℤ} (hK : CochainComplex.plus A K)
    (I : K.CartanEilenbergResolution)
    [HomologicalComplex₂.HasTotal
      (((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex) (ComplexShape.up ℤ)] :
    let L : HomologicalComplex₂ B (ComplexShape.up ℤ) (ComplexShape.up ℤ) :=
      ((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex
    let E₁ := spectralSequenceFunctor.obj L.totalFiltration₁
    let E₂ := spectralSequenceFunctor.obj L.totalFiltration₂
    let H : ℤ → B := fun n => (DerivedCategory.Plus.homologyFunctor B n).obj
      (F.rightDerivedFunctorPlus.obj (DerivedCategory.Plus.Q.obj ⟨K, hK⟩))
    (∃ α : ∀ p q : ℤ, (E₁.page 1 zero_le_one).X (p, q) ≅ (F.rightDerivedPlus q).obj (K.X p),
      ∀ p q : ℤ, (E₁.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (α (p + 1) q).hom =
        (α p q).hom ≫ (F.rightDerivedPlus q).map (K.d p (p + 1))) ∧
    (∃ β : ∀ p q : ℤ, (E₂.page 1 zero_le_one).X (p, q) ≅ F.obj ((I.bicomplex.homology q).X p),
      ∀ p q : ℤ, (E₂.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (β (p + 1) q).hom =
        (β p q).hom ≫ (q.negOnePow • F.map ((I.bicomplex.homology q).d p (p + 1)))) ∧
    Nonempty (∀ p q : ℤ,
      (E₂.page 2 zero_le_two).X (p, q) ≅ (F.rightDerivedPlus p).obj (K.homology q)) ∧
    IsBounded E₁ ∧ IsBounded E₂ ∧
    L.ConvergesToTotalHomology₁ ∧ L.ConvergesToTotalHomology₂ ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ inducedFiltrationStep L.totalFiltration₁ n a = ⊤ ∧
      inducedFiltrationStep L.totalFiltration₁ n b = ⊥) ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ inducedFiltrationStep L.totalFiltration₂ n a = ⊤ ∧
      inducedFiltrationStep L.totalFiltration₂ n b = ⊥) ∧
    Nonempty (∀ n : ℤ, (L.total (ComplexShape.up ℤ)).homology n ≅ H n) ∧
    SpectralSequence.AbutsTo E₁ H ∧ SpectralSequence.AbutsTo E₂ H
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.21, Tag 015G](https://stacks.math.columbia.edu/tag/015G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
