---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.Newform.L_eulerProduct
statement: formalized
proof: formalized
---

# HeckeRing.GL2.Newform.L_eulerProduct

Finite Euler products converge to Mathlib's `ModularForm.L` for a newform.

```lean
HeckeRing.GL2.Newform.L_eulerProduct {N : ℕ} [NeZero N] {k : ℤ} (f : HeckeRing.GL2.Newform N k)
  (hk : 0 < k) {s : ℂ} (hs : ↑k / 2 + 1 < s.re) :
  Filter.Tendsto
    (fun n =>
      ∏ p ∈ n.primesBelow,
        (1 - (PowerSeries.coeff p) (UpperHalfPlane.qExpansion 1 ⇑f.toCuspForm) * ↑p ^ (-s) +
            f.dirichletLift ↑p * ↑p ^ (k - 1) * ↑p ^ (-2 * s))⁻¹)
    Filter.atTop (nhds (ModularForm.L hk f.toCuspForm s))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A newform is an eigenvector of `U_p` at every prime `p` dividing the level, with eigenvalue `a_p(f)`](a-newform-is-an-eigenvector-of-u-p-at-every-prim.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../../part-02/hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.L_eulerProduct`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LFunction/EulerProduct.html#HeckeRing.GL2.Newform.L_eulerProduct).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.L_eulerProduct`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LFunction/EulerProduct.html#HeckeRing.GL2.Newform.L_eulerProduct)
- [Source of `HeckeRing.GL2.Newform.L_eulerProduct` in TauCeti/NumberTheory/ModularForms/LFunction/EulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/LFunction/EulerProduct.lean#L243)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
