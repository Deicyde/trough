---
declaration: theorem
origin: cited
lean: RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset
statement: formalized
proof: formalized
---

# Exact Weyl Jacobian formula

for a base `b` of a finite reduced crystallographic root
pairing on a finite-dimensional space `M` in characteristic zero, up to a nonzero scalar in `K`,
the Jacobian of any finite homogeneous basic invariant system of `Sym(M*)^W` is the product of the
positive coroots `∏ α ∈ posRootsFinset P b, ι (P.coroot' α)`.

```lean
RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset.{u_1, u_2, u_3, u_4, u_5}
  {ι : Type u_1} {K : Type u_2} {M : Type u_3} {N : Type u_4} {κ : Type u_5} [Field K] [CharZero K]
  [AddCommGroup M] [_root_.Module K M] [FiniteDimensional K M] [AddCommGroup N] [_root_.Module K N]
  (P : RootPairing ι K M N) [Finite ι] [P.IsCrystallographic] [P.IsReduced] [Fintype κ]
  [DecidableEq κ] (b : P.Base) (B : Module.Basis κ K (Module.Dual K M))
  {f : κ → ↥P.weylGroupRootRep.dual.symmetricAlgebraInvariants} {d : κ → ℕ}
  (hf : ∀ (k : κ), ↑(f k) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (Module.Dual K M) (d k))
  (hbij : Function.Bijective ⇑(MvPolynomial.aeval f)) :
  ∃ c,
    c ≠ 0 ∧
      (SymmetricAlgebra.jacobian B fun k => ↑(f k)) =
        (algebraMap K (SymmetricAlgebra K (Module.Dual K M))) c *
          ∏ α ∈ TauCeti.posRootsFinset P b, (SymmetricAlgebra.ι K (Module.Dual K M)) (P.coroot' α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The exact Jacobian formula](../finite-reflection-invariants-degrees-and-weyl-ex/the-exact-jacobian-formula.md)
- [Serre's criterion](../../ring-theory/part-01/ideal/serres-criterion.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Weyl/Invariants.html#RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset).

## Sources

- [Tau Ceti documentation: `RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Weyl/Invariants.html#RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset)
- [Source of `RootPairing.exists_jacobian_eq_algebraMap_mul_prod_posRootsFinset` in TauCeti/RepresentationTheory/SymmetricAlgebra/Weyl/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/Weyl/Invariants.lean#L268)
