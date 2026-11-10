---
declaration: section
origin: cited
lean: MulSemiringAction.exists_monic_map_eq_X_sub_C_pow_card, FixedPoints.quotientComparison_injective, FixedPoints.compMap_isIntegral, FixedPoints.quotientComparison_comap_isHomeomorph, FixedPoints.quotientComparison_residueField_isPurelyInseparable, Stacks.Invariant.QuotientComparison.charpolyFixed_map_mk_of_mem, Stacks.Invariant.QuotientComparison.exists_monic_map_eq_X_sub_C_pow, Stacks.Invariant.QuotientComparison.X_sub_C_pow_eq_X_pow_of_mem_ker
statement: formalized
proof: formalized
---

# 15.112 Group actions and integral closure

Section 15.112 of the Stacks Project, [Tag 0BRE](https://stacks.math.columbia.edu/tag/0BRE). 11 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BRF, a lemma

[Tag 0BRF](https://stacks.math.columbia.edu/tag/0BRF) in the Stacks Project.

**`MulSemiringAction.exists_monic_map_eq_X_sub_C_pow_card`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 1050](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L1050).

> **Stacks 0BRF.** Let `φ : A → B` be a surjective `G`-equivariant ring homomorphism for a
> finite group `G`.  Every `b ∈ B^G` is matched by a monic polynomial `P` over `A^G` whose image
> under the restriction `A^G → B^G` of `φ` is `(X - C b) ^ |G|`.
>
> The witness is the orbit polynomial `∏_{g ∈ G} (X - C (g • a))` of any lift `a` of `b`: its
> coefficients are `G`-invariant, and each factor maps to `X - C b`, since
> `φ (g • a) = g • b = b`.

```lean
theorem exists_monic_map_eq_X_sub_C_pow_card
    {G : Type*} [Group G] [Finite G]
    {A B : Type*} [CommRing A] [CommRing B]
    [MulSemiringAction G A] [MulSemiringAction G B]
    (φ : A →+*[G] B) (hφ : Function.Surjective φ)
    (b : FixedPoints.subring B G) :
    ∃ P : Polynomial (FixedPoints.subring A G), P.Monic ∧
      Polynomial.map
          ((φ : A →+* B).restrict (FixedPoints.subring A G) (FixedPoints.subring B G)
            (by
              intro a ha g
              change g • φ a = φ a
              rw [← map_smul φ, ha g])) P =
        (Polynomial.X - Polynomial.C b) ^ Nat.card G
```

## Tag 09EG, a lemma

[Tag 09EG](https://stacks.math.columbia.edu/tag/09EG) in the Stacks Project.

**`FixedPoints.quotientComparison_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L376).

> **(Well-definedness of `R^G/I^G ⊆ (R/I)^G`.)** The canonical comparison map
> `φ` is injective, so `R^G / I^G` is (isomorphic to) a subring of `(R/I)^G`.
>
> Proof: `φ` is `Ideal.Quotient.lift` of `toFixedQuot : R^G → (R/I)^G`, so it
> suffices to show `ker(toFixedQuot) = I^G = invariantIdeal`. If `a ∈ R^G` maps to `0`,
> then `mk_I (a : R) = 0` in `R/I`, i.e. `a ∈ I`; and `a ∈ R^G`, so
> `a ∈ invariantIdeal R G I` by definition (`I.comap (R^G).subtype`). Conversely the
> quotient by `invariantIdeal` already kills these, so the lifted map is injective.

```lean
theorem quotientComparison_injective :
    Function.Injective (compMap R G I hcompat)
```

**`FixedPoints.compMap_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L461).

> **(Integrality.)** Via the comparison map `φ`, the ring `(R/I)^G` is an
> integral extension of `R^G / I^G`: every element of `(R/I)^G` is a root of a monic
> polynomial with coefficients in the image of `R^G / I^G`.
>
> Proof: by `Algebra.IsIntegral.mk`, fix `b ∈ (R/I)^G`. Take the monic witness `P`
> over `R^G/I^G` from `compMap_polyWitness b`, with `map φ P = (X - C b)^{|G|}`.
> Then under the algebra structure `φ.toAlgebra`, `aeval b P = (map φ P).eval b
> = ((X - C b)^{|G|}).eval b = (b - b)^{|G|} = 0` (using
> `Polynomial.aeval_def`, `Polynomial.eval_map`, `Polynomial.eval_pow`,
> `Polynomial.eval_sub`, `Polynomial.eval_X`, `Polynomial.eval_C`), and `P` is
> monic, so `b` is integral.

```lean
theorem compMap_isIntegral :
    letI := (compMap R G I hcompat).toAlgebra
    Algebra.IsIntegral (FixedPoints.subring R G ⧸ invIdeal R G I)
      (FixedPoints.subring (R ⧸ I) G)
```

**`FixedPoints.quotientComparison_comap_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L475).

> **(Homeomorphism on spectra.)** The induced map on prime spectra
> `Spec(φ) : Spec((R/I)^G) → Spec(R^G/I^G)` is a homeomorphism for the Zariski topologies.
> This is `PrimeSpectrum.isHomeomorph_comap` (the abstract form of Stacks 09EF) applied to the
> two facts read off from `quotientComparison_polyWitness` and `quotientComparison_injective`: every
> `b ∈ (R/I)^G` has `b ^ |G|` in the range of `φ`, and `ker φ = 0` is nil.

```lean
theorem quotientComparison_comap_isHomeomorph :
    IsHomeomorph (PrimeSpectrum.comap (compMap R G I hcompat))
```

**`FixedPoints.quotientComparison_residueField_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L504).

