---
declaration: section
origin: cited
lean: Stacks.SectionsVanishingOnSubscheme.exists_bound_generatesOffSupport_and_isImmersion, Stacks.Bertini.FamilyDivisors.divisor, Stacks.Bertini.FamilyDivisors, Stacks.Bertini.FamilyDivisors.universalSection, Stacks.Bertini.FamilyDivisors.universalDivisor, Stacks.Bertini.FamilyDivisors.specializedSection, Stacks.Bertini.FamilyDivisors.specializedDivisor, Stacks.Bertini.FamilyDivisors.specializedDivisor_eq_comap
statement: formalized
proof: formalized
---

# 33.47 Bertini theorems

Section 33.47 of the Stacks Project, [Tag 0FD4](https://stacks.math.columbia.edu/tag/0FD4). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FD5, a lemma

[Tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5) in the Stacks Project.

**`Stacks.SectionsVanishingOnSubscheme.exists_bound_generatesOffSupport_and_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VanishingSystemImmersion/Basic.lean, line 790](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VanishingSystemImmersion/Basic.lean#L790).

> **[Stacks, Tag 0FD5].** Let `k` be a field, let `X` be a proper scheme over `k`, let `ℒ` be an
> ample invertible `𝒪_X`-module and let `Z ⊂ X` be the closed subscheme cut out by a quasi-coherent
> sheaf of ideals `I`. Then there is an integer `n₀` such that for every `n ≥ n₀` the kernel `V_n`
> of `Γ(X, ℒ ^⊗ n) ⟶ Γ(Z, ℒ ^⊗ n|_Z)` generates `ℒ ^⊗ n` on `X ∖ Z` and the canonical morphism
>
> `X ∖ Z ⟶ 𝐏(V_n)`
>
> of [Stacks, Tag 0FCY] is an immersion of schemes over `k`.
>
> The generation is the hypothesis `h` the existential carries: `GeneratesOffSupport k f I L n` says
> that the germs of the members of `V_n` span the stalk of `ℒ ^⊗ n` at every point of `X ∖ Z`, and
> it is what makes the canonical morphism exist. That morphism is
> `AlgebraicGeometry.toProjectiveSpaceOfModule`, the morphism of [Stacks, Tag 0FCY], applied to the
> linear system `V_n` restricted to `X ∖ Z`: that is what
> `Stacks.SectionsVanishingOnSubscheme.toProjectiveSpaceOfVanishingSections_eq` proves the morphism
> named below to be. The source speaks of *the* canonical morphism, which is basis free, and the
> conclusion is asserted for the morphism built in **every** basis of `V_n` — the presentation of
> `𝐏(V_n)` as `ℙᴺ_k` that [Stacks, Tag 0FCY] is stated with needs one.

```lean
theorem exists_bound_generatesOffSupport_and_isImmersion [IsProper f]
    (hL : IsAmple X L) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n → ∃ h : GeneratesOffSupport k f I L n,
      ∀ (N : ℕ) (b : Module.Basis (Fin (N + 1)) k (vanishingSections k f I L n)),
        IsImmersion (toProjectiveSpaceOfVanishingSections k f b h) ∧
        toProjectiveSpaceOfVanishingSections k f b h ≫
            projectiveSpaceOfModuleToSpec k (vanishingSections k f I L n) =
          (openComplement I).ι ≫ f
```

## Tag 0G47, a situation

[Tag 0G47](https://stacks.math.columbia.edu/tag/0G47) in the Stacks Project.

**`Stacks.Bertini.FamilyDivisors.divisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean#L89). The attribute's comment: “the divisor of a vector of the linear system”.

> **The divisor `H_w = Z(ψ(w))`** cut out on `X` by a vector of the linear system, as a
> quasi-coherent ideal sheaf.

```lean
def divisor (w : D.V) : D.X.IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L94). The attribute's comment: “the standing situation”.

> **Stacks Project, Tag 0G47.** The standing situation of the Bertini theorems: a field `k`,
> a scheme `X` over `k`, an invertible `𝒪_X`-module `L`, a finite dimensional `k`-vector space
> `V` with a chosen basis `v₁, …, v_r`, and a `k`-linear map `ψ : V → Γ(X, L)`.

```lean
structure FamilyDivisors
```

**`Stacks.Bertini.FamilyDivisors.universalSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L172). The attribute's comment: “the universal section”.

