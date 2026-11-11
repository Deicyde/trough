---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSeparated_iff_identity_isClosedImmersion, AlgebraicGeometry.Space.isLocallySeparated_iff_identity_isImmersion, AlgebraicGeometry.Space.isQuasiSeparated_iff_identity_isQuasiCompact, AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_at_identity, AlgebraicGeometry.Space.isUnramified_iff_at_identity, AlgebraicGeometry.Space.locallyQuasiFiniteBaseLocus, AlgebraicGeometry.Space.le_locallyQuasiFiniteBaseLocus, AlgebraicGeometry.Space.isOpenSubspace_locallyQuasiFiniteBaseLocus
statement: formalized
proof: formalized
---

# 78.6 Properties of group algebraic spaces

Section 78.6 of the Stacks Project, [Tag 06P5](https://stacks.math.columbia.edu/tag/06P5). 3 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06P6, a lemma

[Tag 06P6](https://stacks.math.columbia.edu/tag/06P6) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_iff_identity_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean#L153). The attribute's comment: “separatedness”. References: SGA 3 VIB (5.1).

> **Stacks 06P6.** A group algebraic space is separated over its base exactly when its
> identity section is a closed immersion.

```lean
theorem isSeparated_iff_identity_isClosedImmersion (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    IsSeparated 𝒞 S hS G.obj.X.hom ↔
      IsClosedImmersion 𝒞 S hS (η[G.obj.X]).left
```

**`AlgebraicGeometry.Space.isLocallySeparated_iff_identity_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean#L161). The attribute's comment: “local separatedness”.

> **Stacks 06P6.** A group algebraic space is locally separated over its base exactly when
> its identity section is an immersion.

```lean
theorem isLocallySeparated_iff_identity_isImmersion (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    IsLocallySeparated 𝒞 S hS G.obj.X.hom ↔
      IsImmersion 𝒞 S hS (η[G.obj.X]).left
```

**`AlgebraicGeometry.Space.isQuasiSeparated_iff_identity_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Separation.lean#L169). The attribute's comment: “quasi-separatedness”.

> **Stacks 06P6.** A group algebraic space is quasi-separated over its base exactly when its
> identity section is quasi-compact.

```lean
theorem isQuasiSeparated_iff_identity_isQuasiCompact (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    IsQuasiSeparated 𝒞 S hS G.obj.X.hom ↔
      IsQuasiCompact 𝒞 S hS (η[G.obj.X]).left
```

## Tag 0DSI, a lemma

[Tag 0DSI](https://stacks.math.columbia.edu/tag/0DSI) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_at_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/AtIdentity.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/AtIdentity.lean#L211). The attribute's comment: “the locally quasi-finite characterization”.

> **Stacks 0DSI.** A group algebraic space locally of finite type over its base is locally
> quasi-finite exactly when it is quasi-finite at the identity point over every point of the
> base.

```lean
theorem isLocallyQuasiFinite_iff_at_identity (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom) :
    IsLocallyQuasiFinite B S hS G.obj.X.hom ↔
      ∀ b : points B S hS Bs,
        IsQuasiFiniteAt B S hS G.obj.X.hom
          (pointsMap B S hS Bs (MonObj.one (X := G.obj.X)).left b)
```

**`AlgebraicGeometry.Space.isUnramified_iff_at_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/AtIdentity.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/AtIdentity.lean#L332). The attribute's comment: “the unramified characterization”.

> **Stacks 0DSI.** A group algebraic space locally of finite type over its base is unramified
> exactly when it is unramified at the identity point over every point of the base.

```lean
theorem isUnramified_iff_at_identity (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom) :
    IsUnramified B S hS G.obj.X.hom ↔
      ∀ b : points B S hS Bs,
        IsUnramifiedAt B S hS G.obj.X.hom
          (pointsMap B S hS Bs (MonObj.one (X := G.obj.X)).left b)
```

## Tag 0DSJ, a lemma

[Tag 0DSJ](https://stacks.math.columbia.edu/tag/0DSJ) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyQuasiFiniteBaseLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L390). The attribute's comment: “the locally quasi-finite base locus”.

> **Stacks 0DSJ, the locally quasi-finite case.** The *locally quasi-finite base locus* of a
> group algebraic space: the union of all open subspaces of the base over which it is locally
> quasi-finite.

```lean
def locallyQuasiFiniteBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs) : Subfunctor Bs
```

**`AlgebraicGeometry.Space.le_locallyQuasiFiniteBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L398). The attribute's comment: “maximality of the locally quasi-finite base locus”.

> **Stacks 0DSJ, maximality in the locally quasi-finite case.** Every open subspace of the
> base over which a group algebraic space is locally quasi-finite is contained in its locally
> quasi-finite base locus: it is a member of the family that locus is the supremum of.

```lean
theorem le_locallyQuasiFiniteBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs)
    {U : Subfunctor Bs} (hU : IsOpenSubspace B S hS U)
    (hGU : IsLocallyQuasiFinite B S hS (pullback.snd G.obj.X.hom U.ι)) :
    U ≤ locallyQuasiFiniteBaseLocus B S hS G
```

**`AlgebraicGeometry.Space.isOpenSubspace_locallyQuasiFiniteBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L434). The attribute's comment: “openness of the locally quasi-finite base locus”.

> **Stacks 0DSJ, openness in the locally quasi-finite case.** The locally quasi-finite base
> locus of a group algebraic space locally of finite type over its base is an open subspace.

```lean
theorem isOpenSubspace_locallyQuasiFiniteBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom) :
    IsOpenSubspace B S hS (locallyQuasiFiniteBaseLocus B S hS G)
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_locallyQuasiFiniteBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L443). The attribute's comment: “local quasi-finiteness over the locally quasi-finite base locus”.

