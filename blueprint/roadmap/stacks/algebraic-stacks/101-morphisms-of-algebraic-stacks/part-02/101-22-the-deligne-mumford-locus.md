---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.dmLocus, AlgebraicGeometry.Stack.quasiDMLocus, AlgebraicGeometry.Stack.le_dmLocus, AlgebraicGeometry.Stack.le_quasiDMLocus, AlgebraicGeometry.Stack.dmLocus_le_quasiDMLocus, AlgebraicGeometry.Stack.exists_nested_largest_isAbsolutelyDM_openSubstacks, AlgebraicGeometry.Stack.dmLocus_apply_iff_isUnramifiedAutomorphismGroupSpace, AlgebraicGeometry.Stack.quasiDMLocus_apply_iff_isLocallyQuasiFiniteAutomorphismGroupSpace
statement: formalized
proof: formalized
---

# 101.22 The Deligne-Mumford locus

Section 101.22 of the Stacks Project, [Tag 0DSL](https://stacks.math.columbia.edu/tag/0DSL). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DSM, a lemma

[Tag 0DSM](https://stacks.math.columbia.edu/tag/0DSM) in the Stacks Project.

**`AlgebraicGeometry.Stack.dmLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L130). The attribute's comment: “the DM locus, as the supremum of the DM open substacks”.

> **Stacks 0DSM**, the Deligne–Mumford locus. The object property of an algebraic stack `𝒳`
> cut out by the supremum of the object properties of its Deligne–Mumford open substacks; this is
> the substack `𝒳''` of the source.

```lean
noncomputable def dmLocus (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS) : ObjectProperty 𝒳.val.val.obj
```

**`AlgebraicGeometry.Stack.quasiDMLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L138). The attribute's comment: “the quasi-DM locus, as the supremum of the quasi-DM open substacks”.

> **Stacks 0DSM**, the quasi-Deligne–Mumford locus. The object property of an algebraic stack
> `𝒳` cut out by the supremum of the object properties of its quasi-Deligne–Mumford open
> substacks; this is the substack `𝒳'` of the source.

```lean
noncomputable def quasiDMLocus (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS) : ObjectProperty 𝒳.val.val.obj
```

**`AlgebraicGeometry.Stack.le_dmLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L169). The attribute's comment: “maximality of the DM locus”.

> **Stacks 0DSM, maximality for the DM locus.** Every Deligne–Mumford open substack of `𝒳` is
> contained in the Deligne–Mumford locus. This is the force of the word *largest* in the source,
> and it holds with no hypothesis beyond those of the ambient site.

```lean
theorem le_dmLocus (U : OpenSubstack 𝒳)
    (hU : AlgebraicStacks.IsAbsolutelyDM B S hS hZ U.toAlgebraicStack) :
    U.property ≤ dmLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.le_quasiDMLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L177). The attribute's comment: “maximality of the quasi-DM locus”.

> **Stacks 0DSM, maximality for the quasi-DM locus.** Every quasi-Deligne–Mumford open
> substack of `𝒳` is contained in the quasi-Deligne–Mumford locus.

```lean
theorem le_quasiDMLocus (U : OpenSubstack 𝒳)
    (hU : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ U.toAlgebraicStack) :
    U.property ≤ quasiDMLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.dmLocus_le_quasiDMLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L204). The attribute's comment: “the DM locus is contained in the quasi-DM locus”.

> **Stacks 0DSM, the nesting `𝒳'' ⊆ 𝒳'`.** The Deligne–Mumford locus is contained in the
> quasi-Deligne–Mumford locus, because a Deligne–Mumford open substack is quasi-Deligne–Mumford by
> **Stacks 050E** (`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isDM`). This holds with
> no further input.

