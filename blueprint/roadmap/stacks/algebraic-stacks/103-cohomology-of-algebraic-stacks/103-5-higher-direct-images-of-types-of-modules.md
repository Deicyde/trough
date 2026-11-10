---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion, AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion_unconditional, AlgebraicGeometry.Stack.AlgebraicStacks.higherDirectImage_mem_of_quasiCompact_quasiSeparated, AlgebraicGeometry.Stack.StackModuleRule.preservesHigherDirectImages_fppf
statement: formalized
proof: formalized
---

# 103.5 Higher direct images of types of modules

Section 103.5 of the Stacks Project, [Tag 076Y](https://stacks.math.columbia.edu/tag/076Y). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 076Z, a lemma

[Tag 076Z](https://stacks.math.columbia.edu/tag/076Z) in the Stacks Project.

**`AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageRuleSpectralSequence.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageRuleSpectralSequence.lean#L114). The attribute's comment: “the whole statement: every rule satisfying the source's four hypotheses, every quasi-compact quasi-separated 1-morphism of algebraic stacks and every degree; hypothesis (3) is read for the families indexed in a universe containing u, which the source's hypothesis implies, so the statement is no weaker than the source's”.

> **Stacks 076Z.** Let `M` be a rule assigning to a category fibred in groupoids over `S` a
> predicate on the modules on its étale site. If `M` cuts out a weak Serre subcategory everywhere,
> is stable under inverse image along a smooth 1-morphism, is local for every jointly surjective
> family of smooth 1-morphisms indexed in `Type (max u s)`, and is preserved by the higher direct
> images between algebraic stacks representable by affine schemes, then the higher direct images
> carry the rule into the rule along every quasi-compact (**Stacks 050U**) quasi-separated
> (**Stacks 04YW**) 1-morphism of algebraic stacks, in every degree.
>
> This is `AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion_unconditional`.
> Hypothesis (3) is the source's, read for the families indexed in `Type (max u s)`: the source asks
> it of every jointly surjective family whatever its index set, so its hypothesis implies this one
> and this statement implies the source's.

```lean
alias smoothLocalHigherDirectImageCriterion
```

**`AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmoothLocalHigherDirectImageCriterionProof.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmoothLocalHigherDirectImageCriterionProof.lean#L85). The attribute's comment: “the whole statement: every rule satisfying the source's four hypotheses, every quasi-compact quasi-separated 1-morphism of algebraic stacks and every degree; hypothesis (3) is read for the families indexed in a universe containing u, which the source's hypothesis implies, so the statement is no weaker than the source's”.

> Let `M` be a rule on the modules on the étale sites of the algebraic stacks over `S` such that
> (1) it cuts out a weak Serre subcategory on every algebraic stack, (2) it is preserved by inverse
> image along every smooth 1-morphism, (3) membership in it is local for every jointly surjective
> family of smooth 1-morphisms indexed in `Type (max u s)`, and (4) the higher direct images along
> every 1-morphism between algebraic stacks representable by affine schemes carry it into itself.
> Then the higher direct images along every quasi-compact quasi-separated 1-morphism of algebraic
> stacks carry `M` into `M`, in every degree.
>
> Hypothesis (3) is the source's, read for the families indexed in `Type (max u s)`: the source asks
> it of every jointly surjective family whatever its index set, so its hypothesis implies this one
> and this statement implies the source's (see the module documentation).

```lean
theorem smoothLocalHigherDirectImageCriterion_unconditional :
    SmoothLocalHigherDirectImageCriterion.{u, t, max u s} B S hS
```

## Tag 0770, a lemma

[Tag 0770](https://stacks.math.columbia.edu/tag/0770) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.higherDirectImage_mem_of_quasiCompact_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFppfWeakSerre.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFppfWeakSerre.lean#L486). The attribute's comment: “the reduction of the quasi-compact quasi-separated case to the affine case, which is the source's own clause (4), from clauses (1) to (4) together with two hypothesised prerequisites, the base-change isomorphisms of Stacks 075H and the fppf relative Cech pushforward spectral sequence of Stacks 072G part (2)(b)”.

> **Stacks 0770.** Let `M` be a rule which associates to every algebraic stack `𝒳` over `S` a
> subcategory `M_𝒳` of `Mod(𝒪_𝒳)`, the modules on the fppf site of `𝒳`, such that
>
> 1. `M_𝒳` is a weak Serre subcategory of `Mod(𝒪_𝒳)` for every algebraic stack `𝒳`;
> 2. for a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` the inverse image `f^*` maps `M_𝒴` into `M_𝒳`;
> 3. `M` is smooth-local on the target; and
> 4. for a 1-morphism of stacks representable by affine schemes, `Rⁱf_*` maps `M` into `M`.
>
> Then for every quasi-compact and quasi-separated 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks and
> every `F` in `M_𝒳`, the higher direct image `Rⁱf_* F`, computed in the fppf topology, lies in
> `M_𝒴`.
>
> The proof is the source's: the first move
> (`AlgebraicGeometry.Stack.AlgebraicStacks.higherDirectImagesMapInto_of_smoothAffineCover`)
> transports the question along a smooth presentation of `𝒴` by affine-representable stacks, using
> clauses (1), (2), (3) and the base-change isomorphisms; the second
> (`AlgebraicGeometry.Stack.AlgebraicStacks.higherDirectImagesMapInto_of_abutsTo`) settles each
> base-changed 1-morphism, whose target is affine-representable and which is again quasi-compact
> and quasi-separated, from clauses (1), (2), (4) and the Čech spectral sequence.
>
> Two prerequisites beyond the four clauses are hypothesised, `hpres` and `hcech`: the base-change
> isomorphisms of **Stacks 075H** and the Čech spectral sequence of **Stacks 072G** part (2).

```lean
theorem higherDirectImage_mem_of_quasiCompact_quasiSeparated (M : ModuleRule.{u, w} B S hS)
    (hSerre : ∀ 𝒳 : AlgebraicStacks.{u, w} B S hS, (M 𝒳).IsWeakSerreClass)
    (hSmooth : IsSmoothPullbackStable B S hS M) (hLocal : IsSmoothLocal B S hS M)
    (hAffine : AffineHigherDirectImagesMapInto B S hS M)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : Stack.IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (hpres : HasSmoothAffineBaseChange B S hS f)
    (hcech : ∀ {𝒳' 𝒴' : AlgebraicStacks.{u, w} B S hS} (f' : 𝒳' ⟶ 𝒴'),
      Stack.IsQuasiCompactMorphism B S hS f' →
      AlgebraicStacks.IsQuasiSeparated B S hS f' → IsAffineRepresentable B S hS 𝒴' →
      HasFppfCechPresentation B S hS f')
    (i : ℕ) (F : fppfModules B S hS 𝒳) (hF : M 𝒳 F) :
    M 𝒴 ((fppfHigherDirectImage B S hS f i).obj F)
```

**`AlgebraicGeometry.Stack.StackModuleRule.preservesHigherDirectImages_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalRule.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalRule.lean#L153). The attribute's comment: “the whole statement: every rule satisfying (1)-(4), every quasi-compact quasi-separated 1-morphism of algebraic stacks and every degree, higher direct images in the fppf topology; (1) read as M\_X weak Serre (the source's O\_X is a typo), (3) asked for families indexed by Type u only”.

> **Stacks 0770.** Let `M` be a rule which associates to every algebraic stack `𝒳` over `S` a
> property `M_𝒳` of the sheaves of `𝒪_𝒳`-modules on the fppf site of `𝒳` such that
>
> 1. `M_𝒳` is a weak Serre subcategory of `Mod(𝒪_𝒳)` for all algebraic stacks `𝒳`;
> 2. for a smooth 1-morphism `f : 𝒵 ⟶ 𝒳` the inverse image `f^*` maps `M_𝒳` into `M_𝒵`;
> 3. if `fᵢ : 𝒳ᵢ ⟶ 𝒳` is a family of smooth 1-morphisms with `|𝒳| = ⋃ᵢ |fᵢ|(|𝒳ᵢ|)`, then a module
>    `ℱ` lies in `M_𝒳` if and only if every `fᵢ^*ℱ` lies in `M_{𝒳ᵢ}`; and
> 4. if `f : 𝒳 ⟶ 𝒴` is a 1-morphism of algebraic stacks and `𝒳` and `𝒴` are representable by
>    affine schemes, then `Rⁱf_*` maps `M_𝒳` into `M_𝒴`.
>
> Then for every quasi-compact and quasi-separated 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks,
> `Rⁱf_*` maps `M_𝒳` into `M_𝒴` in every degree, the higher direct images being computed in the
> fppf topology.
>
> Clause (1) is read as "`M_𝒳` is a weak Serre subcategory": the source prints "`𝒪_𝒳` is a weak
> Serre subcategory", a typo, as the identical clause (1) of **Stacks 076Z** shows. Clause (3) is
> asked only for families indexed by a type in the universe of the schemes, which makes the
> hypothesis weaker and the theorem stronger. "Representable by an affine scheme" in clause (4) is
> equivalence over the site with the big site of an affine scheme
> (`AlgebraicGeometry.Stack.AlgebraicStacks.IsAffineRepresentable`). Modules have sections in the
> universe of the schemes, and the higher direct images are the right derived functors of the
> direct image right adjoint to the inverse image.

```lean
theorem preservesHigherDirectImages_fppf (M : StackModuleRule.{u, t} B S hS .fppf)
    (h1 : IsWeakSerre .fppf M) (h2 : IsStableUnderSmoothPullback .fppf M)
    (h3 : IsSmoothLocal.{u, t, u} .fppf M)
    (h4 : PreservesHigherDirectImagesOfAffine (stackModuleDirectImageData.{u, t} B S hS .fppf) M) :
    PreservesHigherDirectImages (stackModuleDirectImageData.{u, t} B S hS .fppf) M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.5, Tag 076Y](https://stacks.math.columbia.edu/tag/076Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
