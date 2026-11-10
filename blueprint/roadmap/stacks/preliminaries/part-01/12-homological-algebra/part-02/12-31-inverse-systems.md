---
declaration: section
origin: cited
lean: inverseSystem_preadditive, inverseSystem_hasFiniteBiproducts, inverseSystem_abelian, inverseSystem_shortComplex_exact_iff, IsMittagLefflerCategorical, Ab.mono_lim_map_and_exact_of_shortExact, Ab.isMittagLeffler_X₃_of_shortExact, Ab.shortExact_lim_of_isMittagLeffler
statement: formalized
proof: formalized
---

# 12.31 Inverse systems

Section 12.31 of the Stacks Project, [Tag 02MY](https://stacks.math.columbia.edu/tag/02MY). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02MZ, a lemma

[Tag 02MZ](https://stacks.math.columbia.edu/tag/02MZ) in the Stacks Project.

**`inverseSystem_preadditive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean#L46). The attribute's comment: “(1) preadditive”.

> **Stacks 02MZ (1), preadditive.** If `C` is preadditive, then so is the
> category of inverse systems in `C`.

```lean
noncomputable def inverseSystem_preadditive
    (C : Type*) [Category C] [Preadditive C] : Preadditive (InverseSystemCategoricalFunctorial C)
```

**`inverseSystem_hasFiniteBiproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean#L53). The attribute's comment: “(1) biproducts”.

> **Stacks 02MZ (1), biproducts.** If `C` is preadditive with finite
> biproducts, then the category of inverse systems in `C` has finite biproducts.

```lean
theorem inverseSystem_hasFiniteBiproducts
    (C : Type*) [Category C] [Preadditive C] [HasFiniteBiproducts C] :
    HasFiniteBiproducts (InverseSystemCategoricalFunctorial C)
```

**`inverseSystem_abelian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean#L61). The attribute's comment: “(2) abelian”.

> **Stacks 02MZ (2), abelian.** If `C` is an abelian category, then the
> category of inverse systems in `C` is abelian.

```lean
noncomputable def inverseSystem_abelian
    (C : Type*) [Category C] [Abelian C] : Abelian (InverseSystemCategoricalFunctorial C)
```

**`inverseSystem_shortComplex_exact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean#L69). The attribute's comment: “(2) exactness”. References: SGA 3 I (5.2), “partial”.

> **Stacks 02MZ (2), exactness.** A short complex `(Kᵢ) → (Lᵢ) → (Mᵢ)` of
> inverse systems over an abelian category is exact if and only if its evaluation
> at every index `i` (i.e. `Kᵢ → Lᵢ → Mᵢ`) is exact.

```lean
theorem inverseSystem_shortComplex_exact_iff
    (C : Type*) [Category C] [Abelian C] (S : ShortComplex (InverseSystemCategoricalFunctorial C)) :
    S.Exact ↔ ∀ (i : ℕᵒᵖ), (S.map ((evaluation ℕᵒᵖ C).obj i)).Exact
```

## Tag 02N0, a definition

[Tag 02N0](https://stacks.math.columbia.edu/tag/02N0) in the Stacks Project.

**`IsMittagLefflerCategorical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/InverseSystem.lean#L107). References: EGA 0 (13.1.2), “ℕ-indexed systems”; EGA III (4.1.7); SGA 4½ Rapport (4.11).

> **Stacks Tag 02N0.** The inverse system `F : ℕᵒᵖ ⥤ C` over an abelian
> category satisfies the *Mittag-Leffler condition* if for every `i` there exists
> `c = c(i) ≥ i` such that `Im(A_k → A_i) = Im(A_c → A_i)` for all `k ≥ c`.

```lean
def IsMittagLefflerCategorical (F : ℕᵒᵖ ⥤ C) : Prop
```

## Tag 02N1, a lemma

[Tag 02N1](https://stacks.math.columbia.edu/tag/02N1) in the Stacks Project.

**`Ab.mono_lim_map_and_exact_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L379). The attribute's comment: “left_exact”.

> Part (1): for any short exact sequence of inverse systems, the limit
> sequence `0 → lim A → lim B → lim C` is exact.

```lean
theorem Ab.mono_lim_map_and_exact_of_shortExact
    (S : ShortComplex (ℕᵒᵖ ⥤ Ab.{u})) (h : S.ShortExact) :
    Mono (S.map (lim : (ℕᵒᵖ ⥤ Ab.{u}) ⥤ Ab.{u})).f ∧
      (S.map (lim : (ℕᵒᵖ ⥤ Ab.{u}) ⥤ Ab.{u})).Exact
```

**`Ab.isMittagLeffler_X₃_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L389). The attribute's comment: “ML_quotient”. References: EGA 0 (13.2.1), “(i), systems over ℕ”; SGA 5 V (2.1.2), “(i)”.

> Part (2): a quotient of a Mittag-Leffler inverse system is Mittag-Leffler.

```lean
theorem Ab.isMittagLeffler_X₃_of_shortExact
    (S : ShortComplex (ℕᵒᵖ ⥤ Ab.{u})) (h : S.ShortExact)
    (hB : (S.X₂ ⋙ forget Ab).IsMittagLeffler) : (S.X₃ ⋙ forget Ab).IsMittagLeffler
```

**`Ab.shortExact_lim_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L399). The attribute's comment: “ML_short_exact”. References: EGA 0 (13.2.2), “systems over ℕ”.

> Part (3): if the kernel system is Mittag-Leffler, then the limit sequence
> `0 → lim A → lim B → lim C → 0` is short exact.

```lean
theorem Ab.shortExact_lim_of_isMittagLeffler
    (S : ShortComplex (ℕᵒᵖ ⥤ Ab.{u})) (h : S.ShortExact)
    (hA : (S.X₁ ⋙ forget Ab).IsMittagLeffler) :
    (S.map (lim : (ℕᵒᵖ ⥤ Ab.{u}) ⥤ Ab.{u})).ShortExact
```

**`ModuleCat.shortExact_lim_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L490). The attribute's comment: “ML_short_exact, for towers of modules”. References: EGA 0 (13.2.2), “ℕ-indexed systems”; EGA III (4.1.7.21), “more general”.

> Stacks 02N1 part (3) for towers of modules: if the kernel system is Mittag-Leffler, then the
> limit sequence `0 → lim A → lim B → lim C → 0` is short exact. This is
> `CategoryTheory.ShortComplex.shortExact_map_lim_of_isMittagLeffler` with the pointwise short
> exactness obtained from short exactness in the functor category, evaluation being exact.

```lean
theorem ModuleCat.shortExact_lim_of_isMittagLeffler {R : Type u} [Ring R]
    (S : ShortComplex (ℕᵒᵖ ⥤ ModuleCat.{v} R)) (h : S.ShortExact)
    (hA : (S.X₁ ⋙ forget (ModuleCat.{v} R)).IsMittagLeffler) :
    (S.map (lim : (ℕᵒᵖ ⥤ ModuleCat.{v} R) ⥤ ModuleCat.{v} R)).ShortExact
```

**`ModuleCat.isMittagLeffler_X₃_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L500). The attribute's comment: “ML_quotient, for towers of modules”.

