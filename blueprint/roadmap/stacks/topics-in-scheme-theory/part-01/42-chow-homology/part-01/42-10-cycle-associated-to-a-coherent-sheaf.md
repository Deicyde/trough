---
declaration: section
origin: cited
lean: Stacks.Chow.locallyFinite_irreducibleComponents_supp, Stacks.Chow.isFiniteLength_stalk_of_isGenericPoint_component_supp, Stacks.Chow.isGenericPoint_component_supp_of_relativeDimension_eq, Stacks.Chow.sheafMultiplicity, Stacks.Chow.cycleAssociatedToCoherentSheaf, Stacks.Chow.exists_cycleAssociatedToCoherentSheaf, Stacks.Chow.cycleAssociatedToClosedSubscheme_eq_cycleAssociatedToCoherentSheaf, Stacks.Chow.cycleAssociatedToCoherentSheaf_add
statement: formalized
proof: formalized
---

# 42.10 Cycle associated to a coherent sheaf

Section 42.10 of the Stacks Project, [Tag 02QV](https://stacks.math.columbia.edu/tag/02QV). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02QW, a lemma

[Tag 02QW](https://stacks.math.columbia.edu/tag/02QW) in the Stacks Project.

**`Stacks.Chow.locallyFinite_irreducibleComponents_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean#L96). The attribute's comment: “part (1): local finiteness”.

> **Stacks 02QW (1).** The irreducible components of the support of a coherent sheaf on a
> locally Noetherian scheme form a locally finite family.

```lean
theorem locallyFinite_irreducibleComponents_supp [IsLocallyNoetherian X] (F : X.Modules)
    [F.IsCoherent] :
    LocallyFinite fun Z : irreducibleComponents (SheafOfModules.supp F : Set X) ↦
      (Subtype.val '' Z.1 : Set X)
```

**`Stacks.Chow.isFiniteLength_stalk_of_isGenericPoint_component_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean#L186). The attribute's comment: “part (2): finite stalk length”. References: EGA IV (4.7.7), “partial”; SGA 6 X (1.1.2), “partial”.

> **Stacks 02QW (2).** At the generic point of an irreducible component of its support, the
> stalk of a coherent sheaf on a locally Noetherian scheme has finite length over the local ring
> of the scheme.

```lean
theorem isFiniteLength_stalk_of_isGenericPoint_component_supp [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent]
    (Z : irreducibleComponents (SheafOfModules.supp F : Set X)) (ξ : X)
    (hξ : IsGenericPoint ξ (Subtype.val '' Z.1 : Set X)) :
    IsFiniteLength (X.presheaf.stalk ξ) (F.presheaf.stalk ξ)
```

**`Stacks.Chow.isGenericPoint_component_supp_of_relativeDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Support.lean#L234). The attribute's comment: “part (3): maximal-dimension generic points”.

> **Stacks 02QW (3).** If the support of a coherent sheaf has delta-dimension at most `k`, then
> a point of the support of delta-dimension `k` is the generic point of an irreducible component of
> the support.

```lean
theorem isGenericPoint_component_supp_of_relativeDimension_eq (C : ChowSituation.{u})
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (F : X.Modules) [F.IsCoherent] (k : ℤ) (ξ : X)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ f) ≤ (k : EInt))
    (hξ : ξ ∈ SheafOfModules.supp F)
    (hδ : relativeDimension C.dimensionFunction f ξ = k) :
    ∃ Z : irreducibleComponents (SheafOfModules.supp F : Set X),
      IsGenericPoint ξ (Subtype.val '' Z.1 : Set X)
```

## Tag 02QX, a definition

[Tag 02QX](https://stacks.math.columbia.edu/tag/02QX) in the Stacks Project.

**`Stacks.Chow.sheafMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean#L69). The attribute's comment: “part (1): multiplicity”.

> **Stacks 02QX.** The length of the stalk of a sheaf of modules at a point, as an integer. At
> a generic point of an irreducible component of the support of a coherent sheaf this length is
> finite and is the multiplicity of that component in the sheaf.

