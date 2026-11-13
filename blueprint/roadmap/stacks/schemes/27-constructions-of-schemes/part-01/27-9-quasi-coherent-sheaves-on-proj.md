---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjStalkGlobalSections.degreeZeroToGlobalSections, Stacks.AlgebraicGeometry.ProjShiftedSections.degreeNToGlobalSections, Stacks.GradedModule.shiftedGrading_zero, Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap, Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap_standardOpen, Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap_stalk, Stacks.AlgebraicGeometry.ProjStalkGlobalSections.associatedModuleSheafTensorMap_globalSections, Stacks.ProjTensorComparison.tensorComparison_not_isomorphism
statement: formalized
proof: formalized
---

# 27.9 Quasi-coherent sheaves on Proj

Section 27.9 of the Stacks Project, [Tag 01MJ](https://stacks.math.columbia.edu/tag/01MJ). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AG1, an equation

[Tag 0AG1](https://stacks.math.columbia.edu/tag/0AG1) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.ProjStalkGlobalSections.degreeZeroToGlobalSections`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjStalkGlobalSections/GlobalSections.lean#L184), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistGlobalSections.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistGlobalSections.lean#L134) (StacksFrontier).

## Tag 0AG2, an equation

[Tag 0AG2](https://stacks.math.columbia.edu/tag/0AG2) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjShiftedSections.degreeNToGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjShiftedSectionModule.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjShiftedSectionModule.lean#L309). The attribute's comment: “map\_degree\_n\_global\_sections”. References: EGA II (3.3.2), “partial, special case”.

> The canonical map from the degree-`n` homogeneous elements of `M` to the global sections of
> `M(n)~`, as an additive homomorphism: it is the degree-zero global-sections map of the shift.
> This is the map `Mₙ → Γ(Proj(S), M(n)~)` of Tag 0AG2, obtained from the degree-zero map of Tag
> 0AG1 for the grading of `M(n)` and the identification `M(n)₀ = Mₙ` of
> `Stacks.GradedModule.shiftedGrading_zero`.

```lean
public noncomputable def degreeNToGlobalSections (n : ℤ) :
    𝒨 n →+ shiftedSectionsComponent 𝒮 𝒨 n
```

**`Stacks.GradedModule.shiftedGrading_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistGlobalSections.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistGlobalSections.lean#L78). The attribute's comment: “twist\_degree\_zero”.

> The degree-zero piece of the twist `M(n)` is the degree-`n` piece of `M`: `M(n)₀ = Mₙ`.
> The two indices are `0 + n` and `n`, which are equal by `zero_add` and not by reduction.

```lean
public theorem shiftedGrading_zero {M : Type v} {τ : Type t} [SetLike τ M] (𝒩 : ℤ → τ) (n : ℤ) :
    shiftedGrading 𝒩 n 0 = 𝒩 n
```

## Tag 01MK, a lemma

[Tag 01MK](https://stacks.math.columbia.edu/tag/01MK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean#L659). The attribute's comment: “canonical sheaf morphism”. References: EGA II (2.5.11), “(2.5.11.2)”; EGA II (3.2.6), “λ (3.2.6.1)”.

> The canonical morphism from the tensor product of the associated sheaves of `M` and `N`
> to the associated sheaf of the graded tensor product `M ⊗[S] N`.

```lean
def associatedModuleSheafTensorMap :
    letI := tensorGrading_decomposition (S := S) 𝒮 𝒨 𝒩
    letI := tensorGrading_gradedSMul (S := S) 𝒮 𝒨 𝒩
    (((Stacks.SheafOfModules.Tensor.sheafTensor ((_root_.AlgebraicGeometry.Proj
      𝒮).toRingedSpace).sheaf).obj ((ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨))).obj
      ((ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒩))) ⟶
      ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 (tensorGrading (S := S) 𝒨 𝒩)
```

**`Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap_standardOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean, line 729](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean#L729). The attribute's comment: “formula on standard opens”. References: EGA II (2.5.11), “λ\_f on D\_+(f)”.

> On a positive-degree standard open, the canonical morphism sends the tensor of two
> homogeneous fractions to the fraction of their tensor over the product of the denominators.

```lean
theorem associatedModuleSheafTensorMap_standardOpen
    {f : S} {d : ℕ} (hf : f ∈ 𝒮 d) (hd : 0 < d)
    (p q : ℕ) (m : M) (hm : m ∈ 𝒨 (p • (d : ℤ)))
    (n : N) (hn : n ∈ 𝒩 (q • (d : ℤ))) :
    letI := tensorGrading_decomposition (S := S) 𝒮 𝒨 𝒩
    letI := tensorGrading_gradedSMul (S := S) 𝒮 𝒨 𝒩
    let U := ProjectiveSpectrum.basicOpen 𝒮 f
    let F := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨
    let G := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒩
    ((associatedModuleSheafTensorMap 𝒮 𝒨 𝒩).val.app (op U))
      (Stacks.SheafOfModules.TensorStalkRingedSpace.toTensorSheafSection
        (_root_.AlgebraicGeometry.Proj 𝒮).toRingedSpace F G (op U)
        (((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒨 hf hd).symm
          (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 𝒨 hf p m hm)) ⊗ₜ[_]
         ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒩 hf hd).symm
          (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 𝒩 hf q n hn)))) =
      (ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮
        (tensorGrading (S := S) 𝒨 𝒩) hf hd).symm
        (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 (tensorGrading (S := S) 𝒨 𝒩)
          hf (p + q) (m ⊗ₜ[S] n)
          (by
            apply AddSubgroup.subset_closure
            refine ⟨p • (d : ℤ), q • (d : ℤ), ?_, m, hm, n, hn, rfl⟩
            simp [add_mul]))
```

**`Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean, line 792](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSheafFunctoriality/Tensor.lean#L792). The attribute's comment: “formula on stalks”.

> On the stalk at a homogeneous prime of a positive-degree standard open, the canonical
> morphism carries the tensor of the germs of two homogeneous fractions to the germ of the
> fraction of their tensor.

```lean
theorem associatedModuleSheafTensorMap_stalk
    {f : S} {d : ℕ} (hf : f ∈ 𝒮 d) (hd : 0 < d)
    (x : ProjectiveSpectrum.top 𝒮)
    (hx : x ∈ ProjectiveSpectrum.basicOpen 𝒮 f)
    (p q : ℕ) (m : M) (hm : m ∈ 𝒨 (p • (d : ℤ)))
    (n : N) (hn : n ∈ 𝒩 (q • (d : ℤ))) :
    letI := tensorGrading_decomposition (S := S) 𝒮 𝒨 𝒩
    letI := tensorGrading_gradedSMul (S := S) 𝒮 𝒨 𝒩
    let X := (_root_.AlgebraicGeometry.Proj 𝒮).toRingedSpace
    let U := ProjectiveSpectrum.basicOpen 𝒮 f
    let F := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨
    let G := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒩
    let T := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 (tensorGrading (S := S) 𝒨 𝒩)
    letI := Stacks.SheafOfModules.TensorStalkRingedSpace.stalkModule X F.val x
    letI := Stacks.SheafOfModules.TensorStalkRingedSpace.stalkModule X G.val x
    letI := Stacks.SheafOfModules.TensorStalkRingedSpace.stalkModule X
      ((((Stacks.SheafOfModules.Tensor.sheafTensor (X).sheaf).obj (F)).obj (G))).val x
    letI := Stacks.SheafOfModules.TensorStalkRingedSpace.stalkModule X T.val x
    Stacks.SheafOfModules.TensorStalkRingedSpace.stalkMapL X
      ((((Stacks.SheafOfModules.Tensor.sheafTensor (X).sheaf).obj (F)).obj (G))).val T.val
      (associatedModuleSheafTensorMap 𝒮 𝒨 𝒩).val x
      ((Stacks.SheafOfModules.TensorStalkRingedSpace.tensorStalkIso X x F G).symm
        ((Stacks.SheafOfModules.TensorStalkRingedSpace.grpGerm X F.val x U hx
            ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒨 hf hd).symm
              (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 𝒨 hf p m hm)))
          ⊗ₜ[Stacks.SheafOfModules.TensorStalkRingedSpace.ringStalk X x]
         (Stacks.SheafOfModules.TensorStalkRingedSpace.grpGerm X G.val x U hx
            ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮 𝒩 hf hd).symm
              (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 𝒩 hf q n hn))))) =
      Stacks.SheafOfModules.TensorStalkRingedSpace.grpGerm X T.val x U hx
        ((ProjectiveSpectrum.Proj.associatedModuleSheafStandardOpenEquiv 𝒮
          (tensorGrading (S := S) 𝒨 𝒩) hf hd).symm
          (ProjectiveSpectrum.Proj.degreeZeroFraction 𝒮 (tensorGrading (S := S) 𝒨 𝒩)
            hf (p + q) (m ⊗ₜ[S] n)
            (by
              apply AddSubgroup.subset_closure
              refine ⟨p • (d : ℤ), q • (d : ℤ), ?_, m, hm, n, hn, rfl⟩
              simp [add_mul])))
