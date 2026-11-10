---
declaration: section
origin: cited
lean: length_K0prime_hom_exists, finrank_additive_of_shortExact, K0_polynomial_isoZ, K0'_polynomial_isoZ, K0toK0'_polynomial_bijective, nodeRing, K0_product, K0prime_product
statement: formalized
proof: formalized
---

# 10.55 K-groups

Section 10.55 of the Stacks Project, [Tag 00JC](https://stacks.math.columbia.edu/tag/00JC). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00JD, a lemma

[Tag 00JD](https://stacks.math.columbia.edu/tag/00JD) in the Stacks Project.

**`length_K0prime_hom_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Defs.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Defs.lean#L185).

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

**`finrank_additive_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Field.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Field.lean#L55). References: SGA 6 I (6.0), “(ii), special case”.

> Over a field `k`, the (finite) dimension function is additive on short
> exact sequences of `k`-vector spaces in `ModuleCat.{u} k`: if
> `0 → X₁ → X₂ → X₃ → 0` is short exact and `X₂` is finite-dimensional, then
> `finrank k X₂ = finrank k X₁ + finrank k X₃`.
>
> This is the core computation underlying the informal Stacks remark that
> `K₀(k) = K'₀(k) ≅ ℤ` for a field `k`, with the isomorphism given by the
> dimension/length function. Indeed, this additivity is exactly the condition
> that makes `finrank` descend to a well-defined homomorphism from the
> Grothendieck group of finitely generated `k`-modules to `ℤ`.

```lean
theorem finrank_additive_of_shortExact {k : Type u} [Field k]
    (S : ShortComplex (ModuleCat.{u} k))
    (hfin : Module.Finite k S.X₂)
    (hS : S.ShortExact) :
    Module.finrank k S.X₂ = Module.finrank k S.X₁ + Module.finrank k S.X₃
```

## Tag 00JF, an example

[Tag 00JF](https://stacks.math.columbia.edu/tag/00JF) in the Stacks Project.

**`K0_polynomial_isoZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 977](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/PID.lean#L977). The attribute's comment: “K0(k[x]) ≅ ℤ”. References: SGA 6 IX (1.7), “special case”.

> `K0(k[x]) ≅ ℤ`, exhibited by an explicit isomorphism that sends
> the class `[k[x]]` of the rank-1 free module to `1`.  (The rank map.)

```lean
theorem K0_polynomial_isoZ (k : Type*) [Field k] :
    ∃ e : K0OfProjGen (Polynomial k) ≃+ ℤ,
      e (K0OfProjGen.mk (Polynomial k) (K0Gen.free1 (Polynomial k))) = 1
```

**`K0'_polynomial_isoZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/PID.lean#L989). The attribute's comment: “K0'(k[x]) ≅ ℤ”. References: SGA 6 IX (1.7), “Lemma 1.7, case A = k[T]”; SGA 6 IX (3.4), “Case S = Spec k”.

> `K0'(k[x]) ≅ ℤ`, exhibited by an explicit isomorphism that sends
> the class `[k[x]]` to `1` (the rank of the free part).  Every torsion finite
> module has class `0`.

```lean
theorem K0'_polynomial_isoZ (k : Type*) [Field k] :
    ∃ e : K0PrimeOfFinPres (Polynomial k) ≃+ ℤ,
      e (K0PrimeOfFinPres.mk (Polynomial k) (K0'Gen.free1 (Polynomial k))) = 1
```

**`K0toK0'_polynomial_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/PID.lean, line 1005](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/PID.lean#L1005). The attribute's comment: “K0(k[x]) ≅ K0'(k[x])”.

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

**`nodeRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodeRing.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NodeRing.lean#L59). References: EGA IV (6.5.5).

> The "node" ring `R = {f ∈ k[x] ∣ f(0) = f(1)}`, the subring of polynomials
> agreeing at `0` and `1`.

```lean
def nodeRing (k : Type*) [Field k] : Subring (Polynomial k)
```

## Tag 00JH, a lemma

[Tag 00JH](https://stacks.math.columbia.edu/tag/00JH) in the Stacks Project.

**`K0_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Product/K0.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Product/K0.lean#L405). The attribute's comment: “K\_0”.

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

**`K0prime_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Product/K0Prime.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Product/K0Prime.lean#L513). The attribute's comment: “K'\_0”.

> Assume in addition that `R₁` and `R₂` are Noetherian
> (equivalently that `R = R₁ × R₂` is Noetherian).  Then the natural
> homomorphism `K'₀(R) → K'₀(R₁) × K'₀(R₂)`, given on generators by
> `[M] ↦ ([M ⊗_R R₁], [M ⊗_R R₂])`, is an isomorphism of abelian groups.
>
> As for Statement 1, the classes `K0prime.mk M` generate `K0prime (R₁ × R₂)`, so the
> additive isomorphism `e` is uniquely determined by the stated property.

```lean
theorem K0prime_product (R1 R2 : Type u) [CommRing R1] [CommRing R2]
    [IsNoetherianRing R1] [IsNoetherianRing R2] :
    ∃ e : K0prime (R1 × R2) ≃+ (K0prime R1 × K0prime R2),
      ∀ M : FGPres (R1 × R2),
        e (K0prime.mk M) =
          ( K0prime.baseChangeMk (RingHom.fst R1 R2) M.module,
            K0prime.baseChangeMk (RingHom.snd R1 R2) M.module )
```

## Tag 00JI, a lemma

[Tag 00JI](https://stacks.math.columbia.edu/tag/00JI) in the Stacks Project.

**`exists_finite_module_length_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Artinian.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Artinian.lean#L92). The attribute's comment: “Surjectivity ingredient only: every n : ℕ is the length of a finite module. K'\_0(R) and the isomorphism length\_R : K'\_0(R) ≃ ℤ are not formalized.”.

> **Stacks 00JI (length-surjectivity form).**
>
> For an Artinian local ring `R`, the length map on finitely generated `R`-modules
> hits every natural number: for each `n : ℕ` there is a finitely generated
> `R`-module `M` with `Module.length R M = n`.
>
> This is the surjectivity ingredient of the Stacks statement that
> `length_R : K'_0(R) → ℤ` is an isomorphism. The full Stacks statement also needs
> the construction of `K'_0(R)` (Stacks 00JH) and the injectivity of `length_R`;
> those rely on the composition-series structure of Artinian local rings and are
> left to a follow-up file once Mathlib has `K'_0(R)`. The witness here is the
> standard one: `M = (ResidueField R)^n`.

```lean
theorem exists_finite_module_length_eq.{u} {R : Type u} [CommRing R] [IsLocalRing R]
    [IsArtinianRing R] (n : ℕ) :
    ∃ (M : Type u) (_ : AddCommGroup M) (_ : Module R M) (_ : Module.Finite R M),
      Module.length R M = n
```

## Tag 00JJ, a lemma

[Tag 00JJ](https://stacks.math.columbia.edu/tag/00JJ) in the Stacks Project.

**`K0.rank_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Defs.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Defs.lean#L508).

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

**`length_eq_finrank_mul_length_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Artinian.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Artinian.lean#L143). The attribute's comment: “Numerical identity length P = rank P * length R only; the commutative diagram K\_0(R) → K'\_0(R) → ℤ is not formalized.”.

> Over a local Artinian ring `R`, the length of any finite projective
> `R`-module `P` equals the rank of `P` times the length of `R`. This is the
> mathematical content of the commutative diagram relating `K₀(R)` and
> `K'₀(R)` for a local Artinian ring `R`: the rank-of-`R` length factor is
> exactly the bottom map of the diagram, and both vertical maps (rank and
> length) are isomorphisms with `ℤ`.
>
> Proof sketch. Since `R` is a local ring and `P` is finitely generated and
> projective (hence flat), `P` is free of finite rank by
> `Module.free_of_flat_of_isLocalRing`. Then
> `Module.length_of_free_of_finite` gives the desired identity.

```lean
theorem length_eq_finrank_mul_length_self
    (R : Type*) [CommRing R] [IsLocalRing R] [IsArtinianRing R]
    (P : Type*) [AddCommGroup P] [Module R P]
    [Module.Finite R P] [Module.Projective R P] :
    Module.length R P = Module.finrank R P * Module.length R R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.55, Tag 00JC](https://stacks.math.columbia.edu/tag/00JC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
