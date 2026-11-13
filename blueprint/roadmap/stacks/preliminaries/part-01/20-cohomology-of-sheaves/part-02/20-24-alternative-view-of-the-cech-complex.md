---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.CoveringResolutionQuasiIso.exists_coveringResolution, LocallyFinite, Stacks.CechTotalComplex.CoveringResolution.isColimitCoveringTermCofan, Stacks.LocallyFiniteCover.isColimitCofanProduct, Stacks.LocallyFiniteCover.isIso_coproductToProduct, Stacks.LocallyFiniteCover.isIso_sectionsComparison
statement: formalized
proof: formalized
---

# 20.24 Alternative view of the Čech complex

Section 20.24 of the Stacks Project, [Tag 02FR](https://stacks.math.columbia.edu/tag/02FR). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02FU, a lemma

[Tag 02FU](https://stacks.math.columbia.edu/tag/02FU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoveringResolutionQuasiIso.exists_coveringResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoveringResolutionQuasiIso/Main.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CoveringResolutionQuasiIso/Main.lean#L153).

> **Stacks Project, Tag 02FU.** Every open covering of a ringed space gives a canonical
> augmented Čech resolution, functorial in the module sheaf: the complex, its augmentation,
> the product coordinates of its terms with Equation 01EE for the differential, the existence
> of homology, and the quasi-isomorphism.

```lean
theorem exists_coveringResolution (hU : ⨆ i, U i = ⊤) :
    Nonempty (Stacks.CechTotalComplex.CoveringResolution.{u, v, w, t} X R U)
```

## Tag 02FS, a definition

[Tag 02FS](https://stacks.math.columbia.edu/tag/02FS) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyFinite#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch20.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch20.lean#L41) (StacksFrontier): “more general: any family of subsets; Mathlib asks for a neighbourhood of x, equivalently an open one”. References: EGA IV (3.1.6), “more general”; EGA IV (21.10.1), “partial”.

## Tag 02FT, a remark

[Tag 02FT](https://stacks.math.columbia.edu/tag/02FT) in the Stacks Project.

**`Stacks.CechTotalComplex.CoveringResolution.isColimitCoveringTermCofan`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/CoveringResolutionLocallyFinite.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/CoveringResolutionLocallyFinite.lean#L114). The attribute's comment: “(third displayed formula: the terms of the complex of Tag 02FU are 𝔠ᵖ(𝒰, F) = ⨁ (j\_\{i₀…i\_p})\_* F\_\{i₀…i\_p})”.

> **Stacks Project, Tag 02FT, third displayed formula.** Let `(X, R)` be a ringed space, let
> `X = ⋃ i, U i` be a locally finite open covering and let `F` be a sheaf of `R`-modules. Then the
> degree-`p` term `𝔠ᵖ(𝒰, F) = ∏ (j_{i₀ … i_p})_* F_{i₀ … i_p}` of the covering resolution of
> Tag 02FU, together with the canonical injections `coveringTermInj`, is a coproduct of the
> factors: `𝔠ᵖ(𝒰, F) = ⨁ (j_{i₀ … i_p})_* F_{i₀ … i_p}`.
>
> The covering hypothesis is the source's; the proof uses only local finiteness.

```lean
def isColimitCoveringTermCofan (_hU : ⨆ i, U i = ⊤) (hlf : LocallyFinite fun i => (U i : Set X))
    (F : SheafOfModules.{w} R) (p : ℕ) :
    IsColimit (Cofan.mk (((coveringComplex.{u, v, w, t} X R U).obj F).X p)
      (coveringTermInj.{u, v, w, t} X R U F p))
```

**`Stacks.LocallyFiniteCover.isColimitCofanProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean#L393). The attribute's comment: “(second displayed formula: ⨁ (j\_i)\_* F\_i = ∏ (j\_i)\_* F\_i)”.

> **Stacks Project, Tag 02FT, second displayed formula.** Let `X = ⋃ i, U i` be a locally
> finite open covering of a topological space, let `j i : U i → X` be the inclusions and let
> `F i` be an abelian sheaf on `U i`. Then the product of the `(j i)_* (F i)`, equipped with
> the canonical injections `deltaInj`, is a coproduct of the `(j i)_* (F i)`: that is
> `⨁ i, (j i)_* (F i) = ∏ i, (j i)_* (F i)`.

```lean
noncomputable def isColimitCofanProduct (_hcov : IsOpenCover U)
    (hlf : LocallyFinite fun i => (U i : Set X)) : IsColimit (productCofan U F)
```

**`Stacks.LocallyFiniteCover.isIso_coproductToProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean#L431). The attribute's comment: “(second displayed formula, as an isomorphism from ∐ to ∏)”.

> **Stacks Project, Tag 02FT, second displayed formula.** For a locally finite open
> covering the canonical map from the direct sum of the `(j i)_* (F i)` to their direct product
> is an isomorphism.

```lean
theorem isIso_coproductToProduct (hcov : IsOpenCover U)
    (hlf : LocallyFinite fun i => (U i : Set X)) : IsIso (coproductToProduct U F)
```

**`Stacks.LocallyFiniteCover.isIso_sectionsComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/LocallyFiniteCoproductSections.lean#L456). The attribute's comment: “(first displayed formula: Γ(V, 𝒢) = ∏ F\_i(V ∩ U\_i))”.

> **Stacks Project, Tag 02FT, first displayed formula.** With `X = ⋃ i, U i` a locally
> finite open covering and `𝒢 = ⨁ i, (j i)_* (F i)`, for every open `V` of `X` the canonical
> comparison from `Γ (V, 𝒢)` to `∏ i, (F i) (V ∩ U i)` is an isomorphism: the sections of the
> direct sum over `V` are the *product* of the groups `(F i) (V ∩ U i)`.
>
> The comparison is the sections over `V` of the canonical map from the direct sum to the
> product, followed by the canonical comparison from the sections of a product of sheaves to
> the product of their sections. The `i`-th factor of the target is
> `(sectionsFunctor V).obj (pushforwardOpen U F i)`, which is `(F i) (V ∩ U i)` by
> `Stacks.LocallyFiniteCover.sectionsFunctor_obj_pushforwardOpen`.

```lean
theorem isIso_sectionsComparison (hcov : IsOpenCover U)
    (hlf : LocallyFinite fun i => (U i : Set X)) (V : Opens X) :
    IsIso ((sectionsFunctor V).map (coproductToProduct U F) ≫
      piComparison (sectionsFunctor V) (fun i => pushforwardOpen U F i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.24, Tag 02FR](https://stacks.math.columbia.edu/tag/02FR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