```

**`Stacks.AlgebraicGeometry.ProjStalkGlobalSections.associatedModuleSheafTensorMap_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjStalkGlobalSections/Tensor.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjStalkGlobalSections/Tensor.lean#L67). The attribute's comment: “global-sections compatibility”.

> The canonical morphism commutes with the maps from degree-zero elements into global
> sections, evaluated on a pure tensor.

```lean
theorem associatedModuleSheafTensorMap_globalSections (m : 𝒨 0) (n : 𝒩 0) :
    letI := ProjSheafFunctoriality.tensorGrading_decomposition (S := S) 𝒮 𝒨 𝒩
    letI := ProjSheafFunctoriality.tensorGrading_gradedSMul (S := S) 𝒮 𝒨 𝒩
    let F := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒨
    let G := ProjectiveSpectrum.Proj.associatedModuleSheaf 𝒮 𝒩
    ((ProjSheafFunctoriality.associatedModuleSheafTensorMap 𝒮 𝒨 𝒩).val.app (op ⊤))
      (Stacks.SheafOfModules.TensorStalkRingedSpace.toTensorSheafSection
        (_root_.AlgebraicGeometry.Proj 𝒮).toRingedSpace F G (op ⊤)
        ((degreeZeroToGlobalSections 𝒮 𝒨 m) ⊗ₜ[_]
         (degreeZeroToGlobalSections 𝒮 𝒩 n))) =
      degreeZeroToGlobalSections 𝒮 (tensorGrading (S := S) 𝒨 𝒩)
        ⟨m.1 ⊗ₜ[S] n.1,
          (by
            apply AddSubgroup.subset_closure
            exact ⟨0, 0, by simp, m.1, m.2, n.1, n.2, rfl⟩)⟩
```

