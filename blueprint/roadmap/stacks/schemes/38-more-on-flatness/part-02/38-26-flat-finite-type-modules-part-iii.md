---
declaration: section
origin: cited
lean: AlgebraicGeometry.isFlatOverAt_iff_forall_isAssociatedPoint_specializes, AlgebraicGeometry.isFlatOver_of_isFlatOverAt_closedFiber
statement: formalized
proof: formalized
---

# 38.26 Flat finite type modules, Part III

Section 38.26 of the Stacks Project, [Tag 05U8](https://stacks.math.columbia.edu/tag/05U8). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05UA, a theorem

[Tag 05UA](https://stacks.math.columbia.edu/tag/05UA) in the Stacks Project.

**`AlgebraicGeometry.isFlatOverAt_iff_forall_isAssociatedPoint_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatAtAssociatedPoints.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatAtAssociatedPoints.lean#L260). The attribute's comment: “`Ass_{X_s}(F_s)` is `Stacks.Divisors.associatedPoints` of the pullback of `F` to the scheme-theoretic fibre `f.fiber (f x)`, and flatness at a point is `IsFlatOverAt`.”.

> **Stacks 05UA.** Let `f : X ⟶ S` be locally of finite type, let `F` be a quasi-coherent
> `𝒪_X`-module of finite type and let `x ∈ X`. Then `F` is flat over `S` at `x` if and only if `F`
> is flat over `S` at every associated point of the restriction of `F` to the fibre over `f x`
> which specializes to `x`.

```lean
theorem isFlatOverAt_iff_forall_isAssociatedPoint_specializes {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (x : X) :
    IsFlatOverAt f.toLRSHom.toShHom F x ↔
      ∀ x' : f.fiber (f x),
        x' ∈ Stacks.Divisors.associatedPoints
            ((Scheme.Modules.pullback (f.fiberι (f x))).obj F) →
          f.fiberι (f x) x' ⤳ x → IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι (f x) x')
```

## Tag 05UB, a lemma

[Tag 05UB](https://stacks.math.columbia.edu/tag/05UB) in the Stacks Project.

**`AlgebraicGeometry.isFlatOver_of_isFlatOverAt_closedFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ClosedFibreFlatnessCheck.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ClosedFibreFlatnessCheck.lean#L92). The attribute's comment: “`Ass_{X/S}(F)` is `Stacks.Divisors.relativeAssassin`, the closed fibre `X_s` is `f.fiber s` placed in `X` by `f.fiberι s`, and flatness over the base at a point is `IsFlatOverAt`. A local scheme is an affine scheme whose ring of global sections is local.”.

> **Stacks Project, Tag 05UB.** Let `S` be a local scheme with closed point `s`, let
> `f : X ⟶ S` be locally of finite type and let `F` be a finite type quasi-coherent
> `𝒪_X`-module. If every point of `Ass_{X/S}(F)` specializes to a point of the closed fibre
> `X_s`, and `F` is flat over `S` at every point of `X_s`, then `F` is flat over `S`.
>
> The criterion of Stacks 05UA is
> `isFlatOverAt_iff_forall_isAssociatedPoint_specializes`, read at every point of the source.
> Everything else is `isFlatOverAt_of_mem_relativeAssassin`: the two hypotheses on `F` give
> flatness at every point of the relative assassin, which is what that criterion tests.

```lean
theorem isFlatOver_of_isFlatOverAt_closedFiber
    {X S : Scheme.{u}} [IsAffine S] [IsLocalRing Γ(S, ⊤)]
    (s : S) (_hs : s ∈ closedPoints S)
    (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hass : ∀ x ∈ Stacks.Divisors.relativeAssassin f F,
      ∃ y : f.fiber s, Specializes x (f.fiberι s y))
    (hflat : ∀ y : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s y)) :
    IsFlatOver f.toLRSHom.toShHom F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.26, Tag 05U8](https://stacks.math.columbia.edu/tag/05U8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
