---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.PicardBaseChange.exists_mulEquiv_globalSections_coherentMul_of_faithfullyFlat_trivialization, Stacks.AlgebraicGeometry.PicardBaseChange.invertible_globalSections_tensorInverse_of_faithfullyFlat_trivialization, Stacks.AlgebraicGeometry.PicardBaseChange.invertible_globalSections_of_faithfullyFlat_trivialization, Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_faithfullyFlat, Stacks.AlgebraicGeometry.PicardBaseChange.injective_schemePullbackClass_of_faithfullyFlat, Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_fieldExtension, Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_finiteDimensional, Stacks.ProjectiveLine.subsingleton_picardGroup_basicOpen_map_of_residueFieldAlgHom
statement: formalized
proof: formalized
---

# 33.30 Picard groups of varieties

Section 33.30 of the Stacks Project, [Tag 0BEG](https://stacks.math.columbia.edu/tag/0BEG). 5 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CDX, a lemma

[Tag 0CDX](https://stacks.math.columbia.edu/tag/0CDX) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PicardBaseChange.exists_mulEquiv_globalSections_coherentMul_of_faithfullyFlat_trivialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/CoherentMul.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/CoherentMul.lean#L85). The attribute's comment: “multiplication is an isomorphism”.

> **Stacks Project, Tag 0CDX, the clause that the multiplication is an isomorphism.** For a
> quasi-compact, quasi-separated scheme `X` over `A`, a faithfully flat ring map `φ : A →+* B` and
> an invertible `𝒪_X`-module `L` whose pullback to `X_B` is trivial, the canonical multiplication
>
> `Γ(X, L) ⊗_{Γ(X, 𝒪_X)} Γ(X, L^{⊗ -1}) ⟶ Γ(X, 𝒪_X)`
>
> is an isomorphism. The multiplication is the coherent multiplication of Tag 01CU in degrees
> `(1, -1)`, written out on pure tensors.

```lean
theorem exists_mulEquiv_globalSections_coherentMul_of_faithfullyFlat_trivialization
    {A B : Type u} [CommRing A] [CommRing B] (φ : A →+* B) (hφ : φ.FaithfullyFlat)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [CompactSpace X] [QuasiSeparatedSpace X]
    (L : X.Modules)
    [_root_.AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (hL : _root_.AlgebraicGeometry.SheafOfModules.IsTrivial
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).presheaf
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).ringCatSheaf.property
      ((Scheme.Modules.pullback
        (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ)))).obj L)) :
    letI : Module Γ(X, ⊤)
        ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤)) :=
      ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤)).isModule
    ∃ e : TensorProduct Γ(X, ⊤) Γ(L, ⊤)
        ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤))
        ≃ₗ[Γ(X, ⊤)] Γ(X, ⊤),
      ∀ s t, e (TensorProduct.tmul Γ(X, ⊤) s t) =
        (((tensorPowerCoherence X.presheaf X.ringCatSheaf.property L).mulIso 1 (-1)).hom.val.app
            (.op ⊤)).hom
          (((Stacks.SheafOfModules.TensorSheafification.toSheafify X.presheaf
            X.ringCatSheaf.property
            ((PresheafOfModules.tensorObj (O := X.presheaf)
              ((tensorPower X.presheaf X.ringCatSheaf.property L 1).val)
              ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val)))).app (.op ⊤)).hom
            ((((tensorPowerOneIso X.presheaf X.ringCatSheaf.property L).inv.val.app
              (.op ⊤)).hom s) ⊗ₜ[Γ(X, ⊤)] t))
```

**`Stacks.AlgebraicGeometry.PicardBaseChange.invertible_globalSections_tensorInverse_of_faithfullyFlat_trivialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/InverseSections.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/InverseSections.lean#L189). The attribute's comment: “global sections of the inverse sheaf”.

> **Stacks Project, Tag 0CDX, the clause about the global sections of the inverse sheaf.** For
> a quasi-compact, quasi-separated scheme `X` over `A`, a faithfully flat ring map `φ : A →+* B`
> and an invertible `𝒪_X`-module `L` whose pullback to `X_B` is trivial, the global sections
> `Γ(X, L^{⊗ -1})` of the inverse tensor power form an invertible module over the global functions
> `Γ(X, 𝒪_X)`.

```lean
theorem invertible_globalSections_tensorInverse_of_faithfullyFlat_trivialization
    {A B : Type u} [CommRing A] [CommRing B] (φ : A →+* B) (hφ : φ.FaithfullyFlat)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [CompactSpace X] [QuasiSeparatedSpace X]
    (L : X.Modules)
    [hinv : IsInvertible X.presheaf X.ringCatSheaf.property L]
    (hL : IsTrivial
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).presheaf
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).ringCatSheaf.property
      ((Scheme.Modules.pullback
        (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ)))).obj L)) :
    letI : Module Γ(X, ⊤)
        ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤)) :=
      ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤)).isModule
    Module.Invertible Γ(X, ⊤)
      ((tensorPower X.presheaf X.ringCatSheaf.property L (-1)).val.obj (.op ⊤))
