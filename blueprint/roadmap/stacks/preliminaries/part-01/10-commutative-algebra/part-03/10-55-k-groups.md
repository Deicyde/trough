---
declaration: section
origin: cited
lean: length_K0prime_hom_exists, K0toK0'_field_bijective_and_isoZ, K0_polynomial_isoZ, K0'_polynomial_isoZ, K0toK0'_polynomial_bijective, nodeRing_K0_addEquiv_and_K0prime_addEquiv, K0_product, K0prime_prod
statement: formalized
proof: formalized
---

# 10.55 K-groups

Section 10.55 of the Stacks Project, [Tag 00JC](https://stacks.math.columbia.edu/tag/00JC). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00JD, a lemma

[Tag 00JD](https://stacks.math.columbia.edu/tag/00JD) in the Stacks Project.

**`length_K0prime_hom_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Defs.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Defs.lean#L185).

> **Stacks Tag 00JD.** If `R` is an Artinian local ring then the length
> function defines an abelian group homomorphism `K'_0(R) →+ ℤ` sending the
> class of each presentation `P` to its integer length.

```lean
theorem length_K0prime_hom_exists (R : Type u) [CommRing R]
    [IsArtinianRing R] [IsLocalRing R] :
    ∃ φ : K0prime R →+ ℤ,
      ∀ P : FGPres R, φ (K0prime.mk P) = lengthOfPresℤ R P
```

## Tag 00JE, an example

[Tag 00JE](https://stacks.math.columbia.edu/tag/00JE) in the Stacks Project.

**`K0toK0'_field_bijective_and_isoZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Field.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Field.lean#L93). The attribute's comment: “K0(k) → K'0(k) bijective, K'0(k) ≅ ℤ and K0(k) ≅ ℤ via dimension, dimension equals length”.

> **Stacks Example 00JE.** Let `k` be a field. Then `K₀(k) = K'₀(k) ≅ ℤ`, the
> isomorphism being given by the dimension function, which is also the length function.
> Precisely:
> * the canonical map `K0toK0' k : K₀(k) → K'₀(k)` is bijective;
> * there is an isomorphism `K'₀(k) ≃+ ℤ` sending the class `[M]` of every finite
>   `k`-module `M` to `dim_k M`;
> * there is an isomorphism `K₀(k) ≃+ ℤ` sending the class `[M]` of every finite
>   (projective) `k`-module `M` to `dim_k M`;
> * for every finite `k`-module `M`, `length_k M = dim_k M`.
>
> Here `K'₀(k) = K0PrimeOfFinPres k` and `K₀(k) = K0OfProjGen k` are the Grothendieck
> groups of finite, resp. finite projective, `k`-modules modulo short exact sequences,
> built as in Stacks Section 00JC.

```lean
theorem K0toK0'_field_bijective_and_isoZ (k : Type u) [Field k] :
    Function.Bijective (K0toK0' k) ∧
    (∃ e : K0PrimeOfFinPres k ≃+ ℤ, ∀ (M : Type u) [AddCommGroup M] [Module k M]
        [Module.Finite k M], e (K0PrimeOfFinPres.mkM k M) = Module.finrank k M) ∧
    (∃ e : K0OfProjGen k ≃+ ℤ, ∀ (M : Type u) [AddCommGroup M] [Module k M]
        [Module.Finite k M], e (K0OfProjGen.mkM k M) = Module.finrank k M) ∧
    ∀ (M : Type u) [AddCommGroup M] [Module k M] [Module.Finite k M],
      Module.length k M = Module.finrank k M
```

## Tag 00JF, an example

[Tag 00JF](https://stacks.math.columbia.edu/tag/00JF) in the Stacks Project.

**`K0_polynomial_isoZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 982](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/PID.lean#L982). The attribute's comment: “K0(k[x]) ≅ ℤ”. References: SGA 6 IX (1.7), “special case”.

> `K0(k[x]) ≅ ℤ`, exhibited by an explicit isomorphism that sends
> the class `[k[x]]` of the rank-1 free module to `1`.  (The rank map.)

```lean
theorem K0_polynomial_isoZ (k : Type*) [Field k] :
    ∃ e : K0OfProjGen (Polynomial k) ≃+ ℤ,
      e (K0OfProjGen.mk (Polynomial k) (K0Gen.free1 (Polynomial k))) = 1
```

**`K0'_polynomial_isoZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 994](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/PID.lean#L994). The attribute's comment: “K0'(k[x]) ≅ ℤ”. References: SGA 6 IX (1.7), “Lemma 1.7, case A = k[T]”; SGA 6 IX (3.4), “Case S = Spec k”.

> `K0'(k[x]) ≅ ℤ`, exhibited by an explicit isomorphism that sends
> the class `[k[x]]` to `1` (the rank of the free part).  Every torsion finite
> module has class `0`.

```lean
theorem K0'_polynomial_isoZ (k : Type*) [Field k] :
    ∃ e : K0PrimeOfFinPres (Polynomial k) ≃+ ℤ,
      e (K0PrimeOfFinPres.mk (Polynomial k) (K0'Gen.free1 (Polynomial k))) = 1
```

**`K0toK0'_polynomial_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/PID.lean#L1010). The attribute's comment: “K0(k[x]) ≅ K0'(k[x])”.

> The canonical homomorphism `ι : K0(k[x]) → K0'(k[x])` is an
> isomorphism (it is bijective).
>
> Argument: `rankHom ∘ K0toK0' = rankHomK0` (definitionally, `rankHomK0`), and
> both `rankHom` (D6) and `rankHomK0` (D9) are bijective.  Therefore
> `K0toK0' = rankHom.symm ∘ rankHomK0` (as maps), a composite of bijections,
> hence bijective.  Formally: `K0toK0'` is injective because
> `rankHom ∘ K0toK0' = rankHomK0` is injective; it is surjective because
> `rankHom` is bijective and `rankHomK0 = rankHom ∘ K0toK0'` is surjective.

```lean
theorem K0toK0'_polynomial_bijective (k : Type*) [Field k] :
    Function.Bijective (K0toK0' (Polynomial k))
```

## Tag 00JG, an example

[Tag 00JG](https://stacks.math.columbia.edu/tag/00JG) in the Stacks Project.

**`nodeRing_K0_addEquiv_and_K0prime_addEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/NodeRing.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/NodeRing.lean#L554). The attribute's comment: “`K₀(R) ≅ k^* ⊕ ℤ` and `K'₀(R) ≅ ℤ` for `R = {f ∈ k[x] ∣ f(0) = f(1)}`”.

> **Stacks Example 10.55.5 (tag `00JG`).** Let `k` be a field and
> `R = {f ∈ k[x] ∣ f(0) = f(1)}`. Then `K₀(R) ≅ k^* ⊕ ℤ`, but `K'₀(R) ≅ ℤ`.
>
> Here `K₀(R)` (`K0OfProjGen`) and `K'₀(R)` (`K0PrimeOfFinPres`) are the Grothendieck groups of
> finite projective, respectively finite, `R`-modules, with relations from short exact sequences,
> and `k^*` is written additively. The isomorphisms are `NodeRing.exists_K0_addEquiv` (sending
> `[R]` to `(1, 1)` and the line bundle `L_u = {f ∣ f(1) = u f(0)}` to `(u, 1)`) and
> `NodeRing.exists_K0prime_addEquiv_int` (the rank, sending `[R]` to `1`).

```lean
theorem nodeRing_K0_addEquiv_and_K0prime_addEquiv (k : Type*) [Field k] :
    Nonempty (K0OfProjGen (nodeRing k) ≃+ Additive kˣ × ℤ) ∧
      Nonempty (K0PrimeOfFinPres (nodeRing k) ≃+ ℤ)
```

## Tag 00JH, a lemma

[Tag 00JH](https://stacks.math.columbia.edu/tag/00JH) in the Stacks Project.

**`K0_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Product/K0.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Product/K0.lean#L401). The attribute's comment: “K\_0”.

> For a product ring `R = R₁ × R₂`, the natural
> homomorphism `K₀(R) → K₀(R₁) × K₀(R₂)`, given on generators by
> `[M] ↦ ([M ⊗_R R₁], [M ⊗_R R₂])` (base change along the two projections), is an
> isomorphism of abelian groups.
>
> The product map is characterized by its values on the generating classes
> `K0.mk M`; since these generate `K0 (R₁ × R₂)`, the additive isomorphism `e`
> below is unique with the stated property, so this faithfully expresses that the
> product map is an isomorphism.

```lean
theorem K0_product (R1 R2 : Type u) [CommRing R1] [CommRing R2] :
    ∃ e : K0 (R1 × R2) ≃+ (K0 R1 × K0 R2),
      ∀ M : FGProj (R1 × R2),
        e (K0.mk M) =
          ( K0.mk (M.baseChangeHom (RingHom.fst R1 R2)),
            K0.mk (M.baseChangeHom (RingHom.snd R1 R2)) )
```

**`K0prime_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Product/K0Prime.lean, line 566](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Product/K0Prime.lean#L566). The attribute's comment: “K'\_0 half, for arbitrary commutative rings R\_1, R\_2; the K\_0 half is K0\_product”.

> **Stacks 00JH, `K'_0` half.** Let `R = R₁ × R₂` be a product of two commutative
> rings (no further hypothesis). Then the natural homomorphism
> `K'₀(R) → K'₀(R₁) × K'₀(R₂)`, given on generators by
> `[M] ↦ ([M ⊗_R R₁], [M ⊗_R R₂])`, is an isomorphism of abelian groups.
>
> As for the `K_0` half (`K0_product`), the classes `K0prime.mk M` generate
> `K0prime (R₁ × R₂)`, so the additive isomorphism `e` is uniquely determined by the
> stated property.

```lean
theorem K0prime_prod (R1 R2 : Type u) [CommRing R1] [CommRing R2] :
    ∃ e : K0prime (R1 × R2) ≃+ (K0prime R1 × K0prime R2),
      ∀ M : FGPres (R1 × R2),
        e (K0prime.mk M) =
          ( K0prime.baseChangeMk (RingHom.fst R1 R2) M.module,
            K0prime.baseChangeMk (RingHom.snd R1 R2) M.module )
```

## Tag 00JI, a lemma

[Tag 00JI](https://stacks.math.columbia.edu/tag/00JI) in the Stacks Project.

**`K0prime.lengthHom_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/LengthIso.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/LengthIso.lean#L132).

> **Stacks 00JI.** Let `R` be an Artinian local ring. The length homomorphism
> `length_R : K'_0(R) → ℤ` of Stacks 00JD (`lengthHom R`, sending the class of a finite module
> to its length) is an isomorphism.

```lean
theorem lengthHom_isIso : ∃ e : K0prime R ≃+ ℤ, ⇑e = lengthHom R
```

## Tag 00JJ, a lemma

[Tag 00JJ](https://stacks.math.columbia.edu/tag/00JJ) in the Stacks Project.

**`finite_projective_is_finite_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Defs.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Defs.lean#L308). The attribute's comment: “every finite projective module over a local ring is finite free”. References: EGA 0 (10.1.3), “(ii): b ⇒ a, b ⇒ a”; EGA 0 (17.2.2), “more general”; EGA III (7.9.1), “special case”; SGA 1 IV (4.3), “case (b): (ii) ⇒ (i)”; SGA 3 VIA (2.1.3), “special case”; SGA 3 VIIB (0.3.7), “special case”; SGA 6 I (2.15.1), “special case”.

> Over a local ring, every finitely generated projective module is free, and
> admits a linear equivalence to `Fin n → R` for some `n`. This is the first half
> of Stacks 00JJ.

```lean
theorem finite_projective_is_finite_free
    (R : Type u) [CommRing R] [IsLocalRing R]
    (M : Type v) [AddCommGroup M] [Module R M]
    [Module.Finite R M] [Module.Projective R M] :
    Module.Free R M ∧ ∃ n : ℕ, Nonempty (M ≃ₗ[R] (Fin n → R))
```

**`K0.rank_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Defs.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/Defs.lean#L509). The attribute's comment: “the rank map `[M] ↦ rank_R(M)` is a well-defined isomorphism `K_0(R) ≃+ ℤ`”.

> Over a local ring, the rank map `K_0(R) → ℤ` is an isomorphism. Combined
> with `finite_projective_is_finite_free`, this gives the full statement of
> Stacks 00JJ.

```lean
theorem K0.rank_isIso
    (R : Type u) [CommRing R] [IsLocalRing R] :
    ∃ e : K0 R ≃+ ℤ, ⇑e = K0.rank R
```

## Tag 00JK, a lemma

[Tag 00JK](https://stacks.math.columbia.edu/tag/00JK) in the Stacks Project.

**`K0.toK0prime_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/LengthIso.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/KTheory/Grothendieck/LengthIso.lean#L187).

> **Stacks 00JK.** Let `R` be a local Artinian ring. The diagram
>
> $$
> \begin{array}{ccc}
> K_0(R) & \to & K_0'(R) \\
> \text{rank}_R \downarrow & & \downarrow \text{length}_R \\
> \mathbf{Z} & \xrightarrow{\text{length}_R(R)} & \mathbf{Z}
> \end{array}
> $$
>
> commutes, and its vertical maps are isomorphisms: `K0.rank R` and `lengthHom R` are bijective,
> and `length_R ∘ (K_0(R) → K'_0(R)) = length_R(R) · rank_R`.
>
> Here `K_0(R)` (`K0 R`) is presented by direct-sum relations; since short exact sequences of
> projective modules split, these are the relations of the Stacks definition.

```lean
theorem toK0prime_comm [IsLocalRing R] [IsArtinianRing R] :
    Function.Bijective (K0.rank R) ∧ Function.Bijective (lengthHom R) ∧
      (lengthHom R).comp (toK0prime R) =
        (AddMonoidHom.mulLeft ((Module.length R R).toNat : ℤ)).comp (K0.rank R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.55, Tag 00JC](https://stacks.math.columbia.edu/tag/00JC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
