---
declaration: section
origin: cited
lean: StacksDraft.DerivedHom.evaluationToIteratedDerivedHom_isIso, StacksDraft.DerivedHom.evaluationToIteratedDerivedHom_isIso_of_truncLE_pseudoCoherent, Stacks.DerivedTensorHomDiagonal.isIso_derivedTensorHomDiagonal, Stacks.DerivedHom.KFlatHomComplex.homComplex_kFlat_and_represents_RHom
statement: formalized
proof: formalized
---

# 15.100 Some evaluation maps

Section 15.100 of the Stacks Project, [Tag 0ATJ](https://stacks.math.columbia.edu/tag/0ATJ). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A68, a lemma

[Tag 0A68](https://stacks.math.columbia.edu/tag/0A68) in the Stacks Project.

**`StacksDraft.DerivedHom.evaluationToIteratedDerivedHom_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation/Iterated.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation/Iterated.lean#L184).

> **Stacks 0A68.** The canonical evaluation morphism
> `RHom_R(L, M) ⊗ᴸ_R K ⟶ RHom_R(RHom_R(K, L), M)` is an isomorphism if `K` is
> perfect, or if `K` is pseudo-coherent, `L` is cohomologically bounded below, and `M` has
> finite injective dimension.

```lean
public theorem evaluationToIteratedDerivedHom_isIso
    (K L M : DerivedCategory (ModuleCat R))
    (h : StacksDraft.Perfect.IsPerfect K ∨
      (StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        DerivedCategoryB.IsBoundedBelow L ∧
        StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension M)) :
    let e := Classical.choose
      (exists_evaluationToIteratedDerivedHom (R := R))
    IsIso (e K L M)
```

## Tag 0A69, a lemma

[Tag 0A69](https://stacks.math.columbia.edu/tag/0A69) in the Stacks Project.

**`StacksDraft.DerivedHom.evaluationToIteratedDerivedHom_isIso_of_truncLE_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation/Iterated.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation/Iterated.lean#L583).

> **Stacks 0A69.** The canonical evaluation morphism
> `RHom_R(L, M) ⊗ᴸ_R K ⟶ RHom_R(RHom_R(K, L), M)` is an isomorphism if `L` and `M`
> have finite injective dimension, `RHom_R(L, M)` has finite Tor dimension, and every
> truncation `τ_{≤ n} K` is pseudo-coherent.

```lean
public theorem evaluationToIteratedDerivedHom_isIso_of_truncLE_pseudoCoherent
    (K L M : DerivedCategory (ModuleCat R))
    (hL : StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension L)
    (hM : StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension M)
    (hTor :
      let D := derivedHomAdjunction (R := R)
      ∃ a b : ℤ, ∀ (N : ModuleCat R) (i : ℤ), i ∉ Set.Icc a b →
        Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat R) i).obj
          (D.tensor.obj
            (D.hom.obj (Opposite.op L, M),
              (DerivedCategory.singleFunctor (ModuleCat R) 0).obj N))))
    (hK : ∀ n : ℤ, StacksDraft.PseudoCoherence.IsPseudoCoherent
      ((DerivedCategory.TStructure.t.truncLE n).obj K)) :
    let e := Classical.choose
      (exists_evaluationToIteratedDerivedHom (R := R))
    IsIso (e K L M)
```

## Tag 0ATK, a lemma

[Tag 0ATK](https://stacks.math.columbia.edu/tag/0ATK) in the Stacks Project.

**`Stacks.DerivedTensorHomDiagonal.isIso_derivedTensorHomDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation/TensorHom/PerfectAndCurrying.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation/TensorHom/PerfectAndCurrying.lean#L306). References: SGA 6 I (7.6), “affine case, E perfect”.

> **Stacks 0ATK.** The canonical derived tensor--Hom diagonal
> `K ⊗ᴸ RHom(M, L) ⟶ RHom(M, K ⊗ᴸ L)` is an isomorphism if `M` is perfect, if `K` is perfect, or
> if `M` is pseudo-coherent, `L` is bounded below and `K` has Tor amplitude in `[a, ∞]`.

```lean
public theorem isIso_derivedTensorHomDiagonal
    {R : Type u} [CommRing R]
    (K L M : DerivedCategory (ModuleCat.{u} R)) (a : ℤ)
    (h : StacksDraft.Perfect.IsPerfect M ∨ StacksDraft.Perfect.IsPerfect K ∨
      (StacksDraft.PseudoCoherence.IsPseudoCoherent M ∧
        (∃ b : ℤ, DerivedCategory.IsGE L b) ∧
        ∀ (N : ModuleCat.{u} R) (i : ℤ), i < a →
          IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
            ((((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R).tensor.obj K).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)))))) :
    IsIso (StacksDraft.DerivedHom.derivedTensorHomDiagonal K L M)
```

## Tag 0BYQ, a lemma

[Tag 0BYQ](https://stacks.math.columbia.edu/tag/0BYQ) in the Stacks Project.

**`Stacks.DerivedHom.KFlatHomComplex.homComplex_kFlat_and_represents_RHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Evaluation/KFlat.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/Evaluation/KFlat.lean#L395).

> **Stacks 0BYQ.** Let `P` be a bounded above cochain complex of projective `R`-modules which
> is perfect as an object of the derived category `D(R)`, and let `K` be a K-flat complex of
> `R`-modules.  Then `Hom^•(P, K)` is K-flat, and it represents `RHom_R(P, K)`: for every `n`, the
> map sending a degree-`n` cohomology class of `Hom^•(P, K)` to the corresponding morphism
> `P ⟶ K⟦n⟧` in `D(R)` is bijective.

```lean
theorem homComplex_kFlat_and_represents_RHom [HasDerivedCategory.{w} (ModuleCat.{u} R)]
    (P K : CochainComplex (ModuleCat.{u} R) ℤ) (d : ℤ) [P.IsStrictlyLE d]
    [∀ i, Module.Projective R (P.X i)]
    (hP : StacksDraft.Perfect.IsPerfect (DerivedCategory.Q.obj P)) (hK : K.KFlat) :
    (HomComplexR R P K).KFlat ∧
      ∀ n : ℤ, Function.Bijective
        (fun (c : CohomologyClass P K n) =>
          DerivedCategory.Qh.map (CohomologyClass.homAddEquiv c))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.100, Tag 0ATJ](https://stacks.math.columbia.edu/tag/0ATJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
