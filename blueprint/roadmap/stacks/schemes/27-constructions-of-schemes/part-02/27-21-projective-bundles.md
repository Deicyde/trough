---
declaration: section
origin: cited
lean: Stacks.RelativeProj.projectiveBundle, Stacks.RelativeProj.projectiveBundleToBase, Stacks.AlgebraicGeometry.ProjectiveSpaceOfModuleStatement.coordinates_bundle_points_sections, Stacks.ProjectiveBundle.Noninjective.isSymmetricAlgebra_toQuotientAlgebra, Stacks.ProjectiveBundle.Noninjective.counterexampleSection_mapsTo_zero, Stacks.ProjectiveBundle.Noninjective.iSup_basicOpen_symGen_eq_top, Stacks.ProjectiveBundle.Noninjective.basicOpen_symGen_sup_eq_top, Stacks.ProjectiveBundle.Noninjective.not_injective_toTwistSections
statement: formalized
proof: formalized
---

# 27.21 Projective bundles

Section 27.21 of the Stacks Project, [Tag 01OA](https://stacks.math.columbia.edu/tag/01OA). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01OB, a definition

[Tag 01OB](https://stacks.math.columbia.edu/tag/01OB) in the Stacks Project.

**`Stacks.RelativeProj.projectiveBundle`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBundle/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBundle/Basic.lean#L83). The attribute's comment: “the projective bundle and its projection”. References: EGA II (4.1.1), “P(E) itself”.

> **The projective bundle `𝐏(F) = Proj_X(Sym(F))` of a quasi-coherent sheaf of modules**, the
> relative projective spectrum of its symmetric algebra.

```lean
abbrev projectiveBundle (X : Scheme.{u}) (F : X.Modules) [F.IsQuasicoherent] : Scheme.{u}
```

**`Stacks.RelativeProj.projectiveBundleToBase`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBundle/Basic.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBundle/Basic.lean#L89). The attribute's comment: “the projective bundle and its projection”. References: EGA II (4.1.1), “projection to Y”.

> **The projection `π : 𝐏(F) ⟶ X` of a projective bundle**, the structure morphism of the
> relative projective spectrum of `Sym(F)` over its base.

```lean
abbrev projectiveBundleToBase (X : Scheme.{u}) (F : X.Modules) [F.IsQuasicoherent] :
    projectiveBundle X F ⟶ X
```

## Tag 0FCY, an example

[Tag 0FCY](https://stacks.math.columbia.edu/tag/0FCY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceOfModuleStatement.coordinates_bundle_points_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceOfModuleStatement.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjectiveSpaceOfModuleStatement.lean#L90). The attribute's comment: “the five assertions of the tag in one statement”.

> **[Stacks, Tag 0FCY].** Let `k` be a field and `V` a `k`-vector space, and let
> `𝐏(V) = Proj(Sym_k V)` be the projective space of `V`, with its structure morphism to `Spec k`.
> Then:
>
> * if `dim V = n + 1` then `𝐏(V)` is isomorphic to `ℙⁿ_k` as a scheme over `Spec k`;
> * `𝐏(V)` is the projective space bundle over `Spec k` of `V` read as a quasi-coherent module on
>   `Spec k`, by an isomorphism carrying the bundle projection to the structure morphism;
> * the `k`-valued points of `𝐏(V)`, that is the sections of its structure morphism, correspond
>   to the one-dimensional quotients of `V`, a point going to the space of vectors whose
>   degree-one forms vanish at it;
> * for every scheme `X` over `k`, every invertible `𝒪_X`-module `ℒ` and every `k`-linear map
>   `ψ : V → Γ(X, ℒ)` whose image generates `ℒ`, the morphism `φ_{ℒ,ψ} : X ⟶ 𝐏(V)` is a morphism
>   over `Spec k`, and there is an isomorphism `θ : φ_{ℒ,ψ}^*𝒪_{𝐏(V)}(1) ≅ ℒ` through which each
>   `v : V` is sent to `ψ v` by the universal degree-one section of `v`;
> * for every basis `v₀, …, vₙ` of `V`, the composite of `φ_{ℒ,ψ}` with the coordinate
>   isomorphism `𝐏(V) ≅ ℙⁿ_k` of that basis is the morphism `X ⟶ ℙⁿ_k` of [Stacks, Tag 01ND] for
>   the sections `ψ(v₀), …, ψ(vₙ)`.

```lean
theorem coordinates_bundle_points_sections :
    (∀ n : ℕ, Module.finrank k V = n + 1 →
        Nonempty ((projectiveSpaceOfModule k V).asOver (Spec (.of k)) ≅
          (projectiveSpaceOverRing n (.of k)).asOver (Spec (.of k)))) ∧
      (∃ e : projectiveSpaceOfModule k V ≅
          Stacks.RelativeProj.projectiveBundle (Spec (.of k)) (tildeOfModule k V),
        e.hom ≫ Stacks.RelativeProj.projectiveBundleToBase (Spec (.of k)) (tildeOfModule k V) =
          projectiveSpaceOfModuleToSpec k V) ∧
      (∃ E : {p : Spec (.of k) ⟶ projectiveSpaceOfModule k V //
            p ≫ projectiveSpaceOfModuleToSpec k V = 𝟙 (Spec (.of k))} ≃
          {K : Submodule k V // Module.finrank k (V ⧸ K) = 1},
        ∀ p v, v ∈ (E p).val ↔
          SymmetricAlgebra.ι k V v ∈ (p.val.base default).asHomogeneousIdeal) ∧
      ∀ {X : Scheme.{u}} [X.Over (Spec (.of k))] (L : X.Modules)
          [Stacks.Ample.IsInvertibleModule X L] (ψ : V →ₗ[k] Γ(L, ⊤))
          (hψ : ⨆ v : V, nonvanishingOpen X L (ψ v) = ⊤),
        morphismOfGeneratingSections k V L ψ hψ ≫ projectiveSpaceOfModuleToSpec k V =
            X ↘ Spec (.of k) ∧
          (∃ θ : pullbackTwistOne (grading k V) (morphismOfGeneratingSections k V L ψ hψ) ≅ L,
            ∀ v : V, θ.hom.app ⊤ (pullbackSectionOne (grading k V)
              (morphismOfGeneratingSections k V L ψ hψ) (degreeOneElement k V v)) = ψ v) ∧
          ∀ {n : ℕ} (b : Module.Basis (Fin (n + 1)) k V),
            morphismOfGeneratingSections k V L ψ hψ ≫
                (basisProjectiveSpaceOfModuleIso b).hom.left =
              Stacks.ProjectiveFromSections.toProjectiveSpaceOver (basisSections b ψ)
                (generatesStalks_basisSections b ψ hψ) (X ↘ Spec (.of k))
```

## Tag 01OC, an example

[Tag 01OC](https://stacks.math.columbia.edu/tag/01OC) in the Stacks Project.

**`Stacks.ProjectiveBundle.Noninjective.isSymmetricAlgebra_toQuotientAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean#L180). The attribute's comment: “the presentation of the symmetric algebra of the module”.

> **`Sym(M) = A[x, y] / (ū x + v̄ y)`.** This is the displayed identity of Stacks 01OC that
> makes the example concrete: `M` is `A x ⊕ A y` modulo the single relation `ū x + v̄ y`, so its
> symmetric algebra is the polynomial ring `A[x, y]` modulo the ideal generated by that same
> linear form, which `symmetricAlgebra_relationForm_eq` identifies.

```lean
public theorem isSymmetricAlgebra_toQuotientAlgebra :
    IsSymmetricAlgebra
      (SymmetricAlgebra.toQuotientAlgebra (coefficientRing R) (relationVector R))
```

**`Stacks.ProjectiveBundle.Noninjective.counterexampleSection_mapsTo_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean#L193). The attribute's comment: “the section maps to zero in the first twist”.

> **`m` maps to zero in `Γ(P, 𝒪_P(1))`.**

```lean
public theorem counterexampleSection_mapsTo_zero :
    SymmetricAlgebra.toTwistSections (coefficientRing R) (presentedModule R)
      (counterexampleSection R) = 0
```

**`Stacks.ProjectiveBundle.Noninjective.iSup_basicOpen_symGen_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean#L202). The attribute's comment: “the two-chart affine open covering of the projective bundle”.

> **`P = D₊(x) ∪ D₊(y)`**: the two standard opens of the degree-one generators cover the
> projective bundle. This is the affine open covering Stacks 01OC records.

```lean
public theorem iSup_basicOpen_symGen_eq_top :
    ⨆ i : Fin 2, Proj.basicOpen
      (SymmetricAlgebra.grading (coefficientRing R) (presentedModule R)) (symGen R i) = ⊤
```

**`Stacks.ProjectiveBundle.Noninjective.basicOpen_symGen_sup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean#L221). The attribute's comment: “the two-chart affine open covering of the projective bundle”.

> `P = D₊(x) ∪ D₊(y)`, written as a binary union.

```lean
public theorem basicOpen_symGen_sup_eq_top :
    Proj.basicOpen (SymmetricAlgebra.grading (coefficientRing R) (presentedModule R))
        (symGen R 0) ⊔
      Proj.basicOpen (SymmetricAlgebra.grading (coefficientRing R) (presentedModule R))
        (symGen R 1) = ⊤
```

**`Stacks.ProjectiveBundle.Noninjective.not_injective_toTwistSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Noninjective.lean#L245). The attribute's comment: “the map from the first symmetric power is not injective”.

> **The map `M = Sym¹(ℰ) → Γ(P, 𝒪_P(1))` is not injective.** This is the conclusion of
> Stacks 01OC: `m` is a nonzero global section of `ℰ` whose image in `Γ(P, 𝒪_P(1))` is zero, so
> the canonical map `Sym¹(ℰ) → π_* 𝒪_{𝐏(ℰ)}(1)` of Stacks 01OB is not injective, and in
> particular not an isomorphism.

```lean
public theorem not_injective_toTwistSections :
    ¬ Function.Injective
      (SymmetricAlgebra.toTwistSections (coefficientRing R) (presentedModule R))
```

**`Stacks.ProjectiveBundle.Noninjective.counterexampleSection_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean#L259). The attribute's comment: “the section is nonzero”.

> For a nontrivial ring `R`, the element `m = ū s̄₁ x + v̄ t̄₂ y` of `M` is nonzero.

```lean
public theorem counterexampleSection_ne_zero : counterexampleSection R ≠ 0
```

**`Stacks.ProjectiveBundle.Noninjective.X_zero_mul_counterexampleForm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean#L318). The attribute's comment: “the first displayed congruence”.

> In `A[x, y]`, `x (ū s̄₁ x + v̄ t̄₂ y) = (s̄₁ x + s̄₂ y)(ū x + v̄ y)`.

```lean
public theorem X_zero_mul_counterexampleForm :
    X 0 * counterexampleForm R =
      (C (coefficient R 2) * X 0 + C (coefficient R 3) * X 1) * relationForm R
```

**`Stacks.ProjectiveBundle.Noninjective.X_one_mul_counterexampleForm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/NoninjectiveAlgebra.lean#L327). The attribute's comment: “the second displayed congruence”.

> In `A[x, y]`, `y (ū s̄₁ x + v̄ t̄₂ y) = (t̄₁ x + t̄₂ y)(ū x + v̄ y)`.

```lean
public theorem X_one_mul_counterexampleForm :
    X 1 * counterexampleForm R =
      (C (coefficient R 4) * X 0 + C (coefficient R 5) * X 1) * relationForm R
```

## Tag 01OD, a lemma

[Tag 01OD](https://stacks.math.columbia.edu/tag/01OD) in the Stacks Project.

**`Stacks.SymGraded.isSeparated_projectiveBundleToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionClosedImmersion.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionClosedImmersion.lean#L81).

> **The structure morphism of the projective bundle of a quasi-coherent module on an arbitrary
> scheme is separated.**
>
> This is `Stacks.SymGraded.isSeparated_schemeProjectiveBundleToBase` with its quasi-coherence
> hypothesis discharged, and it is the single assertion of Tag 01OD.

```lean
public theorem isSeparated_projectiveBundleToBase :
    IsSeparated
      (schemeProjectiveBundle E (isQuasicoherentPieces_of_isQuasicoherent E)).toBase
```

## Tag 01OE, a lemma

[Tag 01OE](https://stacks.math.columbia.edu/tag/01OE) in the Stacks Project.

**`Stacks.SymGraded.projectiveBundleIsoProjectiveSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafSymmetricAlgebra/ProjectiveSpaceMorphism.lean, line 658](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafSymmetricAlgebra/ProjectiveSpaceMorphism.lean#L658).

> **`ℙⁿ_X` is a projective bundle over `X`**: the projective bundle of the free module sheaf
> `𝒪_X^{n+1}` — that is `Proj_X(Sym(𝒪_X^{n+1}))` — is projective `n`-space over `X`.
>
> This is the isomorphism; `Stacks.SymGraded.projectiveBundleIsoProjectiveSpace_hom_comp_fst` is
> the other half of the statement, that it is an isomorphism **over `X`**.

```lean
def projectiveBundleIsoProjectiveSpace :
    (freeProjectiveBundle (X := X) n).scheme ≅
      AlgebraicGeometry.projectiveSpaceOver.{u} n X
```

**`Stacks.SymGraded.projectiveBundleIsoProjectiveSpace_hom_comp_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafSymmetricAlgebra/ProjectiveSpaceMorphism.lean, line 669](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafSymmetricAlgebra/ProjectiveSpaceMorphism.lean#L669).

> **The isomorphism of Tag 01OE is an isomorphism over `X`**: it carries the structure morphism
> of `ℙⁿ_X` to the projection of the bundle. Together with
> `Stacks.SymGraded.projectiveBundleIsoProjectiveSpace` this is the whole assertion of the tag,
> which is that `ℙⁿ_X` is a projective bundle **over `X`** and not merely abstractly isomorphic to
> one.

```lean
theorem projectiveBundleIsoProjectiveSpace_hom_comp_fst :
    (projectiveBundleIsoProjectiveSpace (X := X) n).hom ≫
        pullback.fst (terminal.from X)
          (terminal.from (AlgebraicGeometry.projectiveSpaceAtUniverse.{u} n)) =
      (freeProjectiveBundle (X := X) n).toBase
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.21, Tag 01OA](https://stacks.math.columbia.edu/tag/01OA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
