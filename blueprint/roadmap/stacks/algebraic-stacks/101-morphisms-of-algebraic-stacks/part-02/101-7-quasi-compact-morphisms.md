---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isQuasiCompact_iff_baseChange_quasiCompact, AlgebraicGeometry.Stack.IsQuasiCompactMorphism, AlgebraicGeometry.Stack.isQuasiCompactMorphism_baseChange, AlgebraicGeometry.Stack.isQuasiCompactMorphism_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiCompactMorphism_of_isClosedImmersion, AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_comp_of_isSurjective, AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_comp_of_isQuasiSeparated, AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack
statement: formalized
proof: formalized
---

# 101.7 Quasi-compact morphisms

Section 101.7 of the Stacks Project, [Tag 050S](https://stacks.math.columbia.edu/tag/050S). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 050T, a lemma

[Tag 050T](https://stacks.math.columbia.edu/tag/050T) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompact_iff_baseChange_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphism.lean, line 800](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphism.lean#L800).

> For a 1-morphism of algebraic stacks over `S` representable by algebraic
> spaces, quasi-compactness in the sense of Properties of Stacks, Section 04XB — every algebraic
> space representing a base change along a scheme-valued point of the target is quasi-compact over
> its base — is equivalent to quasi-compactness in the sense of Stacks 050U: every base change by a
> quasi-compact algebraic stack is a quasi-compact algebraic stack.

```lean
public theorem isQuasiCompact_iff_baseChange_quasiCompact
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    IsQuasiCompact B S hS f.hom ↔ IsQuasiCompactMorphism.{u, w} B S hS f
```

## Tag 050U, a definition

[Tag 050U](https://stacks.math.columbia.edu/tag/050U) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsQuasiCompactMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphism.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphism.lean#L58).

> A 1-morphism of algebraic stacks over `S` is *quasi-compact* when every base change of it by
> a quasi-compact algebraic stack is again a quasi-compact algebraic stack, the fibre product being
> the canonical 2-fibre product of algebraic stacks and quasi-compactness being
> `AlgebraicGeometry.Stack.IsQuasiCompactStack`.

```lean
abbrev IsQuasiCompactMorphism {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 050V, a lemma

[Tag 050V](https://stacks.math.columbia.edu/tag/050V) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean#L104).

> **Stacks 050V.** A base change of a quasi-compact 1-morphism of algebraic stacks over `S` is
> quasi-compact: if `P` is a 2-fibre product of the cospan `(g, f)` and `f` is quasi-compact, then
> the projection `P.fst` is quasi-compact.
>
> The base change of `P.fst` by a test 1-morphism `k` is `𝒵 ×_{𝒴'} P.pt`, and Stacks 02XD at the
> recognised 2-fibre product `P` identifies it with a 2-fibre product of the cospan `(f, k ≫ g)`;
> the base change of `f` along `k ≫ g` is another, and it is quasi-compact by hypothesis.

```lean
theorem isQuasiCompactMorphism_baseChange {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P) (hf : IsQuasiCompactMorphism B S hS f) :
    IsQuasiCompactMorphism B S hS P.fst
```

## Tag 050W, a lemma

[Tag 050W](https://stacks.math.columbia.edu/tag/050W) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean#L86).

> **Stacks 050W.** The composite of two quasi-compact 1-morphisms of algebraic stacks over `S`
> is quasi-compact.
>
> A base change of `f ≫ g` by a quasi-compact algebraic stack is the iterated 2-fibre product
> `(𝒲 ×_𝒵 𝒴) ×_𝒴 𝒳`; the inner apex is quasi-compact because `g` is, the outer one because `f` is,
> and Stacks 02XD identifies the outer apex with a 2-fibre product of the cospan of `f ≫ g`.

```lean
theorem isQuasiCompactMorphism_comp {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsQuasiCompactMorphism B S hS f) (hg : IsQuasiCompactMorphism B S hS g) :
    IsQuasiCompactMorphism B S hS (f ≫ g)
```

## Tag 0CL1, a lemma

[Tag 0CL1](https://stacks.math.columbia.edu/tag/0CL1) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiCompactMorphism_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClosedImmersionQuasiCompact.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ClosedImmersionQuasiCompact.lean#L71).

> **Stacks 0CL1.** A closed immersion of algebraic stacks over `S` is quasi-compact.
>
> A closed immersion is representable by algebraic spaces (Stacks 04YL, part (2)), which is the
> hypothesis of **Stacks 050T**; and its second conjunct `AlgebraicGeometry.Stack.IsClosedImmersion`
> differs from `AlgebraicGeometry.Stack.IsQuasiCompact` only in the property demanded of the
> structural morphism of each representing algebraic space, so **Stacks 04CG** transfers it
> pointwise.

```lean
theorem isQuasiCompactMorphism_of_isClosedImmersion
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsClosedImmersion B S hS f) :
    Stack.IsQuasiCompactMorphism.{u, w} B S hS f
```

## Tag 050X, a lemma

[Tag 050X](https://stacks.math.columbia.edu/tag/050X) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_comp_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean#L139).

> **Stacks 050X.** Let `f : 𝒳 ⟶ 𝒴`, `p : 𝒳 ⟶ 𝒵` and `q : 𝒴 ⟶ 𝒵` be a 2-commutative triangle
> of 1-morphisms of algebraic stacks over `S`. If `f` is surjective and `p` is quasi-compact, then
> `q` is quasi-compact.
>
> A base change `𝒯 ×_𝒵 𝒴` of `q` by a quasi-compact algebraic stack receives the iterated product
> `(𝒯 ×_𝒵 𝒴) ×_𝒴 𝒳`, which is a base change of the surjective `f` and hence surjects onto it
> (Stacks 04ZU); Stacks 02XD identifies that iterated apex with a 2-fibre product of the cospan
> `(k, p)`, quasi-compact by the hypothesis on `p`, and quasi-compactness of an algebraic stack
> passes along a surjection.

```lean
theorem isQuasiCompactMorphism_of_comp_of_isSurjective
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒵) (q : 𝒴 ⟶ 𝒵) (e : f ≫ q ≅ p)
    (hf : IsSurjective B S hS f) (hp : IsQuasiCompactMorphism B S hS p) :
    IsQuasiCompactMorphism B S hS q
```

## Tag 050Y, a lemma

[Tag 050Y](https://stacks.math.columbia.edu/tag/050Y) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_comp_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactMorphismPermanence.lean#L186). References: EGA IV (1.2.4).

> **Stacks 050Y.** If a composite of 1-morphisms of algebraic stacks over `S` is quasi-compact
> and its second factor is quasi-separated, then its first factor is quasi-compact.
>
> `f` is the composite of its graph section with the projection of `𝒴 ×_𝒵 𝒳` to `𝒴`. The projection
> to `𝒳` is a base change of `g`, hence quasi-separated (Stacks 050F), so the graph section is
> quasi-compact by Stacks 050J part (5); the projection to `𝒴` is a base change of `f ≫ g`, hence
> quasi-compact by Stacks 050V; and Stacks 050W composes the two.

```lean
theorem isQuasiCompactMorphism_of_comp_of_isQuasiSeparated (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hgf : IsQuasiCompactMorphism B S hS (f ≫ g))
    (hg : AlgebraicStacks.IsQuasiSeparated B S hS g) :
    IsQuasiCompactMorphism B S hS f
```

## Tag 075S, a lemma

[Tag 075S](https://stacks.math.columbia.edu/tag/075S) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean#L172). The attribute's comment: “part (1)”. References: SGA 4 VI (1.14), “(i), algebraic stacks”.

> **Stacks 075S, part (1).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over a
> quasi-separated base scheme with `𝒳` quasi-compact and `𝒴` quasi-separated over the base is
> quasi-compact.
>
> The structure morphism of `𝒳` is `f` followed by the structure morphism of `𝒴`, and it is
> quasi-compact because `𝒳` is; the structure morphism of `𝒴` is quasi-separated because `𝒴` is
> quasi-separated over the base; so Stacks 050Y cancels it.

```lean
theorem isQuasiCompactMorphism_of_isQuasiCompactStack (hqs : QuasiSeparatedSpace S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒴 : IsQuasiSeparatedOver.{u, w} B S hS 𝒴) :
    IsQuasiCompactMorphism.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_and_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean#L190). The attribute's comment: “part (2)”. References: SGA 4 VI (1.14), “(i), stacks, X also qs”.

> **Stacks 075S, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over a
> quasi-separated base scheme with `𝒳` quasi-compact and quasi-separated over the base and `𝒴`
> quasi-separated over the base is quasi-compact and quasi-separated.
>
> Quasi-compactness is part (1); quasi-separatedness is Stacks 050N part (8), whose hypothesis on
> the relative diagonal of the structure morphism of `𝒴` is the second conjunct of
> quasi-separatedness of `𝒴` over the base.

```lean
theorem isQuasiCompactMorphism_and_isQuasiSeparated (hqs : QuasiSeparatedSpace S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒳qc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : IsQuasiSeparatedOver.{u, w} B S hS 𝒳)
    (h𝒴 : IsQuasiSeparatedOver.{u, w} B S hS 𝒴) :
    IsQuasiCompactMorphism.{u, w} B S hS f ∧
      AlgebraicStacks.IsQuasiSeparated.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiCompactStack_and_isQuasiSeparatedOver_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStack.lean#L209). The attribute's comment: “part (3)”.

> **Stacks 075S, part (3).** A 2-fibre product `𝒳 ×_𝒴 𝒵` of algebraic stacks over a
> quasi-separated base scheme, with `𝒳`, `𝒵` quasi-compact and quasi-separated over the base and
> `𝒴` quasi-separated over the base, is quasi-compact and quasi-separated over the base.
>
> The projection to `𝒵` is a base change of `f`, which is quasi-compact and quasi-separated by
> part (2), hence is itself quasi-compact (Stacks 050V) and quasi-separated (Stacks 050F). A
> quasi-compact 1-morphism into the quasi-compact `𝒵` has quasi-compact source, and Stacks 050L
> part (4) carries quasi-separatedness over the base from `𝒵` to the apex.

```lean
theorem isQuasiCompactStack_and_isQuasiSeparatedOver_twoFibreProduct
    (hqs : QuasiSeparatedSpace S) {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (h𝒳qc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : IsQuasiSeparatedOver.{u, w} B S hS 𝒳)
    (h𝒵qc : IsQuasiCompactStack.{u, w} B S hS 𝒵.val 𝒵.property)
    (h𝒵qs : IsQuasiSeparatedOver.{u, w} B S hS 𝒵)
    (h𝒴 : IsQuasiSeparatedOver.{u, w} B S hS 𝒴) :
    IsQuasiCompactStack.{u, w} B S hS
        (twoFibreProductAlgebraicStack B S hS f g).val
        (twoFibreProductAlgebraicStack B S hS f g).property ∧
      IsQuasiSeparatedOver.{u, w} B S hS (twoFibreProductAlgebraicStack B S hS f g)
```

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack_absolute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean#L155). The attribute's comment: “part (1)”. References: SGA 4 VI (1.14), “(i), algebraic stacks”.

> **Stacks 075S, part (1).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks with `𝒳` quasi-compact
> and `𝒴` quasi-separated in the absolute sense of Stacks 050D part (8) is quasi-compact. Nothing is
> asked of the base scheme of the big fppf site.
>
> Quasi-compactness of a 1-morphism is Stacks 050U, so what has to be shown is quasi-compactness of
> each base change of `f` by a quasi-compact algebraic stack. Over the terminal scheme the relative
> statement `AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack` applies with no
> hypothesis — the terminal scheme is affine, hence quasi-separated — to the views of `f` and of the
> test stack, whose quasi-compactness is
> `AlgebraicGeometry.Stack.isQuasiCompactStack_changeBaseAlgebraicStack_iff`; and
> `AlgebraicGeometry.Stack`
> `.isQuasiCompactStack_twoFibreProductAlgebraicStack_of_viewOverIntegers` brings the resulting
> quasi-compact 2-fibre product back to `S`.

```lean
theorem isQuasiCompactMorphism_of_isQuasiCompactStack_absolute
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒴 : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒴) :
    IsQuasiCompactMorphism.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_and_isQuasiSeparated_absolute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean#L177). The attribute's comment: “part (2)”. References: SGA 4 VI (1.14), “(i), stacks, X also qs”.

> **Stacks 075S, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks with `𝒳` quasi-compact
> and quasi-separated and `𝒴` quasi-separated, both in the absolute sense of Stacks 050D part (8),
> is quasi-compact and quasi-separated.
>
> Quasi-compactness is part (1). Quasi-separatedness is Stacks 050N part (8), whose two inputs are
> the over-the-base readings of the two absolute hypotheses, supplied by Stacks 050N part (4).

```lean
theorem isQuasiCompactMorphism_and_isQuasiSeparated_absolute
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒳qc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳)
    (h𝒴 : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒴) :
    IsQuasiCompactMorphism.{u, w} B S hS f ∧
      AlgebraicStacks.IsQuasiSeparated.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiCompactStack_and_isAbsolutelyQuasiSeparated_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean#L203). The attribute's comment: “part (3)”.

> **Stacks 075S, part (3).** A 2-fibre product `𝒳 ×_𝒴 𝒵` of algebraic stacks, with `𝒳`, `𝒵`
> quasi-compact and quasi-separated and `𝒴` quasi-separated, all in the absolute sense of
> Stacks 050D part (8), is quasi-compact and quasi-separated in that same absolute sense. Nothing is
> asked of the base scheme of the big fppf site.
>
> The projection to `𝒵` is a base change of `f`, which is quasi-compact and quasi-separated by
> part (2), hence is itself quasi-compact (Stacks 050V) and quasi-separated (Stacks 050F). A
> quasi-compact 1-morphism into the quasi-compact `𝒵` has quasi-compact source, and Stacks 050L
> part (8) carries absolute quasi-separatedness from `𝒵` to the apex.
>
> The absolute conclusion is what the next application of part (1) needs of its target, which the
> over-the-base conclusion of
> `AlgebraicGeometry.Stack.isQuasiCompactStack_and_isQuasiSeparatedOver_twoFibreProduct` is not.

```lean
theorem isQuasiCompactStack_and_isAbsolutelyQuasiSeparated_twoFibreProduct
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (h𝒳qc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳)
    (h𝒵qc : IsQuasiCompactStack.{u, w} B S hS 𝒵.val 𝒵.property)
    (h𝒵qs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒵)
    (h𝒴 : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒴) :
    IsQuasiCompactStack.{u, w} B S hS
        (twoFibreProductAlgebraicStack B S hS f g).val
        (twoFibreProductAlgebraicStack B S hS f g).property ∧
      AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ
        (twoFibreProductAlgebraicStack B S hS f g)
```

## Tag 0CL2, a lemma

[Tag 0CL2](https://stacks.math.columbia.edu/tag/0CL2) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_valuationRing_of_mem_closure_range_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClosureImageValuativePoint.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ClosureImageValuativePoint.lean#L473).

> A point in the closure of the image of a quasi-compact 1-morphism of algebraic stacks is
> reached by the closed point of a valuative square. **Stacks 0CL2.**

```lean
theorem exists_valuationRing_of_mem_closure_range_pointsMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hf : IsQuasiCompactMorphism.{u, w} B S hS f)
    (y : points B S hS 𝒴.val.val (Classical.choose 𝒴.property))
    (hy : y ∈ @closure _
      (pointTopology B S hS 𝒴.val)
      (Set.range
      (pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
        (Classical.choose 𝒴.property) f.hom.hom))) :
    ∃ (q : ValuativeSquare B S hS f)
      (hz : B.Contains
        (Spec (.of ((Spec (.of q.R)).residueField (IsLocalRing.closedPoint q.R))))),
      pointClass B S hS 𝒴.val.val
        (Classical.choose 𝒴.property)
        (fieldValuedPointMap B S hS
          (schemeFibredCategory B S hS
            (siteObject B S hS q.ring_mem q.base)).val
          q.y.hom
          (closedPointFieldValuedPoint B S hS
            (siteObject B S hS q.ring_mem q.base)
            (IsLocalRing.closedPoint q.R) hz)) = y
```

## Tag 0DTL, a lemma

[Tag 0DTL](https://stacks.math.columbia.edu/tag/0DTL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactMorphism_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactFppfDescent.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactFppfDescent.lean#L199).

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : W ⟶ 𝒴` be surjective, flat and locally of finite presentation, where `W` is an algebraic
> space. If the base change `W ×_𝒴 𝒳 ⟶ W` of `f` along `g` is quasi-compact, then `f` is
> quasi-compact.

```lean
theorem isQuasiCompactMorphism_of_isQuasiCompactMorphism_fst
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    {W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hW : IsAlgebraicSpace B S hS W)
    (g : algebraicSpaceStack.{u, w} B S hS W hW ⟶ 𝒴)
    (hgsurj : IsSurjective B S hS g)
    (hgflat : AlgebraicStacks.IsFlat B S hS g)
    (hglfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hbase : IsQuasiCompactMorphism B S hS P.fst) :
    IsQuasiCompactMorphism B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.7, Tag 050S](https://stacks.math.columbia.edu/tag/050S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
