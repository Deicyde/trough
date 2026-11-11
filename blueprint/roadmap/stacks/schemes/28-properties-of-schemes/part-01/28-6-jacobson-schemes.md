---
declaration: section
origin: cited
lean: JacobsonSpace, PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace, AlgebraicGeometry.jacobsonSpace_tfae, AlgebraicGeometry.jacobsonSpace_open, JacobsonSpace.of_isOpenEmbedding, PrimeSpectrum.jacobsonSpace_compl_closedPoint, PrimeSpectrum.jacobsonSpace_compl_zeroLocus_jacobson, PrimeSpectrum.jacobsonSpace_compl_zeroLocus_of_le_jacobson
statement: formalized
proof: formalized
---

# 28.6 Jacobson schemes

Section 28.6 of the Stacks Project, [Tag 01P1](https://stacks.math.columbia.edu/tag/01P1). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01P2, a definition

[Tag 01P2](https://stacks.math.columbia.edu/tag/01P2) in the Stacks Project.

Declarations registered for the tag:

- [`JacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=JacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L62) (StacksFrontier): “a Jacobson scheme is `JacobsonSpace` of its underlying space”. References: EGA IV (10.3.1); EGA IV (10.4.1).

## Tag 01P3, a lemma

[Tag 01P3](https://stacks.math.columbia.edu/tag/01P3) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L64) (StacksFrontier): “the equivalence, on the underlying space of Spec R”. References: EGA IV (10.4.2), “special case”; EGA IV (10.4.1), “ring: Spec(A) Jacobson”.

## Tag 01P4, a lemma

[Tag 01P4](https://stacks.math.columbia.edu/tag/01P4) in the Stacks Project.

**`AlgebraicGeometry.jacobsonSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean#L99). The attribute's comment: “the equivalence of the five conditions (1)–(5)”. References: EGA IV (10.3.3), “sufficiency”; EGA IV (10.4.2).

> For a scheme `X` the following are equivalent: `X` is a Jacobson space; `X` is locally
> Jacobson in the sense of Definition 01OQ; the ring of sections over every affine open of `X` is
> Jacobson; there is an affine open covering of `X` whose rings of sections are Jacobson; there is
> an open covering of `X` by Jacobson open subschemes.

```lean
theorem jacobsonSpace_tfae (X : Scheme.{u}) :
    List.TFAE [
      JacobsonSpace X,
      IsLocally (fun (R : Type u) [CommRing R] => IsJacobsonRing R) X,
      ∀ U : X.affineOpens, IsJacobsonRing Γ(X, (U : X.Opens)),
      ∃ (I : Type u) (U : I → X.affineOpens),
        IsOpenCover (fun i ↦ (U i : X.Opens)) ∧
          ∀ i, IsJacobsonRing Γ(X, (U i : X.Opens)),
      ∃ (I : Type u) (U : I → X.Opens),
        IsOpenCover U ∧ ∀ i, JacobsonSpace (U i).toScheme]
```

**`AlgebraicGeometry.jacobsonSpace_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean#L130). The attribute's comment: “the final assertion: every open subscheme of a Jacobson scheme is Jacobson”. References: EGA IV (10.4.3), “Open subpreschemes”.

> Every open subscheme of a Jacobson scheme is Jacobson.

```lean
theorem jacobsonSpace_open {X : Scheme.{u}} (hX : JacobsonSpace X) (U : X.Opens) :
    JacobsonSpace U.toScheme
```

Declarations registered for the tag:

- [`JacobsonSpace.of_isOpenEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=JacobsonSpace.of_isOpenEmbedding#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Jacobson.lean#L137) (StacksFrontier): “jacobson\_open\_subscheme”. References: EGA IV (10.3.2), “special case”; EGA IV (10.3.3), “necessity”; EGA IV (10.4.3), “Open subpreschemes”; EGA IV (10.4.7), “open immersions”.

## Tag 02IM, a lemma

[Tag 02IM](https://stacks.math.columbia.edu/tag/02IM) in the Stacks Project.

**`PrimeSpectrum.jacobsonSpace_compl_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean#L93). The attribute's comment: “part (1)”. References: EGA IV (10.5.9), “Jacobson part”; EGA IV (10.5.7), “Noetherian local ring”; EGA IV (10.5.8), “local case”.

> **Stacks Project, Tag 02IM, part (1).** The punctured spectrum of a Noetherian local ring is
> a Jacobson space.

```lean
theorem jacobsonSpace_compl_closedPoint
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R] :
    JacobsonSpace ↥(({IsLocalRing.closedPoint R} : Set (PrimeSpectrum R))ᶜ)
```

**`PrimeSpectrum.jacobsonSpace_compl_zeroLocus_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean#L109). The attribute's comment: “part (2)”. References: EGA IV (10.5.8), “Spec(A)-V(R) Jacobson”; EGA IV (10.5.9), “Y is Jacobson”; EGA IV (10.5.7), “affine case”.

> **Stacks Project, Tag 02IM, part (2).** The complement of the vanishing locus of the Jacobson
> radical of a Noetherian ring is a Jacobson space.

```lean
theorem jacobsonSpace_compl_zeroLocus_jacobson
    (R : Type u) [CommRing R] [IsNoetherianRing R] :
    JacobsonSpace
      ↥((PrimeSpectrum.zeroLocus (Ring.jacobson R : Set R))ᶜ)
```

**`PrimeSpectrum.jacobsonSpace_compl_zeroLocus_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/JacobsonPuncturedSpectrum/Basic.lean#L119). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 02IM, part (3).** If `(R, I)` is a Noetherian Zariski pair, that is if
> `R` is Noetherian and `I` is contained in the Jacobson radical of `R`, then `Spec R \ V(I)` is a
> Jacobson space.

```lean
theorem jacobsonSpace_compl_zeroLocus_of_le_jacobson
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (I : Ideal R) (hI : I ≤ Ring.jacobson R) :
    JacobsonSpace ↥((PrimeSpectrum.zeroLocus (I : Set R))ᶜ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.6, Tag 01P1](https://stacks.math.columbia.edu/tag/01P1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
