---
declaration: section
origin: cited
lean: encard_minimalPrimes_directLimit, AlgebraicGeometry.numberOfGeometricBranches_eq_iSup_encard, AlgebraicGeometry.numberOfBranches_eq_iSup_encard_irreducibleComponentsThrough, AlgebraicGeometry.isUnibranchAt_iff_existsUnique_irreducibleComponent, AlgebraicGeometry.isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent, AlgebraicGeometry.numberOfBranches_fiber_eq_iSup_encard_irreducibleComponentsThrough, AlgebraicGeometry.numberOfGeometricBranches_fiber_eq_iSup_encard, AlgebraicGeometry.isUnibranchAt_fiber_iff_existsUnique_irreducibleComponent
statement: formalized
proof: formalized
---

# 37.36 Étale neighbourhoods and branches

Section 37.36 of the Stacks Project, [Tag 0CB2](https://stacks.math.columbia.edu/tag/0CB2). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CB3, a lemma

[Tag 0CB3](https://stacks.math.columbia.edu/tag/0CB3) in the Stacks Project.

**`encard_minimalPrimes_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/MinimalPrimesDirectLimit.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/MinimalPrimesDirectLimit.lean#L166).

> **Stacks Project, Tag 0CB3.** For a directed system of rings with faithfully
> flat transition maps, the number of minimal primes of the direct limit is the
> supremum of the numbers of minimal primes at the individual stages.

```lean
theorem encard_minimalPrimes_directLimit
    {ι : Type u} [Preorder ι] [Nonempty ι] [IsDirected ι (· ≤ ·)]
    (R : ι → Type v) [(i : ι) → CommRing (R i)]
    (f : (i j : ι) → i ≤ j → R i →+* R j)
    [DirectedSystem R (fun i j h => (f i j h : R i → R j))]
    (hff : ∀ i j (h : i ≤ j), (f i j h).FaithfullyFlat) :
    Set.encard (minimalPrimes (Ring.DirectLimit R
      (fun i j h => (f i j h : R i → R j)))) =
      ⨆ i, Set.encard (minimalPrimes (R i))
```

## Tag 0CB4, a lemma

[Tag 0CB4](https://stacks.math.columbia.edu/tag/0CB4) in the Stacks Project.

**`AlgebraicGeometry.numberOfGeometricBranches_eq_iSup_encard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Branches.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Branches.lean#L568). The attribute's comment: “geometric\_branches\_supremum”.

> **Stacks Project, Tag 0CB4.** The number of geometric branches at a point is the
> supremum, over all étale neighborhoods of that point, of the number of irreducible components
> of the neighborhood passing through its distinguished point.

```lean
theorem numberOfGeometricBranches_eq_iSup_encard
    (X : AlgebraicGeometry.Scheme.{u}) (x : X) :
    numberOfGeometricBranches X x =
      ⨆ U : EtaleNeighborhood X x,
        Set.encard {Z ∈ irreducibleComponents U.scheme | U.point ∈ Z}
```

**`AlgebraicGeometry.numberOfBranches_eq_iSup_encard_irreducibleComponentsThrough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Branches.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/Branches.lean#L1093). The attribute's comment: “branches\_supremum”.

> **Stacks Project, Tag 0CB4.** The number of branches at a point is the
> supremum, over elementary étale neighborhoods, of the number of irreducible
> components passing through the distinguished point.

```lean
theorem numberOfBranches_eq_iSup_encard_irreducibleComponentsThrough
    (X : Scheme.{u}) (x : X) :
    numberOfBranches X x =
      ⨆ (U : EtaleNeighborhood X x) (_ : U.IsElementary),
        Set.encard {Z ∈ irreducibleComponents U.scheme | U.point ∈ Z}
```

**`AlgebraicGeometry.isUnibranchAt_iff_existsUnique_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/UnibranchEtaleCriterion.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/UnibranchEtaleCriterion.lean#L70). The attribute's comment: “unibranch\_iff”.

> **Stacks Project, Tag 0CB4.** A scheme is unibranch at a point if and only if every
> elementary étale neighbourhood of that point has exactly one irreducible component passing
> through its distinguished point.

```lean
theorem isUnibranchAt_iff_existsUnique_irreducibleComponent (X : Scheme.{u}) (x : X) :
    IsUnibranchAt X x ↔
      ∀ U : EtaleNeighborhood X x, U.IsElementary →
        ∃! Z : irreducibleComponents U.scheme, U.point ∈ (Z : Set U.scheme)
```

**`AlgebraicGeometry.isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/UnibranchEtaleCriterion.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/UnibranchEtaleCriterion.lean#L89). The attribute's comment: “geometrically\_unibranch\_iff”. References: EGA IV (7.9.10), “more general”; SGA 3 X (5.14.0), “partial”.

> **Stacks Project, Tag 0CB4.** A scheme is geometrically unibranch at a point if and only if
> every étale neighbourhood of that point has exactly one irreducible component passing through its
> distinguished point.

```lean
theorem isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent
    (X : Scheme.{u}) (x : X) :
    IsGeometricallyUnibranchAt X x ↔
      ∀ U : EtaleNeighborhood X x,
        ∃! Z : irreducibleComponents U.scheme, U.point ∈ (Z : Set U.scheme)
```

## Tag 0CB5, a lemma

[Tag 0CB5](https://stacks.math.columbia.edu/tag/0CB5) in the Stacks Project.

**`AlgebraicGeometry.numberOfBranches_fiber_eq_iSup_encard_irreducibleComponentsThrough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean#L273). The attribute's comment: “fibre\_branches”.

> **Stacks Project, Tag 0CB5.** The branches of a fibre are counted by
> irreducible components through the distinguished points of fibres of
> elementary étale neighborhoods.

```lean
public theorem numberOfBranches_fiber_eq_iSup_encard_irreducibleComponentsThrough
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    numberOfBranches (f.fiber (f x)) (f.asFiber x) =
      ⨆ (U : EtaleNeighborhood X x) (_ : U.IsElementary),
        Set.encard
          {Z ∈ irreducibleComponents ((U.toBase ≫ f).fiber (f x)) |
            ((U.toBase ≫ f).fiberHomeo (f x)).symm
              ⟨U.point, by simp [U.map_point]⟩ ∈ Z}
```

**`AlgebraicGeometry.numberOfGeometricBranches_fiber_eq_iSup_encard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean#L299). The attribute's comment: “fibre\_geometric\_branches”.

> **Stacks Project, Tag 0CB5.** Geometric branches of a fibre are counted by
> irreducible components through the distinguished points of fibres of étale
> neighbourhoods.

```lean
public theorem numberOfGeometricBranches_fiber_eq_iSup_encard
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    numberOfGeometricBranches (f.fiber (f x)) (f.asFiber x) =
      ⨆ U : EtaleNeighborhood X x,
        Set.encard
          {Z ∈ irreducibleComponents ((U.toBase ≫ f).fiber (f x)) |
            ((U.toBase ≫ f).fiberHomeo (f x)).symm
              ⟨U.point, by simp [U.map_point]⟩ ∈ Z}
```

**`AlgebraicGeometry.isUnibranchAt_fiber_iff_existsUnique_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean#L324). The attribute's comment: “fibre\_unibranch\_iff”.

> **Stacks Project, Tag 0CB5.** The fibre is unibranch at the point if and only if for every
> elementary étale neighbourhood of the point in the total space there is exactly one irreducible
> component of its fibre passing through the distinguished point.

```lean
public theorem isUnibranchAt_fiber_iff_existsUnique_irreducibleComponent
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    IsUnibranchAt (f.fiber (f x)) (f.asFiber x) ↔
      ∀ U : EtaleNeighborhood X x, U.IsElementary →
        ∃! Z : irreducibleComponents ((U.toBase ≫ f).fiber (f x)),
          ((U.toBase ≫ f).fiberHomeo (f x)).symm ⟨U.point, by simp [U.map_point]⟩ ∈
            (Z : Set ((U.toBase ≫ f).fiber (f x)))
```

**`AlgebraicGeometry.isGeometricallyUnibranchAt_fiber_iff_existsUnique_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranches.lean#L358). The attribute's comment: “fibre\_geometrically\_unibranch\_iff”.

> **Stacks Project, Tag 0CB5, part (4), stated about the fibre.** The fibre is geometrically
> unibranch at the point if and only if for every étale neighbourhood of the point in the total
> space there is exactly one irreducible component of its fibre passing through the distinguished
> point.
>
> The source states part (4) as "`X` is geometrically unibranch at `x`", not `X_s`, while its
> right-hand side is about the irreducible components of the *fibre* `U_s`. That pairing of `X`
> with `U_s` is the asymmetry: parts (1), (2) and (3) are all about `X_s`, part (4) is the
> geometric counterpart of part (3), and the cited proof (Tags 0CB4 and 0CAS) yields the statement
> about the fibre. The fibre statement is what is proved here; the deviation from the literal text
> of part (4) is recorded rather than silently adopted.
>
> The deviation is not a choice between two defensible readings:
> `AlgebraicGeometry.not_forall_isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent`
> refutes the literal statement about `X`, so the reading about the fibre proved here is the only
> true one.

```lean
public theorem isGeometricallyUnibranchAt_fiber_iff_existsUnique_irreducibleComponent
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    IsGeometricallyUnibranchAt (f.fiber (f x)) (f.asFiber x) ↔
      ∀ U : EtaleNeighborhood X x,
        ∃! Z : irreducibleComponents ((U.toBase ≫ f).fiber (f x)),
          ((U.toBase ≫ f).fiberHomeo (f x)).symm ⟨U.point, by simp [U.map_point]⟩ ∈
            (Z : Set ((U.toBase ≫ f).fiber (f x)))
```

**`AlgebraicGeometry.not_forall_isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranchesLiteralForm.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/FiberBranchesLiteralForm.lean#L155). The attribute's comment: “part (4) as printed, about X rather than X\_s, is FALSE: counterexample”.

> It is not true that for every morphism `f : X ⟶ S` and every point `x` of `X`, `X` is
> geometrically unibranch at `x` if and only if for every étale neighbourhood `(U, u)` of `(X, x)`
> there is exactly one irreducible component of the fibre of `U ⟶ S` over `f x` through `u`.

```lean
theorem not_forall_isGeometricallyUnibranchAt_iff_existsUnique_irreducibleComponent :
    ¬ ∀ (X S : Scheme.{u}) (f : X ⟶ S) (x : X),
        IsGeometricallyUnibranchAt X x ↔
          ∀ U : EtaleNeighborhood X x,
            ∃! Z : irreducibleComponents ((U.toBase ≫ f).fiber (f x)),
              ((U.toBase ≫ f).fiberHomeo (f x)).symm ⟨U.point, by simp [U.map_point]⟩ ∈
                (Z : Set ((U.toBase ≫ f).fiber (f x)))
```

## Tag 0DQ2, a lemma

[Tag 0DQ2](https://stacks.math.columbia.edu/tag/0DQ2) in the Stacks Project.

**`AlgebraicGeometry.numberOfGeometricBranches_eq_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/SmoothBranches.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/SmoothBranches.lean#L220). The attribute's comment: “geometric\_branches”.

> **Stacks Project, Tag 0DQ2.** A smooth morphism of schemes preserves the number of geometric
> branches at a point.

```lean
public theorem numberOfGeometricBranches_eq_of_smooth {X S : Scheme.{u}} (f : X ⟶ S) [Smooth f]
    (x : X) :
    numberOfGeometricBranches X x = numberOfGeometricBranches S (f.base x)
```

**`AlgebraicGeometry.numberOfBranches_eq_of_smooth_of_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/SmoothBranches.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleNeighbourhood/SmoothBranches.lean#L229). The attribute's comment: “branches\_purely\_inseparable”.

> **Stacks Project, Tag 0DQ2.** A smooth morphism of schemes preserves the number of branches
> at a point whose residue field is a purely inseparable extension of the residue field of its
> image.

```lean
public theorem numberOfBranches_eq_of_smooth_of_isPurelyInseparable {X S : Scheme.{u}}
    (f : X ⟶ S) [Smooth f] (x : X)
    (h : (f.residueFieldMap x).hom.IsPurelyInseparable) :
    numberOfBranches X x = numberOfBranches S (f.base x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.36, Tag 0CB2](https://stacks.math.columbia.edu/tag/0CB2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
