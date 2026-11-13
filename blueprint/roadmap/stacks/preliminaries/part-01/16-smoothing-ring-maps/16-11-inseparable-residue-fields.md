---
declaration: section
origin: cited
lean: Stacks.Smoothing.nonempty_coefficientSectionData_of_finite_h1Cotangent, Stacks.Smoothing.exists_directedOn_flat_essFiniteType, Stacks.Smoothing.exists_directedOn_flat_essFiniteType_of_charP, Stacks.Smoothing.exists_coefficientStage_basis_kaehlerDifferential_primePowerQuotient, Stacks.Smoothing.exists_mvPolynomial_factorization_isEssentiallySmooth_flat, Stacks.Smoothing.exists_mvPolynomial_flat_localization, Stacks.Smoothing.exists_mvPolynomial_factorization_mem_isEssentiallySmooth_flat_of_charP, Stacks.Smoothing.exists_essentiallySmooth_enlargement_containing_pow_of_factorization
statement: formalized
proof: formalized
---

# 16.11 Inseparable residue fields

Section 16.11 of the Stacks Project, [Tag 07FF](https://stacks.math.columbia.edu/tag/07FF). 30 tags here are carried by 41 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07FG, a lemma

[Tag 07FG](https://stacks.math.columbia.edu/tag/07FG) in the Stacks Project.

**`Stacks.Smoothing.nonempty_coefficientSectionData_of_finite_h1Cotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean#L634). The attribute's comment: “The central claim of the source's proof, the only place where char k = p and dim H₁(L\_\{K/k}) < ∞ are used: there exist a ring-theoretic section σ : K → Λ of the residue map, generators λ₁, …, λ\_d of 𝔪, and a finitely generated k ⊆ F₀ ⊆ K with the image of k in Λ contained in Ψ\_σ(F₀[λ₁, …, λ\_d]). The source's induction on the nilpotency order of 𝔪 is followed, including the correction of σ by a derivation K → 𝔪^\{n-1} read off the Jacobi-Zariski sequence. NOT covered: the conclusion of the lemma, which is proved from this claim in `exists_directedOn_flat_essFiniteType`.”.

> **Stacks 07FG**, the central claim of its proof: the data of `CoefficientSectionData` exists
> for every Artinian local algebra over a field of characteristic `p > 0` whose residue field
> extension has `dim_K H₁(L_{K/k}) < ∞`.
>
> No finiteness is assumed of the residue field extension itself; the transcendence degree of `K`
> over `k` may be infinite.

```lean
theorem nonempty_coefficientSectionData_of_finite_h1Cotangent {k Λ : Type*} [Field k]
    [CommRing Λ] [Algebra k Λ] [IsArtinianRing Λ] [IsLocalRing Λ] (p : ℕ) [Fact p.Prime]
    [CharP k p] [Module.Finite (ResidueField Λ) (Algebra.H1Cotangent k (ResidueField Λ))] :
    Nonempty (CoefficientSectionData k Λ)
```

**`Stacks.Smoothing.exists_directedOn_flat_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean, line 665](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean#L665). The attribute's comment: “The lemma, under the source's own hypotheses and nothing else: char k = p > 0, Λ an Artinian local k-algebra, and dim H₁(L\_\{K/k}) < ∞, with no finiteness assumed of K/k. The conclusion is read in the directed-union form in which the source itself reads it (flatness of A → Λ out of a local ring makes it injective, as the source's first line observes): the approximating subalgebras are the stages Ψ\_σ(F[λ]) for finitely generated F₀ ≤ F ≤ K, and they are Artinian local k-subalgebras of Λ, essentially of finite type over k, with Λ flat (indeed free) over each and with 𝔪\_A Λ = 𝔪, and they are directed and cover Λ. The section σ and the finitely generated F₀ are produced by the source's induction on the nilpotency order of 𝔪 in `nonempty_coefficientSectionData_of_finite_h1Cotangent`, the only place where char k = p and dim H₁(L\_\{K/k}) < ∞ are used; the properties of the stages are `exists_directedOn_flat_essFiniteType_of_coefficientSectionData`.”.

> **Stacks 07FG**. Let `k` be a field of characteristic `p > 0` and let `(Λ, 𝔪, K)` be an
> Artinian local `k`-algebra with `dim_K H₁(L_{K/k}) < ∞`. Then there is a directed family `𝒜` of
> `k`-subalgebras of `Λ` which covers `Λ` — so that `Λ` is the filtered colimit of `𝒜` — each
> member `A` of which is Artinian local, is essentially of finite type over `k`, has `Λ` flat over
> it, and satisfies `𝔪_A Λ = 𝔪`.

```lean
theorem exists_directedOn_flat_essFiniteType {k Λ : Type*} [Field k] [CommRing Λ]
    [Algebra k Λ] [IsArtinianRing Λ] [IsLocalRing Λ] (p : ℕ) [Fact p.Prime] [CharP k p]
    [Module.Finite (ResidueField Λ) (Algebra.H1Cotangent k (ResidueField Λ))] :
    ∃ 𝒜 : Set (Subalgebra k Λ), DirectedOn (· ≤ ·) 𝒜 ∧ (∀ y : Λ, ∃ A ∈ 𝒜, y ∈ A) ∧
      ∀ A ∈ 𝒜, ∃ (_ : IsArtinianRing A) (_ : IsLocalRing A),
        Module.Flat A Λ ∧ Algebra.EssFiniteType k A ∧
        Ideal.map A.val.toRingHom (maximalIdeal A) = maximalIdeal Λ
```

**`Stacks.Smoothing.exists_directedOn_flat_essFiniteType_of_charP`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean, line 681](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/CentralClaim.lean#L681). The attribute's comment: “The lemma, under the source's own hypotheses: the statement of `exists_directedOn_flat_essFiniteType`, to which this reduces, under the name used for it in the documentation of the Stacks 07FH material in the second half of this file.”.

> **Stacks 07FG**, under the name used for it in the documentation of the Stacks 07FH material
> in the second half of this file. The statement is that of
> `exists_directedOn_flat_essFiniteType`.

```lean
alias exists_directedOn_flat_essFiniteType_of_charP
```

**`Stacks.Smoothing.exists_coefficientStage_basis_kaehlerDifferential_primePowerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/FlatLocalization.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/FlatLocalization.lean#L85). The attribute's comment: “A strengthening of the central claim of the source's proof, needed by Stacks 07FH and not proved there. 07FH picks λ₁, …, λ\_t ∈ Λ whose images lie in the approximating subalgebra A ⊆ Λ\_𝔮/𝔮^nΛ\_𝔮 of 07FG and whose differentials form a basis of Ω\_\{F/k} for F = A/𝔪\_A; no argument is given, A is never enlarged afterwards, and for a general member of the directed family the residues of elements of Λ lying in F do not generate F. With Λ/𝔮 = k[x, y], so K = k(x, y), and F = k(x/y) one has F ∩ k[x, y] = k, because a nonconstant element of k(x/y) is homogeneous of degree 0, so the differentials of the residues of Λ lying in F span 0 ≠ Ω\_\{F/k}; and by exists\_subalgebra\_residueField\_image\_eq\_of\_charP every finitely generated subfield of K above a bound does occur as A/𝔪\_A. What is added here is that the section σ and the generators λ of 𝔪 may be chosen so that the coefficient field is generated by residues of elements of Λ — it is k(Ȳ) for a finite Y ⊆ Λ containing any prescribed finite set, with the images of all elements of Y inside the stage — whence a basis of Ω\_\{k(Ȳ)/k} among the differentials of residues of elements of Λ whose images lie in the stage. NOT covered: flatness of Λ\_𝔮/𝔮^nΛ\_𝔮 over this particular stage, which exists\_stage supplies only for coefficient fields large enough to contain the b-coordinates of the generators of 𝔪.”.

> **The λ-choice of Stacks 07FH, in the setting of that lemma.** Let `k` be a field of
> characteristic `p > 0`, let `Λ` be a Noetherian `k`-algebra, let `𝔮` be a prime of `Λ`, let
> `n ≥ 1` and assume `dim_K H₁(L_{K/k}) < ∞` for the residue field `K = κ(𝔮)` of
> `Λ̄ = Λ_𝔮/𝔮^nΛ_𝔮`. Then for every finite subset `S` of `Λ` there are a ring-theoretic section
> `σ : K → Λ̄` of the residue map, generators `λ₁, …, λ_d` of the maximal ideal of `Λ̄`, a finite
> `S ⊆ Y ⊆ Λ` and elements `μ₁, …, μ_t` of `Y` such that the stage
> `A = Ψ_σ(F[λ₁, …, λ_d])` of the coefficient field `F = k(ȳ : y ∈ Y)` contains the image of `k`
> and the images of all elements of `Y`, has residue image exactly `F`, and has
> `dμ̄₁, …, dμ̄_t` a basis of `Ω_{F/k}`.
>
> The hypothesis of `exists_coefficientStage_basis_kaehlerDifferential` on the map `Λ → Λ̄` is
> automatic here: `κ(𝔮)` is the fraction field of `Λ/𝔮`.

```lean
theorem exists_coefficientStage_basis_kaehlerDifferential_primePowerQuotient {k Λ : Type*}
    [Field k] [CommRing Λ] [Algebra k Λ] [IsNoetherianRing Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime] {n : ℕ}
    [IsLocalRing (primePowerQuotient 𝔮 n)] (p : ℕ) [Fact p.Prime] [CharP k p]
    [Module.Finite (ResidueField (primePowerQuotient 𝔮 n))
      (Algebra.H1Cotangent k (ResidueField (primePowerQuotient 𝔮 n)))] (S : Finset Λ) :
    ∃ (Y : Finset Λ) (σ : ResidueField (primePowerQuotient 𝔮 n) →+* primePowerQuotient 𝔮 n)
      (d : ℕ) (x : Fin d → primePowerQuotient 𝔮 n)
      (F : IntermediateField k (ResidueField (primePowerQuotient 𝔮 n))) (t : ℕ) (lam : Fin t → Λ)
      (hlam : ∀ j, residue (primePowerQuotient 𝔮 n)
        (algebraMap Λ (primePowerQuotient 𝔮 n) (lam j)) ∈ F),
      S ⊆ Y ∧ (∀ j, lam j ∈ Y) ∧ (∀ c, residue (primePowerQuotient 𝔮 n) (σ c) = c) ∧
      Ideal.span (Set.range x) = maximalIdeal (primePowerQuotient 𝔮 n) ∧
      F = IntermediateField.adjoin k ((fun y => residue (primePowerQuotient 𝔮 n)
        (algebraMap Λ (primePowerQuotient 𝔮 n) y)) '' (Y : Set Λ)) ∧ F.FG ∧
      (∀ a : k, algebraMap k (primePowerQuotient 𝔮 n) a ∈ coefficientStage σ F x) ∧
      (∀ y ∈ Y, algebraMap Λ (primePowerQuotient 𝔮 n) y ∈ coefficientStage σ F x) ∧
      (∀ z ∈ coefficientStage σ F x, residue (primePowerQuotient 𝔮 n) z ∈ F) ∧
      ∃ b : Module.Basis (Fin t) F (Ω[F⁄k]), ∀ j, b j = KaehlerDifferential.D k F
        ⟨residue (primePowerQuotient 𝔮 n) (algebraMap Λ (primePowerQuotient 𝔮 n) (lam j)),
          hlam j⟩
```

## Tag 07FH, a lemma

[Tag 07FH](https://stacks.math.columbia.edu/tag/07FH) in the Stacks Project.

**`Stacks.Smoothing.exists_mvPolynomial_factorization_isEssentiallySmooth_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/EssentiallySmoothFactorization.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/EssentiallySmoothFactorization.lean#L257). The attribute's comment: “clause (2), UNCONDITIONALLY: no hypothesis on `κ(𝔮)` beyond the tag's own (`Λ` Noetherian and geometrically regular over `k`); the characteristic hypothesis is not needed either. `essentially smooth` is `RingHom.IsEssentiallySmooth` (essentially of finite presentation, Tag 00QM (2), plus formally smooth); the Stacks Project uses the term here and in the two following lemmas without ever defining it, and this repository supplies the definition those proofs need, in `StacksFrontier.RingTheory.Smoothing.EssentiallySmooth`. WHAT IS PROVED: `m` and `φ : k[y_1, …, y_m] → Λ` with `𝔭 = φ^{-1}(𝔮)`, the ideal identity `𝔭Λ_𝔮 = 𝔮Λ_𝔮`, flatness of `g : k[y]_𝔭 → Λ_𝔮`, a local Artinian subring `D` of `Λ̄ = Λ_𝔮/𝔮^nΛ_𝔮` and a factorization of the induced map `u : k[y]_𝔭/𝔭^n → Λ̄` as an essentially smooth map into `D` followed by the inclusion `D → Λ̄`, which is flat. HOW: clause (2) on its own needs no approximating subring at either end. Clause (1), `exists_mvPolynomial_flat_localization`, is unconditional and supplies `φ` with `𝔭Λ_𝔮 = 𝔮Λ_𝔮` and `k[y]_𝔭 → Λ_𝔮` flat; hence `𝔭^n Λ_𝔮 = 𝔮^n Λ_𝔮`, so `u` is the base change of a flat map along `k[y]_𝔭 → k[y]_𝔭/𝔭^n` and is flat, and `u` is a local homomorphism of local rings, hence faithfully flat (`Module.FaithfullyFlat.of_flat_of_isLocalHom`), hence INJECTIVE. So `D = range u` is a local Artinian subring of `Λ̄`, `u` restricts to an isomorphism onto it — essentially smooth, a bijective ring map being so — and `D → Λ̄` is flat because `u` is. The source instead draws `D` from the directed family of Stacks 07FG, because it proves clause (3) at the same time: the approximating subring is needed for `E ⊆ D`, and that is where the source's unjustified λ-choice sits. WHAT REMAINS: clause (2) alone places no element inside `D`, so it is Stacks 07FT's joint use of clauses (2) AND (3) that carries the difficulty; see `exists_mvPolynomial_factorization_mem_isEssentiallySmooth_flat`, which is still conditional.”.

> **Stacks 07FH, clause (2)**, in the generality of the tag. Let `k` be a field, let `Λ` be a
> Noetherian geometrically regular `k`-algebra, let `𝔮` be a prime of `Λ` and let `n ≥ 1`. Then
> there are `m ≥ 0` and a `k`-algebra map `φ : k[y_1, …, y_m] → Λ` such that, with
> `𝔭 = φ^{-1}(𝔮)`, one has `𝔭 Λ_𝔮 = 𝔮 Λ_𝔮` with `g : k[y_1, …, y_m]_𝔭 → Λ_𝔮` flat, and the map
> `k[y_1, …, y_m]_𝔭/𝔭^n → Λ_𝔮/𝔮^nΛ_𝔮` induced by `g` factors through a local Artinian subring `D`
> of `Λ_𝔮/𝔮^nΛ_𝔮` by an essentially smooth map followed by the inclusion of `D`, which is flat.
>
> "Essentially smooth" is `RingHom.IsEssentiallySmooth`: essentially of finite presentation
> (Tag 00QM (2)) and formally smooth. The Stacks Project never defines the term; see
> `StacksFrontier/RingTheory/Smoothing/EssentiallySmooth.lean`.

```lean
theorem exists_mvPolynomial_factorization_isEssentiallySmooth_flat
    {k Λ : Type u} [Field k] [CommRing Λ] [Algebra k Λ] [IsNoetherianRing Λ]
    [Algebra.IsGeometricallyRegular k Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime]
    {n : ℕ} (hn : 1 ≤ n) :
    ∃ (m : ℕ) (φ : MvPolynomial (Fin m) k →ₐ[k] Λ)
      (g : Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮) →+* Localization.AtPrime 𝔮)
      (u : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* primePowerQuotient 𝔮 n)
      (D : Subring (primePowerQuotient 𝔮 n))
      (a : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* D),
      Ideal.map ((algebraMap Λ (Localization.AtPrime 𝔮)).comp φ.toRingHom)
          (Ideal.comap φ.toRingHom 𝔮)
        = Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) 𝔮 ∧
      (∀ f, g (algebraMap (MvPolynomial (Fin m) k)
            (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) f)
          = algebraMap Λ (Localization.AtPrime 𝔮) (φ f)) ∧
      g.Flat ∧
      (∀ y, u (Ideal.Quotient.mk (Ideal.map (algebraMap (MvPolynomial (Fin m) k)
              (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)))
              (Ideal.comap φ.toRingHom 𝔮 ^ n)) y)
          = Ideal.Quotient.mk (Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) (𝔮 ^ n))
            (g y)) ∧
      (∀ z, (a z : primePowerQuotient 𝔮 n) = u z) ∧
      ∃ (_ : IsLocalRing D) (_ : IsArtinianRing D),
        a.IsEssentiallySmooth ∧ D.subtype.Flat
```

**`Stacks.Smoothing.exists_mvPolynomial_flat_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/FlatLocalization.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/FlatLocalization.lean#L231). The attribute's comment: “clause (1), unconditionally. The source's choice of `λ_1, …, λ_t ∈ Λ` whose differentials form a basis of `Ω_{F/k}` for the residue field `F` of an approximating subalgebra `A ⊆ Λ_𝔮/𝔮^nΛ_𝔮` of Stacks 07FG is not justified by the source's TEXT, which fixes `A` by 07FG and only afterwards asks for the `λ`, never enlarging `A` again: for SOME members of the directed family no such `λ` exist, the residues of those elements of `Λ` which land in `F` need not generate `F` (see the module docstring for the counterexample `Λ/𝔮 = k[x, y]`, `F = k(x/y)`). That is all the counterexample shows. It says nothing against the source's ROUTE, since `A` may be chosen for the purpose rather than taken as given, and `exists_coefficientStage_basis_kaehlerDifferential` chooses it so. The choice is not needed for clause (1) in any case: the clause is the source's own construction specialized to `F = k`, where `t = 0`, the fibre of `Λ_𝔮` over `k` is `Λ_𝔮` itself, and `λ_1, …, λ_m` is a regular system of parameters of `Λ_𝔮` lifted to `𝔮`. What the λ-choice is needed for is the essential smoothness in clause (2); only regularity of `Λ_𝔮`, not geometric regularity, is used here. `𝔭 Λ_𝔮 = 𝔮 Λ_𝔮` is the stated equality of extended ideals and the flat arrow is the unique `g` with `g ∘ (k[y] → k[y]_𝔭) = (k[y] → Λ → Λ_𝔮)`, flatness being `RingHom.Flat`. The source proves this from Lemma 07E6 and More on Algebra 15.36.2; the route here is miracle flatness, Lemma 00R4.”.

> **Stacks 07FH, clause (1).** Let `k` be a field, let `Λ` be a Noetherian `k`-algebra which is
> geometrically regular over `k` and let `𝔮` be a prime of `Λ`. Then there are `m ≥ 0` and a
> `k`-algebra map `φ : k[y_1, …, y_m] → Λ` such that, with `𝔭 = φ^{-1}(𝔮)`, one has
> `𝔭 Λ_𝔮 = 𝔮 Λ_𝔮` and the induced local map `k[y_1, …, y_m]_𝔭 → Λ_𝔮` is flat.

```lean
theorem exists_mvPolynomial_flat_localization {k Λ : Type u} [Field k] [CommRing Λ] [Algebra k Λ]
    [IsNoetherianRing Λ] [Algebra.IsGeometricallyRegular k Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime] :
    ∃ (m : ℕ) (φ : MvPolynomial (Fin m) k →ₐ[k] Λ)
      (g : Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮) →+* Localization.AtPrime 𝔮),
      Ideal.map ((algebraMap Λ (Localization.AtPrime 𝔮)).comp φ.toRingHom)
          (Ideal.comap φ.toRingHom 𝔮)
        = Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) 𝔮 ∧
      (∀ f, g (algebraMap (MvPolynomial (Fin m) k)
            (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) f)
          = algebraMap Λ (Localization.AtPrime 𝔮) (φ f)) ∧
      g.Flat
