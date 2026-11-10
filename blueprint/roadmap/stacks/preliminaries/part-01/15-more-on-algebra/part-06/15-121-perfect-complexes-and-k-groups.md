---
declaration: section
origin: cited
lean: K0.exists_eulerChar_perfect, K0.exists_k0_perfectDerivedCategory_addEquiv
statement: formalized
proof: formalized
---

# 15.121 Perfect complexes and K-groups

Section 15.121 of the Stacks Project, [Tag 0FJG](https://stacks.math.columbia.edu/tag/0FJG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AFY, a lemma

[Tag 0AFY](https://stacks.math.columbia.edu/tag/0AFY) in the Stacks Project.

**`K0.exists_eulerChar_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PerfectComplex.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/PerfectComplex.lean#L675). References: SGA 6 0 (3.1), “special case”.

> **Stacks 0AFY.** Perfect complexes over `R` have an Euler characteristic in `K₀(R)` which
> changes by `(-1)ⁿ` under a shift by `n`, is additive in distinguished triangles, and is the
> alternating sum of the classes of the terms of every bounded finite-projective representative.

```lean
public theorem K0.exists_eulerChar_perfect (R : Type u) [CommRing R]
    [HasDerivedCategory.{w} (ModuleCat.{u} R)] :
    ∃ c : {K : DerivedCategory (ModuleCat.{u} R) // StacksDraft.Perfect.IsPerfect K} → K0 R,
      (∀ (K : DerivedCategory (ModuleCat.{u} R)) (hK : StacksDraft.Perfect.IsPerfect K) (n : ℤ),
        ∃ hKn : StacksDraft.Perfect.IsPerfect (K⟦n⟧),
          c ⟨K⟦n⟧, hKn⟩ = (n.negOnePow : ℤ) • c ⟨K, hK⟩) ∧
      (∀ (T : Triangle (DerivedCategory (ModuleCat.{u} R))),
        T ∈ distTriang (DerivedCategory (ModuleCat.{u} R)) →
        ∀ (h₁ : StacksDraft.Perfect.IsPerfect T.obj₁) (h₂ : StacksDraft.Perfect.IsPerfect T.obj₂)
          (h₃ : StacksDraft.Perfect.IsPerfect T.obj₃),
          c ⟨T.obj₂, h₂⟩ = c ⟨T.obj₁, h₁⟩ + c ⟨T.obj₃, h₃⟩) ∧
      (∀ (K : DerivedCategory (ModuleCat.{u} R)) (hK : StacksDraft.Perfect.IsPerfect K)
        (P : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ),
        P.IsStrictlyGE a → P.IsStrictlyLE b →
        (hfinite : ∀ i : ℤ, Module.Finite R (P.X i)) →
        (hprojective : ∀ i : ℤ, Module.Projective R (P.X i)) →
        Nonempty (K ≅ DerivedCategory.Q.obj P) →
        c ⟨K, hK⟩ = ∑ i ∈ Finset.Icc a b,
          (i.negOnePow : ℤ) • K0.mk
            ({ carrier := P.X i, finite := hfinite i, projective := hprojective i } : FGProj R))
```

## Tag 0FCU, a lemma

[Tag 0FCU](https://stacks.math.columbia.edu/tag/0FCU) in the Stacks Project.

**`K0.exists_k0_perfectDerivedCategory_addEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PerfectDerivedCategory.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/PerfectDerivedCategory.lean#L505).

> **Stacks 0FCU.** Euler characteristic induces an additive equivalence from the zeroth
> K-group of the perfect derived category of `R` to the zeroth K-group of finite projective
> `R`-modules. On a bounded finite-projective representative it is the alternating sum of the
> classes of its terms.

```lean
public theorem K0.exists_k0_perfectDerivedCategory_addEquiv (R : Type u) [CommRing R] :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} R)) :=
      (ObjectProperty.singleton
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
          (ModuleCat.of R R))).triangEnvelope
    ∃ e : CategoryTheory.Pretriangulated.K0 P.FullSubcategory ≃+ K0 R,
      ∀ (K : P.FullSubcategory)
        (Q : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ),
        Q.IsStrictlyGE a → Q.IsStrictlyLE b →
        (hfinite : ∀ i : ℤ, Module.Finite R (Q.X i)) →
        (hprojective : ∀ i : ℤ, Module.Projective R (Q.X i)) →
        Nonempty (K.obj ≅ DerivedCategory.Q.obj Q) →
        e (CategoryTheory.Pretriangulated.K0.cls K) = ∑ i ∈ Finset.Icc a b,
          (i.negOnePow : ℤ) • K0.mk
            ({ carrier := Q.X i, finite := hfinite i, projective := hprojective i } : FGProj R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.121, Tag 0FJG](https://stacks.math.columbia.edu/tag/0FJG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
