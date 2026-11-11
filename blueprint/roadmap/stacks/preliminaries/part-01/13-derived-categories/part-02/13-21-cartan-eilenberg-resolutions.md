---
declaration: section
origin: cited
lean: CochainComplex.CartanEilenbergResolution, CochainComplex.exists_cartanEilenbergResolution, CochainComplex.CartanEilenbergResolution.exists_homologyIso_rightDerivedPlus
statement: formalized
proof: formalized
---

# 13.21 Cartan-Eilenberg resolutions

Section 13.21 of the Stacks Project, [Tag 015G](https://stacks.math.columbia.edu/tag/015G). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 015H, a definition

[Tag 015H](https://stacks.math.columbia.edu/tag/015H) in the Stacks Project.

**`CochainComplex.CartanEilenbergResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Basic.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/Basic.lean#L52). References: EGA 0 (11.4.2), “injective, bdd below”.

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

**`CochainComplex.exists_cartanEilenbergResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean#L749). References: EGA 0 (11.4.2), “bounded below case”; SGA 2 VIII (1.4), “existence of resolution”.

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

**`CochainComplex.CartanEilenbergResolution.exists_homologyIso_rightDerivedPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/CartanEilenbergResolutions/SpectralSequence.lean#L768). References: EGA 0 (11.4.3), “bounded below case”; EGA 0 (12.4.1), “bounded below complexes”; EGA 0 (12.1.7), “partial”.

> **The spectral sequences of a Cartan-Eilenberg resolution.** Let `F : 𝒜 ⥤ ℬ` be an
> additive functor of abelian categories, with `𝒜` having enough injectives, let `K` be a
> bounded below cochain complex of `𝒜` and let `I` be a Cartan-Eilenberg resolution of `K`.
> For the double complex `L = F(I)`: the `'E₁`-page `H^q(L^{p,•})` is the complex `R^qF(K^p)`
> in `p`, with differential induced by that of `K`; the `''E₂`-page
> `H^p_{II}(H^q_I(L^{•,•}))` is `R^pF(H^q(K^•))`; and `H^n(Tot(L))` is `H^n(RF(K^•))`, the
> abutment of both spectral sequences.

```lean
public theorem _root_.CochainComplex.CartanEilenbergResolution.exists_homologyIso_rightDerivedPlus
    {A : Type u} {B : Type u'} [Category.{v} A] [Category.{v'} B] [Abelian A] [Abelian B]
    [HasDerivedCategory.{w} A] [HasDerivedCategory.{w'} B] (F : A ⥤ B) [F.Additive]
    [EnoughInjectives A] {K : CochainComplex A ℤ} (hK : CochainComplex.plus A K)
    (I : K.CartanEilenbergResolution)
    [HomologicalComplex₂.HasTotal
      (((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex) (ComplexShape.up ℤ)] :
    (∀ q, ∃ e : ∀ p, ((((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex).X p).homology q ≅
          (F.rightDerivedPlus q).obj (K.X p),
      ∀ p p', homologyMap ((((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex).d p p') q ≫ (e p').hom =
          (e p).hom ≫ (F.rightDerivedPlus q).map (K.d p p')) ∧
    (∀ p q, Nonempty (((((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I.bicomplex).homology q).homology p ≅
          (F.rightDerivedPlus p).obj (K.homology q))) ∧
    (∀ n, Nonempty ((HomologicalComplex₂.total
        (((F.mapHomologicalComplex (ComplexShape.up ℤ)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I.bicomplex) (ComplexShape.up ℤ)).homology n ≅
          (DerivedCategory.Plus.homologyFunctor B n).obj
            (F.rightDerivedFunctorPlus.obj (DerivedCategory.Plus.Q.obj ⟨K, hK⟩))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.21, Tag 015G](https://stacks.math.columbia.edu/tag/015G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
