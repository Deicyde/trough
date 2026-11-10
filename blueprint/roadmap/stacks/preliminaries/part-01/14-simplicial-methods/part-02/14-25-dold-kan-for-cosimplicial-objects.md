---
declaration: section
origin: cited
lean: AlgebraicTopology.exists_normalizedCochainComplex
statement: formalized
proof: formalized
---

# 14.25 Dold-Kan for cosimplicial objects

Section 14.25 of the Stacks Project, [Tag 019H](https://stacks.math.columbia.edu/tag/019H). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 019I, a lemma

[Tag 019I](https://stacks.math.columbia.edu/tag/019I) in the Stacks Project.

**`AlgebraicTopology.exists_normalizedCochainComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/DoldKan/Cosimplicial.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/DoldKan/Cosimplicial.lean#L450). References: SGA 4 XVII (5.5.3), “Dold–Puppe equivalence”; SGA 4½ Fonctions L (1.4), “N is an equivalence”.

> **Stacks 019I**.
> Let `A` be an abelian category. (1) The Moore cochain complex functor
> `s : CoSimp(A) ⥤ CoCh_{≥0}(A)` is exact. (2) There is a functor `Q`, the normalized cochain
> complex, together with a natural transformation `π : s ⟶ Q` which is an isomorphism in degree `0`
> and, in degree `n + 1`, a cokernel of the cofaces `δ i : Uₙ ⟶ Uₙ₊₁`, `i ≤ n`. (3) `π` is a split
> epimorphism in the functor category, which is the functorial direct sum decomposition
> `s(U) = D(U) ⊕ Q(U)` with `D = ker π`. (4) `Q` is exact. (5) Each `π.app U` is a quasi-isomorphism.
> (6) `Q` is an equivalence of categories.

```lean
public theorem exists_normalizedCochainComplex :
    (PreservesFiniteLimits (alternatingCofaceMapComplex A) ∧
      PreservesFiniteColimits (alternatingCofaceMapComplex A)) ∧
    ∃ (Q : CosimplicialObject A ⥤ CochainComplex A ℕ)
      (π : alternatingCofaceMapComplex A ⟶ Q),
      (∀ U : CosimplicialObject A, IsIso ((π.app U).f 0)) ∧
      (∀ (U : CosimplicialObject A) (n : ℕ),
        ∃ e : cokernel (Sigma.desc (f := fun _ : Fin (n + 1) => U.obj ⦋n⦌)
            fun i => U.δ i.castSucc) ≅ (Q.obj U).X (n + 1),
          cokernel.π _ ≫ e.hom = (π.app U).f (n + 1)) ∧
      IsSplitEpi π ∧
      (PreservesFiniteLimits Q ∧ PreservesFiniteColimits Q) ∧
      (∀ U : CosimplicialObject A, QuasiIso (π.app U)) ∧
      Q.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.25, Tag 019H](https://stacks.math.columbia.edu/tag/019H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
