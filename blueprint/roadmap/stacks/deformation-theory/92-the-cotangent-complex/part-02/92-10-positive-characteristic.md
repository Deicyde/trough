---
declaration: section
origin: cited
lean: CommAlgCat.nonempty_homotopy_frobeniusEndo_squareEndo, CommAlgCat.nonempty_homotopy_squareCotangentComplexMap_frobeniusSquare, CommAlgCat.isZero_cotangentComplexDerived_of_perfect
statement: formalized
proof: formalized
---

# 92.10 Positive characteristic

Section 92.10 of the Stacks Project, [Tag 0G5X](https://stacks.math.columbia.edu/tag/0G5X). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G5Y, a lemma

[Tag 0G5Y](https://stacks.math.columbia.edu/tag/0G5Y) in the Stacks Project.

**`CommAlgCat.nonempty_homotopy_frobeniusEndo_squareEndo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/StandardResolutionFrobeniusHomotopy.lean, line 1236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/StandardResolutionFrobeniusHomotopy.lean#L1236).

> **Stacks Project, Tag 0G5Y.** Let `A → B` be a ring map with `p = 0` in `A` for a prime `p`,
> and let `P_•` be the standard resolution of `B` over `A`. The endomorphism of `P_•` induced by
> the commutative square of Frobenius maps `F_A` and `F_B` is homotopic to the endomorphism given
> by Frobenius on each term `P_n`. The homotopy produced here runs from the termwise Frobenius to
> the square-induced map; the source states the relation without an orientation.

```lean
public theorem nonempty_homotopy_frobeniusEndo_squareEndo (hp : p.Prime) (A : Type u)
    [CommRing A] (B : CommAlgCat.{max u v} A) (hA : (p : A) = 0) :
    Nonempty (SimplicialObject.Homotopy
      (frobeniusEndo.{u, v} p hp A B hA) (squareEndo.{u, v} p hp A B hA))
```

## Tag 0G5Z, a lemma

[Tag 0G5Z](https://stacks.math.columbia.edu/tag/0G5Z) in the Stacks Project.

**`CommAlgCat.nonempty_homotopy_squareCotangentComplexMap_frobeniusSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FrobeniusNullHomotopy.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/FrobeniusNullHomotopy.lean#L281).

> Let `p` be a prime, let `A → B` be a ring map with `p = 0` in `A`, and let `F_A` and `F_B` be
> the Frobenius endomorphisms. The endomorphism of the cotangent complex `L_{B/A}` induced by the
> commutative square `(F_A, F_B)` — the map of Section 08QL, namely the `complexMap` field of
> `CommAlgCat.squareFunctoriality` at `CommAlgCat.frobeniusSquare` — is homotopic to zero.
>
> The target is the cotangent complex read over `B` along `F_B`: the induced map is semilinear over
> `F_B`, not `B`-linear. Restriction of scalars leaves the underlying complex of abelian groups and
> its differentials unchanged, so a null homotopy of this map is a null homotopy of the endomorphism
> `L_{B/A} → L_{B/A}`.

```lean
public theorem nonempty_homotopy_squareCotangentComplexMap_frobeniusSquare :
    Nonempty (Homotopy
      (squareCotangentComplexMap.{u, v, u} (frobeniusSquare.{u, v} p hp A B hA)) 0)
```

## Tag 0G60, a lemma

[Tag 0G60](https://stacks.math.columbia.edu/tag/0G60) in the Stacks Project.

**`CommAlgCat.isZero_cotangentComplexDerived_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PerfectVanishing.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PerfectVanishing.lean#L100).

> Let `p` be a prime number, let `A → B` be a ring homomorphism with `p = 0` in `A`, and assume
> that `A` and `B` are perfect. Then `L_{B/A}` is zero in `D(B)`.

```lean
theorem isZero_cotangentComplexDerived_of_perfect [PerfectRing A p]
    [PerfectRing (B : Type u) p] :
    IsZero (cotangentComplexDerived.{u, u} A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.10, Tag 0G5X](https://stacks.math.columbia.edu/tag/0G5X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
