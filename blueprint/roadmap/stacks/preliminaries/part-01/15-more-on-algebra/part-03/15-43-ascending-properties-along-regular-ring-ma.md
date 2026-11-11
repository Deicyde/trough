---
declaration: section
origin: cited
lean: isReduced_of_isRegularRingHom, isNormalRing_of_flat_of_isGeometricallyRegular_fiber, isRegularRing_of_isRegularRingHom, isCohenMacaulayRing_of_isRegularRingHom
statement: formalized
proof: formalized
---

# 15.43 Ascending properties along regular ring maps

Section 15.43 of the Stacks Project, [Tag 07QJ](https://stacks.math.columbia.edu/tag/07QJ). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07QK, a lemma

[Tag 07QK](https://stacks.math.columbia.edu/tag/07QK) in the Stacks Project.

**`isReduced_of_isRegularRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean#L79).

> If `f : R →+* S` is regular, `R` and `S` are Noetherian, and `R` is
> reduced, then `S` is reduced.

```lean
public theorem isReduced_of_isRegularRingHom {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : IsRegularRingHom f) [IsNoetherianRing R]
    [IsReduced R] : IsReduced S
```

## Tag 0BFK, a lemma

[Tag 0BFK](https://stacks.math.columbia.edu/tag/0BFK) in the Stacks Project.

**`isNormalRing_of_flat_of_isGeometricallyRegular_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean#L114). References: EGA IV (6.5.4), “(ii), regular fibres”.

> Let `R → S` be a regular map of Noetherian rings. If `R` is normal, then `S` is normal.

```lean
public theorem isNormalRing_of_flat_of_isGeometricallyRegular_fiber
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S] [Module.Flat R S]
    (hR : IsNormalRing R)
    (hfiber : ∀ (p : Ideal R) [p.IsPrime],
      Algebra.IsGeometricallyRegular p.ResidueField (p.Fiber S)) :
    IsNormalRing S
```

## Tag 0H7S, a lemma

[Tag 0H7S](https://stacks.math.columbia.edu/tag/0H7S) in the Stacks Project.

**`isRegularRing_of_isRegularRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean#L143).

> The Noetherian target of a regular ring homomorphism from a regular ring is regular.

```lean
public theorem isRegularRing_of_isRegularRingHom
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : IsRegularRingHom f)
    [IsNoetherianRing S] [IsRegularRing R] : IsRegularRing S
```

## Tag 0H7T, a lemma

[Tag 0H7T](https://stacks.math.columbia.edu/tag/0H7T) in the Stacks Project.

**`isCohenMacaulayRing_of_isRegularRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Regular/AscentAlongRegularRingHom.lean#L211).

> If `f : R →+* S` is regular, `S` is Noetherian, and `R` is Noetherian and
> Cohen–Macaulay, then `S` is Cohen–Macaulay.

```lean
public theorem isCohenMacaulayRing_of_isRegularRingHom
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    [IsNoetherianRing R] [IsNoetherianRing S] (f : R →+* S)
    (hf : IsRegularRingHom f) (hR : IsCohenMacaulayRing R) :
    IsCohenMacaulayRing S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.43, Tag 07QJ](https://stacks.math.columbia.edu/tag/07QJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
