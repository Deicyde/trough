---
declaration: section
origin: cited
lean: Stacks.Intersection.properPushforward_coherentSheafCycle, Stacks.Intersection.properPushforward_closedSubschemeCycle, Stacks.Chow.properPushforward_comp
statement: formalized
proof: formalized
---

# 43.6 Proper pushforward

Section 43.6 of the Stacks Project, [Tag 0AZC](https://stacks.math.columbia.edu/tag/0AZC). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AZD, a lemma

[Tag 0AZD](https://stacks.math.columbia.edu/tag/0AZD) in the Stacks Project.

**`Stacks.Intersection.properPushforward_coherentSheafCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperPushforward/CoherentSheaf.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperPushforward/CoherentSheaf.lean#L78). The attribute's comment: “cycle identity for a coherent sheaf”.

> **Stacks 0AZD.** Let `f : X ⟶ Y` be a proper morphism of varieties over a field `k` and let
> `F` be a coherent `𝒪_X`-module whose support has dimension at most `n`. Then proper pushforward
> of `n`-cycles carries the cycle of `F` to the cycle of its direct image: `f_* [F]_n = [f_* F]_n`.
>
> This is Stacks 02R6 at the Chow situation `Stacks.Chow.fieldChowSituation k`, whose base is
> `Spec k` and whose dimension function vanishes; over that base the delta-dimension of the
> support of `F` is its dimension.

```lean
theorem properPushforward_coherentSheafCycle (k : Type u) [Field k]
    (sX : X ⟶ (fieldChowSituation k).S) [IsVariety k sX]
    (sY : Y ⟶ (fieldChowSituation k).S) [IsVariety k sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (F : X.Modules) [F.IsCoherent] (n : ℤ)
    (hFn : schemeDeltaDimension (fieldChowSituation k)
      ((reducedSupport F).subschemeι ≫ sX) ≤ (n : EInt)) :
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI := ProperCoherenceWitness.isCoherent_pushforward f F
    properPushforward (fieldChowSituation k) sX sY f hf n
        (cycleAssociatedToCoherentSheaf (fieldChowSituation k) sX F n hFn) =
      cycleAssociatedToCoherentSheaf (fieldChowSituation k) sY
        ((Scheme.Modules.pushforward f).obj F) n
        (schemeDeltaDimension_reducedSupport_pushforward_le
          (fieldChowSituation k) sX sY f hf F hFn)
```

**`Stacks.Intersection.properPushforward_closedSubschemeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperPushforward/CoherentSheaf.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperPushforward/CoherentSheaf.lean#L106). The attribute's comment: “closed subscheme”.

> **Stacks 0AZD.** Let `f : X ⟶ Y` be a proper morphism of varieties over a field `k` and let
> `i : Z ⟶ X` be a closed subscheme of dimension at most `n`. Then proper pushforward of
> `n`-cycles carries the cycle of `Z` to the cycle of the direct image of its structure sheaf:
> `f_* [Z]_n = [f_* 𝒪_Z]_n`.
>
> Here `𝒪_Z` is read as the coherent `𝒪_X`-module `i_* 𝒪_Z`, and `f_* 𝒪_Z` as the direct image of
> that module along `f`. This is Stacks 02R6, part (1), at the Chow situation
> `Stacks.Chow.fieldChowSituation k`.

```lean
theorem properPushforward_closedSubschemeCycle (k : Type u) [Field k] {Z : Scheme.{u}}
    (sX : X ⟶ (fieldChowSituation k).S) [IsVariety k sX]
    (sY : Y ⟶ (fieldChowSituation k).S) [IsVariety k sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (i : Z ⟶ X) [IsClosedImmersion i] (n : ℤ)
    (hZ : schemeDeltaDimension (fieldChowSituation k) (i ≫ sX) ≤ (n : EInt)) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI := ProperCoherenceWitness.isCoherent_pushforward f
      ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
    properPushforward (fieldChowSituation k) sX sY f hf n
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX i n) =
      cycleAssociatedToCoherentSheaf (fieldChowSituation k) sY
        ((Scheme.Modules.pushforward f).obj
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))) n
        (schemeDeltaDimension_reducedSupport_pushforward_le (fieldChowSituation k) sX sY f hf
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
          (schemeDeltaDimension_reducedSupport_pushforwardStructureSheaf_le
            (fieldChowSituation k) sX i hZ))
```

## Tag 0B0N, a lemma

[Tag 0B0N](https://stacks.math.columbia.edu/tag/0B0N) in the Stacks Project.

**`Stacks.Chow.properPushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/Functoriality.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/Functoriality.lean#L268). The attribute's comment: “functoriality of proper pushforward of cycles, in the case of varieties”.

> **Stacks 02R5.** Proper pushforward of `k`-cycles is functorial: pushing forward along
> `f : X ⟶ Y` and then along `g : Y ⟶ Z` is pushing forward along the composite.

```lean
theorem properPushforward_comp (C : ChowSituation.{u}) {X Y Z : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (sZ : Z ⟶ C.S)
    [LocallyOfFiniteType sZ] (f : X ⟶ Y) [IsProper f] (g : Y ⟶ Z) [IsProper g]
    (hf : f ≫ sY = sX) (hg : g ≫ sZ = sY) (k : ℤ) :
    properPushforward C sY sZ g hg k ∘ properPushforward C sX sY f hf k =
      properPushforward C sX sZ (f ≫ g) (by rw [Category.assoc, hg, hf]) k
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.6, Tag 0AZC](https://stacks.math.columbia.edu/tag/0AZC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
