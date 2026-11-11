---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isProper_baseChange_of_isLimit, AlgebraicGeometry.exists_isLimit_isProper_finitePresentation_isClosedImmersion, AlgebraicGeometry.exists_isLimit_isProper_finiteType_arrow, AlgebraicGeometry.eventually_isProper_comp_π_app_of_isLimit, AlgebraicGeometry.exists_isProper_schemeTheoreticSupport_baseChange_of_isLimit
statement: formalized
proof: formalized
---

# 32.13 Applications of Chow's lemma

Section 32.13 of the Stacks Project, [Tag 0204](https://stacks.math.columbia.edu/tag/0204). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 081F, a lemma

[Tag 081F](https://stacks.math.columbia.edu/tag/081F) in the Stacks Project.

**`AlgebraicGeometry.exists_isProper_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowFiniteType/ModuleSupport.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ChowFiniteType/ModuleSupport.lean#L202).

> **Stacks 081F.** Assumptions and notation as in Situation 081D: `D` is a cofiltered inverse
> system of schemes with affine transition morphisms and limit cone `c`, and `f₀ : X₀ ⟶ Y₀` is a
> morphism of quasi-compact quasi-separated schemes over the quasi-compact quasi-separated stage
> `D.obj i₀`. If `f₀` is locally of finite type and its base change to the limit is proper, then
> its base change to some later stage is proper.
>
> Chow's lemma over the quasi-compact quasi-separated `Y₀` needs `f₀` to be separated, which is
> not assumed; following the Stacks proof, Stacks 01ZQ supplies separatedness at some stage `i₁`
> and the situation is re-indexed there before
> `AlgebraicGeometry.exists_isProper_baseChange_of_isLimit_of_isOneAffineOpenStep` is applied.

```lean
theorem exists_isProper_baseChange_of_isLimit
    (hc : IsLimit c) (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [IsProper ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (hi : i ⟶ i₀), IsProper ((Over.pullback (D.map hi)).map f₀).left
```

## Tag 09ZR, a lemma

[Tag 09ZR](https://stacks.math.columbia.edu/tag/09ZR) in the Stacks Project.

**`AlgebraicGeometry.exists_isLimit_isProper_finitePresentation_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperFinitePresentationLimit.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/ProperFinitePresentationLimit.lean#L66).

> **Stacks 09ZR.** A proper morphism onto a quasi-compact, quasi-separated scheme is a directed
> inverse limit, over that scheme, of proper morphisms of finite presentation whose transition
> morphisms and limit projections are all closed immersions.

```lean
theorem exists_isLimit_isProper_finitePresentation_isClosedImmersion
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Iᵒᵖ ⥤ Scheme.{u}) (t : D ⟶ (Functor.const Iᵒᵖ).obj S)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (_ : IsLimit (Cone.mk X p)),
      p ≫ t = (Functor.const Iᵒᵖ).map f ∧
        (∀ i, IsProper (t.app i) ∧ FinitePresentation (t.app i)) ∧
        (∀ (i j : Iᵒᵖ) (g : i ⟶ j), IsClosedImmersion (D.map g)) ∧
        (∀ i, IsClosedImmersion (p.app i))
```

## Tag 0A0P, a lemma

[Tag 0A0P](https://stacks.math.columbia.edu/tag/0A0P) in the Stacks Project.

**`AlgebraicGeometry.exists_isLimit_isProper_finiteType_arrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperLimitOfFiniteTypeOverZ.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/ProperLimitOfFiniteTypeOverZ.lean#L230).

> **Stacks 0A0P.** A proper morphism onto a quasi-compact and quasi-separated scheme is the
> inverse limit, over a directed set, of an inverse system of proper morphisms whose targets are of
> finite type over `ℤ` and whose transition morphisms are affine on both sources and targets.

```lean
theorem exists_isLimit_isProper_finiteType_arrow
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirectedOrder I)
      (D : Iᵒᵖ ⥤ Arrow Scheme.{u}) (c : Cone D),
      (∀ i, IsProper (D.obj i).hom) ∧
      (∀ i,
        LocallyOfFiniteType (terminal.from (D.obj i).right) ∧
          QuasiCompact (terminal.from (D.obj i).right)) ∧
      (∀ {i j : Iᵒᵖ} (g : i ⟶ j),
        IsAffineHom (D.map g).left ∧ IsAffineHom (D.map g).right) ∧
      Nonempty (IsLimit c) ∧ Nonempty (c.pt ≅ Arrow.mk f)
```

## Tag 0EX1, a lemma

[Tag 0EX1](https://stacks.math.columbia.edu/tag/0EX1) in the Stacks Project.

**`AlgebraicGeometry.eventually_isProper_comp_π_app_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/EventuallyProperOverLimit.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/EventuallyProperOverLimit.lean#L307).

> **Stacks 0EX1.** Let `X = lim Xᵢ` be the limit of a cofiltered inverse system of quasi-compact
> and quasi-separated schemes over `S` with affine transition morphisms. A proper morphism
> `f : Y ⟶ X` whose source is locally of finite type over `S` is proper over some stage of the
> system and over every later stage.

```lean
theorem eventually_isProper_comp_π_app_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    {S : Scheme.{u}} (D : I ⥤ Scheme.{u}) (t : D ⟶ (Functor.const I).obj S)
    (c : Cone D) (hc : IsLimit c) (pX : c.pt ⟶ S)
    (hpX : c.π ≫ t = (Functor.const I).map pX)
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    {Y : Scheme.{u}} (pY : Y ⟶ S) (f : Y ⟶ c.pt) (hf : f ≫ pX = pY)
    [LocallyOfFiniteType pY] [IsProper f] :
    ∃ i : I, ∀ (j : I) (_ : j ⟶ i), IsProper (f ≫ c.π.app j)
```

## Tag 081G, a lemma

[Tag 081G](https://stacks.math.columbia.edu/tag/081G) in the Stacks Project.

**`AlgebraicGeometry.exists_isProper_schemeTheoreticSupport_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowFiniteType/ModuleSupport.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ChowFiniteType/ModuleSupport.lean#L250).

> **Stacks 081G.** Assumptions and notation as in Situation 081D, and let `F₀` be a
> quasi-coherent `O_{X₀}`-module, with `F` and `F_i` its pullbacks to the base changes `X` and
> `X_i` of `X₀`. Assume `f₀` is locally of finite type, `F₀` is of finite type, and the
> scheme-theoretic support of `F` is proper over `Y`. Then the scheme-theoretic support of `F_i`
> is proper over `Y_i` for some `i`.
>
> The base change of `X₀` to a stage is the fibre product of `X₀.hom` with the transition
> morphism, so the pullback of `F₀` to it is its pullback along
> `CategoryTheory.Limits.pullback.fst`. The proof applies Stacks 081F to the restriction of `f₀`
> to the scheme-theoretic support of `F₀`.

```lean
theorem exists_isProper_schemeTheoreticSupport_baseChange_of_isLimit
    (hc : IsLimit c) (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀) (F₀ : X₀.left.Modules)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left] [F₀.IsQuasicoherent] [F₀.IsFiniteType]
    (hlim : IsProper ((Scheme.Modules.schemeTheoreticSupport
        ((Scheme.Modules.pullback (pullback.fst X₀.hom (c.π.app i₀))).obj F₀)).subschemeι ≫
        ((Over.pullback (c.π.app i₀)).map f₀).left)) :
    ∃ (i : I) (hi : i ⟶ i₀), IsProper ((Scheme.Modules.schemeTheoreticSupport
        ((Scheme.Modules.pullback (pullback.fst X₀.hom (D.map hi))).obj F₀)).subschemeι ≫
        ((Over.pullback (D.map hi)).map f₀).left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.13, Tag 0204](https://stacks.math.columbia.edu/tag/0204)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
