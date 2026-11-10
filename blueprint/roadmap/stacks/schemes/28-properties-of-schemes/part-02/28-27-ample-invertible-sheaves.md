---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.IsAmple, Stacks.AmplePositivePower.isAmple_iff_isAmple_tensorPowModule, AlgebraicGeometry.isAmple_iff_tensorPower_isAmple, AlgebraicGeometry.Scheme.Modules.isAmple_pullback_of_isClosedImmersion, AlgebraicGeometry.Scheme.Modules.isAffineOpen_inf_nonvanishingOpen, Stacks.NonvanishingAffineIntersection.isAffineOpen_inf_nonvanishingOpen, AlgebraicGeometry.Scheme.Modules.isAmple_tensor_of_power_sections_cover, AlgebraicGeometry.Scheme.Modules.isBasis_affine_nonvanishingOpens
statement: formalized
proof: formalized
---

# 28.27 Ample invertible sheaves

Section 28.27 of the Stacks Project, [Tag 01PR](https://stacks.math.columbia.edu/tag/01PR). 15 tags here are carried by 54 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01PS, a definition

[Tag 01PS](https://stacks.math.columbia.edu/tag/01PS) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.IsAmple`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Ample/Defs.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Ample/Defs.lean#L95). References: EGA II (4.5.3).

> An invertible sheaf of modules on a scheme is *ample* if the scheme is quasi-compact and
> every point has an affine nonvanishing locus for some global section of a tensor power of
> positive exponent.

```lean
public def IsAmple : Prop
```

## Tag 01PT, a lemma

[Tag 01PT](https://stacks.math.columbia.edu/tag/01PT) in the Stacks Project.

**`Stacks.AmplePositivePower.isAmple_iff_isAmple_tensorPowModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePositivePower/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePositivePower/Basic.lean#L72). References: EGA II (4.5.6), “(i)”.

> An invertible `𝒪_X`-module `L` is ample if and only if its tensor power `L ^⊗ d` is ample,
> for any `d ≥ 1`.

```lean
theorem isAmple_iff_isAmple_tensorPowModule (d : ℕ) (hd : 1 ≤ d) :
    IsAmple X L ↔ IsAmple X (tensorPowModule X L (d : ℤ))
```

**`AlgebraicGeometry.isAmple_iff_tensorPower_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/TensorPower.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/TensorPower.lean#L589). References: EGA II (4.5.6), “(i)”.

> An invertible sheaf is ample if and only if any of its positive tensor
> powers is ample.

```lean
theorem isAmple_iff_tensorPower_isAmple (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (n : ℕ) (hn : 1 ≤ n) :
    Scheme.Modules.IsAmple X L ↔
    Scheme.Modules.IsAmple X
        (Invertible.tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L (n : ℤ))
```

## Tag 01PU, a lemma

[Tag 01PU](https://stacks.math.columbia.edu/tag/01PU) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isAmple_pullback_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePullback/Affine.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePullback/Affine.lean#L108). References: EGA II (4.5.14), “necessity”; EGA II (4.5.13), “necessity”; EGA III (2.6.2.3), “special case”; EGA III (5.2.5), “Ampleness of L'\_0 = L/JL”.

> **Stacks Project, Tag 01PU.** The restriction of an ample invertible sheaf of modules to a
> closed subscheme is ample. The closed immersion is affine, and its source is quasi-compact
> because its target is.

```lean
public theorem isAmple_pullback_of_isClosedImmersion [IsClosedImmersion f] (h : IsAmple Y L) :
    IsAmple X ((Scheme.Modules.pullback f).obj L)
```

## Tag 01PV, a lemma

[Tag 01PV](https://stacks.math.columbia.edu/tag/01PV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isAffineOpen_inf_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Basic.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Basic.lean#L325). References: EGA II (5.5.8); SGA 6 II (2.2.3.1).

> For an invertible module `L` on a scheme `X` and a global section `s` of `L`, every affine
> open `U ⊆ X` meets the nonvanishing locus `X_s` in an affine open.

```lean
public theorem isAffineOpen_inf_nonvanishingOpen {X : Scheme.{u}} (L : X.Modules)
    [Stacks.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (s : L.sections) (U : X.Opens) (hU : IsAffineOpen U) :
    IsAffineOpen (U ⊓ nonvanishingOpen (X := X.toRingedSpace) L s)
```

**`Stacks.NonvanishingAffineIntersection.isAffineOpen_inf_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NonvanishingAffineIntersection/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NonvanishingAffineIntersection/Basic.lean#L122). References: EGA II (5.5.8); SGA 6 II (2.2.3.1).

> Let `X` be a scheme, `M` an invertible `𝒪_X`-module and `s` a global section of `M`. For every
> affine open `U` of `X`, the intersection `U ∩ X_s` of `U` with the nonvanishing locus of `s` is
> affine.

```lean
theorem isAffineOpen_inf_nonvanishingOpen {U : X.Opens} (hU : IsAffineOpen U) :
    IsAffineOpen (U ⊓ Stacks.NonvanishingOpen.nonvanishingOpen X M s)
```

## Tag 0890, a lemma

[Tag 0890](https://stacks.math.columbia.edu/tag/0890) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isAmple_tensor_of_power_sections_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerProduct/Basic.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerProduct/Basic.lean#L213). References: EGA II (4.5.6), “(ii)”.

> **Stacks Project, Tag 0890.** Let `L` and `M` be invertible modules on a scheme `X`. If `L`
> is ample and the nonvanishing opens of the global sections of the positive tensor powers of `M`
> cover `X`, then `L ⊗ M` is ample.
>
> At a point `x`, ampleness of `L` gives `n ≥ 1` and `s ∈ Γ(X, L^{⊗ n})` with `x ∈ X_s` and `X_s`
> affine, and the cover gives `m ≥ 1` and `t ∈ Γ(X, M^{⊗ m})` with `x ∈ X_t`. The section
> `s^m ⊗ t^n` of `(L ⊗ M)^{⊗ nm}`, read through `tensorPowerProductIso`, has nonvanishing open
> `X_s ⊓ X_t`, which contains `x` and is affine by Tag 01PV.

```lean
theorem isAmple_tensor_of_power_sections_cover (X : Scheme.{u}) (L M : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property M]
    (hL : IsAmple X L)
    (hcover : ∀ x : X, ∃ m : ℕ, 1 ≤ m ∧
      ∃ t : (tensorPower X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property M (m : ℤ)).sections,
        x ∈ nonvanishingOpen (X := X.toRingedSpace)
          (tensorPower X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property M (m : ℤ)) t) :
    IsAmple X (tensorProductModule X L M)
```

## Tag 01PX, a lemma

[Tag 01PX](https://stacks.math.columbia.edu/tag/01PX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isBasis_affine_nonvanishingOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Basis.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Basis.lean#L59).

> **Stacks Project, Tag 01PX.** If the nonvanishing opens of global sections of the positive
> tensor powers of an invertible sheaf form a basis of the topology, then the affine ones among
> them already form a basis.

```lean
public theorem isBasis_affine_nonvanishingOpens
    (hBasis : Opens.IsBasis
      {U : X.Opens | ∃ n : ℕ, 1 ≤ n ∧
        ∃ s : (tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L (n : ℤ)).sections,
          U = nonvanishingOpen (X := X.toLocallyRingedSpace.toRingedSpace)
            (tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s}) :
    Opens.IsBasis
      {U : X.Opens | (∃ n : ℕ, 1 ≤ n ∧
        ∃ s : (tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L (n : ℤ)).sections,
          U = nonvanishingOpen (X := X.toLocallyRingedSpace.toRingedSpace)
            (tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s) ∧
          IsAffineOpen U}
```

## Tag 01PY, a lemma

[Tag 01PY](https://stacks.math.columbia.edu/tag/01PY) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isSeparated_of_affine_nonvanishingOpen_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Separated.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineNonvanishing/Separated.lean#L351).

> **Stacks Project, Tag 01PY.** A scheme carrying an invertible sheaf of modules such that
> every point lies in an *affine* nonvanishing open of a global section of some positive tensor
> power is separated.

```lean
public theorem isSeparated_of_affine_nonvanishingOpen_cover
    (h : ∀ x : X, ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : (tensorPower X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L (n : ℤ)).sections,
        x ∈ nonvanishingOpen (X := X.toLocallyRingedSpace.toRingedSpace)
          (tensorPower X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s ∧
        IsAffineOpen (nonvanishingOpen (X := X.toLocallyRingedSpace.toRingedSpace)
          (tensorPower X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s)) :
    Scheme.IsSeparated X
```

**`Stacks.AmpleNonvanishing.isSeparated_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/AmpleAffineDiagonal.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/AmpleAffineDiagonal.lean#L71). The attribute's comment: “at the predicate Stacks.Ample.IsAmple”.

> **A scheme carrying an ample invertible module is separated**, at the predicate
> `Stacks.Ample.IsAmple`. This is [Stacks, Tag 01PY], available as
> `AlgebraicGeometry.Scheme.Modules.IsAmple.isSeparated` for the other of the two ampleness
> predicates of [Stacks, Tag 01PS], transported along the hypothesis-free
> `Stacks.AmpleBridge.isAmple_iff_isAmple`.

```lean
theorem isSeparated_of_isAmple (X : Scheme.{u}) (L : X.Modules) [IsInvertibleModule X L]
    (hL : IsAmple X L) : Scheme.IsSeparated X
```

**`AlgebraicGeometry.isSeparated_of_exists_affine_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/Separated.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/Separated.lean#L295).

> A scheme is separated as soon as every point lies in an affine nonvanishing open of a global
> section of some positive tensor power of an invertible sheaf.

```lean
theorem isSeparated_of_exists_affine_nonvanishingOpen
    (h : ∀ x : X, ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : (Invertible.tensorPower X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L (n : ℤ)).sections,
        x ∈ nonvanishingOpen (X := X.toRingedSpace)
            (Invertible.tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s ∧
          IsAffineOpen (nonvanishingOpen (X := X.toRingedSpace)
            (Invertible.tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s)) :
    Scheme.IsSeparated X
```

## Tag 09MP, a lemma

[Tag 09MP](https://stacks.math.columbia.edu/tag/09MP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.IsAmple.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/Separated.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/Separated.lean#L342).

> **A scheme carrying an ample invertible sheaf is separated.**

```lean
theorem Scheme.Modules.IsAmple.isSeparated (hL : Scheme.Modules.IsAmple X L) :
    Scheme.IsSeparated X
```

## Tag 01PZ, a lemma

[Tag 01PZ](https://stacks.math.columbia.edu/tag/01PZ) in the Stacks Project.

**`Stacks.SectionRingProjMorphism.projHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean#L177).

> **The canonical morphism `⋃ X_a ⟶ Proj Γ_*(X, L)` of Stacks Tag 01PZ.** It is glued from the
> charts `Stacks.SectionRingChartMap.chartHom` over the cover of `⋃ X_a` by the nonvanishing opens
> of the homogeneous elements of positive degree; the overlap condition is
> `Stacks.SectionRingChartOpen.chartHomOn_eq`, which says that the chart at `a` and the chart at `b`
> agree on `X_a ∩ X_b`.
>
> For `L` ample the source is all of `X` (`Stacks.SectionRingProjMorphism.projHomOfIsAmple`); in
> general `⋃ X_a` is the largest open on which the construction makes sense, and that is where the
> Stacks project's statement puts it as well.

```lean
public noncomputable def projHom : (nvUnion L).toScheme ⟶ Proj (grading L)
```

**`Stacks.SectionRingProjMorphism.homOfLE_projHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean#L203). The attribute's comment: “the restriction to a nonvanishing open is the chart”.

> **On `X_a` the canonical morphism is the chart at `a`.** This is the second half of the
> characterisation of the morphism of Stacks Tag 01PZ, not one of the tag's numbered clauses. For
> `a` homogeneous of positive degree, the restriction of the canonical morphism to `X_a` is the
> morphism `X_a ⟶ Proj Γ_*(X, L)` determined by the degree-zero part of the localization of
> `Γ_*(X, L)` at `a`, namely `Stacks.SectionRingChartMap.chartHom`.

```lean
public theorem homOfLE_projHom {d : ℕ} (a : powSections L d) (hd : 0 < d) :
    X.homOfLE (nvOpen_le_nvUnion L a hd) ≫ projHom L
      = Stacks.SectionRingChartMap.chartHom L a hd
```

**`Stacks.SectionRingProjMorphism.projHom_preimage_projBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean#L216). The attribute's comment: “the preimage of a basic open”.

> **Clause (1) of Stacks Tag 01PZ: the preimage of a basic open.** For every homogeneous element
> `a` of `Γ_*(X, L)` of positive degree, the canonical morphism pulls the chart `D₊(a)` of
> `Proj Γ_*(X, L)` back to the nonvanishing open `X_a`.
>
> The identity is checked on the cover: on the piece `X_b` the composite is the chart at `b`, and
> `Stacks.SectionRingChartOpen.chartHomOn_preimage_projBasicOpen` computes its preimage of `D₊(a)`
> as `X_b ∩ X_a`, which is also what the right-hand side restricts to.

```lean
public theorem projHom_preimage_projBasicOpen {d : ℕ} (a : powSections L d) (hd : 0 < d) :
    projHom L ⁻¹ᵁ Proj.basicOpen (grading L) (DirectSum.of (powSections L) d a)
      = (nvUnion L).ι ⁻¹ᵁ nvOpen L a
```

**`Stacks.SectionRingProjMorphism.image_projHom_preimage_projBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Basic.lean#L231). The attribute's comment: “the preimage of a basic open, as an open of X”.

> **Clause (1) of Stacks Tag 01PZ, read as an open of `X`.** The image in `X` of the preimage of
> `D₊(a)` is the nonvanishing open `X_a` itself, which is the shape the Stacks project's statement
> takes.

```lean
public theorem image_projHom_preimage_projBasicOpen {d : ℕ} (a : powSections L d) (hd : 0 < d) :
    (nvUnion L).ι ''ᵁ
        (projHom L ⁻¹ᵁ Proj.basicOpen (grading L) (DirectSum.of (powSections L) d a))
      = nvOpen L a
```

**`Stacks.SectionRingProjMorphism.Theta.homOfLE_projHom_eq_glued`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L104). The attribute's comment: “the canonical morphism is the morphism r\_\{L,psi} of Tag 01NK at psi the identity map of the section ring, with no hypothesis on L; this is what the clauses below are clauses about”.

> **The canonical morphism `Stacks.SectionRingProjMorphism.projHom` is the morphism `r_{L, ψ}` of
> [Stacks, Tag 01NK] at `ψ` the identity map of `Γ_*(X, L)`**, with no hypothesis on `L`: the two
> morphisms have the same source `U(ψ) = ⋃_a X_a`
> (`Stacks.SectionRingGluedComparison.coveringOpen_canonicalSections`) and agree there.

```lean
theorem homOfLE_projHom_eq_glued :
    X.homOfLE (coveringOpen_canonicalSections L).le
        ≫ Stacks.SectionRingProjMorphism.projHom L
      = (canonicalSections L).glued
```

**`Stacks.SectionRingProjMorphism.Theta.glued_preimage_projBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L120). The attribute's comment: “clause (1): f^\{-1}(D\_+(s)) = X\_s for every homogeneous s in S\_+, for the morphism f = r\_\{L,psi} that clauses (2), (3) and (4) are stated at, as opens of its source U(psi)”.

> `f^{-1}(D₊(s)) = X_s` for every homogeneous `s ∈ S_+`, where `f` is `r_{L, ψ}` at `ψ` the
> identity map of `S = Γ_*(X, L)`. Both sides are opens of the source `U(ψ) = ⋃_a X_a` of `f`, the
> right-hand side being `X_s`, which lies inside it.

```lean
theorem glued_preimage_projBasicOpen {d : ℕ} (a : powSections L d) (hd : 0 < d) :
    (canonicalSections L).glued ⁻¹ᵁ
        AlgebraicGeometry.Proj.basicOpen (grading L) (DirectSum.of (powSections L) d a)
      = (canonicalSections L).coveringOpen.ι ⁻¹ᵁ nvOpen L a
```

**`Stacks.SectionRingProjMorphism.Theta.projTheta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L140). The attribute's comment: “clause (2): the O\_X-module maps f^*O\_Y(n) -> L^\{tensor n} for all n in Z, as a homomorphism of sheaves of Z-graded algebras, whose map\_mul is their compatibility with the multiplication maps of Constructions Equation 01MO”.

> **The `𝒪_X`-module maps `f^*𝒪_Y(n) ⟶ L^{⊗ n}`, compatible with the multiplication maps of
> Constructions, Equation 01MO.** All degrees at once, as a homomorphism of sheaves of `ℤ`-graded
> `𝒪_X`-algebras `f^*(⨁_{n ∈ ℤ} 𝒪_Y(n)) ⟶ ⨁_{n ∈ ℤ} L^{⊗ n}`: its component in degree `n` is the map
> `f^*𝒪_Y(n) ⟶ L^{⊗ n}`, and its `map_mul` field is exactly the compatibility, the multiplication
> maps of the two graded algebras being those of Equation 01MO on the source and the tensor product
> of sections on the target. It is `θ` of [Stacks, Tag 01NK] at `ψ` the identity map of `Γ_*(X, L)`,
> taken along `f = r_{L, ψ}`.

```lean
def projTheta : SheafOfModules.GradedAlgebra.Hom
    (Stacks.Conormal.gradedPullback (canonicalSections L).glued
      (Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebra (grading L)))
    (laurentRestrict (grading L) (canonicalSections L))
```

**`Stacks.SectionRingProjMorphism.Theta.projTheta_app_top_degreeSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/Theta.lean#L163). The attribute's comment: “clause (3): the composite S\_d -> Gamma(Y, O\_Y(d)) -> Gamma(X, L^\{tensor d}) is the identity map, read on the open where the canonical morphism is defined”.

> **The composite `S_d ⟶ Γ(Y, 𝒪_Y(d)) ⟶ Γ(X, L^{⊗ d})` is the identity map.** For a homogeneous
> element `z` of `S = Γ_*(X, L)` of degree `d`, the first map sends `z` to the global section of
> `𝒪_Y(d)` attached to it by [Stacks, Tag 01MP], the second pulls that back along `f` and applies the
> degree-`d` component of `projTheta`, and the result is `z` itself: the global section of `L^{⊗ d}`
> that the degree-`d` component `z d` of `z` names.
>
> Both sides are sections of `L^{⊗ d}` over `⋃_a X_a`, where `f` is defined, with `L^{⊗ d}` read in
> the family `Stacks.AmpleProjectiveImmersion.tensorPowerModule` and compared with the iterated
> tensor power by `Stacks.AlgebraicGeometry.CoherentMulSections.powCompare`.

```lean
theorem projTheta_app_top_degreeSection (d : ℕ) {z : sectionRing L} (hz : z ∈ grading L d) :
    ((projTheta L).app (d : ℤ)).val.app (op ⊤)
        (Scheme.Modules.pullbackSection (canonicalSections L).glued
          (twistM (grading L) (d : ℤ)) ⊤ ⊤ (fun _ _ => trivial)
          (degreeSection (grading L) d ⟨z, hz⟩))
      = resTop (tensorPowerModule X L (d : ℤ))
          ((powCompare L d).hom.app ⊤ (globalSection X (natTensorPow L d) (z d)))
          ((canonicalSections L).coveringOpen.ι ''ᵁ ⊤)
```

**`Stacks.SectionRingProjMorphism.Theta.exists_isIso_pullback_projTheta_app_intMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/ThetaIso.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjMorphism/ThetaIso.lean#L484). The attribute's comment: “clause (4): every point of the open where the canonical morphism is defined has an integer d >= 1 and an open neighbourhood U of it on which f^*O\_Y(dn) -> L^\{tensor dn} is an isomorphism for all n in Z, positive, zero and negative; d is the degree of a homogeneous element of the section ring not vanishing at the point and U is the nonvanishing open of that element”.

> Every point of `⋃_a X_a` has an integer `d ≥ 1` and an open neighbourhood `U` on which
> `f^*𝒪_Y(d n)|_U ⟶ L^{⊗ d n}|_U` is an isomorphism **for all `n ∈ ℤ`**.

```lean
theorem exists_isIso_pullback_projTheta_app_intMul {x : X}
    (hx : x ∈ (canonicalSections L).coveringOpen) :
    ∃ (e : ℕ) (_ : 0 < e) (V : X.Opens) (_ : x ∈ V) (hVU : V ≤ (canonicalSections L).coveringOpen),
      ∀ n : ℤ,
        IsIso ((Scheme.Modules.pullback (X.homOfLE hVU)).map
          ((projTheta L).app ((e : ℤ) * n)))
```

## Tag 01Q0, a lemma

[Tag 01Q0](https://stacks.math.columbia.edu/tag/01Q0) in the Stacks Project.

**`Stacks.SectionRingProjQuasiCompact.quasiCompact_projHomOfCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjQuasiCompact/Basic.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjQuasiCompact/Basic.lean#L220). The attribute's comment: “the canonical morphism of 01PZ is quasi-compact, under (a) the X\_s cover X and (b) X quasi-compact”.

> **Stacks Tag 01Q0, the quasi-compactness.** Under clause (a) of Stacks Tag 01PZ — the `X_s`
> cover `X` — and `X` quasi-compact, the canonical morphism `f : X ⟶ Proj Γ_*(X, L)` of Stacks Tag
> 01PZ is quasi-compact.
>
> `Proj` of any graded ring is quasi-separated
> (`Stacks.AlgebraicGeometry.ProjQuasiSeparated.quasiSeparatedSpace_proj`), so this is
> `AlgebraicGeometry.quasiCompact_of_compactSpace`, which is Stacks Tag 01KO.

```lean
theorem quasiCompact_projHomOfCovers [CompactSpace X]
    (hcov : Stacks.SectionRingProjMorphism.nvUnion L = ⊤) :
    QuasiCompact (Stacks.SectionRingProjMorphism.projHomOfCovers L hcov)
```

**`Stacks.SectionRingProjQuasiCompact.denseRange_projHomOfCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjQuasiCompact/Basic.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjQuasiCompact/Basic.lean#L233). The attribute's comment: “the canonical morphism of 01PZ has dense image, under (a) the X\_s cover X and (b) X quasi-compact”.

> **Stacks Tag 01Q0, the dense image.** Under clause (a) of Stacks Tag 01PZ — the `X_s` cover
> `X` — and `X` quasi-compact, the canonical morphism `f : X ⟶ Proj Γ_*(X, L)` of Stacks Tag 01PZ
> has dense image.
>
> A nonempty open of `Proj Γ_*(X, L)` missing the image would contain a nonempty `D₊(a)` with `a`
> homogeneous of positive degree, whose preimage `X_a` would then be empty; but then `a` is
> nilpotent and `D₊(a) = ∅`.

```lean
theorem denseRange_projHomOfCovers [CompactSpace X]
    (hcov : Stacks.SectionRingProjMorphism.nvUnion L = ⊤) :
    DenseRange (Stacks.SectionRingProjMorphism.projHomOfCovers L hcov).base
```

## Tag 01Q1, a lemma

[Tag 01Q1](https://stacks.math.columbia.edu/tag/01Q1) in the Stacks Project.

**`Stacks.SectionRingProjImmersion.isOpenImmersion_projHomOfIsAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjImmersion/Basic.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjImmersion/Basic.lean#L141). The attribute's comment: “open immersion”. References: EGA II (4.5.2), “partial”.

> **Stacks Tag 01Q1, the open immersion.** For `L` an ample invertible `𝒪_X`-module, the
> canonical morphism `X ⟶ Proj Γ_*(X, L)` of Stacks Tag 01PZ is an open immersion.

```lean
theorem isOpenImmersion_projHomOfIsAmple (hL : IsAmple X L) :
    IsOpenImmersion (Stacks.SectionRingProjMorphism.projHomOfIsAmple L hL)
```

**`Stacks.SectionRingProjImmersion.denseRange_projHomOfIsAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjImmersion/Basic.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjImmersion/Basic.lean#L166). The attribute's comment: “dense image”.

> **Stacks Tag 01Q1, the dense image.** For `L` an ample invertible `𝒪_X`-module, the canonical
> morphism `X ⟶ Proj Γ_*(X, L)` of Stacks Tag 01PZ has dense image.
>
> This is Stacks Tag 01Q0 (`Stacks.SectionRingProjQuasiCompact.denseRange_projHomOfCovers`), which
> the source cites here: ampleness gives both of that tag's hypotheses, that the `X_s` cover `X`
> (`Stacks.SectionRingProjMorphism.nvUnion_eq_top_of_isAmple`) and that `X` is quasi-compact.

```lean
theorem denseRange_projHomOfIsAmple (hL : IsAmple X L) :
    DenseRange (Stacks.SectionRingProjMorphism.projHomOfIsAmple L hL).base
```

## Tag 01Q2, a lemma

[Tag 01Q2](https://stacks.math.columbia.edu/tag/01Q2) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjAmpleTwist.exists_isAmple_pullback_twistingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleProjOpenImmersion.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleProjOpenImmersion.lean#L208). References: EGA II (8.14.4), “invertible for some d”.

> **Stacks Project, Tag 01Q2.** Let `X` be a quasi-compact scheme and `S` a graded ring, and
> assume there is an open immersion `j : X ⟶ Proj(S)`. Then `j^* 𝒪(d)` is an invertible ample
> `𝒪_X`-module for some `d > 0`.

```lean
theorem exists_isAmple_pullback_twistingSheaf {X : Scheme.{u}} [CompactSpace X]
    (j : X ⟶ AlgebraicGeometry.Proj 𝒮) [IsOpenImmersion j] :
    ∃ d : ℕ, 0 < d ∧ ∃ h : IsInvertibleModule X
        ((modulePullback j.toLRSHom.toShHom).obj (twistingSheaf 𝒮 (d : ℤ))),
      @IsAmple X ((modulePullback j.toLRSHom.toShHom).obj (twistingSheaf 𝒮 (d : ℤ))) h
```

## Tag 01Q3, a proposition

[Tag 01Q3](https://stacks.math.columbia.edu/tag/01Q3) in the Stacks Project.

**`Stacks.AmpleCharacterization.exists_nvUnion_eq_top_and_isOpenImmersion_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean#L129). The attribute's comment: “clause (2)”. References: EGA II (4.5.2), “(a) ⇒ (a'')”.

> **Clause (2) of [Stacks, Tag 01Q3]** — the clause labelled 01Q5: for `L` ample the open sets
> `X_s`, with `s ∈ S₊` homogeneous, cover `X`, and the associated morphism `X ⟶ Proj S` is an open
> immersion.
>
> The covering is `Stacks.SectionRingProjMorphism.nvUnion_eq_top_of_isAmple`; it is also what makes
> the morphism `Stacks.SectionRingProjMorphism.projHomOfCovers` of Stacks Tag 01PZ exist at all. The
> open immersion is Stacks Tag 01Q1,
> `Stacks.SectionRingProjImmersion.isOpenImmersion_projHomOfIsAmple`.

```lean
theorem exists_nvUnion_eq_top_and_isOpenImmersion_of_isAmple (hL : IsAmple X L) :
    ∃ h : Stacks.SectionRingProjMorphism.nvUnion L = ⊤,
      IsOpenImmersion (Stacks.SectionRingProjMorphism.projHomOfCovers L h)
```

**`Stacks.AmpleCharacterization.isAmple_of_isOpenImmersion_projHomOfCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean#L145). The attribute's comment: “clause (2) implies (1)”. References: EGA II (4.5.2), “(a) ⇐ (a'')”.

> **Clause (2) of [Stacks, Tag 01Q3] implies clause (1).** If the opens `X_s` cover the
> quasi-compact scheme `X` and the resulting morphism `j : X ⟶ Proj Γ_*(X, L)` is an open immersion,
> then `L` is ample.
>
> This is the source's implication `(2) ⇒ (4) ⇒ (1)` in one step: the basic opens `D₊(a)` of the
> homogeneous elements of positive degree are a basis of `Proj S` and are affine, so every point of
> `X` has one of them around its image inside the (open) range of `j`; its preimage is `X_a`, is
> affine because `j` is an open immersion, and contains the point. That is clause (1) of Stacks
> Tag 01PS verbatim.

```lean
theorem isAmple_of_isOpenImmersion_projHomOfCovers [CompactSpace X]
    (h : Stacks.SectionRingProjMorphism.nvUnion L = ⊤)
    (hj : IsOpenImmersion (Stacks.SectionRingProjMorphism.projHomOfCovers L h)) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.isAmple_of_isBasisNonvanishing_and_isBasisAffineNonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean#L188). The attribute's comment: “(3) and (4) imply (1)”. References: EGA II (4.5.2), “(a) ⇐ (a')”.

> **Clauses (3) and (4) of [Stacks, Tag 01Q3] imply clause (1)** — the converse of
> `Stacks.SheafOfModules.Invertible.exists_sections_mem_nonvanishingOpen_le_of_isAmple`, which is the
> implication `(1) ⇒ (3) ∧ (4)`.
>
> Either clause alone suffices on a quasi-compact scheme: clause (4) applied at the ambient open `⊤`
> is condition (2) of Stacks Tag 01PS, and clause (3) yields clause (4) by Stacks Tag 01PX, which is
> unconditional here because Tag 01PV is proved. Both are stated so that the conjunction the forward
> implication produces can be fed back verbatim.

```lean
theorem isAmple_of_isBasisNonvanishing_and_isBasisAffineNonvanishing [CompactSpace X]
    (h : Stacks.AmpleTheory.IsBasisNonvanishing X L ∧
      Stacks.AmpleTheory.IsBasisAffineNonvanishing X L) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.isAmple_of_isBasisNonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean#L232). The attribute's comment: “clause (3) implies (1)”. References: EGA II (4.5.2), “(a) ⇐ (a')”; EGA II (5.1.2), “d) ⇒ c')”; SGA 6 II (2.2.3), “(i) ⇒ (ii)”; SGA 6 II (2.2.4), “partial”.

> **Clause (3) of [Stacks, Tag 01Q3] implies clause (1)**, from clause (3) alone: on a
> quasi-compact scheme, an invertible `L` whose nonvanishing opens `X_s` — for `s` a global section
> of a positive tensor power of `L` — form a basis for the topology is ample.
>
> This is the implication the conjunction above does not give, since that one consumes only its
> clause (4) conjunct. Stacks Tag 01PX supplies the step clause (3) ⇒ clause (4): the affine opens
> are themselves a basis, so the prescribed open may be shrunk to an affine one before clause (3) is
> applied, and the resulting `X_s`, sitting inside an affine open, is affine by Stacks Tag 01PV.
> Clause (4) at the ambient open `⊤` is then condition (2) of Stacks Tag 01PS.
>
> The implication was already proved, as the `mpr` of
> `Stacks.SectionExtension.isAmple_iff_compactSpace_and_isBasisNonvanishing`, and that is what is
> invoked here rather than a second derivation; what this declaration adds is the standalone
> statement of the clause, and its registration, beside the other clauses of the tag. Tag 01PX is
> likewise already proved and registered — as
> `AlgebraicGeometry.Scheme.Modules.isBasis_affine_nonvanishingOpens`, in the Tag 01PS vocabulary —
> and in the vocabulary these clauses are stated in it is
> `Stacks.NonvanishingAffineIntersection.isBasisAffineNonvanishing_of_isBasisNonvanishing`, which
> carries no hypothesis beyond invertibility because Tag 01PV is proved
> (`AlgebraicGeometry.Scheme.Modules.isAffineOpen_inf_nonvanishingOpen`).
>
> The hypotheses are exactly clause (3) and the quasi-compactness standing over the whole source
> Proposition; nothing is assumed about affineness of the `X_s`, which is precisely what clause (3)
> as the tag states it leaves out.

```lean
theorem isAmple_of_isBasisNonvanishing [CompactSpace X]
    (h : Stacks.AmpleTheory.IsBasisNonvanishing X L) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_ideal_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/Basic.lean#L271). The attribute's comment: “clause (9)”. References: EGA II (2.7.10), “ideals”; EGA II (4.5.5), “(a) ⇒ (d'), ideals”.

> **Clause (9) of [Stacks, Tag 01Q3]** — the clause labelled 01QC: `X` is quasi-separated, and
> every sheaf of ideals of finite type on `X` is a quotient of a direct sum of `k` copies of
> `L ^⊗ (-n)` for some `n > 0` and `k ≥ 0`.
>
> A sheaf of ideals is presented as a module `J` together with a monomorphism `J ⟶ 𝒪_X`, which is
> what "sheaf of ideals" means; `k` is the cardinality of the finite index type `ι`, a direct sum
> over a finite index type being a direct sum of `Nat.card ι` copies.
>
> The clause is read with its ideals **quasi-coherent**, as clause (6) of the source states them
> explicitly, and this is forced rather than chosen: a quotient of a direct sum of quasi-coherent
> modules is quasi-coherent, so the clause would be false for a sheaf of ideals that is not. It is
> also what makes the source's "the implication (8) ⇒ (9) is trivial" true, and it is the generality
> in which clause (8) is registered
> (`Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_exists_epi_biproduct_of_isAmple`).
>
> The proof is exactly the source's: clause (9) is clause (8) with its quantifier restricted, so
> clause (8) applied to `J` is the whole content.

```lean
theorem quasiSeparatedSpace_and_exists_epi_biproduct_ideal_of_isAmple (hL : IsAmple X L) :
    QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
      J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : CategoryTheory.Limits.Bicone fun _ : ι => tensorPowModule X L (-n))
            (_ : b.IsBilimit) (p : b.pt ⟶ J), CategoryTheory.Epi p
```

**`Stacks.AmpleCharacterization.iSup_range_twistHom_eq_top_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseFive.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseFive.lean#L289). The attribute's comment: “clause (5)”. References: EGA II (4.5.5), “(a) ⇒ (b)”.

> **Clause (5) of [Stacks, Tag 01Q3]** — the clause labelled 01Q8: for every quasi-coherent
> sheaf `F` on `X` the sum of the images of the canonical maps
> `Γ(X, F ⊗ L^{⊗ n}) ⊗_𝐙 L^{⊗ -n} ⟶ F`, over `n ≥ 1`, equals `F`.
>
> The `n`-th canonical map is the sum over `m ∈ Γ(X, F ⊗ L^{⊗ n})` of the maps
> `Stacks.AmpleCharacterization.twistHom L F n m`, a tensor product over `𝐙` with a free abelian
> group being the direct sum; so the sum of the images of the canonical maps is the sum of the
> images of the `twistHom L F n m`, which is what is written.
>
> **The equality of subsheaves is read on stalks**, as `Stacks.AmpleLocalGeneration.IsFinGenOn` and
> every other generation statement in this repository is. For sheaves of modules the two readings
> agree: the stalk functor is exact and commutes with the filtered colimit defining a sum of
> subsheaves, and a submodule of `F` whose stalks are all of `F` is `F`. What is proved is in fact
> stronger than the clause and is what the source's proof gives — every germ lies in the image of a
> *single* one of the maps, by `Stacks.AmpleCharacterization.exists_mem_range_twistHom`.

```lean
theorem iSup_range_twistHom_eq_top_of_isAmple (hL : IsAmple X L) :
    ∀ F : X.Modules, F.IsQuasicoherent → ∀ x : X,
      (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(F ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L F (n : ℤ) m) x)) = ⊤
```

**`Stacks.AmpleCharacterization.iSup_range_twistHom_ideal_eq_top_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseFive.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseFive.lean#L308). The attribute's comment: “clause (6)”. References: EGA II (4.5.5), “(a) ⇒ (b), ideals”.

> **Clause (6) of [Stacks, Tag 01Q3]** — the clause labelled 01Q9: clause (5) with `F` ranging
> over the quasi-coherent sheaves of ideals of `X`.
>
> A sheaf of ideals is a module `J` with a monomorphism into `𝒪_X`. The clause is clause (5) with
> its quantifier restricted, which is why the source proves it by the single word "clearly"; the
> restriction is recorded here rather than left implicit because clauses (6) and (9) are the two
> the source's cycle re-enters ampleness through.

```lean
theorem iSup_range_twistHom_ideal_eq_top_of_isAmple (hL : IsAmple X L) :
    ∀ (J : X.Modules) (j : J ⟶ Stacks.Ample.unitModule X), Mono j → J.IsQuasicoherent →
      ∀ x : X, (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(J ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L J (n : ℤ) m) x)) = ⊤
```

**`Stacks.AmpleCharacterization.iSup_range_twistHom_ideal_eq_top_of_exists_epi_biproduct_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseNineDirect.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseNineDirect.lean#L167). The attribute's comment: “clause (9) implies (6)”.

> **Clause (9) of [Stacks, Tag 01Q3] implies clause (6)**, by the source's own argument through
> [Stacks, Tag 01PG] rather than through ampleness.
>
> Given a quasi-coherent sheaf of ideals `j : ℐ ⟶ 𝒪_X`, a point `x` and a germ `u ∈ ℐ_x`: the germ
> comes from a section of `ℐ` over an affine open `V ∋ x`, and Tag 01PG in the form
> `AlgebraicGeometry.exists_finiteTypeQuasicoherentSubobject_section` — where quasi-separatedness
> is used — puts that section inside a quasi-coherent subobject `G ⊆ ℐ` of finite type. Then
> `G.arrow ≫ j` is a monomorphism, so clause (9) applies to `G` and writes it as a quotient of a
> finite direct sum of copies of `L ^⊗ (-n)` with `n > 0`; the germ of `G` decomposes as a finite
> sum of germs from the summands (`Stacks.ModuleBicone.exists_germ_sum_of_epi`), and pushing the
> decomposition forward along `G.arrow` writes `u` as a finite sum of images of morphisms
> `L ^⊗ (-n) ⟶ ℐ`, each of which is one of the maps of clause (6) by
> `Stacks.AmpleCharacterization.exists_twistHom_eq`.
>
> The other proof of this implication, `Stacks.AmpleCharacterization`
> `.iSup_range_twistHom_ideal_eq_top_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal`, goes
> `(9) ⇒ (1) ⇒ (6)` instead; both are kept, as the tag's implication and as the route the
> nine-clause equivalence was first closed along.

```lean
theorem iSup_range_twistHom_ideal_eq_top_of_exists_epi_biproduct_ideal [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
      J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ J), Epi p) :
    ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j → J.IsQuasicoherent →
      ∀ x : X, (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(J ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L J (n : ℤ) m) x)) = ⊤
```

**`Stacks.AmpleCharacterization.isAmple_of_iSup_range_twistHom_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L445). The attribute's comment: “clause (6) implies (1)”. References: EGA II (4.5.5), “(b) ⇒ (a), ideals”.

> **Clause (6) of [Stacks, Tag 01Q3] implies clause (1)** — the implication the source's cycle
> re-enters ampleness through. If for every quasi-coherent sheaf of ideals of the quasi-compact
> scheme `X` the sum of the images of the canonical maps
> `Γ(X, ℐ ⊗ L^{⊗ n}) ⊗_𝐙 L^{⊗ -n} ⟶ ℐ`, `n ≥ 1`, is all of `ℐ`, then `L` is ample.
>
> This is the source's argument verbatim. Given `x`, choose an affine open `U ∋ x` and apply the
> hypothesis to the quasi-coherent sheaf of ideals `Stacks.ComplementIdeal.sheaf` of the reduced
> closed subscheme on `X ∖ U` (Schemes, Section 01IZ, i.e. [Stacks, Tag 01J3]). Its stalk at `x`
> contains the germ of `1`, so some single map `L ^⊗ (-n) ⟶ ℐ` composed with the inclusion
> `ℐ ⟶ 𝒪_X` has image at `x` outside `𝔪_x`. That composite is multiplication by a global section
> `s` of `L ^⊗ n` (`Stacks.AmpleCharacterization.exists_twistUnitHom_eq`); `s` does not vanish at
> `x`, and it vanishes along `X ∖ U` because the composite factors through `ℐ`, so `X_s ⊆ U` and
> `X_s` is affine by [Stacks, Tag 01PV].

```lean
theorem isAmple_of_iSup_range_twistHom_ideal [CompactSpace X]
    (h : ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j → J.IsQuasicoherent →
      ∀ x : X, (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(J ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L J (n : ℤ) m) x)) = ⊤) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.isAmple_of_iSup_range_twistHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L489). The attribute's comment: “clause (5) implies (1)”. References: EGA II (4.5.5), “(b) ⇒ (a)”.

> **Clause (5) of [Stacks, Tag 01Q3] implies clause (1)**: clause (5) is clause (6) with its
> quantifier widened from the quasi-coherent sheaves of ideals to all quasi-coherent sheaves, so
> this is `Stacks.AmpleCharacterization.isAmple_of_iSup_range_twistHom_ideal` with the hypothesis
> restricted.

```lean
theorem isAmple_of_iSup_range_twistHom [CompactSpace X]
    (h : ∀ F : X.Modules, F.IsQuasicoherent → ∀ x : X,
      (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(F ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L F (n : ℤ) m) x)) = ⊤) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L532). The attribute's comment: “clause (7) implies (8)”. References: EGA II (2.7.10), “(d) ⇒ (d')”.

> **Clause (7) of [Stacks, Tag 01Q3] implies clause (8), at clause (7)'s own strength.** The
> clause asks only that `F ⊗ L ^⊗ n` be *globally generated* for every `n ≥ n₀` — generated by
> *some* family of global sections, [Stacks, Tag 03DE] (3), with no finiteness demanded of that
> family — and that is the hypothesis carried here. The quasi-compactness of `X` is the standing
> hypothesis of the tag and nothing else is added.
>
> The finiteness clause (8) asks for is supplied by that quasi-compactness, which is where the
> source puts it too. `F ⊗ L ^⊗ n` is of finite type (`isFiniteType_tensor`: `F` is of finite type
> by the clause's own hypothesis and `L ^⊗ n` is of finite type, being invertible), and on a
> quasi-compact scheme a module of finite type generated by global sections is generated by
> finitely many of them — Modules, Lemma 17.9.7 ([Stacks, Tag 01BB]), available as
> `Stacks.AmpleEventualGeneration.isFinGen_of_generatingSections`. From there the step is the one
> `Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_exists_epi_biproduct_of_isAmple` runs: a
> finite family of global sections generating `F ⊗ L ^⊗ n` for one `n ≥ 1` is exactly an
> epimorphism onto `F` from a finite direct sum of copies of `L ^⊗ (-n)`, by
> `Stacks.AmpleGlobalGeneration.exists_epi_biproduct_of_epi_free`.

```lean
theorem quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections
    [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
          _root_.SheafOfModules.IsGeneratedByGlobalSections.{u, u, u}
            ((F ⊗ tensorPowModule X L n : X.Modules))) :
    QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ F), Epi p
```

**`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_of_isEventuallyGloballyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L570). The attribute's comment: “clause (7) implies (8), under the strengthened hypothesis that the twists are generated by finitely many global sections; the tag's own implication is `quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections` above”. References: EGA II (2.7.10), “(d) ⇒ (d')”.

> **Clause (7) of [Stacks, Tag 01Q3] implies clause (8)**, from the *strengthened* hypothesis
> that the twists are generated by **finitely many** global sections — which is more than clause
> (7) says, and so is not the tag's implication; that one is
> `quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections` above, and it is
> what the equivalences below rest on. This variant is kept because it needs no quasi-compactness:
> it is the proof
> `Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_exists_epi_biproduct_of_isAmple` runs with
> ampleness replaced by the strengthened clause, a finite family of global sections generating
> `F ⊗ L ^⊗ n` for one `n ≥ 1` being exactly an epimorphism onto `F` from a finite direct sum of
> copies of `L ^⊗ (-n)`, by
> `Stacks.AmpleGlobalGeneration.exists_epi_biproduct_of_epi_free`.

```lean
theorem quasiSeparatedSpace_and_exists_epi_biproduct_of_isEventuallyGloballyGenerated
    (h : QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
          ∃ σ : (F ⊗ tensorPowModule X L n).GeneratingSections, Finite σ.I) :
    QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ F), Epi p
```

**`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_ideal_of_exists_epi_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L591). The attribute's comment: “clause (8) implies (9)”. References: EGA II (2.7.10), “(d'), ideals”.

> **Clause (8) of [Stacks, Tag 01Q3] implies clause (9)**, the source's "trivial" step: clause
> (9) is clause (8) with its quantifier restricted to the sheaves of ideals.

```lean
theorem quasiSeparatedSpace_and_exists_epi_biproduct_ideal_of_exists_epi_biproduct
    (h : QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ F), Epi p) :
    QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
      J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ J), Epi p
```

**`Stacks.AmpleCharacterization.isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L630). The attribute's comment: “clause (9) implies (1)”. References: EGA II (2.7.10), “(d') ⇒ (a), ideals”; EGA II (4.5.5), “(d') ⇒ (a), ideals”.

> **Clause (9) of [Stacks, Tag 01Q3] implies clause (1)** — the step the source's second cycle
> re-enters ampleness through, and with the two implications above the last link of the
> nine-clause equivalence.
>
> The argument is the source's, with [Stacks, Tag 01PG] where the source puts it. Fix `x`, choose
> an affine open `U ∋ x` and let `Z = X ∖ U` with its reduced closed subscheme structure. Its
> sheaf of ideals `ℐ_Z` is the unit ideal on some affine open `V ∋ x`, so Tag 01PG — in its
> ideal-sheaf form `Stacks.IdealSheaf.exists_fg_le_of_mem`, which is what quasi-separatedness is
> used for — produces a quasi-coherent sheaf of ideals `ℐ ⊆ ℐ_Z`, finitely generated on every
> affine open and still containing the unit section over `V`. Being finitely generated affine-
> locally it is of finite type (`Stacks.IdealSheafModules.isFiniteType_sheaf`), so clause (9)
> applies to it: `ℐ` is a quotient of a finite direct sum of copies of `L ^⊗ (-n)` with `n > 0`.
>
> The germ at `x` of that unit section is not in `𝔪_x · (𝒪_X)_x`, and
> `Stacks.ModuleBicone.exists_germ_sum_of_epi` writes it as a finite sum of germs coming from the
> summands; since `𝔪_x · (𝒪_X)_x` is a submodule, one summand `i` already escapes it. Its
> composite `L ^⊗ (-n) ⟶ ℐ ⟶ 𝒪_X` is multiplication by a global section `σ` of `L ^⊗ n`
> (`Stacks.AmpleCharacterization.exists_twistUnitHom_eq`), and from here the argument is the one
> `Stacks.AmpleCharacterization.isAmple_of_iSup_range_twistHom_ideal` runs: `σ` does not vanish at
> `x`, and it vanishes at every point of `Z` — which is in the support of `ℐ` because `ℐ ⊆ ℐ_Z` —
> so `X_σ ⊆ U` and `X_σ` is affine by [Stacks, Tag 01PV].

```lean
theorem isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
      J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ J), Epi p) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.iSup_range_twistHom_ideal_eq_top_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/ClauseSixConverse.lean#L702). The attribute's comment: “clause (9) implies (6)”. References: EGA II (4.5.5), “(d') ⇒ (b), ideals”.

