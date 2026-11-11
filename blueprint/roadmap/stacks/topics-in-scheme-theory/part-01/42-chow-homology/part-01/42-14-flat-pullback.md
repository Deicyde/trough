---
declaration: section
origin: cited
lean: Stacks.Chow.flatPullback_cycleAssociatedToClosedSubscheme, Stacks.Chow.flatPullback, Stacks.Chow.cycleGroupRestrict_surjective, Stacks.Chow.cycleGroupRestrict_eq_zero_iff, Stacks.Chow.flatPullback_comp, AlgebraicGeometry.Flat.comp, AlgebraicGeometry.RelativeDimension.comp_of_flat, Stacks.Chow.flatPullback_cycleAssociatedToClosedSubscheme_of_le
statement: formalized
proof: formalized
---

# 42.14 Flat pullback

Section 42.14 of the Stacks Project, [Tag 02RA](https://stacks.math.columbia.edu/tag/02RA). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02RB, a definition

[Tag 02RB](https://stacks.math.columbia.edu/tag/02RB) in the Stacks Project.

**`Stacks.Chow.flatPullback_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Cycles.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Cycles.lean#L41). The attribute's comment: “pullback of an integral closed subscheme”.

> The flat pullback of the cycle of an integral closed subscheme
> `i : Z ⟶ X` of delta-dimension `k` is the cycle of delta-dimension `k + r` of its
> scheme-theoretic inverse image `X' ×_X Z`.

```lean
theorem flatPullback_cycleAssociatedToClosedSubscheme (C : ChowSituation.{u})
    {X' X Z : Scheme.{u}} (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX']
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (f : X' ⟶ X) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sX = sX') (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) (k : ℤ)
    (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z]
    (hZ : schemeDeltaDimension C (i ≫ sX) = (k : EInt)) :
    flatPullback C sX' sX f hbase r hf k (cycleAssociatedToClosedSubscheme C sX i k) =
      cycleAssociatedToClosedSubscheme C sX' (pullback.fst f i) (k + (r : ℤ))
```

**`Stacks.Chow.flatPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullback.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullback.lean#L263). The attribute's comment: “flat pullback homomorphism”.

> **Stacks 02RB.** Flat pullback of cycles along a flat morphism of relative dimension `r`, as
> a homomorphism `Z_k(X) ⟶ Z_{k+r}(X')`.

```lean
def flatPullback (C : ChowSituation.{u}) {X' X : Scheme.{u}} (sX' : X' ⟶ C.S)
    [LocallyOfFiniteType sX'] (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (f : X' ⟶ X)
    [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sX = sX') (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (k : ℤ) :
    CycleGroup C sX k →+ CycleGroup C sX' (k + (r : ℤ))
```

## Tag 02RC, a lemma

[Tag 02RC](https://stacks.math.columbia.edu/tag/02RC) in the Stacks Project.

**`Stacks.Chow.cycleGroupRestrict_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocalizationSequence.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocalizationSequence.lean#L266). The attribute's comment: “surjectivity onto the open complement”.

> Restriction of cycles along an open immersion is surjective.

```lean
theorem cycleGroupRestrict_surjective (C : ChowSituation.{u}) {X U : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sU : U ⟶ C.S) [LocallyOfFiniteType sU]
    (j : U ⟶ X) [IsOpenImmersion j] (hj : j ≫ sX = sU) (k : ℤ) :
    Function.Surjective (cycleGroupRestrict C sX sU j hj k)
```

**`Stacks.Chow.cycleGroupRestrict_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocalizationSequence.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocalizationSequence.lean#L317). The attribute's comment: “kernel of restriction”.

> A cycle restricts to zero on the open complement exactly when it is the proper pushforward of
> a cycle on the closed complement.

```lean
theorem cycleGroupRestrict_eq_zero_iff (C : ChowSituation.{u}) {X Y U : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sU : U ⟶ C.S) [LocallyOfFiniteType sU] (i : Y ⟶ X) [IsClosedImmersion i]
    (hi : i ≫ sX = sY) (j : U ⟶ X) [IsOpenImmersion j] (hj : j ≫ sX = sU)
    (hcomplement : Set.range i.base = (Set.range j.base)ᶜ) (k : ℤ) (c : CycleGroup C sX k) :
    cycleGroupRestrict C sX sU j hj k c = 0 ↔
      ∃ d : CycleGroup C sY k, properPushforward C sY sX i hi k d = c
```

## Tag 02RD, a lemma

[Tag 02RD](https://stacks.math.columbia.edu/tag/02RD) in the Stacks Project.

**`Stacks.Chow.flatPullback_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean#L225). The attribute's comment: “composition of flat pullbacks”.

> **Stacks 02RD.** For flat morphisms `f : X ⟶ Y` and `g : Y ⟶ Z` of relative dimensions `r`
> and `s`, flat pullback of cycles satisfies `f^* ∘ g^* = (g ∘ f)^*` as maps
> `Z_k(Z) ⟶ Z_{k+r+s}(X)`.
>
> That `f ≫ g` is flat is `AlgebraicGeometry.Flat.comp` and that it has relative dimension
> `r + s` is Stacks 02NL, `AlgebraicGeometry.RelativeDimension.comp_of_flat`; both are recorded
> against this tag in this file.

```lean
theorem flatPullback_comp (C : ChowSituation.{u}) {X Y Z : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (g : Y ⟶ Z) [LocallyOfFiniteType g] [Flat g] (hfbase : f ≫ sY = sX) (hgbase : g ≫ sZ = sY)
    (r s : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (hg : AlgebraicGeometry.RelativeDimension g s) (k : ℤ)
    (hcast : k + (s : ℤ) + (r : ℤ) = k + ((r + s : ℕ) : ℤ)) (c : CycleGroup C sZ k) :
    (hcast ▸ flatPullback C sX sY f hfbase r hf (k + (s : ℤ))
          (flatPullback C sY sZ g hgbase s hg k c) :
        CycleGroup C sX (k + ((r + s : ℕ) : ℤ))) =
      flatPullback C sX sZ (f ≫ g) (by rw [Category.assoc, hgbase, hfbase]) (r + s)
        (AlgebraicGeometry.RelativeDimension.comp_of_flat f g hf hg) k c
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Flat.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean#L181) (StacksFrontier): “flatness of the composite”. References: EGA 0 (6.7.5), “Schemes (EGA preschemes)”; EGA IV (2.1.5), “global case Y' = Y”; EGA IV (2.1.6); EGA IV (2.2.11), “(iii), special case”; EGA IV (2.2.13), “(iii)”; EGA IV (6.6.1), “(i): flatness of h = g∘f”; EGA IV (7.3.5), “partial”; SGA 3 VIIB (1.3.3), “(i), special case”.
- [`AlgebraicGeometry.RelativeDimension.comp_of_flat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Composition.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/Composition.lean#L190) (StacksFrontier): “relative dimension of the composite”.

## Tag 02RE, a lemma

[Tag 02RE](https://stacks.math.columbia.edu/tag/02RE) in the Stacks Project.

**`Stacks.Chow.flatPullback_cycleAssociatedToClosedSubscheme_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean#L490). The attribute's comment: “part (1): cycle identity”.

> **Stacks 02RE, part (1), cycle identity.** For `q : X' ⟶ X` flat of relative dimension `r`
> between schemes locally of finite type over the base of chapter 42, and `i : Z ⟶ X` a closed
> subscheme of delta-dimension at most `k`, the flat pullback of the cycle `[Z]_k` is the cycle
> `[q^{-1}(Z)]_{k+r}` of the scheme-theoretic inverse image, here presented as `pullback.fst q i`:
>
> `q^*[Z]_k = [X' ×_X Z]_{k+r}`.
>
> No irreducibility is assumed of `Z` and only an inequality on its delta-dimension is required,
> so this is the full generality of the source; the integral case is
> `Stacks.Chow.flatPullback_cycleAssociatedToClosedSubscheme`, which carries `@[stacks 02RB]`.
> The companion dimension bound `dim_δ(q^{-1}(Z)) ≤ k + r`, in the same presentation of the
> inverse image, is `Stacks.Chow.schemeDeltaDimension_pullback_le`.
>
> The source deduces part (1) from part (2), and so does this proof: `[Z]_k` is the cycle of the
> coherent sheaf `i_* 𝒪_Z` by Stacks 02QY, flat pullback commutes with passing to the cycle of a
> coherent sheaf by Stacks 02RE part (2),
> `Stacks.Chow.flatPullback_cycleAssociatedToCoherentSheaf`, and the inverse image of `i_* 𝒪_Z`
> along `q` is the direct image of the structure sheaf of `X' ×_X Z` — the identity
> `q^* 𝒪_Z = 𝒪_{q^{-1}(Z)}` of the source — because a closed immersion is affine and so its
> direct image commutes with the flat base change.

```lean
theorem flatPullback_cycleAssociatedToClosedSubscheme_of_le (C : ChowSituation.{u})
    {X' X Z : Scheme.{u}} (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX']
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (q : X' ⟶ X) [LocallyOfFiniteType q] [Flat q]
    (hbase : q ≫ sX = sX') (r : ℕ) (hq : AlgebraicGeometry.RelativeDimension q r)
    (i : Z ⟶ X) [IsClosedImmersion i] (k : ℤ)
    (hZ : schemeDeltaDimension C (i ≫ sX) ≤ (k : EInt)) :
    flatPullback C sX' sX q hbase r hq k (cycleAssociatedToClosedSubscheme C sX i k) =
      cycleAssociatedToClosedSubscheme C sX' (pullback.fst q i) (k + (r : ℤ))
```

**`Stacks.Chow.flatPullback_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/CoherentSheafCycle.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/CoherentSheafCycle.lean#L161). The attribute's comment: “part (2): cycle identity”.

> For `f : X ⟶ Y` flat of relative dimension `r` between schemes locally of finite type over
> the base of chapter 42, and `F` a coherent sheaf on `Y` whose support has delta-dimension at most
> `k`, the flat pullback of the cycle of `F` is the cycle of the pullback of `F`:
>
> `f^*[F]_k = [f^*F]_{k+r}`.

```lean
theorem flatPullback_cycleAssociatedToCoherentSheaf (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sY = sX) (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (F : Y.Modules) [hF : F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sY) ≤ (k : EInt)) :
    flatPullback C sX sY f hbase r hf k (cycleAssociatedToCoherentSheaf C sY F k hFk) =
      @cycleAssociatedToCoherentSheaf X C sX inferInstance
        ((Scheme.Modules.pullback f).obj F)
        (@AlgebraicGeometry.isCoherent_pullback X Y
          (LocallyOfFiniteType.isLocallyNoetherian sX) f F hF)
        (k + (r : ℤ))
        (schemeDeltaDimension_support_pullback_le C sX sY f hbase r hf F k hFk)
```

**`Stacks.Chow.flatPullback_closedSubscheme_cycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageCycle.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageCycle.lean#L65). The attribute's comment: “part (1)”.

> **Stacks 02RE, part (1).** Let `f : X ⟶ Y` be flat of relative dimension `r` between schemes
> locally of finite type over the base of chapter 42, and let `i : Z ⟶ Y` be a closed subscheme
> with `dim_δ(Z) ≤ k`. Then the inverse image `f⁻¹ Z = X ×_Y Z` satisfies
> `dim_δ(f⁻¹ Z) ≤ k + r`, and `[f⁻¹ Z]_{k+r} = f^*[Z]_k` in `Z_{k+r}(X)`.

```lean
theorem flatPullback_closedSubscheme_cycle (C : ChowSituation.{u}) {X Y Z : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sY = sX) (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (i : Z ⟶ Y) [IsClosedImmersion i] (k : ℤ)
    (hZ : schemeDeltaDimension C (i ≫ sY) ≤ (k : EInt)) :
    schemeDeltaDimension C (pullback.fst f i ≫ sX) ≤ ((k + (r : ℤ) : ℤ) : EInt) ∧
      cycleAssociatedToClosedSubscheme C sX (pullback.fst f i) (k + (r : ℤ)) =
        flatPullback C sX sY f hbase r hf k (cycleAssociatedToClosedSubscheme C sY i k)
```

**`Stacks.Chow.flatPullback_coherentSheaf_cycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageCycle.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageCycle.lean#L81). The attribute's comment: “part (2)”.

> **Stacks 02RE, part (2).** Let `f : X ⟶ Y` be flat of relative dimension `r` between schemes
> locally of finite type over the base of chapter 42, and let `F` be a coherent sheaf on `Y` with
> `dim_δ(Supp F) ≤ k`. Then `f^*F` is coherent, `dim_δ(Supp f^*F) ≤ k + r`, and
> `f^*[F]_k = [f^*F]_{k+r}` in `Z_{k+r}(X)`.

```lean
theorem flatPullback_coherentSheaf_cycle (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sY = sX) (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (F : Y.Modules) [hF : F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sY) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : ((Scheme.Modules.pullback f).obj F).IsCoherent :=
      AlgebraicGeometry.isCoherent_pullback f F
    ∃ hFk' : schemeDeltaDimension C
        ((reducedSupport ((Scheme.Modules.pullback f).obj F)).subschemeι ≫ sX) ≤
          ((k + (r : ℤ) : ℤ) : EInt),
      flatPullback C sX sY f hbase r hf k (cycleAssociatedToCoherentSheaf C sY F k hFk) =
        cycleAssociatedToCoherentSheaf C sX ((Scheme.Modules.pullback f).obj F)
          (k + (r : ℤ)) hFk'
```

**`Stacks.Chow.schemeDeltaDimension_pullback_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean#L336). The attribute's comment: “part (1): dimension bound”.

> **Stacks 02RE, part (1), dimension bound.** The scheme-theoretic inverse image of a closed
> subscheme of delta-dimension at most `k` under a flat morphism of relative dimension `r` has
> delta-dimension at most `k + r`.

```lean
theorem schemeDeltaDimension_pullback_le
    (C : ChowSituation.{u}) {X Y Z : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sY = sX) (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (i : Z ⟶ Y) [IsClosedImmersion i] (k : ℤ)
    (hZ : schemeDeltaDimension C (i ≫ sY) ≤ (k : EInt)) :
    schemeDeltaDimension C (pullback.fst f i ≫ sX) ≤ ((k + (r : ℤ) : ℤ) : EInt)
```

**`Stacks.Chow.schemeDeltaDimension_support_pullback_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean#L398). The attribute's comment: “part (2): support dimension bound”.

> **Stacks 02RE, part (2), dimension bound.** If a coherent sheaf on `Y` has support of
> delta-dimension at most `k`, then the support of its pullback along a flat morphism of relative
> dimension `r` has delta-dimension at most `k + r`.

```lean
theorem schemeDeltaDimension_support_pullback_le
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sY = sX) (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (F : Y.Modules) [hF : F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sY) ≤ (k : EInt)) :
    schemeDeltaDimension C
        ((@reducedSupport X ((Scheme.Modules.pullback f).obj F)
          (@AlgebraicGeometry.isCoherent_pullback X Y
            (LocallyOfFiniteType.isLocallyNoetherian sX) f F hF)).subschemeι ≫ sX) ≤
      ((k + (r : ℤ) : ℤ) : EInt)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isCoherent_pullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPullback/Basic.lean#L48), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDeltaDimension.lean#L330) (StacksFrontier): “part (2): pullback coherence”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.14, Tag 02RA](https://stacks.math.columbia.edu/tag/02RA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
