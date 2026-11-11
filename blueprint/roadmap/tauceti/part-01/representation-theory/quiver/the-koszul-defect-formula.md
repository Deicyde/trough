---
declaration: theorem
origin: cited
lean: TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner
statement: formalized
proof: formalized
---

# The Koszul defect formula

For vertices `i` and `v` and every degree `m`,

```text
dim e_v Π_{m+2} e_i + dim e_v Π_m e_i = ∑_w #(w ⟶ v) dim e_w Π_{m+1} e_i + dim K_m(i, v),
```

the sum running over the arrows of the doubled quiver into `v`, where `K_m(i, v)` is the space of
`y ∈ e_v Π_m e_i` killed by the reverse `b*` of every arrow `b` into `v`, the kernel of the left
map of the Koszul complex of `S_v`.

```lean
TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner.{u, v, w} (k : Type w)
  (Q : Type u) [Field k] [Quiver Q] [Fintype Q] [(i j : Q) → Fintype (i ⟶ j)] (m : ℕ)
  (i : Quiver.Symmetrify Q) (v : Q) :
  Module.finrank k ↥(TauCeti.preprojectiveCorner k Q (m + 2) i (Quiver.Symmetrify.of.obj v)) +
      Module.finrank k ↥(TauCeti.preprojectiveCorner k Q m i (Quiver.Symmetrify.of.obj v)) =
    ∑ w,
        Fintype.card (w ⟶ Quiver.Symmetrify.of.obj v) *
          Module.finrank k ↥(TauCeti.preprojectiveCorner k Q (m + 1) i w) +
      Module.finrank k
        ↥(TauCeti.preprojectiveCorner k Q m i (Quiver.Symmetrify.of.obj v) ⊓
            ⨅ w,
              ⨅ b,
                (LinearMap.mulLeft k
                    ((TauCeti.preprojectiveMk k Q)
                      (TauCeti.PathAlgebra.ofArrow (Quiver.reverse b)))).ker)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/Basic.html#TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/Basic.html#TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner)
- [Source of `TauCeti.finrank_preprojectiveCorner_add_two_add_finrank_preprojectiveCorner` in TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/Basic.lean#L497)
