---
declaration: section
origin: cited
lean: DifferentialGradedAlgebra.SystemProHom.isEquivalence_qcPullback, DifferentialGraded.nonempty_iso_of_proIsoDerived, Koszul.powBaseTensorBalanceDerivedObjIso, Koszul.nonempty_iso_of_isDerivedLimit_powBaseTensorBalance, Koszul.nonempty_iso_of_isDerivedLimit_powKoszulTensorBalance, Koszul.powProIsoDerived, Koszul.idealPowKoszulDerivedCompleteEquivalences, Koszul.nonempty_qcIdealPow_qcKoszul_derivedComplete_equivalences
statement: formalized
proof: formalized
---

# 24.35 Inverse systems of differential graded algebras

Section 24.35 of the Stacks Project, [Tag 0GZG](https://stacks.math.columbia.edu/tag/0GZG). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GZH, a lemma

[Tag 0GZH](https://stacks.math.columbia.edu/tag/0GZH) in the Stacks Project.

**`DifferentialGradedAlgebra.SystemProHom.isEquivalence_qcPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticProIsomorphism.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticProIsomorphism.lean#L414).

> **Stacks 0GZH.** **Let `(A_n)` and `(B_n)` be inverse systems of differential graded
> `R`-algebras, and let `φ : (A_n) → (B_n)` be a morphism of pro-objects, given by a representative
> `(m(·), A_{m(n)} → B_n)`. If `φ` is an isomorphism of pro-objects, then the functor
> `QC(𝒜) ⥤ QC(ℬ)` it induces is an equivalence.**
>
> Here the index category is a linearly ordered type `ι` with finite lower sets, the source's `ℕ`
> being an instance, `𝒜` and `ℬ` are the sheaves of differential graded algebras on the chaotic site
> `ι` with the constant sheaf of rings `R` attached to the two systems, and the functor is the
> derived pullback of Tag 0GZC along the morphism of chaotic sites given by the representative,
> restricted to the quasi-coherent objects of Definition 24.33.1. That `φ` is an isomorphism of
> pro-objects is `IsProIso`: a representative of a morphism of pro-objects in the other direction
> whose composites with `φ` agree with the transition maps after restriction to a further stage.

```lean
theorem isEquivalence_qcPullback (φ : SystemProHom A B) (hφ : φ.IsProIso) :
    φ.qcPullback.IsEquivalence
```

## Tag 0GZI, a lemma

[Tag 0GZI](https://stacks.math.columbia.edu/tag/0GZI) in the Stacks Project.

**`DifferentialGraded.nonempty_iso_of_proIsoDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InverseSystemProIsomorphism.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/InverseSystemProIsomorphism.lean#L372).

> **Stacks 0GZI.** Let `(A_n)` be an inverse system of differential graded algebras over `R`,
> let `(N_n)` and `(N'_n)` be inverse systems of left differential graded modules over it which are
> pro-isomorphic in the derived category, and let `(M_n)` be an inverse system of differential
> graded `(A_n, B)`-bimodules. Then the derived limits of the two towers
> `n ↦ M_n ⊗^𝐋_{A_n} N_n` and `n ↦ M_n ⊗^𝐋_{A_n} N'_n` of `D(B, d)` are isomorphic, although not
> canonically. With `B` concentrated in degree zero with `B^0 = R` this is the source's
> `R lim (M_n ⊗^𝐋_{A_n} N_n) = R lim (M_n ⊗^𝐋_{A_n} N'_n)` in `D(R)`.

```lean
theorem nonempty_iso_of_proIsoDerived {S : AlgebraSystem R}
    {B : DifferentialGradedAlgebra.{u, u} R} {N N' : ModuleSystem S} (p : ProIsoDerived N N')
    (M : BimoduleSystem S B)
    [HasProduct fun n : ℕ => (M.tower N).obj (op n)]
    [HasProduct fun n : ℕ => (M.tower N').obj (op n)] (K K' : derivedCategory' B)
    (hK : Pretriangulated.IsDerivedLimit (M.tower N) K)
    (hK' : Pretriangulated.IsDerivedLimit (M.tower N') K') :
    Nonempty (K ≅ K')
```

## Tag 0GZJ, a lemma

[Tag 0GZJ](https://stacks.math.columbia.edu/tag/0GZJ) in the Stacks Project.

**`Koszul.powBaseTensorBalanceDerivedObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/PowBaseTensorBalanceDerived.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/PowBaseTensorBalanceDerived.lean#L136). The attribute's comment: “the identification M\_n ⊗^𝐋\_R K\_t = M\_n ⊗^𝐋\_\{K\_n} (K\_n ⊗\_R K\_t), objectwise”.

> **The first step of the proof of Tag 0GZJ, one index at a time:**
> `M_m ⊗_{K_m}^𝐋 (K_m ⊗_R K_t) ≅ M_m ⊗_R^𝐋 K_t` in `D(B, d)`, for `m = b + k`.
>
> Both sides are computed by their plain tensor products, because `K_m ⊗_R K_t` and `K_t` are
> orthogonal on the left to the acyclic modules, and the plain tensor products are identified by
> `Koszul.powBaseTensorBalanceObjIso`.

```lean
def powBaseTensorBalanceDerivedObjIso (k : ℕ) :
    (powBaseTensorDerivedTensorTower f t hb bimod bimodTrans).obj k ≅
      (powBaseDegreeZeroDerivedTensorTower f t hb bimod bimodTrans).obj k
```

**`Koszul.nonempty_iso_of_isDerivedLimit_powBaseTensorBalance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/PowBaseTensorBalanceDerived.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/PowBaseTensorBalanceDerived.lean#L179). The attribute's comment: “the identification M\_n ⊗^𝐋\_R K\_t = M\_n ⊗^𝐋\_\{K\_n} (K\_n ⊗\_R K\_t), passed to R lim”.

> **The first step of the proof of Tag 0GZJ, passed to derived limits:**
> `R lim (M_m ⊗_R^𝐋 K_t) = R lim (M_m ⊗_{K_m}^𝐋 (K_m ⊗_R K_t))` in `D(B, d)`.
>
> The isomorphism is not canonical — a derived limit is pinned only up to a non-unique isomorphism
> — so the conclusion is stated for an arbitrary derived limit of each tower. This is Tag 0H9L
> applied to the pro-isomorphism `Koszul.powBaseTensorBalanceProIso`.
>
> Replacing `K_m ⊗_R K_t` by `K_t` on the right-hand side, which turns this into the statement of
> Tag 0GZJ, is the second step of the source's proof and is not done here.

```lean
theorem nonempty_iso_of_isDerivedLimit_powBaseTensorBalance
    [HasProduct fun k : ℕ =>
      (powBaseTensorDerivedTensorTower f t hb bimod bimodTrans).tower.obj (op k)]
    [HasProduct fun k : ℕ =>
      (powBaseDegreeZeroDerivedTensorTower f t hb bimod bimodTrans).tower.obj (op k)]
    (K K' : DifferentialGradedModule.derivedCategory' B)
    (hK : Pretriangulated.IsDerivedLimit
      (powBaseTensorDerivedTensorTower f t hb bimod bimodTrans).tower K)
    (hK' : Pretriangulated.IsDerivedLimit
      (powBaseDegreeZeroDerivedTensorTower f t hb bimod bimodTrans).tower K') :
    Nonempty (K ≅ K')
```

**`Koszul.nonempty_iso_of_isDerivedLimit_powKoszulTensorBalance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/PowKoszulDerivedLimit.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/PowKoszulDerivedLimit.lean#L155). The attribute's comment: “R lim (M\_n ⊗^𝐋\_R K\_t) = R lim (M\_n ⊗^𝐋\_\{K\_n} K\_t)”.

> Let `R` be a ring, let `f₁, …, f_r ∈ R` and let `K_n` be the Koszul complex on `f₁^n, …, f_r^n`
> viewed as a differential graded `R`-algebra. Let `(M_n)` be an object of `D(ℕ, (K_n))`. Then for
> every `t ≥ 1` `R lim (M_n ⊗_R^𝐋 K_t) = R lim (M_n ⊗_{K_n}^𝐋 K_t)`.
>
> The isomorphism is not canonical, so the conclusion is stated for an arbitrary derived limit of
> each tower. With `B` concentrated in degree zero with `B^0 = R` the target `D(B, d)` is the
> source's `D(R)`.

```lean
theorem nonempty_iso_of_isDerivedLimit_powKoszulTensorBalance
    [HasProduct fun n : ℕ => (M.tower (powRestrictedModuleSystem f ht)).obj (op n)]
    [HasProduct fun n : ℕ =>
      (powBaseDegreeZeroDerivedTensorTower f t ht M.obj bimodTrans).tower.obj (op n)]
    (K K' : derivedCategory' B)
    (hK : Pretriangulated.IsDerivedLimit (M.tower (powRestrictedModuleSystem f ht)) K)
    (hK' : Pretriangulated.IsDerivedLimit
      (powBaseDegreeZeroDerivedTensorTower f t ht M.obj bimodTrans).tower K') :
    Nonempty (K ≅ K')
```

**`Koszul.powProIsoDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/PowSystemsProIso.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/PowSystemsProIso.lean#L247). The attribute's comment: “the pro-isomorphism of (\{}\_nK\_t) with (K\_n ⊗\_R K\_t) in the derived category”.

> **The second step of the proof of Tag 0GZJ:** the system `({}_{t+n}K_t)` and the system
> `(K_{t+n} ⊗_R K_t)` of left differential graded modules over the Koszul algebras are
> pro-isomorphic in the derived category.
>
> The indices are the multiples of `t`, the comparison maps are those of Tag 0GZ7
> (`Koszul.powComparisonArrow`), the maps in the other direction are the multiplication maps, and
> the two composition identities are the two composites of Tag 0GZ7.

```lean
def powProIsoDerived :
    ProIsoDerived (powRestrictedModuleSystem f ht) (powBaseTensorModuleSystem f ht)
```

## Tag 0GZK, a proposition

[Tag 0GZK](https://stacks.math.columbia.edu/tag/0GZK) in the Stacks Project.

**`Koszul.idealPowKoszulDerivedCompleteEquivalences`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/NoetherianDerivedCompleteEquivalence.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/NoetherianDerivedCompleteEquivalence.lean#L57).

> **Stacks 0GZK.** Let `R` be a Noetherian ring and `I ⊆ R` an ideal, with generators
> `f₁, …, f_r`. Let `𝒜` be the sheaf of `R`-algebras on the chaotic site of the natural numbers of
> the inverse system `R / I ^ n`, and `ℬ` the sheaf of differential graded `R`-algebras of the
> inverse system of Koszul algebras on `f₁ ^ n, …, f_r ^ n` (both indexed so that the stage `n`
> carries the exponent `n + 1`). Then the three categories `QC(𝒜)`, `QC(ℬ)` and the full
> subcategory `D_comp(R, I)` of derived complete objects of `D(R)` are canonically equivalent:
> `QC(𝒜) ≌ QC(ℬ)` along the pro-isomorphisms of the quotient and Koszul–Tate systems and the
> quasi-isomorphism of the Tate resolution (Tags 0GZH, 0GZF, 0GZ5), and `QC(ℬ) ≌ D_comp(R, I)` by the
> derived global sections, with quasi-inverse `K ↦ K ⊗^𝐋_R ℬ`.

```lean
def idealPowKoszulDerivedCompleteEquivalences [IsNoetherianRing R] (I : Ideal R) {r : ℕ}
    (f : Fin r → R) (generators : Ideal.span (Set.range f) = I) :
    ((Chaotic.QC (liftedIdealPowSheafAlgebra.{u} I)).FullSubcategory ≌
      (Chaotic.QC (liftedPowSheafAlgebra.{u} f)).FullSubcategory) ×
    ((Chaotic.QC (liftedPowSheafAlgebra.{u} f)).FullSubcategory ≌
      (derivedCompleteObjects I).FullSubcategory)
```

## Tag 0H1E, a remark

[Tag 0H1E](https://stacks.math.columbia.edu/tag/0H1E) in the Stacks Project.

**`Koszul.nonempty_qcIdealPow_qcKoszul_derivedComplete_equivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/WeaklyProregularDerivedComplete.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/WeaklyProregularDerivedComplete.lean#L81).

> **Stacks 0H1E.** Let `R` be a ring and let `f₁, …, f_r` be a weakly proregular sequence
> generating the ideal `I`. Then the arguments of the proof of Proposition 0GZK continue to work:
> the three categories `QC({R / I ^ n})` (the sheaf of algebras `𝒜 = (R / I ^ n)` on `ℕ` with the
> chaotic topology), `QC(ℬ)` (the sheaf `ℬ` of Koszul algebras on `f₁ ^ n, …, f_r ^ n`) and the
> category `D_comp(R, I)` of derived complete objects of `D(R)` are equivalent, as `R`-linear
> triangulated categories: `QC(𝒜) ≃ QC(ℬ)` and `QC(ℬ) ≃ D_comp(R, I)`, and hence
> `QC(𝒜) ≃ D_comp(R, I)`.

```lean
theorem nonempty_qcIdealPow_qcKoszul_derivedComplete_equivalences (I : Ideal R) {r : ℕ}
    (f : Fin r → R) (proregular : IsWeaklyProregular f)
    (generators : Ideal.span (Set.range f) = I) :
    Nonempty (LinearTriangulatedEquivalence R
        (Chaotic.QC (liftedIdealPowSheafAlgebra.{u} I)).FullSubcategory
        (Chaotic.QC (liftedPowSheafAlgebra.{u} f)).FullSubcategory) ∧
      Nonempty (LinearTriangulatedEquivalence R
        (Chaotic.QC (liftedPowSheafAlgebra.{u} f)).FullSubcategory
        (ObjectProperty.FullSubcategory
          (fun K : DerivedCategory (ModuleCat.{u} R) => IsDerivedComplete I K))) ∧
      Nonempty (LinearTriangulatedEquivalence R
        (Chaotic.QC (liftedIdealPowSheafAlgebra.{u} I)).FullSubcategory
        (ObjectProperty.FullSubcategory
          (fun K : DerivedCategory (ModuleCat.{u} R) => IsDerivedComplete I K)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.35, Tag 0GZG](https://stacks.math.columbia.edu/tag/0GZG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
