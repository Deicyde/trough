---
declaration: theorem
origin: cited
lean: TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ
statement: formalized
proof: formalized
---

# Indices of the congruence filtration of a smooth group

Let `𝒢 = Spec H` be an affine group
over a complete discrete valuation ring `O` with maximal ideal `m` and residue field `κ`, with `H`
formally smooth and of finite type over `O`, and let `d` be the rank of the free `O`-module
`ker ε / (ker ε)²`. For `n ≥ 1`, the quotient `𝒢(O)_n / 𝒢(O)_{n+1}` of successive congruence
subgroups has `|κ| ^ d` elements. When `κ` is infinite and `d ≠ 0`, both sides are `0`.

```lean
TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ.{u_4, u_5} {O : Type u_4}
  [CommRing O] [IsDomain O] [IsDiscreteValuationRing O] {H : Type u_5} [CommRing H]
  [HopfAlgebra O H] [IsAdicComplete (IsLocalRing.maximalIdeal O) O] [Algebra.FormallySmooth O H]
  [Algebra.FiniteType O H] {n : ℕ} (hn : n ≠ 0) :
  Nat.card
      (↥(TauCeti.HopfAlgebra.congruenceSubgroup O H (IsLocalRing.maximalIdeal O ^ n)) ⧸
        (TauCeti.HopfAlgebra.congruenceSubgroup O H
              (IsLocalRing.maximalIdeal O ^ (n + 1))).subgroupOf
          (TauCeti.HopfAlgebra.congruenceSubgroup O H (IsLocalRing.maximalIdeal O ^ n))) =
    Nat.card (IsLocalRing.ResidueField O) ^ Module.finrank O (TauCeti.Bialgebra.CotangentSpace O H)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Quotient.html#TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Quotient.html#TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ)
- [Source of `TauCeti.HopfAlgebra.natCard_quotient_congruenceSubgroup_pow_succ` in TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/CongruenceSubgroup/Quotient.lean#L285)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
