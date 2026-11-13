---
declaration: section
origin: cited
lean: Stacks.SectionsVanishingOnSubscheme.exists_bound_generatesOffSupport_and_isImmersion, Stacks.Bertini.FamilyDivisors.divisor, Stacks.Bertini.FamilyDivisors, Stacks.Bertini.FamilyDivisors.universalSection, Stacks.Bertini.FamilyDivisors.universalDivisor, Stacks.Bertini.FamilyDivisors.specializedSection, Stacks.Bertini.FamilyDivisors.specializedDivisor, Stacks.Bertini.FamilyDivisors.specializedDivisor_eq_comap
statement: formalized
proof: formalized
---

# 33.47 Bertini theorems

Section 33.47 of the Stacks Project, [Tag 0FD4](https://stacks.math.columbia.edu/tag/0FD4). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FD5, a lemma

[Tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5) in the Stacks Project.

**`Stacks.SectionsVanishingOnSubscheme.exists_bound_generatesOffSupport_and_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VanishingSystemImmersion/Basic.lean, line 790](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/VanishingSystemImmersion/Basic.lean#L790).

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

**`Stacks.Bertini.FamilyDivisors.divisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean#L89). The attribute's comment: “the divisor of a vector of the linear system”.

> **The divisor `H_w = Z(ψ(w))`** cut out on `X` by a vector of the linear system, as a
> quasi-coherent ideal sheaf.

```lean
def divisor (w : D.V) : D.X.IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L94). The attribute's comment: “the standing situation”.

> **Stacks Project, Tag 0G47.** The standing situation of the Bertini theorems: a field `k`,
> a scheme `X` over `k`, an invertible `𝒪_X`-module `L`, a finite dimensional `k`-vector space
> `V` with a chosen basis `v₁, …, v_r`, and a `k`-linear map `ψ : V → Γ(X, L)`.

```lean
structure FamilyDivisors
```

**`Stacks.Bertini.FamilyDivisors.universalSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L172). The attribute's comment: “the universal section”.

> **The universal section** `s_univ = Σᵢ xᵢ ψ(vᵢ)` of `pr₂^* L` on `𝔸^r_k ×_k X`, where
> `x₁, …, x_r` are the coordinates of the parameter affine space.

```lean
def universalSection :
    Γ((Scheme.Modules.pullback D.parameterProjection).obj D.L, ⊤)
```

**`Stacks.Bertini.FamilyDivisors.universalDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L181). The attribute's comment: “the universal divisor”.

> **The universal divisor** `H_univ = Z(s_univ) ⊂ 𝔸^r_k ×_k X`, the zero scheme of the
> universal section.

```lean
def universalDivisor : D.parameterSpace.IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors.specializedSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L206). The attribute's comment: “the section attached to a vector over an extension field”.

> **The section `ψ(v) = Σᵢ aᵢ ψ(vᵢ)`** of `L|_{X_{k'}}` attached to the vector
> `v = Σᵢ aᵢ vᵢ` of `V ⊗_k k'` with coordinate tuple `a` over a field extension `k'/k`.

```lean
def specializedSection (a : Fin (Module.finrank D.k D.V) → K) :
    Γ((Scheme.Modules.pullback (D.baseChangeToX K)).obj D.L, ⊤)
```

**`Stacks.Bertini.FamilyDivisors.specializedDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L215). The attribute's comment: “the divisor attached to a vector over an extension field”.

> **The divisor `H_v = Z(ψ(v))`** on `X_{k'}` attached to the vector of `V ⊗_k k'` with
> coordinate tuple `a`, as the zero scheme of the section it determines.

```lean
def specializedDivisor (a : Fin (Module.finrank D.k D.V) → K) :
    (D.baseChange K).IdealSheafData
```

**`Stacks.Bertini.FamilyDivisors.specializedDivisor_eq_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L248). The attribute's comment: “the fibre of the universal divisor”.

> **`H_v = H_{univ, v}`.** The divisor attached to a vector of `V ⊗_k k'` is the fibre of
> the universal divisor over the corresponding `k'`-point of `𝔸^r_k`, as quasi-coherent sheaves
> of ideals on `X_{k'}`.

```lean
theorem specializedDivisor_eq_comap (a : Fin (Module.finrank D.k D.V) → K) :
    D.specializedDivisor K a = D.universalDivisor.comap (D.fibreParameterMap K a)
```

**`Stacks.Bertini.FamilyDivisors.ForGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniFamilyDivisors.lean#L268). The attribute's comment: “holding for general vectors”.

> **A property of vectors holds for general `v`** when there is one nonempty open
> `U ⊂ 𝔸^r_k` such that `P` holds at every vector of `V ⊗_k k'` whose coordinate tuple gives a
> `k'`-point of `U`, for every field extension `k'/k`.

```lean
def ForGeneral
    (P : ∀ (K : Type u) [Field K] [Algebra D.k K], TensorProduct D.k D.V K → Prop) : Prop
```

## Tag 0FD6, a lemma

[Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6) in the Stacks Project.

**`Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor_of_isImmersion_canonicalMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCanonicalImmersion.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCanonicalImmersion.lean#L131). The attribute's comment: “hypothesis (3) is stated on the canonical morphism phi\_(L, psi) : X -> P(V) of Tag 0FCY; arbitrary base field, any dim V”.

> **[Stacks, Tag 0FD6].** In the standing situation of [Stacks, Tag 0G47] — a field `k`, a
> scheme `X` over `k`, an invertible `𝒪_X`-module `L`, a finite dimensional `k`-vector space `V`
> with a basis, and a `k`-linear map `ψ : V → Γ(X, L)` — assume that
>
> 1. `X` is smooth over `k`,
> 2. the image of `ψ` generates `L`,
> 3. the corresponding morphism `φ_{L,ψ} : X → 𝐏(V)` of [Stacks, Tag 0FCY] is an immersion.
>
> Then for general `v ∈ V ⊗_k k'` the scheme `H_v` is smooth over `k'`: there is a nonempty open
> `U ⊂ 𝔸^r_k` such that for every field extension `k'/k` and every `v ∈ V ⊗_k k'` whose coordinate
> tuple is a `k'`-point of `U`, the zero scheme `H_v = Z(ψ(v)) ⊂ X_{k'}` is smooth over `k'`.
>
> Hypothesis (1) is the instance `[Smooth D.toBase]`, (2) is `hgen`, and (3) is `himm`, stated on
> the basis-free morphism `Stacks.Bertini.FamilyDivisors.canonicalMorphism`. The base field is
> arbitrary, and `dim V` may be `0`. The proof transports (3) to every basis by
> `Stacks.Bertini.FamilyDivisors.isImmersive_iff_isImmersion_canonicalMorphism` and applies
> `Stacks.Bertini.FamilyDivisors.forGeneral_smooth_specializedDivisor`.

```lean
theorem forGeneral_smooth_specializedDivisor_of_isImmersion_canonicalMorphism [Smooth D.toBase]
    (hgen : D.Generates) (himm : IsImmersion (D.canonicalMorphism hgen)) :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          Smooth ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.47, Tag 0FD4](https://stacks.math.columbia.edu/tag/0FD4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
