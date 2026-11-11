---
declaration: section
origin: cited
lean: PrimeSpectrum.infinite_of_two_le_ringKrullDim, Ring.krullDimLE_one_of_finite_primeSpectrum, Algebra.FiniteType.krullDimLE_zero_tfae, isJacobsonRing_of_forall_isMaximal_or_infinite_setOf_isPrime
statement: formalized
proof: formalized
---

# 10.61 Applications of dimension theory

Section 10.61 of the Stacks Project, [Tag 02IF](https://stacks.math.columbia.edu/tag/02IF). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02IG, a lemma

[Tag 02IG](https://stacks.math.columbia.edu/tag/02IG) in the Stacks Project.

**`PrimeSpectrum.infinite_of_two_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/DimensionTwoOpens.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/DimensionTwoOpens.lean#L129). References: EGA IV (10.5.1), “e) ⇒ f) for local B”.

> A nonempty open subset of the spectrum of a Noetherian local domain of dimension at least
> two is infinite.

```lean
public theorem infinite_of_two_le_ringKrullDim (R : Type*) [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] [IsDomain R] (hR : 2 ≤ ringKrullDim R) (U : Set (PrimeSpectrum R))
    (hU : IsOpen U) (hU' : U.Nonempty) : U.Infinite
```

## Tag 0ALV, a lemma

[Tag 0ALV](https://stacks.math.columbia.edu/tag/0ALV) in the Stacks Project.

**`Ring.krullDimLE_one_of_finite_primeSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/FinitePrimeSpectrum.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/FinitePrimeSpectrum.lean#L181).

> A Noetherian ring with finitely many primes has dimension at most `1`: every prime ideal is
> either minimal or maximal.

```lean
public theorem krullDimLE_one_of_finite_primeSpectrum (R : Type*) [CommRing R]
    [IsNoetherianRing R] [Finite (PrimeSpectrum R)] :
    KrullDimLE 1 R
```

## Tag 0ALW, a lemma

[Tag 0ALW](https://stacks.math.columbia.edu/tag/0ALW) in the Stacks Project.

**`Algebra.FiniteType.krullDimLE_zero_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/FiniteType.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Artinian/FiniteType.lean#L580). The attribute's comment: “Items (1)-(8); (4) via 04MG's Hausdorff and totally disconnected conditions.”. References: EGA I (6.4.4), “affine case”.

> **Zero-dimensional finite type algebras.** For an algebra `S` of finite type over an
> Artinian ring `R` the following are equivalent: `S` has Krull dimension at most `0`; `S` has
> finitely many prime ideals; `S` has finitely many maximal ideals; `Spec S` is Hausdorff; `S` is
> finite as an `R`-module; `S` is Artinian; `Spec S` is discrete; and `Spec S` is totally
> disconnected. Over a field `R = k` the fifth condition says that `S` is finite dimensional
> as a `k`-vector space.

```lean
public theorem krullDimLE_zero_tfae (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [IsArtinianRing R] [Algebra.FiniteType R S] :
    List.TFAE
      [ Ring.KrullDimLE 0 S,
        Finite (PrimeSpectrum S),
        Finite (MaximalSpectrum S),
        T2Space (PrimeSpectrum S),
        Module.Finite R S,
        IsArtinianRing S,
        DiscreteTopology (PrimeSpectrum S),
        TotallyDisconnectedSpace (PrimeSpectrum S) ]
```

## Tag 00KX, a lemma

[Tag 00KX](https://stacks.math.columbia.edu/tag/00KX) in the Stacks Project.

**`isJacobsonRing_of_forall_isMaximal_or_infinite_setOf_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Criteria.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Criteria.lean#L203). References: EGA IV (10.5.2), “sufficiency”; EGA IV (10.5.5), “(ii) sufficiency, affine”; EGA IV (10.4.3), “Artinian, PID clauses”.

> A Noetherian ring in which every prime ideal is either maximal or contained in infinitely
> many prime ideals is a Jacobson ring.

```lean
public theorem isJacobsonRing_of_forall_isMaximal_or_infinite_setOf_isPrime (R : Type*)
    [CommRing R] [IsNoetherianRing R] (h : ∀ p : Ideal R, p.IsPrime →
      p.IsMaximal ∨ {q : Ideal R | p ≤ q ∧ q.IsPrime}.Infinite) :
    IsJacobsonRing R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.61, Tag 02IF](https://stacks.math.columbia.edu/tag/02IF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
