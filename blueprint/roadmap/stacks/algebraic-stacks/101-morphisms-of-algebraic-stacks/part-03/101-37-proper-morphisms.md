---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsProper, AlgebraicGeometry.Stack.AlgebraicStacks.isProper_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isProper_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_isClosedImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_comp_of_isSeparated, AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_range_of_comp_of_isSeparated, AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_comp_of_isSeparated, AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_surjective_comp
statement: formalized
proof: formalized
---

# 101.37 Proper morphisms

Section 101.37 of the Stacks Project, [Tag 0CL4](https://stacks.math.columbia.edu/tag/0CL4). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CL5, a definition

[Tag 0CL5](https://stacks.math.columbia.edu/tag/0CL5) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsProper`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean#L111).

> **Stacks 0CL5.** A 1-morphism of algebraic stacks over `S` *is proper* when it is separated
> (**Stacks 04YW**), of finite type (**Stacks 06FS**, part (2)) and universally closed
> (**Stacks 0513**, part (2)).
>
> This is properness for an *arbitrary* 1-morphism of algebraic stacks; the Stacks 04XB relative
> notion for a 1-morphism representable by algebraic spaces is
> `AlgebraicGeometry.Stack.IsProper`.

```lean
abbrev IsProper {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CL6, a lemma

[Tag 0CL6](https://stacks.math.columbia.edu/tag/0CL6) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperBaseChangeAlgebraicStack.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperBaseChangeAlgebraicStack.lean#L84).

> **Stacks 0CL6.** A base change of a proper 1-morphism of algebraic stacks over `S` is proper:
> if `f : 𝒳 ⟶ 𝒴` is proper and `P` is any 2-fibre product square of the cospan `(g, f)` for some
> `g : 𝒴' ⟶ 𝒴`, then the projection `P.fst` — the base change of `f` along `g` — is proper.
>
> Properness is separatedness, finite type and universal closedness (Stacks 0CL5), and the three
> conjuncts base change by **Stacks 050F**, **Stacks 06FU** and **Stacks 0514** respectively, which
> is the source's own proof.

```lean
theorem isProper_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsProper B S hS f) :
    IsProper B S hS P.fst
```

## Tag 0CL7, a lemma

[Tag 0CL7](https://stacks.math.columbia.edu/tag/0CL7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperCompositionAlgebraicStack.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperCompositionAlgebraicStack.lean#L78).

> **Stacks 0CL7.** A composition of proper 1-morphisms of algebraic stacks over `S` is proper:
> if `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` are proper, then so is `f ≫ g`.
>
> Properness is separatedness, finite type and universal closedness (Stacks 0CL5), and the three
> conjuncts compose by **Stacks 050K**, **Stacks 06FT** and **Stacks 0515** respectively, which is
> the source's own proof.

```lean
theorem isProper_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsProper B S hS f) (hg : IsProper B S hS g) :
    IsProper B S hS (f ≫ g)
```

## Tag 0CL8, a lemma

[Tag 0CL8](https://stacks.math.columbia.edu/tag/0CL8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperClosedImmersionAlgebraicStack.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperClosedImmersionAlgebraicStack.lean#L130).

> **Stacks 0CL8.** A closed immersion of algebraic stacks over `S` is a proper 1-morphism of
> algebraic stacks.
>
> Properness is the conjunction of **Stacks 0CL5**, and its three conjuncts are discharged in
> turn: separatedness through monomorphy (**Stacks 0504** and **06MY**), local finite type by
> **Stacks 06FV** for immersions, quasi-compactness by **Stacks 0CL1**, and universal closedness
> from stability of closed immersions under base change (**Stacks 045C**) together with their
> closedness on points (**Stacks 0H20**).

```lean
theorem isProper_of_isClosedImmersion (f : 𝒳 ⟶ 𝒴) (hf : IsClosedImmersion B S hS f) :
    IsProper B S hS f
```

## Tag 0CPT, a lemma

[Tag 0CPT](https://stacks.math.columbia.edu/tag/0CPT) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean#L146). The attribute's comment: “part (1): universal closedness”. References: EGA II (5.4.9), “5.4.3 univ. closed”.

> **Stacks 0CPT, part (1).** If a composite of 1-morphisms of algebraic stacks over `S` is
> universally closed and its second factor is separated, then its first factor is universally
> closed.
>
> `f` is 2-isomorphic to its graph over `𝒵` followed by the second projection of the canonical
> 2-fibre product of the cospan `(f ≫ g, g)`. The graph is universally closed because `g` is
> separated, the projection is the base change of `f ≫ g` along `g` and so is universally closed
> by **Stacks 0514**, and **Stacks 0515** composes them.

```lean
theorem universallyClosed_of_comp_of_isSeparated (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : UniversallyClosed B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_range_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean#L163). The attribute's comment: “part (1): closed image”.

> **Stacks 0CPT, part (1).** Under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_comp_of_isSeparated` the image of
> `|𝒳|` in `|𝒴|` is closed for the topology of Stacks 04XL.

```lean
theorem isClosed_range_of_comp_of_isSeparated (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : UniversallyClosed B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    @_root_.IsClosed _ (Stack.pointTopology B S hS 𝒴.val)
      (Set.range (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperCancellation.lean#L182). The attribute's comment: “part (2): properness”.

> **Stacks 0CPT, part (2).** If a composite of 1-morphisms of algebraic stacks over `S` is
> proper and its second factor is separated, then its first factor is proper.
>
> Properness of **Stacks 0CL5** is separatedness, finite type and universal closedness. The first
> is **Stacks 050M** part (3), whose hypothesis on `Δ_g` is separatedness in the sense of
> Stacks 04XB and follows from the properness of `Δ_g` that separatedness of `g` asserts. Finite
> type is local finite type, which cancels outright by **Stacks 06U9**, together with
> quasi-compactness, which cancels against the quasi-separatedness of `g` by **Stacks 050Y**.
> Universal closedness is part (1).

```lean
theorem isProper_of_comp_of_isSeparated (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsProper B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    IsProper B S hS f
```

## Tag 0CQK, a lemma

[Tag 0CQK](https://stacks.math.columbia.edu/tag/0CQK) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_surjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperImageAlgebraicStack.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperImageAlgebraicStack.lean#L107). The attribute's comment: “universally closed image”.

> **Stacks 0CQK, universal closedness of the image.** If the composite `f ≫ q` of 1-morphisms
> of algebraic stacks over `S` is universally closed and `f` is surjective, then `q` is universally
> closed.

```lean
theorem universallyClosed_of_surjective_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : UniversallyClosed B S hS (f ≫ q)) (hf : Stack.IsSurjective B S hS f) :
    UniversallyClosed B S hS q
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_surjective_universallyClosed_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperImageAlgebraicStack.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProperImageAlgebraicStack.lean#L139). The attribute's comment: “properness of the image”. References: EGA II (5.4.3), “(ii)”.

> **Stacks 0CQK, properness of the image.** If the composite `f ≫ q` of 1-morphisms of
> algebraic stacks over `S` is universally closed, `f` is surjective and `q` is separated and of
> finite type, then `q` is proper.

```lean
theorem isProper_of_surjective_universallyClosed_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : UniversallyClosed B S hS (f ≫ q)) (hf : Stack.IsSurjective B S hS f)
    (hsep : IsSeparated B S hS q) (hft : IsFiniteType B S hS q) :
    IsProper B S hS q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.37, Tag 0CL4](https://stacks.math.columbia.edu/tag/0CL4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
