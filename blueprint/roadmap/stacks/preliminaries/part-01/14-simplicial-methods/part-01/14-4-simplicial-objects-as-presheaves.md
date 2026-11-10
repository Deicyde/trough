---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.existsUnique_hom_app_eq
statement: formalized
proof: formalized
---

# 14.4 Simplicial objects as presheaves

Section 14.4 of the Stacks Project, [Tag 016G](https://stacks.math.columbia.edu/tag/016G). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 016H, an equation

[Tag 016H](https://stacks.math.columbia.edu/tag/016H) in the Stacks Project.

**`CategoryTheory.SimplicialObject.existsUnique_hom_app_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Basic.lean#L217). The attribute's comment: “the common hom-set is the set of degreewise families commuting with the faces and the degeneracies”.

> **Stacks 016H**.
> Let `U`, `U'` be simplicial objects of a category `C`, and let `d n : U_n ⟶ U'_n` be a family of
> morphisms commuting with the face maps `δ i` and with the degeneracy maps `σ i`. Then there is a
> unique morphism of simplicial objects `f : U ⟶ U'` — equivalently, by definition, a unique morphism
> `U ⟶ U'` of `C`-valued presheaves on `Δ` — whose component in degree `n` is `d n`.

```lean
public theorem existsUnique_hom_app_eq {U U' : SimplicialObject C}
    (d : ∀ n : ℕ, U.obj (op ⦋n⦌) ⟶ U'.obj (op ⦋n⦌))
    (hδ : ∀ (n : ℕ) (i : Fin (n + 2)), U.δ i ≫ d n = d (n + 1) ≫ U'.δ i)
    (hσ : ∀ (n : ℕ) (i : Fin (n + 1)), U.σ i ≫ d (n + 1) = d n ≫ U'.σ i) :
    ∃! f : U ⟶ U', ∀ n : ℕ, f.app (op ⦋n⦌) = d n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.4, Tag 016G](https://stacks.math.columbia.edu/tag/016G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
