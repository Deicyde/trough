---
declaration: section
origin: cited
lean: height_add_trdeg_residue_le, height_add_trdeg_residue_eq, Ideal.primesOver_finite_and_forall_height_eq_one
statement: formalized
proof: formalized
---

# 10.113 The dimension formula

Section 10.113 of the Stacks Project, [Tag 02II](https://stacks.math.columbia.edu/tag/02II). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02IJ, a lemma

[Tag 02IJ](https://stacks.math.columbia.edu/tag/02IJ) in the Stacks Project.

**`height_add_trdeg_residue_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DimensionFormula/GeneratorInduction.lean, line 790](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DimensionFormula/GeneratorInduction.lean#L790). References: EGA IV (13.3.4), “partial”; EGA IV (5.5.6), “partial”; EGA IV (5.5.7), “more general”; EGA IV (5.5.8), “more general”; EGA IV (5.6.5), “special case”.

> **Stacks 02IJ**.
> For `R` Noetherian, `S` a finite-type domain extension of the domain `R`, and `q` a prime of `S`
> lying over `p`, `q.height + trdeg_{κ(p)} κ(q) ≤ p.height + trdeg_R S`.

```lean
theorem height_add_trdeg_residue_le
    [IsNoetherianRing R] [Algebra.FiniteType R S] [IsDomain R] [IsDomain S]
    (hinj : Function.Injective (algebraMap R S))
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p] :
    letI := Ideal.ResidueField.algebraOfLiesOver p q
    q.height + (Cardinal.toNat (Algebra.trdeg p.ResidueField q.ResidueField) : ℕ∞)
      ≤ p.height + (Cardinal.toNat (Algebra.trdeg R S) : ℕ∞)
```

**`height_add_trdeg_residue_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DimensionFormula/GeneratorInduction.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DimensionFormula/GeneratorInduction.lean#L810). References: EGA IV (13.3.4), “special case”; EGA IV (5.5.6), “special case”; EGA IV (5.5.7), “special case”; EGA IV (5.6.5), “partial”.

> **Stacks 02IJ**.
> If in addition `R` is universally catenary, the dimension formula is an equality:
> `q.height + trdeg_{κ(p)} κ(q) = p.height + trdeg_R S`.

```lean
theorem height_add_trdeg_residue_eq
    [IsNoetherianRing R] [Algebra.FiniteType R S] [IsDomain R] [IsDomain S]
    (hinj : Function.Injective (algebraMap R S)) (hcat : IsUniversallyCatenary R)
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p] :
    letI := Ideal.ResidueField.algebraOfLiesOver p q
    q.height + (Cardinal.toNat (Algebra.trdeg p.ResidueField q.ResidueField) : ℕ∞)
      = p.height + (Cardinal.toNat (Algebra.trdeg R S) : ℕ∞)
```

## Tag 02MA, a lemma

[Tag 02MA](https://stacks.math.columbia.edu/tag/02MA) in the Stacks Project.

**`Ideal.primesOver_finite_and_forall_height_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Over/HeightOne.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/Over/HeightOne.lean#L325). The attribute's comment: “Finiteness of the induced extension of fraction fields is stated as `Algebra.IsAlgebraic A B`, to which it is equivalent for `B` of finite type over `A`; see the module docstring.”.

> **Generically finite maps are quasi-finite in codimension one.**
> Let `A ⊆ B` be an extension of domains with `A` Noetherian, `B` algebraic and of finite type over
> `A`, and let `p` be a prime of `A` of height one. Then only finitely many primes of `B` lie over
> `p`, and each of them has height one. Algebraicity of `B` over `A` is, under the finite type
> hypothesis, finiteness of the induced extension of fraction fields.

```lean
public theorem Ideal.primesOver_finite_and_forall_height_eq_one {A : Type*} [CommRing A]
    [IsNoetherianRing A] (p : Ideal A) [p.IsPrime] (B : Type*) [CommRing B] [IsDomain B]
    [Algebra A B] [FaithfulSMul A B] [Algebra.IsAlgebraic A B] [Algebra.FiniteType A B]
    (hp : p.height = 1) :
    (p.primesOver B).Finite ∧ ∀ q ∈ p.primesOver B, q.height = 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.113, Tag 02II](https://stacks.math.columbia.edu/tag/02II)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
