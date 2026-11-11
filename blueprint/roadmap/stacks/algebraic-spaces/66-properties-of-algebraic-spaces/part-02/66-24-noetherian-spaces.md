---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsNoetherian, AlgebraicGeometry.Space.isLocallyNoetherianSpace_of_isLocallyNoetherian, AlgebraicGeometry.Space.noetherianSpace_of_isQuasiCompact_of_isLocallyNoetherian, AlgebraicGeometry.Space.stacksSober_points_of_isNoetherian, AlgebraicGeometry.Space.noetherianSpace_points_of_isNoetherian, AlgebraicGeometry.Space.stacksSober_and_noetherianSpace_points_of_isNoetherian, AlgebraicGeometry.Space.isLocalRing_etaleLocalRing, AlgebraicGeometry.Space.isNoetherianRing_etaleLocalRing
statement: formalized
proof: formalized
---

# 66.24 Noetherian spaces

Section 66.24 of the Stacks Project, [Tag 03E9](https://stacks.math.columbia.edu/tag/03E9). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03EA, a definition

[Tag 03EA](https://stacks.math.columbia.edu/tag/03EA) in the Stacks Project.

**`AlgebraicGeometry.Space.IsNoetherian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianSpaces.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianSpaces.lean#L56).

> An algebraic space over `S` is *Noetherian* when it is quasi-compact, quasi-separated and
> locally Noetherian. Quasi-separatedness is the absolute notion of Stacks 03BS, part (3), which
> is why the containment `hZ` of the terminal scheme in the site is required; local
> Noetherianity is the étale-local scheme property `AlgebraicGeometry.IsLocallyNoetherian`.

```lean
abbrev IsNoetherian (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 04ZF, a lemma

[Tag 04ZF](https://stacks.math.columbia.edu/tag/04ZF) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyNoetherianSpace_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPoints.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPoints.lean#L59). The attribute's comment: “part (1)”.

> **Stacks 04ZF, part (1).** The space of points of a locally Noetherian algebraic space
> over `S` is a locally Noetherian topological space.

```lean
theorem isLocallyNoetherianSpace_of_isLocallyNoetherian
    (hN : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsLocallyNoetherian X)) :
    IsLocallyNoetherianSpace (points B S hS F)
```

**`AlgebraicGeometry.Space.noetherianSpace_of_isQuasiCompact_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPoints.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPoints.lean#L75). The attribute's comment: “part (2)”.

> **Stacks 04ZF, part (2).** The space of points of a quasi-compact locally Noetherian
> algebraic space over `S` is a Noetherian topological space.

```lean
theorem noetherianSpace_of_isQuasiCompact_of_isLocallyNoetherian
    (hqc : IsQuasiCompactSpace B S hS F)
    (hN : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsLocallyNoetherian X)) :
    NoetherianSpace (points B S hS F)
```

## Tag 04ZG, a lemma

[Tag 04ZG](https://stacks.math.columbia.edu/tag/04ZG) in the Stacks Project.

**`AlgebraicGeometry.Space.stacksSober_points_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean#L70). The attribute's comment: “sobriety”.

> **Stacks 04ZG, sobriety.** The space of points of a Noetherian algebraic space over `S`
> is sober in the sense of Definition 004X: every irreducible closed subset of it has a unique
> generic point.
>
> Only quasi-separatedness is used: it makes the space Zariski locally quasi-separated by
> Tag 03JX, `(η) ⇒ (ζ)` and Tag 03W7, so Tag 06NJ applies.

```lean
theorem stacksSober_points_of_isNoetherian (hF : IsAlgebraicSpace B S hS F)
    (hN : IsNoetherian B S hS hZ F) : StacksSober (points B S hS F)
```

**`AlgebraicGeometry.Space.noetherianSpace_points_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean#L82). The attribute's comment: “Noetherianity”.

> **Stacks 04ZG, Noetherianity.** The space of points of a Noetherian algebraic space over
> `S` is a Noetherian topological space.
>
> Only quasi-compactness and local Noetherianity are used, which is Tag 04ZF (2).

```lean
theorem noetherianSpace_points_of_isNoetherian (hF : IsAlgebraicSpace B S hS F)
    (hN : IsNoetherian B S hS hZ F) : NoetherianSpace (points B S hS F)
```

**`AlgebraicGeometry.Space.stacksSober_and_noetherianSpace_points_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianPointSpaceSober.lean#L89).

> **Stacks 04ZG.** The space of points of a Noetherian algebraic space over `S` is a sober
> Noetherian topological space.

```lean
theorem stacksSober_and_noetherianSpace_points_of_isNoetherian
    (hF : IsAlgebraicSpace B S hS F) (hN : IsNoetherian B S hS hZ F) :
    StacksSober (points B S hS F) ∧ NoetherianSpace (points B S hS F)
```

## Tag 08AH, a lemma

[Tag 08AH](https://stacks.math.columbia.edu/tag/08AH) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalRing_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingNoetherian.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingNoetherian.lean#L119). The attribute's comment: “local ring”.

> **Stacks 08AH.** The étale local ring of an algebraic space at a geometric point is a
> local ring.

```lean
theorem isLocalRing_etaleLocalRing (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : GeometricPoint B S hS F) :
    IsLocalRing (etaleLocalRing B S hS F x)
```

**`AlgebraicGeometry.Space.isNoetherianRing_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingNoetherian.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingNoetherian.lean#L134). The attribute's comment: “Noetherian ring”.

> **Stacks 08AH.** The étale local ring of a Noetherian algebraic space at a geometric point
> is a Noetherian ring.

```lean
theorem isNoetherianRing_etaleLocalRing (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hNoetherian : IsNoetherian B S hS hZ F) (x : GeometricPoint B S hS F) :
    IsNoetherianRing (etaleLocalRing B S hS F x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.24, Tag 03E9](https://stacks.math.columbia.edu/tag/03E9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