```lean
theorem dmLocus_le_quasiDMLocus :
    dmLocus B S hS hZ 𝒳 ≤ quasiDMLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.exists_nested_largest_isAbsolutelyDM_openSubstacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusExistence.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusExistence.lean#L326). The attribute's comment: “open substacks W'' ≤ W' of 𝒳 with W'' absolutely DM and W' absolutely quasi-DM (050D(5),(6)), each containing every absolutely DM, resp. absolutely quasi-DM, open substack of 𝒳”.

> **Stacks 0DSM.** Let `𝒳` be an algebraic stack. There exist open substacks
> `𝒳'' ⊆ 𝒳' ⊆ 𝒳` such that `𝒳''` is DM, `𝒳'` is quasi-DM, and these are the largest open
> substacks with these properties.
>
> Here `W''` is `𝒳''` and `W'` is `𝒳'`. DM and quasi-DM are the absolute notions of
> **Stacks 050D**, parts (5) and (6), read over the terminal scheme `Spec ℤ`, which every big fppf
> site contains (`AlgebraicGeometry.BigFppfSite.contains_terminal`); containment of open substacks
> is containment of their objects.

```lean
theorem exists_nested_largest_isAbsolutelyDM_openSubstacks :
    ∃ W' W'' : OpenSubstack 𝒳,
      W''.property ≤ W'.property ∧
      AlgebraicStacks.IsAbsolutelyDM B S hS B.contains_terminal W''.toAlgebraicStack ∧
      AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal W'.toAlgebraicStack ∧
      (∀ V : OpenSubstack 𝒳,
        AlgebraicStacks.IsAbsolutelyDM B S hS B.contains_terminal V.toAlgebraicStack →
          V.property ≤ W''.property) ∧
      ∀ V : OpenSubstack 𝒳,
        AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal V.toAlgebraicStack →
          V.property ≤ W'.property
```

## Tag 0DSN, a lemma

[Tag 0DSN](https://stacks.math.columbia.edu/tag/0DSN) in the Stacks Project.

**`AlgebraicGeometry.Stack.dmLocus_apply_iff_isUnramifiedAutomorphismGroupSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean#L485). The attribute's comment: “part (1)”.

> **Stacks 0DSN, part (1).** A field-valued point of an algebraic stack lies in its
> Deligne–Mumford locus exactly when its automorphism group algebraic space is unramified over
> its field.
>
> The objects of `𝒳` whose automorphism group algebraic space is unramified form an open substack,
> `AlgebraicGeometry.Stack.automorphismLocusSubstack`, open because the unramified base locus of
> **Stacks 0DSJ** is, and Deligne–Mumford by the pseudo-torsor argument of **Stacks 0CL0** through
> **Stacks 0DSK**; conversely an open substack is Deligne–Mumford only if the automorphism group
> algebraic spaces of its objects, which are those computed in `𝒳`, are unramified.

```lean
theorem dmLocus_apply_iff_isUnramifiedAutomorphismGroupSpace
    (x : FieldValuedPoint B S hS 𝒳.val.val) :
    dmLocus B S hS hZ 𝒳 x.obj ↔ IsUnramifiedAutomorphismGroupSpace B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.quasiDMLocus_apply_iff_isLocallyQuasiFiniteAutomorphismGroupSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean#L499). The attribute's comment: “part (2)”.

> **Stacks 0DSN, part (2).** A field-valued point of an algebraic stack lies in its
> quasi-Deligne–Mumford locus exactly when its automorphism group algebraic space is locally
> quasi-finite over its field. The source says the proof is the same as for part (1), and it
> is.

```lean
theorem quasiDMLocus_apply_iff_isLocallyQuasiFiniteAutomorphismGroupSpace
    (x : FieldValuedPoint B S hS 𝒳.val.val) :
    quasiDMLocus B S hS hZ 𝒳 x.obj ↔
      IsLocallyQuasiFiniteAutomorphismGroupSpace B S hS 𝒳 x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.22, Tag 0DSL](https://stacks.math.columbia.edu/tag/0DSL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