```

**`Stacks.AlgebraicGeometry.PicardBaseChange.invertible_globalSections_of_faithfullyFlat_trivialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/Sections.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/Sections.lean#L157). The attribute's comment: “global sections of the sheaf”.

> **Stacks Project, Tag 0CDX, the clause about the global sections of the sheaf.** For a
> quasi-compact, quasi-separated scheme `X` over `A`, a faithfully flat ring map `φ : A →+* B` and
> an invertible `𝒪_X`-module `L` whose pullback to `X_B` is trivial, the global sections `Γ(X, L)`
> form an invertible module over the global functions `Γ(X, 𝒪_X)`.

```lean
theorem invertible_globalSections_of_faithfullyFlat_trivialization
    {A B : Type u} [CommRing A] [CommRing B] (φ : A →+* B) (hφ : φ.FaithfullyFlat)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [CompactSpace X] [QuasiSeparatedSpace X]
    (L : X.Modules)
    [hinv : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.property L]
    (hL : AlgebraicGeometry.SheafOfModules.IsTrivial
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).presheaf
      (Limits.pullback f (Spec.map (CommRingCat.ofHom φ))).ringCatSheaf.property
      ((Scheme.Modules.pullback
        (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ)))).obj L)) :
    Module.Invertible Γ(X, ⊤) Γ(L, ⊤)
```

## Tag 0CDY, a lemma