> **Clause (9) of [Stacks, Tag 01Q3] implies clause (6)**, the implication the source's cycle
> runs through. It is clause (9) implies clause (1)
> (`Stacks.AmpleCharacterization.isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal`)
> followed by clause (6) from ampleness, rather than the source's direct argument; the ingredient
> the source uses for the direct route, [Stacks, Tag 01PG], is the ingredient used there.

```lean
theorem iSup_range_twistHom_ideal_eq_top_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal
    [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
      J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ J), Epi p) :
    ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j → J.IsQuasicoherent →
      ∀ x : X, (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(J ⊗ tensorPowModule X L (n : ℤ), ⊤)),
        LinearMap.range (Stacks.ModuleStalk.map (twistHom L J (n : ℤ) m) x)) = ⊤
```

**`Stacks.AmpleCharacterization.isBasisNonvanishing_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L123). The attribute's comment: “clause (3)”. References: EGA II (4.5.2), “(a) ⇒ (a')”.

> **Clause (1) of [Stacks, Tag 01Q3] implies clause (3)** — the clause labelled 01Q6: for `L`
> ample the opens `X_s`, with `s ∈ S₊` homogeneous, form a basis for the topology of `X`.
>
> The clause is written out rather than named, and in the `Stacks.Ample.IsAmple` vocabulary the
> other eight clauses of the tag are stated in. The content is
> `Stacks.SectionExtension.isBasisNonvanishing_of_isAmple`.

```lean
theorem isBasisNonvanishing_of_isAmple (hL : IsAmple X L) :
    ∀ (x : X) (U : X.Opens), x ∈ U → ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : Γ(tensorPowModule X L (n : ℤ), ⊤),
        x ∈ powNonvanishingOpen X L n s ∧ powNonvanishingOpen X L n s ≤ U