> **(Purely inseparable residue extensions.)** For every prime `𝔮 ⊆ (R/I)^G` with
> contraction `𝔭 = φ⁻¹(𝔮) ⊆ R^G/I^G`, the induced extension of residue fields
> `κ(𝔭) → κ(𝔮)` is purely inseparable. This is the abstract form of Stacks 09EF,
> `isPurelyInseparable_residueField_of_sub_C_pow_witness`, applied to the monic witness
> `quotientComparison_polyWitness`.

```lean
theorem quotientComparison_residueField_isPurelyInseparable
    (q : Ideal (FixedPoints.subring (R ⧸ I) G)) [q.IsPrime] :
    letI := (Ideal.ResidueField.map (q.comap (compMap R G I hcompat)) q
      (compMap R G I hcompat) rfl).toAlgebra
    IsPurelyInseparable (Ideal.ResidueField (q.comap (compMap R G I hcompat)))
      (Ideal.ResidueField q)
```

## Tag 0H34, a lemma

[Tag 0H34](https://stacks.math.columbia.edu/tag/0H34) in the Stacks Project.

**`Stacks.Invariant.QuotientComparison.charpolyFixed_map_mk_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 861](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L861).

> **Stacks 0H34 (tag 0H34 = Lemma 15.112.3).** For `x ∈ JR`, the characteristic
> polynomial `∏_{σ ∈ G} (T - σ x) = T^n + a₁T^{n-1} + … + aₙ` has all its non-leading
> coefficients `aᵢ` in `J`; equivalently, reducing the coefficients of `charpolyFixed G x`
> modulo `J` gives `X ^ n`.
>
> Implementation note: the coefficients `aᵢ` lie in `R^G`, and what has to be shown is that
> they lie in `J` — the ideal of `R^G` — and not merely in the a priori larger `JR ∩ R^G`.
> Writing `x = Σⱼ fⱼ bⱼ` with `fⱼ ∈ J ⊆ R^G` and `bⱼ ∈ R`, invariance of `fⱼ` gives
> `σ x = Σⱼ fⱼ (σ bⱼ)`, so each elementary symmetric coefficient is a sum of products each
> carrying a factor `∏ fⱼ ∈ J`, and symmetrizing over the orbit keeps the remaining cofactor
> in `R^G`; hence `aᵢ ∈ J · R^G = J`.

```lean
theorem charpolyFixed_map_mk_of_mem [Fintype G] (J : Ideal (FixedPoints.subring R G))
    (x : R) (hx : x ∈ JRideal J) :
    Polynomial.map (Ideal.Quotient.mk J) (charpolyFixed G x)
      = (Polynomial.X : Polynomial ((FixedPoints.subring R G) ⧸ J)) ^ (Fintype.card G)
```

## Tag 0H35, a lemma

[Tag 0H35](https://stacks.math.columbia.edu/tag/0H35) in the Stacks Project.

**`Stacks.Invariant.QuotientComparison.exists_monic_map_eq_X_sub_C_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 898](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L898). The attribute's comment: “(1)”.