[Tag 0CDY](https://stacks.math.columbia.edu/tag/0CDY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean#L222).

> **Stacks Project, Tag 0CDY.** Let `A → B` be a faithfully flat ring map and let `X` be a
> scheme over `A` which is quasi-compact and quasi-separated and whose ring of global functions
> `H⁰(X, 𝒪_X)` is semi-local. Then the pullback map `Pic(X) → Pic(X_B)` is injective.

```lean
theorem injective_picardPullback_of_faithfullyFlat
    {A B : Type u} [CommRing A] [CommRing B] (φ : A →+* B) (hφ : φ.FaithfullyFlat)
    (f : X ⟶ Spec (.of A)) [CompactSpace X] [QuasiSeparatedSpace X]
    [Finite (MaximalSpectrum Γ(X, ⊤))] :
    Function.Injective (Stacks.Picard.schemePullbackClassHom
      (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ))))
```

**`Stacks.AlgebraicGeometry.PicardBaseChange.injective_schemePullbackClass_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/PuncturedSpectrumCompletion.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/PuncturedSpectrumCompletion.lean#L219).

> **Stacks Project, Tag 0CDY.** Let `A → B` be faithfully flat and let `X` be a quasi-compact,
> quasi-separated scheme over `A` whose ring of global functions is semilocal. Then pullback to the
> base change `X_B` is injective on Picard groups.

```lean
theorem injective_schemePullbackClass_of_faithfullyFlat
    {R S : Type u} [CommRing R] [CommRing S] (φ : R →+* S) (hφ : φ.FaithfullyFlat)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [CompactSpace X] [QuasiSeparatedSpace X]
    [Finite (MaximalSpectrum Γ(X, ⊤))] :
    Function.Injective (Stacks.Picard.schemePullbackClass
      (pullback.fst f (Spec.map (CommRingCat.ofHom φ))))
```

## Tag 0CC5, a lemma

[Tag 0CC5](https://stacks.math.columbia.edu/tag/0CC5) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean#L293). The attribute's comment: “The lemma proper; the parenthetical sufficient condition `dim_k H⁰(X, 𝒪_X) < ∞` for semi-locality is `injective_picardPullback_of_finiteDimensional`”.

> **Stacks Project, Tag 0CC5.** Let `k'/k` be a field extension and let `X` be a scheme over
> `k` such that (1) `X` is quasi-compact and quasi-separated, and (2) `R = H⁰(X, 𝒪_X)` is
> semi-local. Then the pullback map `Pic(X) → Pic(X_{k'})` is injective.

```lean
theorem injective_picardPullback_of_fieldExtension
    {k k' : Type u} [Field k] [Field k'] (φ : k →+* k')
    (f : X ⟶ Spec (.of k)) [CompactSpace X] [QuasiSeparatedSpace X]
    [Finite (MaximalSpectrum Γ(X, ⊤))] :
    Function.Injective (Stacks.Picard.schemePullbackClassHom
      (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ))))
```

**`Stacks.AlgebraicGeometry.PicardBaseChange.injective_picardPullback_of_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/Injectivity.lean#L306). The attribute's comment: “The parenthetical sufficient condition `dim_k H⁰(X, 𝒪_X) < ∞` for hypothesis (2); the lemma proper is `injective_picardPullback_of_fieldExtension`”.

> **Stacks Project, Tag 0CC5** with its parenthetical hypothesis: hypothesis (2) holds as soon
> as `dim_k H⁰(X, 𝒪_X)` is finite, `H⁰(X, 𝒪_X)` being then Artinian and hence semi-local.

```lean
theorem injective_picardPullback_of_finiteDimensional
    {k k' : Type u} [Field k] [Field k'] (φ : k →+* k')
    (f : X ⟶ Spec (.of k)) [CompactSpace X] [QuasiSeparatedSpace X]
    (hfd : letI := globalSectionsAlgebra f; FiniteDimensional k Γ(X, ⊤)) :
    Function.Injective (Stacks.Picard.schemePullbackClassHom
      (Limits.pullback.fst f (Spec.map (CommRingCat.ofHom φ))))
```

## Tag 0CDP, an example

[Tag 0CDP](https://stacks.math.columbia.edu/tag/0CDP) in the Stacks Project.

**`Stacks.ProjectiveLine.subsingleton_picardGroup_basicOpen_map_of_residueFieldAlgHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean#L289). The attribute's comment: “clause (6): after enlarging `k` to a field `k'` admitting a `k`-embedding `κ(t) → k'`, the Picard group of the base change of `X = ℙ¹_k ∖ {t}` is trivial”.

> **The Picard group of `ℙ¹_k ∖ {t}` dies over a field embedding `κ(t)`.** Let `t = V₊(f)` be
> the closed point of `ℙ¹_k` cut out by a homogeneous irreducible form `f` not divisible by `T₁`,
> and let `X = ℙ¹_k ∖ {t}`. If a field `k'` admits a `k`-embedding of the residue field `κ(t)`,
> then `Pic(X_{k'}) = 0`.

```lean
theorem subsingleton_picardGroup_basicOpen_map_of_residueFieldAlgHom
    {k k' : Type u} [Field k] [Field k'] [Algebra k k'] {d : ℕ}
    {f : MvPolynomial (Fin 2) k} (hf : f.IsHomogeneous d) (hirr : Irreducible f)
    (hX : ¬ MvPolynomial.X (1 : Fin 2) ∣ f)
    [(Ideal.span {dehomogenize k f}).IsPrime]
    (ψ : (Ideal.span {dehomogenize k f}).ResidueField →ₐ[k] k') :
    Subsingleton (PicardGroup
      (Proj.basicOpen (grading k') (MvPolynomial.map (algebraMap k k') f)).toScheme.presheaf
      (Proj.basicOpen (grading k')
        (MvPolynomial.map (algebraMap k k') f)).toScheme.ringCatSheaf.2)
```

**`Stacks.ProjectiveLine.subsingleton_picardGroup_basicOpen_map_of_X_one_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean#L350). The attribute's comment: “clause (6) at the point at infinity `t = V₊(T₁)`, i.e. for `T₁ ∣ f`: the Picard group of the base change of `X = ℙ¹_k ∖ {t}` to an arbitrary field extension `k'` is trivial, with no hypothesis on `k'`”.

> **The Picard group of `ℙ¹_k ∖ {V₊(T₁)}` dies over every field extension.** If `T₁` divides
> `f`, then the Picard group of the base change of `D₊(f)` to any field extension `k'` of `k` is
> trivial.

```lean
theorem subsingleton_picardGroup_basicOpen_map_of_X_one_dvd
    {k k' : Type u} [Field k] [Field k'] [Algebra k k']
    {f : MvPolynomial (Fin 2) k} (hdvd : MvPolynomial.X (1 : Fin 2) ∣ f) :
    Subsingleton (PicardGroup
      (Proj.basicOpen (grading k') (MvPolynomial.map (algebraMap k k') f)).toScheme.presheaf
      (Proj.basicOpen (grading k')
        (MvPolynomial.map (algebraMap k k') f)).toScheme.ringCatSheaf.2)
```

**`Stacks.ProjectiveLine.subsingleton_picardGroup_basicOpen_map_of_residueFieldAlgHom_of_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardComplement.lean#L382). The attribute's comment: “clause (6) with the extra hypothesis `t ≠ V₊(T₁)` removed from the statement: for a closed point `t` of `ℙ¹_k` presented in the standard chart, a `k`-embedding `κ(t) → k'` makes the Picard group of the base change of `X = ℙ¹_k ∖ {t}` trivial”.

> **The Picard group of `ℙ¹_k ∖ {t}` dies over a field embedding `κ(t)`.** Let `t = V₊(f)` be
> the closed point of `ℙ¹_k` cut out by a homogeneous irreducible form `f`, with `κ(t)` the residue
> field of the prime ideal generated by the dehomogenization of `f`, and let `X = ℙ¹_k ∖ {t}`. If a
> field `k'` admits a `k`-embedding of `κ(t)`, then `Pic(X_{k'}) = 0`.

```lean
theorem subsingleton_picardGroup_basicOpen_map_of_residueFieldAlgHom_of_isPrime
    {k k' : Type u} [Field k] [Field k'] [Algebra k k'] {d : ℕ}
    {f : MvPolynomial (Fin 2) k} (hf : f.IsHomogeneous d) (hirr : Irreducible f)
    [(Ideal.span {dehomogenize k f}).IsPrime]
    (ψ : (Ideal.span {dehomogenize k f}).ResidueField →ₐ[k] k') :
    Subsingleton (PicardGroup
      (Proj.basicOpen (grading k') (MvPolynomial.map (algebraMap k k') f)).toScheme.presheaf
      (Proj.basicOpen (grading k')
        (MvPolynomial.map (algebraMap k k') f)).toScheme.ringCatSheaf.2)
```

**`Stacks.ProjectiveLine.surjective_complementRestrictHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean#L207). The attribute's comment: “the displayed surjection `ℤ = Pic(ℙ¹_k) → Pic(X)` for `X = ℙ¹_k ∖ {t}`, by Tag 0BD9 for the surjectivity and Tag 0BXJ for the identification of `Pic(ℙ¹_k)` with `ℤ`”.

> **The restriction map `ℤ = Pic(ℙ¹_k) → Pic(X)` is surjective**, for
> `X = ℙ¹_k ∖ V₊(f)`.

```lean
theorem surjective_complementRestrictHom : Function.Surjective (complementRestrictHom f)
```

**`Stacks.ProjectiveLine.surjective_complementZModHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean#L239). The attribute's comment: “the computation `Pic(X) = ℤ/dℤ` for `X = ℙ¹_k ∖ {t}`, surjectivity half: the displayed map factors through `ℤ/dℤ` by a surjection, `d = deg f = [κ(t) : k]`”.

> **The map `ℤ/dℤ → Pic(X)` is surjective**, for `X = ℙ¹_k ∖ V₊(f)` and `d = deg f`.

```lean
theorem surjective_complementZModHom {d : ℕ} (hf : f ∈ grading k d) :
    Function.Surjective (complementZModHom f hf)
```

**`Stacks.ProjectiveLine.nsmul_finrank_residueField_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean#L249). The attribute's comment: “`Pic(X)` is killed by `d = [κ(t) : k]` for `X = ℙ¹_k ∖ {t}`, the residue degree read in the standard chart”.

> **`Pic(X)` is killed by `d = [κ(t) : k]`**, the residue degree of the removed closed point
> `t = V₊(f)` of `ℙ¹_k`.

```lean
theorem nsmul_finrank_residueField_eq_zero {d : ℕ} {f : MvPolynomial (Fin 2) k}
    (hf : f.IsHomogeneous d) (hirr : Irreducible f)
    (hX : ¬ MvPolynomial.X (1 : Fin 2) ∣ f)
    [(Ideal.span {dehomogenize k f}).IsPrime]
    (c : (Proj.basicOpen (grading k) f).toScheme.picardGroup) :
    Module.finrank k (Ideal.span {dehomogenize k f}).ResidueField • c = 0
```

**`Stacks.ProjectiveLine.complementZModEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean#L332). The attribute's comment: “the computation `Pic(X) = ℤ/dℤ` for `X = ℙ¹_k ∖ {t}`, as the isomorphism `ℤ/dℤ ≃+ Pic(X)` induced by the displayed surjection, `d = deg f = [κ(t) : k]`”.

> **`Pic(X) = ℤ/dℤ`.** Let `t = V₊(f)` be the closed point of `ℙ¹_k` cut out by a homogeneous
> irreducible form `f` of degree `d`, and let `X = ℙ¹_k ∖ {t}`. The surjection
> `ℤ = Pic(ℙ¹_k) ↠ Pic(X)` has kernel `dℤ`, so it induces an isomorphism `ℤ/dℤ ≃ Pic(X)`.

```lean
def complementZModEquiv {d : ℕ} {f : MvPolynomial (Fin 2) k}
    (hf : f.IsHomogeneous d) (hirr : Irreducible f) :
    ZMod d ≃+ (Proj.basicOpen (grading k) f).toScheme.picardGroup
```

**`Stacks.ProjectiveLine.nontrivial_picardGroup_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveLine/PicardQuotient.lean#L343). The attribute's comment: “`Pic(X) ≠ 0` for `X = ℙ¹_k ∖ {t}` when `t` is not a `k`-rational point, i.e. when `d = [κ(t) : k] > 1`; this is what makes the example a counterexample to Tag 0CC5”.

> **`Pic(X) ≠ 0` for a non-rational point.** If the closed point `t = V₊(f)` of `ℙ¹_k` has
> degree `d > 1`, equivalently is not a `k`-rational point, then the Picard group of
> `X = ℙ¹_k ∖ {t}` is nonzero.

```lean
theorem nontrivial_picardGroup_basicOpen {d : ℕ} {f : MvPolynomial (Fin 2) k}
    (hf : f.IsHomogeneous d) (hirr : Irreducible f) (hd : 2 ≤ d) :
    Nontrivial (Proj.basicOpen (grading k) f).toScheme.picardGroup
```

## Tag 0BEH, a lemma

[Tag 0BEH](https://stacks.math.columbia.edu/tag/0BEH) in the Stacks Project.

**`Stacks.PicardGroup.nonempty_iso_pullback_sectionOfPoint_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/RationalEquivalenceNormalVariety.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardGroup/RationalEquivalenceNormalVariety.lean#L260). The attribute's comment: “k a field, X a normal variety over k, U an open of affine n-space over k with two k-rational points: an invertible module on X ×_{Spec k} U has isomorphic restrictions to X × p and X × q”.

> **Stacks Project, Tag 0BEH.** Let `k` be a field, `X` a normal variety over `k`, and
> `U ⊆ 𝔸^n_k` an open subscheme with `k`-rational points `p, q ∈ U(k)`. For every invertible module
> `ℒ` on `X ×_{Spec k} U` the restrictions `ℒ|_{X × p}` and `ℒ|_{X × q}` are isomorphic.
>
> Nothing is assumed beyond the source's hypotheses. The appeal to [Stacks, Tag 0BD7] at the
> projection `pr : X ×_{Spec k} U → X` is made through
> `Stacks.InvertiblePullback.exists_isInvertible_pullback_iso_of_isTrivial_genericFiber_of_flat`,
> whose hypotheses hold here: `pr` is the base change of `U → Spec k`, which is flat (an open
> immersion followed by the structure morphism of affine space) and, `n` being finite, locally of
> finite type; `X` is integral, normal and — being of finite type over a field — locally
> Noetherian, and so is `X ×_{Spec k} U`; and every fibre of `pr` is integral by
> `Stacks.PicardGroup.isIntegral_fiber_fst`. Its remaining hypothesis, triviality of `ℒ` on the
> generic fibre, is the one `Stacks.PicardGroup.nonempty_iso_pullback_sectionOfPoint` discharges
> from [Stacks, Tag 0BDA].

```lean
theorem nonempty_iso_pullback_sectionOfPoint_of_finite (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] [IsNormal X] {n : Type u} [Finite n]
    (U : (𝔸(n; Spec (.of k))).Opens) (p q : Spec (.of k) ⟶ U.toScheme)
    (hp : p ≫ openAffineSpaceOver k U = 𝟙 (Spec (.of k)))
    (hq : q ≫ openAffineSpaceOver k U = 𝟙 (Spec (.of k)))
    (L : (Limits.pullback f (openAffineSpaceOver k U)).Modules)
    [hL : IsInvertible (Limits.pullback f (openAffineSpaceOver k U)).presheaf
      (structureSheafRing
        (Limits.pullback f (openAffineSpaceOver k U)).toRingedSpace).property L] :
    Nonempty ((Scheme.Modules.pullback (sectionOfPoint f p hp)).obj L ≅
      (Scheme.Modules.pullback (sectionOfPoint f q hq)).obj L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.30, Tag 0BEG](https://stacks.math.columbia.edu/tag/0BEG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