```

**`Stacks.AmpleCharacterization.isBasisAffineNonvanishing_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L137). The attribute's comment: “clause (4)”. References: EGA II (4.5.2), “(a) ⇒ (a')”.

> **Clause (1) of [Stacks, Tag 01Q3] implies clause (4)** — the clause labelled 01Q7: for `L`
> ample the opens `X_s`, with `s ∈ S₊` homogeneous, **which are affine** form a basis for the
> topology of `X`.
>
> The content is `Stacks.SectionExtension.isBasisAffineNonvanishing_of_isAmple`, namely clause (3)
> followed by [Stacks, Tag 01PX], which is unconditional here because [Stacks, Tag 01PV] is
> proved.

```lean
theorem isBasisAffineNonvanishing_of_isAmple (hL : IsAmple X L) :
    ∀ (x : X) (U : X.Opens), x ∈ U → ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : Γ(tensorPowModule X L (n : ℤ), ⊤),
        IsAffineOpen (powNonvanishingOpen X L n s) ∧
          x ∈ powNonvanishingOpen X L n s ∧ powNonvanishingOpen X L n s ≤ U
```

**`Stacks.AmpleCharacterization.isAmple_of_isBasisAffineNonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L156). The attribute's comment: “clause (4) implies (1)”. References: EGA II (4.5.2), “(a) ⇐ (a')”.

> **Clause (4) of [Stacks, Tag 01Q3] implies clause (1)**, with clause (4) as the tag states it
> and nothing else beyond the standing quasi-compactness: if the affine opens `X_s`, for `s ∈ S₊`
> homogeneous, form a basis for the topology of the quasi-compact scheme `X`, then `L` is ample.
>
> `Stacks.AmpleCharacterization.isAmple_of_isBasisNonvanishing_and_isBasisAffineNonvanishing` proves
> the same conclusion from the *conjunction* of clauses (3) and (4), which is more than this clause
> supplies; the clause's own strength suffices, because clause (4) applied at the ambient open `⊤` is
> already condition (2) of [Stacks, Tag 01PS]. That is
> `Stacks.AmpleTheory.isAmple_of_isBasisAffineNonvanishing`.

```lean
theorem isAmple_of_isBasisAffineNonvanishing [CompactSpace X]
    (h : ∀ (x : X) (U : X.Opens), x ∈ U → ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : Γ(tensorPowModule X L (n : ℤ), ⊤),
        IsAffineOpen (powNonvanishingOpen X L n s) ∧
          x ∈ powNonvanishingOpen X L n s ∧ powNonvanishingOpen X L n s ≤ U) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_isGeneratedByGlobalSections_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L178). The attribute's comment: “clause (7)”. References: EGA II (4.5.5), “(a) ⇒ (d)”; EGA II (2.7.9).

