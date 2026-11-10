---
declaration: section
origin: cited
lean: Stacks.Examples.exists_formallyEtale_surjective_mulKernel_ne_bot, Stacks.Examples.exists_formallyEtale_surjective_not_isZero_torTwo
statement: formalized
proof: formalized
---

# 110.43 A formally étale ring map with nontrivial cotangent complex

Section 110.43 of the Stacks Project, [Tag 06E5](https://stacks.math.columbia.edu/tag/06E5). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06E6, a lemma

[Tag 06E6](https://stacks.math.columbia.edu/tag/06E6) in the Stacks Project.

**`Stacks.Examples.exists_formallyEtale_surjective_mulKernel_ne_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FormallyEtaleNontrivialCotangent.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FormallyEtaleNontrivialCotangent.lean#L245). The attribute's comment: “the example: a formally étale surjection with Ker(J ⊗_A J → J²) ≠ 0”.

> **Stacks 06E6**, the example. There is a formally étale surjective map of commutative rings
> `A → B` whose kernel `J` has `Ker(J ⊗_A J → J²) ≠ 0`; equivalently, `J` is idempotent but not
> weakly regular.

```lean
theorem exists_formallyEtale_surjective_mulKernel_ne_bot :
    ∃ (A : Type u) (_ : CommRing A) (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      Algebra.FormallyEtale A B ∧ Function.Surjective (algebraMap A B) ∧
        LinearMap.ker (Submodule.mulMap' (RingHom.ker (algebraMap A B))
          (RingHom.ker (algebraMap A B))) ≠ ⊥
```

**`Stacks.Examples.exists_formallyEtale_surjective_not_isZero_torTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FormallyEtaleNontrivialCotangent.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FormallyEtaleNontrivialCotangent.lean#L261). The attribute's comment: “the example: a formally étale surjection with Tor₂^A(B, B) ≠ 0”.

> **Stacks 06E6**, the example, with the nonvanishing read on `Tor₂`. There is a formally étale
> surjective map of commutative rings `A → B` with `Tor₂^A(B, B) ≠ 0`. By Tag 09D6 this is the same
> statement as `exists_formallyEtale_surjective_mulKernel_ne_bot`; it is the input from which the
> source deduces, via the five-term exact sequence of Quillen's spectral sequence, that
> `L_{B/A} ≠ 0`.

```lean
theorem exists_formallyEtale_surjective_not_isZero_torTwo :
    ∃ (A : Type u) (_ : CommRing A) (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      Algebra.FormallyEtale A B ∧ Function.Surjective (algebraMap A B) ∧
        ¬ IsZero (((Tor' (ModuleCat.{u} A) 2).obj (ModuleCat.of A B)).obj
          (ModuleCat.of A B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.43, Tag 06E5](https://stacks.math.columbia.edu/tag/06E5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
