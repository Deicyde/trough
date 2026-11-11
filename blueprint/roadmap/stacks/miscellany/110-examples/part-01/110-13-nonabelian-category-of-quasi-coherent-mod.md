---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.not_nonempty_abelian_quasicoherentModules_padicCompletion, AlgebraicGeometry.FormalSpace.exists_isNoetherian_not_nonempty_abelian_quasicoherentModules
statement: formalized
proof: formalized
---

# 110.13 Nonabelian category of quasi-coherent modules

Section 110.13 of the Stacks Project, [Tag 0ALF](https://stacks.math.columbia.edu/tag/0ALF). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ALG, a lemma

[Tag 0ALG](https://stacks.math.columbia.edu/tag/0ALG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.not_nonempty_abelian_quasicoherentModules_padicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean#L142). The attribute's comment: “the source's example `Spf(ℤ_p)`, for every prime `p`”.

> **Stacks 0ALG, the source's example.** For a prime `p`, the formal spectrum
> `X = Spf(ℤ_p)` over `Spec ℤ` is a Noetherian affine formal algebraic space whose category of
> quasi-coherent modules (Stacks 06WG) admits no abelian structure: by Examples, Section 0ALF, it
> is the category of `p`-adically complete abelian groups, which is not abelian (Stacks 07JR).

```lean
theorem not_nonempty_abelian_quasicoherentModules_padicCompletion (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (.of (ULift.{u} ℤ)))) (hZp : B.Contains (Spec (.of (ULift.{u} ℤ_[p])))) :
    IsAffineFormalAlgebraicSpace B _ hZ (padicCompletion p B hZ hZp) ∧
      IsNoetherian B _ hZ (padicCompletion p B hZ hZp) ∧
      ¬ Nonempty (Abelian (FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} B _ hZ
        (completionFibred B _ hZ (specULiftZIsTerminal.from _) hZp
          (Ideal.span {(p : ULift.{u} ℤ_[p])})).p
        (isFiberedInGroupoids_completionFibred B _ hZ _ hZp _)))
```

**`AlgebraicGeometry.FormalSpace.exists_isNoetherian_not_nonempty_abelian_quasicoherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean#L164).

> **Stacks 0ALG.** The category of quasi-coherent modules on a formal algebraic space is not
> abelian in general, even for a Noetherian affine formal algebraic space: there is a big fppf
> site with a base scheme and a Noetherian affine formal algebraic space `X` over it — `Spf(ℤ_2)`
> over `Spec ℤ` — whose category of quasi-coherent modules (Stacks 06WG, on the category fibred in
> groupoids of `X`) admits no abelian structure.

```lean
theorem exists_isNoetherian_not_nonempty_abelian_quasicoherentModules :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (X : FppfSheaf B S hS),
      IsAffineFormalAlgebraicSpace B S hS X ∧ IsNoetherian B S hS X ∧
      ¬ Nonempty (Abelian (FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} B S hS
        (presheafOfGroupoids (X.obj ⋙ typeToGrpd)).p
        (isFiberedInGroupoids_presheafOfGroupoids _)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.13, Tag 0ALF](https://stacks.math.columbia.edu/tag/0ALF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