> **Clause (1) of [Stacks, Tag 01Q3] implies clause (7)** — the clause labelled 01QA — *as the
> tag states it*: `X` is quasi-separated, and for every quasi-coherent sheaf `F` of finite type there
> is an `n₀` with `F ⊗ L ^⊗ n` globally generated, [Stacks, Tag 03DE] (3), for all `n ≥ n₀`. Nothing
> is asked of the generating family.
>
> `Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_isEventuallyGloballyGenerated_of_isAmple`
> concludes the stronger statement that the generating family may be taken **finite**, which is more
> than the clause says; this is the clause itself, and it is the form the equivalence below and the
> implication `(7) ⇒ (8)` of
> `Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections`
> are stated at.

```lean
theorem quasiSeparatedSpace_and_isGeneratedByGlobalSections_of_isAmple (hL : IsAmple X L) :
    QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
          _root_.SheafOfModules.IsGeneratedByGlobalSections.{u, u, u}
            ((F ⊗ tensorPowModule X L n : X.Modules))
```

**`Stacks.AmpleCharacterization.isAmple_of_quasiSeparatedSpace_and_isGeneratedByGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L196). The attribute's comment: “clause (7) implies (1)”. References: EGA II (4.5.5), “(d) ⇒ (a)”.

> **Clause (7) of [Stacks, Tag 01Q3] implies clause (1)**, from clause (7) at its own strength —
> the twists merely globally generated, with no bound on the generating family — and with no
> hypothesis beyond the tag's standing quasi-compactness.
>
> The route is the source's own: clause (7) implies clause (8)
> (`Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_of_isGeneratedByGlobalSections`,
> where the quasi-compactness cuts the generating family down to a finite one by
> [Stacks, Tag 01BB]), clause (8) implies clause (9), and clause (9) implies clause (1).

```lean
theorem isAmple_of_quasiSeparatedSpace_and_isGeneratedByGlobalSections [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
          _root_.SheafOfModules.IsGeneratedByGlobalSections.{u, u, u}
            ((F ⊗ tensorPowModule X L n : X.Modules))) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L212). The attribute's comment: “clause (8) implies (1)”. References: EGA II (4.5.5), “(d') ⇒ (a)”.