> **The universal section** `s_univ = Σᵢ xᵢ ψ(vᵢ)` of `pr₂^* L` on `𝔸^r_k ×_k X`, where
> `x₁, …, x_r` are the coordinates of the parameter affine space.

```lean
def universalSection :
    Γ((Scheme.Modules.pullback D.parameterProjection).obj D.L, ⊤)
```

**`Stacks.Bertini.FamilyDivisors.universalDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L181). The attribute's comment: “the universal divisor”.

> **The universal divisor** `H_univ = Z(s_univ) ⊂ 𝔸^r_k ×_k X`, the zero scheme of the
> universal section.

```lean
def universalDivisor : D.parameterSpace.IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors.specializedSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L206). The attribute's comment: “the section attached to a vector over an extension field”.

> **The section `ψ(v) = Σᵢ aᵢ ψ(vᵢ)`** of `L|_{X_{k'}}` attached to the vector
> `v = Σᵢ aᵢ vᵢ` of `V ⊗_k k'` with coordinate tuple `a` over a field extension `k'/k`.

```lean
def specializedSection (a : Fin (Module.finrank D.k D.V) → K) :
    Γ((Scheme.Modules.pullback (D.baseChangeToX K)).obj D.L, ⊤)
```

**`Stacks.Bertini.FamilyDivisors.specializedDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L215). The attribute's comment: “the divisor attached to a vector over an extension field”.

> **The divisor `H_v = Z(ψ(v))`** on `X_{k'}` attached to the vector of `V ⊗_k k'` with
> coordinate tuple `a`, as the zero scheme of the section it determines.

```lean
def specializedDivisor (a : Fin (Module.finrank D.k D.V) → K) :
    (D.baseChange K).IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors.specializedDivisor_eq_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L248). The attribute's comment: “the fibre of the universal divisor”.

> **`H_v = H_{univ, v}`.** The divisor attached to a vector of `V ⊗_k k'` is the fibre of
> the universal divisor over the corresponding `k'`-point of `𝔸^r_k`, as quasi-coherent sheaves
> of ideals on `X_{k'}`.

```lean
theorem specializedDivisor_eq_comap (a : Fin (Module.finrank D.k D.V) → K) :
    D.specializedDivisor K a = D.universalDivisor.comap (D.fibreParameterMap K a)
```

**`Stacks.Bertini.FamilyDivisors.ForGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L268). The attribute's comment: “holding for general vectors”.

> **A property of vectors holds for general `v`** when there is one nonempty open
> `U ⊂ 𝔸^r_k` such that `P` holds at every vector of `V ⊗_k k'` whose coordinate tuple gives a
> `k'`-point of `U`, for every field extension `k'/k`.

```lean
def ForGeneral
    (P : ∀ (K : Type u) [Field K] [Algebra D.k K], TensorProduct D.k D.V K → Prop) : Prop
```

## Tag 0FD6, a lemma

[Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6) in the Stacks Project.

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeDescent.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeDescent.lean#L300). The attribute's comment: “the conclusion from hypotheses (1), (2) and (3) over an ARBITRARY base field -- the algebraically closed case is no longer assumed, the reduction of Tag 02FY to it being carried out by forGeneral_smooth_specializedDivisor_of_forGeneral_baseChangeAlgebraicClosure. No proof obligation and no dimension datum is assumed, and quasi-compactness of X is derived from hypothesis (3) rather than assumed. Carrying a basis of the linear system is NOT a deviation: Situation 0G47 itself says 'Say dim(V) = r and we have a basis v_1, ..., v_r of V', so the basis is the source's own datum, and by isImmersive_congr_basis' the hypothesis does not depend on which basis it is read at. ONE deviation survives, and it is only this: the index type Fin (m + 1) forces dim V >= 1, where the source allows the degenerate r = 0 (there H_univ = X and the conclusion holds trivially by hypothesis (1)). Separately, (3) is spelled through the morphism built from that basis rather than through the source's canonical phi_(L, psi) characterised by theta : phi^*O(1) = L -- the same input Tag 01ND is registered without”.

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] with `X` smooth over
> a field `k`, if the image of `ψ` generates `L` and the morphism `φ_{L,ψ} : X → 𝐏(V)` it
> determines is an immersion, then the divisor `H_v` is smooth over `k'` for general
> `v ∈ V ⊗_k k'`.
>
> This is the statement with **no hypothesis that `k` be algebraically closed**: that case is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_`
> `basis'`, and the reduction of [Stacks, Tag 02FY] to it is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_baseChange`
> `AlgebraicClosure` followed by
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_forGeneral_`
> `baseChangeAlgebraicClosure`.
>
> The registration stays **qualified** for one reason only: hypothesis (3) is spelled as the
> immersiveness of `φ` read at a basis of `V` indexed by `Fin (m + 1)` rather than on the intrinsic
> morphism `φ_{L,ψ}`. Carrying a basis so indexed is an input the source does not make — it forces
> `dim_k V = m + 1`, in particular `V ≠ 0` — and the two readings of (3) agree only up to an
> identity the repository cannot yet prove. Everything else is the source's: (1) is the instance
> `[Smooth D.toBase]`, (2) is `hgen`, quasi-compactness of `X` is derived rather than assumed, and
> no dimension datum or proof obligation is taken.

```lean
theorem forGeneral_smooth_specializedDivisor_of_basis [Smooth D.toBase] (hgen : D.Generates)
    {m : ℕ} (b : Module.Basis (Fin (m + 1)) D.k D.V)
    (himm : D.IsImmersive b (D.generatesBy_basis hgen b)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeDescent.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeDescent.lean#L376).

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] with `X` smooth over
> a field `k`, if the image of `ψ` generates `L` and the morphism `φ_{L,ψ} : X → 𝐏(V)` it
> determines is an immersion, then the divisor `H_v` is smooth over `k'` for general
> `v ∈ V ⊗_k k'`.
>
> This takes the data of [Stacks, Tag 0G47] — the field `k`, the scheme `X` over it, the
> invertible module `L`, the finite dimensional linear system `V` with its basis, and `ψ` — and
> the source's three hypotheses, and nothing else: (1) is the instance `[Smooth D.toBase]`, (2) is
> `hgen`, and (3) is `himm`. There is no hypothesis that `k` be algebraically closed, no
> quasi-compactness assumption, no dimension datum, no proof obligation, and no condition on
> `dim V`: the degenerate case `dim V = 0` that the source allows is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_finrank_eq_zero`, and
> `dim V ≥ 1` is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_basis`, the basis of the
> standing situation reindexed along `dim V = m + 1`.
>
> Hypothesis (3) is read at every basis of `V` indexed by some `Fin (m + 1)` rather than at one:
> that is not a strengthening, because by
> `Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis'` the hypothesis holds at one such basis
> exactly when it holds at all of them, and when `dim V = 0` there are none and `himm` says
> nothing — which is what lets the degenerate case be covered at all.
>
> One caveat on hypothesis (3). It is spelled through the morphism built from a basis rather than
> through the source's canonical `φ_{L,ψ}` characterised by `θ : φ^*𝒪(1) ≅ L`; that is the same
> input [Stacks, Tag 01ND] is itself registered without, and
> `Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis'` shows the hypothesis does not depend on
> which basis it is read at.

