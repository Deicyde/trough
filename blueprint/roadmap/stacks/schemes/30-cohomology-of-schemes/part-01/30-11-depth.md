---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafHasDepthAt, AlgebraicGeometry.SchemeHasDepthAt, AlgebraicGeometry.SheafHasPropertySk, AlgebraicGeometry.HasPropertySk, AlgebraicGeometry.one_le_depth_stalk_internalHom, AlgebraicGeometry.two_le_depth_stalk_internalHom, AlgebraicGeometry.sheafHasPropertySk_one_internalHom, AlgebraicGeometry.sheafHasPropertySk_two_internalHom
statement: formalized
proof: formalized
---

# 30.11 Depth

Section 30.11 of the Stacks Project, [Tag 0340](https://stacks.math.columbia.edu/tag/0340). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0341, a definition

[Tag 0341](https://stacks.math.columbia.edu/tag/0341) in the Stacks Project.

**`AlgebraicGeometry.SheafHasDepthAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean#L54). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0341.** A sheaf of modules has depth `k` at `x` when its stalk has
> depth `k` over the local ring at `x`.

```lean
abbrev SheafHasDepthAt (X : Scheme.{u})
    (F : SheafOfModules.{u} (structureSheafRing
      X.toRingedSpace)) (x : X)
    (k : ℕ) : Prop
```

**`AlgebraicGeometry.SchemeHasDepthAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean#L64). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0341.** A scheme has depth `k` at `x` when its local ring at `x` has
> depth `k` over itself.

```lean
abbrev SchemeHasDepthAt (X : Scheme.{u}) (x : X) (k : ℕ) : Prop
```

**`AlgebraicGeometry.SheafHasPropertySk`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean#L72). The attribute's comment: “part (3)”. References: EGA IV (5.7.2), “more general”.

> **Stacks Project, Tag 0341.** Serre's condition `(Sₖ)` for a sheaf of modules: at every
> point its depth is at least the minimum of `k` and the dimension of the support of its
> stalk.

```lean
abbrev SheafHasPropertySk (X : Scheme.{u})
    (F : SheafOfModules.{u} (structureSheafRing
      X.toRingedSpace))
    (k : ℕ) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.HasPropertySk`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Serre.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean#L83) (StacksFrontier): “part (4)”.

## Tag 0EBC, a lemma

[Tag 0EBC](https://stacks.math.columbia.edu/tag/0EBC) in the Stacks Project.

**`AlgebraicGeometry.one_le_depth_stalk_internalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean#L157). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0EBC], part (1).** For coherent modules on a locally Noetherian scheme, the
> stalk of `SheafHom(F, G)` at `x` has depth at least one as soon as `G_x` does.

```lean
public theorem one_le_depth_stalk_internalHom [IsLocallyNoetherian X] (F G : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (H : SheafHom X.sheaf F G) (x : X)
    (hx : (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (G.presheaf.stalk x)) :
    (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      ((internalHomOf H).presheaf.stalk x)
```

**`AlgebraicGeometry.two_le_depth_stalk_internalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean#L170). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0EBC], part (2).** For coherent modules on a locally Noetherian scheme, the
> stalk of `SheafHom(F, G)` at `x` has depth at least two as soon as `G_x` does.

```lean
public theorem two_le_depth_stalk_internalHom [IsLocallyNoetherian X] (F G : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (H : SheafHom X.sheaf F G) (x : X)
    (hx : (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (G.presheaf.stalk x)) :
    (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      ((internalHomOf H).presheaf.stalk x)
```

## Tag 0AXQ, a lemma

[Tag 0AXQ](https://stacks.math.columbia.edu/tag/0AXQ) in the Stacks Project.

**`AlgebraicGeometry.sheafHasPropertySk_one_internalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean#L204). The attribute's comment: “hom\_into\_s1”.

> **[Stacks, Tag 0AXQ], part (1).** On a locally Noetherian scheme the internal hom of
> coherent modules into a module satisfying Serre's condition `(S₁)` satisfies `(S₁)`.

```lean
public theorem sheafHasPropertySk_one_internalHom [IsLocallyNoetherian X] (F G : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (H : SheafHom X.sheaf F G) (hG : SheafHasPropertySk X G 1) :
    SheafHasPropertySk X (internalHomOf H) 1
```

**`AlgebraicGeometry.sheafHasPropertySk_two_internalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/InternalHomDepth.lean#L216). The attribute's comment: “hom\_into\_s2”.

> **[Stacks, Tag 0AXQ], part (2).** On a locally Noetherian scheme the internal hom of
> coherent modules into a module satisfying Serre's condition `(S₂)` satisfies `(S₂)`.

```lean
public theorem sheafHasPropertySk_two_internalHom [IsLocallyNoetherian X] (F G : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (H : SheafHom X.sheaf F G) (hG : SheafHasPropertySk X G 2) :
    SheafHasPropertySk X (internalHomOf H) 2
```

## Tag 0343, a definition

[Tag 0343](https://stacks.math.columbia.edu/tag/0343) in the Stacks Project.

**`AlgebraicGeometry.SheafIsCohenMacaulay`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Depth.lean#L88). References: EGA IV (5.7.1).

> **Stacks Project, Tag 0343.** A sheaf of modules is Cohen–Macaulay when it satisfies
> Serre's condition `(Sₖ)` for every `k`.

```lean
abbrev SheafIsCohenMacaulay (X : Scheme.{u})
    (F : SheafOfModules.{u} (structureSheafRing
      X.toRingedSpace)) : Prop
```

## Tag 0B3K, a lemma

[Tag 0B3K](https://stacks.math.columbia.edu/tag/0B3K) in the Stacks Project.

**`AlgebraicGeometry.sheafIsCohenMacaulay_and_supp_eq_univ_iff_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/CohenMacaulayRegular.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/CohenMacaulayRegular.lean#L220). References: EGA 0 (17.3.5), “(i)”.

> **Stacks Project, Tag 0B3K.** Let `X` be a regular scheme and `F` a coherent
> `𝒪_X`-module. Then `F` is Cohen–Macaulay with support all of `X` if and only if it is finite
> locally free of positive rank at every point.

```lean
public theorem sheafIsCohenMacaulay_and_supp_eq_univ_iff_isFiniteLocallyFree
    (hX : IsRegular X) (F : X.Modules) [_root_.SheafOfModules.IsCoherent F] :
    (SheafIsCohenMacaulay X F ∧ _root_.SheafOfModules.supp F = Set.univ) ↔
      SheafOfModules.IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) F ∧
        ∀ x : X, 0 < Scheme.Modules.fiberRank F x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.11, Tag 0340](https://stacks.math.columbia.edu/tag/0340)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