```

**`Stacks.Smoothing.exists_mvPolynomial_factorization_mem_isEssentiallySmooth_flat_of_charP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/GlobalStage.lean, line 718](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/GlobalStage.lean#L718). The attribute's comment: “All three clauses, in the generality of the tag: no hypothesis on κ(𝔮) beyond the tag's own (Λ Noetherian and geometrically regular over a field k of characteristic p, 𝔮 a prime, n ≥ 1, E a finite subset of Λ\_𝔮/𝔮^nΛ\_𝔮). Clause (1) is the ideal identity 𝔭Λ\_𝔮 = 𝔮Λ\_𝔮 together with flatness of k[y]\_𝔭 → Λ\_𝔮; clause (2) is the factorization of k[y]\_𝔭/𝔭^n → Λ\_𝔮/𝔮^nΛ\_𝔮 through a local Artinian subring D by an essentially smooth map followed by a flat one; clause (3) is E ⊆ D. `Essentially smooth' is RingHom.IsEssentiallySmooth: essentially of finite presentation (Tag 00QM (2)) and formally smooth; the Stacks Project never defines the term. The λ-choice of the source's proof is not justified by its text and is false for a general member of the directed family of 07FG; the repair implemented here is due to Brian Nugent and is described in the module docstring and in `exists\_global\_stage\_primePowerQuotient`.”.

> **Stacks 07FH, all three clauses, in the generality of the tag.** Let `k` be a field of
> characteristic `p > 0`, let `Λ` be a Noetherian geometrically regular `k`-algebra, let `𝔮` be a
> prime of `Λ`, let `n ≥ 1` and let `E` be a finite subset of `Λ̄ = Λ_𝔮/𝔮^nΛ_𝔮`. Then there are
> `m ≥ 0` and a `k`-algebra map `φ : k[y_1, …, y_m] → Λ` such that, with `𝔭 = φ^{-1}(𝔮)`:
>
> * `𝔭 Λ_𝔮 = 𝔮 Λ_𝔮` and the induced local map `g : k[y_1, …, y_m]_𝔭 → Λ_𝔮` is flat — clause (1);
> * the map `u : k[y_1, …, y_m]_𝔭/𝔭^n → Λ̄` induced by `g` factors through a local Artinian
>   subring `D` of `Λ̄` as an essentially smooth map `a` followed by the inclusion of `D`, which is
>   flat — clause (2);
> * `E ⊆ D` — clause (3).
>
> No hypothesis is placed on `κ(𝔮)`. **The proof of clause (3) is Brian Nugent's**: see
> `exists_global_stage_primePowerQuotient` for his repair of the λ-choice, which the source's text
> leaves unjustified and which is false for a general member of the directed family of Stacks 07FG
> (two counterexamples are recorded in the implementation notes, the second of them his). The two
> ingredients are that the generating family of `𝔪_Λ̄` used to build the approximating subalgebra
> `D` is kept GLOBAL — chosen in `𝔮 ⊆ Λ` once and for all, so that `exists_stage` still grants
> freeness and the fibre's regular parameters can be extracted from it as a subfamily by Nakayama —
> and that the coefficient field is pushed up to one generated by residues of global elements
> `s^P`, `a·s^{P-1}` whose images lie in `σ(F)`, where `σ(f) = q(a)/q(s)` is an exact relation in
> `Λ̄` and `P` is a `p`-power at least `n`. The pair `s^P`, `a·s^{P-1}` generates what neither
> member does: their residues are `α^P` and `f·α^P`, of ratio `f`.

```lean
theorem exists_mvPolynomial_factorization_mem_isEssentiallySmooth_flat_of_charP
    {k Λ : Type u} [Field k] [CommRing Λ] [Algebra k Λ] [IsNoetherianRing Λ]
    [Algebra.IsGeometricallyRegular k Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime] (p : ℕ) [Fact p.Prime]
    [CharP k p] {n : ℕ} (hn : 1 ≤ n) (E : Finset (primePowerQuotient 𝔮 n)) :
    ∃ (m : ℕ) (φ : MvPolynomial (Fin m) k →ₐ[k] Λ)
      (g : Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮) →+* Localization.AtPrime 𝔮)
      (u : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* primePowerQuotient 𝔮 n)
      (D : Subring (primePowerQuotient 𝔮 n))
      (a : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* D),
      Ideal.map ((algebraMap Λ (Localization.AtPrime 𝔮)).comp φ.toRingHom)
          (Ideal.comap φ.toRingHom 𝔮)
        = Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) 𝔮 ∧
      (∀ f, g (algebraMap (MvPolynomial (Fin m) k)
            (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) f)
          = algebraMap Λ (Localization.AtPrime 𝔮) (φ f)) ∧
      g.Flat ∧
      (∀ y, u (Ideal.Quotient.mk (Ideal.map (algebraMap (MvPolynomial (Fin m) k)
              (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)))
              (Ideal.comap φ.toRingHom 𝔮 ^ n)) y)
          = Ideal.Quotient.mk (Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) (𝔮 ^ n))
            (g y)) ∧
      (∀ z, (a z : primePowerQuotient 𝔮 n) = u z) ∧
      (∀ x ∈ E, x ∈ D) ∧
      ∃ (_ : IsLocalRing D) (_ : IsArtinianRing D),
        a.IsEssentiallySmooth ∧ D.subtype.Flat
```

## Tag 07FI, a lemma

[Tag 07FI](https://stacks.math.columbia.edu/tag/07FI) in the Stacks Project.

**`Stacks.Smoothing.exists_essentiallySmooth_enlargement_containing_pow_of_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/InseparableResidueField/EnlargementContainingPow.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/InseparableResidueField/EnlargementContainingPow.lean#L93). The attribute's comment: “in the full setup of Lemma 07FH: `Λ` Noetherian and geometrically regular over `k` of characteristic `p > 0`, `n ≥ 1`, `φ : k[y₁,…,y_m] → Λ` with clause (1) (`𝔭Λ_𝔮 = 𝔮Λ_𝔮`, `k[y]_𝔭 → Λ_𝔮` flat), the factorization `k[y]_𝔭/𝔭ⁿ → D → Λ_𝔮/𝔮ⁿΛ_𝔮` of clause (2) through a local Artinian `D` (first arrow essentially smooth, second flat) and the finite `E ⊆ D` of clause (3), and `λ ∉ 𝔮`. `D'` is a ring with an injective flat local map to `Λ_𝔮/𝔮ⁿΛ_𝔮`, and `λ^q ∈ D'` means the image of `λ^q` lies in its range. Essentially smooth is `RingHom.IsEssentiallySmooth` (essentially of finite presentation, Tag 00QM (2), and formally smooth)”.

> **Stacks 07FI.** Let `k` be a field of characteristic `p > 0`, let `Λ` be a Noetherian
> geometrically regular `k`-algebra, let `𝔮 ⊆ Λ` be a prime and let `n ≥ 1`. Let
> `φ : k[y₁, …, y_m] → Λ` be a `k`-algebra map, `𝔭 = φ⁻¹(𝔮)`, and suppose, as in Lemma 07FH,
>
> 1. `𝔭Λ_𝔮 = 𝔮Λ_𝔮` and `g : k[y₁, …, y_m]_𝔭 → Λ_𝔮` is flat;
> 2. the induced map `u : k[y₁, …, y_m]_𝔭/𝔭ⁿ → Λ_𝔮/𝔮ⁿΛ_𝔮` factors as `b ∘ a` through a local
>    Artinian ring `D`, with `a` essentially smooth and `b` flat;
> 3. a finite subset `E ⊆ Λ_𝔮/𝔮ⁿΛ_𝔮` is contained in `D`.
>
> Then for every `λ ∈ Λ ∖ 𝔮` there are an integer `q > 0` and a factorization
> `k[y₁, …, y_m]_𝔭/𝔭ⁿ → D → D' → Λ_𝔮/𝔮ⁿΛ_𝔮` of `u`, with `D'` local Artinian, `c : D → D'` an
> essentially smooth local homomorphism, `b' : D' → Λ_𝔮/𝔮ⁿΛ_𝔮` flat, local and injective (so
> that `D'` is a subring of `Λ_𝔮/𝔮ⁿΛ_𝔮`), `b' ∘ c = b`, and `λ^q ∈ D'`.

```lean
theorem exists_essentiallySmooth_enlargement_containing_pow_of_factorization
    {k Λ : Type u} [Field k] (p : ℕ) [CharP k p] (hp : 0 < p)
    [CommRing Λ] [Algebra k Λ] [IsNoetherianRing Λ] [Algebra.IsGeometricallyRegular k Λ]
    (𝔮 : Ideal Λ) [𝔮.IsPrime] {n : ℕ} (hn : 1 ≤ n)
    {m : ℕ} (φ : MvPolynomial (Fin m) k →ₐ[k] Λ)
    (g : Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮) →+* Localization.AtPrime 𝔮)
    (_hmap : Ideal.map ((algebraMap Λ (Localization.AtPrime 𝔮)).comp φ.toRingHom)
        (Ideal.comap φ.toRingHom 𝔮) = Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) 𝔮)
    (_hg : ∀ f, g (algebraMap (MvPolynomial (Fin m) k)
        (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) f)
          = algebraMap Λ (Localization.AtPrime 𝔮) (φ f))
    (_hgflat : g.Flat)
    (u : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* primePowerQuotient 𝔮 n)
    (_hu : ∀ y, u (Ideal.Quotient.mk (Ideal.map (algebraMap (MvPolynomial (Fin m) k)
          (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮))) (Ideal.comap φ.toRingHom 𝔮 ^ n)) y)
        = Ideal.Quotient.mk (Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) (𝔮 ^ n)) (g y))
    {D : Type u} [CommRing D] [IsLocalRing D] [IsArtinianRing D]
    (a : primePowerQuotient (Ideal.comap φ.toRingHom 𝔮) n →+* D)
    (b : D →+* primePowerQuotient 𝔮 n)
    (_ha : a.IsEssentiallySmooth) (hb : b.Flat) (hab : b.comp a = u)
    (E : Finset (primePowerQuotient 𝔮 n)) (_hE : ∀ x ∈ E, x ∈ b.range)
    (lam : Λ) (_hlam : lam ∉ 𝔮) :
    ∃ (q : ℕ) (D' : Type u) (_ : CommRing D') (_ : IsLocalRing D') (_ : IsArtinianRing D')
      (c : D →+* D') (b' : D' →+* primePowerQuotient 𝔮 n) (_ : IsLocalHom c)
      (_ : IsLocalHom b'),
      0 < q ∧ c.IsEssentiallySmooth ∧ b'.Flat ∧ b'.comp c = b ∧ (b'.comp c).comp a = u ∧
        Function.Injective b' ∧
        algebraMap Λ (primePowerQuotient 𝔮 n) (lam ^ q) ∈ b'.range
```

## Tag 07FJ, a lemma

[Tag 07FJ](https://stacks.math.columbia.edu/tag/07FJ) in the Stacks Project.

**`Stacks.Smoothing.canBeResolvedInPositiveCharacteristic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/TwistedQuotientClosure.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/TwistedQuotientClosure.lean#L291). The attribute's comment: “the lemma in full generality, with NO carried hypotheses: the whole of Situation 07F7 over a field of characteristic `p > 0`, with `𝔮` minimal over `𝔥_A`, and the conclusion `CanBeResolved k A Λ 𝔮`. Its two inputs are both proved in this library. The first is item (9), Stacks 07FT, `hasArtinianApproximationData`; the second is items (22)-(26), Stacks 07G6-07GA, `twistedQuotientLocallyResolvable`. The λ-choice in the source's proof of Stacks 07FH, on which 07FT turns, is not justified by the source's text and is false for a general member of the directed family of 07FG; the repair is due to BRIAN NUGENT, and is implemented in `exists_global_stage_primePowerQuotient`.”.

> **Stacks 07FJ.** Let `k → A → Λ ⊃ 𝔮` be as in Situation 07F7 with `k` of characteristic
> `p > 0`, `A` of finite presentation over `k`, `Λ` Noetherian and geometrically regular over `k`,
> and `𝔮` minimal over `𝔥_A`. Then the chain can be resolved at `𝔮`.
>
> This is `Stacks.Smoothing.canBeResolvedInPositiveCharacteristic_of_locallyResolvable` with both
> of its hypotheses discharged: item (9), Stacks 07FT, by
> `Stacks.Smoothing.hasArtinianApproximationData`, and items (22)–(26) by
> `Stacks.Smoothing.twistedQuotientLocallyResolvable` above. Every one of the twenty-six items of
> the source's proof is therefore proved.

```lean
theorem canBeResolvedInPositiveCharacteristic : CanBeResolvedInPositiveCharacteristic.{u}
```

## Tag 07FK, an item

[Tag 07FK](https://stacks.math.columbia.edu/tag/07FK) in the Stacks Project.

**`Stacks.Smoothing.LocalSmoothingSituation.exists_pos_map_pow_le_map_singularIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean#L60).

> **Stacks 07FK.** In a local smoothing situation with `Λ` Noetherian and `q` minimal over
> `𝔥_A = √(H_{A/R} Λ)`, some positive power of `q` extends into `H_{A/R} Λ_q`.

```lean
theorem exists_pos_map_pow_le_map_singularIdeal [IsNoetherianRing S.Λ]
    (hq : S.q ∈ S.radicalSingularIdealExtension.minimalPrimes) :
    ∃ N : ℕ, 0 < N ∧
      Ideal.map (algebraMap S.Λ (Localization.AtPrime S.q)) (S.q ^ N) ≤
        Ideal.map (algebraMap S.Λ (Localization.AtPrime S.q))
          (Ideal.map (algebraMap S.A S.Λ) (singularIdeal S.R S.A))
```

## Tag 07FL, an item

[Tag 07FL](https://stacks.math.columbia.edu/tag/07FL) in the Stacks Project.

**`Stacks.Smoothing.LocalSmoothingSituation.exists_fin_span_range_eq_singularIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean#L88).

> **Stacks 07FL.** The singular ideal `H_{A/R}` of a local smoothing situation is generated by
> finitely many elements of `A`.

```lean
theorem exists_fin_span_range_eq_singularIdeal :
    ∃ (t : ℕ) (a : Fin t → S.A), Ideal.span (Set.range a) = singularIdeal S.R S.A
```

## Tag 07FM, an item

[Tag 07FM](https://stacks.math.columbia.edu/tag/07FM) in the Stacks Project.

**`Stacks.Smoothing.LocalSmoothingSituation.exists_nat_eq_ringKrullDim_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/MinimalSingularPrime.lean#L97).

> **Stacks 07FM.** The Krull dimension of the localization `Λ_q` of a local smoothing situation
> with `Λ` Noetherian is a natural number.

```lean
theorem exists_nat_eq_ringKrullDim_localization [IsNoetherianRing S.Λ] :
    ∃ d : ℕ, ringKrullDim (Localization.AtPrime S.q) = (d : WithBot ℕ∞)
```

## Tag 07FN, an item

[Tag 07FN](https://stacks.math.columbia.edu/tag/07FN) in the Stacks Project.

**`Stacks.Smoothing.parameterPowerIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean#L51).

> The ideal `(x_i^{2N} - Σ_j z_{ij} a_j : i = 1, …, d)` of the polynomial ring
> `A[x_1, …, x_d, z_{ij}]`, whose variables are indexed by `Fin d ⊕ Fin d × Fin t` so that
> `x_i = X (Sum.inl i)` and `z_{ij} = X (Sum.inr (i, j))`.

```lean
noncomputable def parameterPowerIdeal {A : Type v} [CommRing A] (d : ℕ) {t : ℕ} (N : ℕ)
    (a : Fin t → A) : Ideal (MvPolynomial (Fin d ⊕ Fin d × Fin t) A)
```

**`Stacks.Smoothing.parameterPowerAlgebra`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean#L61).

> The algebra `B = A[x_1, …, x_d, z_{ij}]/(x_i^{2N} - Σ_j z_{ij} a_j)`: the algebra `A` with
> `d` generic elements `x_i` adjoined whose `2N`-th powers lie in the ideal generated by
> `a_1, …, a_t`.

```lean
abbrev parameterPowerAlgebra (A : Type v) [CommRing A] (d : ℕ) {t : ℕ} (N : ℕ)
    (a : Fin t → A) : Type v
```

## Tag 07FP, an item

[Tag 07FP](https://stacks.math.columbia.edu/tag/07FP) in the Stacks Project.

**`Stacks.Smoothing.exists_retraction_parameterPowerAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ParameterPowerAlgebra.lean#L129).

> Let `B = A[x_i, z_{ij}]/(x_i^{2N} - Σ_j z_{ij} a_j)`, viewed as a `k[x_1, …, x_d]`-algebra.
> There is a finite-type `B`-algebra `C`, of finite presentation over `k[x_1, …, x_d]`, with a
> `k[x_1, …, x_d]`-algebra retraction `C → B`, such that for each `b ∈ B`: if `B_b` is a local
> complete intersection over `k[x_1, …, x_d]`, then `C_b` is smooth over `B_b` and has a
> presentation over `k[x_1, …, x_d]` with free conormal module; and if `B_b` is smooth over
> `k[x_1, …, x_d]`, then the module of differentials of `C_b` over `k[x_1, …, x_d]` is free.

```lean
theorem exists_retraction_parameterPowerAlgebra (k : Type u) (A : Type v) [Field k] [CommRing A]
    [Algebra k A] [Algebra.FiniteType k A] (d : ℕ) {t : ℕ} (N : ℕ) (a : Fin t → A) :
    ∃ (C : Type v) (_ : CommRing C) (_ : Algebra (MvPolynomial (Fin d) k) C)
      (_ : Algebra (parameterPowerAlgebra A d N a) C)
      (_ : IsScalarTower (MvPolynomial (Fin d) k) (parameterPowerAlgebra A d N a) C)
      (_ : Algebra.FiniteType (parameterPowerAlgebra A d N a) C)
      (_ : Algebra.FinitePresentation (MvPolynomial (Fin d) k) C)
      (g : C →ₐ[MvPolynomial (Fin d) k] parameterPowerAlgebra A d N a),
      g.comp (IsScalarTower.toAlgHom (MvPolynomial (Fin d) k)
          (parameterPowerAlgebra A d N a) C) =
        AlgHom.id (MvPolynomial (Fin d) k) (parameterPowerAlgebra A d N a) ∧
      (∀ b : parameterPowerAlgebra A d N a,
        RingHom.IsLocalCompleteIntersection
            (algebraMap (MvPolynomial (Fin d) k) (Localization.Away b)) →
          (letI : Algebra (Localization.Away b)
              (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)) :=
            (Localization.awayMap
              (algebraMap (parameterPowerAlgebra A d N a) C) b).toAlgebra;
          Algebra.Smooth (Localization.Away b)
              (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)) ∧
            HasFreeConormalPresentation (MvPolynomial (Fin d) k)
              (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)))) ∧
      (∀ b : parameterPowerAlgebra A d N a,
        Algebra.Smooth (MvPolynomial (Fin d) k) (Localization.Away b) →
          Module.Free (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b))
            (KaehlerDifferential (MvPolynomial (Fin d) k)
              (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b))))
```

## Tag 07FQ, an item

[Tag 07FQ](https://stacks.math.columbia.edu/tag/07FQ) in the Stacks Project.

**`Stacks.Smoothing.exists_pos_isStrictlyStandard_X_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean#L594).

> **Stacks 07FQ.** Let `A` be of finite type over a field `k`, let `a_1, …, a_t` generate the
> singular ideal `H_{A/k}`, and let `C` be an algebra over `B = A[x\_i, z\_\{ij}]/(x\_i^\{2N} - Σ\_j
> z\_\{ij} a\_j)` with the two localization properties that Stacks 07FP supplies. Then some positive
> power `x_i^c`, one `c` for all `i`, is strictly standard in `C` over `k[x_1, …, x_d]`.

```lean
theorem exists_pos_isStrictlyStandard_X_pow (k : Type u) (A : Type v) [Field k] [CommRing A]
    [Algebra k A] [Algebra.FiniteType k A] (d N : ℕ) {t : ℕ} (a : Fin t → A)
    (ha : Ideal.span (Set.range a) = singularIdeal k A) (C : Type v) [CommRing C]
    [Algebra (MvPolynomial (Fin d) k) C] [Algebra (parameterPowerAlgebra A d N a) C]
    [IsScalarTower (MvPolynomial (Fin d) k) (parameterPowerAlgebra A d N a) C]
    [Algebra.FinitePresentation (MvPolynomial (Fin d) k) C]
    (hC₁ : ∀ b : parameterPowerAlgebra A d N a,
      RingHom.IsLocalCompleteIntersection
          (algebraMap (MvPolynomial (Fin d) k) (Localization.Away b)) →
        (letI : Algebra (Localization.Away b)
            (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)) :=
          (Localization.awayMap (algebraMap (parameterPowerAlgebra A d N a) C) b).toAlgebra
        Algebra.Smooth (Localization.Away b)
            (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)) ∧
          HasFreeConormalPresentation (MvPolynomial (Fin d) k)
            (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b))))
    (hC₂ : ∀ b : parameterPowerAlgebra A d N a,
      Algebra.Smooth (MvPolynomial (Fin d) k) (Localization.Away b) →
        Module.Free (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b))
          (KaehlerDifferential (MvPolynomial (Fin d) k)
            (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)))) :
    ∃ c : ℕ, 0 < c ∧ ∀ i : Fin d, IsStrictlyStandard (R := MvPolynomial (Fin d) k)
      (algebraMap (MvPolynomial (Fin d) k) C (MvPolynomial.X i) ^ c)
```

## Tag 07FR, an item

[Tag 07FR](https://stacks.math.columbia.edu/tag/07FR) in the Stacks Project.

**`Stacks.Smoothing.resolutionTruncationOrder`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean#L657).

> **Stacks 07FR.** The order `n = N + dc` to which the local ring `Λ_q` is truncated in the
> proof of Stacks 07FJ.

```lean
def resolutionTruncationOrder (N d c : ℕ) : ℕ
```

**`Stacks.Smoothing.resolutionPowerExponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean, line 663](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/StrictlyStandardParameterPowers.lean#L663).

> **Stacks 07FR.** The exponent `e = 8c` used in the proof of Stacks 07FJ: it is eight times
> the exponent `c` making `x_i^c` strictly standard, so that `γ_i^e = (γ_i^c)^8` is the eighth
> power required by Stacks 07F8.

```lean
def resolutionPowerExponent (c : ℕ) : ℕ
```

## Tag 07FS, an item

[Tag 07FS](https://stacks.math.columbia.edu/tag/07FS) in the Stacks Project.

**`Stacks.Smoothing.exists_finset_primePowerQuotient_eq_image_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean#L77). The attribute's comment: “Item 8 of the proof of Stacks 07FJ. `E` is produced as a `Finset` of `Λ_𝔮/𝔮^nΛ_𝔮`, which is the shape in which clause (3) of Stacks 07FH consumes it; the generating family of `A` is a `Finset` because `A` is of finite type over `k`.”.

> **Stacks 07FS.** Let `A` be a `k`-algebra of finite type mapping to a ring `Λ` with a prime
> `𝔮`, and let `n` be an exponent. Then `A` has a finite `k`-algebra generating family whose image
> in `Λ_𝔮/𝔮^nΛ_𝔮` is a finite subset of that ring.

```lean
theorem exists_finset_primePowerQuotient_eq_image_generators (k : Type u) (A : Type v)
    (Λ : Type w) [CommRing k] [CommRing A] [Algebra k A] [Algebra.FiniteType k A] [CommRing Λ]
    [Algebra A Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime] (n : ℕ) :
    ∃ (s : Finset A) (E : Finset (primePowerQuotient 𝔮 n)),
      Algebra.adjoin k (s : Set A) = ⊤ ∧
      (E : Set (primePowerQuotient 𝔮 n)) =
        toPrimePowerQuotient 𝔮 n '' (algebraMap A Λ '' (s : Set A))
```

## Tag 07FT, an item

[Tag 07FT](https://stacks.math.columbia.edu/tag/07FT) in the Stacks Project.

**`Stacks.Smoothing.hasArtinianApproximationData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianApproximationGeneral.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianApproximationGeneral.lean#L85). The attribute's comment: “The lemma in full generality: for every field k of characteristic p > 0, every Noetherian geometrically regular k-algebra Λ, every prime 𝔮 of Λ, every n ≥ 1 and every finite subset E of Λ\_𝔮/𝔮^nΛ\_𝔮, there are m and a k-algebra map φ : k[y\_1, …, y\_m] → Λ such that, with 𝔭 = φ⁻¹(𝔮), the induced local map k[y]\_𝔭 → Λ\_𝔮 is flat with 𝔭Λ\_𝔮 = 𝔮Λ\_𝔮, and the induced map k[y]\_𝔭/𝔭^n → Λ\_𝔮/𝔮^nΛ\_𝔮 factors through a local Artinian subring D containing E by an essentially smooth map followed by a flat one. The three clauses of Stacks 07FH that this consumes are proved in `Stacks.Smoothing.exists_mvPolynomial_factorization_mem_isEssentiallySmooth_flat_of_charP`; the λ-choice of the source's proof of 07FH is not justified by its text and is false for a general member of the directed family of 07FG, and the repair is due to Brian Nugent.”.

> **Stacks 07FT in full generality**, the predicate
> `Stacks.Smoothing.HasArtinianApproximationData` proved: for every field `k` of characteristic
> `p > 0`, every Noetherian geometrically regular `k`-algebra `Λ`, every prime `𝔮` of `Λ`, every
> `n ≥ 1` and every finite subset `E` of `Λ_𝔮/𝔮^nΛ_𝔮`, the Artinian approximation data exist.
>
> This was item (9) of the proof of Stacks 07FJ, carried as a hypothesis there and in
> `Stacks.Smoothing.TwistedQuotientResolution`. The λ-choice of Stacks 07FH, on which it turns, is
> not justified by the source's text; **the repair implemented here is due to Brian Nugent**.
>
> This is the only declaration carrying `@[stacks 07FT]`: the special case
> `Stacks.Smoothing.exists_mvPolynomial_localArtinianFactorization_mem`, which assumes in addition
> that the residue field `κ(𝔮)` is essentially of finite type over `k`, is untagged.

```lean
theorem hasArtinianApproximationData : HasArtinianApproximationData.{u}
```

## Tag 07FU, an item

[Tag 07FU](https://stacks.math.columbia.edu/tag/07FU) in the Stacks Project.

**`Stacks.Smoothing.exists_fin_mem_span_eq_maximalIdeal_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean#L254). The attribute's comment: “Item 10 of the proof of Stacks 07FJ. `d` is `dim Λ_𝔮` of item 07FM, and the first thing proved is that it is also `dim k[y_1, …, y_m]_𝔭`: `𝔭Λ_𝔮 = 𝔮Λ_𝔮` makes the fibre of `g` over the closed point a field, and `g` is flat, hence satisfies going down, so Stacks 00ON gives `height 𝔮Λ_𝔮 = height 𝔭k[y]_𝔭 + 0`. A polynomial ring over a field is regular, so `k[y]_𝔭` is a regular local ring and its maximal ideal is generated by `dim k[y]_𝔭` elements; each may be taken to be the image of an element of `𝔭`, because an element of the maximal ideal of a localization is a unit multiple of such an image. `d` elements of `𝔭` whose images generate the maximal ideal of the `d`-dimensional regular local ring `k[y]_𝔭` is exactly a regular system of parameters of `k[y]_𝔭`, and the dimension equality is part of the conclusion so that this reading is pinned down. The hypotheses are the part of item 07FT that the step uses: `φ`, the flat `g` compatible with `φ`, and the ideal identity.”.

> **Stacks 07FU.** Let `𝔮` be a prime of a Noetherian ring `Λ`, let `𝔭` be the contraction of
> `𝔮` along a `k`-algebra map `φ : k[y_1, …, y_m] → Λ` and suppose the induced map
> `g : k[y_1, …, y_m]_𝔭 → Λ_𝔮` is flat with `𝔭Λ_𝔮 = 𝔮Λ_𝔮`. If `d = dim Λ_𝔮`, then
> `dim k[y_1, …, y_m]_𝔭 = d` and there are `π_1, …, π_d ∈ 𝔭` whose images generate the maximal
> ideal of `k[y_1, …, y_m]_𝔭`, that is, form a regular system of parameters of it.

```lean
theorem exists_fin_mem_span_eq_maximalIdeal_of_flat {k : Type u} [Field k] {Λ : Type v}
    [CommRing Λ] [Algebra k Λ] [IsNoetherianRing Λ] (𝔮 : Ideal Λ) [𝔮.IsPrime] {m : ℕ}
    (φ : MvPolynomial (Fin m) k →ₐ[k] Λ)
    (g : Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮) →+* Localization.AtPrime 𝔮)
    (hmap : Ideal.map ((algebraMap Λ (Localization.AtPrime 𝔮)).comp φ.toRingHom)
          (Ideal.comap φ.toRingHom 𝔮)
        = Ideal.map (algebraMap Λ (Localization.AtPrime 𝔮)) 𝔮)
    (hg : ∀ f, g (algebraMap (MvPolynomial (Fin m) k)
          (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) f)
        = algebraMap Λ (Localization.AtPrime 𝔮) (φ f))
    (hgflat : g.Flat) {d : ℕ}
    (hd : ringKrullDim (Localization.AtPrime 𝔮) = (d : WithBot ℕ∞)) :
    ringKrullDim (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) = (d : WithBot ℕ∞) ∧
      ∃ π : Fin d → MvPolynomial (Fin m) k, (∀ i, π i ∈ Ideal.comap φ.toRingHom 𝔮) ∧
        Ideal.span (Set.range fun i => algebraMap (MvPolynomial (Fin m) k)
            (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮)) (π i))
          = maximalIdeal (Localization.AtPrime (Ideal.comap φ.toRingHom 𝔮))
```

## Tag 07FV, an item

[Tag 07FV](https://stacks.math.columbia.edu/tag/07FV) in the Stacks Project.

**`Stacks.Smoothing.parameterScalingRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean#L324). The attribute's comment: “Item 11 of the proof of Stacks 07FJ, with one correction: the source writes `R = k[y_1, …, y_m, t_1, …, t_m]`, but the `t`-block has `d` members, not `m`. Every later use of `R` in the proof writes `k[y_1, …, y_m, t_1, …, t_d]` — items 07FZ, 07G3 and 07G9, and repeatedly in the justifications — and `γ_i = π_i t_i` is defined only for `i = 1, …, d`, the `π_i` being the `d` elements supplied by item 07FU, with `I = (γ_1^e, …, γ_d^e)` in item 07G1. `R` is `MvPolynomial (Fin m ⊕ Fin d) k` with `y_j = X (Sum.inl j)` and `t_i = X (Sum.inr i)`; the `k`-algebra map `k[y_1, …, y_m] → R` of the source is `MvPolynomial.rename Sum.inl`.”.

> The polynomial ring `R = k[y_1, …, y_m, t_1, …, t_d]`, with `y_j = X (Sum.inl j)` the
> variables of the polynomial ring of Stacks 07FT and `t_i = X (Sum.inr i)` one new variable for
> each member of the regular system of parameters of Stacks 07FU.

```lean
abbrev parameterScalingRing (k : Type u) [CommRing k] (m d : ℕ) : Type u
```

**`Stacks.Smoothing.parameterScalingGen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianApproximationData.lean#L332). The attribute's comment: “Item 11 of the proof of Stacks 07FJ; see `parameterScalingRing` for the correction to the source's `R`. `γ_i` is defined for `i = 1, …, d`, matching the `d` elements `π_i` of item 07FU.”.

> The element `γ_i = π_i t_i` of `R = k[y_1, …, y_m, t_1, …, t_d]`: the `i`-th member of a
> family `π_1, …, π_d` in `k[y_1, …, y_m]`, scaled by the new variable `t_i`.

```lean
noncomputable def parameterScalingGen {k : Type u} [CommRing k] {m d : ℕ}
    (π : Fin d → MvPolynomial (Fin m) k) (i : Fin d) : parameterScalingRing k m d
```

## Tag 07FW, an item

[Tag 07FW](https://stacks.math.columbia.edu/tag/07FW) in the Stacks Project.

**`Stacks.Smoothing.exists_annihilator_scaledVariable_sq_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/AnnihilatorStabilizedParameters.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/AnnihilatorStabilizedParameters.lean#L244). The attribute's comment: “the source's `R = k[y_1, …, y_m]` is an arbitrary Noetherian ring `P`, and the data of (07FU) — the lifts of a regular system of parameters of `P_p` — are the hypotheses on `π`; `γ_i = π_i t_i` is `scaledVariable π i`”.

> **Stacks 07FW.** Let `P` be a Noetherian ring, let `p ⊂ P` be a prime such that `P_p` is a
> regular local ring of dimension `d`, and let `π₁, …, π_d ∈ P` map to a regular system of
> parameters of `P_p`. For every `e > 0` the `π_i` may be rescaled by elements of `P \ p`, which
> leaves them a regular system of parameters, so that in `R ⧸ (γ₁ ^ e, …, γ_{i-1} ^ e)` the
> annihilator of `γ_i` is the annihilator of `γ_i ^ 2`, where `R = P[t₁, …, t_d]` and
> `γ_i = π_i t_i`.

```lean
theorem exists_annihilator_scaledVariable_sq_eq {P : Type u} [CommRing P] [IsNoetherianRing P]
    (p : Ideal P) [p.IsPrime] [IsRegularLocalRing (Localization.AtPrime p)] {d : ℕ}
    (hd : ringKrullDim (Localization.AtPrime p) = d) (π : Fin d → P)
    (hspan : Ideal.span (Set.range fun i => algebraMap P (Localization.AtPrime p) (π i)) =
      IsLocalRing.maximalIdeal (Localization.AtPrime p))
    {e : ℕ} (he : 0 < e) :
    ∃ π' : Fin d → P, (∀ i, ∃ s ∈ p.primeCompl, π' i = s * π i) ∧
      Ideal.span (Set.range fun i => algebraMap P (Localization.AtPrime p) (π' i)) =
        IsLocalRing.maximalIdeal (Localization.AtPrime p) ∧
      ∀ i : Fin d, ∀ x : MvPolynomial (Fin d) P ⧸ Ideal.span (Set.range fun j : Fin i.1 =>
          scaledVariable π' (j.castLE (Nat.le_of_lt i.2)) ^ e),
        x * Ideal.Quotient.mk _ (scaledVariable π' i) = 0 ↔
          x * Ideal.Quotient.mk _ (scaledVariable π' i ^ 2) = 0
```

## Tag 07FX, an item

[Tag 07FX](https://stacks.math.columbia.edu/tag/07FX) in the Stacks Project.

**`Stacks.Smoothing.exists_essentiallySmooth_enlargement_annihilator_sq_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/AnnihilatorStabilizedParameters.lean, line 602](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/AnnihilatorStabilizedParameters.lean#L602). The attribute's comment: “the data of (07FT) — the Artinian local `D`, the flat local `D → Λ_q/q^nΛ_q`, and the memberships of the generators of `A` — are hypotheses, as are the lifts of (07FU); `H_{A/k}Λ` is the ideal generated by the images `a_1, …, a_r` and `(a)` is stated as the relation in `Λ` together with the reduction of each `λ_{ij}` into the image of `D'`”.

> **Stacks 07FX.** In the situation of Stacks 07FJ, with `N ≤ n`, `q ^ N Λ_q ⊆ (a_1, …, a_r)Λ_q`
> and `π_1, …, π_d ∈ q` lifting a regular system of parameters of `Λ_q`, suppose the `a_j` and the
> `π_i` reduce in `Λ_q/q^nΛ_q` into the image of an Artinian local ring `D` mapping to
> `Λ_q/q^nΛ_q` by a flat local homomorphism. Then there are `δ_1, …, δ_d ∈ Λ \ q` and a
> factorization `D → D' → Λ_q/q^nΛ_q` with `D'` Artinian local, `D → D'` essentially smooth and
> `D' → Λ_q/q^nΛ_q` flat and local, such that, writing `π'_i = δ_i π_i`:
> `(π'_i)^{2N} = Σ_j a_j λ_{ij}` in `Λ` with every `λ_{ij}` reducing into the image of `D'`; the
> annihilator of `π'_i` in `Λ ⧸ ((π'_1)^e, …, (π'_{i-1})^e)` is the annihilator of `(π'_i)^2`; and
> every `δ_i` reduces into the image of `D'`.

```lean
theorem exists_essentiallySmooth_enlargement_annihilator_sq_eq
    (k : Type u) [Field k] (p : ℕ) [CharP k p] (hp : 0 < p)
    (Λ : Type u) [CommRing Λ] [IsNoetherianRing Λ] [Algebra k Λ]
    (q : Ideal Λ) [q.IsPrime] [IsRegularLocalRing (Localization.AtPrime q)]
    {d r N n e : ℕ} (hd : ringKrullDim (Localization.AtPrime q) = d)
    (hN : 0 < N) (hn : N ≤ n) (he : 0 < e)
    [IsLocalRing (truncatedLocalization Λ q n)] [IsArtinianRing (truncatedLocalization Λ q n)]
    (a : Fin r → Λ)
    (hqN : Ideal.map (algebraMap Λ (Localization.AtPrime q)) (q ^ N) ≤
      Ideal.map (algebraMap Λ (Localization.AtPrime q)) (Ideal.span (Set.range a)))
    (π : Fin d → Λ) (hπq : ∀ i, π i ∈ q)
    (hπspan : Ideal.span (Set.range fun i => algebraMap Λ (Localization.AtPrime q) (π i)) =
      IsLocalRing.maximalIdeal (Localization.AtPrime q))
    {D : Type u} [CommRing D] [IsLocalRing D] [IsArtinianRing D]
    (b : D →+* truncatedLocalization Λ q n) [IsLocalHom b] (hb : RingHom.Flat b)
    (haD : ∀ j, ∃ w : D, b w = algebraMap Λ (truncatedLocalization Λ q n) (a j))
    (hπD : ∀ i, ∃ w : D, b w = algebraMap Λ (truncatedLocalization Λ q n) (π i)) :
    ∃ (δ : Fin d → Λ) (lam : Fin d → Fin r → Λ) (D' : Type u) (_ : CommRing D')
      (_ : IsLocalRing D') (_ : IsArtinianRing D') (c : D →+* D')
      (b' : D' →+* truncatedLocalization Λ q n) (_ : IsLocalHom c) (_ : IsLocalHom b'),
      c.IsEssentiallySmooth ∧ RingHom.Flat b' ∧ b'.comp c = b ∧
      (∀ i, δ i ∈ q.primeCompl) ∧
      (∀ i, (δ i * π i) ^ (2 * N) = ∑ j, a j * lam i j) ∧
      (∀ i j, ∃ w : D', b' w = algebraMap Λ (truncatedLocalization Λ q n) (lam i j)) ∧
      (∀ i, ∃ w : D', b' w = algebraMap Λ (truncatedLocalization Λ q n) (δ i)) ∧
      (∀ i : Fin d, ∀ x : Λ ⧸ Ideal.span (Set.range fun j : Fin i.1 =>
          (δ (j.castLE (Nat.le_of_lt i.2)) * π (j.castLE (Nat.le_of_lt i.2))) ^ e),
        x * Ideal.Quotient.mk _ (δ i * π i) = 0 ↔
          x * Ideal.Quotient.mk _ ((δ i * π i) ^ 2) = 0)
```

## Tag 07FY, an item

[Tag 07FY](https://stacks.math.columbia.edu/tag/07FY) in the Stacks Project.

**`Stacks.Smoothing.parameterPowerAlgebraToTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L101).

> The `A`-algebra map `B = A[x_i, z_{ij}]/(x_i^{2N} - Σ_j z_{ij} a_j) → Λ` sending `x_i` to
> `π'_i` and `z_{ij}` to `λ_{ij}`, where `(π'_i)^{2N} = Σ_j a_j λ_{ij}` in `Λ`.

```lean
noncomputable def parameterPowerAlgebraToTarget {A : Type v} {Λ : Type w} [CommRing A]
    [CommRing Λ] [Algebra A Λ] {d t : ℕ} (N : ℕ) (a : Fin t → A) (π' : Fin d → Λ)
    (lam : Fin d → Fin t → Λ)
    (hπ' : ∀ i, π' i ^ (2 * N) = ∑ j, algebraMap A Λ (a j) * lam i j) :
    parameterPowerAlgebra A d N a →ₐ[A] Λ
```

**`Stacks.Smoothing.improvedAlgebraToTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L145).

> The ring map `C → Λ` obtained by composing the `k[x_1, …, x_d]`-algebra retraction `g : C → B`
> of Stacks 07FP with the map `B → Λ` of `Stacks.Smoothing.parameterPowerAlgebraToTarget`.

```lean
noncomputable def improvedAlgebraToTarget {k : Type u} {A : Type v} {Λ : Type w} {C : Type v}
    [CommRing k] [CommRing A] [CommRing Λ] [CommRing C] [Algebra k A] [Algebra A Λ] {d t : ℕ}
    [Algebra (MvPolynomial (Fin d) k) C] (N : ℕ) (a : Fin t → A) (π' : Fin d → Λ)
    (lam : Fin d → Fin t → Λ)
    (hπ' : ∀ i, π' i ^ (2 * N) = ∑ j, algebraMap A Λ (a j) * lam i j)
    (g : C →ₐ[MvPolynomial (Fin d) k] parameterPowerAlgebra A d N a) : C →+* Λ
```

## Tag 07FZ, an item

[Tag 07FZ](https://stacks.math.columbia.edu/tag/07FZ) in the Stacks Project.

**`Stacks.Smoothing.twistedBaseToTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L176).

> The `k`-algebra map `R = k[y_1, …, y_m, t_1, …, t_d] → Λ` which is a given
> `φ : k[y_1, …, y_m] → Λ` on the variables `y_j` and sends `t_i` to `δ_i ∈ Λ`.

```lean
noncomputable def twistedBaseToTarget {k : Type u} {Λ : Type w} [CommRing k] [CommRing Λ]
    [Algebra k Λ] {m d : ℕ} (φ : MvPolynomial (Fin m) k →ₐ[k] Λ) (δ : Fin d → Λ) :
    MvPolynomial (Fin m ⊕ Fin d) k →ₐ[k] Λ
```

**`Stacks.Smoothing.twistedBaseHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L200).

> The `k`-algebra map `k[x_1, …, x_d] → R = k[y_1, …, y_m, t_1, …, t_d]` sending `x_i` to the
> twisted parameter `γ_i = π_i t_i`.

```lean
noncomputable def twistedBaseHom {k : Type u} [CommRing k] {m d : ℕ}
    (π : Fin d → MvPolynomial (Fin m) k) :
    MvPolynomial (Fin d) k →ₐ[k] MvPolynomial (Fin m ⊕ Fin d) k
```

## Tag 07G0, an item

[Tag 07G0](https://stacks.math.columbia.edu/tag/07G0) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_canBeResolved_twistedBase_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/TwistedBaseChangeReduction.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/TwistedBaseChangeReduction.lean#L60).

> **Stacks 07G0.** Let `k` be a field, `A` a finite type `k`-algebra with
> `H_{A/k} = (a_1, …, a_t)`, `A → Λ` a `k`-algebra map and `q ⊂ Λ`. Let
> `B = A[x_1, …, x_d, z_{ij}]/(x_i^{2N} - Σ_j z_{ij} a_j)` and let `B → C` be as in Stacks 07CE
> (07FP), with `k[x_1, …, x_d]`-algebra retraction `g : C → B`. Let `φ : k[y_1, …, y_m] → Λ`,
> `π_1, …, π_d ∈ k[y_1, …, y_m]`, `δ_1, …, δ_d ∈ Λ` and `λ_{ij} ∈ Λ` with
> `(π'_i)^{2N} = Σ_j a_j λ_{ij}` for `π'_i = δ_i π_i`; map `B → Λ` by `x_i ↦ π'_i`,
> `z_{ij} ↦ λ_{ij}` and `C → Λ` through `g` (step (14)); let `R = k[y_1, …, y_m, t_1, …, t_d]`
> map to `Λ` by `φ` and `t_i ↦ δ_i`, and `k[x_1, …, x_d] → R` by `x_i ↦ γ_i = π_i t_i` (step
> (15)). Then it suffices to resolve `R → C ⊗_{k[x_1, …, x_d]} R → Λ ⊃ q`, where
> `C ⊗_{k[x_1, …, x_d]} R → Λ` is induced by the two maps `C → Λ` and `R → Λ`.
>
> The base change is written `R ⊗_{k[x_1, …, x_d]} C`, the same ring with its two factors swapped,
> for which the `R`-algebra structure is Mathlib's canonical one. The structure maps
> `k[x_1, …, x_d] → R`, `R → Λ` and `R ⊗_{k[x_1, …, x_d]} C → Λ` are arbitrary instances pinned
> down by `hR`, `hRΛ` and `hTΛ` to the maps of steps (14)–(15). The further properties of the `π_i`
> and `δ_i` chosen in steps (10)–(13) are not needed for this step.

```lean
theorem canBeResolved_of_canBeResolved_twistedBase_tensorProduct {k : Type u} {A : Type u}
    {Λ : Type w} {C : Type u} [Field k] [CommRing A] [CommRing Λ] [CommRing C] [Algebra k A]
    [Algebra k Λ] [Algebra A Λ] [IsScalarTower k A Λ] [Algebra.FiniteType k A] {t d N m : ℕ}
    (a : Fin t → A) (ha : Ideal.span (Set.range a) = singularIdeal k A)
    [Algebra (MvPolynomial (Fin d) k) C] [Algebra (parameterPowerAlgebra A d N a) C]
    [IsScalarTower (MvPolynomial (Fin d) k) (parameterPowerAlgebra A d N a) C]
    [Algebra.FinitePresentation (MvPolynomial (Fin d) k) C]
    (g : C →ₐ[MvPolynomial (Fin d) k] parameterPowerAlgebra A d N a)
    (hg : g.comp (IsScalarTower.toAlgHom (MvPolynomial (Fin d) k)
        (parameterPowerAlgebra A d N a) C) =
      AlgHom.id (MvPolynomial (Fin d) k) (parameterPowerAlgebra A d N a))
    (hC : ∀ b : parameterPowerAlgebra A d N a,
      RingHom.IsLocalCompleteIntersection
          (algebraMap (MvPolynomial (Fin d) k) (Localization.Away b)) →
      (letI : Algebra (Localization.Away b)
          (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b)) :=
        (Localization.awayMap (algebraMap (parameterPowerAlgebra A d N a) C) b).toAlgebra
      Algebra.Smooth (Localization.Away b)
        (Localization.Away (algebraMap (parameterPowerAlgebra A d N a) C b))))
    (φ : MvPolynomial (Fin m) k →ₐ[k] Λ) (π : Fin d → MvPolynomial (Fin m) k) (δ : Fin d → Λ)
    (lam : Fin d → Fin t → Λ)
    (hrel : ∀ i, (δ i * φ (π i)) ^ (2 * N) = ∑ j, algebraMap A Λ (a j) * lam i j)
    [Algebra (MvPolynomial (Fin d) k) (MvPolynomial (Fin m ⊕ Fin d) k)]
    (hR : algebraMap (MvPolynomial (Fin d) k) (MvPolynomial (Fin m ⊕ Fin d) k) =
      (twistedBaseHom π).toRingHom)
    [Algebra (MvPolynomial (Fin m ⊕ Fin d) k) Λ]
    (hRΛ : algebraMap (MvPolynomial (Fin m ⊕ Fin d) k) Λ = (twistedBaseToTarget φ δ).toRingHom)
    [Algebra (MvPolynomial (Fin m ⊕ Fin d) k ⊗[MvPolynomial (Fin d) k] C) Λ]
    [IsScalarTower (MvPolynomial (Fin m ⊕ Fin d) k)
      (MvPolynomial (Fin m ⊕ Fin d) k ⊗[MvPolynomial (Fin d) k] C) Λ]
    (hTΛ : ∀ (r : MvPolynomial (Fin m ⊕ Fin d) k) (c : C),
      algebraMap (MvPolynomial (Fin m ⊕ Fin d) k ⊗[MvPolynomial (Fin d) k] C) Λ (r ⊗ₜ c) =
        twistedBaseToTarget φ δ r *
          improvedAlgebraToTarget N a (fun i => δ i * φ (π i)) lam hrel g c)
    (q : Ideal Λ)
    (h : CanBeResolved (MvPolynomial (Fin m ⊕ Fin d) k)
      (MvPolynomial (Fin m ⊕ Fin d) k ⊗[MvPolynomial (Fin d) k] C) Λ q) :
    CanBeResolved k A Λ q
```

## Tag 07G1, an item

[Tag 07G1](https://stacks.math.columbia.edu/tag/07G1) in the Stacks Project.

**`Stacks.Smoothing.twistedParameterPowerIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L215).

> The ideal `I = (γ_1^e, …, γ_d^e)` of `R = k[y_1, …, y_m, t_1, …, t_d]` generated by the `e`-th
> powers of the twisted parameters.

```lean
noncomputable def twistedParameterPowerIdeal {k : Type u} [CommRing k] {m d : ℕ}
    (π : Fin d → MvPolynomial (Fin m) k) (e : ℕ) : Ideal (MvPolynomial (Fin m ⊕ Fin d) k)
```

## Tag 07G2, an item

[Tag 07G2](https://stacks.math.columbia.edu/tag/07G2) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_quotient_span_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L481). The attribute's comment: “for arbitrary γ\_1, …, γ\_d ∈ R, d ≥ 1”.

> Let `R → D → Λ ⊃ q` be a chain with `R` Noetherian and `D` of finite presentation over `R`, let
> `γ_1, …, γ_d ∈ R` with `d ≥ 1`, and let `I = (γ_1^{8c}, …, γ_d^{8c})`. Assume each `γ_i^c` maps
> into `q`, is strictly standard in `D` over `R`, and has the annihilator condition of Stacks 07FW
> and 07FX in `R` and in `Λ` modulo the eighth powers of `γ_1^c, …, γ_{i-1}^c`. Then resolving
> `R/I → D/ID → Λ/IΛ` resolves `R → D → Λ ⊃ q`.

```lean
theorem canBeResolved_of_quotient_span_pow {R : Type u} {D : Type v} {Λ : Type w} [CommRing R]
    [CommRing D] [CommRing Λ] [Algebra R D] [Algebra D Λ] [Algebra R Λ] [IsScalarTower R D Λ]
    [IsNoetherianRing R] [Algebra.FinitePresentation R D] (q : Ideal Λ) [q.IsPrime] {d : ℕ}
    (hd : 1 ≤ d) (γ : Fin d → R) (c : ℕ) (I : Ideal R)
    (hI : I = Ideal.span (Set.range fun i => γ i ^ (8 * c)))
    (hγq : ∀ i, algebraMap R Λ (γ i ^ c) ∈ q)
    (hannR : ∀ i,
      let K := eighthPowerPrefixIdeal (fun i => γ i ^ c) i
      (Submodule.span (R ⧸ K) {Ideal.Quotient.mk K (γ i ^ c)}).annihilator =
        (Submodule.span (R ⧸ K) {(Ideal.Quotient.mk K (γ i ^ c)) ^ 2}).annihilator)
    (hannΛ : ∀ i,
      let K := Ideal.map (algebraMap R Λ) (eighthPowerPrefixIdeal (fun i => γ i ^ c) i)
      (Submodule.span (Λ ⧸ K)
          {Ideal.Quotient.mk K (algebraMap R Λ (γ i ^ c))}).annihilator =
        (Submodule.span (Λ ⧸ K)
          {(Ideal.Quotient.mk K (algebraMap R Λ (γ i ^ c))) ^ 2}).annihilator)
    (hstd : ∀ i, IsStrictlyStandard (R := R) (A := D) (algebraMap R D (γ i ^ c)))
    (hresolve :
      let ID := Ideal.map (algebraMap R D) I
      let IΛ := Ideal.map (algebraMap D Λ) ID
      letI : Algebra (R ⧸ I) (Λ ⧸ IΛ) :=
        ((algebraMap (D ⧸ ID) (Λ ⧸ IΛ)).comp (algebraMap (R ⧸ I) (D ⧸ ID))).toAlgebra
      letI : IsScalarTower (R ⧸ I) (D ⧸ ID) (Λ ⧸ IΛ) :=
        IsScalarTower.of_algebraMap_eq (fun _ => rfl)
      CanBeResolved (R ⧸ I) (D ⧸ ID) (Λ ⧸ IΛ) (Ideal.map (Ideal.Quotient.mk IΛ) q)) :
    CanBeResolved R D Λ q
```

## Tag 07G3, an item

[Tag 07G3](https://stacks.math.columbia.edu/tag/07G3) in the Stacks Project.

**`Stacks.Smoothing.twistedBasePrime`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L222).

> The prime `r ⊂ R = k[y_1, …, y_m, t_1, …, t_d]` which is the inverse image of `q ⊂ Λ` under the
> map of `Stacks.Smoothing.twistedBaseToTarget`.

```lean
noncomputable def twistedBasePrime {k : Type u} {Λ : Type w} [CommRing k] [CommRing Λ]
    [Algebra k Λ] {m d : ℕ} (φ : MvPolynomial (Fin m) k →ₐ[k] Λ) (δ : Fin d → Λ) (q : Ideal Λ) :
    Ideal (MvPolynomial (Fin m ⊕ Fin d) k)
```

## Tag 07G4, an item

[Tag 07G4](https://stacks.math.columbia.edu/tag/07G4) in the Stacks Project.

**`Stacks.Smoothing.LocalSmoothingSituation.canBeResolved_of_nilpotent_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L346). The attribute's comment: “for a chain whose localized target has maximal ideal generated by finitely many nilpotents, which is the form taken by the quotient by (γ\_1^e, …, γ\_d^e)”.

> **Stacks 07FJ, step 20** (tag 07G4). It suffices to resolve the localized chain
> `(R/I)_𝔯 → C ⊗ (R/I)_𝔯 → Λ_𝔮/IΛ_𝔮`: a chain `R → A → Λ ⊃ 𝔮` whose prime is minimal over
> `𝔥_A`, whose localized chain can be resolved, and in whose localization `Λ_𝔮` the maximal ideal
> is generated by finitely many nilpotent elements, can be resolved. The last condition is the
> one supplied by the step: the images of the parameters `π_1, …, π_d` generate the maximal ideal
> and their `e`-th powers already lie in the ideal `I` divided out.

```lean
theorem LocalSmoothingSituation.canBeResolved_of_nilpotent_generators
    (S : LocalSmoothingSituation.{u, v, w}) {d : ℕ} (π : Fin d → Localization.AtPrime S.q)
    (hgen : IsLocalRing.maximalIdeal (Localization.AtPrime S.q) = Ideal.span (Set.range π))
    (hnil : ∀ i, IsNilpotent (π i))
    (hq : S.q ∈ S.radicalSingularIdealExtension.minimalPrimes)
    (hres : S.IsResolvableAfterLocalizing) : S.CanBeResolved
```

## Tag 07G5, an item

[Tag 07G5](https://stacks.math.columbia.edu/tag/07G5) in the Stacks Project.

**`Stacks.Smoothing.baseParameterPowerIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ResolutionReductions.lean#L235).

> The ideal `J = (π_1^e, …, π_d^e)` of `k[y_1, …, y_m]`.

```lean
noncomputable def baseParameterPowerIdeal {k : Type u} [CommRing k] {m d : ℕ}
    (π : Fin d → MvPolynomial (Fin m) k) (e : ℕ) : Ideal (MvPolynomial (Fin m) k)
```

## Tag 07G6, an item

[Tag 07G6](https://stacks.math.columbia.edu/tag/07G6) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_canBeResolved_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L437). The attribute's comment: “for an arbitrary base change R₁ → R₂ of the chain in place of the passage from (R/JR)\_𝔭 to its localization (R/I)\_𝔯, the base-changed target receiving the original target”.

> **Stacks 07FJ, step 22** (tag 07G6). It suffices to resolve the chain over `(R/JR)_𝔭`: a
> solution there, localized at `𝔯`, solves the chain of step (20) over `(R/I)_𝔯`. Over a local
> Artinian target resolvability is the existence of a smooth factorization, and a smooth
> factorization is carried along any base change of the chain.

```lean
theorem canBeResolved_of_canBeResolved_baseChange [IsLocalRing L₁]
    [Algebra.IsPushout R₁ A₁ R₂ A₂] {q : Ideal L₂} (hq : q ≠ ⊤)
    (h : CanBeResolved R₁ A₁ L₁ (IsLocalRing.maximalIdeal L₁)) : CanBeResolved R₂ A₂ L₂ q
```

## Tag 07G7, an item

[Tag 07G7](https://stacks.math.columbia.edu/tag/07G7) in the Stacks Project.

**`Stacks.Smoothing.span_range_pow_le_span_range_pow_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L494). The attribute's comment: “with the hypothesis d*(e-1)+1 ≤ n in place of the source's n = N + dc, which does not give 𝔭^n ⊆ J: a degree-n monomial in the regular system of parameters π\_1, …, π\_d lies in (π\_1^e, …, π\_d^e) only if some exponent reaches e, so the containment needs d*(e-1) < n, whereas N is fixed in step (1) before c and hence before e = 8c”.

> **The bound of Stacks 07FJ, step 23, corrected.** If `𝔭 = (π_1, …, π_d)` and
> `J = (π_1^e, …, π_d^e)` then `𝔭^n ⊆ J` as soon as `d(e - 1) < n`, and this is sharp: a monomial
> of degree `n` in the `π_i` is forced into `J` only when one of its exponents reaches `e`. The
> bound `d·e < n` of `Stacks.AlgebraicGeometry.IdealPowerSections.span_range_pow_le_span_range_pow`
> is the same statement with a weaker hypothesis.

```lean
theorem span_range_pow_le_span_range_pow_of_le {d : ℕ} (π : Fin d → Y) {e n : ℕ} (he : 1 ≤ e)
    (hn : d * (e - 1) + 1 ≤ n) :
    Ideal.span (Set.range π) ^ n ≤ Ideal.span (Set.range fun i => π i ^ e)
```

**`Stacks.Smoothing.canBeResolved_quotient_of_canBeResolved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L543). The attribute's comment: “the reduction half of the step: the solution of the chain over (R/p^nR)\_p is divided by J, which is a base change of the chain; the numeric input p^n ⊆ J is span\_range\_pow\_le\_span\_range\_pow\_of\_le, stated with the corrected bound”.

> **Stacks 07FJ, step 23** (tag 07G7). It suffices to resolve the chain before dividing by the
> ideal: dividing a solution of `R → A → Λ` by an ideal `I` of the base gives a solution of
> `R/I → A/IA → Λ/IΛ`, because `A/IA` is the base change of `A` along `R → R/I`. In step (23) the
> base is `(R/𝔭^nR)_𝔭`, the ideal is `J = (π_1^e, …, π_d^e)`, and
> `span_range_pow_le_span_range_pow_of_le` is what makes `(R/JR)_𝔭` that quotient.

```lean
theorem canBeResolved_quotient_of_canBeResolved [IsLocalRing L] (I : Ideal R)
    (h : CanBeResolved R A L (IsLocalRing.maximalIdeal L)) :
    let IA := Ideal.map (algebraMap R A) I
    let IL := Ideal.map (algebraMap A L) IA
    letI : Algebra (R ⧸ I) (L ⧸ IL) :=
      ((algebraMap (A ⧸ IA) (L ⧸ IL)).comp (algebraMap (R ⧸ I) (A ⧸ IA))).toAlgebra
    letI : IsScalarTower (R ⧸ I) (A ⧸ IA) (L ⧸ IL) := IsScalarTower.of_algebraMap_eq fun _ => rfl
    ∀ q : Ideal (L ⧸ IL), q ≠ ⊤ → CanBeResolved (R ⧸ I) (A ⧸ IA) (L ⧸ IL) q
```

## Tag 07G8, an item

[Tag 07G8](https://stacks.math.columbia.edu/tag/07G8) in the Stacks Project.

**`Stacks.Smoothing.hasSmoothFactorization_of_algHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L375).

> **Stacks 07FJ, step 24** (tag 07G8). It suffices to resolve the chain with `B` in place of
> `C`: an `R`-algebra section `C → B` compatible with the maps to the target carries a smooth
> factorization of `B → Λ` to one of `C → Λ`.

```lean
theorem hasSmoothFactorization_of_algHom {C₀ : Type u} [CommRing C₀] [Algebra R₀ C₀]
    [Algebra C₀ L] [IsScalarTower R₀ C₀ L] (σ : C₀ →ₐ[R₀] A₀)
    (hσ : ∀ c, algebraMap A₀ L (σ c) = algebraMap C₀ L c)
    (h : HasSmoothFactorization R₀ A₀ L) : HasSmoothFactorization R₀ C₀ L
```

## Tag 07G9, an item

[Tag 07G9](https://stacks.math.columbia.edu/tag/07G9) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_factorization_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L616). The attribute's comment: “for a chain whose middle term is an arbitrary algebra of finite presentation over Λ₀[t\_1, …, t\_d] in place of B ⊗\_\{k[x\_1, …, x\_d]} (R/p^nR)\_p, with essential smoothness of Λ₀ → D' spelled out as: D' is a localization of a Λ₀-algebra of finite presentation and is formally smooth over Λ₀”.

> **Stacks 07FJ, step 25** (tag 07G9). It suffices to find a factorization
> `B ⊗_{k[x_1, …, x_d]} (R/𝔭^nR)_𝔭 → D'[t_1, …, t_d] → Λ_𝔮/𝔮^nΛ_𝔮`: the ring
> `R_𝔭/𝔭^nR_𝔭` is the polynomial ring `Λ₀[t_1, …, t_d]` over
> `Λ₀ = k[y_1, …, y_m]_𝔭/𝔭^nk[y_1, …, y_m]_𝔭`, the algebra `D'` is essentially smooth over `Λ₀`,
> hence `D'[t_1, …, t_d]` is a filtered colimit of smooth `Λ₀[t_1, …, t_d]`-algebras and the
> finitely presented middle term factors through one of them.

```lean
theorem canBeResolved_of_factorization_mvPolynomial {Λ₀ B₀ D A L : Type u} [CommRing Λ₀]
    [CommRing B₀] [CommRing D] [CommRing A] [CommRing L] [Algebra Λ₀ B₀] [Algebra B₀ D]
    [Algebra Λ₀ D] [IsScalarTower Λ₀ B₀ D] [Algebra.FinitePresentation Λ₀ B₀] (M : Submonoid B₀)
    [IsLocalization M D] (hD : Algebra.FormallySmooth Λ₀ D) {d : ℕ}
    [Algebra (MvPolynomial (Fin d) Λ₀) A] [Algebra A L] [Algebra (MvPolynomial (Fin d) Λ₀) L]
    [IsScalarTower (MvPolynomial (Fin d) Λ₀) A L]
    [Algebra.FinitePresentation (MvPolynomial (Fin d) Λ₀) A]
    (g : A →ₐ[MvPolynomial (Fin d) Λ₀] MvPolynomial (Fin d) D)
    (k : MvPolynomial (Fin d) D →ₐ[MvPolynomial (Fin d) Λ₀] L)
    (hgk : k.comp g = IsScalarTower.toAlgHom (MvPolynomial (Fin d) Λ₀) A L)
    {q : Ideal L} (hq : q ≠ ⊤) :
    CanBeResolved (MvPolynomial (Fin d) Λ₀) A L q
```

## Tag 07GA, an item

[Tag 07GA](https://stacks.math.columbia.edu/tag/07GA) in the Stacks Project.

**`Stacks.Smoothing.exists_algHom_parameterPowerAlgebra_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ArtinianFactorizationDescent.lean#L651). The attribute's comment: “the choices of (07FT), (07FU) and (07FX) are hypotheses: the map A → D' whose existence is the condition E ⊆ D of (07FT), the images π\_i, δ\_i, λ\_\{ij} in D' of (07FU) and (07FX), the invertibility of δ\_i in the local ring D', and clause (a) of (07FX) read in D'. The target D'[t\_1, …, t\_d] is MvPolynomial (Fin d) D'”.

> **Stacks 07FJ, step 26** (tag 07GA). The factorization required by step (25) exists. Its
> twist is that `B = A[x_i, z_{ij}]/(x_i^{2N} - Σ_j z_{ij}a_j)` must send `x_i` to `π_i t_i`, not
> to `π'_i = δ_i π_i`, for the square over `k[x_1, …, x_d] → R_𝔭/𝔭^nR_𝔭` to commute; the defining
> relation then forces `z_{ij} ↦ λ_{ij} t_i^{2N}/δ_i^{2N}`, which lies in `D'[t_1, …, t_d]`
> because `δ_i` is a unit of the local ring `D'`. The map is produced as a
> `k[x_1, …, x_d]`-algebra map for the structure `x_i ↦ π_i t_i` on `D'[t_1, …, t_d]`, which is
> exactly the commutation of the square in the source.

```lean
theorem exists_algHom_parameterPowerAlgebra_mvPolynomial (k : Type u) {A D : Type u} [CommRing k]
    [CommRing A] [CommRing D] [Algebra k A] [Algebra k D] {d r N : ℕ} (a : Fin r → A)
    (φ : A →ₐ[k] D) (π δ : Fin d → D) (lam : Fin d → Fin r → D) (hδ : ∀ i, IsUnit (δ i))
    (hrel : ∀ i, (δ i * π i) ^ (2 * N) = ∑ j, φ (a j) * lam i j) :
    letI : Algebra (MvPolynomial (Fin d) k) (MvPolynomial (Fin d) D) :=
      (MvPolynomial.aeval (R := k) fun i => C (π i) * X i).toRingHom.toAlgebra
    ∃ ψ : parameterPowerAlgebra A d N a →ₐ[MvPolynomial (Fin d) k] MvPolynomial (Fin d) D,
      (∀ x : A, ψ (algebraMap A (parameterPowerAlgebra A d N a) x) = C (φ x)) ∧
      (∀ i, ψ (Ideal.Quotient.mk (parameterPowerIdeal d N a) (X (Sum.inl i))) = C (π i) * X i) ∧
      ∀ i j, ψ (Ideal.Quotient.mk (parameterPowerIdeal d N a) (X (Sum.inr (i, j)))) =
        C (lam i j * (↑(hδ i).unit⁻¹ : D) ^ (2 * N)) * X i ^ (2 * N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.11, Tag 07FF](https://stacks.math.columbia.edu/tag/07FF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
