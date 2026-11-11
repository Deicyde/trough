---
declaration: theorem
origin: cited
lean: CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant
statement: formalized
proof: formalized
---

# Kostant's decomposition

The Clifford algebra of the Killing form, under left multiplication
by the quadratic lift of the adjoint representation, is a direct sum of `2 ^ ((d + l) / 2)` copies
of `L(ρ)`, for `L` of dimension `d` and rank `l`.

```lean
CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant.{u, v}
  {K : Type u} [Field K] [CharZero K] {L : Type v} [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L] {H : LieSubalgebra K L}
  [H.IsCartanSubalgebra] [IsAlgClosed K] (base : (LieAlgebra.IsKilling.rootSystem H).Base) :
  Nonempty
    (CliffordAlgebra (TauCeti.LieAlgebra.killingQuadraticForm K L) ≃ₗ⁅K,L⁆
      DirectSum (Fin (2 ^ ((Module.finrank K L + LieAlgebra.rank K L) / 2))) fun x =>
        TauCeti.irreducibleQuotient base
          (TauCeti.weylVector (LieAlgebra.IsKilling.rootSystem H) base))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The lattice form of Weyl's theorem](../../algebra/part-02/lie/part-01/the-lattice-form-of-weyls-theorem.md)
- [The multiplicity theorem](../../ring-theory/part-01/semisimple/the-multiplicity-theorem.md)
- [The Weyl dimension formula (`TauCeti.finrank_eq_prod_coweightPairing_div`)](../../algebra/part-02/lie/part-02/the-weyl-dimension-formula-tauceti-finrank-eq-pr.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant)
- [Source of `CliffordAlgebra.nonempty_lieModuleEquiv_directSum_irreducibleQuotient_weylVector_kostant` in TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean#L128)
