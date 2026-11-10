---
declaration: section
origin: cited
lean: AssociatedGraded.dInvariant, AssociatedGraded.qInvariant, Stacks.LocalCohomology.UniformityIII.blowupHmod_of_qS_le, AlgebraicGeometry.exceptionalIdeal_pow_le_annihilator_kernel, AlgebraicGeometry.schemeTheoreticSupport_iff_exceptionalTwistContraction_eq_zero, Stacks.LocalCohomology.UniformityIII.ModuleSituation.subsingleton_H_top, Stacks.LocalCohomology.UniformityIII.ModuleSituation.subsingleton_H_next, Stacks.LocalCohomology.UniformityIII.TwistedModuleSituation.Htr_eq_zero
statement: formalized
proof: formalized
---

# 51.22 A bit of uniformity, III

Section 51.22 of the Stacks Project, [Tag 0GA6](https://stacks.math.columbia.edu/tag/0GA6). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GA6, the section

[Tag 0GA6](https://stacks.math.columbia.edu/tag/0GA6) in the Stacks Project.

**`AssociatedGraded.dInvariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/AssociatedGradedInvariants.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/AssociatedGradedInvariants.lean#L126). The attribute's comment: “the invariant d(S) of the associated graded ring S = Gr\_I(A), as the maximum of the dimensions of the fibres of Proj(S) → Spec(S₀), which is clause (2) of the paragraph defining d; the equality with the maximum of the fibre dimensions of the blowup p : X → Spec(A), the paragraph's primary phrasing, is not proved here”.

> **The invariant `d(S) = d(Gr_I(A))`**: the maximum of the dimensions of the fibres of
> `Proj(S) → Spec(S₀)`, a fibre with empty underlying space contributing `0`.
>
> This is clause (2) of the paragraph of [Stacks, Tag 0GA6] that introduces `d`; see the
> implementation notes for its relation to the paragraph's primary phrasing in terms of the
> blowup.

```lean
def dInvariant : ℕ∞
```

**`AssociatedGraded.qInvariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/AssociatedGradedInvariants.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/AssociatedGradedInvariants.lean#L166). The attribute's comment: “the invariant q(S) of the associated graded ring S = Gr\_I(A), as the smallest q(S) ≥ 0 such that for all q ≥ q(S) one has Hⁱ(Y, 𝒪\_Y(q)) = 0 for 1 ≤ i ≤ d(S) and H⁰(Y, 𝒪\_Y(q)) = I^q/I^\{q+1} for Y = Proj(S); the appeal to Cohomology of Schemes Lemmas 0AG6 and 0AG7 that makes the set of such bounds nonempty is not proved here, and is carried as a hypothesis by isRegularDegree\_of\_qInvariant\_le”.

> **The invariant `q(S) = q(Gr_I(A))`**: the smallest `q₀ ≥ 0` such that
> `AssociatedGraded.IsRegularDegree` holds at every `q ≥ q₀`.
>
> That the set of such `q₀` is nonempty is Cohomology of Schemes, Lemmas [Stacks, Tag 0AG6] and
> [Stacks, Tag 0AG7], which are not available in this generality; it is therefore a hypothesis of
> `AssociatedGraded.isRegularDegree_of_qInvariant_le` and not proved here.

```lean
def qInvariant : ℕ
```

## Tag 0GA7, a lemma

[Tag 0GA7](https://stacks.math.columbia.edu/tag/0GA7) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityIII.blowupHmod_of_qS_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/BlowupSituation.lean, line 705](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/BlowupSituation.lean#L705).

> **[Stacks, Tag 0GA7]**: with `q₀ = q(S)` (`qS I`, the least integer such that for all
> `q ≥ q₀` one has `Hⁱ(Y, 𝒪_Y(q)) = 0` for `i ≥ 1` and `H⁰(Y, 𝒪_Y(q)) = Iᑫ/I^{q+1}`), for a
> Noetherian ring `A` and any ideal `I`, on the blowup `X` of `Spec A` in `I`:
>
> 1. for `n ≥ 1`, `q ≥ q₀` and `i > 0`, `Hⁱ(X, 𝒪_{Yₙ}(q)) = 0`;
> 2. for `n ≥ 1` and `q ≥ q₀`, the canonical map `Iᑫ/I^{q+n} → H⁰(X, 𝒪_{Yₙ}(q))` is an
>    isomorphism — stated as the bijectivity of `cdivMod I m q`, whose source is `Iᑫ/I^{q+m+1}`
>    and whose target is `H⁰(X, 𝒪_{Y_{m+1}}(q))`, for every `m`, i.e. at `n = m + 1`;
> 3. for `q ≥ q₀` and `i > 0`, `Hⁱ(X, 𝒪_X(q)) = 0`;
> 4. for `q ≥ q₀`, the canonical map `Iᑫ → H⁰(X, 𝒪_X(q))` is an isomorphism.
>
> The cohomology is `A`-module-valued, the source's identifications being isomorphisms of
> `A`-modules. The integer `d = d(S)` the tag names enters only through the definition of `q(S)`,
> where it bounds the degrees in which vanishing is asked; see `IsBaseThreshold`,
> `isBaseThreshold_iff_of_vanishing_gt` and `exists_qS_isLeast_isBaseThresholdUpTo`.

```lean
theorem blowupHmod_of_qS_le [IsNoetherianRing A] :
    (∀ n i q : ℕ, 1 ≤ n → 1 ≤ i → qS I ≤ q →
        Subsingleton (blowupHmod I i (thickeningTwist I n q))) ∧
      (∀ n q : ℕ, qS I ≤ q → Function.Bijective (cdivMod I n q)) ∧
      (∀ i q : ℕ, 1 ≤ i → qS I ≤ q → Subsingleton (blowupHmod I i (blowupTwist I q))) ∧
      (∀ q : ℕ, qS I ≤ q → Function.Bijective (ambientSectionsMod I q))
```

## Tag 0GA8, a lemma

[Tag 0GA8](https://stacks.math.columbia.edu/tag/0GA8) in the Stacks Project.

**`AlgebraicGeometry.exceptionalIdeal_pow_le_annihilator_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AlmostExactness.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AlmostExactness.lean#L421).

> In a short exact sequence over `A ⧸ I ^ n` whose quotient is finite and
> `I ^ c / I ^ n`-projective, the kernel of the pulled-back first map is
> annihilated by the ideal of the `c`-th exceptional thickening.

```lean
public theorem exceptionalIdeal_pow_le_annihilator_kernel
    {A : Type u} [CommRing A] (I : Ideal A) (n c : ℕ) (_hcn : c ≤ n)
    (K L M : ModuleCat.{u} (A ⧸ I ^ n))
    (f : K ⟶ L) (g : L ⟶ M) (w : f ≫ g = 0)
    (hExact : (ShortComplex.mk f g w).ShortExact)
    [Module.Finite (A ⧸ I ^ n) M]
    (hM : Module.IsIProjective (A ⧸ I ^ n)
      (Ideal.map (Ideal.Quotient.mk (I ^ n)) (I ^ c)) M) :
    (exceptionalIdeal (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom I))) ^ c ≤
      Scheme.Modules.annihilatorIdeal
        (kernel ((Scheme.Modules.pullback
          (blowUpToBase (Scheme.IdealSheafData.ofIdealTop
            (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom I)))).map
              ((tilde.functor (.of A)).map
              ((ModuleCat.restrictScalars (Ideal.Quotient.mk (I ^ n))).map f))))
```

## Tag 0GA9, a lemma

[Tag 0GA9](https://stacks.math.columbia.edu/tag/0GA9) in the Stacks Project.

**`AlgebraicGeometry.schemeTheoreticSupport_iff_exceptionalTwistContraction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalTwist.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalTwist.lean#L227). The attribute's comment: “corrected: the canonical map runs 𝓕(c) ⟶ 𝓕, since 𝒪(1) is the ideal sheaf of Y”.

> **Stacks Project, Tag 0GA9.** A quasi-coherent module of finite type on the blowup of a
> scheme in a quasi-coherent sheaf of ideals is scheme theoretically supported on the `c`-fold
> thickening `Y_c` of the exceptional divisor if and only if the canonical map `𝓕(c) ⟶ 𝓕`
> vanishes.

```lean
theorem schemeTheoreticSupport_iff_exceptionalTwistContraction_eq_zero
    (F : (blowUp ℐ).Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    exceptionalIdeal ℐ ^ c ≤ Scheme.Modules.schemeTheoreticSupport F ↔
      exceptionalTwistContraction ℐ c F = 0
```

## Tag 0GAA, a lemma

[Tag 0GAA](https://stacks.math.columbia.edu/tag/0GAA) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityIII.ModuleSituation.subsingleton_H_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean#L591). The attribute's comment: “clause (1), H^d(X, p^*M(q)) = 0 for i = d ≥ 1 and q ≥ q₀”.

> **Stacks Project, Tag 0GAA, clause (1).** For an `(A, n, c)`-module `M`, in the case
> `i = d ≥ 1` and `q ≥ q₀` we have `H^d(X, p^*M(q)) = 0`.
>
> The long exact sequence of `0 → 𝒢 → (𝒪_{Yₙ})^{⊕r} → p^*M → 0` sits `H^d(X, p^*M(q))` between
> `H^d(X, (𝒪_{Yₙ})^{⊕r}(q))`, which vanishes by Tag 0GA7(1), and `H^{d+1}(X, 𝒢(q))`, which
> vanishes because `d` bounds the fibre dimensions.

```lean
theorem subsingleton_H_top (M : ANCModule I n c) {q : ℤ}
    (hd : 1 ≤ S.d) (hq : (S.q₀ : ℤ) ≤ q) : Subsingleton (S.H M S.d q)
```

**`Stacks.LocalCohomology.UniformityIII.ModuleSituation.subsingleton_H_next`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean#L616). The attribute's comment: “clause (2), H^\{d-1}(X, p^*M(q)) = 0 for i = d - 1 ≥ 1 and q ≥ q₀”.

> **Stacks Project, Tag 0GAA, clause (2).** For an `(A, n, c)`-module `M`, in the case
> `i = d - 1 ≥ 1` and `q ≥ q₀` we have `H^{d-1}(X, p^*M(q)) = 0`.
>
> The long exact sequence of `0 → 𝒢 → (𝒪_{Yₙ})^{⊕r} → p^*M → 0` sits `H^{d-1}(X, p^*M(q))`
> between `H^{d-1}(X, (𝒪_{Yₙ})^{⊕r}(q))`, which vanishes by Tag 0GA7(1) since `d - 1 ≥ 1`, and
> `H^d(X, 𝒢(q))`, which vanishes by `subsingleton_HG_top`.
>
> The hypothesis `i = d - 1` is written `i + 1 = d` to avoid a truncated subtraction.

```lean
theorem subsingleton_H_next (M : ANCModule I n c) {i : ℕ} {q : ℤ}
    (hi : 1 ≤ i) (hid : i + 1 = S.d) (hq : (S.q₀ : ℤ) ≤ q) : Subsingleton (S.H M i q)
```

**`Stacks.LocalCohomology.UniformityIII.TwistedModuleSituation.Htr_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean, line 863](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean#L863). The attribute's comment: “clause (3), Hⁱ(X, p^*M(q)) → Hⁱ(X, p^*M(q-(d-1-i)c)) is zero for d-1 > i > 0”.

> **Stacks Project, Tag 0GAA, clause (3).** For an `(A, n, c)`-module `M`, in the case
> `d - 1 > i > 0` and `q ≥ q₀ + (d - 1 - i)c` the map
> `Hⁱ(X, p^*M(q)) → Hⁱ(X, p^*M(q - (d - 1 - i)c))` is zero.
>
> The case distinction `d - 1 > i > 0` is written `1 ≤ i` together with `i + k + 1 = d` and
> `1 ≤ k`, which fixes `k = d - 1 - i`; the target twist `q - kc` is carried as a parameter `r`
> with `r + kc = q`. The proof reduces the statement to `HGtr_eq_zero`, whose induction it is.

```lean
theorem Htr_eq_zero (M : ANCModule I n c) {i k : ℕ} {q r : ℤ} (h : r ≤ q)
    (hi : 1 ≤ i) (hk : 1 ≤ k) (hik : i + k + 1 = S.d) (hr : r + k * c = q)
    (hq : (S.q₀ : ℤ) + k * c ≤ q) : S.Htr M i q r h = 0
```

**`Stacks.LocalCohomology.UniformityIII.TwistedModuleSituation.surjective_secM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean#L899). The attribute's comment: “clause (4), surjectivity onto H⁰(X, p^*M(q)) for i = 0, d ≤ 1, q ≥ q₀; corrected: the source is I^q ⊗\_A M, not the submodule I^qM, for which this is false”.

> **Stacks Project, Tag 0GAA, clause (4).** For an `(A, n, c)`-module `M`, in the case
> `i = 0`, `d ∈ {0, 1}` and `q ≥ q₀` the canonical map `I^q ⊗_A M → H⁰(X, p^*M(q))` is
> surjective.
>
> The long exact sequence of `0 → ℱ → p^*K → 𝒢 → 0` makes `H¹(X, p^*K(q)) → H¹(X, 𝒢(q))`
> surjective, since `H²(X, ℱ(q)) = 0` for `d ≤ 1`; its source vanishes, by clause (1) if `d = 1`
> and because `d` bounds the fibre dimensions if `d = 0`. So `H¹(X, 𝒢(q)) = 0` and the long exact
> sequence of `0 → 𝒢 → (𝒪_{Yₙ})^{⊕r} → p^*M → 0` makes `H⁰(X, (𝒪_{Yₙ})^{⊕r}(q)) → H⁰(X, p^*M(q))`
> surjective; for `q ≥ q₀` the source is `(I^q/I^{q+n})^{⊕r}` by Tag 0GA7(2), and the composite
> with it factors through `I^q ⊗_A M` by `ANCPresentation.freeTensor_surjective`.
>
> The Stacks Project writes the source `I^qM`. Read as the submodule `I^q·M` of `M` the clause
> is false: for `A = ℤ`, `I = (2)` (so the blowing up is an isomorphism, `d = 0`, `q₀ = 0`),
> `n = 1`, `c = 0` and `M = A ⧸ I`, at `q = 1` that submodule is `0` while Tag 0GA7(2) gives
> `H⁰(X, p^*M(1)) = H⁰(X, 𝒪_{Y₁}(1)) = I/I² ≅ ℤ/2`. What the proof produces, and what is
> formalized, is the surjection out of `I^q ⊗_A M = (I^q/I^{q+n}) ⊗_A M`, which agrees with
> `I^q/I^{q+n}` for `M = A ⧸ Iⁿ` as Tag 0GA7(2) demands.

```lean
theorem surjective_secM (M : ANCModule I n c) {q : ℕ} (hd : S.d ≤ 1) (hq : S.q₀ ≤ q) :
    Function.Surjective (S.secM M q)
```

**`Stacks.LocalCohomology.UniformityIII.TwistedModuleSituation.range_Htr_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean, line 930](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/PullbackCohomology.lean#L930). The attribute's comment: “clause (5), H⁰(p^*M(q)) → H⁰(p^*M(q-(d-1)c)) lands in the image of the canonical map out of I^\{q-(d-1)c} ⊗\_A M; corrected as in clause (4)”.

> **Stacks Project, Tag 0GAA, clause (5).** For an `(A, n, c)`-module `M`, in the case
> `i = 0`, `d > 1` and `q ≥ q₀ + (d - 1)c` the image of
> `H⁰(X, p^*M(q)) → H⁰(X, p^*M(q - (d - 1)c))` is contained in the image of the canonical map
> `I^{q - (d-1)c} ⊗_A M → H⁰(X, p^*M(q - (d - 1)c))`, the map of clause (4); as there, the source
> is the tensor product and not the submodule `I^{q-(d-1)c}M` of `M`.
>
> The case `d > 1` is written `k + 1 = d` with `1 ≤ k`, which fixes `k = d - 1`; the target
> twist `q - kc` is carried as a natural number `r` with `r + kc = q`, which is no restriction
> since `q ≥ q₀ + kc` forces `q - kc ≥ q₀ ≥ 0`. Arguing as in clause (4)
> it suffices that the image lie in the image of `H⁰(X, (𝒪_{Yₙ})^{⊕r}(q - (d-1)c))`, which by the
> long exact sequence of `0 → 𝒢 → (𝒪_{Yₙ})^{⊕r} → p^*M → 0` holds as soon as the boundary in
> `H¹(X, 𝒢(q))` dies in `H¹(X, 𝒢(q - (d-1)c))`; that is `HGtr_eq_zero` at `i = 0`.

```lean
theorem range_Htr_le (M : ANCModule I n c) {k r : ℕ} {q : ℤ} (h : (r : ℤ) ≤ q)
    (hk : 1 ≤ k) (hkd : k + 1 = S.d) (hr : (r : ℤ) + k * c = q)
    (hq : (S.q₀ : ℤ) + k * c ≤ q) :
    LinearMap.range (S.Htr M 0 q (r : ℤ) h) ≤ LinearMap.range (S.secM M r)
```

## Tag 0GAB, a remark

[Tag 0GAB](https://stacks.math.columbia.edu/tag/0GAB) in the Stacks Project.

**`Stacks.SheafOfModules.PullbackDual.dualModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/PullbackOfDualSheaf.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/PullbackOfDualSheaf.lean#L119). The attribute's comment: “the dual F^∨ = SheafHom(F, O), for a sheaf of modules on a ringed site”. References: EGA 0 (4.1.5); SGA 3 I (4.6.5.1), “more general”; SGA 3 III (0.6); SGA 3 VIIA (4.3.3), “more general”.

> The dual `F^∨ = SheafHom_O(F, O)` of a sheaf of modules on a ringed site: the internal Hom
> of Tag 03EM out of `F` into the structure sheaf, the structure sheaf being read as a module
> over itself.  This is the `(-)^∨` of Tag 0GAB.

```lean
noncomputable def dualModuleSheaf (Z : RingedSite.{u, u, u})
    (F : _root_.SheafOfModules.{u} (Tensor.ringSheaf Z.O)) :
    _root_.SheafOfModules.{u} (Tensor.ringSheaf Z.O)
```

**`Stacks.LocalCohomology.UniformityIII.moduleDual`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullback.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullback.lean#L130). The attribute's comment: “the dual M^∨ = Hom\_\{A/Iⁿ}(M, A/Iⁿ) of a module over A/Iⁿ, and its functoriality”. References: SGA 3 VIIA (3.1.1), “affine dual object”; SGA 3 VIIA (4.3.3), “special case”; SGA 3 VIIB (1.3.5.C), “more general”; SGA 3 VIII (6.8).

> The dual `M^∨ = Hom_R(M, R)` of an `R`-module, as a functor contravariant in `M`: on
> morphisms it is `LinearMap.dualMap`, that is, precomposition. For `R = A/Iⁿ` this is the `M^∨`
> of Tag 0GAB; no finiteness of `M` is needed to form it.

```lean
noncomputable def moduleDual : (ModuleCat.{u} R)ᵒᵖ ⥤ ModuleCat.{u} R
```

**`Stacks.LocalCohomology.UniformityIII.IsANCModule.exists_finFree_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullback.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullback.lean#L259). The attribute's comment: “for a ∈ I^c the map a : M → M factors through a finite free A/Iⁿ-module”.

> **Stacks Project, Tag 0GAB.** For an `(A, n, c)`-module `M` and `a ∈ I^c` the
> multiplication-by-`a` endomorphism of `M` factors through a *finite free* `A/Iⁿ`-module.
>
> This is the step the remark's proof of clause (4) opens with. By `IsANCModule` the map factors
> through a projective module; since `M` is finite it factors through a finite projective module
> by Tag 0G91, and a finite projective module is a retract of a finite free one.

```lean
theorem IsANCModule.exists_finFree_factorization {A : Type u} [CommRing A] {I : Ideal A}
    {n c : ℕ} {M : ModuleCat.{u} (A ⧸ I ^ n)} (hM : IsANCModule I n c M)
    {a : A ⧸ I ^ n} (ha : a ∈ Ideal.map (Ideal.Quotient.mk (I ^ n)) (I ^ c)) :
    ∃ (r : ℕ) (α : M ⟶ finFreeModule (A ⧸ I ^ n) r)
      (β : finFreeModule (A ⧸ I ^ n) r ⟶ M), α ≫ β = a • 𝟙 M
```

**`Stacks.LocalCohomology.UniformityIII.pullbackModuleDualMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean#L314). The attribute's comment: “the canonical map can : p^*(M^∨) ⟶ (p^*M)^∨”.

> **Tag 0GAB, the canonical map `can : p^*(M^∨) ⟶ (p^*M)^∨`.**  For a morphism of ringed sites
> `f : X ⟶ Spec R` and an `R`-module `M`, with `p^*N = f^*(N~)`: the pullback of the comparison
> `(M^∨)~ ⟶ (M~)^∨`, followed by the canonical map `f^*((M~)^∨) ⟶ (f^*(M~))^∨` of
> `Stacks.SheafOfModules.PullbackDual.pullbackDualMap`.

```lean
noncomputable def pullbackModuleDualMap (M : ModuleCat.{u} R) :
    (ringedSitePullback f).obj ((specTilde R).obj ((moduleDual R).obj (op M))) ⟶
      dualModuleSheaf X ((ringedSitePullback f).obj ((specTilde R).obj M))
```

**`Stacks.LocalCohomology.UniformityIII.pullbackModuleDualMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean#L322). The attribute's comment: “the construction of can is functorial in M”.

> **Tag 0GAB, the construction of `can` is functorial in `M`.**  For `g : M ⟶ N` the square
> formed by `can` at `M` and at `N`, by `p^*(g^∨)` and by `(p^*g)^∨` commutes.

```lean
theorem pullbackModuleDualMap_naturality {M N : ModuleCat.{u} R} (g : M ⟶ N) :
    (ringedSitePullback f).map ((specTilde R).map ((moduleDual R).map g.op)) ≫
        pullbackModuleDualMap f M =
      pullbackModuleDualMap f N ≫
        dualModuleSheafMap X ((ringedSitePullback f).map ((specTilde R).map g))
```

**`Stacks.LocalCohomology.UniformityIII.isIso_pullbackModuleDualMap_finFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean#L347). The attribute's comment: “can is an isomorphism at a finite free A/Iⁿ-module”.

> **Tag 0GAB: `can` is an isomorphism at a finite free module `R^{⊕r}`.**  The comparison is
> invertible there, `R^{⊕r}` being of finite presentation, and so is the sheaf-level `can` at
> `(R^{⊕r})~`, `M ↦ M~` being additive with `R~ = 𝒪`.

```lean
theorem isIso_pullbackModuleDualMap_finFree (r : ℕ) :
    IsIso (pullbackModuleDualMap f (finFreeModule R r))
```

**`Stacks.LocalCohomology.UniformityIII.IsANCModule.kernel_map_pullbackModuleDualMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean#L528). The attribute's comment: “for an (A,n,c)-module M, every a ∈ I^c annihilates the kernel of can”.

> **Tag 0GAB, the kernel of `can`.**  Let `M` be an `(A, n, c)`-module, `a ∈ I^c` and
> `f : X ⟶ Spec(A/Iⁿ)` any morphism of ringed sites.  Then `a` annihilates the kernel of
> `can : p^*(M^∨) ⟶ (p^*M)^∨`: the endomorphism of `ker(can)` induced by multiplication by `a` on
> `p^*(M^∨)` and on `(p^*M)^∨` is zero.  The source's reason is the proof: `a : M → M` factors
> through a finite free `A/Iⁿ`-module (`IsANCModule.exists_finFree_factorization`), at which
> `can` is an isomorphism.

```lean
theorem IsANCModule.kernel_map_pullbackModuleDualMap_eq_zero {X : RingedSite.{u, u, u}}
    (f : RingedSite.Hom X (specRingedSite (CommRingCat.of (A ⧸ I ^ n))))
    {M : ModuleCat.{u} (A ⧸ I ^ n)} (hM : IsANCModule I n c M) {a : A ⧸ I ^ n}
    (ha : a ∈ Ideal.map (Ideal.Quotient.mk (I ^ n)) (I ^ c)) :
    letI := specLinear (CommRingCat.of (A ⧸ I ^ n))
    kernel.map (pullbackModuleDualMap f M) (pullbackModuleDualMap f M)
        ((ringedSitePullback f).map (a • 𝟙 ((specTilde (CommRingCat.of (A ⧸ I ^ n))).obj
          ((moduleDual (CommRingCat.of (A ⧸ I ^ n))).obj (op M)))))
        (dualModuleSheafMap X ((ringedSitePullback f).map
          (a • 𝟙 ((specTilde (CommRingCat.of (A ⧸ I ^ n))).obj M))))
        (pullbackModuleDualMap_smul_naturality f M a) = 0
```

**`Stacks.LocalCohomology.UniformityIII.IsANCModule.cokernel_map_pullbackModuleDualMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DualPullbackSource.lean#L545). The attribute's comment: “for an (A,n,c)-module M, every a ∈ I^c annihilates the cokernel of can”.

> **Tag 0GAB, the cokernel of `can`.**  For an `(A, n, c)`-module `M`, `a ∈ I^c` and any
> morphism of ringed sites `f : X ⟶ Spec(A/Iⁿ)`, `a` annihilates the cokernel of
> `can : p^*(M^∨) ⟶ (p^*M)^∨`.

```lean
theorem IsANCModule.cokernel_map_pullbackModuleDualMap_eq_zero {X : RingedSite.{u, u, u}}
    (f : RingedSite.Hom X (specRingedSite (CommRingCat.of (A ⧸ I ^ n))))
    {M : ModuleCat.{u} (A ⧸ I ^ n)} (hM : IsANCModule I n c M) {a : A ⧸ I ^ n}
    (ha : a ∈ Ideal.map (Ideal.Quotient.mk (I ^ n)) (I ^ c)) :
    letI := specLinear (CommRingCat.of (A ⧸ I ^ n))
    cokernel.map (pullbackModuleDualMap f M) (pullbackModuleDualMap f M)
        ((ringedSitePullback f).map (a • 𝟙 ((specTilde (CommRingCat.of (A ⧸ I ^ n))).obj
          ((moduleDual (CommRingCat.of (A ⧸ I ^ n))).obj (op M)))))
        (dualModuleSheafMap X ((ringedSitePullback f).map
          (a • 𝟙 ((specTilde (CommRingCat.of (A ⧸ I ^ n))).obj M))))
        (pullbackModuleDualMap_smul_naturality f M a) = 0
```

## Tag 0GAC, a lemma

[Tag 0GAC](https://stacks.math.columbia.edu/tag/0GAC) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityIII.DualSituation.exists_sum_powQuotSmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DivisibleMaps.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DivisibleMaps.lean#L358). The attribute's comment: “with max(d, 1) in place of d, since at d = 0 the source's own argument reaches only level n - 2c while the source states n - c; its one open input is the level-(n-2c) section σ' of p^*(M^∨) produced by factoring through can, hypothesis `hσ`”.

> **Stacks Project, Tag 0GAC.** With `q₀ = q(S)` and `d = d(S)`, let `M` be an
> `(A, n, c)`-module and `φ : M → Iⁿ/I^{2n}` an `A`-linear map. Write `D = max(d, 1)` and assume
> `n ≥ q₀ + (1 + D)c` and `n ≥ (2 + D)c`. Then the composition
>
> `M --φ--> Iⁿ/I^{2n} → I^{n-(1+D)c}/I^{2n-(1+D)c}`
>
> is of the form `∑ aᵢψᵢ` with `aᵢ ∈ I^c` and `ψᵢ : M → I^{n-(2+D)c}/I^{2n-(2+D)c}`.
>
> The levels are carried as parameters so that no truncated subtraction appears in a type:
> `k + 1 = D`, `g + c = f`, `f + kc = e` and `e + 2c = n`, so that `f = n - (1 + D)c`,
> `g = n - (2 + D)c` and `e = n - 2c`; the two numerical hypotheses of the source are the
> existence of `g` as a natural number (`n ≥ (2 + D)c`) and `q₀ ≤ f` (`n ≥ q₀ + (1 + D)c`).
>
> **Deviation from the source, at `d = 0`.** The source writes `d` where this statement writes
> `D = max(d, 1)`, and adds for `d = 0` the hypothesis `n ≥ q₀ + 2c`. For `d ≥ 1` the two agree
> exactly. For `d = 0` the source's own argument does not reach the level it asserts: it produces
> `σ'` at level `n - 2c` — the cost of factoring through `can : p^*(M^∨) → (p^*M)^∨`, whose
> kernel and cokernel are supported on `Y_c`, and which is independent of `d` — and then applies
> clause (4) of Tag 0GAA at that level, which gives no further drop, so the argument ends at
> `n - 2c` while the statement asserts `n - (1 + 0)c = n - c`, a discrepancy of `c` in the wrong
> direction. The source's extra hypothesis `n ≥ q₀ + 2c` for `d = 0` is precisely what makes
> clause (4) applicable at `n - 2c`, which corroborates that `n - 2c` is the level reached. So
> for `d = 0` the levels stated here are the ones the argument supports, namely the `d = 1`
> numbers `2c` and `3c`; the hypothesis `n ≥ 3c` this needs is not implied by the source's `d = 0`
> hypotheses and is therefore part of `n ≥ (2 + D)c` above. Twisting the identity proved here
> down by `c` recovers the source's numbering, so the source's `d = 0` form is strictly stronger
> than what its argument establishes.
>
> **The one open input.** The level-`(n - 2c)` section `σ'` is a hypothesis, not a conclusion:
> producing it is the duality step of the source, which rests on the kernel and cokernel of `can`
> being scheme-theoretically supported on `Y_c` — a statement about the blowup situation that
> `Stacks.SheafOfModules.PullbackDual` (Tag 0GAB) explicitly does not prove. Everything after it
> is derived: the `(d-1)c` drop is Tag 0GAA clause (5) for `d ≥ 2` and clause (4) for `d ≤ 1`
> (`exists_ev_secM_eq`), and the passage from the resulting element of `I^f ⊗_A M^∨` to the sum
> `∑ aᵢψᵢ` is `ev_secM_mem_divisibleMaps`.

```lean
theorem exists_sum_powQuotSmul (M : ANCModule I n c)
    (φ : resModule I n M.1 →ₗ[A] powQuot I n n) {g f e k : ℕ}
    (hgf : g + c = f) (hk : max S.d 1 = k + 1) (he : f + k * c = e) (hen : e + 2 * c = n)
    (hq : S.q₀ ≤ f) (σ' : S.H M.dual 0 (e : ℤ))
    (hσ : S.ev M e (hq.trans (Nat.le.intro he)) σ' =
      (powQuotLe I (Nat.le.intro hen)).comp φ) :
    ∃ (N : ℕ) (a : Fin N → A) (ha : ∀ i, a i ∈ I ^ c)
      (ψ : Fin N → (resModule I n M.1 →ₗ[A] powQuot I g n)),
      (powQuotLe I ((Nat.le.intro he).trans (Nat.le.intro hen))).comp φ =
        ∑ i, (powQuotSmul I (ha i) hgf).comp (ψ i)
```

**`Stacks.LocalCohomology.UniformityIII.exists_sum_powQuotSmul_blowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DivisibleMapsBlowup.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/DivisibleMapsBlowup.lean#L66).

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal, `q₀ = q(S)` and `d = d(S)` the integers
> attached to the blowing up of `Spec(A)` in `I` (`qS I` and `fibreDim I`), `M` an
> `(A, n, c)`-module and `φ : M → Iⁿ/I^{2n}` an `A`-linear map. If `n ≥ q₀ + (1 + d)c` and
> `n ≥ (2 + d)c`, then the composition `M → Iⁿ/I^{2n} → I^{n-(1+d)c}/I^{2n-(1+d)c}` is of the
> form `∑ aᵢψᵢ` with `aᵢ ∈ I^c` and `ψᵢ : M → I^{n-(2+d)c}/I^{2n-(2+d)c}`. No hypothesis
> `n ≥ q₀ + 2c` is imposed when `d = 0`.

```lean
theorem exists_sum_powQuotSmul_blowup {n c : ℕ} (M : ANCModule I n c)
    (φ : resModule I n M.1 →ₗ[A] powQuot I n n)
    (hn₁ : qS I + (1 + fibreDim I) * c ≤ n) (hn₂ : (2 + fibreDim I) * c ≤ n) :
    ∃ (N : ℕ) (a : Fin N → A) (ha : ∀ i, a i ∈ I ^ c)
      (ψ : Fin N → (resModule I n M.1 →ₗ[A] powQuot I (n - (2 + fibreDim I) * c) n)),
      (powQuotLe I (Nat.sub_le n ((1 + fibreDim I) * c))).comp φ =
        ∑ i, (powQuotSmul I (ha i) (show n - (2 + fibreDim I) * c + c =
          n - (1 + fibreDim I) * c by
            have := two_add_mul_eq (fibreDim I) c; omega)).comp (ψ i)
```

## Tag 0GAD, a lemma

[Tag 0GAD](https://stacks.math.columbia.edu/tag/0GAD) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityIII.ext_one_powQuot_map_eq_zero_blowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/TwoTermExtBoundBlowup.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityIII/TwoTermExtBoundBlowup.lean#L84).

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal, and `q₀ = q(S)`, `d = d(S)` the integers
> attached to the blowing up of `Spec(A)` in `I` (`qS I` and `fibreDim I`). Let `c ≥ 0` and
> `n ≥ q₀ + (1 + d)c`, and let `K` be an object of `D(A/Iⁿ)` with `Hⁱ(K) = 0` for `i ≠ -1, 0`, with
> `H⁻¹(K)` and `H⁰(K)` finite, and such that `Ext¹_{A/Iⁿ}(K, N)` is annihilated by `I^c` for every
> finite `A/Iⁿ`-module `N`. Then the map
>
> `Ext¹_{A/Iⁿ}(K, Iⁿ/I^{2n}) ⟶ Ext¹_{A/Iⁿ}(K, I^{n-(1+d)c}/I^{2n-2(1+d)c})`
>
> induced by the canonical map of coefficients is zero.
>
> The target is written `powQuot I f f = I^f/I^{f+f}` with `f = n - (1 + d)c`, as an
> `A/Iⁿ`-module (`powQuotObjOfLe`); the map is the one induced by `Iⁿ ⊆ I^f` (`powQuotToOfLe`).

```lean
theorem ext_one_powQuot_map_eq_zero_blowup {n c : ℕ}
    (hn : qS I + (1 + fibreDim I) * c ≤ n)
    (K : DerivedCategory (ModuleCat.{u} (A ⧸ I ^ n)))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⧸ I ^ n)) i).obj K))
    (hfin₁ : Module.Finite (A ⧸ I ^ n)
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⧸ I ^ n)) (-1)).obj K))
    (hfin₀ : Module.Finite (A ⧸ I ^ n)
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⧸ I ^ n)) 0).obj K))
    (hann : ∀ (N : ModuleCat.{u} (A ⧸ I ^ n)), Module.Finite (A ⧸ I ^ n) N →
      ∀ a ∈ Ideal.map (Ideal.Quotient.mk (I ^ n)) (I ^ c),
      ∀ ξ : DerivedCategory.Ext K
        ((DerivedCategory.singleFunctor (ModuleCat.{u} (A ⧸ I ^ n)) 0).obj N) 1, a • ξ = 0)
    (ξ : DerivedCategory.Ext K
      ((DerivedCategory.singleFunctor (ModuleCat.{u} (A ⧸ I ^ n)) 0).obj (powQuotObj I n n)) 1) :
    ξ ≫ (CategoryTheory.shiftFunctor (DerivedCategory (ModuleCat.{u} (A ⧸ I ^ n))) (1 : ℤ)).map
        ((DerivedCategory.singleFunctor (ModuleCat.{u} (A ⧸ I ^ n)) 0).map
          (powQuotToOfLe I (Nat.sub_le n ((1 + fibreDim I) * c)) (by omega)
            (Nat.sub_le n ((1 + fibreDim I) * c)))) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.22, Tag 0GA6](https://stacks.math.columbia.edu/tag/0GA6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