```lean
theorem forGeneral_smooth_specializedDivisor [Smooth D.toBase] (hgen : D.Generates)
    (himm : ∀ (m : ℕ) (b : Module.Basis (Fin (m + 1)) D.k D.V),
      D.IsImmersive b (D.generatesBy_basis hgen b)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_baseChangeAlgebraicClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeImmersion.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFieldBaseChangeImmersion.lean#L134). The attribute's comment: “the conclusion of the tag for the standing situation base changed to an algebraic closure of the base field, with hypotheses (1), (2) and (3) assumed only for the original situation over k -- hypothesis (3) transfers by isImmersive_baseChangeFamily. This is NOT the tag for an arbitrary base field: the descent of the conclusion from kbar back to k (the reduction of Tag 02FY) needs a nonempty open of A^r_k whose points lift into the given nonempty open of A^r_kbar, which is not proved. Hypothesis (3) is also still spelled at a basis of the linear system rather than on the intrinsic morphism phi_(L, psi)”.

> **[Stacks, Tag 0FD6] for the situation base changed to an algebraic closure of the base
> field, from the source's three hypotheses for the original situation.** `X` smooth over `k`, the
> image of `ψ` generating `L`, and `φ_{L,ψ}` an immersion: then over `k̄` the divisor `H_v` is
> smooth for general `v`.
>
> All three hypotheses transfer to `D.baseChangeAlgebraicClosure`
> (`Stacks.Bertini.FamilyDivisors.smooth_baseChangeFamily`,
> `Stacks.Bertini.FamilyDivisors.generates_baseChangeFamily` and
> `Stacks.Bertini.FamilyDivisors.isImmersive_baseChangeFamily`), and `k̄` is algebraically closed,
> so the carrier of the tag applies to the base-changed situation.
>
> The registration is **qualified**: the conclusion drawn is the tag's conclusion for
> `D.baseChangeAlgebraicClosure`, not for `D`, and the passage between the two is what
> [Stacks, Tag 02FY] still owes — a nonempty open of `𝔸^r_k` whose points lift into the given
> nonempty open of `𝔸^r_{k̄}`, together with the identification of `H_v` on `X_{k'}` with its own
> base change.

```lean
theorem forGeneral_smooth_specializedDivisor_baseChangeAlgebraicClosure [Smooth D.toBase]
    (hgen : D.Generates) {m : ℕ} (b : Module.Basis (Fin (m + 1)) D.k D.V)
    (himm : D.IsImmersive b (D.generatesBy_basis hgen b)) :
    D.baseChangeAlgebraicClosure.ForGeneral (fun K' _ _ w =>
      ∀ a : Fin (Module.finrank D.baseChangeAlgebraicClosure.k
          D.baseChangeAlgebraicClosure.V) → K',
        w = ∑ i, TensorProduct.tmul D.baseChangeAlgebraicClosure.k
            (D.baseChangeAlgebraicClosure.basis i) (a i) →
          Smooth ((D.baseChangeAlgebraicClosure.specializedDivisor K' a).subschemeι ≫
            D.baseChangeAlgebraicClosure.baseChangeToSpec K'))
```

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_basis'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniImmersionQuasiCompact.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniImmersionQuasiCompact.lean#L147). The attribute's comment: “the conclusion from hypotheses (2) and (3) with no proof obligation and no dimension data assumed, with (3) at an arbitrary basis of the linear system, and with quasi-compactness of X no longer assumed -- it is derived from hypothesis (3), P(V) having a Noetherian space. ONE hypothesis here is not the source's: that k is algebraically closed, the case Tag 02FY reduces to. (3) is also still spelled at a basis rather than on the intrinsic morphism phi_(L, psi), but that is now only a spelling: they agree by Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis, so the hypothesis is independent of the basis it is read at; what is still unproved is its agreement with the source's canonical phi_(L, psi) as characterised by theta : phi^*O(1) = L, the same input Tag 01ND is registered without”.

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] with `X` smooth over
> an algebraically closed field `k`, if the image of `ψ` generates `L` and the morphism
> `φ_{L,ψ} : X → 𝐏(V)` it determines is an immersion, then the divisor `H_v` is smooth over `k'`
> for general `v ∈ V ⊗_k k'`.
>
> This is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_`
> `basis` with `[QuasiCompact D.toBase]` removed. That binder was not a hypothesis of the source:
> [Stacks, Tag 0G47] assumes of `X` only that it is a scheme over `k`, and [Stacks, Tag 0FD6] adds
> only smoothness, generation and the immersion — and smoothness gives `X` locally of finite
> presentation, hence locally of finite type, but not quasi-compact. It is discharged rather than
> dropped, from the immersion hypothesis itself: see
> `Stacks.Bertini.FamilyDivisors.quasiCompact_of_isImmersive`.
>
> `[IsAlgClosed D.k]` is then the only hypothesis of this statement that the source does not make.
> It is the case the source reduces to by [Stacks, Tag 02FY]; that reduction is a development of
> its own rather than a loose end. Its first half is done: the base change of the whole standing
> situation along `k → k̄` is `Stacks.Bertini.FamilyDivisors.baseChangeAlgebraicClosure`, all three
> hypotheses transfer to it — the third by
> `Stacks.Bertini.FamilyDivisors.isImmersive_baseChangeFamily` — and
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_baseChangeAlgebraicClosure`
> draws the conclusion of this statement over `k̄` from the source's three hypotheses over `k`.
> What is still owed is the descent of that conclusion: a nonempty open of `𝔸^r_k` whose points
> lift into the nonempty open of `𝔸^r_{k̄}` the conclusion over `k̄` provides, and the
> identification of `H_v` on `X_{k'}` with its own base change along an extension of `k'`.
> Hypothesis (3) is also still spelled at a basis of `V` rather than on the intrinsic
> morphism `φ_{L,ψ}` — but that is now only a spelling, the two agreeing by
> `Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis`, so hypothesis (3) does not depend on
> which basis it is read at. What is not yet proved is its agreement with the source's canonical
> `φ_{L,ψ}` as characterised by an isomorphism `θ : φ^*𝒪(1) ≅ ℒ` through which `ψ` factors — the
> same input [Stacks, Tag 01ND] is registered without.

