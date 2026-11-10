---
declaration: section
origin: cited
lean: Crystalline.TorsionExample.completedDifferential_tauForm, Crystalline.TorsionExample.frobeniusPullback_tauClass_eq_envelopeMapOfLift, Crystalline.TorsionExample.frobeniusPullback_tauClass, Crystalline.TorsionExample.tauClass_ne_zero_and_prime_smul_eq_zero, Crystalline.TorsionExample.exists_ne_zero_prime_smul_eq_zero_cohomologyZero, Crystalline.TorsionExample.not_injective_frobeniusPullback, Crystalline.TorsionExample.quotientRingEquiv, Crystalline.TorsionExample.base_dividedPowers_unique
statement: formalized
proof: formalized
---

# 60.22 Two counter examples

Section 60.22 of the Stacks Project, [Tag 07LI](https://stacks.math.columbia.edu/tag/07LI). 2 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07LJ, an example

[Tag 07LJ](https://stacks.math.columbia.edu/tag/07LJ) in the Stacks Project.

**`Crystalline.TorsionExample.completedDifferential_tauForm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCompletedDeRham.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCompletedDeRham.lean#L286). The attribute's comment: “dτ = 0 in Ω_D, the p-adic completion of the divided power differentials of D = D_{P,γ}(J)^∧ over ZZ_p: τ lies in the kernel of the degree zero differential of D → Ω¹_D → Ω²_D → ⋯”.

> **`τ` lies in the kernel of the degree zero differential of the complex of
> [Stacks, Tag 07LG]**, which is the example's identity `dτ = 0` read through `Ω^0_D = D`.

```lean
theorem completedDifferential_tauForm : completedDifferential p 0 (tauForm p) = 0
```

**`Crystalline.TorsionExample.frobeniusPullback_tauClass_eq_envelopeMapOfLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean#L583). The attribute's comment: “F^*(τ) = σ(τ): for every lift φ of Frobenius on P = ZZ_p[x, y] over ZZ_p, with σ the map it induces on the divided power envelope, the Frobenius pullback of the class of τ in H^0(Cris(X/S), O_{X/S}) is the class defined by σ(τ)”.

> **`F^*(τ) = σ(τ)`**: for every lift `φ` of Frobenius on `P` and the map `σ` it induces on the
> divided power envelope, the class `F^*(τ) ∈ H⁰(Cris(X/S), 𝒪_{X/S})` is the class defined by
> `σ(τ)`: on every object `(U, T, δ)` of `Cris(X/S)` its value is the image of `σ(τ)` under a lift
> `E → Γ(T, 𝒪_T)` of the coordinates.

```lean
theorem frobeniusPullback_tauClass_eq_envelopeMapOfLift
    (φ : polynomial p →ₐ[ℤ_[p]] polynomial p)
    (hφ : ∀ f, φ f - f ^ p ∈ Ideal.span {(p : polynomial p)})
    (A : GlobalCrystallineSituation.CrystallineThickening (situation p)) :
    (cohomologyZeroEquiv p (frobeniusPullback p (tauClass p))).val (op A) =
      toSections (envelopeLift A.obj) (envelopeMapOfLift p φ hφ (envelopeTau p))
```

**`Crystalline.TorsionExample.frobeniusPullback_tauClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean, line 604](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean#L604). The attribute's comment: “for the lift of Frobenius x ↦ x^p, y ↦ y^p one has F^*(τ) = 0 in H^0(Cris(X/S), O_{X/S})”.

> **`F^*(τ) = 0`** for the lift of Frobenius `x ↦ x^p`, `y ↦ y^p`: the class `F^*(τ) = σ(τ)`
> vanishes, as `σ(τ) = γ_p(x^{2p}) γ_p(y^{2p}) − γ_p(x^p y^p)² = 0`.

```lean
theorem frobeniusPullback_tauClass : frobeniusPullback p (tauClass p) = 0
```

**`Crystalline.TorsionExample.tauClass_ne_zero_and_prime_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean#L627). The attribute's comment: “τ defines a nonzero element of H^0(Cris(X/S), O_{X/S}) killed by p, for X = Spec(F_p[x, y]/(x^2, xy, y^2)) and S = Spec(ZZ_p) with the divided power ideal (p)”.

> **`τ` defines a nonzero `p`-torsion element of `H⁰(Cris(X/S), 𝒪_{X/S})`.**

```lean
theorem tauClass_ne_zero_and_prime_smul_eq_zero : tauClass p ≠ 0 ∧ p • tauClass p = 0
```

**`Crystalline.TorsionExample.exists_ne_zero_prime_smul_eq_zero_cohomologyZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean#L634). The attribute's comment: “conclusion (1): H^0(Cris(X/S), O_{X/S}) has p-torsion, for X = Spec(F_p[x, y]/(x^2, xy, y^2)) and S = Spec(ZZ_p) with the divided power ideal (p)”.

> **`H⁰(Cris(X/S), 𝒪_{X/S})` has `p`-torsion**, for `X = Spec(𝐅_p[x, y]/(x², xy, y²))` and
> `S = Spec(ℤ_p)` with the divided power ideal `(p)` and its divided powers.

```lean
theorem exists_ne_zero_prime_smul_eq_zero_cohomologyZero :
    ∃ a : cohomologyZero p, a ≠ 0 ∧ p • a = 0
```

**`Crystalline.TorsionExample.not_injective_frobeniusPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionCrystallineCohomology.lean#L644). The attribute's comment: “conclusion (2): pulling back by Frobenius F^* : H^0(Cris(X/S), O_{X/S}) → H^0(Cris(X/S), O_{X/S}) is not injective, for X = Spec(F_p[x, y]/(x^2, xy, y^2)) and S = Spec(ZZ_p) with the divided power ideal (p)”.

> **Pulling back by Frobenius `F^* : H⁰(Cris(X/S), 𝒪_{X/S}) → H⁰(Cris(X/S), 𝒪_{X/S})` is not
> injective**, for `X = Spec(𝐅_p[x, y]/(x², xy, y²))` and `S = Spec(ℤ_p)` with the divided power
> ideal `(p)`.

```lean
theorem not_injective_frobeniusPullback : ¬ Function.Injective (frobeniusPullback p)
```

**`Crystalline.TorsionExample.quotientRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean#L297). The attribute's comment: “the example's presentation C = P/J: reduction of coefficients ZZ_p[x, y] -> F_p[x, y] induces a ring isomorphism ZZ_p[x, y]/(p, x^2, xy, y^2) = F_p[x, y]/(x^2, xy, y^2), carrying the class of each variable to that variable”.

> **The presentation of [Stacks, Tag 07LJ].**  Coefficient reduction induces a ring
> isomorphism
>
> `P/J = ℤ_[p][x, y]/(p, x², xy, y²) ≅ 𝐅_p[x, y]/(x², xy, y²) = C`
>
> carrying the class of `x` to `x` and the class of `y` to `y`, which is the identification the
> example writes as `C = P/J`.  Its effect on classes is `quotientRingEquiv_mk`.

```lean
noncomputable def quotientRingEquiv : quotientRing p ≃+* residueQuotient p
```

**`Crystalline.TorsionExample.base_dividedPowers_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean#L331). The attribute's comment: “the example's base: the ideal (p) of ZZ_p has exactly one divided power structure, so gamma is determined”.

> **The base of [Stacks, Tag 07LJ] is uniquely divided.**  The divided powers `γ` on the ideal
> `(p) ⊆ ℤ_[p]` are the only ones: `ℤ_[p]` is torsion free as a `ℤ`-module, so `n! γ_n(a) = aⁿ`
> determines `γ_n(a)`, which is the uniqueness half of [Stacks, Tag 07GM].

```lean
theorem base_dividedPowers_unique (γ : DividedPowers (Ideal.span {(p : ℤ_[p])})) :
    γ = PadicInt.dividedPowers p
```

**`Crystalline.TorsionExample.prime_mul_tau_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionDegreeZero.lean#L537). The attribute's comment: “the example's identity p τ = 0 in D, for τ = gammabar_p(x^2) gammabar_p(y^2) - gammabar_p(xy)^2, by the example's own display p! gammabar_p(x^2) gammabar_p(y^2) = x^{2p} gammabar_p(y^2) = gammabar_p(x^2 y^2) = x^p y^p gammabar_p(xy) = p! gammabar_p(xy)^2 together with the invertibility of (p-1)! in D”.

> **`p τ = 0`.**  Multiplying `τ` by `p!` gives
> `γ̄_p(x²y²) − γ̄_p((xy)(xy)) = 0`, and `p! = p (p − 1)!` with `(p − 1)!` invertible.

```lean
theorem prime_mul_tau_eq_zero : (p : completedEnvelope p) * tau p = 0
```

**`Crystalline.TorsionExample.toWitnessRing_envelopeTau`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionNonvanishing.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionNonvanishing.lean#L201). The attribute's comment: “the example's computation inside its witness thickening: the divided power morphism D_{P, γ}(J) -> B out of the universal property of the envelope sends γ_p(x^2) γ_p(y^2) - γ_p(xy)^2 to uv, which is nonzero in B (u_mul_v_ne_zero of RingTheory.DividedPowers.TorsionWitnessRing), at every prime p”.

> **The computation of [Stacks, Tag 07LJ].**  The element
> `γ_p(x²) γ_p(y²) − γ_p(xy)²` of the divided power envelope has image `u v` in the witness
> thickening `B`.

```lean
theorem toWitnessRing_envelopeTau :
    (toWitnessRing p).toRingHom (envelopeTau p) = u p * v p
```

**`Crystalline.TorsionExample.tau_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionNonvanishing.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/TorsionNonvanishing.lean#L225). The attribute's comment: “the example's claim that τ ≠ 0 in D, at every prime p, by the source's own witness thickening B = F_p[x, y, u, v]/(x^3, x^2 y, x y^2, y^3, xu, yu, xv, yv, u^2, v^2) with the divided powers of DividedPowers.TorsionWitness on K = ker(B -> C), which send x^2 to u and y^2 to v, in which τ maps to uv ≠ 0, so that the first level of the p-adic completion already sees τ”.

> **`τ ≠ 0` in `D`**, the last claim of [Stacks, Tag 07LJ] about `τ`.
>
> Were `τ` zero, its first level in the `p`-adic completion would vanish, so the envelope-level
> element `envelopeTau` would be a multiple of `p`.  Its image in the witness thickening `B` would
> then be zero, `p` being zero in `B`; but that image is `u v ≠ 0`.

```lean
theorem tau_ne_zero : tau p ≠ 0
```

## Tag 07LK, an example

[Tag 07LK](https://stacks.math.columbia.edu/tag/07LK) in the Stacks Project.

**`Crystalline.AffineSpaceCrystallineSetup.crisCohomologyIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L121). The attribute's comment: “RΓ(Cris(X/S), O_{X/S}) is represented by the complex D -> Omega^1_D -> ... -> Omega^r_D, D = Z_p[x_1, ..., x_r]^wedge, degreewise: H^j(Cris(X/S), O_{X/S}) is the j-th cohomology of that complex for every j, by 07LG/07LH for the presentation C = P/pP”.

> **`RΓ(Cris(X/S), 𝒪_{X/S})` is represented by the complex `D → Ω¹_D → Ω²_D → ⋯ → Ω^r_D`**, for
> `X = Spec(𝐅_p[x_1, …, x_r])` over `S = Spec(𝐙_p, (p), γ)` and `D = P^∧`,
> `P = 𝐙_p[x_1, …, x_r]`: in every degree `j`, `H^j(Cris(X/S), 𝒪_{X/S})` is the `j`-th cohomology
> of the completed divided power de Rham complex of `D`
> (`Crystalline.AffineSpaceCrystallineSetup.deRhamComplexNat`, whose terms vanish above `r`).
>
> This is [Stacks, Lemma 60.21.4, Tag 07LH]
> (`...SmallSite.smoothPresentationPair_computesCohomology`) for the crystal `𝒪_{X/S}` and the
> example's presentation `P → Γ(X, 𝒪_X)`, which is smooth with
> kernel `pP` (`Crystalline.AffineSpaceCrystallineSetup.presentation`), through any divided power
> map of envelopes compatible with the augmentations (`Crystalline.exists_smoothPresentationMap`):
> the pair of `𝒪_{X/S}` is `(D, d)` (`structureModulePairHom`), its base change to the completed
> envelope of `P → P/pP` is the structure module of that envelope
> (`Crystalline.FormsData.baseChangeUnitHom`), and the envelope of `P → P/pP` is `P`, `pP` having
> divided powers by [Stacks, Tag 07H1] (`Crystalline.AffineSpaceCrystallineSetup.envelopeEquiv`), so
> that the complex is the example's
> (`Crystalline.AffineSpaceCrystallineSetup.unitBaseChangeComplexIso`).

```lean
theorem crisCohomologyIso (j : ℕ) :
    Nonempty (T.crisCohomology j ≅
      AddCommGrpCat.uliftFunctor.{1, 0}.obj (T.deRhamComplexNat.homology j))
```

**`Crystalline.AffineSpaceCrystallineSetup.isZero_crisCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L173). The attribute's comment: “conclusion (1): H^j(Cris(X/S), O_{X/S}) = 0 for j > r, X = A^r_{F_p}, S = Spec(Z_p)”.

> **Conclusion (1) of [Stacks, Tag 07LK]: the crystalline cohomology of the crystalline
> structure sheaf of `X = 𝐀^r_{𝐅_p}` over `S = Spec(𝐙_p)` is zero except in degrees `0, …, r`.**
> Cohomology is indexed by `ℕ`, so this is the vanishing above `r`; it holds for every `r` (the
> source states its conclusions under `r > 0`).  The term `Ω^i_D` of the complex itself vanishes for
> `i > r`.

```lean
theorem isZero_crisCohomology {j : ℕ} (hj : T.r < j) : IsZero (T.crisCohomology j)
```

**`Crystalline.AffineSpaceCrystallineSetup.crisCohomologyZeroIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L185). The attribute's comment: “conclusion (2): H^0(Cris(X/S), O_{X/S}) = Z_p”.

> **Conclusion (2) of [Stacks, Tag 07LK]: `H⁰(Cris(X/S), 𝒪_{X/S}) = 𝐙_p`**, for every `r` (the
> source states its conclusions under `r > 0`): the kernel of `d : D → Ω¹_D` consists of the
> constants, an element of `𝐙_p[x_1, …, x_r]^∧` all of whose partial derivatives vanish being a
> constant.  The universe lift is the one `H^j(Cris(X/S), -)` is valued in.

```lean
theorem crisCohomologyZeroIso :
    Nonempty (T.crisCohomology 0 ≅ AddCommGrpCat.of (ULift.{1, 0} T.A))
```

**`Crystalline.AffineSpaceCrystallineSetup.infinite_and_not_isAddTorsion_crisCohomology_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L199). The attribute's comment: “conclusion (3): for r > 0, H^r(Cris(X/S), O_{X/S}) is infinite and is not a torsion abelian group”.

> **Conclusion (3) of [Stacks, Tag 07LK]: for `r > 0` the cohomology group
> `H^r(Cris(X/S), 𝒪_{X/S})` is infinite and is not a torsion abelian group.**

```lean
theorem infinite_and_not_isAddTorsion_crisCohomology_top (hr : 0 < T.r) :
    Infinite (T.crisCohomology T.r) ∧ ¬ IsAddTorsion (T.crisCohomology T.r)
```

**`Crystalline.AffineSpaceCrystallineSetup.not_isHausdorff_crisCohomology_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L214). The attribute's comment: “conclusion (4): for r > 0, H^r(Cris(X/S), O_{X/S}) is not separated for the p-adic topology”.

> **Conclusion (4) of [Stacks, Tag 07LK]: for `r > 0` the cohomology group
> `H^r(Cris(X/S), 𝒪_{X/S})` is not separated for the `p`-adic topology.**

```lean
theorem not_isHausdorff_crisCohomology_top (hr : 0 < T.r) :
    ¬ IsHausdorff (Ideal.span {(T.p : ℤ)}) (T.crisCohomology T.r)
```

**`Crystalline.AffineSpaceCrystallineSetup.exists_padicInt_crisCohomology_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Examples/AffineSpaceCrystallineCohomology.lean#L236). The attribute's comment: “closing remark on eta, the quoted 'generates a copy of Q_p' in the sense its argument shows: for r > 0 an injective Z_p -> H^r(Cris(X/S), O_{X/S}) through the class of eta, with [eta] in p^t H^r for every t, and no additive Q_p -> H^r extending it”.

> **The closing remark of [Stacks, Tag 07LK] on `η`, in the sense its argument shows.**  For
> `r > 0` the class of `η = ∑_{e > 0} p^e x_1^{p^e - 1} ⋯ x_r^{p^e - 1} dx_1 ∧ ⋯ ∧ dx_r` in
> `H^r(Cris(X/S), 𝒪_{X/S})` generates a copy of `𝐙_p` (no nonzero `𝐙_p`-multiple of `η`, in
> particular no `p^N η`, is exact), and it is divisible by every power of `p`; but no additive map
> `𝐐_p → H^r(Cris(X/S), 𝒪_{X/S})` sends `1` to it.  The source says that `η` "generates" a copy of
> `𝐐_p`, in quotation marks, and this theorem formalizes that remark in the sense its argument
> shows: an injective `𝐙_p → H^r` through `[η]`, with `[η] ∈ ⋂_t p^t H^r`.  The third clause records
> that the quotation marks are needed: there is no additive `𝐐_p → H^r` extending it, because the
> elements `x` with `p x = [η]` cannot themselves be divisible by every power of `p`
> (`Crystalline.AffineSpaceCrystallineSetup.not_exists_pow_smul_eq_etaTop`).

```lean
theorem exists_padicInt_crisCohomology_top (hr : 0 < T.r) :
    ∃ f : ℤ_[T.p] →+ T.crisCohomology T.r, Function.Injective f ∧
      (∀ t : ℕ, ∃ y, f 1 = (T.p ^ t) • y) ∧
      ¬ ∃ g : ℚ_[T.p] →+ T.crisCohomology T.r, g 1 = f 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.22, Tag 07LI](https://stacks.math.columbia.edu/tag/07LI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
