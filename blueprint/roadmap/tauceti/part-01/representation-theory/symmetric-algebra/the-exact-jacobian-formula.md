---
declaration: theorem
origin: cited
lean: Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one
statement: formalized
proof: formalized
---

# The exact Jacobian formula

For homogeneous basic invariants of a faithful finite
linear action in characteristic zero, the Jacobian is a nonzero scalar times the product
over distinct reflecting hyperplanes, with exponent the pointwise stabilizer order minus
one. Defining forms and the basis of `V*` affect only the nonzero scalar.

```lean
Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one.{u_1, u_2, u_3, u_4}
  {K : Type u_1} {G : Type u_2} {V : Type u_3} [Field K] [CharZero K] [Group G] [Finite G]
  [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] (ρ : Representation K G V)
  {n : Type u_4} [Fintype n] [DecidableEq n] (hρ : Function.Injective ⇑ρ)
  (b : Module.Basis n K (Module.Dual K V)) (ℓ : ↥ρ.reflectingHyperplanes → Module.Dual K V)
  (hker : ∀ (H : ↥ρ.reflectingHyperplanes), LinearMap.ker (ℓ H) = ↑H)
  {f : n → ↥ρ.dual.symmetricAlgebraInvariants} {d : n → ℕ}
  (hf : ∀ (i : n), ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (Module.Dual K V) (d i))
  (hbij : Function.Bijective ⇑(MvPolynomial.aeval f)) :
  ∃ c,
    c ≠ 0 ∧
      (SymmetricAlgebra.jacobian b fun i => ↑(f i)) =
        (algebraMap K (SymmetricAlgebra K (Module.Dual K V))) c *
          ∏ H,
            (SymmetricAlgebra.ι K (Module.Dual K V)) (ℓ H) ^
              (Nat.card
                  ↥(Ideal.inertia G (Ideal.span {(SymmetricAlgebra.ι K (Module.Dual K V)) (ℓ H)})) -
                1)
```

## Depends on

- [Representation.symmetricAlgebraInvariants](../finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)

## Proof depends on

- [The Jacobian criterion](../../linear-algebra/other-results/the-jacobian-criterion.md)
- [Molien's formula](../finite-reflection-invariants-degrees-and-weyl-ex/moliens-formula.md)
- [Serre's criterion](../../ring-theory/part-01/ideal/serres-criterion.md)

## Lean

Formalized in Tau Ceti as [`Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Hyperplane/Jacobian.html#Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one).

## Sources

- [Tau Ceti documentation: `Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Hyperplane/Jacobian.html#Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one)
- [Source of `Representation.exists_jacobian_eq_algebraMap_mul_prod_dual_inertia_sub_one` in TauCeti/RepresentationTheory/SymmetricAlgebra/Hyperplane/Jacobian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/Hyperplane/Jacobian.lean#L50)