```lean
theorem forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_basis' [IsAlgClosed D.k]
    [Smooth D.toBase] (hgen : D.Generates) {m : ℕ}
    (b : Module.Basis (Fin (m + 1)) D.k D.V)
    (himm : D.IsImmersive b (D.generatesBy_basis hgen b)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniJacobianDivisor.lean, line 613](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniJacobianDivisor.lean#L613). The attribute's comment: “the conclusion from hypotheses (2) and (3) with no proof obligation assumed and no dimension data assumed -- the whole of the source's proof is discharged, the count being run at each closed point with the local dimension of X there -- but over an algebraically closed field, and with (3) taken at the standing basis; the source assumes neither of those two”.

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] with `X` smooth and
> of finite type over an algebraically closed field `k`, if the image of `ψ` generates `L` and the
> morphism `φ_{L,ψ} : X → 𝐏(V)` it determines is an immersion, then the divisor `H_v` is smooth
> over `k'` for general `v ∈ V ⊗_k k'`.
>
> This is `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates` with
> its three non-source numerical and finiteness hypotheses removed. Hypothesis (1) of the tag is
> `[Smooth D.toBase]` together with `[QuasiCompact D.toBase]`, which is `X` of finite type over
> `k` in the shape clause (1) of `Stacks.Bertini.FamilyDivisors.Hypotheses` uses; hypothesis (2) is
> `Stacks.Bertini.FamilyDivisors.Generates` and hypothesis (3) is
> `Stacks.Bertini.FamilyDivisors.IsImmersive`. The whole of the source's proof is proved, as for
> that theorem, and in addition:
>
> * the Noetherianness of `H_univ`, which is derived from `X` being of finite type over `k`
>   (`Stacks.Bertini.FamilyDivisors.noetherianSpace_universalDivisorScheme`) rather than assumed;
> * the dimension data. The count is run at each closed point `x` of `X` with the local dimension
>   `n_x` of `X` at `x` in place of one global `n`: `n_x` exists because the local ring of a
>   smooth scheme at a closed point is regular
>   (`Stacks.Bertini.FamilyDivisors.exists_natCast_eq_topologicalKrullDimAt_of_isClosed`), the
>   inequality `n_x + 1 ≤ dim V` is read off the surjectivity of `ev_x`
>   (`Stacks.Bertini.FamilyDivisors.succ_le_of_smooth`) as it is in the source, and the fibre bound
>   `dim V - (n_x + 1)` is combined with `n_x` itself rather than with a global bound, by
>   `AlgebraicGeometry.topologicalKrullDim_le_of_isClosed_singleton_fiber_add_target`. So no
>   equidimensionality, no bound on `dim X`, and no numerical hypothesis `n + 1 ≤ dim V` remain.
>
> What remains in the signature and is **not** a hypothesis of the source: `[IsAlgClosed D.k]`,
> the case the source reduces to by [Stacks, Tag 02FY], a reduction not formalized here; and that
> hypothesis (3) is taken at the standing basis of the linear system read through `Fin (m + 1)`
> rather than at an arbitrary basis.

```lean
theorem forGeneral_smooth_specializedDivisor_of_generates_pointwise [IsAlgClosed D.k]
    [Smooth D.toBase] [QuasiCompact D.toBase] (hgen : D.Generates) {m : ℕ}
    (hm : Module.finrank D.k D.V = m + 1)
    (himm : D.IsImmersive (D.basis.reindex (finCongr hm))
      (D.generatesBy_basis hgen (D.basis.reindex (finCongr hm)))) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniJacobianDivisor.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniJacobianDivisor.lean#L681). The attribute's comment: “the conclusion from hypotheses (2) and (3) with no proof obligation and no dimension data assumed, and with (3) at an arbitrary basis of the linear system -- the whole of the source's proof is discharged, the count being run at each closed point with the local dimension of X there. TWO hypotheses here are not the source's: that k is algebraically closed, the case Tag 02FY reduces to, and [QuasiCompact D.toBase]. Situation 0G47 assumes only that X is a scheme over k and Tag 0FD6 adds only smoothness, so quasi-compactness is an addition; it is NOT clause (1) of this project's Hypotheses bundle, which is Tag 0G4F's hypothesis, not 0G47's standing situation. (3) is also still spelled at a basis rather than on the intrinsic morphism phi_(L, psi), but that is now only a spelling: the two agree by Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis, so the hypothesis does not depend on which basis it is read at”.

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] with `X` smooth and
> of finite type over an algebraically closed field `k`, if the image of `ψ` generates `L` and the
> morphism `φ_{L,ψ} : X → 𝐏(V)` it determines is an immersion, then the divisor `H_v` is smooth
> over `k'` for general `v ∈ V ⊗_k k'`.
>
> This is
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise` with
> **hypothesis (3) taken at an arbitrary basis of the linear system** rather than at the standing
> basis: the basis `b` is any basis of `V`, and the generation hypothesis at it is hypothesis (2)
> of the tag, which is basis free (`Stacks.Bertini.FamilyDivisors.generates_iff_generatesBy_basis`).
> No relation between `b` and the standing basis `D.basis` is assumed, and no bound on `dim V` is
> needed: `b` itself exhibits one.
>
> The basis enters the proof in two roles, which this statement separates. Hypothesis (3) feeds
> only the surjectivity of the evaluation `ev_x`, a property of the basis-free map
> `Stacks.Bertini.FamilyDivisors.evalVector` and so of no basis at all
> (`Stacks.Bertini.FamilyDivisors.surjective_evalCoord_sectionOf_iff`); the Jacobian criterion
> `Stacks.Bertini.FamilyDivisors.JacobianAtDivisor`, on the other hand, can only be stated against
> the standing basis, since the coordinates of the parameter space are coefficients against it.
> The chain
> `Stacks.Bertini.FamilyDivisors.exists_evalMatrix_of_basis` →
> `…smooth_specializedDivisor_forGeneral_of_jacobianAtDivisor_pointwise_of_basis` carries the two
> as separate parameters, and this statement instantiates the second at
> `D.basis.reindex (finCongr …)`, which is where
> `Stacks.Bertini.FamilyDivisors.jacobianAtDivisor` applies.
>
> What remains in the signature and is **not** a hypothesis of the source: `[IsAlgClosed D.k]` and
> `[QuasiCompact D.toBase]`. `[Smooth D.toBase]` is hypothesis (1); it gives `X` locally of finite
> presentation, hence locally of finite type, but not quasi-compact, so `[QuasiCompact D.toBase]`
> is an addition — [Stacks, Tag 0G47] assumes of `X` only that it is a scheme over `k`, and
> clause (1) of `Stacks.Bertini.FamilyDivisors.Hypotheses`, which does assume finite type, is
> [Stacks, Tag 0G4F]'s hypothesis rather than 0G47's standing situation. It is however not needed:
> hypothesis (3) implies it, since `𝐏(V)` has a Noetherian underlying space and an immersion
> embeds `X` in it. The sibling
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_`
> `basis'` is this statement with the binder discharged that way; see
> `Stacks.Bertini.FamilyDivisors.quasiCompact_of_isImmersive`. Every proof obligation of the
> source's argument is discharged, and so is all the dimension data: no equidimensionality of `X`,
> no bound on `dim X`, no inequality `n + 1 ≤ dim V`, and no Noetherianness of `H_univ` is
> assumed, the count being run at each closed point of `X` with the local dimension of `X` there.
> `[IsAlgClosed D.k]` is the case the source reduces to by [Stacks, Tag 02FY]; that reduction is
> **not** formalized here, and it is not a loose end but a development of its own — it needs the
> base change of the standing situation along `k → k̄`, which nothing in the library constructs,
> and above all the transfer of hypothesis (3) itself, for which the base-change compatibility of
> `AlgebraicGeometry.toProjectiveSpaceOfModule` is missing.