```lean
def sheafMultiplicity (F : X.Modules) (x : X) : ℤ
```

**`Stacks.Chow.cycleAssociatedToCoherentSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean#L156). The attribute's comment: “part (2): associated cycle”.

> **Stacks 02QX.** The `k`-cycle `[F]_k` associated to a coherent sheaf whose support has
> delta-dimension at most `k`: the coefficient at a point of the support whose closure has
> delta-dimension `k` is the length of the stalk there.

```lean
def cycleAssociatedToCoherentSheaf (C : ChowSituation.{u}) (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ f) ≤ (k : EInt)) :
    CycleGroup C f k
```

**`Stacks.Chow.exists_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Basic.lean#L177). The attribute's comment: “part (2): existence of the associated cycle”.

> **Stacks 02QX.** The coefficient formula for the cycle of a coherent sheaf does define a
> `k`-cycle when the support of the sheaf has delta-dimension at most `k`.

```lean
theorem exists_cycleAssociatedToCoherentSheaf (C : ChowSituation.{u}) (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ f) ≤ (k : EInt)) :
    ∃ c : CycleGroup C f k, ∀ x : X, (c : AlgebraicCycle X ℤ) x =
      open Classical in
      if x ∈ SheafOfModules.supp F ∧ relativeDimension C.dimensionFunction f x = k then
        sheafMultiplicity F x
      else 0
```

## Tag 02QY, a lemma

[Tag 02QY](https://stacks.math.columbia.edu/tag/02QY) in the Stacks Project.

**`Stacks.Chow.cycleAssociatedToClosedSubscheme_eq_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/ClosedSubscheme.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/ClosedSubscheme.lean#L280).

> **Stacks 02QY.** For a closed subscheme `i : Z ⟶ X` of delta-dimension at most `k`, the
> `k`-cycle of `Z` is the `k`-cycle of its structure sheaf: `[Z]_k = [𝒪_Z]_k`.

```lean
theorem cycleAssociatedToClosedSubscheme_eq_cycleAssociatedToCoherentSheaf
    (C : ChowSituation.{u}) {X Z : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (i : Z ⟶ X) [IsClosedImmersion i] (k : ℤ)
    (hZ : schemeDeltaDimension C (i ≫ f) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    cycleAssociatedToClosedSubscheme C f i k =
      cycleAssociatedToCoherentSheaf C f ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z)) k
        (schemeDeltaDimension_reducedSupport_pushforwardStructureSheaf_le C f i hZ)
```

## Tag 02QZ, a lemma

[Tag 02QZ](https://stacks.math.columbia.edu/tag/02QZ) in the Stacks Project.

**`Stacks.Chow.cycleAssociatedToCoherentSheaf_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Additivity.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/Additivity.lean#L52).

> **Stacks 02QZ.** The cycle of a coherent sheaf is additive along a short exact sequence of
> coherent sheaves whose supports all have delta-dimension at most `k`.

```lean
theorem cycleAssociatedToCoherentSheaf_add (C : ChowSituation.{u}) (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (E : ShortComplex X.Modules) (hE : E.ShortExact)
    [E.X₁.IsCoherent] [E.X₂.IsCoherent] [E.X₃.IsCoherent] (k : ℤ)
    (hk₁ : schemeDeltaDimension C ((reducedSupport E.X₁).subschemeι ≫ f) ≤ (k : EInt))
    (hk₂ : schemeDeltaDimension C ((reducedSupport E.X₂).subschemeι ≫ f) ≤ (k : EInt))
    (hk₃ : schemeDeltaDimension C ((reducedSupport E.X₃).subschemeι ≫ f) ≤ (k : EInt)) :
    cycleAssociatedToCoherentSheaf C f E.X₂ k hk₂ =
      cycleAssociatedToCoherentSheaf C f E.X₁ k hk₁ +
        cycleAssociatedToCoherentSheaf C f E.X₃ k hk₃
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.10, Tag 02QV](https://stacks.math.columbia.edu/tag/02QV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
