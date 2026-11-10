---
declaration: section
origin: cited
lean: Stacks.CoordinateImmersion.hasImmersionTwistOver_of_isRelativelyVeryAmple, AlgebraicGeometry.exists_immersion_affineSpace, Stacks.StalkwiseGeneration.exists_immersion_projectiveSpaceOver_of_isAmple, Stacks.AmpleRelativeFiniteType.tfae, Stacks.AmpleRelativeFiniteType.tfae_six, Stacks.AmpleRelativeFiniteType.isAmple_iff_exists_isRelativelyVeryAmple, Stacks.AmpleRelativeFiniteType.isAmple_iff_eventually_isRelativelyVeryAmple, Stacks.AmpleRelativeFiniteType.tfae_six_pos
statement: formalized
proof: formalized
---

# 29.40 Ample and very ample sheaves relative to finite type morphisms

Section 29.40 of the Stacks Project, [Tag 02NO](https://stacks.math.columbia.edu/tag/02NO). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02NP, a lemma

[Tag 02NP](https://stacks.math.columbia.edu/tag/02NP) in the Stacks Project.

**`Stacks.CoordinateImmersion.hasImmersionTwistOver_of_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmpleAffineBase/CoordinateImmersion.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmpleAffineBase/CoordinateImmersion.lean#L593). References: EGA II (5.3.3), “special case”.

> **Stacks Tag 02NP.** A relatively very ample invertible sheaf on a scheme of finite type over
> an affine base is the hyperplane sheaf pulled back along an immersion into a finite-dimensional
> projective space over that base, lying over the base.
>
> Finite type is the conjunction of local finiteness of type with quasi-compactness, and the
> conclusion is `Stacks.AmpleProjectiveImmersion.HasImmersionTwistOver`, the source's conclusion
> written out.
>
> `Stacks.VeryAmpleAffineBase.hasImmersionTwistOver_of_isRelativelyVeryAmple` is the same statement
> on the hypothesis `Stacks.VeryAmpleAffineBase.ProjCoordinateCut`, the coordinate-cutting step of
> the source's proof; that hypothesis is discharged by
> `Stacks.CoordinateImmersion.projCoordinateCut`.

```lean
theorem hasImmersionTwistOver_of_isRelativelyVeryAmple {S X : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L] [LocallyOfFiniteType f]
    [QuasiCompact f] [IsAffine S]
    (hL : Tag01VMVeryAmple.IsRelativelyVeryAmple f L) :
    AmpleProjectiveImmersion.HasImmersionTwistOver f L
```

## Tag 04II, a lemma

[Tag 04II](https://stacks.math.columbia.edu/tag/04II) in the Stacks Project.

**`AlgebraicGeometry.exists_immersion_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineSpaceImmersion.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineSpaceImmersion.lean#L162).

> **Stacks Project, Tag 04II.** A quasi-affine scheme locally of finite type over `S` admits,
> over `S`, an immersion into a finite-dimensional relative affine space.

```lean
theorem exists_immersion_affineSpace
    {X S : Scheme.{u}} (f : X ⟶ S) [X.IsQuasiAffine] [LocallyOfFiniteType f] :
    ∃ (n : ℕ) (i : X ⟶ AffineSpace (ULift.{u} (Fin n)) S),
      IsImmersion i ∧ i ≫ (AffineSpace (ULift.{u} (Fin n)) S ↘ S) = f
```

## Tag 01VS, a lemma

[Tag 01VS](https://stacks.math.columbia.edu/tag/01VS) in the Stacks Project.

**`Stacks.StalkwiseGeneration.exists_immersion_projectiveSpaceOver_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StalkwiseGeneration/Ample.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StalkwiseGeneration/Ample.lean#L81).

> **[Stacks, Tag 01VS].** For `f : X ⟶ S` locally of finite type and `L` an ample invertible
> `𝒪_X`-module there is a `d₀ ≥ 1` such that every degree `d ≥ d₀` admits an immersion
> `i : X ⟶ ℙⁿ_S` over `S` pulling the twisting sheaf `𝒪(1)` back to `L ^⊗ d`.

```lean
theorem exists_immersion_projectiveSpaceOver_of_isAmple {S : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] (hL : IsAmple X L) [LocallyOfFiniteType f] :
    ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
      ∃ (n : ℕ) (i : X ⟶ projectiveSpaceOver n S),
        IsImmersion i ∧
        i ≫ pullback.fst (terminal.from S)
          (terminal.from (projectiveSpaceAtUniverse.{u} n)) = f ∧
        Nonempty (tensorPowModule X L (d : ℤ) ≅
          (Scheme.Modules.pullback i).obj (projectiveSpaceTwistingSheaf n S))
```

## Tag 01VT, a lemma

[Tag 01VT](https://stacks.math.columbia.edu/tag/01VT) in the Stacks Project.

**`Stacks.AmpleRelativeFiniteType.tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/Basic.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/Basic.lean#L151). The attribute's comment: “conditions (1), (2), (5) and (6) of the six; conditions (3) and (4), relative very ampleness, are stated together with these four by `Stacks.AmpleRelativeFiniteType.tfae_six`, and (5), (6) are taken with no lower bound on `n`, which `Stacks.AmpleProjectiveImmersion.hasImmersionTwistOverPos_iff` shows is the source's `n ≥ 1` clause”.

> **[Stacks, Tag 01VT], conditions (1), (2), (5) and (6), unconditionally.** For `f : X ⟶ S`
> of finite type with `S` affine and `L` an invertible `𝒪_X`-module, the following are equivalent:
>
> 1. `L` is ample on `X`;
> 2. `L` is ample relative to `f`;
> 3. (the source's (5)) `L ^⊗ d` is `𝒪(1)` pulled back along an immersion `X ⟶ ℙⁿ_S` over `S`, for
>    some `d ≥ 1`;
> 4. (the source's (6)) the same, for every sufficiently large `d`.
>
> The cycle is (1) ⟹ (4) ⟹ (3) ⟹ (2) ⟹ (1). The first step is [Stacks, Tag 01VS] at the single
> situation `(X, S, f, L)` — no covering of the base and no glueing, which is what affineness of
> `S` buys — the second is dropping the lower bound on the degree, the third is [Stacks, Tag 01VN]
> together with [Stacks, Tag 02NN], and the last two are the two halves of [Stacks, Tag 01VK].
>
> The source's conditions (3) and (4), relative very ampleness, are not among the four; they join
> them in `Stacks.AmpleRelativeFiniteType.tfae_six`, in the sibling module
> `StacksFrontier.AlgebraicGeometry.AmpleRelativeFiniteType.VeryAmple`.

```lean
theorem tfae [IsAffine S] (f : X ⟶ S) (L : X.Modules) [IsInvertibleModule X L]
    [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE [
      IsAmple X L,
      Stacks.RelativeAmple.IsRelativelyAmple f L,
      ∃ d : ℕ, 1 ≤ d ∧ HasImmersionTwistOver f (tensorPowModule X L (d : ℤ)),
      ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
        HasImmersionTwistOver f (tensorPowModule X L (d : ℤ))]
```

**`Stacks.AmpleRelativeFiniteType.tfae_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean#L190). The attribute's comment: “all six conditions, with no named input: ampleness, `f`-ampleness, relative very ampleness of some and of every sufficiently high tensor power, and the two immersion clauses; the immersion clauses are taken with no lower bound on the dimension `n` of the projective space, where the source writes `n ≥ 1` — the two agree by `Stacks.AmpleProjectiveImmersion.hasImmersionTwistOverPos_iff`, and `Stacks.AmpleRelativeFiniteType.tfae_six_pos` is the list with the source's clauses”.

> **[Stacks, Tag 01VT], all six conditions, with no named input.** For
> `f : X ⟶ S` of finite type with `S` affine and `L` an invertible `𝒪_X`-module, the following are
> equivalent:
>
> 1. `L` is ample on `X`;
> 2. `L` is ample relative to `f`;
> 3. `L ^⊗ d` is very ample relative to `f`, for some `d ≥ 1`;
> 4. `L ^⊗ d` is very ample relative to `f`, for every sufficiently large `d`;
> 5. `L ^⊗ d` is `𝒪(1)` pulled back along an immersion `X ⟶ ℙⁿ_S` over `S`, for some `d ≥ 1`;
> 6. the same, for every sufficiently large `d`.
>
> The cycle is (1) ⟹ (6) ⟹ (4) ⟹ (3) ⟹ (2) ⟹ (1), with (5) attached to (1) in both directions.
> Only (6) ⟹ (4) uses the module half of [Stacks, Tag 01OE], which over an affine base is
> `Stacks.SymGraded.hasFreeBundleTwistOne`; see the module documentation for the rest.
>
> Conditions (5) and (6) are taken with no lower bound on `n`, as in
> `Stacks.AmpleRelativeFiniteType.tfae`.

```lean
theorem tfae_six [IsAffine S]
    (f : X ⟶ S) (L : X.Modules) [IsInvertibleModule X L] [LocallyOfFiniteType f]
    [QuasiCompact f] :
    List.TFAE [
      IsAmple X L,
      Stacks.RelativeAmple.IsRelativelyAmple f L,
      ∃ d : ℕ, 1 ≤ d ∧
        Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ)),
      ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
        Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ)),
      ∃ d : ℕ, 1 ≤ d ∧ HasImmersionTwistOver f (tensorPowModule X L (d : ℤ)),
      ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
        HasImmersionTwistOver f (tensorPowModule X L (d : ℤ))]
```

**`Stacks.AmpleRelativeFiniteType.isAmple_iff_exists_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean#L224). The attribute's comment: “the equivalence of conditions (1) and (3): ampleness and relative very ampleness of some positive tensor power”.

> **The equivalence of (1) and (3) of [Stacks, Tag 01VT]**: `L` is ample exactly when some
> tensor power `L ^⊗ d` with `d ≥ 1` is very ample relative to `f`.

```lean
theorem isAmple_iff_exists_isRelativelyVeryAmple [IsAffine S] (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] [LocallyOfFiniteType f] [QuasiCompact f] :
    IsAmple X L ↔ ∃ d : ℕ, 1 ≤ d ∧
      Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ))
```

**`Stacks.AmpleRelativeFiniteType.isAmple_iff_eventually_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean#L234). The attribute's comment: “the equivalence of conditions (1) and (4): ampleness and relative very ampleness of every sufficiently high tensor power”. References: EGA II (4.5.10), “more general”.

> **The equivalence of (1) and (4) of [Stacks, Tag 01VT]**: `L` is ample exactly when every
> sufficiently high tensor power of `L` is very ample relative to `f`.

```lean
theorem isAmple_iff_eventually_isRelativelyVeryAmple [IsAffine S] (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] [LocallyOfFiniteType f] [QuasiCompact f] :
    IsAmple X L ↔ ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
      Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ))
