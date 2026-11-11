---
declaration: section
origin: cited
lean: Ideal.exists_mem_ideal_transcendental_residue, AlgebraicGeometry.eventually_topologicalKrullDim_fiber_specMapAeval_pow_add_le, Algebra.exists_quasiFinite_mvPolynomial_of_relativeDimension_le, Algebra.exists_quasiFinite_mvPolynomial_of_relativeDimension_eq
statement: formalized
proof: formalized
---

# 37.31 Weak relative Noether normalization

Section 37.31 of the Stacks Project, [Tag 0GTD](https://stacks.math.columbia.edu/tag/0GTD). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GTE, a lemma

[Tag 0GTE](https://stacks.math.columbia.edu/tag/0GTE) in the Stacks Project.

**`Ideal.exists_mem_ideal_transcendental_residue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/NoetherNormalization.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/NoetherNormalization.lean#L34).

> An ideal avoiding finitely many incomparable prime ideals contains an element whose image is
> transcendental over each of the prescribed subfields of the residue fields.

```lean
theorem exists_mem_ideal_transcendental_residue
    (R : Type*) [CommRing R] (ι : Type*) [Finite ι]
    (p : ι → PrimeSpectrum R)
    (k : ∀ i, Subfield (p i).asIdeal.ResidueField)
    (hinc : ∀ i j, i ≠ j → ¬ (p i).asIdeal ≤ (p j).asIdeal)
    (htrans : ∀ i, ¬ Algebra.IsAlgebraic (k i) (p i).asIdeal.ResidueField)
    (J : Ideal R) (hJ : ∀ i, ¬ J ≤ (p i).asIdeal) :
    ∃ x ∈ J, ∀ i, Transcendental (k i)
      (algebraMap R (p i).asIdeal.ResidueField x)
```

## Tag 0GTF, a lemma

[Tag 0GTF](https://stacks.math.columbia.edu/tag/0GTF) in the Stacks Project.

**`AlgebraicGeometry.eventually_topologicalKrullDim_fiber_specMapAeval_pow_add_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/EventualFibreDimension.lean, line 2905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/EventualFibreDimension.lean#L2905).

> **Stacks Project, Tag 0GTF.** If the morphism to the affine line determined by `a` has
> fibres of dimension at most `d`, then so does the morphism determined by `a ^ n + b`, for every
> sufficiently large exponent `n`.

```lean
public theorem eventually_topologicalKrullDim_fiber_specMapAeval_pow_add_le
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (d : ℕ) (a b : S)
    (ha : ∀ q : Spec (.of (Polynomial R)),
      topologicalKrullDim ((specMapAeval a).fiber q) ≤ (d : WithBot ℕ∞)) :
    ∃ n₀ : ℕ, ∀ n : ℕ, n₀ ≤ n →
      ∀ q : Spec (.of (Polynomial R)),
        topologicalKrullDim ((specMapAeval (a ^ n + b)).fiber q) ≤
          (d : WithBot ℕ∞)
```

## Tag 0GTG, a lemma

[Tag 0GTG](https://stacks.math.columbia.edu/tag/0GTG) in the Stacks Project.

**`Algebra.exists_quasiFinite_mvPolynomial_of_relativeDimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/WeakRelativeNoetherNormalization.lean, line 1145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/WeakRelativeNoetherNormalization.lean#L1145). The attribute's comment: “The maximum of the dimensions of the fibres is `Algebra.relativeDimension R S` (Tag 00QD) and is bounded by, rather than equal to, the natural number `d`; the two are equivalent, and the inequality is what covers `Spec S = ∅`, where the maximum is `⊥`. Quasi-finiteness is Mathlib's `RingHom.QuasiFinite`, which asks only for finite fibres, so the finite type of the map is a separate conjunct.”.

> **Stacks Project, Tag 0GTG.** Let `R → S` be a finite type ring map and let `d` bound the
> maximum `Algebra.relativeDimension R S` of the dimensions of the fibres of `Spec S → Spec R`.
> Then there is a quasi-finite `R`-algebra map `R[t_1, …, t_d] → S`.

```lean
public theorem exists_quasiFinite_mvPolynomial_of_relativeDimension_le
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (d : ℕ)
    (hd : Algebra.relativeDimension R S ≤ (d : WithBot ℕ∞)) :
    ∃ φ : MvPolynomial (Fin d) R →ₐ[R] S,
      φ.toRingHom.FiniteType ∧ φ.toRingHom.QuasiFinite
```

**`Algebra.exists_quasiFinite_mvPolynomial_of_relativeDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/WeakRelativeNoetherNormalization.lean, line 1160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/WeakRelativeNoetherNormalization.lean#L1160). The attribute's comment: “The source's form, with `d` equal to the maximum `Algebra.relativeDimension R S` (Tag 00QD) of the dimensions of the fibres. Quasi-finiteness is Mathlib's `RingHom.QuasiFinite`, which asks only for finite fibres, so the finite type of the map is a separate conjunct.”.

> **Stacks Project, Tag 0GTG**, in the source's form: `d` *is* the maximum of the dimensions of
> the fibres of `Spec S → Spec R`.

```lean
public theorem exists_quasiFinite_mvPolynomial_of_relativeDimension_eq
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (d : ℕ)
    (hd : Algebra.relativeDimension R S = (d : WithBot ℕ∞)) :
    ∃ φ : MvPolynomial (Fin d) R →ₐ[R] S,
      φ.toRingHom.FiniteType ∧ φ.toRingHom.QuasiFinite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.31, Tag 0GTD](https://stacks.math.columbia.edu/tag/0GTD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