> Stacks 02N1 part (2) for towers of modules: a quotient of a Mittag-Leffler inverse system is
> Mittag-Leffler.

```lean
theorem ModuleCat.isMittagLeffler_X₃_of_shortExact {R : Type u} [Ring R]
    (S : ShortComplex (ℕᵒᵖ ⥤ ModuleCat.{v} R)) (h : S.ShortExact)
    (hB : (S.X₂ ⋙ forget (ModuleCat.{v} R)).IsMittagLeffler) :
    (S.X₃ ⋙ forget (ModuleCat.{v} R)).IsMittagLeffler
```

## Tag 070B, a lemma

[Tag 070B](https://stacks.math.columbia.edu/tag/070B) in the Stacks Project.

**`Ab.exact_lim_map_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L472). References: EGA 0 (13.2.2), “partial”.

> Let `A → B → C → D` be an exact sequence of inverse systems of abelian groups indexed by
> `ℕ`. If `A` satisfies the Mittag-Leffler condition, then the induced sequence on inverse limits
> `lim B → lim C → lim D` is exact at `lim C`.
>
> The proof is the source's: `ψ` factors through `K = Ker(χ)` by an epimorphism `ψ'`, whose kernel
> is a quotient of `A`, hence Mittag-Leffler (02N1); so `lim B → lim K` is onto (02N1), and
> `lim K = Ker(lim χ)` because `lim` preserves kernels.

```lean
theorem Ab.exact_lim_map_of_isMittagLeffler {A B C D : ℕᵒᵖ ⥤ Ab.{u}} (φ : A ⟶ B) (ψ : B ⟶ C)
    (χ : C ⟶ D)
    (hφψ : φ ≫ ψ = 0) (hψχ : ψ ≫ χ = 0)
    (hAB : (ShortComplex.mk φ ψ hφψ).Exact) (hBC : (ShortComplex.mk ψ χ hψχ).Exact)
    (hML : (A ⋙ forget Ab).IsMittagLeffler) :
    (ShortComplex.mk (lim.map ψ) (lim.map χ)
      (by rw [← lim.map_comp, hψχ, Functor.map_zero])).Exact
```

**`ModuleCat.exact_lim_map_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L518). The attribute's comment: “for towers of modules”. References: EGA 0 (13.2.2), “partial”.

> **Stacks 070B for towers of modules.** Let `A → B → C → D` be an exact sequence of inverse
> systems of `R`-modules indexed by `ℕ`. If `A` satisfies the Mittag-Leffler condition, then the
> induced sequence on inverse limits `lim B → lim C → lim D` is exact at `lim C`.
>
> This is the same argument as `Ab.exact_lim_map_of_isMittagLeffler`, run with the two inputs for
> towers of modules: `ψ` factors through `K = Ker(χ)` by an epimorphism `ψ'`, whose kernel is a
> quotient of `A`, hence Mittag-Leffler; so `lim B → lim K` is onto, and `lim K = Ker(lim χ)`
> because `lim` preserves kernels.

```lean
theorem ModuleCat.exact_lim_map_of_isMittagLeffler {R : Type u} [Ring R]
    {A B C D : ℕᵒᵖ ⥤ ModuleCat.{v} R} (φ : A ⟶ B) (ψ : B ⟶ C) (χ : C ⟶ D)
    (hφψ : φ ≫ ψ = 0) (hψχ : ψ ≫ χ = 0)
    (hAB : (ShortComplex.mk φ ψ hφψ).Exact) (hBC : (ShortComplex.mk ψ χ hψχ).Exact)
    (hML : (A ⋙ forget (ModuleCat.{v} R)).IsMittagLeffler) :
    (ShortComplex.mk (lim.map ψ) (lim.map χ)
      (by rw [← lim.map_comp, hψχ, Functor.map_zero])).Exact
```

## Tag 070C, a lemma

[Tag 070C](https://stacks.math.columbia.edu/tag/070C) in the Stacks Project.

**`essentially_constant_iff_direct_sum_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean#L562).

> For a directed preorder `ι` and an inverse system `F : ιᵒᵖ ⥤ 𝓐` in an
> abelian category with a limit cone `c`, the system is essentially constant if
> and only if there is an index `i₀` admitting a compatible direct-sum
> decomposition with eventually-vanishing `Z`-summand.

```lean
theorem essentially_constant_iff_direct_sum_decomposition
    [IsDirected ι (· ≤ ·)]
    (F : ιᵒᵖ ⥤ 𝓐) (c : Cone F) (_hc : IsLimit c) :
    (∃ (i : ιᵒᵖ) (s : F.obj i ⟶ c.pt),
        EssentiallyConstantPro.IsEssentiallyConstantWith F c i s) ↔
      HasDirectSumDecomposition F c
```

## Tag 070D, a lemma

[Tag 070D](https://stacks.math.columbia.edu/tag/070D) in the Stacks Project.

**`isMittagLeffler_forget_iff_of_isEssentiallyConstantPro`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L707).

> Let `0 → (A_i) → (B_i) → (C_i) → 0` be a short exact sequence of inverse
> systems of abelian groups indexed by a cofiltered category `J`. If `(C_i)` is
> essentially constant, then `(A_i)` has the Mittag-Leffler property iff
> `(B_i)` does.

```lean
theorem isMittagLeffler_forget_iff_of_isEssentiallyConstantPro
    {J : Type*} [Category J] [IsCofiltered J]
    (S : ShortComplex (J ⥤ Ab))
    (hS : S.ShortExact)
    (hC : EssentiallyConstantPro.IsEssentiallyConstantPro S.X₃) :
    (S.X₁ ⋙ forget Ab).IsMittagLeffler ↔ (S.X₂ ⋙ forget Ab).IsMittagLeffler
```

## Tag 070E, a lemma

[Tag 070E](https://stacks.math.columbia.edu/tag/070E) in the Stacks Project.

**`isIso_comparisonHomologyLimit_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InverseLimit.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InverseLimit.lean#L534). References: EGA 0 (13.2.3), “special case”.

> For a countable inverse system of 4-term complexes of abelian groups, if
> `(A^{-2}_i)` and `(A^{-1}_i)` are Mittag-Leffler and
> `(H^{-1}_i)` is essentially constant, then the comparison morphism from the
> `0`-cohomology of the limit complex to the limit of the `0`-cohomologies is an
> isomorphism.

```lean
theorem isIso_comparisonHomologyLimit_of_isMittagLeffler
    (A_neg2 A_neg1 A_0 A_1 : ℕᵒᵖ ⥤ Ab.{v})
    (d_neg2 : A_neg2 ⟶ A_neg1) (d_neg1 : A_neg1 ⟶ A_0) (d_0 : A_0 ⟶ A_1)
    (h_neg1 : ∀ i, d_neg2.app i ≫ d_neg1.app i = 0)
    (h_0 : ∀ i, d_neg1.app i ≫ d_0.app i = 0)
    (hML_neg2 : (A_neg2 ⋙ forget Ab).IsMittagLeffler)
    (hML_neg1 : (A_neg1 ⋙ forget Ab).IsMittagLeffler)
    (hEC : EssentiallyConstantPro.IsEssentiallyConstantPro
      (homologyInvSystem d_neg2 d_neg1 h_neg1)) :
    IsIso (comparisonHomologyLimit d_neg1 d_0 h_0)
```

## Tag 0AAT, a lemma

[Tag 0AAT](https://stacks.math.columbia.edu/tag/0AAT) in the Stacks Project.

**`acyclic_limit_of_acyclic_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/InverseLimit.lean, line 922](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/InverseLimit.lean#L922).

> Let `α` be an ordinal and `K` an inverse system of cochain complexes of
> abelian groups over `α`. If every `K_β` is acyclic and the comparison map
> `K^n_β → lim_{γ < β} K^n_γ` is surjective for every `β` and `n`, then the
> limit complex `lim_{β < α} K_β` is acyclic.

```lean
theorem acyclic_limit_of_acyclic_of_surjective (α : Ordinal.{u})
    (K : (α.ToType)ᵒᵖ ⥤ CochainComplex AddCommGrpCat.{u} ℤ)
    (hAcyclic : ∀ β : α.ToType, (K.obj (op β)).Acyclic)
    (hSurj : ∀ (β : α.ToType) (n : ℤ),
      Function.Surjective
        (ConcreteCategory.hom (comparisonMap α K β n))) :
    (limit K).Acyclic
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.31, Tag 02MY](https://stacks.math.columbia.edu/tag/02MY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
