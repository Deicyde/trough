---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.SmoothProjectiveScheme.ChowMotive.chowGroup, Stacks.WeilCohomology.SmoothProjectiveScheme.ChowMotive.mem_chowGroup_iff, Stacks.WeilCohomology.ChowMotiveCat.chowGroupEquivHom, Stacks.WeilCohomology.ChowMotiveCat.chowGroupEquivHom_naturality, Stacks.WeilCohomology.ChowMotiveCat.chowFunctorIso, Stacks.WeilCohomology.MotiveCalculus.chowGroupEquivHom, Stacks.WeilCohomology.MotiveCalculus.chowGroupEquivHom_naturality, Stacks.WeilCohomology.MotiveCalculus.chowFunctorIso
statement: formalized
proof: formalized
---

# 45.5 Chow groups of motives

Section 45.5 of the Stacks Project, [Tag 0FGK](https://stacks.math.columbia.edu/tag/0FGK). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FGL, a definition

[Tag 0FGL](https://stacks.math.columbia.edu/tag/0FGL) in the Stacks Project.

**`Stacks.WeilCohomology.SmoothProjectiveScheme.ChowMotive.chowGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ChowGroupsOfMotives.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ChowGroupsOfMotives.lean#L256). The attribute's comment: “the i-th Chow group CH^i(M) = p(CH^\{i+m}(X) ⊗ Q) of a Chow motive M = (X, p, m) over a field, X smooth projective and p\_* the pushforward action of the projector”.

> **Stacks Project, Tag 0FGL.** The `i`-th Chow group of a Chow motive `M = (X, p, m)` over a
> field `k`,
>
>   `CH^i(M) = p(CH^{i + m}(X) ⊗ ℚ)`,
>
> the image of the pushforward action `p_*` of the projector `p ∈ Corr⁰(X, X)` (Section 0FFZ) on
> the rational Chow group of codimension `i + m` classes of the smooth projective scheme `X`, as a
> `ℚ`-subspace of `CH^{i + m}(X) ⊗ ℚ`.
>
> This is the complete, unconditional registration of Stacks 0FGL: the composition and the
> pushforward of correspondences are the ones constructed in this file. It supersedes
> `Stacks.WeilCohomology.ChowMotive.chowGroup`, which takes them as a carried
> `Stacks.WeilCohomology.CorrespondenceCalculus` and no longer carries the tag.

```lean
def chowGroup (i : ℤ) : Submodule ℚ (RationalCodimChowGroup M.X (i + M.twist))
```

**`Stacks.WeilCohomology.SmoothProjectiveScheme.ChowMotive.mem_chowGroup_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ChowGroupsOfMotives.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ChowGroupsOfMotives.lean#L262). The attribute's comment: “membership in CH^i(M) = p(CH^\{i+m}(X) ⊗ Q)”.

> **Stacks Project, Tag 0FGL.** The classes of `CH^i(M)` are the classes `p_*(β)` for
> `β ∈ CH^{i + m}(X) ⊗ ℚ`.

```lean
theorem mem_chowGroup_iff (i : ℤ) (α : RationalCodimChowGroup M.X (i + M.twist)) :
    α ∈ M.chowGroup i ↔ ∃ β, M.projectorAction i β = α
```

## Tag 0FGM, a lemma

[Tag 0FGM](https://stacks.math.columbia.edu/tag/0FGM) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.chowGroupEquivHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean#L459). The attribute's comment: “CH^i(M) = Hom\_\{M\_k}(1(-i), M)”.

> The functor `CH^i(-)` on the category `M_k` of Chow motives is representable by `𝟏(-i)`: for
> every motive `M` there is a `ℚ`-linear isomorphism
>
>   `CH^i(M) = Hom_{M_k}(𝟏(-i), M)`,
>
> sending `α ∈ CH^i(X, p, m) = p(CH^{i+m}(X) ⊗ ℚ)` to the correspondence
> `α ∈ Corr^{i+m}(Spec k, X)` of Stacks 0FG0 (3). It is natural in `M`:
> `Stacks.WeilCohomology.ChowMotiveCat.chowGroupEquivHom_naturality`.

```lean
def chowGroupEquivHom (M : ChowMotiveCat k) (i : ℤ) : chowGroup M i ≃ₗ[ℚ] (tate k (-i) ⟶ M)
```

**`Stacks.WeilCohomology.ChowMotiveCat.chowGroupEquivHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean#L473). The attribute's comment: “CH^i(M) = Hom\_\{M\_k}(1(-i), M) functorially in M”.

> The identification `CH^i(M) = Hom_{M_k}(𝟏(-i), M)` is natural in `M`: for a morphism of
> motives `c : M ⟶ N` it carries `c_* : CH^i(M) ⟶ CH^i(N)` to postcomposition with `c`.

```lean
theorem chowGroupEquivHom_naturality {M N : ChowMotiveCat k} (f : M ⟶ N) (i : ℤ)
    (α : chowGroup M i) :
    chowGroupEquivHom N i (chowMap f i α) = chowGroupEquivHom M i α ≫ f
```

**`Stacks.WeilCohomology.ChowMotiveCat.chowFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ChowGroupsOfMotives.lean#L482). The attribute's comment: “the functor CH^i(-) on M\_k is representable by 1(-i)”.

> The functor `CH^i(-) : M_k ⥤ ℚ-vector spaces` is representable by `𝟏(-i)`: it is isomorphic
> to the functor `Hom_{M_k}(𝟏(-i), -)`, functorially in the motive.

```lean
def chowFunctorIso (i : ℤ) :
    chowFunctor k i ≅ (linearCoyoneda ℚ (ChowMotiveCat k)).obj (Opposite.op (tate k (-i)))
```

**`Stacks.WeilCohomology.MotiveCalculus.chowGroupEquivHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean#L633). The attribute's comment: “CH^i(M) = Hom(1(-i), M)”.

> The functor `CH^i(-)` on the category of Chow motives is represented by the `(-i)`-twist of
> the unit motive: the identification
> `CH^{i+m}(X) ⊗ ℚ = Corr^{i+m}(Spec k, X)` of Stacks 0FG0 (3) restricts to an isomorphism of
> `ℚ`-vector spaces
>
>   `CH^i(M) ≃ Hom_{M_k}(𝟙(-i), M)`.
>
> Naturality in `M` is `Stacks.WeilCohomology.MotiveCalculus.chowGroupEquivHom_naturality`, and
> the two together are packaged as
> `Stacks.WeilCohomology.MotiveCalculus.chowFunctorIso`.

```lean
def chowGroupEquivHom (M : D.Obj) (i : ℤ) : ↥(M.as.chowGroup i) ≃ₗ[ℚ] (D.unitTwist i ⟶ M)
```

**`Stacks.WeilCohomology.MotiveCalculus.chowGroupEquivHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean#L672). The attribute's comment: “the identification is functorial in the motive”.

> The isomorphism `CH^i(M) ≃ Hom(𝟙(-i), M)` is natural in `M`: it carries the map on Chow
> groups induced by a morphism of motives `f : M → N` — the restriction of the action of the
> correspondence underlying `f` — to postcomposition with `f`.

```lean
theorem chowGroupEquivHom_naturality {M N : D.Obj} (i : ℤ) (f : M ⟶ N)
    (α : ↥(M.as.chowGroup i)) :
    D.chowGroupEquivHom N i (D.chowGroupMap i f α) = D.chowGroupEquivHom M i α ≫ f
```

**`Stacks.WeilCohomology.MotiveCalculus.chowFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean, line 718](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean#L718). The attribute's comment: “CH^i(-) is representable by 1(-i), as functors”.

> The functor `CH^i(-)` on the category of Chow motives is representable by `𝟙(-i)`: an
> isomorphism of functors `CH^i(-) ≅ Hom_{M_k}(𝟙(-i), -)` with values in `ℚ`-vector spaces.

```lean
def chowFunctorIso (i : ℤ) : D.chowFunctor i ≅ D.homFunctor i
```

## Tag 0FGN, a lemma

[Tag 0FGN](https://stacks.math.columbia.edu/tag/0FGN) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.isIso_of_bijective_chowMap_tensorHom_h`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ManinIdentityPrinciple.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ManinIdentityPrinciple.lean#L89). The attribute's comment: “Manin's identity principle, on the category M\_k of Chow motives”.

> **Stacks Project, Tag 0FGN** (Manin's identity principle). Let `k` be a field and let
> `c : M ⟶ N` be a morphism of Chow motives over `k`. If for every smooth projective scheme `X` over
> `k` the morphism `c ⊗ 1 : M ⊗ h(X) ⟶ N ⊗ h(X)` induces an isomorphism
> `CH^i(M ⊗ h(X)) → CH^i(N ⊗ h(X))` on Chow groups in every degree `i`, then `c` is an
> isomorphism.

```lean
theorem isIso_of_bijective_chowMap_tensorHom_h {M N : ChowMotiveCat k} (c : M ⟶ N)
    (hc : ∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i : ℤ),
      Function.Bijective (chowMap (c ⊗ₘ 𝟙 ((h k).obj (op X))) i)) :
    IsIso c
```

**`Stacks.WeilCohomology.isIso_of_bijective_chowMap_tensorUnitHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ManinIdentityPrinciple.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ManinIdentityPrinciple.lean#L196). The attribute's comment: “Manin's identity principle: c is an isomorphism if c tensor 1 is an isomorphism on the Chow groups of M tensor h(X) for every smooth projective X, over every degree i. STATED IN AN ABSTRACT MONOIDAL CATEGORY, not on this library's category of motives, because the monoidal structure on Karoubi S.Obj is Stacks 0FGC, which is only stated, not constructed, in this library -- so `M ⊗ h(X)` cannot be written on `S.Motive` at all. The statement specialises to the source's setting as soon as 0FGC is available, and `h : D → Mot` is kept untwisted on purpose so that quantifying the hypothesis over D does not silently assume it for the twists h(X)(m), which is what the source's proof has to earn. Four pieces of data are carried rather than used, each named in the signature: the representability CH^i(-) = Hom(1(-i), -) of Stacks 0FGM (the field chowEquiv of ChowRepresentability, together with its naturality), invertibility of the Tate motive in the Stacks 0FFP sense (tateExactPairing), Stacks 0FGJ that every object has a left dual (hdual), and generation, that every motive is a retract of a twist h(X)(m) (hgen), taken in the weak Retract sense so the theorem is stronger. Proved here rather than carried: Stacks 0FFQ, the summand step, the degree shift and the Yoneda step”.

> **Manin's identity principle.** Let `c : M ⟶ N` be a morphism of motives. If for every
> smooth projective scheme `X` over `k` the morphism `c ⊗ 1 : M ⊗ h(X) ⟶ N ⊗ h(X)` induces an
> isomorphism on the Chow group `CH^i` in every degree `i ∈ ℤ`, then `c` is an isomorphism.
>
> Here `Mot` stands for the monoidal category `M_k` of motives, `h X` is the motive of a smooth
> projective scheme `X` over `k`, and `R` carries the Chow groups together with the
> representability `CH^i(-) = Hom(1(-i), -)`. The theorem takes as hypotheses `hdual`, that every
> object of `M_k` has a left dual, and `hgen`, that every object of `M_k` is a direct summand of a
> twist `h(X)(m)`.

```lean
theorem isIso_of_bijective_chowMap_tensorUnitHom (R : ChowRepresentability Mot)
    (hdual : ∀ L : Mot, HasRightDual L) {D : Type w} (h : D → Mot)
    (hgen : ∀ L : Mot, ∃ (X : D) (m : ℤ), Nonempty (Retract L (h X ⊗ R.unitTwist m)))
    {M N : Mot} (c : M ⟶ N)
    (hc : ∀ (X : D) (i : ℤ), Function.Bijective (R.chowMap i (c ⊗ₘ 𝟙 (h X)))) :
    IsIso c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.5, Tag 0FGK](https://stacks.math.columbia.edu/tag/0FGK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