> **(Lifting characteristic-polynomial form.)** For every `b ∈ (R / JR)^G`
> there is a monic polynomial `P ∈ (R^G / J)[T]` whose image under
> `Polynomial.map (invariantComparison J)` equals `(X - C b) ^ n`, where
> `n = Fintype.card G`.

```lean
theorem exists_monic_map_eq_X_sub_C_pow [Fintype G] (J : Ideal (FixedPoints.subring R G))
    (b : FixedPoints.subring (R ⧸ JRideal J) G) :
    ∃ P : Polynomial ((FixedPoints.subring R G) ⧸ J),
      P.Monic ∧
        P.map (invariantComparison J)
          = (Polynomial.X - Polynomial.C b) ^ (Fintype.card G)
```

**`Stacks.Invariant.QuotientComparison.X_sub_C_pow_eq_X_pow_of_mem_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 928](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L928). The attribute's comment: “(2)”.

> **(Kernel elements are nilpotent-like.)** For every
> `a ∈ ker(invariantComparison J)` we have `(X - C a) ^ n = X ^ n` in
> `(R^G / J)[T]`, where `n = Fintype.card G`.

```lean
theorem X_sub_C_pow_eq_X_pow_of_mem_ker [Fintype G] (J : Ideal (FixedPoints.subring R G))
    (a : (FixedPoints.subring R G) ⧸ J) (ha : a ∈ RingHom.ker (invariantComparison J)) :
    (Polynomial.X - Polynomial.C a) ^ (Fintype.card G)
      = (Polynomial.X : Polynomial ((FixedPoints.subring R G) ⧸ J)) ^ (Fintype.card G)
```

**`Stacks.Invariant.QuotientComparison.invariantComparison_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 974](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L974). The attribute's comment: “final statement, integrality”.

> **(In particular: integrality.)** The comparison map
> `Φ : R^G / J → (R / JR)^G` is an integral ring map: every `b ∈ (R / JR)^G` is a root
> of the monic polynomial over `R^G / J` supplied by `exists_monic_map_eq_X_sub_C_pow`, because
> that polynomial maps to `(X - C b) ^ n`, which vanishes at `b`.

```lean
theorem invariantComparison_isIntegral [Fintype G] (J : Ideal (FixedPoints.subring R G)) :
    (invariantComparison J).IsIntegral
```

**`Stacks.Invariant.QuotientComparison.invariantComparison_comap_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 986](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L986). The attribute's comment: “final statement, homeomorphism on spectra”.

> **(In particular: homeomorphism on spectra.)** `Spec(Φ) : Spec((R / JR)^G) →
> Spec(R^G / J)` is a homeomorphism.  This is `PrimeSpectrum.isHomeomorph_comap`
> (Stacks 0BR8) applied to the two facts extracted from parts (1) and (2): every
> `b ∈ (R / JR)^G` has `b ^ n` in the range of `Φ` (`exists_apply_eq_pow`), and
> `ker Φ` is nil (`ker_invariantComparison_le_nilradical`).

```lean
theorem invariantComparison_comap_isHomeomorph [Fintype G] (J : Ideal (FixedPoints.subring R G)) :
    IsHomeomorph (PrimeSpectrum.comap (invariantComparison J))
```

**`Stacks.Invariant.QuotientComparison.invariantComparison_residueField_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 1000](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L1000). The attribute's comment: “final statement, purely inseparable residue fields”.

> **(In particular: purely inseparable residue extensions.)** For every prime
> `𝔮 ⊆ (R / JR)^G` with contraction `𝔭 = Φ⁻¹(𝔮) ⊆ R^G / J`, the induced extension of
> residue fields `κ(𝔭) → κ(𝔮)` is purely inseparable.  This is the abstract form of
> Stacks 09EF (`isPurelyInseparable_residueField_of_sub_C_pow_witness`, proved with
> Stacks 09EG) applied to the monic witness of part (1).

