---
declaration: section
origin: cited
lean: Stacks.Blowup.normalizedBlowUpScheme, Stacks.Blowup.normalizedBlowUp, Stacks.Blowup.isNormal_normalizedBlowUpScheme, Stacks.Blowup.isNagataScheme_normalizedBlowUpScheme, Stacks.Blowup.isProper_normalizedBlowUp, AlgebraicGeometry.isNormal_isNagataScheme_and_isProper_normalizedBlowUp, Stacks.ResolutionOfSurfaces.exists_normalizedBlowUpChain_dominating, Stacks.ResolutionOfSurfaces.exists_normalizedBlowUpChain_resolving_partialMap
statement: formalized
proof: formalized
---

# 54.5 Dominating by normalized blowups

Section 54.5 of the Stacks Project, [Tag 0BBR](https://stacks.math.columbia.edu/tag/0BBR). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BBS, a definition

[Tag 0BBS](https://stacks.math.columbia.edu/tag/0BBS) in the Stacks Project.

**`Stacks.Blowup.normalizedBlowUpScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUp.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUp.lean#L184). The attribute's comment: “normalized blowup scheme”.

> **Stacks Project, Tag 0BBS.** The normalized blowup of `X` at a closed point `x`: the
> normalization of the blowup of `X` in the reduced closed subscheme supported at `x`.

```lean
abbrev normalizedBlowUpScheme (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) : Scheme.{u}
```

**`Stacks.Blowup.normalizedBlowUp`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUp.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUp.lean#L193). The attribute's comment: “normalized blowup morphism”.

> **Stacks Project, Tag 0BBS.** The normalized blowup of `X` at a closed point `x`, as a
> morphism to `X`: the normalization of the blowup followed by the blowup morphism.

```lean
abbrev normalizedBlowUp (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) : normalizedBlowUpScheme X hX x hx ⟶ X
```

## Tag 0BFT, a lemma

[Tag 0BFT](https://stacks.math.columbia.edu/tag/0BFT) in the Stacks Project.

**`Stacks.Blowup.isNormal_normalizedBlowUpScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean#L63). The attribute's comment: “normal”.

> **Stacks Project, Tag 0BFT.** The normalized blowup of `X` at a closed point is a normal
> scheme: it is by construction the normalization of the blowup of `X` at that point.

```lean
instance isNormal_normalizedBlowUpScheme {X : Scheme.{u}}
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) :
    IsNormal (normalizedBlowUpScheme X hX x hx)
```

**`Stacks.Blowup.isNagataScheme_normalizedBlowUpScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean#L98). The attribute's comment: “Nagata”.

> **Stacks Project, Tag 0BFT.** The normalized blowup of a Nagata scheme at a closed point is
> Nagata: the blowup is Nagata because it is of finite type over `X`, and the normalization of a
> Nagata scheme is finite, hence again of finite type.

```lean
theorem isNagataScheme_normalizedBlowUpScheme {X : Scheme.{u}}
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) (hNagata : IsNagataScheme X) :
    IsNagataScheme (normalizedBlowUpScheme X hX x hx)
```

**`Stacks.Blowup.isProper_normalizedBlowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/NormalizedBlowUpNagata.lean#L112). The attribute's comment: “proper over the base”.

> **Stacks Project, Tag 0BFT.** The normalized blowup of a Nagata scheme at a closed point is
> proper over it: the blowup is proper because `X` is locally Noetherian, and the normalization of
> the blowup is finite because the blowup is Nagata.

```lean
theorem isProper_normalizedBlowUp {X : Scheme.{u}}
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) (hNagata : IsNagataScheme X) :
    IsProper (normalizedBlowUp X hX x hx)
```

**`AlgebraicGeometry.isNormal_isNagataScheme_and_isProper_normalizedBlowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpSequence.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpSequence.lean#L90).

> **Stacks Project, Tag 0BFT.** The normalized blowup of a Nagata scheme `X` at a closed point
> is a normal, Nagata scheme, and its structure morphism is proper over `X`.

```lean
public theorem isNormal_isNagataScheme_and_isProper_normalizedBlowUp {X : Scheme.{u}}
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) (hx : IsClosed ({x} : Set X)) (hNagata : IsNagataScheme X) :
    IsNormal (Stacks.Blowup.normalizedBlowUpScheme X hX x hx) ∧
      IsNagataScheme (Stacks.Blowup.normalizedBlowUpScheme X hX x hx) ∧
      IsProper (Stacks.Blowup.normalizedBlowUp X hX x hx)
```

## Tag 0BBT, a lemma

[Tag 0BBT](https://stacks.math.columbia.edu/tag/0BBT) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_normalizedBlowUpChain_dominating`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DominateByNormalizedBlowUps/Basic.lean, line 2370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DominateByNormalizedBlowUps/Basic.lean#L2370).

> **Stacks Project, Tag 0BBT.** Let `X` be a Noetherian Nagata scheme of dimension two and let
> `f : Y ⟶ X` be a proper birational morphism. Then there is a scheme `Z` obtained from the
> normalization of `X` by finitely many normalized blowups at closed points which dominates `Y`:
> its structure morphism `g : Z ⟶ X` factors as `h ≫ f` for a morphism `h : Z ⟶ Y`, so the whole
> diagram commutes over `X`.

```lean
theorem exists_normalizedBlowUpChain_dominating
    {X Y : Scheme.{u}} [IsNoetherian X] (hNagata : IsNagataScheme X)
    (hdim : topologicalKrullDim X = 2) (f : Y ⟶ X)
    [IsProper f] (hf : IsBirational f) :
    ∃ (Z : Scheme.{u}) (g : Z ⟶ X) (h : Z ⟶ Y),
      NormalizedBlowUpChain X finite_irreducibleComponents_isCompactOpen_of_isNoetherian Z g ∧
        h ≫ f = g
```

## Tag 0C5I, a lemma

[Tag 0C5I](https://stacks.math.columbia.edu/tag/0C5I) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_normalizedBlowUpChain_resolving_partialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DominateByNormalizedBlowUps/Basic.lean, line 2473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DominateByNormalizedBlowUps/Basic.lean#L2473).

> **Stacks Project, Tag 0C5I.** Let `X` be a Noetherian Nagata scheme of dimension two over
> `S` and let `Y` be proper over `S`. Any `S`-rational map from `X` to `Y` becomes an `S`-morphism
> after passing to the normalization of `X` followed by finitely many normalized blowups at closed
> points, and the resulting morphism agrees with the rational map over its domain.

```lean
theorem exists_normalizedBlowUpChain_resolving_partialMap
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S] [IsNoetherian X] [IsProper (Y ↘ S)]
    (hNagata : IsNagataScheme X) (hdim : topologicalKrullDim X = 2)
    (f : X.PartialMap Y) [f.IsOver S] :
    ∃ (Z : Scheme.{u}) (g : Z ⟶ X) (h : Z ⟶ Y),
      NormalizedBlowUpChain X finite_irreducibleComponents_isCompactOpen_of_isNoetherian Z g ∧
        h ≫ (Y ↘ S) = g ≫ (X ↘ S) ∧
          Limits.pullback.fst g f.domain.ι ≫ h =
            Limits.pullback.snd g f.domain.ι ≫ f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.5, Tag 0BBR](https://stacks.math.columbia.edu/tag/0BBR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
