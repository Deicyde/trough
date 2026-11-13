---
declaration: section
origin: cited
lean: Stacks.Thickenings.nthOrderInfinitesimalNeighbourhood, Stacks.Thickenings.firstOrderInfinitesimalNeighbourhood, Stacks.Thickenings.nthOrderInclusion, Stacks.Thickenings.nthOrderToBase, Stacks.Thickenings.nthOrderInclusion_toBase, Stacks.Thickenings.nthOrderInclusion_isNthOrderThickening, Stacks.Thickenings.nthOrderInclusion_isFirstOrderThickening, Stacks.Thickenings.existsUnique_nthOrderLift
statement: formalized
proof: formalized
---

# 37.5 Infinitesimal neighbourhoods

Section 37.5 of the Stacks Project, [Tag 05YW](https://stacks.math.columbia.edu/tag/05YW). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04EY, a definition

[Tag 04EY](https://stacks.math.columbia.edu/tag/04EY) in the Stacks Project.

**`Stacks.Thickenings.nthOrderInfinitesimalNeighbourhood`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L81). The attribute's comment: “part (2): nth-order infinitesimal neighbourhood”. References: EGA IV (16.1.2), “special case”; EGA IV (19.4.6); SGA 2 XI (3.18), “more general”.

> **Stacks Project, Tag 04EY, part (2).** The `n`th-order infinitesimal neighbourhood of `Z`
> in `X` for an immersion `i : Z ⟶ X`: the closed subscheme of the canonical open neighbourhood
> `AlgebraicGeometry.Scheme.Hom.coborderRange` of the image of `i` cut out by the `(n+1)`st power
> of the defining ideal sheaf of `AlgebraicGeometry.Scheme.Hom.liftCoborder`.

```lean
def nthOrderInfinitesimalNeighbourhood (n : ℕ) : Scheme.{u}
```

**`Stacks.Thickenings.firstOrderInfinitesimalNeighbourhood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L88). The attribute's comment: “part (1): first-order infinitesimal neighbourhood”. References: EGA IV (16.1.2), “Y^\{(1)}, immersions”.

> **Stacks Project, Tag 04EY, part (1).** The first-order infinitesimal neighbourhood of `Z`
> in `X`, cut out by the square of the defining ideal sheaf of the immersion.

```lean
abbrev firstOrderInfinitesimalNeighbourhood : Scheme.{u}
```

**`Stacks.Thickenings.nthOrderInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L111). The attribute's comment: “part (2): inclusion into the nth-order neighbourhood”. References: EGA IV (16.1.2), “Y^\{(n)} inclusion”.

> The inclusion of `Z` into its `n`th-order infinitesimal neighbourhood.

```lean
def nthOrderInclusion (n : ℕ) : Z ⟶ nthOrderInfinitesimalNeighbourhood i n
```

**`Stacks.Thickenings.nthOrderToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L120). The attribute's comment: “part (2): map from the nth-order neighbourhood to the base”.

> The structure morphism from the `n`th-order infinitesimal neighbourhood of `Z` in `X`
> to `X`.

```lean
def nthOrderToBase (n : ℕ) : nthOrderInfinitesimalNeighbourhood i n ⟶ X
```

**`Stacks.Thickenings.nthOrderInclusion_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L141). The attribute's comment: “part (2): factorization over the base”.

> The inclusion of `Z` into its `n`th-order infinitesimal neighbourhood, followed by the
> structure morphism to `X`, is the original immersion.

```lean
theorem nthOrderInclusion_toBase (n : ℕ) :
    nthOrderInclusion i n ≫ nthOrderToBase i n = i
```

**`Stacks.Thickenings.nthOrderInclusion_isNthOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L181). The attribute's comment: “part (2): nth-order thickening”.

> **Stacks Project, Tag 04EY, part (2).** The inclusion of `Z` into its `n`th-order
> infinitesimal neighbourhood is an `n`th-order thickening: it is a closed immersion whose
> defining ideal sheaf has vanishing `(n+1)`st power.
>
> Affine-locally on the open neighbourhood `AlgebraicGeometry.Scheme.Hom.coborderRange`, the
> `(n+1)`st power of the ideal sheaf of `i.liftCoborder` is the kernel of the surjection onto the
> sections of the neighbourhood, so the `(n+1)`st power of its image vanishes.

```lean
theorem nthOrderInclusion_isNthOrderThickening (n : ℕ) :
    IsNthOrderThickening n (nthOrderInclusion i n)
```

**`Stacks.Thickenings.nthOrderInclusion_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L216). The attribute's comment: “part (1): first-order thickening”.

