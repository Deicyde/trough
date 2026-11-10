---
declaration: section
origin: cited
lean: Stacks.AmpleFamilyCartier.exists_isAmpleFamily_of_isAmpleOnComplement_cover, Stacks.DenseOpenAdmissibleBlowup.exists_isCompact_dense_admissibleBlowup_isAmpleFamily, Stacks.BlowupAmpleFamily.exists_finitePresentation_proper_completelyDecomposed_isAmpleFamily
statement: formalized
proof: formalized
---

# 37.80 Blowing up and ample families of invertible modules

Section 37.80 of the Stacks Project, [Tag 0GTR](https://stacks.math.columbia.edu/tag/0GTR). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GTS, a lemma

[Tag 0GTS](https://stacks.math.columbia.edu/tag/0GTS) in the Stacks Project.

**`Stacks.AmpleFamilyCartier.exists_isAmpleFamily_of_isAmpleOnComplement_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AmpleFamilyCartier/AmpleFamily.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AmpleFamilyCartier/AmpleFamily.lean#L153).

> **[Stacks, Tag 0GTS].** Let `X` be a scheme, let `D 0, …, D (m-1)` be effective Cartier
> divisors on `X` and `L 0, …, L (m-1)` invertible `𝒪_X`-modules such that the divisors have empty
> common intersection (every point lies in the complement of some `D i`) and `L i` restricted to
> `X ∖ D i` is ample. Then `X` has an ample family of invertible modules.

```lean
theorem exists_isAmpleFamily_of_isAmpleOnComplement_cover {m : ℕ}
    (D : Fin m → X.IdealSheafData) (L : Fin m → X.Modules)
    (hD : ∀ i, Stacks.Divisors.IsEffectiveCartierDivisor (D i))
    (hL : ∀ i, Stacks.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L i))
    (hcover : ∀ x : X, ∃ i, x ∈ (D i).support.compl)
    (hample : ∀ i, IsAmpleOnComplement (D i) (L i)) :
    ∃ (J : Type u) (N : J → X.Modules), X.IsAmpleFamily N
```

## Tag 0GTT, a lemma

[Tag 0GTT](https://stacks.math.columbia.edu/tag/0GTT) in the Stacks Project.

**`Stacks.DenseOpenAdmissibleBlowup.exists_isCompact_dense_admissibleBlowup_isAmpleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DenseOpenAdmissibleBlowup/AmpleFamily.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DenseOpenAdmissibleBlowup/AmpleFamily.lean#L42).

> **[Stacks, Tag 0GTT].** Let `X` be a quasi-compact and quasi-separated scheme with finitely
> many irreducible components. There exist a quasi-compact dense open `U ⊆ X` and a `U`-admissible
> blowup `X' ⟶ X` such that `X'` has an ample family of invertible modules.

```lean
public theorem exists_isCompact_dense_admissibleBlowup_isAmpleFamily
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    [Finite (irreducibleComponents X)] :
    ∃ U : X.Opens, IsCompact (U : Set X) ∧ Dense (U : Set X) ∧
      ∃ (X' : Scheme.{u}) (f : X' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup U f ∧
        ∃ (J : Type u) (N : J → X'.Modules), X'.IsAmpleFamily N
```

## Tag 0GTU, a proposition

[Tag 0GTU](https://stacks.math.columbia.edu/tag/0GTU) in the Stacks Project.

**`Stacks.BlowupAmpleFamily.exists_finitePresentation_proper_completelyDecomposed_isAmpleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BlowupAmpleFamily/Noetherian.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BlowupAmpleFamily/Noetherian.lean#L187).

> **[Stacks, Tag 0GTU].** Let `X` be a quasi-compact and quasi-separated scheme. There is a
> morphism of schemes `f : Y ⟶ X` which is of finite presentation, proper and completely
> decomposed ([Stacks, Tag 0GTI]) and such that `Y` has an ample family of invertible modules.
>
> The reduction to a base of finite type over `ℤ` is
> `exists_finitePresentation_proper_completelyDecomposed_isAmpleFamily_of_finiteTypeCase`, and the
> case of such a base, which is Noetherian, is
> `exists_finitePresentation_proper_completelyDecomposed_isAmpleFamily_of_isNoetherian`.

```lean
theorem exists_finitePresentation_proper_completelyDecomposed_isAmpleFamily
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), FinitePresentation f ∧ IsProper f ∧
      IsCompletelyDecomposed f ∧ ∃ (J : Type u) (N : J → Y.Modules), Y.IsAmpleFamily N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.80, Tag 0GTR](https://stacks.math.columbia.edu/tag/0GTR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
