---
declaration: section
origin: cited
lean: IsLocalRing.exists_isPrime_height_eq_one_of_mem_maximalIdeal, AlgebraicGeometry.etaleAt_of_flat_of_unramifiedAt_codimensionOne, Stacks.PurityDimensionTwo.quotient_maximalIdeal_counterexample_clauseTwo, Stacks.PurityDimensionTwo.hasPurity_of_ringKrullDim_eq_two, Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_two_le_ringKrullDim, Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_ringKrullDim_eq_two, AlgebraicGeometry.purityAtRegularLocalRings, AlgebraicGeometry.etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne
statement: formalized
proof: formalized
---

# 58.21 Purity of branch locus

Section 58.21 of the Stacks Project, [Tag 0BJE](https://stacks.math.columbia.edu/tag/0BJE). 6 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJG, a lemma

[Tag 0BJG](https://stacks.math.columbia.edu/tag/0BJG) in the Stacks Project.

**`IsLocalRing.exists_isPrime_height_eq_one_of_mem_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/Basic.lean#L40).

> An element of the maximal ideal of a positive-dimensional Noetherian local ring is
> contained in a prime ideal of height one.

```lean
public theorem exists_isPrime_height_eq_one_of_mem_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hdim : 1 ≤ ringKrullDim A) (f : A) (hf : f ∈ IsLocalRing.maximalIdeal A) :
    ∃ p : Ideal A, p.IsPrime ∧ f ∈ p ∧ p.height = 1
```

## Tag 0BJH, a lemma

[Tag 0BJH](https://stacks.math.columbia.edu/tag/0BJH) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_of_flat_of_unramifiedAt_codimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/UnramifiedCodimensionOne.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/UnramifiedCodimensionOne.lean#L328).

> **Stacks Project, Tag 0BJH.** A flat morphism of locally Noetherian schemes which is
> quasi-finite at a point that is not the generic point of an irreducible component of its source
> is étale at that point, provided it is unramified at every one-dimensional generization of the
> point.

```lean
public theorem etaleAt_of_flat_of_unramifiedAt_codimensionOne
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat f]
    (x : X) (hqf : quasiFiniteAt f x) (hgen : x ∉ genericPoints X)
    (hunr : ∀ x' : X, x' ⤳ x → ringKrullDim (X.presheaf.stalk x') = 1 → UnramifiedAt f x') :
    EtaleAt f x
```

## Tag 0BMA, a lemma

[Tag 0BMA](https://stacks.math.columbia.edu/tag/0BMA) in the Stacks Project.

**`Stacks.PurityDimensionTwo.quotient_maximalIdeal_counterexample_clauseTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityClauseTwoCounterexample.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityClauseTwoCounterexample.lean#L116). The attribute's comment: “clause (2) as literally stated is false: for every regular local ring `A` with `2 ≤ ringKrullDim A`, `B = A ⧸ 𝔪` is a finite `A`-algebra and a normal ring (`IsNormalRing`), the preimage of the punctured spectrum under `Spec B ⟶ Spec A` is empty, so the induced morphism over the punctured spectrum is finite étale, but `A → B` is not étale (`A ⧸ 𝔪` is not even torsion-free over `A`). This is why the clause-(2) declaration `Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_two_le_ringKrullDim` carries the extra hypothesis `Module.IsTorsionFree A B`.”.

> **Clause (2) of [Stacks, Tag 0BMA] as literally stated is false: the residue field is a
> counterexample.** Let `A` be a regular local ring of dimension at least two and `B = A ⧸ 𝔪`.
> Then `B` is a finite `A`-algebra and a normal ring, the preimage of the punctured spectrum `U`
> under `Spec B ⟶ Spec A` is empty (so `Spec B ×_X U = ∅`), and `Spec B ⟶ Spec A` is étale over
> `U` (it is finite everywhere); but `A → B` is not étale. These are the hypotheses of clause (2)
> in the spelling of `Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_two_le_ringKrullDim`
> without its added hypothesis `Module.IsTorsionFree A B`, which `A ⧸ 𝔪` violates.

```lean
theorem quotient_maximalIdeal_counterexample_clauseTwo [IsRegularLocalRing A]
    (hdim : (2 : WithBot ℕ∞) ≤ ringKrullDim A) :
    Module.Finite A (A ⧸ maximalIdeal A) ∧ IsNormalRing (A ⧸ maximalIdeal A) ∧
      IsEmpty ↥(Spec.map (CommRingCat.ofHom (algebraMap A (A ⧸ maximalIdeal A))) ⁻¹ᵁ
        Stacks.puncturedSpectrum A) ∧
      Etale (Spec.map (CommRingCat.ofHom (algebraMap A (A ⧸ maximalIdeal A))) ∣_
        Stacks.puncturedSpectrum A) ∧
      ¬ Algebra.Etale A (A ⧸ maximalIdeal A)
```

**`Stacks.PurityDimensionTwo.hasPurity_of_ringKrullDim_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularDimensionTwo.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularDimensionTwo.lean#L127). The attribute's comment: “clause (1) of the tag, and in the case `d = 2`: `A` regular local with `ringKrullDim A = 2`, and the conclusion is `AlgebraicGeometry.HasPurity A`, i.e. essential surjectivity of `FÉt_{Spec A} ⟶ FÉt_U`, which is the source's definition of purity for `(A, 𝔪)`. This is the base case of the source's induction on `d`; the inductive step is tag 0BLM.”. References: SGA 2 X (3.4), “partial”.

> **Purity of the branch locus, [Stacks, Tag 0BMA] clause (1), in dimension two.** Let `A` be
> a regular local ring of Krull dimension `2`. Then every finite étale cover of the punctured
> spectrum of `A` is the restriction of a finite étale cover of `Spec A`.
>
> This is the source's argument. A regular local ring is a normal ring, so [Stacks, Tag 0BM9]
> applies to it: the global sections `B = Γ(V, 𝒪_V)` of a finite étale `V ⟶ U` are a finite normal
> `A`-algebra, torsion-free over `A`, whose spectrum is étale over `U`, and `V` extends over
> `Spec A` exactly when `B` is finite étale over `A`. The latter is clause (2) of the tag in
> dimension two, `etale_of_isNormalRing_of_ringKrullDim_eq_two`, whose hypotheses — normality of
> `B`, finiteness and torsion-freeness over `A`, and étaleness over the punctured spectrum — are
> precisely what [Stacks, Tag 0BM9] supplies.

```lean
public theorem hasPurity_of_ringKrullDim_eq_two (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdimA : ringKrullDim A = 2) :
    HasPurity A
```

**`Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_two_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularLocal.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularLocal.lean#L85). The attribute's comment: “clause (2) of the tag, at every `d ≥ 2`: `A` regular local with `2 ≤ ringKrullDim A`, `B` a finite `A`-algebra which is a normal ring in the sense of `IsNormalRing` (item (1) of tag 030C) and is torsion-free over `A`, and `Spec B ⟶ Spec A` étale over the punctured spectrum; the conclusion is `Algebra.Etale A B`. The source's derivation from clause (1) through tag 0BM9 is the proof, and clause (1) at every `d ≥ 2` is `AlgebraicGeometry.purityAtRegularLocalRings`. Torsion-freeness over `A` is an extra hypothesis, not present in the source and necessary for the statement to be true: the residue field `A ⧸ 𝔪` is a finite normal `A`-algebra whose spectrum misses the punctured spectrum, hence is étale there, and is not flat over `A`. Weakening it to injectivity of `algebraMap A B`, or to surjectivity of `Spec B ⟶ Spec A`, leaves the statement false as well: `B = A × (A ⧸ 𝔪)` is a finite normal `A`-algebra with both properties which is the identity over the punctured spectrum and is not flat over `A`. That clause (2) as literally stated is false is proved in `Stacks.PurityDimensionTwo.quotient_maximalIdeal_counterexample_clauseTwo` (`PurityBranchLocus.PurityClauseTwoCounterexample`); see also the module docstring of `PurityBranchLocus.RegularDimensionTwo`.”. References: SGA 1 X (3.2), “Case B finite over A”; SGA 4½ Arcata (5.2.4), “special case”.

> **[Stacks, Tag 0BMA] clause (2) for every `d ≥ 2`.** Let `A` be a regular local ring of
> dimension at least two and let `B` be a finite `A`-algebra which is a normal ring and
> torsion-free over `A`, such that `Spec B ⟶ Spec A` is étale over the punctured spectrum. Then
> `A → B` is étale.
>
> This is the source's derivation of clause (2) from clause (1) through [Stacks, Tag 0BM9]: `A` is
> normal, so `B` is an object of the category `NormalFiniteEtaleAwayAlgebra A` equivalent to
> `(FÉt_U)ᵒᵖ`, hence `B ≅ Γ(V, 𝒪_V)` for some finite étale `V ⟶ U`; purity extends `V` over
> `Spec A`, and the extension criterion of [Stacks, Tag 0BM9] then says that `Γ(V, 𝒪_V)` is finite
> étale over `A`.
>
> The hypothesis `Module.IsTorsionFree A B` is not in the source, and is necessary: it is exactly
> the point at which the source's statement of clause (2) is wrong, and the counterexample is
> recorded in the module docstring of
> `StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/RegularDimensionTwo.lean`. In
> brief: `B = A ⧸ 𝔪` is finite over `A`, is a field and hence a normal ring, and has empty
> punctured spectrum, so it is étale over `U` vacuously; but `A` is a domain with `𝔪 ≠ 0`, so
> `A ⧸ 𝔪` is not even flat over `A`; this is proved as
> `Stacks.PurityDimensionTwo.quotient_maximalIdeal_counterexample_clauseTwo`. Nor does it help to
> ask only that `algebraMap A B` be injective, or that `Spec B ⟶ Spec A` be surjective:
> `B = A × (A ⧸ 𝔪)` is a finite normal `A`-algebra satisfying both, is the identity over `U`, and
> is not flat over `A`.

```lean
public theorem etale_of_isNormalRing_of_two_le_ringKrullDim
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B] [IsRegularLocalRing A]
    [Module.Finite A B] [Module.IsTorsionFree A B] (hB : IsNormalRing B)
    (hdim : (2 : WithBot ℕ∞) ≤ ringKrullDim A)
    (hetale : Etale (Spec.map (CommRingCat.ofHom (algebraMap A B)) ∣_
      Stacks.puncturedSpectrum A)) :
    Algebra.Etale A B
```

**`Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_ringKrullDim_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/RegularDimensionTwo.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/RegularDimensionTwo.lean#L439). The attribute's comment: “clause (2) of the tag, and only in the case `d = 2`: `A` regular local with `ringKrullDim A = 2`, `B` a finite `A`-algebra which is a normal ring in the sense of `IsNormalRing` (item (1) of tag 030C) and is torsion-free over `A`, and `Spec B ⟶ Spec A` étale over the punctured spectrum; the conclusion is `Algebra.Etale A B`. This is the base case of the source's induction on `d`; the inductive step is tag 0BLM, and clause (2) for every `d ≥ 2` is `etale_of_isNormalRing_of_two_le_ringKrullDim` in `PurityBranchLocus.PurityRegularLocal`. Clause (1) at `d = 2` — essential surjectivity of `FÉt_X ⟶ FÉt_U`, i.e. purity for `A` — follows from this result through tag 0BM9 and is `Stacks.PurityDimensionTwo.hasPurity_of_ringKrullDim_eq_two`. Torsion-freeness over `A` is an extra hypothesis, not present in the source and necessary for the statement to be true: the residue field `A ⧸ 𝔪` is a finite normal `A`-algebra whose spectrum misses the punctured spectrum, hence is étale there, and is not étale over `A`. See the module docstring.”. References: SGA 1 X (3.2), “special case”.

> Let `A` be a regular local ring of Krull dimension `2`, and let `B` be a finite `A`-algebra
> which is a normal ring and torsion-free over `A`, such that the induced morphism on punctured
> spectra is étale. Then `A → B` is étale.

```lean
public theorem etale_of_isNormalRing_of_ringKrullDim_eq_two
    [IsRegularLocalRing A] [Module.Finite A B] [Module.IsTorsionFree A B]
    (hB : IsNormalRing B) (hdimA : ringKrullDim A = 2)
    (hetale : Etale (Spec.map (CommRingCat.ofHom (algebraMap A B)) ∣_
      Stacks.puncturedSpectrum A)) :
    Algebra.Etale A B
```

Declarations registered for the tag:

- [`AlgebraicGeometry.purityAtRegularLocalRings`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/RegularPurity.lean#L234), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularLocal.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/PurityRegularLocal.lean#L128) (StacksFrontier): “clause (1) of the tag, at every `d ≥ 2`: for every regular local ring `A` with `2 ≤ ringKrullDim A`, `AlgebraicGeometry.HasPurity A`, i.e. essential surjectivity of `FÉt_{Spec A} ⟶ FÉt_U` for `U` the punctured spectrum, which is the source's definition of purity for `(A, 𝔪)`.”.

## Tag 0BMB, a lemma

[Tag 0BMB](https://stacks.math.columbia.edu/tag/0BMB) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/AnyDimension.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/AnyDimension.lean#L697). The attribute's comment: “the whole tag, in every dimension: hypotheses (1) `𝒪_{X,x}` normal, (2) `𝒪_{Y,f x}` regular, (3) `f` quasi-finite at `x`, (4) `dim 𝒪_{X,x} = dim 𝒪_{Y,f x}` and `1 ≤ dim 𝒪_{X,x}`, and (5) `f` unramified at every point specializing to `x` whose local ring has dimension one; the conclusion is `EtaleAt f x`. The proof is the source's induction on `dim 𝒪_{X,x}`, with the case `dim 𝒪_{X,x} ≤ 2` as its base case and tag 0BMA clause (2) in every dimension, `Stacks.PurityDimensionTwo.etale_of_isNormalRing_of_two_le_ringKrullDim`, supplying Cohen–Macaulayness of `𝒪_{X,x}` above it.”. References: EGA IV (21.12.14), “(v), (v), special case”; SGA 1 X (3.1), “more general”; SGA 1 X (3.2), “more general”.

> **Purity of the branch locus, [Stacks, Tag 0BMB], in any dimension.** Let `f : X ⟶ Y` be a
> morphism of locally Noetherian schemes and let `x : X` be a point whose local ring is normal,
> with regular local ring at `f x`, at which `f` is quasi-finite, and such that the two local rings
> have the same dimension, which is at least one. If `f` is unramified at every point specializing
> to `x` whose local ring has dimension one, then `f` is étale at `x`.
>
> The hypotheses are exactly the tag's own.
>
> The proof is the source's induction on `d = dim 𝒪_{X,x}`. For `d ≤ 2` the conclusion is
> `AlgebraicGeometry.etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_le_two`. For
> `d ≥ 3` the induction hypothesis gives étaleness at every proper generization of `x` — their local
> rings are normal, the local rings below them regular, `f` is quasi-finite there because the
> quasi-finite locus is open, and the two dimensions agree there by
> `AlgebraicGeometry.ringKrullDim_stalk_eq_of_specializes_of_quasiFiniteAt` — and that is what makes
> `𝒪_{X,x}` Cohen–Macaulay, whence the conclusion. The Cohen–Macaulay step is where
> [Stacks, Tag 0BMA] clause (2) enters, through
> `Stacks.PurityBranchLocus.purityFiniteNormal`.

```lean
public theorem etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (x : X)
    (hX : IsNormalRing (X.presheaf.stalk x))
    (hY : IsRegularLocalRing (Y.presheaf.stalk (f x)))
    (hqf : quasiFiniteAt f x)
    (hdim : ringKrullDim (X.presheaf.stalk x) = ringKrullDim (Y.presheaf.stalk (f x)))
    (hone : 1 ≤ ringKrullDim (X.presheaf.stalk x))
    (hunr : ∀ x' : X, x' ⤳ x → ringKrullDim (X.presheaf.stalk x') = 1 → UnramifiedAt f x') :
    EtaleAt f x
```

**`AlgebraicGeometry.etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/DimensionAtMostTwo.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/DimensionAtMostTwo.lean#L232). The attribute's comment: “the case `1 ≤ dim 𝒪_{X,x} = dim 𝒪_{Y,f x} ≤ 2`. Hypotheses (1), (2), (3) and (5) are the tag's own; hypothesis (4) is the tag's `dim 𝒪_{X,x} = dim 𝒪_{Y,f x} ≥ 1` together with the case restriction `dim 𝒪_{X,x} ≤ 2`. Flatness of `𝒪_{Y,f x} → 𝒪_{X,x}` is miracle flatness (tag 00R4), a normal Noetherian local ring of dimension at most two being Cohen–Macaulay by Serre's criterion (tag 031S) and the fibre ring being zero-dimensional by quasi-finiteness; étaleness at `x` then follows from tag 0BJH. For `dim 𝒪_{X,x} ≥ 3` the same reduction leaves exactly the flatness of `𝒪_{Y,f x} → 𝒪_{X,x}`, which is tag 0BMA clause (2) at a general dimension. See the module docstring.”. References: EGA IV (21.12.14), “(v), (v), special case”; SGA 1 X (3.1), “partial, special case”.

> **Purity of the branch locus, [Stacks, Tag 0BMB], in dimension at most two.** Let
> `f : X ⟶ Y` be a morphism of locally Noetherian schemes and let `x : X` be a point whose local
> ring is normal, with regular local ring at `f x`, at which `f` is quasi-finite, and such that the
> two local rings have the same dimension, which is at least one and at most two. If `f` is
> unramified at every point specializing to `x` whose local ring has dimension one, then `f` is
> étale at `x`.
>
> This is the tag with its hypothesis `1 ≤ dim 𝒪_{X,x}` supplemented by `dim 𝒪_{X,x} ≤ 2`. See the
> module docstring for what the case `dim 𝒪_{X,x} ≥ 3` comes down to.

```lean
public theorem etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_le_two
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (x : X)
    (hX : IsNormalRing (X.presheaf.stalk x))
    (hY : IsRegularLocalRing (Y.presheaf.stalk (f x)))
    (hqf : quasiFiniteAt f x)
    (hdim : ringKrullDim (X.presheaf.stalk x) = ringKrullDim (Y.presheaf.stalk (f x)))
    (hone : 1 ≤ ringKrullDim (X.presheaf.stalk x))
    (hle : ringKrullDim (X.presheaf.stalk x) ≤ 2)
    (hunr : ∀ x' : X, x' ⤳ x → ringKrullDim (X.presheaf.stalk x') = 1 → UnramifiedAt f x') :
    EtaleAt f x
```

**`AlgebraicGeometry.etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/DimensionOne.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/DimensionOne.lean#L201). The attribute's comment: “the case `dim 𝒪_{X,x} = dim 𝒪_{Y,f x} = 1`, which is the base case of the source's induction on the dimension; hypotheses (1), (2), (3) and (5) are the tag's own and hypothesis (4) is the tag's with `1 ≤ d` restricted to `d = 1`. The range `1 ≤ d ≤ 2` is `etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_le_two` in `PurityBranchLocus.DimensionAtMostTwo`.”. References: EGA IV (21.12.14), “(v)”; SGA 1 X (3.1), “partial”.

> **Purity of the branch locus, [Stacks, Tag 0BMB], in dimension one.** Let `f : X ⟶ Y` be a
> morphism of locally Noetherian schemes and let `x : X` be a point whose local ring is normal,
> with regular local ring at `f x`, at which `f` is quasi-finite, and such that the two local
> rings have the same dimension, equal to one. If `f` is unramified at every point specializing
> to `x` whose local ring has dimension one, then `f` is étale at `x`.
>
> This is the tag with its hypothesis `1 ≤ dim 𝒪_{X,x}` restricted to `dim 𝒪_{X,x} = 1`, the base
> case of the source's induction on the dimension. The whole range `1 ≤ dim 𝒪_{X,x} ≤ 2` is
> `etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_le_two` in
> `PurityBranchLocus.DimensionAtMostTwo`, which subsumes this statement.

```lean
theorem etaleAt_of_quasiFiniteAt_of_unramifiedAt_codimensionOne_of_dim_eq_one
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (x : X)
    (hX : IsNormalRing (X.presheaf.stalk x))
    (hY : IsRegularLocalRing (Y.presheaf.stalk (f x)))
    (hqf : quasiFiniteAt f x)
    (hdim : ringKrullDim (X.presheaf.stalk x) = ringKrullDim (Y.presheaf.stalk (f x)))
    (hone : ringKrullDim (X.presheaf.stalk x) = 1)
    (hunr : ∀ x' : X, x' ⤳ x → ringKrullDim (X.presheaf.stalk x') = 1 → UnramifiedAt f x') :
    EtaleAt f x
```

## Tag 0EY6, a lemma

[Tag 0EY6](https://stacks.math.columbia.edu/tag/0EY6) in the Stacks Project.

**`Stacks.FundamentalGroup.flatBaseChange_algebraPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/AlgebraComparisonEpi.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/AlgebraComparisonEpi.lean#L395). The attribute's comment: “flat\_base\_change”.

> **The base-change clause of [Stacks, Tag 0EY6].**  For a quasi-compact quasi-separated
> morphism `f : V ⟶ Y` and a flat morphism `q : Y' ⟶ Y`, the pushed-forward structure sheaf of the
> base change is the extension of scalars of the inverse image of `f_* 𝒪_V`.

```lean
public theorem flatBaseChange_algebraPullback {V Y Y' : Scheme.{u}} (f : V ⟶ Y)
    [QuasiCompact f] [QuasiSeparated f] (q : Y' ⟶ Y) [Flat q] :
    IsPushout
      ((TopCat.Sheaf.pullback CommRingCat q.base).map (pushforwardAlgebra f).hom)
      (inverseImageStructureMap q)
      (pushforwardBaseChangeMap q (Over.mk f))
      (pushforwardAlgebra ((Over.pullback q).obj (Over.mk f)).hom).hom
```

**`Stacks.FundamentalGroup.exists_extendedEtaleAlgebraComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/ExtensionAlgebra.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/ExtensionAlgebra.lean#L266). The attribute's comment: “flat\_base\_change”.

> **[Stacks, Tag 0EY6], flat base change of the extension algebra.**  Let `X` be locally
> Noetherian, `j : U ⟶ X` an open immersion whose complement carries depth at least two and
> `π : V ⟶ U` a finite étale cover, and let `g : X' ⟶ X` be flat with `j'` the base change of `j`
> and `π'` the base change of `π`.  Then every extension of scalars of the extension algebra
> `𝓑 = (π ≫ j)_* 𝒪_V` along `g` is canonically isomorphic to the extension algebra
> `(π' ≫ j')_* 𝒪_{V'}` of the base-changed cover, by an isomorphism carrying the canonical map
> `g⁻¹𝓑 ⟶ g⁺𝓑` to the base-change morphism transported along the Cartesian comparison of
> covers.
>
> This is stated for an arbitrary `Stacks.RelativeSpec.AlgebraPullback`, hence in particular for
> any choice of one;  `exists_extendedEtaleAlgebraComparison_algebraPullbackOfFlat` is the
> instance at `algebraPullbackOfFlat`.

```lean
public theorem exists_extendedEtaleAlgebraComparison {U X V U' X' V' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (π' : V' ⟶ U') [IsFinite π'] [Etale π'] (gV : V' ⟶ V)
    (hj : IsPullback j' gU g j)
    (hπ : IsPullback π' gV gU π)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x))
    (d : AlgebraPullback (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g) :
    let hdepth' := extendedEtaleDepth_flatBaseChange j g j' gU hj hdepth
    let e : Over.mk (π' ≫ j') ≅ (Over.pullback g).obj (Over.mk (π ≫ j)) :=
      Over.isoMk (hπ.paste_horiz hj).flip.isoPullback (by simp)
    ∃ i : d.algebra ≅
        (ExtendedEtaleFold.extendedEtaleSituation j' π' hdepth').algebra,
      d.map ≫ i.hom.right =
        pushforwardBaseChangeMap g (Over.mk (π ≫ j)) ≫
          (pushforwardAlgebraMap e.hom).right
```

**`Stacks.FundamentalGroup.extendedEtaleAlgebraComparison_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean#L125). The attribute's comment: “flat\_base\_change”.

> **The comparison carries the canonical map of the extension of scalars to the base-change
> morphism**, transported along the Cartesian comparison of covers.  This is the property that
> specifies `Stacks.FundamentalGroup.extendedEtaleAlgebraComparison`.

```lean
public theorem extendedEtaleAlgebraComparison_map {U X V U' X' V' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (π' : V' ⟶ U') [IsFinite π'] [Etale π'] (gV : V' ⟶ V)
    (hj : IsPullback j' gU g j)
    (hπ : IsPullback π' gV gU π)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x))
    (d : AlgebraPullback (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g) :
    d.map ≫
        (extendedEtaleAlgebraComparison j π g j' gU π' gV hj hπ hdepth d).hom.right =
      pushforwardBaseChangeMap g (Over.mk (π ≫ j)) ≫
        (pushforwardAlgebraMap
          (Over.isoMk (hπ.paste_horiz hj).flip.isoPullback (by simp) :
            Over.mk (π' ≫ j') ≅ (Over.pullback g).obj (Over.mk (π ≫ j))).hom).right
```

**`Stacks.FundamentalGroup.extendedEtaleSpectrumComparison_universalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean#L187). The attribute's comment: “flat\_base\_change”.

> **[Stacks, Tag 0EY6], the universal-map equation for the spectrum comparison.**  Under the
> representing bijection of [Stacks, Tag 01LV] the comparison is the structure morphism of the
> base-changed relative spectrum together with its universal algebra map precomposed with the
> algebra comparison.  This is the defining property of
> `Stacks.FundamentalGroup.extendedEtaleSpectrumComparison`, so it holds by
> `Equiv.apply_symm_apply`.

```lean
public theorem extendedEtaleSpectrumComparison_universalMap {U X V U' X' V' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (π' : V' ⟶ U') [IsFinite π'] [Etale π'] (gV : V' ⟶ V)
    (hj : IsPullback j' gU g j)
    (hπ : IsPullback π' gV gU π)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x))
    (d : AlgebraPullback (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g) :
    let e := ExtendedEtaleFold.extendedEtaleSituation j' π'
      (extendedEtaleDepth_flatBaseChange j g j' gU hj hdepth)
    (relativeSpecRepresentableBy d.situation).homEquiv
        (extendedEtaleSpectrumComparison j π g j' gU π' gV hj hπ hdepth d) =
      ⟨(gluedSpectrum e).toBase,
        algebraHomAsUnder
            (extendedEtaleAlgebraComparison j π g j' gU π' gV hj hπ hdepth d).hom ≫
          universalAlgebraMap e⟩
```

**`Stacks.FundamentalGroup.isIso_extendedEtaleSpectrumComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/SpectrumComparison.lean#L216). The attribute's comment: “flat\_base\_change”.

> **[Stacks, Tag 0EY6], the spectrum comparison is an isomorphism.**  The two relative spectra
> represent functors identified by
> `Stacks.RelativeSpec.relativeSpecFunctorIsoOfAlgebraIso`, and the comparison is the induced
> comparison of representing objects.

```lean
public theorem isIso_extendedEtaleSpectrumComparison {U X V U' X' V' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (π' : V' ⟶ U') [IsFinite π'] [Etale π'] (gV : V' ⟶ V)
    (hj : IsPullback j' gU g j)
    (hπ : IsPullback π' gV gU π)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x))
    (d : AlgebraPullback (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g) :
    IsIso (extendedEtaleSpectrumComparison j π g j' gU π' gV hj hπ hdepth d)
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtaleAlgebra_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean#L134). The attribute's comment: “algebra”.

> **The extension algebra of a finite étale cover is a coherent module over the base.** Let
> `j : U ⟶ X` be an open immersion into a locally Noetherian scheme whose complement carries depth at
> least two and let `π : V ⟶ U` be finite étale. Then the `𝒪_X`-module underlying
> `𝓑 = (π ≫ j)_* 𝒪_V` is coherent.

```lean
public theorem extendedEtaleAlgebra_isCoherent {U X V : Scheme.{u}} [IsLocallyNoetherian X]
    (j : U ⟶ X) [IsOpenImmersion j] (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    _root_.SheafOfModules.IsCoherent
      (AlgebraSheaf.underlyingModule (pushforwardAlgebra (π ≫ j)))
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtaleAlgebra_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean#L149). The attribute's comment: “algebra”.

> **The extension algebra of a finite étale cover is reflexive as a module over the base.** Let
> `j : U ⟶ X` be an open immersion into a locally Noetherian scheme whose complement carries depth at
> least two and let `π : V ⟶ U` be finite étale. Then the `𝒪_X`-module underlying
> `𝓑 = (π ≫ j)_* 𝒪_V` is reflexive.

```lean
public theorem extendedEtaleAlgebra_isReflexive {U X V : Scheme.{u}} [IsLocallyNoetherian X]
    (j : U ⟶ X) [IsOpenImmersion j] (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    IsReflexive (AlgebraSheaf.underlyingModule (pushforwardAlgebra (π ≫ j)))
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtaleSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Algebra.lean#L165). The attribute's comment: “algebra”.

> **The extension algebra, with its quasi-coherence, as a relative-spectrum situation.** It is
> the pair consisting of `X` and the quasi-coherent `𝒪_X`-algebra `𝓑 = (π ≫ j)_* 𝒪_V`, whose relative
> spectrum `Spec_X(𝓑)` is the extension scheme of the cover.

```lean
public def extendedEtaleSituation {U X V : Scheme.{u}} [IsLocallyNoetherian X] (j : U ⟶ X)
    [IsOpenImmersion j] (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    Stacks.RelativeSpec.RelativeSpecSituation.{u}
```

**`Stacks.FundamentalGroup.extendedEtaleSpectrum_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/FlatBaseChangeSquare.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/FlatBaseChangeSquare.lean#L122). The attribute's comment: “flat\_base\_change”.

> **The `flat_base_change` clause of [Stacks, Tag 0EY6], the Cartesian square of relative
> spectra.** Let `X` be locally Noetherian, `j : U ⟶ X` an open immersion whose complement
> carries depth at least two and `π : V ⟶ U` a finite étale cover, and let `g : X' ⟶ X` be flat
> with `j'` the base change of `j` and `π'` the base change of `π`. Then
> `Spec_{X'}((π' ≫ j')_* 𝒪_{V'})` is the fibre product of `Spec_X((π ≫ j)_* 𝒪_V)` with `X'` over
> `X`.
>
> The morphism exhibiting it is the comparison
> `extendedEtaleSpectrumComparison` of the two algebras on `X'` — an isomorphism over `X'`,
> because flat base change identifies the extension of scalars of `(π ≫ j)_* 𝒪_V` with
> `(π' ≫ j')_* 𝒪_{V'}` — followed by the canonical base-change morphism
> `Stacks.RelativeSpec.relativeSpectrumBaseChangeMap`, whose square is Cartesian by
> [Stacks, Tag 01LX] part (2). Transporting the latter square along the former isomorphism is
> `extendedEtaleSpectrum_flatBaseChange_of_isPullback`.

```lean
public theorem extendedEtaleSpectrum_flatBaseChange {U X V U' X' V' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (π' : V' ⟶ U') [IsFinite π'] [Etale π'] (gV : V' ⟶ V)
    (hj : IsPullback j' gU g j)
    (hπ : IsPullback π' gV gU π)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x)) :
    IsPullback
      (gluedSpectrum (ExtendedEtaleFold.extendedEtaleSituation j' π'
        (extendedEtaleDepth_flatBaseChange j g j' gU hj hdepth))).toBase
      (extendedEtaleSpectrumComparison j π g j' gU π' gV hj hπ hdepth
            (pullbackAlgebra (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g) ≫
        relativeSpectrumBaseChangeMap (ExtendedEtaleFold.extendedEtaleSituation j π hdepth) g)
      g (gluedSpectrum (ExtendedEtaleFold.extendedEtaleSituation j π hdepth)).toBase
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.existsUnique_restrictionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/LargerOpenIso.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/LargerOpenIso.lean#L68). The attribute's comment: “larger\_open”.

> **The `larger_open` clause of [Stacks, Tag 0EY6].** Let `i : U ⟶ U'` and `k : U' ⟶ X` be
> open immersions into a locally Noetherian scheme with `X ∖ (i ≫ k)(U)` of depth at least two,
> let `π : V ⟶ U` be a finite étale cover and let `Y = Spec_X(𝓑)` be its canonical extension, for
> `𝓑 = (π ≫ i ≫ k)_* 𝒪_V`. Given a finite étale cover `π' : V' ⟶ U'` of the larger open
> subscheme, an identification `eY` of the restriction of `Y` to `U` with `π`, and an
> identification `eV` of the restriction of `π'` to `U` with `π`, there is exactly one
> isomorphism over `U'` between the restriction of `Y` to `U'` and `π'` whose own restriction to
> `U` carries `eV` back to `eY`.
>
> Both `Y ×_X U'` and `V'` are finite over `U'`, restrict over `U` to `π`, and have depth at
> least two above `U' ∖ i(U)`; so `extendedEtale_unique`, over the base `U'`, identifies each
> with the extension of `π` across that complement, and the isomorphism is the composite of those
> two identifications. Its uniqueness is the uniqueness in that clause.

```lean
public theorem existsUnique_restrictionIso {U U' X V V' : Scheme.{u}} [IsLocallyNoetherian X]
    (i : U ⟶ U') [IsOpenImmersion i] (k : U' ⟶ X) [IsOpenImmersion k]
    (π : V ⟶ U) [IsFinite π] [Etale π] (π' : V' ⟶ U') [IsFinite π'] [Etale π']
    (hdepth : ∀ x : X, x ∉ ((i ≫ k).opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    let Y := gluedSpectrum (extendedEtaleSituation (i ≫ k) π hdepth)
    ∀ (eY : (Over.pullback (i ≫ k)).obj (Over.mk Y.toBase) ≅ Over.mk π)
      (eV : (Over.pullback i).obj (Over.mk π') ≅ Over.mk π),
      ∃! e : (Over.pullback k).obj (Over.mk Y.toBase) ≅ Over.mk π',
        (Over.pullbackComp i k).hom.app (Over.mk Y.toBase) ≫
          (Over.pullback i).map e.hom ≫ eV.hom = eY.hom
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.etaleAt_iff_isFlatAt_extendedEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Purity.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Purity.lean#L148). The attribute's comment: “etale\_iff\_flat”.

> **The `etale_iff_flat` clause of [Stacks, Tag 0EY6].** Let `j : U ⟶ X` be an open immersion
> into a locally Noetherian scheme whose complement carries depth at least two and let
> `π : V ⟶ U` be finite étale. At every point of the canonical extension `Y = Spec_X(𝓑)`, for
> `𝓑 = (π ≫ j)_* 𝒪_V`, the structure morphism `Y ⟶ X` is étale if and only if it is flat.
>
> Forwards this is one half of "étale is flat and G-unramified". Backwards, write `W` for the flat
> locus of `Y ⟶ X`, an open subscheme by [Stacks, Tag 05IM] since the base has locally finite
> weakly associated points, and let `y ∈ W`. If `y` lies over the open `j(U)` then `Y ⟶ X` is
> étale at `y` outright, because over `j(U)` it is the finite étale cover `π`
> (`extendedEtaleCoverMap_isPullback`). Otherwise the depth clause
> (`extendedEtale_depth_ge_two`) gives `depth 𝒪_{Y, y} ≥ 2`, hence `dim 𝒪_{Y, y} ≥ 2`; so `y` is
> not a generic point of a component of `W`, and any `z ⤳ y` with `dim 𝒪_{W, z} = 1` must lie over
> `j(U)`, where `Y ⟶ X` is étale and so unramified. Those are the hypotheses of
> [Stacks, Tag 0BJH], which turns flatness at `y` into étaleness at `y`.

```lean
public theorem etaleAt_iff_isFlatAt_extendedEtale {U X V : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    let Y := gluedSpectrum (extendedEtaleSituation j π hdepth)
    ∀ y : Y.scheme,
      EtaleAt Y.toBase y ↔ IsFlatAt Y.toBase.toLRSHom.toShHom y
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.etale_iff_isFiniteLocallyFree_extendedEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Purity.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/Purity.lean#L238). The attribute's comment: “etale\_iff\_free”.

> **The `etale_iff_free` clause of [Stacks, Tag 0EY6].** The structure morphism of the
> canonical extension `Y = Spec_X(𝓑)` is étale if and only if `𝓑 = (π ≫ j)_* 𝒪_V` is finite
> locally free as an `𝒪_X`-module.
>
> The chain is: étale means étale at every point
> (`AlgebraicGeometry.etale_iff_forall_etaleAt`); at every point étale is flat
> (`etaleAt_iff_isFlatAt_extendedEtale`); flat at every point means flat
> (`AlgebraicGeometry.Flat.iff_flat_stalkMap`); and for a morphism over a locally Noetherian base
> finite plus flat is finite locally free ([Stacks, Tag 02KB]), which for an affine morphism is
> finite local freeness of the direct image of its structure sheaf ([Stacks, Tag 02KA]). That
> direct image is `𝓑` itself, because `Y` is the relative spectrum of `𝓑`
> (`Stacks.AffineAlgebraEquivalence.pushforwardAlgebraIso`).

```lean
public theorem etale_iff_isFiniteLocallyFree_extendedEtale {U X V : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    let Y := gluedSpectrum (extendedEtaleSituation j π hdepth)
    Etale Y.toBase ↔
      _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (AlgebraSheaf.underlyingModule (pushforwardAlgebra (π ≫ j)))
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.isFinite_extendedEtaleToBase`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtension.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtension.lean#L70). The attribute's comment: “unique\_extension”.

> The extension of a finite étale cover across a depth-two complement is finite over the base:
> the structure morphism of `Spec_X(𝓑)`, for `𝓑 = (π ≫ j)_* 𝒪_V`, is a finite morphism.

```lean
public instance isFinite_extendedEtaleToBase : IsFinite (extendedEtaleToBase j π hdepth)
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtaleCoverMap_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionCover.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionCover.lean#L134). The attribute's comment: “unique\_extension”.

> **The comparison morphism identifies the cover with the restriction of the extension to the
> open subscheme.** This is the pullback clause of [Stacks, Tag 0EY6]: the square formed by the
> cover `π`, the comparison morphism, the open immersion `j` and the structure morphism of the
> extension is cartesian.

```lean
public theorem extendedEtaleCoverMap_isPullback :
    IsPullback π (extendedEtaleCoverMap j π hdepth) j
      (gluedSpectrum (extendedEtaleSituation j π hdepth)).toBase
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtale_depth_ge_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionDepth.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionDepth.lean#L284). The attribute's comment: “unique\_extension”.

> **The depth clause of [Stacks, Tag 0EY6].** The local rings of the extension
> `Spec_X(𝓑)` of a finite étale cover across a depth-two complement have depth at least two above
> every point of `X` outside the cover.
>
> The stalk of `𝓑` at such a point has depth at least two over the local ring of the base
> (`two_le_depth_stalk_extendedEtaleAlgebra`); the local ring of `Spec_X(𝓑)` at a point above it is
> a localization of that stalk at a maximal ideal, so its depth is at least as large
> (`depth_stalk_pushforwardAlgebra_le_depth_stalk`). The identification of `𝓑` with the structure
> algebra of its own relative spectrum is
> `Stacks.AffineAlgebraEquivalence.pushforwardAlgebraIso`.

```lean
public theorem extendedEtale_depth_ge_two :
    let Y := (relativeSpectrum (extendedEtaleSituation j π hdepth)).scheme
    let f := (relativeSpectrum (extendedEtaleSituation j π hdepth)).toBase
    ∀ y : Y, f y ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (Y.presheaf.stalk y)
        (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
        (Y.presheaf.stalk y)
```

**`Stacks.FundamentalGroup.ExtendedEtaleFold.extendedEtale_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionUniqueness.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtale/UniqueExtensionUniqueness.lean#L245). The attribute's comment: “unique\_extension”.

> **The extension of a finite étale cover is the unique finite extension with the same
> restriction over the open subscheme and the same depth condition off it.** This is the
> uniqueness clause of [Stacks, Tag 0EY6]: for any finite `f' : Y' ⟶ X` whose restriction over
> `U` is the given cover and whose local rings off `U` have depth at least two, there is exactly
> one isomorphism of `Y'` with the relative spectrum of `(π ≫ j)_* 𝒪_V` commuting both with the
> structure morphisms to `X` and with the canonical comparison from the cover.

```lean
public theorem extendedEtale_unique {U X V Y' : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    (π : V ⟶ U) [IsFinite π] [Etale π]
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x))
    (f' : Y' ⟶ X) [IsFinite f'] (g' : V ⟶ Y')
    (hg' : IsPullback π g' j f')
    (hdepth' : ∀ y : Y', f' y ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (Y'.presheaf.stalk y)
        (IsLocalRing.maximalIdeal (Y'.presheaf.stalk y))
        (Y'.presheaf.stalk y)) :
    ∃! e : Y' ≅ (gluedSpectrum (extendedEtaleSituation j π hdepth)).scheme,
      (e.hom ≫ (gluedSpectrum (extendedEtaleSituation j π hdepth)).toBase = f') ∧
      (g' ≫ e.hom = extendedEtaleCoverMap j π hdepth)
```

**`Stacks.FundamentalGroup.extendedEtaleDepth_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtaleBaseChange.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ExtendedEtaleBaseChange.lean#L92). The attribute's comment: “flat\_base\_change”.

> **Stacks 0EY6, flat base change: the depth condition.** Depth at least two outside the open
> subscheme persists after flat base change: if the local rings of `X` at the points outside the
> open `U` have depth at least two and `g : X' ⟶ X` is flat with `U' = g⁻¹(U)`, then the local
> rings of `X'` at the points outside `U'` have depth at least two.
>
> This is one of the seven declarations making up tag 0EY6's `flat_base_change` clause. All
> seven are now proved — the last was the Cartesian square of relative spectra, in
> `StacksFrontier.AlgebraicGeometry.FundamentalGroup.ExtendedEtale.FlatBaseChangeSquare` — so each
> carries `@[stacks 0EY6 "flat_base_change"]`, the clause string recording which part of the tag
> is covered.

```lean
theorem extendedEtaleDepth_flatBaseChange {U X U' X' : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian X']
    (j : U ⟶ X) [IsOpenImmersion j]
    (g : X' ⟶ X) [Flat g]
    (j' : U' ⟶ X') [IsOpenImmersion j'] (gU : U' ⟶ U)
    (hj : IsPullback j' gU g j)
    (hdepth : ∀ x : X, x ∉ (j.opensRange : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x)) :
    ∀ x' : X', x' ∉ (j'.opensRange : Set X') →
      (2 : ℕ∞) ≤ Module.depth (X'.presheaf.stalk x')
        (IsLocalRing.maximalIdeal (X'.presheaf.stalk x'))
        (X'.presheaf.stalk x')
```

## Tag 0EY7, a lemma

[Tag 0EY7](https://stacks.math.columbia.edu/tag/0EY7) in the Stacks Project.

**`AlgebraicGeometry.essSurj_finiteEtaleBaseChange_of_hasPurity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendFiniteEtale.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendFiniteEtale.lean#L346).

> **Stacks Project, Tag 0EY7.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes
> such that purity holds for `𝒪_{X, x}` at every point `x` outside the image of `j`.  Then every
> finite étale cover of `U` is the restriction of a finite étale cover of `X`.

```lean
theorem essSurj_finiteEtaleBaseChange_of_hasPurity
    {X U : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] [IsNoetherian X]
    (h : ∀ x : X, x ∉ j.opensRange → HasPurity (X.presheaf.stalk x)) :
    (finiteEtaleBaseChange j).EssSurj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.21, Tag 0BJE](https://stacks.math.columbia.edu/tag/0BJE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
