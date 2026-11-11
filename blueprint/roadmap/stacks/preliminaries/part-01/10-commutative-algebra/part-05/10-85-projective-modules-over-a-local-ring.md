---
declaration: section
origin: cited
lean: Module.forall_free_of_projective_iff_forall_free_of_projective_of_countable_span, countablyGenerated_propertyP_free, projective_local_free_summand, Module.free_of_projective_of_isLocalRing
statement: formalized
proof: formalized
---

# 10.85 Projective modules over a local ring

Section 10.85 of the Stacks Project, [Tag 058Z](https://stacks.math.columbia.edu/tag/058Z). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0590, a lemma

[Tag 0590](https://stacks.math.columbia.edu/tag/0590) in the Stacks Project.

**`Module.forall_free_of_projective_iff_forall_free_of_projective_of_countable_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean#L167). The attribute's comment: “The equivalence, with countable generation written as a countable spanning set.”.

> Let `R` be a ring. Every projective `R`-module is free if and only if every projective
> `R`-module admitting a countable generating set is free.

```lean
public theorem Module.forall_free_of_projective_iff_forall_free_of_projective_of_countable_span
    (R : Type u) [Ring R] :
    (∀ (M : Type v) [AddCommGroup M] [Module R M], Module.Projective R M → Module.Free R M) ↔
      ∀ (M : Type v) [AddCommGroup M] [Module R M], Module.Projective R M →
        (∃ s : Set M, s.Countable ∧ Submodule.span R s = ⊤) → Module.Free R M
```

## Tag 0591, a lemma

[Tag 0591](https://stacks.math.columbia.edu/tag/0591) in the Stacks Project.

**`countablyGenerated_propertyP_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Kaplansky.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Kaplansky.lean#L375).

> Stacks Tag 0591 / Lemma 10.85.2: a countably generated module satisfying
> property (P) is free.

```lean
theorem countablyGenerated_propertyP_free
    (hcg : CountablyGenerated R M) (hP : PropertyP R M) :
    Module.Free R M
```

## Tag 0592, a lemma

[Tag 0592](https://stacks.math.columbia.edu/tag/0592) in the Stacks Project.

**`projective_local_free_summand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Kaplansky.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Kaplansky.lean#L512).

> **Stacks Tag 0592, Lemma 10.85.3.** Any element of a projective module over a
> (commutative) local ring is contained in a free direct summand. Concretely, for
> every `x` in a projective module `P` over a local ring `R`, there is a submodule
> `N` of `P` with `x ∈ N`, with `N` free as an `R`-module, and with `N` a direct
> summand of `P` (witnessed by a complementary submodule `N'`, `IsCompl N N'`).

```lean
theorem projective_local_free_summand {R : Type*} [CommRing R] [IsLocalRing R]
    {P : Type*} [AddCommGroup P] [Module R P] [Module.Projective R P] (x : P) :
    ∃ N : Submodule R P, x ∈ N ∧ Module.Free R N ∧ ∃ N' : Submodule R P, IsCompl N N'
```

## Tag 0593, a theorem

[Tag 0593](https://stacks.math.columbia.edu/tag/0593) in the Stacks Project.

**`Module.free_of_projective_of_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Kaplansky.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Kaplansky.lean#L621). The attribute's comment: “Projective modules over local rings are free, with no finiteness hypothesis.”. References: SGA 3 VIA (2.1.3).

> **Stacks 0593** (Kaplansky). If `P` is a projective module over a commutative local ring `R`,
> then `P` is free. No finiteness hypothesis on `P` is needed.

```lean
public theorem Module.free_of_projective_of_isLocalRing {R : Type u} {P : Type v} [CommRing R]
    [AddCommGroup P] [Module R P] [IsLocalRing R] [Module.Projective R P] : Module.Free R P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.85, Tag 058Z](https://stacks.math.columbia.edu/tag/058Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