## Tag 01ML, a remark

[Tag 01ML](https://stacks.math.columbia.edu/tag/01ML) in the Stacks Project.

**`Stacks.ProjTensorComparison.tensorComparison_not_isomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTensorComparisonStatement.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTensorComparisonStatement.lean#L146). The attribute's comment: “Remark 27.10.3 as one theorem: the canonical comparison morphism M-tilde ⊗ N-tilde ⟶ (M ⊗\_S N)-tilde of sheaves of modules on Proj(S) is not an isomorphism, and for k[x, y, z] with weights 1, 2, 3, M = S(1) and N = S(2) the remark's computation — S\_z is S with 1/z adjoined, M ⊗\_S N = S(3) degreewise, S₍z₎ ≅ k[u, v, w]/(uw - v³) by the map sending the variables to u, v, w, M₍z₎ = S₍z₎x + S₍z₎y²/z, N₍z₎ = S₍z₎y + S₍z₎x², S(3)₍z₎ = S₍z₎z, the ideal (u, v, w) is maximal with residue field k, the fibres of M₍z₎ and N₍z₎ there have dimension 2 and that of S(3)₍z₎ dimension 1, and the multiplication map M₍z₎ ⊗ N₍z₎ → S(3)₍z₎ is not bijective. The first conjunct is witnessed by k[X] with deg X = 2 and M = N = S(1)”.

> **Stacks Project, Tag 01ML.** The canonical comparison morphism
> `M̃ ⊗_𝒪 Ñ ⟶ (M ⊗_S N)~` of sheaves of modules on `Proj(S)` is not an isomorphism, and the
> remark's example computes why. For a field `k` and `S = k[x, y, z]` with weights `1, 2, 3`,
> `M = S(1)`, `N = S(2)`:
>
> 1. the comparison morphism of sheaves of modules is not an isomorphism;
> 2. `S_z` is `S` with `1/z` adjoined;
> 3. `M ⊗_S N = S(3)`, degreewise;
> 4. `S₍z₎ ≅ k[u, v, w]/(uw - v³)`, by the map carrying the three variables to `u`, `v`, `w`;
> 5. `M₍z₎ = S₍z₎ · x + S₍z₎ · y²/z`;
> 6. `N₍z₎ = S₍z₎ · y + S₍z₎ · x²`;
> 7. `S(3)₍z₎ = S₍z₎ · z`;
> 8. `𝔪 = (u, v, w)` is a maximal ideal of `S₍z₎`;
> 9. its residue field is `k`;
> 10. the fibres of `M₍z₎` and of `N₍z₎` at `𝔪` have dimension `2`, and that of `S(3)₍z₎`
>     dimension `1`;
> 11. the multiplication map `M₍z₎ ⊗_{S₍z₎} N₍z₎ → S(3)₍z₎` is not bijective.
>
> Conjunct (1) is the failure of generality asserted by Stacks Tag 01ML of the morphism
> constructed in Stacks Tag 01MK, and it is witnessed by `k[X]` with `deg X = 2` and
> `M = N = S(1)` rather than by the remark's own weights; see the module docstring for what a
> derivation from the remark's own witness would still need. Conjunct (4) is stated as the
> existence of an algebra isomorphism together with its values on the three variables, which pins
> it down to the map the remark writes.

```lean
theorem tensorComparison_not_isomorphism :
    letI : (situation k).vertexIdeal.IsMaximal :=
      WeightedPolynomialSituation.vertexIdeal_isMaximal (situation k)
    (¬ IsIso (Stacks.AlgebraicGeometry.ProjSheafFunctoriality.associatedModuleSheafTensorMap
        (Stacks.EvenWeightProj.grading k) (Stacks.EvenWeightProj.oddTwist k)
        (Stacks.EvenWeightProj.oddTwist k))) ∧
      Algebra.adjoin (situation k).S
          ({(IsLocalization.Away.invSelf (situation k).z :
              (situation k).ordinaryLocalization)} :
            Set (situation k).ordinaryLocalization) = ⊤ ∧
      (∀ n : ℤ,
        Submodule.map
            ((TensorProduct.lid (situation k).S (situation k).S).toLinearMap.restrictScalars
              (situation k).k)
            (Submodule.span (situation k).k
              {t : TensorProduct (situation k).S (situation k).S (situation k).S |
                ∃ i j : ℤ, i + j = n ∧
                  ∃ a b : (situation k).S, a ∈ (situation k).grading (i + 1) ∧
                    b ∈ (situation k).grading (j + 2) ∧
                      t = TensorProduct.tmul (situation k).S a b}) =
          (situation k).grading (n + 3)) ∧
      (∃ e :
          (MvPolynomial (Fin 3) (situation k).k ⧸ cubicRelationIdeal (situation k).k)
            ≃ₐ[(situation k).k] (situation k).R,
        ∀ i : Fin 3,
          e (Ideal.Quotient.mk (cubicRelationIdeal (situation k).k) (MvPolynomial.X i)) =
            ![(situation k).u, (situation k).v, (situation k).w] i) ∧
      (situation k).firstTwistLocalization =
        Submodule.span (situation k).R
          {Localization.mk (situation k).x (1 : Submonoid.powers (situation k).z),
            Localization.mk ((situation k).y ^ 2)
              ⟨(situation k).z, Submonoid.mem_powers (situation k).z⟩} ∧
      (situation k).secondTwistLocalization =
        Submodule.span (situation k).R
          ({algebraMap (situation k).S (situation k).ordinaryLocalization (situation k).y,
            algebraMap (situation k).S (situation k).ordinaryLocalization
              ((situation k).x ^ 2)} : Set (situation k).ordinaryLocalization) ∧
      (situation k).localizedTwist 3 =
        Submodule.span (situation k).R
          {algebraMap (situation k).S (Localization.Away (situation k).z) (situation k).z} ∧
      (situation k).vertexIdeal.IsMaximal ∧
      Function.Bijective (algebraMap (situation k).k (situation k).vertexIdeal.ResidueField) ∧
      Module.finrank (situation k).vertexIdeal.ResidueField
        ((situation k).vertexIdeal.ResidueField ⊗[(situation k).R]
          (situation k).firstTwistLocalization) = 2 ∧
      Module.finrank ((situation k).R ⧸ (situation k).vertexIdeal)
        ((situation k).secondTwistLocalization ⧸
          (situation k).vertexIdeal •
            (⊤ : Submodule (situation k).R (situation k).secondTwistLocalization)) = 2 ∧
      Module.finrank ((situation k).R ⧸ (situation k).vertexIdeal)
        ((situation k).localizedTwist 3 ⧸
          (situation k).vertexIdeal •
            (⊤ : Submodule (situation k).R ((situation k).localizedTwist 3))) = 1 ∧
      ¬ Function.Bijective
          (WeightedPolynomialSituation.localizedTwistTensorMap (situation k))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.9, Tag 01MJ](https://stacks.math.columbia.edu/tag/01MJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
