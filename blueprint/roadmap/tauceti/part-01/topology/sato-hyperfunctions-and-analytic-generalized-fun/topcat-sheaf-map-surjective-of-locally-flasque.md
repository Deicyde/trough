---
declaration: theorem
origin: cited
lean: TopCat.Sheaf.map_surjective_of_locally_flasque
statement: formalized
proof: formalized
---

# TopCat.Sheaf.map_surjective_of_locally_flasque

If every restriction map of a sheaf inside some neighbourhood of each point is surjective, then
every restriction map is surjective.

```lean
TopCat.Sheaf.map_surjective_of_locally_flasque.{u, v_1, u_1, u_2, u_3} {X : TopCat} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] {FC : C → C → Type u_2} {CC : C → Type u_3}
  [(X Y : C) → FunLike (FC X Y) (CC X) (CC Y)] [CategoryTheory.ConcreteCategory C FC]
  [CategoryTheory.Limits.PreservesLimitsOfSize.{u, u, v_1, u_3, u_1, u_3 + 1}
      (CategoryTheory.forget C)]
  (F : TopCat.Sheaf C X)
  (h :
    ∀ (x : ↑X),
      ∃ W,
        x ∈ W ∧
          ∀ ⦃U V : TopologicalSpace.Opens ↑X⦄ (hUV : U ≤ V),
            V ≤ W →
              Function.Surjective
                ⇑(CategoryTheory.ConcreteCategory.hom (F.obj.map (CategoryTheory.homOfLE hUV).op)))
  {U V : TopologicalSpace.Opens ↑X} (hUV : U ≤ V) :
  Function.Surjective
    ⇑(CategoryTheory.ConcreteCategory.hom (F.obj.map (CategoryTheory.homOfLE hUV).op))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.Sheaf.map_surjective_of_locally_flasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Flasque/Locality.html#TopCat.Sheaf.map_surjective_of_locally_flasque).

## Sources

- [Tau Ceti documentation: `TopCat.Sheaf.map_surjective_of_locally_flasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Flasque/Locality.html#TopCat.Sheaf.map_surjective_of_locally_flasque)
- [Source of `TopCat.Sheaf.map_surjective_of_locally_flasque` in TauCeti/Topology/Sheaves/Flasque/Locality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Flasque/Locality.lean#L141)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Hyperfunctions/STATUS.md)
