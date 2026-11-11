---
declaration: section
origin: cited
lean: IsAbsolutelyIntegrallyClosed, isAbsolutelyIntegrallyClosed_iff_exists_root, isAbsolutelyIntegrallyClosed_quotient, isAbsolutelyIntegrallyClosed_localization, isAbsolutelyIntegrallyClosed_of_localization, isAbsolutelyIntegrallyClosed_iff_isAlgClosed_fractionRing, exists_absolutelyIntegrallyClosed_extension_as_filteredColimit, IsAbsolutelyIntegrallyClosed.isStrictlyHenselian_atPrime
statement: formalized
proof: formalized
---

# 15.14 Absolute integral closure

Section 15.14 of the Stacks Project, [Tag 0DCK](https://stacks.math.columbia.edu/tag/0DCK). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DCL, a definition

[Tag 0DCL](https://stacks.math.columbia.edu/tag/0DCL) in the Stacks Project.

**`IsAbsolutelyIntegrallyClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L61).

> **Stacks 0DCL.**
> A ring `A` is *absolutely integrally closed* if every monic polynomial in `A[X]` is the product
> of the linear factors `X - C a` over some multiset `s` of elements of `A`.

```lean
def IsAbsolutelyIntegrallyClosed (A : Type*) [CommRing A] : Prop
```

## Tag 0DCM, a lemma

[Tag 0DCM](https://stacks.math.columbia.edu/tag/0DCM) in the Stacks Project.

**`isAbsolutelyIntegrallyClosed_iff_exists_root`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L133).

> **Stacks 0DCM**.
> A ring `A` is absolutely integrally closed if and only if every monic polynomial of degree at least
> `1` has a root in `A`.

```lean
theorem isAbsolutelyIntegrallyClosed_iff_exists_root (A : Type*) [CommRing A] :
    IsAbsolutelyIntegrallyClosed A ↔
      ∀ f : A[X], f.Monic → 1 ≤ f.natDegree → ∃ a : A, f.eval a = 0
```

## Tag 0DCN, a lemma

[Tag 0DCN](https://stacks.math.columbia.edu/tag/0DCN) in the Stacks Project.

**`isAbsolutelyIntegrallyClosed_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L175). The attribute's comment: “(1)”.

> **Stacks 0DCN** (part 1).
> If `A` is absolutely integrally closed, then so is the quotient `A ⧸ I` for every ideal `I`.

```lean
theorem isAbsolutelyIntegrallyClosed_quotient (A : Type*) [CommRing A] (I : Ideal A)
    (hA : IsAbsolutelyIntegrallyClosed A) : IsAbsolutelyIntegrallyClosed (A ⧸ I)
```

**`isAbsolutelyIntegrallyClosed_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L191). The attribute's comment: “(2)”.

> **Stacks 0DCN** (part 2).
> If `A` is absolutely integrally closed, then so is every localization `B` of `A` at a submonoid
> `S`.

```lean
theorem isAbsolutelyIntegrallyClosed_localization (A : Type*) [CommRing A] (S : Submonoid A)
    (B : Type*) [CommRing B] [Algebra A B] [IsLocalization S B]
    (hA : IsAbsolutelyIntegrallyClosed A) : IsAbsolutelyIntegrallyClosed B
```

## Tag 0DCP, a lemma

[Tag 0DCP](https://stacks.math.columbia.edu/tag/0DCP) in the Stacks Project.

**`isAbsolutelyIntegrallyClosed_of_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L230).

> **Stacks 0DCP**.
> Let `B = S⁻¹A` be the localization of `A` at a submonoid `S` of nonzerodivisors. If `B` is
> absolutely integrally closed and `A` is integrally closed in `B`, then `A` is absolutely integrally
> closed.

```lean
theorem isAbsolutelyIntegrallyClosed_of_localization (A : Type*) [CommRing A] (B : Type*)
    [CommRing B] [Algebra A B] (S : Submonoid A) [IsLocalization S B] (hS : S ≤ nonZeroDivisors A)
    (hB : IsAbsolutelyIntegrallyClosed B) (hAB : IsIntegrallyClosedIn A B) :
    IsAbsolutelyIntegrallyClosed A
```