```lean
theorem forGeneral_smooth_specializedDivisor_of_generates_pointwise_of_basis [IsAlgClosed D.k]
    [Smooth D.toBase] [QuasiCompact D.toBase] (hgen : D.Generates) {m : ℕ}
    (b : Module.Basis (Fin (m + 1)) D.k D.V)
    (himm : D.IsImmersive b (D.generatesBy_basis hgen b)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Stacks.Bertini.FamilyDivisors.smooth_specializedDivisor_forGeneral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmooth.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmooth.lean#L147). The attribute's comment: “carrying the Tag 0B2L dimension bound on the singular locus of q”.

> In the standing situation of `Stacks.Bertini.FamilyDivisors` with `X` smooth over `k`, the
> divisor `H_v` is smooth over `k'` for general `v ∈ V ⊗_k k'`.
>
> It takes as hypothesis `hsing`: there is a nonempty open `U` of `𝔸^r_k` whose preimage under
> `q : H_univ → 𝔸^r_k` lies in the smooth locus of `q`. It also takes the instance argument
> `LocallyOfFinitePresentation q`, which `locallyOfFinitePresentation_universalFamilyMap` supplies
> from the smoothness of `X` over `k`.

```lean
public theorem smooth_specializedDivisor_forGeneral [Smooth D.toBase]
    [LocallyOfFinitePresentation D.universalFamilyMap]
    (U : D.parameterBase.Opens) (hU : (U : Set D.parameterBase).Nonempty)
    (hsing : ((D.universalFamilyMap ⁻¹ᵁ U : D.universalDivisor.subscheme.Opens) :
        Set D.universalDivisor.subscheme) ⊆
      (D.universalFamilyMap.smoothLocus : Set D.universalDivisor.subscheme)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.47, Tag 0FD4](https://stacks.math.columbia.edu/tag/0FD4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
