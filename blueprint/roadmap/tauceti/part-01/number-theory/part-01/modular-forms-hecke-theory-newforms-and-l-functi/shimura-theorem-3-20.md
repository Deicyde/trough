---
declaration: def
origin: cited
lean: HeckeRing.GLn.polynomialRingEquiv
statement: formalized
---

# Shimura, Theorem 3.20

for `p` prime, the `p`-local Hecke ring `R_p` of `GL_n` is the
polynomial ring `ℤ[X₁, …, Xₙ]` on the diagonal prime cosets
`heckeGen k = T(1, …, 1, p, …, p)`, with `k + 1` entries equal to `p`.

```lean
HeckeRing.GLn.polynomialRingEquiv (n : ℕ) {p : ℕ} (hp : Nat.Prime p) :
  MvPolynomial (Fin n) ℤ ≃+* ↥(HeckeRing.GLn.pLocalSubring n p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The generators generate `R_p` (Shimura, Theorem 3.20)](the-generators-generate-r-p-shimura-theorem-3-20.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GLn.polynomialRingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.polynomialRingEquiv).

## Sources

- [Tau Ceti documentation: `HeckeRing.GLn.polynomialRingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.html#HeckeRing.GLn.polynomialRingEquiv)
- [Source of `HeckeRing.GLn.polynomialRingEquiv` in TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/HeckeRing/GLn/PolynomialRing/Presentation.lean#L257)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularForms/STATUS.md)
