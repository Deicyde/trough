---
declaration: section
origin: cited
lean: SSet.trivialKanFibrations, SSet.trivialKanFibrations_eq_rlp_monomorphisms, SSet.trivialKanFibrations_isStableUnderBaseChange, SSet.trivialKanFibrations_comp, SSet.trivialKanFibrations_limit_π_zero, SSet.isStableUnderProductsOfShape_trivialKanFibrations, SSet.isStableUnderFilteredColimits_trivialKanFibrations, SSet.trivialKanFibrations_isHomotopyEquiv
statement: formalized
proof: formalized
---

# 14.30 Trivial Kan fibrations

Section 14.30 of the Stacks Project, [Tag 08NK](https://stacks.math.columbia.edu/tag/08NK). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08NL, a definition

[Tag 08NL](https://stacks.math.columbia.edu/tag/08NL) in the Stacks Project.

**`SSet.trivialKanFibrations`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L77). The attribute's comment: “the two clauses `X₀ → Y₀` surjective and lifting for `n ≥ 1` are the single right lifting property against all boundary inclusions, the case `n = 0` being the surjectivity since `∂Δ[0] = ⊥`”.

> **Stacks 08NL**.
> The class of *trivial Kan fibrations*: the morphisms `f : X ⟶ Y` of simplicial sets having the
> right lifting property with respect to every boundary inclusion `∂Δ[n].ι : ∂Δ[n] ⟶ Δ[n]`, that
> is, such that `X₀ → Y₀` is surjective and, for `n ≥ 1`, every commutative square with
> `∂Δ[n] ⟶ X` on top and `Δ[n] ⟶ Y` at the bottom has a diagonal filler `Δ[n] ⟶ X`.

```lean
public def trivialKanFibrations : MorphismProperty SSet.{u}
```

## Tag 08NM, a lemma

[Tag 08NM](https://stacks.math.columbia.edu/tag/08NM) in the Stacks Project.

**`SSet.trivialKanFibrations_eq_rlp_monomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L246). The attribute's comment: “stated as the equality of morphism properties; the source's containment `≤` is the content, the reverse being `antitone_rlp` on `I_le_monomorphisms`, and "`Z → W` termwise injective" is `monomorphisms SSet`”.

> **A trivial Kan fibration lifts against any degreewise injective map.** For a trivial Kan
> fibration `f : X ⟶ Y` of simplicial sets, every solid commutative square
>
> ```
> Z --b--> X
> |        |
> v        v
> W --a--> Y
> ```
>
> with `Z ⟶ W` a monomorphism, i.e. injective in every degree, admits a diagonal `W ⟶ X`
> making both triangles commute; conversely such a morphism `f` is a trivial Kan fibration,
> the boundary inclusions being monomorphisms. Equivalently, the trivial Kan fibrations are
> precisely the right lifting class of the monomorphisms of simplicial sets.

```lean
public theorem trivialKanFibrations_eq_rlp_monomorphisms :
    trivialKanFibrations.{u} = (monomorphisms SSet.{u}).rlp
```

## Tag 08NN, a lemma

[Tag 08NN](https://stacks.math.columbia.edu/tag/08NN) in the Stacks Project.

**`SSet.trivialKanFibrations_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L85).

> **Stacks 08NN**.
> Trivial Kan fibrations are stable under arbitrary base change. This is the general base-change
> closure of a right lifting class, applied to the boundary-inclusion definition above.

```lean
public instance trivialKanFibrations_isStableUnderBaseChange :
    trivialKanFibrations.{u}.IsStableUnderBaseChange
```

## Tag 08NP, a lemma

[Tag 08NP](https://stacks.math.columbia.edu/tag/08NP) in the Stacks Project.

**`SSet.trivialKanFibrations_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L481).

> **Stacks 08NP**.
> The composition of two trivial Kan fibrations is a trivial Kan fibration.

```lean
public theorem trivialKanFibrations_comp {X Y Z : SSet.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : trivialKanFibrations f) (hg : trivialKanFibrations g) :
    trivialKanFibrations (f ≫ g)
```

## Tag 08NQ, a lemma

[Tag 08NQ](https://stacks.math.columbia.edu/tag/08NQ) in the Stacks Project.

**`SSet.trivialKanFibrations_limit_π_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L491).

> **Stacks 08NQ**.
> Let `⋯ → U² → U¹ → U⁰` be a tower of simplicial sets, encoded as a functor `F : ℕᵒᵖ ⥤ SSet`, and
> let `U = limₜ Uᵗ` be its levelwise inverse limit. If every transition map `Uᵗ⁺¹ ⟶ Uᵗ` is a trivial
> Kan fibration, then the projection `π⁰ : U ⟶ U⁰` is a trivial Kan fibration.

```lean
public theorem trivialKanFibrations_limit_π_zero (F : ℕᵒᵖ ⥤ SSet.{u})
    (h : ∀ t : ℕ, trivialKanFibrations (F.map (homOfLE (Nat.le_succ t)).op)) :
    trivialKanFibrations (limit.π F (Opposite.op 0))
```

## Tag 08NR, a lemma

[Tag 08NR](https://stacks.math.columbia.edu/tag/08NR) in the Stacks Project.

**`SSet.isStableUnderProductsOfShape_trivialKanFibrations`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L258). The attribute's comment: “stability under products is stated for arbitrary product cones, as `IsStableUnderProductsOfShape` for the class of Tag 08NL; the source's `∏ X_i → ∏ Y_i` is the case of `Limits.Pi.map`, and the index type is in an arbitrary universe where the source says "a set"”.

> **A product of trivial Kan fibrations is a trivial Kan fibration.** If `f i : X i ⟶ Y i` is
> a family of trivial Kan fibrations of simplicial sets, that is, of morphisms having the right
> lifting property with respect to every boundary inclusion `∂Δ[n].ι`, then so is the induced
> morphism `∏ X i ⟶ ∏ Y i` between any products of the `X i` and of the `Y i`.

```lean
public instance isStableUnderProductsOfShape_trivialKanFibrations (J : Type w) :
    trivialKanFibrations.{u}.IsStableUnderProductsOfShape J
```

## Tag 08Q5, a lemma

[Tag 08Q5](https://stacks.math.columbia.edu/tag/08Q5) in the Stacks Project.

**`SSet.isStableUnderFilteredColimits_trivialKanFibrations`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L382). The attribute's comment: “stability under filtered colimits is stated for arbitrary colimit cocones over an arbitrary filtered index category, as `IsStableUnderFilteredColimits` for the class of Tag 08NL; the source's `colim X₁ → colim X₂` is the case of `colimMap`, and the index category is in arbitrary universes, the hypothesis `HasColimitsOfSize` being what makes the colimits degreewise as in the source's hint”.

> **A filtered colimit of trivial Kan fibrations is a trivial Kan fibration.** If `J` is a
> filtered category and `f : X₁ ⟶ X₂` is a morphism of diagrams `J ⥤ SSet` whose components
> `f.app j` are all trivial Kan fibrations, that is, all have the right lifting property with
> respect to every boundary inclusion `∂Δ[n].ι`, then so is the induced morphism
> `colim X₁ ⟶ colim X₂` between any colimits of `X₁` and of `X₂`.

```lean
public instance isStableUnderFilteredColimits_trivialKanFibrations
    [HasColimitsOfSize.{w, w'} (Type u)] :
    MorphismProperty.IsStableUnderFilteredColimits.{w, w'} trivialKanFibrations.{u}
```

## Tag 08NS, a lemma

[Tag 08NS](https://stacks.math.columbia.edu/tag/08NS) in the Stacks Project.

**`SSet.trivialKanFibrations_isHomotopyEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration.lean#L691).

> **Stacks 08NS**.
> A trivial Kan fibration `f : X ⟶ Y` of simplicial sets — one with the right lifting property
> against every boundary inclusion `∂Δ[n] ↪ Δ[n]` — is a homotopy equivalence: there is a
> `g : Y ⟶ X` with `f ≫ g` homotopic to `𝟙 X` and `g ≫ f` homotopic to `𝟙 Y`.

```lean
theorem trivialKanFibrations_isHomotopyEquiv
    {X Y : SSet.{u}} (f : X ⟶ Y) (hf : trivialKanFibrations f) :
    ∃ g : Y ⟶ X,
      Nonempty (Homotopy (f ≫ g) (𝟙 X)) ∧
      Nonempty (Homotopy (g ≫ f) (𝟙 Y))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.30, Tag 08NK](https://stacks.math.columbia.edu/tag/08NK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
