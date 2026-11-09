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
HeckeRing.GLn.range_evalHom (n : ℕ) [NeZero n] {p : ℕ} (hp : Nat.Prime p) :
  (HeckeRing.GLn.evalHom n p).range = HeckeRing.GLn.pLocalSubring n p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](shimuras-commutativity-criterion-proposition-3-8.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GLn.range_evalHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.range_evalHom).

## Sources

- [Tau Ceti documentation: `HeckeRing.GLn.range_evalHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.range_evalHom)
- [Source of `HeckeRing.GLn.range_evalHom` in TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean#L240)