> **Clause (8) of [Stacks, Tag 01Q3] implies clause (1)**: the source's `(8) ⇒ (9) ⇒ (1)` in one
> step, `Stacks.AmpleCharacterization.quasiSeparatedSpace_and_exists_epi_biproduct_ideal_of_exists_epi_biproduct`
> followed by
> `Stacks.AmpleCharacterization.isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct_ideal`.

```lean
theorem isAmple_of_quasiSeparatedSpace_and_exists_epi_biproduct [CompactSpace X]
    (h : QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ F), Epi p) :
    IsAmple X L
```

**`Stacks.AmpleCharacterization.tfae_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCharacterization/NineClauses.lean#L246). References: EGA II (4.5.2); EGA II (4.5.5); EGA II (2.7.10); SGA 6 II (2.2.3), “single L”.

> **[Stacks, Tag 01Q3].** Let `X` be a quasi-compact scheme, `L` an invertible `𝒪_X`-module, and
> `S = Γ_*(X, L)`. The nine conditions of the source Proposition are equivalent:
>
> 1. `L` is ample;
> 2. the opens `X_s`, `s ∈ S₊` homogeneous, cover `X` and the resulting `X ⟶ Proj S` is an open
>    immersion;
> 3. those opens form a basis for the topology of `X`;
> 4. the affine ones among them form a basis for the topology of `X`;
> 5. for every quasi-coherent `F` the images of the canonical maps
>    `Γ(X, F ⊗ L^{⊗ n}) ⊗_𝐙 L^{⊗ -n} ⟶ F`, `n ≥ 1`, sum to `F`;
> 6. the same for `F` a quasi-coherent sheaf of ideals;
> 7. `X` is quasi-separated and every finite-type quasi-coherent `F` has `F ⊗ L^{⊗ n}` globally
>    generated for all large `n`;
> 8. `X` is quasi-separated and every finite-type quasi-coherent `F` is a quotient of a finite direct
>    sum of copies of a single `L ^⊗ (-n)`, `n > 0`;
> 9. the same for `F` a finite-type quasi-coherent sheaf of ideals.
>
> The only hypothesis is the source's own: `X` quasi-compact, which is `[CompactSpace X]`, plus the
> invertibility of `L`. Clause (1), `Stacks.Ample.IsAmple`, carries the quasi-compactness in its own
> definition, so the instance is what puts the remaining eight clauses at the strength the source
> gives them. The module docstring says where each `1 ↔ i` comes from.

```lean
theorem tfae_isAmple [CompactSpace X] :
    List.TFAE
      [ IsAmple X L,
        ∃ h : Stacks.SectionRingProjMorphism.nvUnion L = ⊤,
          IsOpenImmersion (Stacks.SectionRingProjMorphism.projHomOfCovers L h),
        ∀ (x : X) (U : X.Opens), x ∈ U → ∃ n : ℕ, 1 ≤ n ∧
          ∃ s : Γ(tensorPowModule X L (n : ℤ), ⊤),
            x ∈ powNonvanishingOpen X L n s ∧ powNonvanishingOpen X L n s ≤ U,
        ∀ (x : X) (U : X.Opens), x ∈ U → ∃ n : ℕ, 1 ≤ n ∧
          ∃ s : Γ(tensorPowModule X L (n : ℤ), ⊤),
            IsAffineOpen (powNonvanishingOpen X L n s) ∧
              x ∈ powNonvanishingOpen X L n s ∧ powNonvanishingOpen X L n s ≤ U,
        ∀ F : X.Modules, F.IsQuasicoherent → ∀ x : X,
          (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(F ⊗ tensorPowModule X L (n : ℤ), ⊤)),
            LinearMap.range (Stacks.ModuleStalk.map (twistHom L F (n : ℤ) m) x)) = ⊤,
        ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j → J.IsQuasicoherent →
          ∀ x : X, (⨆ (n : ℕ) (_ : 1 ≤ n) (m : Γ(J ⊗ tensorPowModule X L (n : ℤ), ⊤)),
            LinearMap.range (Stacks.ModuleStalk.map (twistHom L J (n : ℤ) m) x)) = ⊤,
        QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
          SheafOfModules.IsFiniteType.{u, u, u} F →
            ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
              _root_.SheafOfModules.IsGeneratedByGlobalSections.{u, u, u}
                ((F ⊗ tensorPowModule X L n : X.Modules)),
        QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
          SheafOfModules.IsFiniteType.{u, u, u} F →
            ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
              ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
                (p : b.pt ⟶ F), Epi p,
        QuasiSeparatedSpace X ∧ ∀ (J : X.Modules) (j : J ⟶ unitModule X), Mono j →
          J.IsQuasicoherent → SheafOfModules.IsFiniteType.{u, u, u} J →
            ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
              ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
                (p : b.pt ⟶ J), Epi p ]
