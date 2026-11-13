---
declaration: section
origin: cited
lean: Stacks.Chow.flatPullback_cycleAssociatedToCoherentSheaf_of_isVariety, Stacks.Chow.flat_comp_and_flatPullback_comp_of_isVariety
statement: formalized
proof: formalized
---

# 43.7 Flat pullback

Section 43.7 of the Stacks Project, [Tag 0AZE](https://stacks.math.columbia.edu/tag/0AZE). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AZF, a lemma

[Tag 0AZF](https://stacks.math.columbia.edu/tag/0AZF) in the Stacks Project.

**`Stacks.Chow.flatPullback_cycleAssociatedToCoherentSheaf_of_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/FlatPullbackVariety.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/FlatPullbackVariety.lean#L310).

> **Stacks 0AZF.** Let `f : X ⟶ Y` be a flat morphism of varieties over a field `k` and set
> `r = dim X - dim Y`. If `F` is a coherent sheaf on `Y` whose support has dimension at most `k`,
> then
>
> `f^*[F]_k = [f^*F]_{k+r}`.
>
> The dimension of the support is read as the delta-dimension of the base situation `Spec k`, which
> over a field is the dimension; see
> `Stacks.Chow.flatPullback_cycleAssociatedToCoherentSheaf_of_isVariety'` for the topological
> form.

```lean
theorem flatPullback_cycleAssociatedToCoherentSheaf_of_isVariety (k : Type u) [Field k]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k))
    [IsVariety k sX] [IsVariety k sY] (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX) (r : ℕ)
    (hr : topologicalKrullDim X = topologicalKrullDim Y + (r : WithBot ℕ∞))
    (F : Y.Modules) [hF : F.IsCoherent] (j : ℤ)
    (hFj : schemeDeltaDimension (fieldChowSituation k)
      ((reducedSupport F).subschemeι ≫ sY) ≤ (j : EInt)) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp k sX sY f hbase
    flatPullback (fieldChowSituation k) sX sY f hbase r
        (relativeDimension_of_flat_of_isVariety k sX sY f hbase r hr) j
        (cycleAssociatedToCoherentSheaf (fieldChowSituation k) sY F j hFj) =
      @cycleAssociatedToCoherentSheaf X (fieldChowSituation k) sX inferInstance
        ((Scheme.Modules.pullback f).obj F)
        (@AlgebraicGeometry.isCoherent_pullback X Y
          (LocallyOfFiniteType.isLocallyNoetherian sX) f F hF)
        (j + (r : ℤ))
        (schemeDeltaDimension_support_pullback_le (fieldChowSituation k) sX sY f hbase r
          (relativeDimension_of_flat_of_isVariety k sX sY f hbase r hr) F j hFj)
```

## Tag 0B0P, a lemma

[Tag 0B0P](https://stacks.math.columbia.edu/tag/0B0P) in the Stacks Project.

**`Stacks.Chow.flat_comp_and_flatPullback_comp_of_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/FlatPullbackVariety.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/FlatPullbackVariety.lean#L446). The attribute's comment: “the whole lemma: both that the composite of two flat morphisms of varieties over a field is flat and the identity `f^* ∘ g^* = (g ∘ f)^*` of flat pullbacks of cycles, as maps `Z_j(Z) ⟶ Z_{j + dim X - dim Z}(X)`, under the source's own hypotheses that `f : X ⟶ Y` and `g : Y ⟶ Z` are flat morphisms of varieties over `k`. Flat pullback is the homomorphism `Stacks.Chow.flatPullback` of Tag 02RB in the base situation `Spec k` with the zero dimension function, where the delta-dimension of an integral closed subscheme is its dimension, so the cycle groups are the source's `Z_j`. `WithBot ℕ∞` has no subtraction, so the relative dimensions `r = dim X - dim Y` and `s = dim Y - dim Z` are natural numbers together with the relations `dim X = dim Y + r` and `dim Y = dim Z + s`, and the source's degree shift `dim X - dim Z` is `r + s`; `hcast` is the equality in `ℤ` of the degree `(j + s) + r` reached by pulling back along `g` and then `f` with the degree `j + (r + s)` of the right-hand side, along which the left-hand side is transported. That the relative dimension of the composite is `r + s` is `AlgebraicGeometry.relativeDimension_comp_of_flat_of_isVariety`, the fibre-dimension formula of Tag 02JS which the section's introduction invokes, and the coefficientwise form of the identity is `Stacks.Chow.flatPullback_comp_apply_of_isVariety`.”.

> **Stacks Project, Tag 0B0P.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be flat morphisms of varieties
> over a field `k`. Then `g ∘ f` is flat and
>
> `f^* ∘ g^* = (g ∘ f)^*`   as maps `Z_j(Z) ⟶ Z_{j + dim X - dim Z}(X)`.
>
> `WithBot ℕ∞` has no subtraction, so `r = dim X - dim Y` and `s = dim Y - dim Z` are natural
> numbers together with the relations `dim X = dim Y + r` and `dim Y = dim Z + s`, and the degree
> `dim X - dim Z` of the composite is `r + s`. Pulling back first along `g` and then along `f`
> lands in degree `(j + s) + r`, so the left-hand side is transported along the equality `hcast`
> of that degree with `j + (r + s)`, exactly as `Stacks.Chow.flatPullback_comp` does.

```lean
theorem flat_comp_and_flatPullback_comp_of_isVariety (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k)) (sZ : Z ⟶ Spec (.of k))
    [IsVariety k sX] [IsVariety k sY] [IsVariety k sZ]
    (f : X ⟶ Y) [Flat f] (g : Y ⟶ Z) [Flat g] (hfbase : f ≫ sY = sX) (hgbase : g ≫ sZ = sY)
    (r s : ℕ)
    (hr : topologicalKrullDim X = topologicalKrullDim Y + (r : WithBot ℕ∞))
    (hs : topologicalKrullDim Y = topologicalKrullDim Z + (s : WithBot ℕ∞))
    (j : ℤ) (hcast : j + (s : ℤ) + (r : ℤ) = j + ((r + s : ℕ) : ℤ))
    (c : CycleGroup (fieldChowSituation k) sZ j) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp k sX sY f hfbase
    letI : LocallyOfFiniteType g := locallyOfFiniteType_of_isVariety_comp k sY sZ g hgbase
    Flat (f ≫ g) ∧
      (hcast ▸ flatPullback (fieldChowSituation k) sX sY f hfbase r
            (relativeDimension_of_flat_of_isVariety k sX sY f hfbase r hr) (j + (s : ℤ))
            (flatPullback (fieldChowSituation k) sY sZ g hgbase s
              (relativeDimension_of_flat_of_isVariety k sY sZ g hgbase s hs) j c) :
          CycleGroup (fieldChowSituation k) sX (j + ((r + s : ℕ) : ℤ))) =
        flatPullback (fieldChowSituation k) sX sZ (f ≫ g)
          (by rw [Category.assoc, hgbase, hfbase]) (r + s)
          (relativeDimension_comp_of_flat_of_isVariety k sX sY sZ f g hfbase hgbase r s hr hs)
          j c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.7, Tag 0AZE](https://stacks.math.columbia.edu/tag/0AZE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
