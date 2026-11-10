---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.dmLocus, AlgebraicGeometry.Stack.quasiDMLocus, AlgebraicGeometry.Stack.le_dmLocus, AlgebraicGeometry.Stack.le_quasiDMLocus, AlgebraicGeometry.Stack.dmLocus_le_quasiDMLocus, AlgebraicGeometry.Stack.exists_largest_isAbsolutelyDM_openSubstack, AlgebraicGeometry.Stack.exists_largest_isAbsolutelyQuasiDM_openSubstack, AlgebraicGeometry.Stack.exists_nested_largest_isAbsolutelyDM_isAbsolutelyQuasiDM_openSubstack
statement: formalized
proof: formalized
---

# 101.22 The Deligne-Mumford locus

Section 101.22 of the Stacks Project, [Tag 0DSL](https://stacks.math.columbia.edu/tag/0DSL). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DSM, a lemma

[Tag 0DSM](https://stacks.math.columbia.edu/tag/0DSM) in the Stacks Project.

**`AlgebraicGeometry.Stack.dmLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L124). The attribute's comment: “the DM locus, as the supremum of the DM open substacks”.

> **Stacks 0DSM**, the Deligne–Mumford locus. The object property of an algebraic stack `𝒳`
> cut out by the supremum of the object properties of its Deligne–Mumford open substacks; this is
> the substack `𝒳''` of the source.

```lean
noncomputable def dmLocus (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS) : ObjectProperty 𝒳.val.val.obj
```

**`AlgebraicGeometry.Stack.quasiDMLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L132). The attribute's comment: “the quasi-DM locus, as the supremum of the quasi-DM open substacks”.

> **Stacks 0DSM**, the quasi-Deligne–Mumford locus. The object property of an algebraic stack
> `𝒳` cut out by the supremum of the object properties of its quasi-Deligne–Mumford open
> substacks; this is the substack `𝒳'` of the source.

```lean
noncomputable def quasiDMLocus (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS) : ObjectProperty 𝒳.val.val.obj
```

**`AlgebraicGeometry.Stack.le_dmLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L163). The attribute's comment: “maximality of the DM locus”.

> **Stacks 0DSM, maximality for the DM locus.** Every Deligne–Mumford open substack of `𝒳` is
> contained in the Deligne–Mumford locus. This is the force of the word *largest* in the source,
> and it holds with no hypothesis beyond those of the ambient site.

```lean
theorem le_dmLocus (U : OpenSubstack 𝒳)
    (hU : AlgebraicStacks.IsAbsolutelyDM B S hS hZ U.toAlgebraicStack) :
    U.property ≤ dmLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.le_quasiDMLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L171). The attribute's comment: “maximality of the quasi-DM locus”.

> **Stacks 0DSM, maximality for the quasi-DM locus.** Every quasi-Deligne–Mumford open
> substack of `𝒳` is contained in the quasi-Deligne–Mumford locus.

```lean
theorem le_quasiDMLocus (U : OpenSubstack 𝒳)
    (hU : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ U.toAlgebraicStack) :
    U.property ≤ quasiDMLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.dmLocus_le_quasiDMLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L198). The attribute's comment: “the DM locus is contained in the quasi-DM locus”.

> **Stacks 0DSM, the nesting `𝒳'' ⊆ 𝒳'`.** The Deligne–Mumford locus is contained in the
> quasi-Deligne–Mumford locus, because a Deligne–Mumford open substack is quasi-Deligne–Mumford by
> **Stacks 050E** (`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isDM`). This holds with
> no further input.

```lean
theorem dmLocus_le_quasiDMLocus :
    dmLocus B S hS hZ 𝒳 ≤ quasiDMLocus B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.exists_largest_isAbsolutelyDM_openSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L270). The attribute's comment: “existence of the largest DM open substack; the structure theorem Stacks 06N3 is not in the library, so its two uses are carried as the hypotheses `hLocal` (a union of DM open substacks is DM) and `hOpen` (the DM locus is cut out by an open substack)”.

> **Stacks 0DSM for the DM property.** An algebraic stack has a largest Deligne–Mumford open
> substack, and it cuts out the Deligne–Mumford locus.
>
> Two inputs are carried, both standing for **Stacks 06N3**, which the library does not have:
> `hOpen`, that the Deligne–Mumford locus is cut out by an open substack at all, and `hLocal`,
> the local-global step. Maximality is not among them — it is
> `AlgebraicGeometry.Stack.le_dmLocus`, which holds unconditionally.

```lean
theorem exists_largest_isAbsolutelyDM_openSubstack
    (hLocal : IsAbsolutelyDMLocalOnOpenSubstacks.{u, w} B S hS hZ)
    (hOpen : ∃ W : OpenSubstack 𝒳, W.property = dmLocus B S hS hZ 𝒳) :
    ∃ W : OpenSubstack 𝒳,
      W.property = dmLocus B S hS hZ 𝒳 ∧
      AlgebraicStacks.IsAbsolutelyDM B S hS hZ W.toAlgebraicStack ∧
      ∀ V : OpenSubstack 𝒳, AlgebraicStacks.IsAbsolutelyDM B S hS hZ V.toAlgebraicStack →
        V.property ≤ W.property
