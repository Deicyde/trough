---
declaration: section
origin: cited
lean: Stacks.Examples.exists_formallyEtale_surjective_cotangentComplex_ne_zero
statement: formalized
proof: formalized
---

# 110.43 A formally étale ring map with nontrivial cotangent complex

Section 110.43 of the Stacks Project, [Tag 06E5](https://stacks.math.columbia.edu/tag/06E5). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06E6, a lemma

[Tag 06E6](https://stacks.math.columbia.edu/tag/06E6) in the Stacks Project.

**`Stacks.Examples.exists_formallyEtale_surjective_cotangentComplex_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FormallyEtaleCotangentComplexNonzero.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Algebra/FormallyEtaleCotangentComplexNonzero.lean#L156).

> **Stacks 06E6.** There exists a formally étale surjective ring map `A → B` with
> `L_{B/A} ≠ 0`: the cotangent complex `CommAlgCat.cotangentComplex A B` of Tag 08PN is not zero in
> the derived category `D(B)`, in every model of it, and indeed
> `H^{-2}(L_{B/A}) = H_2(L_{B/A}) ≠ 0`, as the source concludes. The example is that of
> `exists_formallyEtale_surjective_not_isZero_torTwo`, and the deduction is the source's:
> `Tor₂^A(B, B) ≠ 0`, `∧²_B(J/J²) = 0` because `J = J²`, and the five term exact sequence of
> Quillen's fundamental spectral sequence (Remark 08RG).

```lean
theorem exists_formallyEtale_surjective_cotangentComplex_ne_zero :
    ∃ (A : Type u) (_ : CommRing A) (B : CommAlgCat.{u} A),
      Algebra.FormallyEtale A B ∧ Function.Surjective (algebraMap A B) ∧
        (∀ [HasDerivedCategory.{w} (ModuleCat.{u} B)],
          ¬ IsZero (DerivedCategory.Q.obj (CommAlgCat.cotangentComplex.{u, u} A B))) ∧
        ¬ IsZero ((CommAlgCat.cotangentComplex.{u, u} A B).homology (-2))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.43, Tag 06E5](https://stacks.math.columbia.edu/tag/06E5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