```

**`Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_isEventuallyGloballyGenerated_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleLocalGeneration/FromExtension.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleLocalGeneration/FromExtension.lean#L226). The attribute's comment: “clause (7)”. References: EGA II (4.6.8), “absolute case of (c)”; EGA II (4.5.5), “(a) ⇒ (d)”; EGA II (2.7.9).

> **Clause (7) of [Stacks, Tag 01Q3]** — the clause labelled 01QA: `X` is quasi-separated, and
> for every quasi-coherent sheaf `F` of finite type on `X` there is an integer `n₀` such that
> `F ⊗ L ^⊗ n` is globally generated for all `n ≥ n₀`.
>
> Both conjuncts follow from ampleness of `L`, which is clause (1): quasi-separatedness by
> [Stacks, Tag 01PV] (`Stacks.AmplePullbackPart1.quasiSeparatedSpace_of_isAmple`, the affine
> nonvanishing opens being a basis), and the generation by
> `Stacks.AmpleLocalGeneration.isEventuallyGloballyGenerated_of_isAmple`.
>
> The generation is obtained in the stronger form the source does not ask for: the twist is
> generated by **finitely many** global sections, not merely by all of them.

```lean
theorem quasiSeparatedSpace_and_isEventuallyGloballyGenerated_of_isAmple (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L) :
    QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n →
          ∃ σ : (F ⊗ tensorPowModule X L n).GeneratingSections, Finite σ.I
```