```

**`AlgebraicGeometry.Stack.exists_largest_isAbsolutelyQuasiDM_openSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L289). The attribute's comment: “existence of the largest quasi-DM open substack; the structure theorem Stacks 06MF is not in the library, so its two uses are carried as the hypotheses `hLocal` (a union of quasi-DM open substacks is quasi-DM) and `hOpen` (the quasi-DM locus is cut out by an open substack)”.

> **Stacks 0DSM for the quasi-DM property.** An algebraic stack has a largest
> quasi-Deligne–Mumford open substack, and it cuts out the quasi-Deligne–Mumford locus. The two
> carried inputs stand for **Stacks 06MF**, as in
> `AlgebraicGeometry.Stack.exists_largest_isAbsolutelyDM_openSubstack`.

```lean
theorem exists_largest_isAbsolutelyQuasiDM_openSubstack
    (hLocal : IsAbsolutelyQuasiDMLocalOnOpenSubstacks.{u, w} B S hS hZ)
    (hOpen : ∃ W : OpenSubstack 𝒳, W.property = quasiDMLocus B S hS hZ 𝒳) :
    ∃ W : OpenSubstack 𝒳,
      W.property = quasiDMLocus B S hS hZ 𝒳 ∧
      AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ W.toAlgebraicStack ∧
      ∀ V : OpenSubstack 𝒳, AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ V.toAlgebraicStack →
        V.property ≤ W.property
```

**`AlgebraicGeometry.Stack.exists_nested_largest_isAbsolutelyDM_isAbsolutelyQuasiDM_openSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocus.lean#L314). The attribute's comment: “the lemma: nested largest DM and quasi-DM open substacks. The structure theorems Stacks 06N3 and 06MF are not in the library, so their uses are carried as the hypotheses `hLocalDM`, `hLocalQuasiDM` (a union of DM, resp. quasi-DM, open substacks has that property) and `hOpenDM`, `hOpenQuasiDM` (each locus is cut out by an open substack)”.

> **Stacks 0DSM.** For an algebraic stack `𝒳` there are open substacks `𝒳'' ⊆ 𝒳' ⊆ 𝒳` with
> `𝒳''` Deligne–Mumford, `𝒳'` quasi-Deligne–Mumford, and each the largest open substack of `𝒳`
> with its property. This is the statement of the source lemma.
>
> The four carried hypotheses are the two uses apiece of **Stacks 06N3** and **Stacks 06MF**
> described on
> `AlgebraicGeometry.Stack.exists_largest_isAbsolutelyDM_openSubstack` and
> `AlgebraicGeometry.Stack.exists_largest_isAbsolutelyQuasiDM_openSubstack`. The nesting
> `𝒳'' ⊆ 𝒳'` is not among them: it is `AlgebraicGeometry.Stack.dmLocus_le_quasiDMLocus`, which
> holds unconditionally.

```lean
theorem exists_nested_largest_isAbsolutelyDM_isAbsolutelyQuasiDM_openSubstack
    (hLocalDM : IsAbsolutelyDMLocalOnOpenSubstacks.{u, w} B S hS hZ)
    (hLocalQuasiDM : IsAbsolutelyQuasiDMLocalOnOpenSubstacks.{u, w} B S hS hZ)
    (hOpenDM : ∃ W : OpenSubstack 𝒳, W.property = dmLocus B S hS hZ 𝒳)
    (hOpenQuasiDM : ∃ W : OpenSubstack 𝒳, W.property = quasiDMLocus B S hS hZ 𝒳) :
    ∃ W' W'' : OpenSubstack 𝒳,
      W''.property ≤ W'.property ∧
      AlgebraicStacks.IsAbsolutelyDM B S hS hZ W''.toAlgebraicStack ∧
      AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ W'.toAlgebraicStack ∧
      (∀ V : OpenSubstack 𝒳, AlgebraicStacks.IsAbsolutelyDM B S hS hZ V.toAlgebraicStack →
        V.property ≤ W''.property) ∧
      ∀ V : OpenSubstack 𝒳, AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ V.toAlgebraicStack →
        V.property ≤ W'.property
```

**`AlgebraicGeometry.Stack.exists_nested_largest_isAbsolutelyDM_openSubstacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusExistence.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusExistence.lean#L324).

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

**`AlgebraicGeometry.Stack.dmLocus_apply_iff_isUnramifiedAutomorphismGroupSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean#L485). The attribute's comment: “part (1)”.

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

**`AlgebraicGeometry.Stack.quasiDMLocus_apply_iff_isLocallyQuasiFiniteAutomorphismGroupSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordLocusPoints.lean#L499). The attribute's comment: “part (2)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
