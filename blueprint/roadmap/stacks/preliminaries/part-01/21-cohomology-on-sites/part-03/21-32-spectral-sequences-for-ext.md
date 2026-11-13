---
declaration: section
origin: cited
lean: CochainComplex.exists_cohomologyExtSpectralSequence, CochainComplex.exists_termwiseExtSpectralSequence
statement: formalized
proof: formalized
---

# 21.32 Spectral sequences for Ext

Section 21.32 of the Stacks Project, [Tag 07A9](https://stacks.math.columbia.edu/tag/07A9). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07AA, an example

[Tag 07AA](https://stacks.math.columbia.edu/tag/07AA) in the Stacks Project.

**`CochainComplex.exists_cohomologyExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomBicomplexSpectralSequences.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomBicomplexSpectralSequences.lean#L104). The attribute's comment: “cohomology\_ext”.

> **Stacks Project, Tag 07AA, the hyper-`Ext` spectral sequence.** Let `C` be an abelian
> category with enough injectives, let `K^•` be a bounded above complex of `C` and let `F` be an
> object of `C`. There is a cohomological spectral sequence, starting on page two, with
> `E₂^{i,j} = Extⁱ(H⁻ʲ(K^•), F)`, abutting to `Extⁱ⁺ʲ(K^•, F)`.
>
> It is the spectral sequence of the total complex of the Hom bicomplex `Hom_C(K⁻ᵖ, Iᑫ)` filtered
> by the second coordinate, for `I^•` an injective resolution of `F`.

```lean
public theorem exists_cohomologyExtSpectralSequence (K : CochainComplex C ℤ)
    (hK : CochainComplex.minus C K) (F : C) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{max u v} 2,
      (∀ i j : ℤ, Nonempty
        ((E.page 2).X (i, j) ≅
          AddCommGrpCat.of (Abelian.zExt (K.homology (-j)) F i))) ∧
      SpectralSequence.AbutsTo E (fun n ↦
        AddCommGrpCat.of
          (DerivedCategory.Ext (DerivedCategory.Q.obj K)
            ((DerivedCategory.singleFunctor C 0).obj F) n))
```

**`CochainComplex.exists_termwiseExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomBicomplexSpectralSequences.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomBicomplexSpectralSequences.lean#L143). The attribute's comment: “termwise\_ext”.

> **Stacks Project, Tag 07AA, the termwise `Ext` spectral sequence.** Let `C` be an abelian
> category with enough injectives, let `K^•` be a bounded above complex of `C` and let `F` be an
> object of `C`. There is a cohomological spectral sequence, starting on page one, with
> `E₁^{i,j} = Extʲ(K⁻ⁱ, F)`, abutting to `Extⁱ⁺ʲ(K^•, F)`.
>
> It is the spectral sequence of the total complex of the Hom bicomplex `Hom_C(K⁻ᵖ, Iᑫ)` filtered
> by the first coordinate, for `I^•` an injective resolution of `F`.

```lean
public theorem exists_termwiseExtSpectralSequence (K : CochainComplex C ℤ)
    (hK : CochainComplex.minus C K) (F : C) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{max u v} 1,
      (∀ i j : ℤ, Nonempty
        ((E.page 1).X (i, j) ≅ AddCommGrpCat.of (Abelian.zExt (K.X (-i)) F j))) ∧
      SpectralSequence.AbutsTo E (fun n ↦
        AddCommGrpCat.of
          (DerivedCategory.Ext (DerivedCategory.Q.obj K)
            ((DerivedCategory.singleFunctor C 0).obj F) n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.32, Tag 07A9](https://stacks.math.columbia.edu/tag/07A9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