**`Stacks.AmpleLocalGeneration.quasiSeparatedSpace_and_exists_epi_biproduct_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleLocalGeneration/FromExtension.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleLocalGeneration/FromExtension.lean#L253). The attribute's comment: “clause (8)”. References: EGA II (2.7.10), “exists n,k quotient”; EGA II (4.5.5), “(a) ⇒ (d')”; SGA 6 II (2.2.3), “(iii), single L”.

> **Clause (8) of [Stacks, Tag 01Q3]** — the clause labelled 01QB: `X` is quasi-separated, and
> for every quasi-coherent sheaf `F` of finite type on `X` there are integers `n > 0` and `k ≥ 0`
> such that `F` is a quotient of a direct sum of `k` copies of `L ^⊗ (-n)`.
>
> The summands all carry the *same* degree `-n`, as the source's clause does; the weaker statement
> with varying degrees is `Stacks.AmpleLocalGeneration.isQuotientOfNegativeTwists_of_isAmple`. The
> `k` of the source is the cardinality of the index type `ι` below: a direct sum over a finite index
> type is a direct sum of `Nat.card ι` copies, and the two existence statements are the same.
>
> The proof is clause (7) at a degree `n ≥ max n₀ 1`, which makes `F ⊗ L ^⊗ n` a quotient of a
> finite free module, followed by
> `Stacks.AmpleGlobalGeneration.exists_epi_biproduct_of_epi_free`, which untwists: tensoring the
> epimorphism `𝒪_X^{⊕ ι} ↠ F ⊗ L ^⊗ n` by `L ^⊗ (-n)` presents `F` as a quotient of
> `(L ^⊗ (-n))^{⊕ ι}`.

```lean
theorem quasiSeparatedSpace_and_exists_epi_biproduct_of_isAmple (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L) :
    QuasiSeparatedSpace X ∧ ∀ F : X.Modules, F.IsQuasicoherent →
      SheafOfModules.IsFiniteType.{u, u, u} F →
        ∃ (n : ℤ) (ι : Type u) (_ : Finite ι), 0 < n ∧
          ∃ (b : Bicone fun _ : ι => tensorPowModule X L (-n)) (_ : b.IsBilimit)
            (p : b.pt ⟶ F), Epi p
