---
declaration: theorem
origin: cited
lean: Subgroup.comap_subtype_indClassFunction_mackey
statement: formalized
proof: formalized
---

# The Mackey decomposition of a restricted induced class function

Restricting to `K` a
class function induced from `H` gives the sum, over the double cosets `K \ G / H`, of the class
functions induced to `K` from the Mackey subgroups.

This is `Subgroup.indClassFun_mackey` rewritten as an identity of bundled class functions, which is
the form the character pairing consumes.

```lean
Subgroup.comap_subtype_indClassFunction_mackey.{u_1, u_2} {k : Type u_1} [Semiring k] {G : Type u_2}
  [Group G] (K : Subgroup G) {H : Subgroup G} [H.FiniteIndex] (f : ↥(TauCeti.ClassFunction k ↥H)) :
  (TauCeti.ClassFunction.comap K.subtype) (H.indClassFunction f) =
    ∑ D,
      ((TauCeti.mackeySubgroup (Quotient.out D) H K).subgroupOf K).indClassFunction
        (TauCeti.mackeyClassFunction (Quotient.out D) H K f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mackey decomposition formula, character form](the-mackey-decomposition-formula-character-form.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.comap_subtype_indClassFunction_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#Subgroup.comap_subtype_indClassFunction_mackey).

## Sources

- [Tau Ceti documentation: `Subgroup.comap_subtype_indClassFunction_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#Subgroup.comap_subtype_indClassFunction_mackey)
- [Source of `Subgroup.comap_subtype_indClassFunction_mackey` in TauCeti/RepresentationTheory/Induction/Mackey/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Mackey/Basic.lean#L423)
