---
declaration: theorem
origin: cited
lean: HeckeRing.GLn.range_evalHom
statement: formalized
proof: formalized
---

# The generators generate `R_p` (Shimura, Theorem 3.20)

for `p` prime, the polynomials in
the generators `heckeGen k` are exactly the elements of the `p`-local Hecke ring.

```lean
HeckeRing.GLn.range_evalHom (n : ℕ) {p : ℕ} (hp : Nat.Prime p) :
  (HeckeRing.GLn.evalHom n p).range = HeckeRing.GLn.pLocalSubring n p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GLn.range_evalHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.range_evalHom).

## Sources

- [Tau Ceti documentation: `HeckeRing.GLn.range_evalHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.range_evalHom)
- [Source of `HeckeRing.GLn.range_evalHom` in TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean#L237)
