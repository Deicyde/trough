---
declaration: section
origin: cited
lean: CategoryTheory.Sites.Sheaf.Action.exists_equivalence_sheaf
statement: formalized
proof: formalized
---

# 7.9 The example of G-sets

Section 7.9 of the Stacks Project, [Tag 00VZ](https://stacks.math.columbia.edu/tag/00VZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00W0, a proposition

[Tag 00W0](https://stacks.math.columbia.edu/tag/00W0) in the Stacks Project.

**`CategoryTheory.Sites.Sheaf.Action.exists_equivalence_sheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheaf/ExampleOfGSets.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheaf/ExampleOfGSets.lean#L597). References: SGA 4 IV (2.3), “special case”; SGA 4 IV (9.1.12), “Clause e)”.

> **Stacks 00W0**. Sheaves on `𝒯_G` are `G`-sets: let `G` be a monoid and let `J` be a
> Grothendieck topology on a full subcategory `ι : T ⥤ Action (Type u) G` of the category of `G`-sets
> whose essential image contains the left regular `G`-set `{}_G G` and whose covering sieves are
> exactly the jointly surjective ones. Then `G`-sets are equivalent to the sheaves of sets on
> `(T, J)` by an equivalence whose forward functor sends a `G`-set `S` to the sheaf
> `U ↦ Hom_G(ι U, S)`; the quasi-inverse is `F ↦ F({}_G G)`. The source states this for a group.

```lean
public theorem Action.exists_equivalence_sheaf {T : Type w} [Category.{v} T] {G : Type u}
    [Monoid G] (ι : T ⥤ Action (Type u) G) [ι.Full] [ι.Faithful]
    (hreg : ι.essImage (Action.leftRegular G)) (J : GrothendieckTopology T)
    (hJ :
      ∀ (U : T) (S : Sieve U),
        S ∈ J U ↔
          ∀ a : Action.leftRegular G ⟶ ι.obj U,
            ∃ (V : T) (f : V ⟶ U) (b : Action.leftRegular G ⟶ ι.obj V),
              S.arrows f ∧ b ≫ ι.map f = a) :
    ∃ e : Action (Type u) G ≌ Sheaf J (Type u),
      e.functor ⋙ sheafToPresheaf J (Type u) =
        yoneda ⋙ (Functor.whiskeringLeft Tᵒᵖ (Action (Type u) G)ᵒᵖ (Type u)).obj ι.op
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.9, Tag 00VZ](https://stacks.math.columbia.edu/tag/00VZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
