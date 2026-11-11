---
declaration: theorem
origin: cited
lean: TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom
statement: formalized
proof: formalized
---

# TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom

The uniform integrality set in `continuous_rationalDiagonal` cannot be dropped. Take
discrete groups with trivial reference subgroups, infinitely many of them nontrivial, and for `Γ`
the range of the coercion from the restricted product to the full product, that is, the finitely
supported elements, with the topology induced from the full product. The coordinate maps are
continuous and every element of `Γ` is eventually integral (it is the coercion of an element of
the restricted product), but the diagonal is not continuous:
it would make the restricted-product topology the one induced from the full product,
contradicting `not_isInducing_coe_bot`.

```lean
TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom.{u, v} {ι : Type u}
  {G : ι → Type v} [(i : ι) → Group (G i)] [(i : ι) → TopologicalSpace (G i)]
  [∀ (i : ι), DiscreteTopology (G i)] (hG : {i | Nontrivial (G i)}.Infinite) :
  (∀ (i : ι),
      Continuous ⇑((Pi.evalMonoidHom G i).comp RestrictedProduct.coeMonoidHom.range.subtype)) ∧
    ¬Continuous
        ⇑(TauCeti.rationalDiagonal
            (fun i => (Pi.evalMonoidHom G i).comp RestrictedProduct.coeMonoidHom.range.subtype)
            (fun x => ⊥) ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom)
- [Source of `TauCeti.continuous_eval_and_not_continuous_rationalDiagonal_range_coeMonoidHom` in TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean#L188)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
