---
declaration: theorem
origin: cited
lean: ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq
statement: formalized
proof: formalized
---

# The Frattini criterion for a kernel

If every continuous `𝔽_p`-valued character of `G`
factors through a continuous homomorphism `φ : G → H`, then the kernel of `φ` lies in the pro-`p`
Frattini subgroup of `G`.

```lean
ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq.{u, u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [ContinuousMul G] {H : Type u_1}
  [Group H] [TopologicalSpace H] (φ : G →ₜ* H)
  (h : ∀ (ψ : G →ₜ* Multiplicative (ZMod p)), ∃ χ, χ.comp φ = ψ) : φ.ker ≤ TauCeti.proPFrattini p G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/ContinuousDual.html#ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq).

## Sources

- [Tau Ceti documentation: `ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/ContinuousDual.html#ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq)
- [Source of `ContinuousMonoidHom.ker_le_proPFrattini_of_forall_exists_comp_eq` in TauCeti/Topology/Algebra/Group/Profinite/ProP/ContinuousDual.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/ContinuousDual.lean#L109)