```

**`Stacks.AmpleRelativeFiniteType.tfae_six_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleRelativeFiniteType/VeryAmple.lean#L256). The attribute's comment: “all six conditions verbatim and with no named input: ampleness, `f`-ampleness, relative very ampleness of some and of every sufficiently high tensor power, and the two immersion clauses with the source's lower bound `n ≥ 1` on the dimension of the projective space”.

> **[Stacks, Tag 01VT], all six conditions, with the source's own immersion clauses.** The
> immersion clauses (5) and (6) are
> `Stacks.AmpleProjectiveImmersion.HasImmersionTwistOverPos`, which writes `∃ n ≥ 1` as the source
> does, rather than `Stacks.AmpleProjectiveImmersion.HasImmersionTwistOver`'s `∃ n : ℕ`.
>
> The two agree — `Stacks.AmpleProjectiveImmersion.hasImmersionTwistOverPos_iff` — because an
> immersion into `ℙⁿ_S` composed with the linear embedding `ℙⁿ_S ↪ ℙᴺ_S` is an immersion into
> `ℙᴺ_S` carrying the same hyperplane sheaf, so a witness at `n` gives one at `max n 1`. This is
> therefore `Stacks.AmpleRelativeFiniteType.tfae_six` with two clauses rewritten, and the tag's
> six conditions hold verbatim.

