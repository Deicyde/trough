---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.exists_invariant_affine_open_of_orbit_subset_affine, AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_isAffineOpen_mem
statement: formalized
proof: formalized
---

# 39.24 Finite flat groupoids

Section 39.24 of the Stacks Project, [Tag 03JD](https://stacks.math.columbia.edu/tag/03JD). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03JE, a lemma

[Tag 03JE](https://stacks.math.columbia.edu/tag/03JE) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_invariant_affine_open_of_orbit_subset_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/InvariantAffineOpen.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/InvariantAffineOpen.lean#L351). References: SGA 1 V (1.8), “orbit⊂affine⇒inv affine”.

> **Stacks Project, Tag 03JE.** In a groupoid scheme with finite locally free source and
> target maps, a point whose orbit is contained in an affine open has an invariant affine open
> neighbourhood.

```lean
theorem exists_invariant_affine_open_of_orbit_subset_affine {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S)
    [Stacks.Morphisms.IsFiniteLocallyFree G.source.left]
    [Stacks.Morphisms.IsFiniteLocallyFree G.target.left] (x : G.objects.left)
    (h : ∃ W : G.objects.left.Opens, IsAffineOpen W ∧
      ∀ r : G.arrows.left, G.source.left.base r = x → G.target.left.base r ∈ W) :
    ∃ V : G.objects.left.Opens, IsAffineOpen V ∧ x ∈ V ∧ IsInvariantOpen G V
```

**`AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_isAffineOpen_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantAffineOpen.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantAffineOpen.lean#L160). References: SGA 1 V (1.8), “orbit⊂affine⇒inv affine”.

> **Stacks Project, Tag 03JE.** Let `(U, R, s, t, c)` be a groupoid scheme with `s` and `t`
> finite locally free, and let `u` be a point of `U` whose equivalence class `t(s⁻¹({u}))` is
> contained in an affine open of `U`. Then `u` has an `R`-invariant affine open neighbourhood in
> `U`.
>
> The neighbourhood is the nonvanishing locus of the norm along `s` of the pullback along `t` of a
> function cutting the class of `u` out of an invariant open inside the given affine open; see the
> implementation notes.

```lean
theorem exists_isInvariantOpen_isAffineOpen_mem
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (u : G.objects.left)
    (hu : ∃ W : G.objects.left.Opens, IsAffineOpen W ∧
      G.target.left.base '' (G.source.left.base ⁻¹' {u}) ⊆ (W : Set G.objects.left)) :
    ∃ V : G.objects.left.Opens, IsInvariantOpen G V ∧ IsAffineOpen V ∧ u ∈ V
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.24, Tag 03JD](https://stacks.math.columbia.edu/tag/03JD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