## Tag 0DCQ, a lemma

[Tag 0DCQ](https://stacks.math.columbia.edu/tag/0DCQ) in the Stacks Project.

**`isAbsolutelyIntegrallyClosed_iff_isAlgClosed_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed.lean#L264).

> **Stacks 0DCQ**.
> A normal domain is absolutely integrally closed if and only if its fraction field is
> algebraically closed.

```lean
theorem isAbsolutelyIntegrallyClosed_iff_isAlgClosed_fractionRing
    (A : Type*) [CommRing A] [IsDomain A] [IsIntegrallyClosed A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K] :
    IsAbsolutelyIntegrallyClosed A ↔ IsAlgClosed K
```

## Tag 0DCR, a lemma

[Tag 0DCR](https://stacks.math.columbia.edu/tag/0DCR) in the Stacks Project.

**`exists_absolutelyIntegrallyClosed_extension_as_filteredColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed/Extension.lean, line 1409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AbsolutelyIntegrallyClosed/Extension.lean#L1409).

> **Stacks 0DCR.** Every commutative ring has an injective extension which is a filtered
> colimit of finite free algebras, is free as a module over the original ring, and is absolutely
> integrally closed.

```lean
theorem exists_absolutelyIntegrallyClosed_extension_as_filteredColimit
    (A : Type u) [CommRing A] :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      Function.Injective (algebraMap A B) ∧
      (∃ (J : Type u) (_ : SmallCategory J) (_ : IsFiltered J)
        (F : J ⥤ CommAlgCat.{u} A) (c : Cocone F),
          (∀ j, Module.Finite A (F.obj j) ∧ Module.Free A (F.obj j)) ∧
          Nonempty (IsColimit c) ∧ Nonempty (c.pt ≅ CommAlgCat.of A B)) ∧
      Module.Free A B ∧ IsAbsolutelyIntegrallyClosed B
```

## Tag 0DCS, a lemma

[Tag 0DCS](https://stacks.math.columbia.edu/tag/0DCS) in the Stacks Project.

**`IsAbsolutelyIntegrallyClosed.isStrictlyHenselian_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/AbsolutelyIntegrallyClosed.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/AbsolutelyIntegrallyClosed.lean#L436).

> **Stacks 0DCS**.
> The localization of an absolutely integrally closed ring at a prime ideal is strictly
> henselian: it is a henselian local ring and its residue field is separably closed.

```lean
theorem IsAbsolutelyIntegrallyClosed.isStrictlyHenselian_atPrime
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B]
    (hA : IsAbsolutelyIntegrallyClosed A) (p : Ideal A) [p.IsPrime]
    [IsLocalization.AtPrime B p]
    (h : IsLocalRing B := IsLocalization.AtPrime.isLocalRing B p) :
    HenselianLocalRing B ∧ IsSepClosed (IsLocalRing.ResidueField B)
```

## Tag 0DCT, a lemma

[Tag 0DCT](https://stacks.math.columbia.edu/tag/0DCT) in the Stacks Project.

**`henselianPair_iff_of_absolutelyIntegrallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/AbsolutelyIntegrallyClosed.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/AbsolutelyIntegrallyClosed.lean#L424).

> **Stacks 0DCT**.
> Let `A` be an absolutely integrally closed ring and `I ⊆ A` an ideal. Then `(A, I)` is a
> henselian pair if and only if `I` is contained in the Jacobson radical of `A` and the map
> `A → A ⧸ I` induces a bijection on idempotents.

```lean
theorem henselianPair_iff_of_absolutelyIntegrallyClosed
    {A : Type*} [CommRing A] (hA : IsAbsolutelyIntegrallyClosed A)
    (I : Ideal A) :
    HenselianPair A I ↔
      IsContainedInJacobson I ∧ InducesBijectionOnIdempotents I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.14, Tag 0DCK](https://stacks.math.columbia.edu/tag/0DCK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
