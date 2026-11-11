---
declaration: section
origin: cited
lean: IsFormallyCatenary, not_isUniversallyCatenary_of_not_isFormallyCatenary, flat_local_catenary_equidim_fibre, flat_local_catenary_equidim_base, isUniversallyCatenary_of_isFormallyCatenary, isUniversallyCatenary_iff_isFormallyCatenary, StacksDraft.Catenary.isUniversallyCatenary_henselization_and_of_isUnibranch
statement: formalized
proof: formalized
---

# 15.111 Formally catenary rings

Section 15.111 of the Stacks Project, [Tag 0AW1](https://stacks.math.columbia.edu/tag/0AW1). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AW2, a definition

[Tag 0AW2](https://stacks.math.columbia.edu/tag/0AW2) in the Stacks Project.

**`IsFormallyCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Formal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Formal.lean#L116). References: EGA IV (7.1.9).

> A local ring `A` is formally catenary if, for every minimal prime `p` of `A`, the spectrum
> of the quotient of its maximal-ideal-adic completion by the extension of `p` is
> equidimensional.

```lean
def IsFormallyCatenary (A : Type*) [CommRing A] [IsLocalRing A] : Prop
```

## Tag 0AW3, a lemma

[Tag 0AW3](https://stacks.math.columbia.edu/tag/0AW3) in the Stacks Project.

**`not_isUniversallyCatenary_of_not_isFormallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Formal.lean, line 1715](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Formal.lean#L1715).

> **Stacks 0AW3.** A Noetherian local ring which is not formally catenary is not universally
> catenary.

```lean
theorem not_isUniversallyCatenary_of_not_isFormallyCatenary
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : ¬ IsFormallyCatenary A) : ¬ Ring.IsUniversallyCatenary A
```

## Tag 0AW4, a lemma

[Tag 0AW4](https://stacks.math.columbia.edu/tag/0AW4) in the Stacks Project.

**`flat_local_catenary_equidim_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Equidimensional/FlatLocal.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Equidimensional/FlatLocal.lean#L557). The attribute's comment: “(1)”. References: EGA IV (7.1.3), “(ii) 'in particular'”.

> **Stacks 0AW4 (1).** For a flat local map `A → B` of Noetherian local rings with
> `B` catenary and `Spec(B)` equidimensional, the fibre `Spec(B / pB)` is
> equidimensional for every prime `p ⊆ A`.

```lean
theorem flat_local_catenary_equidim_fibre (A B : Type*) [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsLocalRing A] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hcat : IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum B))
    (hequi : SpecEquidimensional B)
    (p : Ideal A) [p.IsPrime] :
    SpecEquidimensional (B ⧸ p.map (algebraMap A B))
```

**`flat_local_catenary_equidim_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Equidimensional/FlatLocal.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Equidimensional/FlatLocal.lean#L570). The attribute's comment: “(2)”. References: EGA IV (7.1.3), “(i)”; EGA IV (7.8.3), “(x)”; EGA IV (7.8.4), “partial”.

> **Stacks 0AW4 (2).** For a flat local map `A → B` of Noetherian local rings with
> `B` catenary and `Spec(B)` equidimensional, the base `A` is catenary and `Spec(A)`
> is equidimensional.

```lean
theorem flat_local_catenary_equidim_base (A B : Type*) [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsLocalRing A] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hcat : IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum B))
    (hequi : SpecEquidimensional B) :
    IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum A) ∧ SpecEquidimensional A
```

## Tag 0AW5, a lemma

[Tag 0AW5](https://stacks.math.columbia.edu/tag/0AW5) in the Stacks Project.

**`isUniversallyCatenary_of_isFormallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Formal.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Formal.lean#L652). References: EGA IV (7.1.11), “(i)”.

> **Stacks 0AW5.** A formally catenary Noetherian local ring is universally catenary.

```lean
theorem isUniversallyCatenary_of_isFormallyCatenary
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsFormallyCatenary A) : Ring.IsUniversallyCatenary A
```

## Tag 0AW6, a proposition

[Tag 0AW6](https://stacks.math.columbia.edu/tag/0AW6) in the Stacks Project.

**`isUniversallyCatenary_iff_isFormallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Formal.lean, line 1742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Formal.lean#L1742). References: EGA IV (7.1.11), “(i)”.

> **Ratliff's theorem (Stacks 0AW6).** A Noetherian local ring is universally catenary if and
> only if it is formally catenary.

```lean
theorem isUniversallyCatenary_iff_isFormallyCatenary
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A] :
    Ring.IsUniversallyCatenary A ↔ IsFormallyCatenary A
```

## Tag 0C2F, a lemma

[Tag 0C2F](https://stacks.math.columbia.edu/tag/0C2F) in the Stacks Project.

**`StacksDraft.Catenary.isUniversallyCatenary_henselization_and_of_isUnibranch`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Henselization.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Henselization.lean#L400).

> **Stacks 0C2F.** A Noetherian local ring with geometrically normal formal fibres has a
> universally catenary henselization, and is itself universally catenary if it is unibranch.

```lean
public lemma isUniversallyCatenary_henselization_and_of_isUnibranch
    (A : Type u) (Ah : Type v)
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    (hformal : ∀ q : PrimeSpectrum A,
      Algebra.IsGeometricallyNormal q.asIdeal.ResidueField
        (q.asIdeal.Fiber (AdicCompletion (maximalIdeal A) A))) :
    Ring.IsUniversallyCatenary Ah ∧ (IsUnibranch A → Ring.IsUniversallyCatenary A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.111, Tag 0AW1](https://stacks.math.columbia.edu/tag/0AW1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