```lean
theorem invariantComparison_residueField_isPurelyInseparable [Fintype G]
    (J : Ideal (FixedPoints.subring R G))
    (q : Ideal (FixedPoints.subring (R ⧸ JRideal J) G)) [q.IsPrime] :
    letI := (Ideal.ResidueField.map (q.comap (invariantComparison J)) q
      (invariantComparison J) rfl).toAlgebra
    IsPurelyInseparable (Ideal.ResidueField (q.comap (invariantComparison J)))
      (Ideal.ResidueField q)
```

## Tag 0H36, a remark

[Tag 0H36](https://stacks.math.columbia.edu/tag/0H36) in the Stacks Project.

**`Stacks.Invariant.QuotientComparison.invariantComparison_bijective_of_isUnit_card`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Quotient.lean, line 1107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Quotient.lean#L1107).

> **Stacks 0H36.** If the order of the finite group `G` acting on `R` is invertible in `R`,
> the canonical comparison map `Φ : R^G / J → (R / JR)^G` is an isomorphism.
>
> Injectivity: for `a ∈ ker Φ` the identity `(X - C a) ^ n = X ^ n` of
> `X_sub_C_pow_eq_X_pow_of_mem_ker` has vanishing coefficient in degree `n - 1`, i.e. `n • a = 0`,
> and `n` is invertible.  Surjectivity: `n⁻¹ ∑_{g ∈ G} g • r` is an invariant lift of any
> invariant class `r̄`.

```lean
theorem invariantComparison_bijective_of_isUnit_card
    {R : Type*} [CommRing R] {G : Type*} [Group G] [Fintype G] [MulSemiringAction G R]
    (J : Ideal (FixedPoints.subring R G)) (hG : IsUnit (Fintype.card G : R)) :
    Function.Bijective (invariantComparison J)
```

## Tag 0BRG, a lemma

[Tag 0BRG](https://stacks.math.columbia.edu/tag/0BRG) in the Stacks Project.

**`FixedPoints.exists_monic_polynomial_and_pow_eq_of_invariant_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/BaseChange.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/BaseChange.lean#L399).

> **Stacks 0BRG.** Invariants in `A ⊗[R^G] R` lift to monic degree-`|G|` polynomial
> relations over `A`; moreover, an element in the kernel of the canonical map from `A` to those
> invariants satisfies `(X - C a) ^ |G| = X ^ |G|`.
>
> Present `A` as a quotient of `MvPolynomial A R^G`.  Base change along `R^G → R` presents
> `A ⊗[R^G] R` as the corresponding quotient of `MvPolynomial A R`, whose invariant subring is
> `MvPolynomial A R^G` (`fixedPolynomialEquiv`), and the kernel of the base-changed presentation
> is the extension `JR` of the kernel `J` of the original one
> (`baseChangePresentation_ker_eq_JRideal`).  Both assertions are therefore the corresponding
> assertions of Stacks 0H35 for `J`, transported along the presentation.

```lean
theorem exists_monic_polynomial_and_pow_eq_of_invariant_tensorProduct
    (R : Type u) [CommRing R]
    (G : Type v) [Group G] [Finite G] [MulSemiringAction G R]
    (A : Type w) [CommRing A] [Algebra (FixedPoints.subring R G) A]
    [MulSemiringAction G (A ⊗[(FixedPoints.subring R G)] R)]
    (smul_tmul : ∀ (g : G) (a : A) (r : R),
      g • (a ⊗ₜ[(FixedPoints.subring R G)] r) = a ⊗ₜ[(FixedPoints.subring R G)] (g • r)) :
    let ι : A →+* FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G :=
      RingHom.codRestrict
        (Algebra.TensorProduct.includeLeftRingHom (R := FixedPoints.subring R G))
        (FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G)
        (fun a g => by
          simpa [Algebra.TensorProduct.includeLeftRingHom_apply] using smul_tmul g a 1)
    (∀ b : FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G,
      ∃ P : Polynomial A, P.Monic ∧
        Polynomial.map ι P = (Polynomial.X - Polynomial.C b) ^ Nat.card G) ∧
    ∀ a : A, a ∈ RingHom.ker ι →
      (Polynomial.X - Polynomial.C a) ^ Nat.card G =
        (Polynomial.X : Polynomial A) ^ Nat.card G
```

## Tag 0BRH, a lemma

[Tag 0BRH](https://stacks.math.columbia.edu/tag/0BRH) in the Stacks Project.

**`FixedPoints.canonicalMap_to_invariants_bijective_of_flat_and_isIntegral_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/BaseChange.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/BaseChange.lean#L500).

> **Stacks 0BRH.** The canonical map from a flat algebra over an invariant ring to the
> invariants after extension of scalars is bijective.  In general, the map is integral, is a
> homeomorphism on prime spectra, and induces purely inseparable residue field extensions.
>
> The unconditional half follows from Stacks 0BRG: the monic witnesses generate the target over
> `A`, and the kernel is nil, so
> `PrimeSpectrum.isHomeomorph_comap_and_isPurelyInseparable_and_baseChange_of_adjoin_eq_top`
> applies.  In the flat case `A ⊗[R^G] R → ∏_{g ∈ G} (A ⊗[R^G] R)` has `A` as the equalizer of
> the two maps `r ↦ (g • r)` and `r ↦ r`, because taking equalizers commutes with a flat base
> change.

```lean
theorem canonicalMap_to_invariants_bijective_of_flat_and_isIntegral_isHomeomorph
    (R : Type u) [CommRing R]
    (G : Type v) [Group G] [Finite G] [MulSemiringAction G R]
    (A : Type w) [CommRing A] [Algebra (FixedPoints.subring R G) A]
    [MulSemiringAction G (A ⊗[(FixedPoints.subring R G)] R)]
    (smul_tmul : ∀ (g : G) (a : A) (r : R),
      g • (a ⊗ₜ[(FixedPoints.subring R G)] r) =
        a ⊗ₜ[(FixedPoints.subring R G)] (g • r)) :
    let ι : A →+* FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G :=
      RingHom.codRestrict
        (Algebra.TensorProduct.includeLeftRingHom (R := FixedPoints.subring R G))
        (FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G)
        (fun a g => by
          simpa [Algebra.TensorProduct.includeLeftRingHom_apply] using smul_tmul g a 1)
    (Module.Flat (FixedPoints.subring R G) A → Function.Bijective ι) ∧
      ι.IsIntegral ∧
      IsHomeomorph (PrimeSpectrum.comap ι) ∧
      ∀ (p : Ideal A) [p.IsPrime]
        (q : Ideal (FixedPoints.subring (A ⊗[(FixedPoints.subring R G)] R) G)) [q.IsPrime]
        (hpq : p = q.comap ι),
        (Ideal.ResidueField.map p q ι hpq).IsPurelyInseparable
```

## Tag 0BRI, a lemma

[Tag 0BRI](https://stacks.math.columbia.edu/tag/0BRI) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.IsInvariant.exists_smul_of_under_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsInvariant.exists_smul_of_under_eq#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Invariant/Primes.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Primes.lean#L60) (StacksFrontier).

## Tag 0BRJ, a lemma

[Tag 0BRJ](https://stacks.math.columbia.edu/tag/0BRJ) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.IsFractionRing.normal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsFractionRing.normal#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Invariant/Primes.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Primes.lean#L62) (StacksFrontier): “normality, hence algebraicity, of the residue field extension”.
- [`IsFractionRing.stabilizerHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsFractionRing.stabilizerHom_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Invariant/Primes.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Primes.lean#L65) (StacksFrontier): “surjectivity of the decomposition group onto the relative automorphisms”. References: SGA 1 V (1.1), “more general”; SGA 1 V (1.3), “special case”.

## Tag 0BRK, a lemma

[Tag 0BRK](https://stacks.math.columbia.edu/tag/0BRK) in the Stacks Project.

**`IsIntegralClosure.exists_smul_of_under_eq_and_residue_normal_stabilizerHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Primes.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Primes.lean#L337). References: SGA 1 V (1.1), “special case”; SGA 1 V (1.3), “special case”.

> In a possibly infinite Galois extension, the primes of an integral closure above a fixed
> prime form one Galois orbit.  The induced residue-field extension is normal, and its
> decomposition group surjects onto the relative automorphism group.

```lean
theorem exists_smul_of_under_eq_and_residue_normal_stabilizerHom_surjective
    (A : Type uA) (K : Type uK) (L : Type uL) (B : Type uB)
    [CommRing A] [CommRing B] [Field K] [Field L]
    [Algebra A K] [Algebra B L] [IsFractionRing A K] [IsFractionRing B L]
    [Algebra A B] [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    [IsScalarTower A B L] [IsIntegrallyClosed A] [IsIntegralClosure B A L]
    [IsGalois K L] :
    letI := IsIntegralClosure.MulSemiringAction A K L B
    letI : SMulCommClass Gal(L/K) A B :=
      ⟨fun σ a b ↦ by
        simp only [Algebra.smul_def, smul_mul']
        congr 1
        exact (galRestrict A K L B σ).commutes a⟩
    (∀ (Q Q' : Ideal B) [Q.IsPrime] [Q'.IsPrime],
      Q.under A = Q'.under A → ∃ σ : Gal(L/K), Q' = σ • Q) ∧
    ∀ (P : Ideal A) (Q : Ideal B) [Q.IsPrime] [Q.LiesOver P],
      ∀ (k l : Type*) [Field k] [Field l] [Algebra k l]
        [Algebra (A ⧸ P) k] [IsFractionRing (A ⧸ P) k]
        [Algebra (B ⧸ Q) l] [IsFractionRing (B ⧸ Q) l]
        [Algebra (A ⧸ P) l] [IsScalarTower (A ⧸ P) (B ⧸ Q) l]
        [IsScalarTower (A ⧸ P) k l],
        Normal k l ∧
          Function.Surjective (IsFractionRing.stabilizerHom Gal(L/K) P Q k l)
```

## Tag 0BSX, a lemma

[Tag 0BSX](https://stacks.math.columbia.edu/tag/0BSX) in the Stacks Project.

**`IsIntegralClosure.image_stabilizer_and_inertia_restrictNormalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Primes.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Primes.lean#L403).

> In a tower of possibly infinite Galois extensions, restriction maps the decomposition group
> and the inertia group at a prime of the larger integral closure onto the corresponding groups at
> its contraction to the smaller integral closure.

```lean
theorem image_stabilizer_and_inertia_restrictNormalHom
    (A : Type uA) (K : Type uK) (L : Type uL) (M : Type uM)
    (B : Type uB) (C : Type uC)
    [CommRing A] [Field K] [Field L] [Field M] [CommRing B] [CommRing C]
    [Algebra A K] [Algebra K L] [Algebra L M] [Algebra K M]
    [Algebra A L] [Algebra A M] [IsScalarTower A K L] [IsScalarTower K L M]
    [IsScalarTower A K M] [IsScalarTower A L M]
    [Algebra A B] [Algebra B L] [IsScalarTower A B L]
    [Algebra A C] [Algebra C M] [IsScalarTower A C M]
    [Algebra B C] [Algebra B M] [IsScalarTower A B C]
    [IsScalarTower B L M] [IsScalarTower B C M]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    [IsIntegrallyClosed A] [IsIntegralClosure B A L] [IsIntegralClosure C A M]
    [IsGalois K L] [IsGalois K M]
    (r : Ideal C) [r.IsPrime] :
    letI := IsIntegralClosure.MulSemiringAction A K M C
    letI : SMulCommClass Gal(M/K) A C :=
      ⟨fun σ a c ↦ by
        simp only [Algebra.smul_def, smul_mul']
        congr 1
        exact (galRestrict A K M C σ).commutes a⟩
    letI := IsIntegralClosure.MulSemiringAction A K L B
    letI : SMulCommClass Gal(L/K) A B :=
      ⟨fun σ a b ↦ by
        simp only [Algebra.smul_def, smul_mul']
        congr 1
        exact (galRestrict A K L B σ).commutes a⟩
    let q := r.under B
    let res : Gal(M/K) →* Gal(L/K) := AlgEquiv.restrictNormalHom L
    res '' (MulAction.stabilizer Gal(M/K) r : Set Gal(M/K)) =
        (MulAction.stabilizer Gal(L/K) q : Set Gal(L/K)) ∧
      res '' (r.inertia Gal(M/K) : Set Gal(M/K)) =
        (q.inertia Gal(L/K) : Set Gal(L/K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.112, Tag 0BRE](https://stacks.math.columbia.edu/tag/0BRE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