```lean
theorem tfae_six_pos [IsAffine S] (f : X ⟶ S) (L : X.Modules) [IsInvertibleModule X L]
    [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE [
      IsAmple X L,
      Stacks.RelativeAmple.IsRelativelyAmple f L,
      ∃ d : ℕ, 1 ≤ d ∧
        Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ)),
      ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
        Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (d : ℤ)),
      ∃ d : ℕ, 1 ≤ d ∧ HasImmersionTwistOverPos f (tensorPowModule X L (d : ℤ)),
      ∃ d₀ : ℕ, 1 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
        HasImmersionTwistOverPos f (tensorPowModule X L (d : ℤ))]
```

## Tag 01VU, a lemma

[Tag 01VU](https://stacks.math.columbia.edu/tag/01VU) in the Stacks Project.

**`Stacks.VeryAmplePowersQuasiCompactBase.existsVeryAmplePower_of_eventuallyVeryAmplePower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean#L92). The attribute's comment: “(3) implies (2)”. References: EGA II (4.5.10), “(ii): e) implies e')”.

> If every sufficiently high tensor power of `L` is very ample relative to `f`, then some
> positive tensor power of `L` is very ample relative to `f`.

```lean
theorem existsVeryAmplePower_of_eventuallyVeryAmplePower (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] (h : EventuallyVeryAmplePower f L) : ExistsVeryAmplePower f L
```

**`Stacks.VeryAmplePowersQuasiCompactBase.isRelativelyAmple_of_existsVeryAmplePower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean#L100). The attribute's comment: “(2) implies (1)”. References: EGA II (4.5.10), “more general”; EGA II (4.6.2), “more general”.

> If some positive tensor power of `L` is very ample relative to a quasi-compact `f`, then `L` is
> ample relative to `f`.

```lean
theorem isRelativelyAmple_of_existsVeryAmplePower (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] (hf : QuasiCompact f) (h : ExistsVeryAmplePower f L) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

**`Stacks.VeryAmplePowersQuasiCompactBase.isRelativelyAmple_of_eventuallyVeryAmplePower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean#L110). The attribute's comment: “(3) implies (1)”. References: EGA II (4.5.10), “(ii): e) implies ample”.

> If every sufficiently high tensor power of `L` is very ample relative to a quasi-compact `f`,
> then `L` is ample relative to `f`.

```lean
theorem isRelativelyAmple_of_eventuallyVeryAmplePower (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] (hf : QuasiCompact f) (h : EventuallyVeryAmplePower f L) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

**`Stacks.VeryAmplePowersQuasiCompactBase.eventuallyVeryAmplePower_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean#L124). The attribute's comment: “(1) implies (3)”. References: EGA II (4.5.10), “(ii): ample implies e)”; EGA II (4.5.11), “The case L' = O\_X”; EGA II (4.6.11), “partial”.

> Let `f : X ⟶ S` be locally of finite type with `S` quasi-compact and let `L` be ample
> relative to `f`. Then `L^{⊗ d}` is very ample relative to `f` for every sufficiently large `d`.

```lean
theorem eventuallyVeryAmplePower_of_isRelativelyAmple (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] [CompactSpace S] [LocallyOfFiniteType f]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    EventuallyVeryAmplePower f L
```

**`Stacks.VeryAmplePowersQuasiCompactBase.tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmplePowersQuasiCompactBase/Basic.lean#L163).

> For `f : X ⟶ S` of finite type with `S` quasi-compact and `L` an invertible `𝒪_X`-module, the
> three conditions
>
> 1. `L` is `f`-relatively ample,
> 2. `L^{⊗ d}` is `f`-relatively very ample for some `d ≥ 1`, and
> 3. `L^{⊗ d}` is `f`-relatively very ample for every sufficiently large `d`
>
> are equivalent.

```lean
theorem tfae (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] [CompactSpace S] [LocallyOfFiniteType f]
    (hf : QuasiCompact f) :
    List.TFAE [Stacks.RelativeAmple.IsRelativelyAmple f L, ExistsVeryAmplePower f L,
      EventuallyVeryAmplePower f L]
```

## Tag 02NQ, a lemma

[Tag 02NQ](https://stacks.math.columbia.edu/tag/02NQ) in the Stacks Project.

**`Stacks.VeryAmpleFiniteTypeCover.hasProjectiveImmersionCover_of_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean#L114). The attribute's comment: “(1) implies (2)”.

> **Stacks Tag 02NQ, (1) implies (2).** Let `f : X ⟶ S` be of finite type and `L` an invertible
> `𝒪_X`-module. If `L` is `f`-relatively very ample then there are an open covering `S = ⋃ V_j`, for
> each `j` an integer `n_j`, and immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying the
> hyperplane sheaf to `L|_{f⁻¹(V_j)}`.
>
> This is the source's own proof: take an affine open covering of `S` and apply Stacks Tag 02NP,
> `Stacks.CoordinateImmersion.hasImmersionTwistOver_of_isRelativelyVeryAmple`, to each of the
> restrictions of `f` and `L`; relative very ampleness of the restrictions is Stacks Tag 01VR's
> (1) implies (2) at the member, `Stacks.Tag01VMVeryAmple.isRelativelyVeryAmple_morphismRestrict`.

```lean
theorem hasProjectiveImmersionCover_of_isRelativelyVeryAmple (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] [LocallyOfFiniteType f] [QuasiCompact f]
    (hL : Tag01VMVeryAmple.IsRelativelyVeryAmple f L) :
    HasProjectiveImmersionCover f L
```

**`Stacks.VeryAmpleFiniteTypeCover.isRelativelyVeryAmple_of_hasProjectiveImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean#L194). The attribute's comment: “(2) implies (1)”.

> **Stacks Tag 02NQ, (2) implies (1).** Let `f : X ⟶ S` be quasi-compact and `L` an invertible
> `𝒪_X`-module. If there are an open covering `S = ⋃ V_j`, for each `j` an integer `n_j`, and
> immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying the hyperplane sheaf to
> `L|_{f⁻¹(V_j)}`, then `L` is `f`-relatively very ample.
>
> The covering is refined to the affine opens of `S` contained in one of its members, which cover `S`
> because the affine opens are a basis (`AlgebraicGeometry.Scheme.isBasis_affineOpens`); over each of
> them the immersion clause is the restriction of the one over the member,
> `Stacks.VeryAmpleFiniteTypeCover.hasImmersionTwistOver_morphismRestrict_of_le`, and the immersions
> over an affine covering give relative very ampleness by
> `Stacks.VeryAmpleGlue.isRelativelyVeryAmple_of_affine_cover_hasImmersionTwistOver`.
>
> Only quasi-compactness of `f` is used, not the whole of the source's finite-type assumption.

```lean
theorem isRelativelyVeryAmple_of_hasProjectiveImmersionCover (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] (hqc : QuasiCompact f) (h : HasProjectiveImmersionCover f L) :
    Tag01VMVeryAmple.IsRelativelyVeryAmple f L
```

**`Stacks.VeryAmpleFiniteTypeCover.isRelativelyVeryAmple_iff_hasProjectiveImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmpleFiniteTypeCover/Equivalence.lean#L221).

> **Stacks Tag 02NQ.** For `f : X ⟶ S` of finite type and `L` an invertible `𝒪_X`-module,
> relative very ampleness of `L` is equivalent to the existence of an open covering `S = ⋃ V_j`, of
> an integer `n_j` for each `j`, and of immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying the
> hyperplane sheaf to `L|_{f⁻¹(V_j)}`.
>
> The two implications are
> `Stacks.VeryAmpleFiniteTypeCover.hasProjectiveImmersionCover_of_isRelativelyVeryAmple` and
> `Stacks.VeryAmpleFiniteTypeCover.isRelativelyVeryAmple_of_hasProjectiveImmersionCover`.

```lean
theorem isRelativelyVeryAmple_iff_hasProjectiveImmersionCover (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] [LocallyOfFiniteType f] [hqc : QuasiCompact f] :
    Tag01VMVeryAmple.IsRelativelyVeryAmple f L ↔ HasProjectiveImmersionCover f L
```

## Tag 02NR, a lemma

[Tag 02NR](https://stacks.math.columbia.edu/tag/02NR) in the Stacks Project.

**`Stacks.AmplePowerImmersionCover.hasPowerProjectiveImmersionCover_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean#L247). The attribute's comment: “(a) implies (b), with no hypothesis”.

> **Stacks Tag 02NR, (a) ⟹ (b).** Let `f : X ⟶ S` be of finite type and `L` an invertible
> `𝒪_X`-module. If `L` is `f`-relatively ample then there are an open covering `S = ⋃ V_j`, for each
> `j` integers `d_j ≥ 1` and `n_j ≥ 0`, and immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying
> the hyperplane sheaf to `L^{⊗ d_j}|_{f⁻¹(V_j)}`.
>
> This is the source's own proof — take an affine open covering of `S` and apply Stacks Tag 01VS to
> each of the restrictions of `f` and `L` — and it needs no hypothesis: Tag 01VS is proved
> unconditionally, and the stronger affine-and-eventual form is
> `exists_affine_cover_eventually_hasImmersionTwistOver_of_isRelativelyAmple`, from which one degree
> is read off at the bound itself. Only local finiteness of type is used;
> quasi-compactness of `f` is already part of relative ampleness.

```lean
theorem hasPowerProjectiveImmersionCover_of_isRelativelyAmple (f : X ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] [LocallyOfFiniteType f]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    HasPowerProjectiveImmersionCover f L
```

**`Stacks.AmplePowerImmersionCover.isRelativelyAmple_of_hasPowerProjectiveImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean#L510). The attribute's comment: “(b) implies (a), with no hypothesis: the source's covering is by arbitrary opens, and the immersion clause at a member is restricted to the affine opens of that member by `hasImmersionTwistOver_morphismRestrict`, projective space over a base being a fibre product over the terminal scheme”.

> **Stacks Tag 02NR, (b) ⟹ (a).** Let `f : X ⟶ S` be quasi-compact and `L` an invertible
> `𝒪_X`-module. If there are an open covering `S = ⋃ V_j`, for each `j` integers `d_j ≥ 1` and
> `n_j ≥ 0`, and immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying the hyperplane sheaf to
> `L^{⊗ d_j}|_{f⁻¹(V_j)}`, then `L` is `f`-relatively ample.
>
> The route is the source's, taken member by member. At a member `V_j` the clause of (b) is the
> immersion `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over `V_j` carrying the hyperplane sheaf to
> `L^{⊗ d_j}|_{f⁻¹(V_j)}`;
> `Stacks.RelativeVeryAmple.pullbackTensorPowModuleIso` rewrites that module as the `d_j`-th power
> of `L|_{f⁻¹(V_j)}`, and
> `Stacks.AmplePowerImmersionCover.isRelativelyAmple_of_hasImmersionTwistOver` turns the clause into
> relative ampleness of `L|_{f⁻¹(V_j)}` over `V_j` — over a base that need not be affine, because
> `Stacks.AmplePowerImmersionCover.hasImmersionTwistOver_morphismRestrict` restricts the immersion
> clause to the affine opens of `V_j`. The members are then glued by
> `Stacks.AmplePowerImmersionCover.isRelativelyAmple_of_forall_isRelativelyAmple_morphismRestrict`,
> which is Stacks Tag 01VJ's (2) ⟹ (1) and is proved above — so the gluing of *very* ampleness,
> Stacks Tag 01VR's (2) ⟹ (1), is **not** needed, and neither is any statement about relative very
> ampleness. Because the degrees `d_j` are consumed one member at a time, no common degree has to
> be produced.
>
> Only quasi-compactness of `f` is used, not the whole of the source's finite-type hypothesis.

```lean
theorem isRelativelyAmple_of_hasPowerProjectiveImmersionCover (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] (hf : QuasiCompact f)
    (h : HasPowerProjectiveImmersionCover f L) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

**`Stacks.AmplePowerImmersionCover.isRelativelyAmple_iff_hasPowerProjectiveImmersionCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePowerImmersionCover/Basic.lean#L538). The attribute's comment: “the equivalence, with no hypothesis”.

> **Stacks Tag 02NR.** For `f : X ⟶ S` of finite type and `L` an invertible `𝒪_X`-module,
> relative ampleness of `L` is equivalent to the existence of an open covering `S = ⋃ V_j`, of
> integers `d_j ≥ 1` and `n_j ≥ 0` for each `j`, and of immersions `f⁻¹(V_j) ⟶ 𝐏^{n_j}_{V_j}` over
> `V_j` carrying the hyperplane sheaf to `L^{⊗ d_j}|_{f⁻¹(V_j)}`.
>
> The two implications are
> `Stacks.AmplePowerImmersionCover.hasPowerProjectiveImmersionCover_of_isRelativelyAmple` and
> `Stacks.AmplePowerImmersionCover.isRelativelyAmple_of_hasPowerProjectiveImmersionCover`; neither
> has a hypothesis, and this is their conjunction.

```lean
theorem isRelativelyAmple_iff_hasPowerProjectiveImmersionCover (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] [LocallyOfFiniteType f] (hf : QuasiCompact f) :
    Stacks.RelativeAmple.IsRelativelyAmple f L ↔ HasPowerProjectiveImmersionCover f L
```

## Tag 0FVC, a lemma

[Tag 0FVC](https://stacks.math.columbia.edu/tag/0FVC) in the Stacks Project.

**`Stacks.VeryAmpleFixedTwist.eventuallyVeryAmpleFixedTwist_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/VeryAmpleFixedTwist/Basic.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/VeryAmpleFixedTwist/Basic.lean#L586). References: EGA II (4.5.10), “(ii): ample implies e)”; EGA II (4.5.11), “more general”; EGA II (4.6.12).

> **Stacks Tag 0FVC.** Let `f : X ⟶ S` be a morphism of schemes and `N`, `L` invertible
> `𝒪_X`-modules. If `S` is quasi-compact, `f` is of finite type and `L` is `f`-relatively ample,
> then `N ⊗ L^{⊗ d}` is `f`-relatively very ample for every sufficiently large `d`.
>
> The proof is the source's. The affine open covering `S.affineCover.finiteSubcover` of `S` is
> finite because `S` is quasi-compact, and
> `Stacks.VeryAmpleFixedTwist.eventually_familyImmersion_tensor` at the restriction of `f`, whose
> ampleness hypothesis is the defining clause of relative ampleness, gives over each member a bound
> past which `N ⊗ L^{⊗ d}` restricted to the member carries a generating family pinning an
> immersion into projective space over the member — the source's reduction to an affine base, Tag
> 02NQ, performed by hand so that the engine runs with absolute ampleness. The largest of the
> finitely many bounds serves every member, and
> `Stacks.VeryAmpleGlue.isRelativelyVeryAmple_of_cover` (Stacks Tag 01VT's (5) ⟹ (3) and Stacks Tag
> 01VR's (2) ⟹ (1) together) turns the families into relative very ampleness over `S`; the
> restriction of `N ⊗ L^{⊗ d}` is matched with the module the families live on by
> `Stacks.VeryAmpleFixedTwist.pullbackTensorTwistIso`. Quasi-compactness of `f` is taken from
> relative ampleness.

```lean
theorem eventuallyVeryAmpleFixedTwist_of_isRelativelyAmple {S : Scheme.{u}}
    (f : X ⟶ S) (N L : X.Modules) [IsInvertibleModule X N] [IsInvertibleModule X L]
    [CompactSpace S] [LocallyOfFiniteType f]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    EventuallyVeryAmpleFixedTwist f N L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.40, Tag 02NO](https://stacks.math.columbia.edu/tag/02NO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
