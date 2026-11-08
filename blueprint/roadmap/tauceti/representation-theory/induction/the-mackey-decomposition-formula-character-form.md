---
declaration: theorem
origin: cited
lean: TauCeti.character_resFDRep_indFDRep_mackey, Subgroup.indClassFun_mackey, Subgroup.comap_subtype_indClassFunction_mackey
statement: formalized
proof: formalized
---

# The Mackey decomposition formula, character form

For a finite-dimensional representation
`A` of a finite-index subgroup `H` and an element `x` of a subgroup `K`, the character of
`Res_K (Ind_H^G A)` at `x` is the sum, over the double cosets `K \ G / H`, of the characters of
the Mackey summands.

The character of `Ind_H^G A` at `x : K`, read on `G`, is
the same number: `FDRep.character_actionRes` is a `simp` lemma rewriting the left-hand side into
it.

```lean
TauCeti.character_resFDRep_indFDRep_mackey.{u} {k G : Type u} [Field k] [Group G] {H K : Subgroup G}
  [H.FiniteIndex] (A : FDRep k ↥H) (x : ↥K) :
  (K.resFDRep (TauCeti.indFDRep A)).character x =
    ∑ D, (TauCeti.mackeySummand (Quotient.out D) A).character x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.character_resFDRep_indFDRep_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#TauCeti.character_resFDRep_indFDRep_mackey).

## Other forms

**The Mackey decomposition formula for class functions.** Formalized in Tau Ceti as [`Subgroup.indClassFun_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#Subgroup.indClassFun_mackey).

```lean
Subgroup.indClassFun_mackey.{u_1, u_2} {k : Type u_1} [Semiring k] {G : Type u_2} [Group G]
  (H : Subgroup G) {K : Subgroup G} [H.FiniteIndex] {f : ↥H → k}
  (hf : f ∈ TauCeti.ClassFunction k ↥H) (x : ↥K) :
  H.indClassFun f ↑x =
    ∑ D,
      ((TauCeti.mackeySubgroup (Quotient.out D) H K).subgroupOf K).indClassFun
        (TauCeti.mackeyClassFun (Quotient.out D) H K f) x
```

**The Mackey decomposition of a restricted induced class function.** Formalized in Tau Ceti as [`Subgroup.comap_subtype_indClassFunction_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#Subgroup.comap_subtype_indClassFunction_mackey).

```lean
Subgroup.comap_subtype_indClassFunction_mackey.{u_1, u_2} {k : Type u_1} [Semiring k] {G : Type u_2}
  [Group G] (K : Subgroup G) {H : Subgroup G} [H.FiniteIndex] (f : ↥(TauCeti.ClassFunction k ↥H)) :
  (TauCeti.ClassFunction.comap K.subtype) (H.indClassFunction f) =
    ∑ D,
      ((TauCeti.mackeySubgroup (Quotient.out D) H K).subgroupOf K).indClassFunction
        (TauCeti.mackeyClassFunction (Quotient.out D) H K f)
```

## Sources

- [Tau Ceti documentation: `TauCeti.character_resFDRep_indFDRep_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Basic.html#TauCeti.character_resFDRep_indFDRep_mackey)
- [Source of `TauCeti.character_resFDRep_indFDRep_mackey` in TauCeti/RepresentationTheory/Induction/Mackey/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Mackey/Basic.lean#L501)
