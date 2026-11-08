---
declaration: theorem
origin: cited
lean: TauCeti.weylGroupCorootRep_cartanEquivDual_symm
statement: formalized
proof: formalized
---

# The Killing duality is Weyl-equivariant

The opposite of a Weyl group element `w`, acting
on `H` through the coroot representation `RootPairing.weylGroupCorootRep`, sends the vector `t_λ`
representing a weight `λ` under the Killing form to `t_{w⁻¹ λ}`.

```lean
TauCeti.weylGroupCorootRep_cartanEquivDual_symm.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [CharZero K]
  [LieModule.IsTriangularizable K (↥H) L] (w : ↥(LieAlgebra.IsKilling.rootSystem H).weylGroup)
  (lam : Module.Dual K ↥H) :
  ((LieAlgebra.IsKilling.rootSystem H).weylGroupCorootRep
        ((LieAlgebra.IsKilling.rootSystem H).weylGroup.equivOp w))
      ((LieAlgebra.IsKilling.cartanEquivDual H).symm lam) =
    (LieAlgebra.IsKilling.cartanEquivDual H).symm (w⁻¹ • lam)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weylGroupCorootRep_cartanEquivDual_symm`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Weights/InvariantForm.html#TauCeti.weylGroupCorootRep_cartanEquivDual_symm).

## Sources

- [Tau Ceti documentation: `TauCeti.weylGroupCorootRep_cartanEquivDual_symm`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Weights/InvariantForm.html#TauCeti.weylGroupCorootRep_cartanEquivDual_symm)
- [Source of `TauCeti.weylGroupCorootRep_cartanEquivDual_symm` in TauCeti/Algebra/Lie/Weights/InvariantForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Weights/InvariantForm.lean#L290)