```

**`Stacks.SheafOfModules.Invertible.exists_sections_mem_nonvanishingOpen_le_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionExtensionAffineCover/Basic.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionExtensionAffineCover/Basic.lean#L380). The attribute's comment: “(1) implies (3) and (4)”. References: EGA II (4.5.2), “(a') => (a)”; SGA 6 II (2.2.3), “(i), single L”.

> **Tag 01Q6 (item (3) of Tag 01Q3): the nonvanishing opens of the global sections of the
> positive tensor powers of an ample invertible sheaf form a basis for the topology** -- and the
> members of that basis can be taken affine, which is item (4) of Tag 01Q3 (tag 01Q7) and is the
> one-point case of [Stacks, Tag 09NV](https://stacks.math.columbia.edu/tag/09NV).
>
> Affineness is free here: the section produced has nonvanishing open a *basic* open of the
> affine `X_{σ i₀}`, by `AlgebraicGeometry.IsAffineOpen.basicOpen`.

```lean
theorem exists_sections_mem_nonvanishingOpen_le_of_isAmple
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple Y M)
    (W : Y.Opens) (x : Y) (hx : x ∈ W) :
    ∃ (m : ℕ) (_ : 1 ≤ m) (gg : Mpow[m].sections),
      x ∈ NV[m, gg] ∧ NV[m, gg] ≤ W ∧ IsAffineOpen NV[m, gg]
```

## Tag 0B3E, a lemma

[Tag 0B3E](https://stacks.math.columbia.edu/tag/0B3E) in the Stacks Project.

**`Stacks.AmplePullbackCovering.isAmple_modulePullback_of_immersion_or_isEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePullbackCovering/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePullbackCovering/Basic.lean#L84). References: EGA II (4.6.13), “(i bis), absolute case”.

> **Stacks Tag 0B3E.** For `L` an ample invertible `𝒪_X`-module and `i : X' ⟶ X` a
> quasi-compact immersion, an immersion of a quasi-compact scheme, a quasi-compact homeomorphism
> onto its image, or a homeomorphism onto its image out of a quasi-compact scheme, the pullback
> `i^* L` is ample on `X'`.
>
> The proof is `Stacks.SectionExtension.isAmple_pullbackModule`; see the module documentation for
> why the attribute sits here rather than there.

```lean
theorem isAmple_modulePullback_of_immersion_or_isEmbedding {X X' : Scheme.{u}} (i : X' ⟶ X)
    (L : X.Modules) [IsInvertibleModule X L] (hL : IsAmple X L)
    (hi : (QuasiCompact i ∧ IsImmersion i) ∨ (CompactSpace X' ∧ IsImmersion i) ∨
      (QuasiCompact i ∧ Topology.IsEmbedding i) ∨
      (CompactSpace X' ∧ Topology.IsEmbedding i)) :
    IsAmple X' (Stacks.AmpleLocallyClosed.pullbackModule i L)
```

## Tag 0DNK, a lemma

[Tag 0DNK](https://stacks.math.columbia.edu/tag/0DNK) in the Stacks Project.

**`Stacks.AmpleExternalTensor.isInvertibleModule_externalTensor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleExternalTensorProduct.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleExternalTensorProduct.lean#L119). The attribute's comment: “invertibility: the half of Tag 0DNK's conclusion saying that `pr₁^* L ⊗ pr₂^* N` is an invertible module on `X ×_S Y`. No hypothesis on `S` and no ampleness; the ample half is `isAmple_externalTensor`.”.

> The external tensor product of two invertible modules is invertible.

```lean
instance isInvertibleModule_externalTensor (L : X.Modules) (N : Y.Modules)
    [IsInvertibleModule X L] [IsInvertibleModule Y N] :
    IsInvertibleModule (pullback f g) (externalTensor f g L N)
```

**`Stacks.AmpleExternalTensor.isAmple_externalTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleExternalTensorProduct.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleExternalTensorProduct.lean#L348). The attribute's comment: “the whole lemma: for `S` quasi-separated, `X` and `Y` schemes over `S`, `L` ample invertible on `X` and `N` ample invertible on `Y`, the external tensor product `pr₁^* L ⊗ pr₂^* N` is ample on `X ×_S Y`. Invertibility of that module, the other half of the tag's conclusion, is the instance `isInvertibleModule_externalTensor` of this file, which the statement uses. No hypothesis beyond the tag's own.”.

> **Stacks Tag 0DNK.** Let `S` be a quasi-separated scheme, let `X` and `Y` be schemes over
> `S`, let `L` be an ample invertible `𝒪_X`-module and `N` an ample invertible `𝒪_Y`-module. Then
> `pr₁^* L ⊗_{𝒪_{X ×_S Y}} pr₂^* N` is an ample invertible module on `X ×_S Y`.
>
> Invertibility is the instance `Stacks.AmpleExternalTensor.isInvertibleModule_externalTensor`,
> which the statement of ampleness already presupposes. Ampleness is the composite of the two
> halves proved above: the absolute case
> `Stacks.AmpleExternalTensor.isAmple_externalTensor_of_isAffine`, taken at the terminal scheme
> `Spec ℤ`, which is affine, and the descent
> `Stacks.AmpleExternalTensor.isAmple_externalTensor_of_isAmple_absolute` along the quasi-compact
> immersion `X ×_S Y ⟶ X ×_{Spec ℤ} Y`, which is where quasi-separatedness of `S` is used.

```lean
theorem isAmple_externalTensor [QuasiSeparatedSpace S] (hL : IsAmple X L) (hN : IsAmple Y N) :
    IsAmple (pullback f g) (externalTensor f g L N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.27, Tag 01PR](https://stacks.math.columbia.edu/tag/01PR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