> **Stacks Project, Tag 04EY, part (1).** The inclusion of `Z` into its first-order
> infinitesimal neighbourhood is a first-order thickening.

```lean
theorem nthOrderInclusion_isFirstOrderThickening :
    IsFirstOrderThickening (nthOrderInclusion i 1)
```

## Tag 04EZ, a lemma

[Tag 04EZ](https://stacks.math.columbia.edu/tag/04EZ) in the Stacks Project.

**`Stacks.Thickenings.existsUnique_nthOrderLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L385). The attribute's comment: “part (2): nth-order universal property”.

> **Stacks Project, Tag 04EZ, part (2).** The universal property of the `n`th-order
> infinitesimal neighbourhood: given an `n`th-order thickening `j : T ⟶ T'`, a morphism
> `a : T ⟶ Z` and a morphism `b : T' ⟶ X` making the square commute, there is a unique morphism
> `T' ⟶ Z_n` extending `a` and lying over `b`.
>
> Since `j` is surjective on points, `b` lands in the open subscheme
> `AlgebraicGeometry.Scheme.Hom.coborderRange` and so factors as `f ≫ i.coborderRange.ι`. The
> square then reads `j ≫ f = a ≫ i.liftCoborder`, so
> `Stacks.Thickenings.ker_pow_le_ker_of_comm_square` gives `i.liftCoborder.ker ^ (n + 1) ≤ f.ker`
> and `f` factors through the closed subscheme cut out by `i.liftCoborder.ker ^ (n + 1)`, which is
> `Z_n`. Uniqueness is monomorphicity of the two immersions.
>
> The source's hypothesis `1 ≤ n` is retained for faithfulness but is not needed: the argument is
> uniform in `n`, and at `n = 0` both sides degenerate to `Z` itself.

```lean
theorem existsUnique_nthOrderLift {T T' : Scheme.{u}}
    (n : ℕ) (_hn : 1 ≤ n) (j : T ⟶ T') (hj : IsNthOrderThickening n j)
    (a : T ⟶ Z) (b : T' ⟶ X) (h : j ≫ b = a ≫ i) :
    ∃! a' : T' ⟶ nthOrderInfinitesimalNeighbourhood i n,
      (j ≫ a' = a ≫ nthOrderInclusion i n) ∧ (a' ≫ nthOrderToBase i n = b)
```

**`Stacks.Thickenings.existsUnique_firstOrderLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Infinitesimal.lean#L432). The attribute's comment: “part (1): first-order universal property”.

> **Stacks Project, Tag 04EZ, part (1).** The universal property of the first-order
> infinitesimal neighbourhood, the case `n = 1` of
> `Stacks.Thickenings.existsUnique_nthOrderLift`.

```lean
theorem existsUnique_firstOrderLift {T T' : Scheme.{u}}
    (j : T ⟶ T') (hj : IsFirstOrderThickening j)
    (a : T ⟶ Z) (b : T' ⟶ X) (h : j ≫ b = a ≫ i) :
    ∃! a' : T' ⟶ firstOrderInfinitesimalNeighbourhood i,
      (j ≫ a' = a ≫ nthOrderInclusion i 1) ∧ (a' ≫ nthOrderToBase i 1 = b)
```

## Tag 04F0, a lemma

[Tag 04F0](https://stacks.math.columbia.edu/tag/04F0) in the Stacks Project.

**`Stacks.Thickenings.isIso_conormalTransitivityMap_nthOrderInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/InfinitesimalConormalSheaf.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/InfinitesimalConormalSheaf.lean#L460).

> **Stacks Project, Tag 04F0.** For an immersion `i : Z ⟶ X` with first-order infinitesimal
> neighbourhood `Z ⊂ Z'` of [Stacks Project, Tag 04EY], the canonical map of conormal sheaves
> `𝒞_{Z/X} ⟶ 𝒞_{Z/Z'}` of [Stacks Project, Tag 01R4] is an isomorphism.
>
> The map is `Stacks.ConormalSequenceTwoImmersions.conormalTransitivityMap` for the factorization
> `Z ⟶ Z' ⟶ X` of `i`, which is the map of [Stacks Project, Tag 01R4] for the square with
> horizontal arrows `Z ⟶ Z'` and `Z ⟶ X` and vertical arrows the identity of `Z` and `Z' ⟶ X`.

```lean
theorem isIso_conormalTransitivityMap_nthOrderInclusion :
    IsIso (Stacks.ConormalSequenceTwoImmersions.conormalTransitivityMap
      (nthOrderInclusion i 1) i (nthOrderToBase i 1) (nthOrderInclusion_toBase i 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.5, Tag 05YW](https://stacks.math.columbia.edu/tag/05YW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
