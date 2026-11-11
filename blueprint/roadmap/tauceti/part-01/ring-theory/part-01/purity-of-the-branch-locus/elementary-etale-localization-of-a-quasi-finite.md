---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated
statement: formalized
proof: formalized
---

# Elementary étale localization of a quasi-finite point (Stacks, Lemma 37.41.1 (02LK))

Let `f : X ⟶ S` be locally of finite type and quasi-finite at `x` (so `x` is isolated in its
fibre). Then there are an étale `φ : U ⟶ S` and `u : U` with `φ u = f x` and `κ(f x) ≅ κ(u)`, and
an open `V` of `X ×[S] U`, finite over `U`, containing a point `v` over `x` and `u` with
`κ(x) ≅ κ(v)`, which is the only point of `V` over `u`.

The persistence clause of 02LK, that the conclusion survives further elementary étale
neighbourhoods of `(U, u)`, is supplied by `Scheme.Hom.exists_finite_open_baseChange`.

```lean
AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated.{u}
  {X S : AlgebraicGeometry.Scheme} (f : X ⟶ S) [AlgebraicGeometry.LocallyOfFiniteType f] {x : ↥X}
  (hx : AlgebraicGeometry.Scheme.Hom.QuasiFiniteAt f x) :
  ∃ U φ u,
    AlgebraicGeometry.Etale φ ∧
      φ u = f x ∧
        CategoryTheory.IsIso (AlgebraicGeometry.Scheme.Hom.residueFieldMap φ u) ∧
          ∃ V v,
            AlgebraicGeometry.IsFinite
                (CategoryTheory.CategoryStruct.comp V.ι (CategoryTheory.Limits.pullback.snd f φ)) ∧
              (CategoryTheory.Limits.pullback.fst f φ) ↑v = x ∧
                (CategoryTheory.Limits.pullback.snd f φ) ↑v = u ∧
                  CategoryTheory.IsIso
                      (AlgebraicGeometry.Scheme.Hom.residueFieldMap
                        (CategoryTheory.Limits.pullback.fst f φ) ↑v) ∧
                    ∀ (w : ↥V), (CategoryTheory.Limits.pullback.snd f φ) ↑w = u → w = v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/ElementaryEtale/Basic.html#AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/ElementaryEtale/Basic.html#AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated)
- [Source of `AlgebraicGeometry.Scheme.Hom.exists_elementaryEtale_finite_of_isolated` in TauCeti/AlgebraicGeometry/Morphisms/ElementaryEtale/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Morphisms/ElementaryEtale/Basic.lean#L61)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