> **Stacks 0DSJ, the locally quasi-finite case.** A group algebraic space locally of finite
> type over its base is locally quasi-finite over its locally quasi-finite base locus.

```lean
theorem isLocallyQuasiFinite_locallyQuasiFiniteBaseLocus
    (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom) :
    IsLocallyQuasiFinite B S hS
      (pullback.snd G.obj.X.hom (locallyQuasiFiniteBaseLocus B S hS G).ι)
```

**`AlgebraicGeometry.Space.locallyQuasiFiniteBaseLocus_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L462). The attribute's comment: “base change of the locally quasi-finite base locus”.

> **Stacks 0DSJ, base change in the locally quasi-finite case.** Forming the locally
> quasi-finite base locus of a group algebraic space locally of finite type commutes with
> arbitrary base change of algebraic spaces over `S`.

```lean
theorem locallyQuasiFiniteBaseLocus_preimage (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom)
    {Bt : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hBt : IsAlgebraicSpace B S hS Bt) (f : Bt ⟶ Bs) :
    locallyQuasiFiniteBaseLocus B S hS (GroupAlgebraicSpace.baseChange B S hS hBt f G) =
      (locallyQuasiFiniteBaseLocus B S hS G).preimage f
```

**`AlgebraicGeometry.Space.unramifiedBaseLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L494). The attribute's comment: “the unramified base locus”.

> **Stacks 0DSJ, the unramified case.** The *unramified base locus* of a group algebraic
> space: the union of all open subspaces of the base over which it is unramified.

```lean
def unramifiedBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs) : Subfunctor Bs
```

**`AlgebraicGeometry.Space.le_unramifiedBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L502). The attribute's comment: “maximality of the unramified base locus”.

> **Stacks 0DSJ, maximality in the unramified case.** Every open subspace of the base over
> which a group algebraic space is unramified is contained in its unramified base locus: it is a
> member of the family that locus is the supremum of.

```lean
theorem le_unramifiedBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs)
    {U : Subfunctor Bs} (hU : IsOpenSubspace B S hS U)
    (hGU : IsUnramified B S hS (pullback.snd G.obj.X.hom U.ι)) :
    U ≤ unramifiedBaseLocus B S hS G
```

**`AlgebraicGeometry.Space.isOpenSubspace_unramifiedBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L511). The attribute's comment: “openness of the unramified base locus”.

> **Stacks 0DSJ, openness in the unramified case.** The unramified base locus of a group
> algebraic space is an open subspace.

```lean
theorem isOpenSubspace_unramifiedBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs) :
    IsOpenSubspace B S hS (unramifiedBaseLocus B S hS G)
```

**`AlgebraicGeometry.Space.isUnramified_unramifiedBaseLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L520). The attribute's comment: “unramifiedness over the unramified base locus”.

> **Stacks 0DSJ, the unramified case.** A group algebraic space is unramified over its
> unramified base locus.

```lean
theorem isUnramified_unramifiedBaseLocus (G : GroupAlgebraicSpace B S hS Bs hBs) :
    IsUnramified B S hS (pullback.snd G.obj.X.hom (unramifiedBaseLocus B S hS G).ι)
```

**`AlgebraicGeometry.Space.unramifiedBaseLocus_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseLocus.lean#L618). The attribute's comment: “base change of the unramified base locus”.

> **Stacks 0DSJ, base change in the unramified case.** Forming the unramified base locus of a
> group algebraic space locally of finite type commutes with arbitrary base change of algebraic
> spaces over `S`.

```lean
theorem unramifiedBaseLocus_preimage (G : GroupAlgebraicSpace B S hS Bs hBs)
    (hG : IsLocallyOfFiniteType B S hS G.obj.X.hom)
    {Bt : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hBt : IsAlgebraicSpace B S hS Bt) (f : Bt ⟶ Bs) :
    unramifiedBaseLocus B S hS (GroupAlgebraicSpace.baseChange B S hS hBt f G) =
      (unramifiedBaseLocus B S hS G).preimage f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.6, Tag 06P5](https://stacks.math.columbia.edu/tag/06P5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
