---
declaration: section
origin: cited
lean: KaehlerDifferential.mapBaseChange_injective, KaehlerDifferential.split_exact_kerCotangentToTensor_mapBaseChange, Algebra.FormallySmooth.exists_leftInverse_mapCotangent, conormal_finite_projective, adicCompletion_algEquiv_mvPowerSeries
statement: formalized
proof: formalized
---

# 10.139 Smoothness and differentials

Section 10.139 of the Stacks Project, [Tag 05D4](https://stacks.math.columbia.edu/tag/05D4). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04B2, a lemma

[Tag 04B2](https://stacks.math.columbia.edu/tag/04B2) in the Stacks Project.

**`KaehlerDifferential.mapBaseChange_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/JacobiZariski.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Kaehler/JacobiZariski.lean#L167). The attribute's comment: “Exactness at `C ⊗_B Ω_{B/A}`, the one node of the sequence that is not already in Mathlib; the other two are `KaehlerDifferential.exact_mapBaseChange_map` and `KaehlerDifferential.map_surjective`. Stated under `H₁(L_{C/B}) = 0`, the hypothesis the source's second proof uses, which the tag's smoothness gives by instance inference. See the module docstring.”. References: SGA 6 VIII (2.6), “partial”.

> **The sequence of differentials of a tower is exact on the left**: let `R → A → B` be ring
> maps such that `H₁(L_{B/A}) = 0`, for instance with `A → B` smooth. Then the canonical map
> `B ⊗_A Ω_{A/R} → Ω_{B/R}` is injective, so that `0 → B ⊗_A Ω_{A/R} → Ω_{B/R} → Ω_{B/A} → 0` is
> a short exact sequence.

```lean
public theorem KaehlerDifferential.mapBaseChange_injective (R : Type*) [CommRing R]
    (A B : Type*) [CommRing A] [CommRing B] [Algebra R A] [Algebra A B] [Algebra R B]
    [IsScalarTower R A B] [Subsingleton (Algebra.H1Cotangent A B)] :
    Function.Injective (KaehlerDifferential.mapBaseChange R A B)
```

## Tag 06A8, a lemma

[Tag 06A8](https://stacks.math.columbia.edu/tag/06A8) in the Stacks Project.

**`KaehlerDifferential.split_exact_kerCotangentToTensor_mapBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 1160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Conormal.lean#L1160). The attribute's comment: “Stated for a formally smooth `R → S`, which is the source's own generalisation 06A6, and with no hypothesis on `P`. Split exactness is recorded as injectivity of the left hand map together with an `S`-linear section of the right hand map, the exactness of the sequence of 00RU in the middle and on the right being Mathlib's `KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange` and `KaehlerDifferential.mapBaseChange_surjective`. See the module docstring.”. References: EGA 0 (20.5.14), “injectivity, splitting”; EGA IV (17.2.5), “affine case”; EGA 0 (20.5.14), “injectivity, splitting”; EGA 0 (20.6.22), “partial”; EGA 0 (22.4.4.2), “partial”; SGA 3 III (4.25), “(ii) inj. + splitting”.

> **Stacks 06A8.** Let `R → P → S` be ring maps with `R → S` smooth and `P → S` surjective with
> kernel `J`. Then the exact sequence `0 → J/J² → S ⊗[P] Ω[P⁄R] → Ω[S⁄R] → 0` of Stacks 00RU is
> split short exact: its left hand map `J/J² → S ⊗[P] Ω[P⁄R]` is injective and its right hand map
> `S ⊗[P] Ω[P⁄R] → Ω[S⁄R]` admits an `S`-linear section. Only formal smoothness of `R → S` is used,
> and nothing is required of `P`.

```lean
theorem KaehlerDifferential.split_exact_kerCotangentToTensor_mapBaseChange
    (R P S : Type*) [CommRing R] [CommRing P] [CommRing S] [Algebra R P] [Algebra P S]
    [Algebra R S] [IsScalarTower R P S] [Algebra.FormallySmooth R S]
    (hf : Function.Surjective (algebraMap P S)) :
    Function.Injective (kerCotangentToTensor R P S) ∧
      ∃ σ : Ω[S⁄R] →ₗ[S] S ⊗[P] Ω[P⁄R], mapBaseChange R P S ∘ₗ σ = LinearMap.id
```

## Tag 06A9, a lemma

[Tag 06A9](https://stacks.math.columbia.edu/tag/06A9) in the Stacks Project.

**`Algebra.FormallySmooth.exists_leftInverse_mapCotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 1225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Conormal.lean#L1225). The attribute's comment: “Stated for a formally smooth `A → B`, which is the source's own generalisation 06A7, and with the retraction that generalisation asserts rather than bare injectivity, the latter following by `Function.LeftInverse.injective`. Exactness at `J/J²` and surjectivity of `KaehlerDifferential.kerCotangentToTensor A B C` are the neighbouring tag 065V and are not restated. See the module docstring.”.

> **Stacks 06A9.** Let `A → B → C` be ring maps with `A → C` surjective and `A → B` smooth, and
> put `I = ker (A → C)` and `J = ker (B → C)`. Then the map `I/I² → J/J²` of Stacks 065V admits an
> `A`-linear left inverse; in particular it is injective, so that the sequence
> `0 → I/I² → J/J² → Ω[B⁄A] ⊗[B] B/J → 0` of Stacks 065V is exact, indeed split exact. Only formal
> smoothness of `A → B` is used.

```lean
theorem Algebra.FormallySmooth.exists_leftInverse_mapCotangent
    (A B C : Type*) [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra B C]
    [Algebra A C] [IsScalarTower A B C] [Algebra.FormallySmooth A B]
    (h : Function.Surjective (algebraMap A C)) :
    ∃ ρ : (RingHom.ker (algebraMap B C)).Cotangent →ₗ[A]
        (RingHom.ker (algebraMap A C)).Cotangent,
      ρ ∘ₗ Ideal.mapCotangent (RingHom.ker (algebraMap A C))
        (RingHom.ker (algebraMap B C)) (Algebra.ofId A B)
        (((RingHom.comap_ker (algebraMap B C) (algebraMap A B)).trans
          (congrArg RingHom.ker (IsScalarTower.algebraMap_eq A B C).symm)).ge) =
        LinearMap.id
```

## Tag 05D5, a lemma

[Tag 05D5](https://stacks.math.columbia.edu/tag/05D5) in the Stacks Project.

**`conormal_finite_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Conormal.lean#L188). The attribute's comment: “(1)”. References: EGA 0 (19.5.3), “(i), special case”; EGA 0 (19.5.4.1), “a), special case”; EGA 0 (19.5.7), “Clause (i), special case”; EGA 0 (22.1.1), “(ii), condition α”; EGA IV (17.10.4), “special case”; SGA 1 II (4.10), “(iv)”; SGA 3 III (4.25), “(ii), special case”; SGA 3 VIB (1.6), “special case”; SGA 6 VII (1.6), “special case”; SGA 6 VIII (2.4), “special case”; SGA 6 X (7.1), “special case”.

> Part (1) of Stacks tag 05D5: the conormal module is finite locally free.
> If `S` is a smooth `R`-algebra and `σ : S →ₐ[R] R`, then the conormal module `I/I²` of
> `I = Ker(σ)` is a finitely generated projective `R`-module.

```lean
theorem conormal_finite_projective (h : Algebra.Smooth R S) :
    Module.Finite R (RingHom.ker σ).Cotangent ∧
      Module.Projective R (RingHom.ker σ).Cotangent
```

**`adicCompletion_algEquiv_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 1068](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Conormal.lean#L1068). The attribute's comment: “(2)”. References: EGA 0 (19.0.2), “special case”; EGA 0 (19.5.4), “a) ⇒ c)”; EGA 0 (19.5.4.4), “partial”; EGA 0 (21.9.2), “special case”; EGA IV (17.5.3), “partial”; SGA 1 II (4.17), “affine case, (i)⇒(iii)”; SGA 1 III (1.5), “necessity, special case”; SGA 3 VIIB (5.5.2), “partial”; SGA 3 XI (1.2), “(ii), special case”.

> Part (2) of Stacks tag 05D5: the completion is a power series ring when the conormal
> module is free. If `S` is a smooth `R`-algebra, `σ : S →ₐ[R] R`, and the conormal module `I/I²` of
> `I = Ker(σ)` is free (necessarily of finite rank `d := Module.finrank R (I/I²)` by (1)),
> then the `I`-adic completion `S^∧` is isomorphic, as an `R`-algebra, to the formal power
> series `R`-algebra in `d` variables `R[[t_1, …, t_d]]`.

```lean
theorem adicCompletion_algEquiv_mvPowerSeries (h : Algebra.Smooth R S)
    (hfree : Module.Free R (RingHom.ker σ).Cotangent) :
    Nonempty (AdicCompletion (RingHom.ker σ) S ≃ₐ[R]
      MvPowerSeries (Fin (Module.finrank R (RingHom.ker σ).Cotangent)) R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.139, Tag 05D4](https://stacks.math.columbia.edu/tag/05D4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
